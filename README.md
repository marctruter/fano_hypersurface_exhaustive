# Terminal Fano 4-fold Hypersurfaces

**Source code and data for *Terminal Fano 4-fold Hypersurfaces* (paper in preparation).**

We study terminal Fano fourfold hypersurfaces of index one,

$$
X_d\subset\mathbb{P}(a_1,\ldots,a_6),\qquad d=\sum_{i=1}^{6}a_i-1.
$$

We perform an **exhaustive computational search up to equation degree $d\leq200$**, extending the previously known quasismooth classification to nonquasismooth families. Checking terminality for these families requires analysing singularities that need not be cyclic quotients, including hyperquotient singularities. The accompanying code and data document the search and its certification results.

## Main results

- An exhaustive search in the degree range **$d\leq200$**.
- **77,387 nonquasismooth terminal families** identified in this range.
- Recorded weight vectors and computational information about singularities and terminality. The complete tabulated classification is [archived on Zenodo](https://doi.org/10.5281/zenodo.23836799) [3].

The terminality criteria and methods for analysing hyperquotient singularities are developed in the author's doctoral thesis [7] and will also be presented, together with the exhaustive search procedure and classification results, in *Terminal Fano 4-fold Hypersurfaces* [5].

## Repository structure

```text
code/                               Exhaustive-search and analysis scripts/notebooks

data/
  quasismooth/
    quasismooth_terminal.csv        Reference quasismooth classification
  certification/
    certification_short.csv         Six weights per row (no header)
    certification_short.pkl         Degree and weight records
    certification_medium.pkl        Condensed singularity records
    certification_long.pkl          Detailed certification records
    certification_raw.pkl           Raw records and certification outcomes

figures/                            Figures associated with the analysis
LICENSE                             MIT license
README.md
```

## Classification and certification data

### Exhaustive-search certification datasets

The files in [`data/certification/`](data/certification/) contain the records associated with the exhaustive search and terminality analysis through weighted degree $d\leq200$. The processed datasets describe the families and the singularities used in their certification, while the raw records retain the outcomes of the terminality tests.

| File | Description |
| --- | --- |
| [`certification_short.csv`](data/certification/certification_short.csv) | Six weights $a_1,\ldots,a_6$ per row; **no header** |
| [`certification_short.pkl`](data/certification/certification_short.pkl) | Short records containing equation degree and six ambient weights |
| [`certification_medium.pkl`](data/certification/certification_medium.pkl) | Condensed singularity data for the certified terminal families |
| [`certification_long.pkl`](data/certification/certification_long.pkl) | More detailed singularity and certification records |
| [`certification_raw.pkl`](data/certification/certification_raw.pkl) | Raw certification records, including terminality-test outcomes |

The short CSV contains one row per weight vector, for example:

```csv
1,1,5,25,37,68
```

This represents the hypersurface $X_{136}\subset\mathbb{P}(1,1,5,25,37,68)$; the equation degree is recovered from $d=\sum_i a_i-1$. The `.pkl` files are Python pickle files for use with the scripts and notebooks in [`code/`](code/).

### Full classification: Zenodo

The complete tabulated classification is published as a separate Zenodo dataset [3]:

**[Classification of Terminal Fano 4-Fold Hypersurfaces in Weighted Projective Space of Index 1 up to Degree 200](https://doi.org/10.5281/zenodo.23836799)**  
**DOI:** [`10.5281/zenodo.23836799`](https://doi.org/10.5281/zenodo.23836799)

The SQL archive, **`terminal_fano_4fold_index1_200.sql`**, contains the table `terminal_fano_4fold_index1_200`. It records the equation degree and individual weights, canonical class, point and curve singularity baskets (organised by type), their sizes, and smoothness, quasismoothness, terminality and canonicality indicators. It also records the anticanonical volume

$$
(-K_X)^4=\frac{d}{a_1a_2a_3a_4a_5a_6}.
$$

In the SQL data, `Degree` represents the exact rational volume and `Degree_dec` its decimal approximation.

After downloading the SQL file, it can be imported into SQLite (with the `sqlite3` command-line tool installed):

```bash
sqlite3 terminal_fano_4fold_index1_200.db ".read terminal_fano_4fold_index1_200.sql"
```

For example, the following retrieves all recorded nonquasismooth families of equation degree $200$:

```sql
SELECT *
FROM terminal_fano_4fold_index1_200
WHERE Equation_degree = 200 AND IsQsmooth = 0;
```

### Quasismooth reference classification

[`data/quasismooth/quasismooth_terminal.csv`](data/quasismooth/quasismooth_terminal.csv) contains the quasismooth terminal Fano fourfold reference data of index one. Its sources are the [Graded Ring Database (GRDB)](https://www.grdb.co.uk/) [2] and the classification by Gavin Brown and Alexander M. Kasprzyk [1].

## Reproducing the computations

1. Clone the repository:

   ```bash
   git clone https://github.com/marctruter/fano_hypersurface_exhaustive.git
   cd fano_hypersurface_exhaustive
   ```

2. Set up a Python environment with the packages imported by the relevant scripts and notebooks in [`code/`](code/).
3. Run the relevant scripts or notebooks, checking their expected working directory and relative data paths before execution.

## Companion repository

The companion repository, [*Terminal Fano 4-fold Hypersurfaces via Deep Reinforcement Learning*](https://github.com/marctruter/fano_hypersurface_deep), uses heuristic searches to discover additional terminal Fano fourfold hypersurfaces, including examples with $d>200$. The associated paper [6] is available as [arXiv:2603.15437](https://arxiv.org/abs/2603.15437), and the [sporadic classification dataset](https://doi.org/10.5281/zenodo.23837634) [4] is archived separately on Zenodo.

## Citation

If you use the exhaustive-search code or classification data, please cite the Zenodo classification dataset [3] and the associated mathematical work [5]. The methods for certifying terminality are also developed in the author's doctoral thesis [7].

If you use results from the companion heuristic-search project, please cite its paper [6] and sporadic dataset [4]. If you use the reference quasismooth classification, please also cite Brown–Kasprzyk [1] and the GRDB [2].

## References

[1] Gavin Brown and Alexander Kasprzyk, *Four-dimensional projective orbifold hypersurfaces*, *Experimental Mathematics* **25** (2016), no. 2, 176–193. https://doi.org/10.1080/10586458.2015.1054054.

[2] Gavin Brown and Alexander Kasprzyk, [Graded Ring Database](https://www.grdb.co.uk/).

[3] Marc Truter, *Classification of Terminal Fano 4-Fold Hypersurfaces in Weighted Projective Space of Index 1 up to Degree 200*, version 1.0 [Data set], Zenodo (2026). https://doi.org/10.5281/zenodo.23836799.

[4] Marc Truter, *Sporadic List of Terminal Fano 4-Fold Hypersurfaces in Weighted Projective Space of Index 1*, version 1.0 [Data set], Zenodo (2026). https://doi.org/10.5281/zenodo.23837634.

[5] Marc Truter, *Terminal Fano 4-fold Hypersurfaces*, in preparation.

[6] Marc Truter, *Terminal Fano 4-fold Hypersurfaces via Deep Reinforcement Learning*, [arXiv:2603.15437](https://arxiv.org/abs/2603.15437) (2026).

[7] Marc Truter, *Terminal Hypersurfaces in Weighted Projective Spaces*, PhD thesis, University of Warwick.

## Acknowledgements

This work was supported by the UK Engineering and Physical Sciences Research Council (EPSRC) under grant number EP/W523793/1.

## License

The source code is released under the [MIT license](LICENSE).
