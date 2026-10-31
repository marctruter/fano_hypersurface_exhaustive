'Exhaustive search for Fano 4-fold hypersurfaces with terminal singularities'

#The file is seperated into the following parts:
#0. Setup: Define global constants, and load packages
#1. Terminal: Code to determine whether a point associated to a hypersurface is terminal or not
#2. Exhaustive: Code performing the exhaustive search, run in parallel

###################################################################################################
#0. Setup 
###################################################################################################

#Constants
dim_X = 4 #dimension of hypersurface
alpha_X = 1 #adjunction number of hypersurface

import math
import numpy as np
import itertools as it

###################################################################################################
#1. Terminal 
###################################################################################################

#terminal_point(point): returns True if the point corresponds to a terminal hypersurface, False otherwise 
def terminal_point(point):
    degree = sum(point) - alpha_X
    if wellformedness(degree, point):
        if terminal_sufficient_condition(point):
            sings = terminal_singularities(degree, point)
            if sings !=False:
                return True
        return False
    
#wellformedness(degree, point): returns True if the point is well-formed, False otherwise (Fletcher criterion)
def wellformedness(degree, point): #Fletcher criterion
    #(1)
    for i,j in it.combinations(range(len(point)),2):
        if degree % math.gcd(*(point[k] for k in range(len(point)) if k != i if k != j)) != 0:
            return False
    #(2)
    for i in range(len(point)):
        if math.gcd(*(point[k] for k in range(len(point)) if k != i)) != 1:
            return False
    return True

#terminal_sufficient_condition(point): returns True if the point satisfies the sufficient condition for terminality, False otherwise
def terminal_sufficient_condition(point):
    d = sum(point) - alpha_X
    for a in point:
        if d % a != 0:
            for k in range(1, a):
                discrep_estimate = sum((k * w) % a for w in point) - (k* d) % a - a
                if discrep_estimate <= 0:
                    return False
    return True
    
#terminal_singularities(degree, point): returns list of singularities if all singularities are terminal, False otherwise
def terminal_singularities(degree, point):
    sings = []
    point_strata = strata(point)
    for stratum in point_strata:
        h_I, stratum_weights, stratum_indices, k = stratum
        mu_I = mu(degree, stratum_weights)
        if mu_I == 1:
            continue
        elif mu_I >= 2:
            dim_qs = k - 1
            qsness = "qs"
            if h_I == 1:
                continue 
            else: #h_I >= 2
                sing_type = "quotient"
                t = tangent_index(degree, point, stratum_weights, stratum_indices)
                stratum_indices_without_t = tuple(i for i in stratum_indices if i != t)
                sing_weights = tuple(point[i] % h_I for i in range(len(point)) if i != stratum_indices_without_t[0] if i != t)
                sing = (h_I, sing_weights, point[t], stratum_weights, dim_qs, sing_type, qsness)
                if terminal(degree, point, sing, k):
                    sings.append(sing)
                else:
                    return False
        else: #mu_I == 0
            dim_qs = k
            rho_I = rho(degree, point, stratum_weights)
            stratum_indices_complement = tuple(i for i in range(len(point)) if i not in stratum_indices)
            nonqs_existence  = rank_test(degree, point, stratum_weights, stratum_indices)
            if rho_I > k or nonqs_existence == False:
                qsness = "qs"
                if h_I == 1:
                    continue 
                else: #h_I >= 2
                    sing_type = "quotient"
                    t = tangent_index(degree, point, stratum_weights, stratum_indices_complement)
                    sing_weights = tuple(point[i] % h_I for i in range(len(point)) if i != stratum_indices[0] if i != t)
                    sing = (h_I, sing_weights, point[t], stratum_weights, dim_qs, sing_type, qsness)
                    if terminal(degree, point, sing, k):
                        sings.append(sing)
                    else:
                        return False
            else: #rho_I<=k and nonqs_existence == True
                if rho_I == 0:
                    qsness = "nonqs"
                    dim_nonqs = k
                    if h_I == 1:
                        sing_type = "hypersurface"
                        sing_weights = tuple(point[i] % h_I for i in range(len(point)) if i != stratum_indices[0])
                        e = degree % h_I
                        sing = (h_I, sing_weights, e, stratum_weights, dim_nonqs, sing_type, qsness)
                        if terminal(degree, point, sing, k):
                            sings.append(sing)
                        else:
                            return False
                    else: #h_I >= 2
                        sing_type = "hyperquotient"
                        sing_weights = tuple(point[i] % h_I for i in range(len(point)) if i != stratum_indices[0])
                        e = degree % h_I
                        sing = (h_I, sing_weights, e, stratum_weights, dim_nonqs, sing_type, qsness)
                        if terminal(degree, point, sing, k):
                            sings.append(sing)
                        else:
                            return False
                else: #1<=rho_I<= k
                    dim_nonqs = k - rho_I
                    if h_I == 1:
                        qsness= "nonqs"
                        sing_type = "hypersurface"
                        sing_weights = tuple(point[i] % h_I for i in range(len(point)) if i != stratum_indices[0])
                        e = degree % h_I
                        sing = (h_I, sing_weights, e, stratum_weights, dim_nonqs, sing_type, qsness)
                        if terminal(degree, point, sing, k):
                            sings.append(sing)
                        else:
                            return False
                    else: #h_I >= 2
                        qsness= "qs"
                        sing_type = "quotient"
                        t = tangent_index(degree, point, stratum_weights, stratum_indices_complement) 
                        sing_weights = tuple(point[i] % h_I for i in range(len(point)) if i != stratum_indices[0] if i != t)
                        sing = (h_I, sing_weights, point[t], stratum_weights, dim_qs, sing_type, qsness)
                        if terminal(degree, point, sing, k):
                            sings.append(sing)
                        else:
                            return False
                        qsness= "nonqs"
                        sing_type = "hyperquotient"
                        sing_weights = tuple(point[i] % h_I for i in range(len(point)) if i != stratum_indices[0])
                        e = degree % h_I
                        sing = (h_I, sing_weights, e, stratum_weights, dim_nonqs, sing_type, qsness)
                        if terminal(degree, point, sing, k):
                            sings.append(sing)
                        else:
                            return False
    return sings

