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
  [.rst]{.btn__text-container}](../../../_sources/python/optimizers/_autosummary/mlx.optimizers.Adam.rst "Download source file"){.btn
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
# mlx.optimizers.Adam

::::: {#print-main-content}
:::: {#jb-print-toc}
::: {}
## Contents
:::

- [[`Adam`{.docutils .literal
  .notranslate}]{.pre}](#mlx.optimizers.Adam){.reference .internal
  .nav-link}
::::
:::::
::::::

::: {#searchbox}
:::

::: {#mlx-optimizers-adam .section}
# mlx.optimizers.Adam[\#](#mlx-optimizers-adam "Link to this heading"){.headerlink}

[[[class]{.pre}]{.k}[ ]{.w}]{.property}[[Adam]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[learning_rate]{.pre}]{.n}[[:]{.pre}]{.p}[ ]{.w}[[[float]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)"){.reference .external}[ ]{.w}[[\|]{.pre}]{.p}[ ]{.w}[[Callable]{.pre}](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python v3.14)"){.reference .external}[[\[]{.pre}]{.p}[[\[]{.pre}]{.p}[[array]{.pre}](../../_autosummary/mlx.core.array.html#mlx.core.array "mlx.core.array"){.reference .internal}[[\]]{.pre}]{.p}[[,]{.pre}]{.p}[ ]{.w}[[array]{.pre}](../../_autosummary/mlx.core.array.html#mlx.core.array "mlx.core.array"){.reference .internal}[[\]]{.pre}]{.p}]{.n}*, *[[betas]{.pre}]{.n}[[:]{.pre}]{.p}[ ]{.w}[[[List]{.pre}](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)"){.reference .external}[[\[]{.pre}]{.p}[[float]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)"){.reference .external}[[\]]{.pre}]{.p}]{.n}[ ]{.w}[[=]{.pre}]{.o}[ ]{.w}[[\[0.9,]{.pre} [0.999\]]{.pre}]{.default_value}*, *[[eps]{.pre}]{.n}[[:]{.pre}]{.p}[ ]{.w}[[[float]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)"){.reference .external}]{.n}[ ]{.w}[[=]{.pre}]{.o}[ ]{.w}[[1e-08]{.pre}]{.default_value}*, *[[bias_correction]{.pre}]{.n}[[:]{.pre}]{.p}[ ]{.w}[[[bool]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)"){.reference .external}]{.n}[ ]{.w}[[=]{.pre}]{.o}[ ]{.w}[[False]{.pre}]{.default_value}*[)]{.sig-paren}[\#](#mlx.optimizers.Adam "Link to this definition"){.headerlink}

:   The Adam optimizer \[1\]. In detail,

    \[1\]: Kingma, D.P. and Ba, J., 2015. Adam: A method for stochastic
    optimization. ICLR 2015.

    ::: {.math .notranslate .nohighlight}
    \\\[\\begin{split}m\_{t+1} &= \\beta_1 m_t + (1 - \\beta_1) g_t \\\\
    v\_{t+1} &= \\beta_2 v_t + (1 - \\beta_2) g_t\^2 \\\\ w\_{t+1} &=
    w_t - \\lambda \\frac{m\_{t+1}}{\\sqrt{v\_{t+1}} +
    \\epsilon}\\end{split}\\\]
    :::

    Parameters[:]{.colon}

    :   - **learning_rate**
          ([*float*](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)"){.reference
          .external} *or* *callable*) -- The learning rate
          [\\(\\lambda\\)]{.math .notranslate .nohighlight}.

        - **betas**
          (*Tuple\[*[*float*](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)"){.reference
          .external}*,*
          [*float*](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)"){.reference
          .external}*\],* *optional*) -- The coefficients [\\((\\beta_1,
          \\beta_2)\\)]{.math .notranslate .nohighlight} used for
          computing running averages of the gradient and its square.
          Default: [`(0.9,`{.docutils .literal
          .notranslate}]{.pre}` `{.docutils .literal
          .notranslate}[`0.999)`{.docutils .literal .notranslate}]{.pre}

        - **eps**
          ([*float*](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)"){.reference
          .external}*,* *optional*) -- The term [\\(\\epsilon\\)]{.math
          .notranslate .nohighlight} added to the denominator to improve
          numerical stability. Default: [`1e-8`{.docutils .literal
          .notranslate}]{.pre}

        - **bias_correction**
          ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)"){.reference
          .external}*,* *optional*) -- If set to [`True`{.docutils
          .literal .notranslate}]{.pre}, bias correction is applied.
          Default: [`False`{.docutils .literal .notranslate}]{.pre}

    Methods

    ::: pst-scrollable-table-container
      ------------------------------------------------------------------------------------------------------------ -----------------------------------------------------------------------------------------------------------------------------------------------------------------
      [`__init__`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}(learning_rate\[, betas, eps, \...\])   
      [`apply_single`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}(gradient, parameter, state)        Performs the Adam parameter update and stores [\\(v\\)]{.math .notranslate .nohighlight} and [\\(m\\)]{.math .notranslate .nohighlight} in the optimizer state.
      [`init_single`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}(parameter, state)                   Initialize optimizer state
      ------------------------------------------------------------------------------------------------------------ -----------------------------------------------------------------------------------------------------------------------------------------------------------------
    :::
:::

::::: prev-next-area
[](mlx.optimizers.AdaDelta.html "previous page"){.left-prev}

::: prev-next-info
previous

mlx.optimizers.AdaDelta
:::

[](mlx.optimizers.AdamW.html "next page"){.right-next}

::: prev-next-info
next

mlx.optimizers.AdamW
:::
:::::
::::::::::::::::::::

:::::: {#pst-secondary-sidebar .bd-sidebar-secondary .bd-toc}
::::: {.sidebar-secondary-items .sidebar-secondary__inner}
:::: sidebar-secondary-item
::: {#pst-page-navigation-heading-2 .page-toc .tocsection .onthispage}
Contents
:::

- [[`Adam`{.docutils .literal
  .notranslate}]{.pre}](#mlx.optimizers.Adam){.reference .internal
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
