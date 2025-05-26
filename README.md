# A Closed-Form Hypergeometric Product Formula for General SU(2) 3nj Recoupling Coefficients

This repository contains a mathematical physics paper on a new closed-form expression for SU(2) 3nj recoupling coefficients.

**View the paper online: [https://arcticoder.github.io/su2-3nj-closedform/](https://arcticoder.github.io/su2-3nj-closedform/)**

## Abstract

We present a fully closed-form expression for the SU(2) 3nj recoupling coefficients associated to any trivalent graph. By cutting each edge of the coupling graph and computing matching numbers on the resulting components, one obtains for each edge a ratio. The general 3nj symbol is then given as a product of hypergeometric factors involving these ratios.

## Repository Structure

- `index.md` - Complete paper with abstract and all sections (Jekyll front page)
- `A Closed-Form Hypergeometric Product Formula for General SU(2) 3nj Recoupling Coefficients.tex` - Original LaTeX source
- `A Closed-Form Hypergeometric Product Formula for General SU(2) 3nj Recoupling Coefficients.pdf` - PDF version of the paper
- `scripts/` - Directory containing Python scripts for analysis
  - `coefficient_calculator.py` - Script for calculating and analyzing 3nj coefficients
  - `symmetry_checker.py` - Script for checking reflection symmetry properties of 3nj coefficients
- `data/` - Directory for generated output from analysis scripts

## Analysis Scripts

### Coefficient Calculator (`scripts/coefficient_calculator.py`)

This script calculates SU(2) 3nj recoupling coefficients using the closed-form hypergeometric product formula and analyzes their properties.

**Features:**
- Calculates 3nj symbols for arbitrary angular momentum configurations
- Tests reflection symmetry properties
- Generates analysis data for various test cases

**Usage:**
```bash
# Run from the repository root directory
python scripts/coefficient_calculator.py
```

**Output:**
- Prints analysis results to the console
- Saves results to `data/3nj_analysis.csv`

### Symmetry Checker (`scripts/symmetry_checker.py`)

This script specifically checks the reflection symmetry properties of 3nj symbols (particularly for the 15j-chain).

**Features:**
- Tests reflection symmetry across multiple test cases
- Analyzes differences between original and reflected coefficient values

**Usage:**
```bash
# Run from the repository root directory
python scripts/symmetry_checker.py
```

**Output:**
- Prints symmetry analysis to the console
- Saves results to `data/reflection_symmetry.csv`

## Requirements

The scripts require the following Python packages:
- mpmath
- pandas
- numpy

## Related Works

- [Closed-Form Finite Recurrences for SU(2) 3nj Symbols](https://arcticoder.github.io/su2-3nj-recurrences/)
- [Uniform Closed-Form Representation of SU(2) 12j Symbols](https://arcticoder.github.io/su2-3nj-uniform-closed-form/)
- [A Universal Generating Functional for SU(2) 3nj Symbols](https://arcticoder.github.io/su2-3nj-generating-functional/)