#strata(point): returns list of strata, where each stratum is given by (h_I, stratum_weights, stratum_indices, k)
#h_I is the gcd of the stratum weights, k is the dimension of the stratum
def strata(point):
    strata = []
    for stratum_len in range(1, len(point) + 1):
        for stratum_indices in it.combinations(range(len(point)), stratum_len):
            stratum_weights = tuple(point[i] for i in stratum_indices)
            h_I = math.gcd(*stratum_weights)
            k = len(stratum_weights) - 1
            stratum = (h_I, stratum_weights, stratum_indices, k)
            strata.append(stratum)
    return tuple(strata)

#monomial_exists(degree, stratum_weights): returns True if there exists a monomial of the given degree that can be formed using the stratum weights, False otherwise
def monomial_exists(degree, stratum_weights):
    def monomial_builder_recursive(total,index):
        if index == len(stratum_weights):
            return total == degree
        for m in range((degree - total) // stratum_weights[index] + 1):
            if monomial_builder_recursive(total + m * stratum_weights[index], index + 1):
                return True
        return False
    return monomial_builder_recursive(0, 0)

#tangent_index(degree, point, stratum_weights, search_indices): returns the index of a tangent variable if it exists, None otherwise
def tangent_index(degree, point, stratum_weights, search_indices):
    for i in search_indices:
        if monomial_exists(degree - point[i], stratum_weights):
            return i
    return None

#mu(degree, stratum_weights): returns the number of monomials of the given degree that can be formed using the stratum weights
def mu(degree, stratum_weights):
    combinations = [0] * (degree + 1) # combinations[i] = number of ways to make i from stratum_weights
    combinations[0] = 1 
    for w in stratum_weights:
        for i in range(w, degree + 1): 
            combinations[i] += combinations[i - w]
        if combinations[degree] >= 2:
            return 2
    return combinations[degree]

#rho(degree, point, stratum_weights): returns the number of tangent variables
def rho(degree, point, stratum_weights):
    rho_count = 0
    for a_t in point:
        if mu(degree - a_t, stratum_weights) >= 1:
            rho_count += 1
    return rho_count

#monomial_finder(degree, stratum_weights, monomial_blacklist): returns a monomial of the given degree that can be formed using the stratum weights and is not in the monomial blacklist, None if no such monomial exists
def monomial_finder(degree, stratum_weights, monomial_blacklist):
    n = len(stratum_weights)
    def monomial_builder_recursive(index, monomial):
        total = sum(monomial[i] * stratum_weights[i] for i in range(n))
        if index == n:
            return monomial if (total == degree) and (monomial not in monomial_blacklist) else None
        for m in range((degree - total) // stratum_weights[index] + 1):
            new_monomial = tuple(monomial[i] if i != index else m for i in range(n))
            result = monomial_builder_recursive(index + 1, new_monomial)
            if result is not None:
                return result
        return None
    return monomial_builder_recursive(0, (0,) * n)

#rank_test(degree, point, stratum_weights, search_indices): returns True if the rank condition is satisfied, False otherwise
def rank_test(degree, point, stratum_weights, stratum_indices): 
    stratum_indices_complement = tuple(i for i in range(len(point)) if i not in stratum_indices)
    J = []
    for i in stratum_indices_complement:
        if monomial_exists(degree - point[i], stratum_weights):
            J.append(i)
    if len(J) == 0:
        return True 
    #If any mu(g_j)=1, then fail
    elif any(mu(degree - point[j], stratum_weights) == 1 for j in J):
        return False
    #Else, mu(g_j)>=2 for all j in J
    else:
        monomials_Y = [[] for _ in range(len(point))] # monomials_Y[i] will hold the list of monomials for g_i
        def grab_new_monomial(J):
            for j in J:
                monomial = monomial_finder(degree - point[j], stratum_weights, monomials_Y[j])
                if monomial is not None:
                    monomials_Y[j].append(monomial)
                    return True
            return False  
        def rank_of_MJ(J):
            MJ = []
            for j in J:
                monomials_gj = monomials_Y[j]
                if len(monomials_gj) < 2:
                    continue  # need at least m0_j and one other monomial to get a difference
                m0 = np.array(monomials_gj[0])
                MJ.extend(np.array(m) - m0 for m in monomials_gj[1:])
            return np.linalg.matrix_rank(np.array(MJ))
        grab_available = True
        for l in range(2, len(J) + 1): #automatically satisfies l=1 as mu(gj)>=2 for all j in J
            for I in it.combinations(J, l):
                while rank_of_MJ(I) < l:
                    grab_available = grab_new_monomial(J)
                    if not grab_available:
                        return False
    return True

#terminal(degree, point, sing, stratum): returns True if the given singularity is terminal, False otherwise
def terminal(degree, point, sing, k):
    if k > dim_X - 2:
        return False
    r = sing[0]
    sing_weights = sing[1]
    qsness = sing[-1]
    if qsness == "qs": #quasismooth
        #Apply Reid--Shepherd-Barron--Tai criterion
        for i in range(1, r):
            alpha_sum = sum((i * weight) % r for weight in sing_weights)
            if alpha_sum - r <= 0:
                return False
        return True
    else: #nonquasismooth
        if r == 1:
            return True #An approximation
        else: #r>1
            #Apply Mori's criterion for the unit cube (a neccessary condition for terminality)
            def Mori_criterion(total, index, alpha_f):
                if index == len(alpha):
                    if total == degree and alpha_sum - alpha_f - r > 0:
                        return True
                    return False
                for m in range((degree - total) // point[index] + 1):
                    if Mori_criterion(total + m * point[index], index + 1, alpha_f + m * alpha[index]):
                        return True
                return False
            for i in range(1, r):
                alpha = tuple((i * weight) % r for weight in point)
                alpha_sum = sum((i * weight) % r for weight in sing_weights)
                if Mori_criterion(0, 0, 0) == False:
                    return False
            return True
        
        
#fano_terminal(point): returns the point if it corresponds to a terminal hypersurface, None otherwise. Used for parallelisation of the search.
def fano_terminal(point):
    if terminal_point(point)==True:
        return point
    else:
        return None

#variety_maker(d): returns list of varieties to be checked for a given degree d, given by the points [a1,a2,a3,a4,a5,d+alpha_X-(a1+a2+a3+a4+a5)] with 1<=a1<=a2<=a3<=a4<=a5
def variety_maker(d):
    varieties=[]
    for a1 in range(1,int((d+alpha_X)/6)+1):
        for a2 in range(a1,int((d+alpha_X-a1)/5)+1):
            for a3 in range(a2,int((d+alpha_X-(a1+a2))/4)+1):
                for a4 in range(a3,int((d+alpha_X-(a1+a2+a3))/3)+1):
                    for a5 in range(a4,int((d+alpha_X-(a1+a2+a3+a4))/2)+1):
                        variety=[a1,a2,a3,a4,a5,d+alpha_X-(a1+a2+a3+a4+a5)]
                        varieties.append(variety)
    return varieties
    
if __name__ == '__main__':
    
    ###################################################################################################
    #2. Search
    ###################################################################################################
    
    d_min = 1
    d_max = 200
    
    import multiprocessing as mp
    import time
    import numpy as np
    import os
    from pathlib import Path

    data_terminal_points = []
    time_start = time.time()
    
    #Run the search in parallel, iterating through degrees and checking the corresponding varieties.
    with mp.Pool(mp.cpu_count()) as pool:
        for d in range(d_min, d_max + 1):
            varieties = variety_maker(d)
            if not varieties:
                continue
            chunksize = max(1, len(varieties) // (mp.cpu_count() * 4))
            for result in pool.imap_unordered(fano_terminal, varieties, chunksize=chunksize):
                if result is not None:
                    data_terminal_points.append(result)
            print(d, time.time() - time_start, len(data_terminal_points))

    PROJECT_DIR = Path(__file__).resolve().parent.parent
    DATA_DIR = PROJECT_DIR / "data" / "exhaustive" / "approximation"
    os.makedirs(DATA_DIR, exist_ok=True)
    np.savetxt(DATA_DIR / "approximation_points.csv", data_terminal_points, delimiter=",")
