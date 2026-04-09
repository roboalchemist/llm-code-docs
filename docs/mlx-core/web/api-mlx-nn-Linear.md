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
  [.rst]{.btn__text-container}](../../../_sources/python/nn/_autosummary/mlx.nn.Linear.rst "Download source file"){.btn
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
# mlx.nn.Linear

::::: {#print-main-content}
:::: {#jb-print-toc}
::: {}
## Contents
:::

- [[`Linear`{.docutils .literal
  .notranslate}]{.pre}](#mlx.nn.Linear){.reference .internal .nav-link}
::::
:::::
::::::

::: {#searchbox}
:::

::: {#mlx-nn-linear .section}
# mlx.nn.Linear[\#](#mlx-nn-linear "Link to this heading"){.headerlink}

[[[class]{.pre}]{.k}[ ]{.w}]{.property}[[Linear]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[input_dims]{.pre}]{.n}[[:]{.pre}]{.p}[ ]{.w}[[[int]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"){.reference .external}]{.n}*, *[[output_dims]{.pre}]{.n}[[:]{.pre}]{.p}[ ]{.w}[[[int]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"){.reference .external}]{.n}*, *[[bias]{.pre}]{.n}[[:]{.pre}]{.p}[ ]{.w}[[[bool]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)"){.reference .external}]{.n}[ ]{.w}[[=]{.pre}]{.o}[ ]{.w}[[True]{.pre}]{.default_value}*[)]{.sig-paren}[\#](#mlx.nn.Linear "Link to this definition"){.headerlink}

:   Applies an affine transformation to the input.

    Concretely:

    ::: {.math .notranslate .nohighlight}
    \\\[y = x W\^\\top + b\\\]
    :::

    where: where [\\(W\\)]{.math .notranslate .nohighlight} has shape
    [`[output_dims,`{.docutils .literal
    .notranslate}]{.pre}` `{.docutils .literal
    .notranslate}[`input_dims]`{.docutils .literal .notranslate}]{.pre}
    and [\\(b\\)]{.math .notranslate .nohighlight} has shape
    [`[output_dims]`{.docutils .literal .notranslate}]{.pre}.

    The values are initialized from the uniform distribution
    [\\(\\mathcal{U}(-{k}, {k})\\)]{.math .notranslate .nohighlight},
    where [\\(k = \\frac{1}{\\sqrt{D_i}}\\)]{.math .notranslate
    .nohighlight} and [\\(D_i\\)]{.math .notranslate .nohighlight} is
    equal to [`input_dims`{.docutils .literal .notranslate}]{.pre}.

    Parameters[:]{.colon}

    :   - **input_dims**
          ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"){.reference
          .external}) -- The dimensionality of the input features

        - **output_dims**
          ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"){.reference
          .external}) -- The dimensionality of the output features

        - **bias**
          ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)"){.reference
          .external}*,* *optional*) -- If set to [`False`{.docutils
          .literal .notranslate}]{.pre} then the layer will not use a
          bias. Default is [`True`{.docutils .literal
          .notranslate}]{.pre}.

    Methods

    ::: pst-scrollable-table-container
      ------------------------------------------------------------------------------------------------------------- -------------------------------------------------
      [`to_quantized`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}(\[group_size, bits, mode, \...\])   Return a quantized approximation of this layer.
      ------------------------------------------------------------------------------------------------------------- -------------------------------------------------
    :::
:::

::::: prev-next-area
[](mlx.nn.LeakyReLU.html "previous page"){.left-prev}

::: prev-next-info
previous

mlx.nn.LeakyReLU
:::

[](mlx.nn.LogSigmoid.html "next page"){.right-next}

::: prev-next-info
next

mlx.nn.LogSigmoid
:::
:::::
::::::::::::::::::::

:::::: {#pst-secondary-sidebar .bd-sidebar-secondary .bd-toc}
::::: {.sidebar-secondary-items .sidebar-secondary__inner}
:::: sidebar-secondary-item
::: {#pst-page-navigation-heading-2 .page-toc .tocsection .onthispage}
Contents
:::

- [[`Linear`{.docutils .literal
  .notranslate}]{.pre}](#mlx.nn.Linear){.reference .internal .nav-link}
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
