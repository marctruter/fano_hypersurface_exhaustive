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
- Recorded weight vectors and computational information about singularities and terminality. The complete tabulated classification is [archived on Zenodo](https://doi.org/10.5281/zenodo.23836799).

The precise search procedure, terminality criteria and classification results will be described in *Terminal Fano 4-fold Hypersurfaces* (in preparation).

## Repository structure

```text
code/                               Exhaustive-search and analysis scripts/notebooks

data/
  quasismooth/
    quasismooth_terminal.csv         Reference quasismooth classification
  certification/
    certification_short.pkl          Degree and weight records
    certification_medium.pkl         Condensed singularity records
    certification_long.pkl           Detailed certification records
    certification_raw.pkl            Raw records and certification outcomes

figures/                            Figures associated with the analysis
LICENSE                             MIT licence
README.md
```

The tree highlights the principal directories and certification files; it is not a complete listing of the computational outputs.

## Classification and certification data

### Exhaustive-search certification datasets

The files in [`data/certification/`](data/certification/) contain the records associated with the exhaustive search and terminality analysis through weighted degree $d\leq200$. The processed datasets describe the families and the singularities used in their certification, while the raw records retain the outcomes of the terminality tests.

| File | Description |
| --- | --- |
| [`certification_short.pkl`](data/certification/certification_short.pkl) | Short records containing equation degree and six ambient weights |
| [`certification_medium.pkl`](data/certification/certification_medium.pkl) | Condensed singularity data for the certified terminal families |
| [`certification_long.pkl`](data/certification/certification_long.pkl) | More detailed singularity and certification records |
| [`certification_raw.pkl`](data/certification/certification_raw.pkl) | Raw certification records, including terminality-test outcomes |

Each family is determined by its six ambient weights $(a_1,\ldots,a_6)$, with defining equation degree

$$
d=a_1+\cdots+a_6-1.
$$

For example, the weights $(1,1,5,25,37,68)$ determine the hypersurface $X_{136}\subset\mathbb{P}(1,1,5,25,37,68)$. The `.pkl` files are Python pickle files for use with the scripts and notebooks in [`code/`](code/). Only load pickle files from sources you trust.

### Full classification: Zenodo

The complete tabulated classification is published as a separate Zenodo dataset:

**[Classification of Terminal Fano 4-Fold Hypersurfaces in Weighted Projective Space of Index 1 up to Degree 200](https://doi.org/10.5281/zenodo.23836799)**  
**DOI:** [`10.5281/zenodo.23836799`](https://doi.org/10.5281/zenodo.23836799)

The SQL archive, **`terminal_fano_4fold_index1_200.sql`**, contains the table `terminal_fano_4fold_index1_200`. It records the equation degree and individual weights, canonical class, point and curve singularity baskets (organised by type), their sizes, and smoothness, quasismoothness, terminality and canonicality indicators. It also records the anticanonical volume

$$
(-K_X)^4=\frac{d}{a_1a_2a_3a_4a_5a_6}.
$$

In the SQL data, `Degree` represents the exact rational volume and `Degree_dec` its decimal approximation. The archive allows users to inspect and query the classification without rerunning the exhaustive search.

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

[`data/quasismooth/quasismooth_terminal.csv`](data/quasismooth/quasismooth_terminal.csv) contains the quasismooth terminal Fano fourfold reference data of index one. Its sources are the [Graded Ring Database (GRDB)](https://www.grdb.co.uk/) and the classification by Gavin Brown and Alexander M. Kasprzyk:

> G. Brown and A. M. Kasprzyk, [*Four-dimensional projective orbifold hypersurfaces*](https://doi.org/10.1080/10586458.2015.1054054), *Experimental Mathematics* **25** (2016), no. 2, 176–193.

Please cite these original sources when using the quasismooth data.

## Reproducing the computations

Clone the repository:

```bash
git clone https://github.com/marctruter/fano_hypersurface_exhaustive.git
cd fano_hypersurface_exhaustive
```

Use a Python environment with the dependencies imported by the relevant scripts and notebooks in [`code/`](code/). The scripts use relative paths, so check their expected working directory and data locations before execution. The [Zenodo classification archive](https://doi.org/10.5281/zenodo.23836799) provides the tabulated results without requiring a repeat of the computational search.

## Related work

The companion repository, [*Terminal Fano 4-fold Hypersurfaces via Deep Reinforcement Learning*](https://github.com/marctruter/fano_hypersurface_deep), uses heuristic searches to discover additional terminal Fano fourfold hypersurfaces, including examples with $d>200$. The associated paper is available as [arXiv:2603.15437](https://arxiv.org/abs/2603.15437), and the [sporadic classification dataset](https://doi.org/10.5281/zenodo.23837634) is archived separately on Zenodo.

## Citation

If you use the exhaustive-search code or classification data, please cite the associated mathematical work and the Zenodo dataset:

- **Marc Truter**, *Terminal Fano 4-fold Hypersurfaces*, in preparation.
- **Marc Truter**, [*Classification of Terminal Fano 4-Fold Hypersurfaces in Weighted Projective Space of Index 1 up to Degree 200*](https://doi.org/10.5281/zenodo.23836799), Zenodo (2026). DOI: `10.5281/zenodo.23836799`.

The methods for certifying terminality are also developed in Marc Truter's PhD thesis, *Terminal Hypersurfaces in Weighted Projective Spaces*, University of Warwick.

If you use the reference quasismooth classification, please also cite the [GRDB](https://www.grdb.co.uk/) and [Brown–Kasprzyk (2016)](https://doi.org/10.1080/10586458.2015.1054054).

## Acknowledgements

This work was supported by the UK Engineering and Physical Sciences Research Council (EPSRC) under grant number EP/W523793/1.

## Licence

The source code is released under the [MIT licence](LICENSE).
