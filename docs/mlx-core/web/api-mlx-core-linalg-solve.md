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
  [.rst]{.btn__text-container}](../../_sources/python/_autosummary/mlx.core.linalg.solve.rst "Download source file"){.btn
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
# mlx.core.linalg.solve

::::: {#print-main-content}
:::: {#jb-print-toc}
::: {}
## Contents
:::

- [[`solve()`{.docutils .literal
  .notranslate}]{.pre}](#mlx.core.linalg.solve){.reference .internal
  .nav-link}
::::
:::::
::::::

::: {#searchbox}
:::

::: {#mlx-core-linalg-solve .section}
# mlx.core.linalg.solve[\#](#mlx-core-linalg-solve "Link to this heading"){.headerlink}

[[solve]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[a]{.pre}]{.n}[[:]{.pre}]{.p}[ ]{.w}[[[array]{.pre}](mlx.core.array.html#mlx.core.array "mlx.core.array"){.reference .internal}]{.n}*, *[[b]{.pre}]{.n}[[:]{.pre}]{.p}[ ]{.w}[[[array]{.pre}](mlx.core.array.html#mlx.core.array "mlx.core.array"){.reference .internal}]{.n}*, *[[[\*]{.pre}]{.abbr title="Keyword-only parameters separator (PEP 3102)"}]{.keyword-only-separator .o}*, *[[stream]{.pre}]{.n}[[:]{.pre}]{.p}[ ]{.w}[[[None]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"){.reference .external}[ ]{.w}[[\|]{.pre}]{.p}[ ]{.w}[[Stream]{.pre}](stream_class.html#mlx.core.Stream "mlx.core.Stream"){.reference .internal}[ ]{.w}[[\|]{.pre}]{.p}[ ]{.w}[[Device]{.pre}](mlx.core.Device.html#mlx.core.Device "mlx.core.Device"){.reference .internal}]{.n}[ ]{.w}[[=]{.pre}]{.o}[ ]{.w}[[None]{.pre}]{.default_value}*[)]{.sig-paren} [[→]{.sig-return-icon} [[[array]{.pre}](mlx.core.array.html#mlx.core.array "mlx.core.array"){.reference .internal}]{.sig-return-typehint}]{.sig-return}[\#](#mlx.core.linalg.solve "Link to this definition"){.headerlink}

:   Compute the solution to a system of linear equations [`AX`{.docutils
    .literal .notranslate}]{.pre}` `{.docutils .literal
    .notranslate}[`=`{.docutils .literal
    .notranslate}]{.pre}` `{.docutils .literal
    .notranslate}[`B`{.docutils .literal .notranslate}]{.pre}.

    Parameters[:]{.colon}

    :   - **a**
          ([*array*](mlx.core.array.html#mlx.core.array "mlx.core.array"){.reference
          .internal}) -- Input array.

        - **b**
          ([*array*](mlx.core.array.html#mlx.core.array "mlx.core.array"){.reference
          .internal}) -- Input array.

        - **stream**
          ([*Stream*](stream_class.html#mlx.core.Stream "mlx.core.Stream"){.reference
          .internal}*,* *optional*) -- Stream or device. Defaults to
          [`None`{.docutils .literal .notranslate}]{.pre} in which case
          the default stream of the default device is used.

    Returns[:]{.colon}

    :   The unique solution to the system [`AX`{.docutils .literal
        .notranslate}]{.pre}` `{.docutils .literal
        .notranslate}[`=`{.docutils .literal
        .notranslate}]{.pre}` `{.docutils .literal
        .notranslate}[`B`{.docutils .literal .notranslate}]{.pre}.

    Return type[:]{.colon}

    :   [*array*](mlx.core.array.html#mlx.core.array "mlx.core.array"){.reference
        .internal}
:::

::::: prev-next-area
[](mlx.core.linalg.pinv.html "previous page"){.left-prev}

::: prev-next-info
previous

mlx.core.linalg.pinv
:::

[](mlx.core.linalg.solve_triangular.html "next page"){.right-next}

::: prev-next-info
next

mlx.core.linalg.solve_triangular
:::
:::::
::::::::::::::::::::

:::::: {#pst-secondary-sidebar .bd-sidebar-secondary .bd-toc}
::::: {.sidebar-secondary-items .sidebar-secondary__inner}
:::: sidebar-secondary-item
::: {#pst-page-navigation-heading-2 .page-toc .tocsection .onthispage}
Contents
:::

- [[`solve()`{.docutils .literal
  .notranslate}]{.pre}](#mlx.core.linalg.solve){.reference .internal
  .nav-link}
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
