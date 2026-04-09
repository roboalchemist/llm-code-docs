:::::::::::::::::::::::::::::::::::::::: {#main-content .bd-main role="main"}
::: sbt-scroll-pixel-helper
:::

::::::::::::::::::::::::::::::::: bd-content
:::::::::::::::::::::::::::: bd-article-container
:::::::::: {.bd-header-article .d-print-none}
::::::::: {.header-article-items .header-article__inner}
:::: header-article-items__start
::: header-article-item
[]{.fa-solid .fa-bars}
:::
::::

:::::: header-article-items__end
::::: header-article-item
:::: article-header-buttons
[[
]{.btn__icon-container}](https://github.com/ml-explore/mlx "Source repository"){.btn
.btn-sm .btn-source-repository-button target="_blank"
bs-placement="bottom" bs-toggle="tooltip"}

::: {.dropdown .dropdown-download-buttons}

- [[ ]{.btn__icon-container}
  [.rst]{.btn__text-container}](../_sources/usage/quick_start.rst "Download source file"){.btn
  .btn-sm .btn-download-source-button .dropdown-item target="_blank"
  bs-placement="left" bs-toggle="tooltip"}
- [ ]{.btn__icon-container} [.pdf]{.btn__text-container}
:::

[ ]{.btn__icon-container}

[]{.fa-solid .fa-list}
::::
:::::
::::::
:::::::::
::::::::::

:::::: {#jb-print-docs-body .onlyprint}

# Quick Start Guide

::::: {#print-main-content}
:::: {#jb-print-toc}
::: {}

## Contents

:::

- [Basics](#basics){.reference .internal .nav-link}
- [Function and Graph
  Transformations](#function-and-graph-transformations){.reference
  .internal .nav-link}
::::
:::::
::::::

::: {#searchbox}
:::

::::::::::: {#quick-start-guide .section}

# Quick Start Guide[\#](#quick-start-guide "Link to this heading"){.headerlink}

::::::: {#basics .section}

## Basics[\#](#basics "Link to this heading"){.headerlink}

Import [`mlx.core`{.docutils .literal .notranslate}]{.pre} and make an
[[`array`{.xref .py .py-class .docutils .literal
.notranslate}]{.pre}](../python/_autosummary/mlx.core.array.html#mlx.core.array "mlx.core.array"){.reference
.internal}:

:::: {.highlight-python .notranslate}
::: highlight
    >> import mlx.core as mx
    >> a = mx.array([1, 2, 3, 4])
    >> a.shape
    [4]
    >> a.dtype
    int32
    >> b = mx.array([1.0, 2.0, 3.0, 4.0])
    >> b.dtype
    float32
:::
::::

Operations in MLX are lazy. The outputs of MLX operations are not
computed until they are needed. To force an array to be evaluated use
[[`eval()`{.xref .py .py-func .docutils .literal
.notranslate}]{.pre}](../python/_autosummary/mlx.core.eval.html#mlx.core.eval "mlx.core.eval"){.reference
.internal}. Arrays will automatically be evaluated in a few cases. For
example, inspecting a scalar with [[`array.item()`{.xref .py .py-meth
.docutils .literal
.notranslate}]{.pre}](../python/_autosummary/mlx.core.array.item.html#mlx.core.array.item "mlx.core.array.item"){.reference
.internal}, printing an array, or converting an array from
[[`array`{.xref .py .py-class .docutils .literal
.notranslate}]{.pre}](../python/_autosummary/mlx.core.array.html#mlx.core.array "mlx.core.array"){.reference
.internal} to [[`numpy.ndarray`{.xref .py .py-class .docutils .literal
.notranslate}]{.pre}](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.4)"){.reference
.external} all automatically evaluate the array.

:::: {.highlight-python .notranslate}
::: highlight
    >> c = a + b    # c not yet evaluated
    >> mx.eval(c)  # evaluates c
    >> c = a + b
    >> print(c)     # Also evaluates c
    array([2, 4, 6, 8], dtype=float32)
    >> c = a + b
    >> import numpy as np
    >> np.array(c)   # Also evaluates c
    array([2., 4., 6., 8.], dtype=float32)
:::
::::

See the page on [[Lazy Evaluation]{.std
.std-ref}](lazy_evaluation.html#lazy-eval){.reference .internal} for
more details.
:::::::

::::: {#function-and-graph-transformations .section}

## Function and Graph Transformations[\#](#function-and-graph-transformations "Link to this heading"){.headerlink}

MLX has standard function transformations like [[`grad()`{.xref .py
.py-func .docutils .literal
.notranslate}]{.pre}](../python/_autosummary/mlx.core.grad.html#mlx.core.grad "mlx.core.grad"){.reference
.internal} and [[`vmap()`{.xref .py .py-func .docutils .literal
.notranslate}]{.pre}](../python/_autosummary/mlx.core.vmap.html#mlx.core.vmap "mlx.core.vmap"){.reference
.internal}. Transformations can be composed arbitrarily. For example
[`grad(vmap(grad(fn)))`{.docutils .literal .notranslate}]{.pre} (or any
other composition) is allowed.

:::: {.highlight-python .notranslate}
::: highlight
    >> x = mx.array(0.0)
    >> mx.sin(x)
    array(0, dtype=float32)
    >> mx.grad(mx.sin)(x)
    array(1, dtype=float32)
    >> mx.grad(mx.grad(mx.sin))(x)
    array(-0, dtype=float32)
:::
::::

Other gradient transformations include [[`vjp()`{.xref .py .py-func
.docutils .literal
.notranslate}]{.pre}](../python/_autosummary/mlx.core.vjp.html#mlx.core.vjp "mlx.core.vjp"){.reference
.internal} for vector-Jacobian products and [[`jvp()`{.xref .py .py-func
.docutils .literal
.notranslate}]{.pre}](../python/_autosummary/mlx.core.jvp.html#mlx.core.jvp "mlx.core.jvp"){.reference
.internal} for Jacobian-vector products.

Use [[`value_and_grad()`{.xref .py .py-func .docutils .literal
.notranslate}]{.pre}](../python/_autosummary/mlx.core.value_and_grad.html#mlx.core.value_and_grad "mlx.core.value_and_grad"){.reference
.internal} to efficiently compute both a function's output and gradient
with respect to the function's input.
:::::
:::::::::::

::::: prev-next-area
[](../install.html "previous page"){.left-prev}

::: prev-next-info
previous

Build and Install
:::

[](lazy_evaluation.html "next page"){.right-next}

::: prev-next-info
next

Lazy Evaluation
:::
:::::
::::::::::::::::::::::::::::

:::::: {#pst-secondary-sidebar .bd-sidebar-secondary .bd-toc}
::::: {.sidebar-secondary-items .sidebar-secondary__inner}
:::: sidebar-secondary-item
::: {#pst-page-navigation-heading-2 .page-toc .tocsection .onthispage}
Contents
:::

- [Basics](#basics){.reference .internal .nav-link}
- [Function and Graph
  Transformations](#function-and-graph-transformations){.reference
  .internal .nav-link}
::::
:::::
::::::
:::::::::::::::::::::::::::::::::

::::::: {.bd-footer-content__inner .container}
::: footer-item
By MLX Contributors
:::

::: footer-item
© Copyright 2023, Apple.\
:::

::: footer-item
:::

::: footer-item
:::
:::::::
::::::::::::::::::::::::::::::::::::::::
