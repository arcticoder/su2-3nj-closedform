---
layout: default
title: A Closed-Form Hypergeometric Product Formula for General SU(2) 3nj Recoupling Coefficients
author: Arcticoder
date: May 25, 2025
---

# A Closed-Form Hypergeometric Product Formula for General SU(2) 3nj Recoupling Coefficients

*{{ page.author }}*

*{{ page.date | date: "%B %d, %Y" }}*

## Abstract

We present a fully closed-form expression for the SU(2) 3nj recoupling coefficients associated to any trivalent graph. By cutting each edge of the coupling graph and computing matching numbers on the resulting components, one obtains for each edge a ratio $\rho_e$. The general 3nj symbol is then given as a product of hypergeometric factors:

$$
\{3nj\}(\{j_e\})
=\prod_{e\in E}\frac{1}{(2j_e)!}\;
{}_2F_1\Bigl(-2j_e,\tfrac12;1;-\rho_e\Bigr).
$$

This work builds on the finite recurrence relations of [^finiteRec], the uniform closed-form 12j representation of [^uniform12j], and the universal generating functional framework of [^universalGF].

[View the full paper](/full-paper/)

[^finiteRec]: Arcticoder, "Closed-Form Finite Recurrences for SU(2) 3nj Symbols," May 25, 2025. Available at: <https://arcticoder.github.io/su2-3nj-recurrences/>
[^uniform12j]: Arcticoder, "Uniform Closed-Form Representation of SU(2) 12j Symbols," May 25, 2025. Available at: <https://arcticoder.github.io/su2-3nj-uniform-closed-form/>
[^universalGF]: Arcticoder, "A Universal Generating Functional for SU(2) 3nj Symbols," May 24, 2025. Available at: <https://arcticoder.github.io/su2-3nj-generating-functional/>
