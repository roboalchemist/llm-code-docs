:::::::::::::::::::::::::::::::: {#main-content .bd-main role="main"}
::: sbt-scroll-pixel-helper
:::

::::::::::::::::::::::::: bd-content
:::::::::::::::::::: bd-article-container
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
  [.rst]{.btn__text-container}](../../_sources/python/_autosummary/mlx.core.vjp.rst "Download source file"){.btn
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
# mlx.core.vjp

::::: {#print-main-content}
:::: {#jb-print-toc}
::: {}
## Contents
:::

- [[`vjp()`{.docutils .literal
  .notranslate}]{.pre}](#mlx.core.vjp){.reference .internal .nav-link}
::::
:::::
::::::

::: {#searchbox}
:::

::: {#mlx-core-vjp .section}
# mlx.core.vjp[\#](#mlx-core-vjp "Link to this heading"){.headerlink}

[[vjp]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[fun]{.pre}]{.n}[[:]{.pre}]{.p}[ ]{.w}[[Callable]{.pre}]{.n}*, *[[primals]{.pre}]{.n}[[:]{.pre}]{.p}[ ]{.w}[[[list]{.pre}](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)"){.reference .external}[[\[]{.pre}]{.p}[[array]{.pre}](mlx.core.array.html#mlx.core.array "mlx.core.array"){.reference .internal}[[\]]{.pre}]{.p}]{.n}*, *[[cotangents]{.pre}]{.n}[[:]{.pre}]{.p}[ ]{.w}[[[list]{.pre}](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)"){.reference .external}[[\[]{.pre}]{.p}[[array]{.pre}](mlx.core.array.html#mlx.core.array "mlx.core.array"){.reference .internal}[[\]]{.pre}]{.p}]{.n}*[)]{.sig-paren} [[→]{.sig-return-icon} [[[tuple]{.pre}](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)"){.reference .external}[[\[]{.pre}]{.p}[[list]{.pre}](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)"){.reference .external}[[\[]{.pre}]{.p}[[array]{.pre}](mlx.core.array.html#mlx.core.array "mlx.core.array"){.reference .internal}[[\]]{.pre}]{.p}[[,]{.pre}]{.p}[ ]{.w}[[list]{.pre}](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)"){.reference .external}[[\[]{.pre}]{.p}[[array]{.pre}](mlx.core.array.html#mlx.core.array "mlx.core.array"){.reference .internal}[[\]]{.pre}]{.p}[[\]]{.pre}]{.p}]{.sig-return-typehint}]{.sig-return}[\#](#mlx.core.vjp "Link to this definition"){.headerlink}

:   Compute the vector-Jacobian product.

    Computes the product of the [`cotangents`{.docutils .literal
    .notranslate}]{.pre} with the Jacobian of a function
    [`fun`{.docutils .literal .notranslate}]{.pre} evaluated at
    [`primals`{.docutils .literal .notranslate}]{.pre}.

    Parameters[:]{.colon}

    :   - **fun** (*Callable*) -- A function which takes a variable
          number of [[`array`{.xref .py .py-class .docutils .literal
          .notranslate}]{.pre}](mlx.core.array.html#mlx.core.array "mlx.core.array"){.reference
          .internal} and returns a single [[`array`{.xref .py .py-class
          .docutils .literal
          .notranslate}]{.pre}](mlx.core.array.html#mlx.core.array "mlx.core.array"){.reference
          .internal} or list of [[`array`{.xref .py .py-class .docutils
          .literal
          .notranslate}]{.pre}](mlx.core.array.html#mlx.core.array "mlx.core.array"){.reference
          .internal}.

        - **primals**
          ([*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)"){.reference
          .external}*(*[*array*](mlx.core.array.html#mlx.core.array "mlx.core.array"){.reference
          .internal}*)*) -- A list of [[`array`{.xref .py .py-class
          .docutils .literal
          .notranslate}]{.pre}](mlx.core.array.html#mlx.core.array "mlx.core.array"){.reference
          .internal} at which to evaluate the Jacobian.

        - **cotangents**
          ([*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)"){.reference
          .external}*(*[*array*](mlx.core.array.html#mlx.core.array "mlx.core.array"){.reference
          .internal}*)*) -- A list of [[`array`{.xref .py .py-class
          .docutils .literal
          .notranslate}]{.pre}](mlx.core.array.html#mlx.core.array "mlx.core.array"){.reference
          .internal} which are the "vector" in the vector-Jacobian
          product. The [`cotangents`{.docutils .literal
          .notranslate}]{.pre} should be the same in number, shape, and
          type as the outputs of [`fun`{.docutils .literal
          .notranslate}]{.pre}.

    Returns[:]{.colon}

    :   A tuple with the outputs of [`fun`{.docutils .literal
        .notranslate}]{.pre} in the first position and the
        vector-Jacobian products in the second position.

    Return type[:]{.colon}

    :   [*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)"){.reference
        .external}([*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)"){.reference
        .external}([*array*](mlx.core.array.html#mlx.core.array "mlx.core.array"){.reference
        .internal}),
        [*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)"){.reference
        .external}([*array*](mlx.core.array.html#mlx.core.array "mlx.core.array"){.reference
        .internal}))

    Example

    :::: {.highlight-python .notranslate}
    ::: highlight
        import mlx.core as mx

        outs, vjps = mx.vjp(mx.sin, (mx.array(1.0),), (mx.array(1.0),))
    :::
    ::::
:::

::::: prev-next-area
[](mlx.core.jvp.html "previous page"){.left-prev}

::: prev-next-info
previous

mlx.core.jvp
:::

[](mlx.core.vmap.html "next page"){.right-next}

::: prev-next-info
next

mlx.core.vmap
:::
:::::
::::::::::::::::::::

:::::: {#pst-secondary-sidebar .bd-sidebar-secondary .bd-toc}
::::: {.sidebar-secondary-items .sidebar-secondary__inner}
:::: sidebar-secondary-item
::: {#pst-page-navigation-heading-2 .page-toc .tocsection .onthispage}
Contents
:::

- [[`vjp()`{.docutils .literal
  .notranslate}]{.pre}](#mlx.core.vjp){.reference .internal .nav-link}
::::
:::::
::::::
:::::::::::::::::::::::::

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
::::::::::::::::::::::::::::::::
