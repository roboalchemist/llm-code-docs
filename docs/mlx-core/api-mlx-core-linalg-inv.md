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
  [.rst]{.btn__text-container}](../../_sources/python/_autosummary/mlx.core.linalg.inv.rst "Download source file"){.btn
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
# mlx.core.linalg.inv

::::: {#print-main-content}
:::: {#jb-print-toc}
::: {}
## Contents
:::

- [[`inv()`{.docutils .literal
  .notranslate}]{.pre}](#mlx.core.linalg.inv){.reference .internal
  .nav-link}
::::
:::::
::::::

::: {#searchbox}
:::

::: {#mlx-core-linalg-inv .section}
# mlx.core.linalg.inv[\#](#mlx-core-linalg-inv "Link to this heading"){.headerlink}

[[inv]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[a]{.pre}]{.n}[[:]{.pre}]{.p}[ ]{.w}[[[array]{.pre}](mlx.core.array.html#mlx.core.array "mlx.core.array"){.reference .internal}]{.n}*, *[[[\*]{.pre}]{.abbr title="Keyword-only parameters separator (PEP 3102)"}]{.keyword-only-separator .o}*, *[[stream]{.pre}]{.n}[[:]{.pre}]{.p}[ ]{.w}[[[None]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"){.reference .external}[ ]{.w}[[\|]{.pre}]{.p}[ ]{.w}[[Stream]{.pre}](stream_class.html#mlx.core.Stream "mlx.core.Stream"){.reference .internal}[ ]{.w}[[\|]{.pre}]{.p}[ ]{.w}[[Device]{.pre}](mlx.core.Device.html#mlx.core.Device "mlx.core.Device"){.reference .internal}]{.n}[ ]{.w}[[=]{.pre}]{.o}[ ]{.w}[[None]{.pre}]{.default_value}*[)]{.sig-paren} [[→]{.sig-return-icon} [[[array]{.pre}](mlx.core.array.html#mlx.core.array "mlx.core.array"){.reference .internal}]{.sig-return-typehint}]{.sig-return}[\#](#mlx.core.linalg.inv "Link to this definition"){.headerlink}

:   Compute the inverse of a square matrix.

    This function supports arrays with at least 2 dimensions. When the
    input has more than two dimensions, the inverse is computed for each
    matrix in the last two dimensions of [`a`{.docutils .literal
    .notranslate}]{.pre}.

    Parameters[:]{.colon}

    :   - **a**
          ([*array*](mlx.core.array.html#mlx.core.array "mlx.core.array"){.reference
          .internal}) -- Input array.

        - **stream**
          ([*Stream*](stream_class.html#mlx.core.Stream "mlx.core.Stream"){.reference
          .internal}*,* *optional*) -- Stream or device. Defaults to
          [`None`{.docutils .literal .notranslate}]{.pre} in which case
          the default stream of the default device is used.

    Returns[:]{.colon}

    :   [`ainv`{.docutils .literal .notranslate}]{.pre} such that
        [`dot(a,`{.docutils .literal .notranslate}]{.pre}` `{.docutils
        .literal .notranslate}[`ainv)`{.docutils .literal
        .notranslate}]{.pre}` `{.docutils .literal
        .notranslate}[`=`{.docutils .literal
        .notranslate}]{.pre}` `{.docutils .literal
        .notranslate}[`dot(ainv,`{.docutils .literal
        .notranslate}]{.pre}` `{.docutils .literal
        .notranslate}[`a)`{.docutils .literal
        .notranslate}]{.pre}` `{.docutils .literal
        .notranslate}[`=`{.docutils .literal
        .notranslate}]{.pre}` `{.docutils .literal
        .notranslate}[`eye(a.shape[0])`{.docutils .literal
        .notranslate}]{.pre}

    Return type[:]{.colon}

    :   [*array*](mlx.core.array.html#mlx.core.array "mlx.core.array"){.reference
        .internal}
:::

::::: prev-next-area
[](../linalg.html "previous page"){.left-prev}

::: prev-next-info
previous

Linear Algebra
:::

[](mlx.core.linalg.tri_inv.html "next page"){.right-next}

::: prev-next-info
next

mlx.core.linalg.tri_inv
:::
:::::
::::::::::::::::::::

:::::: {#pst-secondary-sidebar .bd-sidebar-secondary .bd-toc}
::::: {.sidebar-secondary-items .sidebar-secondary__inner}
:::: sidebar-secondary-item
::: {#pst-page-navigation-heading-2 .page-toc .tocsection .onthispage}
Contents
:::

- [[`inv()`{.docutils .literal
  .notranslate}]{.pre}](#mlx.core.linalg.inv){.reference .internal
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
