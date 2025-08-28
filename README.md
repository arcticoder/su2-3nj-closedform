```markdown
# A Closed-Form Hypergeometric Product Formula for General SU(2) 3nj Recoupling Coefficients — Research Paper

This repository hosts the LaTeX source, published PDF, and analysis scripts accompanying a research paper describing a closed-form hypergeometric product expression for SU(2) 3nj recoupling coefficients. The materials are intended for reproducibility and independent verification by researchers in mathematical physics.

**Paper (rendered):** https://arcticoder.github.io/su2-3nj-closedform/

## Abstract (concise)

We present a closed-form product representation for SU(2) 3nj recoupling coefficients associated with trivalent graphs. The expression is constructed by cutting edges and computing matching-number-derived ratios; the 3nj symbol is expressed as a product of hypergeometric factors parameterized by these ratios. Readers should consult the paper for definitions, assumptions, and derivations.

## Repository Contents

- `index.md` — Paper landing page (Jekyll)
- `<paper>.tex` and `<paper>.pdf` — LaTeX source and rendered PDF
- `scripts/` — Analysis scripts (see below)
- `data/` — Generated outputs for reproducing figures and tables

## Analysis Scripts

### `scripts/coefficient_calculator.py`

Computes 3nj coefficients using the closed-form formula and produces analysis outputs. Use for reproducing numerical experiments from the paper.

Usage (research-only):
```bash
python scripts/coefficient_calculator.py --out data/3nj_analysis.csv
```

### `scripts/symmetry_checker.py`

Checks symmetry properties (e.g., reflection) for selected 3nj configurations and produces `data/reflection_symmetry.csv`.

Usage:
```bash
python scripts/symmetry_checker.py --out data/reflection_symmetry.csv
```

## Requirements

- `mpmath`, `numpy`, `pandas` (install via `pip install -r requirements.txt`)

## Scope, Validation & Limitations

Scope
- Audience: mathematical physicists and numerical analysts interested in SU(2) recoupling and hypergeometric representations.
- Purpose: provide reproducible derivations and computational tools to evaluate and analyze the closed-form expressions.

Validation & Reproducibility
- Repro artifacts: include `data/*`, the approximate commit id, and the command-line arguments used for runs when citing numeric results.
- For UQ: if sampling or stochastic methods are used, include seeds and diagnostic outputs (convergence checks, error bounds).

Limitations
- The formulas and numeric examples are derived under the assumptions stated in the paper; applicability outside those assumptions should be validated by readers.

## Citing

If you use these results, cite the paper and include the commit id of this repository and any generated data artifacts.

```

