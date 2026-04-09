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
  [.rst]{.btn__text-container}](../../_sources/python/_autosummary/mlx.core.linalg.eig.rst "Download source file"){.btn
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
# mlx.core.linalg.eig

::::: {#print-main-content}
:::: {#jb-print-toc}
::: {}
## Contents
:::

- [[`eig()`{.docutils .literal
  .notranslate}]{.pre}](#mlx.core.linalg.eig){.reference .internal
  .nav-link}
::::
:::::
::::::

::: {#searchbox}
:::

::: {#mlx-core-linalg-eig .section}
# mlx.core.linalg.eig[\#](#mlx-core-linalg-eig "Link to this heading"){.headerlink}

[[eig]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[a]{.pre}]{.n}[[:]{.pre}]{.p}[ ]{.w}[[[array]{.pre}](mlx.core.array.html#mlx.core.array "mlx.core.array"){.reference .internal}]{.n}*, *[[[\*]{.pre}]{.abbr title="Keyword-only parameters separator (PEP 3102)"}]{.keyword-only-separator .o}*, *[[stream]{.pre}]{.n}[[:]{.pre}]{.p}[ ]{.w}[[[None]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"){.reference .external}[ ]{.w}[[\|]{.pre}]{.p}[ ]{.w}[[Stream]{.pre}](stream_class.html#mlx.core.Stream "mlx.core.Stream"){.reference .internal}[ ]{.w}[[\|]{.pre}]{.p}[ ]{.w}[[Device]{.pre}](mlx.core.Device.html#mlx.core.Device "mlx.core.Device"){.reference .internal}]{.n}[ ]{.w}[[=]{.pre}]{.o}[ ]{.w}[[None]{.pre}]{.default_value}*[)]{.sig-paren} [[→]{.sig-return-icon} [[Tuple]{.pre}[[\[]{.pre}]{.p}[[array]{.pre}](mlx.core.array.html#mlx.core.array "mlx.core.array"){.reference .internal}[[,]{.pre}]{.p}[ ]{.w}[[array]{.pre}](mlx.core.array.html#mlx.core.array "mlx.core.array"){.reference .internal}[[\]]{.pre}]{.p}]{.sig-return-typehint}]{.sig-return}[\#](#mlx.core.linalg.eig "Link to this definition"){.headerlink}

:   Compute the eigenvalues and eigenvectors of a square matrix.

    This function differs from [[`numpy.linalg.eig()`{.xref .py .py-func
    .docutils .literal
    .notranslate}]{.pre}](https://numpy.org/doc/stable/reference/generated/numpy.linalg.eig.html#numpy.linalg.eig "(in NumPy v2.4)"){.reference
    .external} in that the return type is always complex even if the
    eigenvalues are all real.

    This function supports arrays with at least 2 dimensions. When the
    input has more than two dimensions, the eigenvalues and eigenvectors
    are computed for each matrix in the last two dimensions.

    Parameters[:]{.colon}

    :   - **a**
          ([*array*](mlx.core.array.html#mlx.core.array "mlx.core.array"){.reference
          .internal}) -- The input array.

        - **stream**
          ([*Stream*](stream_class.html#mlx.core.Stream "mlx.core.Stream"){.reference
          .internal}*,* *optional*) -- Stream or device. Defaults to
          [`None`{.docutils .literal .notranslate}]{.pre} in which case
          the default stream of the default device is used.

    Returns[:]{.colon}

    :   A tuple containing the eigenvalues and the normalized right
        eigenvectors. The column [`v[:,`{.docutils .literal
        .notranslate}]{.pre}` `{.docutils .literal
        .notranslate}[`i]`{.docutils .literal .notranslate}]{.pre} is
        the eigenvector corresponding to the i-th eigenvalue.

    Return type[:]{.colon}

    :   *Tuple*\[[*array*](mlx.core.array.html#mlx.core.array "mlx.core.array"){.reference
        .internal},
        [*array*](mlx.core.array.html#mlx.core.array "mlx.core.array"){.reference
        .internal}\]

    Example

    :::: {.doctest .highlight-default .notranslate}
    ::: highlight
        >>> A = mx.array([[1., -2.], [-2., 1.]])
        >>> w, v = mx.linalg.eig(A, stream=mx.cpu)
        >>> w
        array([3+0j, -1+0j], dtype=complex64)
        >>> v
        array([[0.707107+0j, 0.707107+0j],
               [-0.707107+0j, 0.707107+0j]], dtype=complex64)
    :::
    ::::
:::

::::: prev-next-area
[](mlx.core.linalg.eigvals.html "previous page"){.left-prev}

::: prev-next-info
previous

mlx.core.linalg.eigvals
:::

[](mlx.core.linalg.eigvalsh.html "next page"){.right-next}

::: prev-next-info
next

mlx.core.linalg.eigvalsh
:::
:::::
::::::::::::::::::::

:::::: {#pst-secondary-sidebar .bd-sidebar-secondary .bd-toc}
::::: {.sidebar-secondary-items .sidebar-secondary__inner}
:::: sidebar-secondary-item
::: {#pst-page-navigation-heading-2 .page-toc .tocsection .onthispage}
Contents
:::

- [[`eig()`{.docutils .literal
  .notranslate}]{.pre}](#mlx.core.linalg.eig){.reference .internal
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
