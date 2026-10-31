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
- Recorded weight vectors and computational information about singularities and terminality; the full classification data will be archived separately on Zenodo.

The precise search procedure, terminality criteria and classification results will be described in *Terminal Fano 4-fold Hypersurfaces* (in preparation).

## Repository structure

```text
code/                  Exhaustive-search and analysis code

data/
  quasismooth/
    quasismooth_terminal.csv
                       Reference quasismooth classification
  ...                  Exhaustive-search and certification data

figures/               Figures associated with the analysis
LICENSE                MIT licence
README.md
```

This overview shows the verified top-level directories and the quasismooth reference file; it is not a complete listing of the contents of `code/` and `data/`.

## Classification data

### Exhaustive search

The data in [`data/`](data/) supports the exhaustive search and terminality analysis through $d\leq200$. A family is specified by its six weights $(a_1,\ldots,a_6)$, with equation degree recovered from

$$
d=a_1+\cdots+a_6-1.
$$

The computational records distinguish quasismooth and nonquasismooth families and include singularity information used in terminality testing.

### Full classification: Zenodo

The full tabulated classification will be published as a separate **Zenodo dataset** alongside the forthcoming paper.

**Zenodo record / DOI:** *Link to be added after publication.*

The planned SQL archive, **`terminal_fano_fourfolds_index1_200.sql`**, records the equation degree and individual weights, canonical class, point, curve and surface singularity baskets, their sizes, and smoothness, quasismoothness, terminality and canonicality indicators. It also records the anticanonical volume

$$
(-K_X)^4=\frac{d}{a_1a_2a_3a_4a_5a_6}.
$$

In the SQL data, `Degree` represents the exact rational volume and `Degree_dec` its decimal approximation. The archive is intended to make the classification straightforward to inspect and query without rerunning the exhaustive search.

### Quasismooth reference classification

[`data/quasismooth/quasismooth_terminal.csv`](data/quasismooth/quasismooth_terminal.csv) contains the quasismooth terminal Fano fourfold reference data of index one. The source is the [Graded Ring Database (GRDB)](https://www.grdb.co.uk/forms/fano4ci1) and the classification by Gavin Brown and Alexander M. Kasprzyk:

> G. Brown and A. M. Kasprzyk, [*Four-dimensional projective orbifold hypersurfaces*](https://doi.org/10.1080/10586458.2015.1054054), *Experimental Mathematics* **25** (2016), no. 2, 176–193.

Please cite these original sources when using the quasismooth data.

## Reproducing the computations

Clone the repository:

```bash
git clone https://github.com/marctruter/fano_hypersurface_exhaustive.git
cd fano_hypersurface_exhaustive
```

Use a Python environment with the dependencies imported by the relevant scripts and notebooks in [`code/`](code/). The scripts use relative paths, so check their expected working directory and data locations before execution. The classification archive on Zenodo will provide the tabulated results without requiring a repeat of the computational search.

## Related work

Our companion repository, [*Deep Reinforcement Learning for Fano Hypersurfaces*](https://github.com/marctruter/fano_hypersurface_deep), uses heuristic searches to discover additional terminal Fano fourfold hypersurfaces, including examples with $d>200$. That project is documented separately in [arXiv:2603.15437](https://arxiv.org/abs/2603.15437).

## Citation

If you use the exhaustive-search code or classification data, please cite the associated paper and, when available, the Zenodo dataset:

- **Marc Truter**, *Terminal Fano 4-fold Hypersurfaces*, in preparation.
- **Zenodo classification dataset:** *DOI to be added.*

If you use the reference quasismooth classification, please also cite the [GRDB](https://www.grdb.co.uk/forms/fano4ci1) and [Brown–Kasprzyk (2016)](https://doi.org/10.1080/10586458.2015.1054054).

## Licence

The source code is released under the [MIT licence](LICENSE).
