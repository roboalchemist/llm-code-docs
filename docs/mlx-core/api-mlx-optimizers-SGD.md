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
  [.rst]{.btn__text-container}](../../../_sources/python/optimizers/_autosummary/mlx.optimizers.SGD.rst "Download source file"){.btn
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
# mlx.optimizers.SGD

::::: {#print-main-content}
:::: {#jb-print-toc}
::: {}
## Contents
:::

- [[`SGD`{.docutils .literal
  .notranslate}]{.pre}](#mlx.optimizers.SGD){.reference .internal
  .nav-link}
::::
:::::
::::::

::: {#searchbox}
:::

::: {#mlx-optimizers-sgd .section}
# mlx.optimizers.SGD[\#](#mlx-optimizers-sgd "Link to this heading"){.headerlink}

[[[class]{.pre}]{.k}[ ]{.w}]{.property}[[SGD]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[learning_rate]{.pre}]{.n}[[:]{.pre}]{.p}[ ]{.w}[[[float]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)"){.reference .external}[ ]{.w}[[\|]{.pre}]{.p}[ ]{.w}[[Callable]{.pre}](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python v3.14)"){.reference .external}[[\[]{.pre}]{.p}[[\[]{.pre}]{.p}[[array]{.pre}](../../_autosummary/mlx.core.array.html#mlx.core.array "mlx.core.array"){.reference .internal}[[\]]{.pre}]{.p}[[,]{.pre}]{.p}[ ]{.w}[[array]{.pre}](../../_autosummary/mlx.core.array.html#mlx.core.array "mlx.core.array"){.reference .internal}[[\]]{.pre}]{.p}]{.n}*, *[[momentum]{.pre}]{.n}[[:]{.pre}]{.p}[ ]{.w}[[[float]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)"){.reference .external}]{.n}[ ]{.w}[[=]{.pre}]{.o}[ ]{.w}[[0.0]{.pre}]{.default_value}*, *[[weight_decay]{.pre}]{.n}[[:]{.pre}]{.p}[ ]{.w}[[[float]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)"){.reference .external}]{.n}[ ]{.w}[[=]{.pre}]{.o}[ ]{.w}[[0.0]{.pre}]{.default_value}*, *[[dampening]{.pre}]{.n}[[:]{.pre}]{.p}[ ]{.w}[[[float]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)"){.reference .external}]{.n}[ ]{.w}[[=]{.pre}]{.o}[ ]{.w}[[0.0]{.pre}]{.default_value}*, *[[nesterov]{.pre}]{.n}[[:]{.pre}]{.p}[ ]{.w}[[[bool]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)"){.reference .external}]{.n}[ ]{.w}[[=]{.pre}]{.o}[ ]{.w}[[False]{.pre}]{.default_value}*[)]{.sig-paren}[\#](#mlx.optimizers.SGD "Link to this definition"){.headerlink}

:   The stochastic gradient descent optimizer.

    Updates a parameter [\\(w\\)]{.math .notranslate .nohighlight} with
    a gradient [\\(g\\)]{.math .notranslate .nohighlight} as follows

    ::: {.math .notranslate .nohighlight}
    \\\[\\begin{split}v\_{t+1} &= \\mu v_t + (1 - \\tau) g_t \\\\
    w\_{t+1} &= w_t - \\lambda v\_{t+1}\\end{split}\\\]
    :::

    Parameters[:]{.colon}

    :   - **learning_rate**
          ([*float*](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)"){.reference
          .external} *or* *callable*) -- The learning rate
          [\\(\\lambda\\)]{.math .notranslate .nohighlight}.

        - **momentum**
          ([*float*](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)"){.reference
          .external}*,* *optional*) -- The momentum strength
          [\\(\\mu\\)]{.math .notranslate .nohighlight}. Default:
          [`0`{.docutils .literal .notranslate}]{.pre}

        - **weight_decay**
          ([*float*](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)"){.reference
          .external}*,* *optional*) -- The weight decay (L2 penalty).
          Default: [`0`{.docutils .literal .notranslate}]{.pre}

        - **dampening**
          ([*float*](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)"){.reference
          .external}*,* *optional*) -- Dampening for momentum
          [\\(\\tau\\)]{.math .notranslate .nohighlight}. Default:
          [`0`{.docutils .literal .notranslate}]{.pre}

        - **nesterov**
          ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)"){.reference
          .external}*,* *optional*) -- Enables Nesterov momentum.
          Default: [`False`{.docutils .literal .notranslate}]{.pre}

    Methods

    ::: pst-scrollable-table-container
      ---------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------
      [`__init__`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}(learning_rate\[, momentum, \...\])   
      [`apply_single`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}(gradient, parameter, state)      Performs the SGD parameter update and stores [\\(v\\)]{.math .notranslate .nohighlight} in the optimizer state.
      [`init_single`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}(parameter, state)                 Initialize optimizer state
      ---------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------
    :::
:::

::::: prev-next-area
[](../common_optimizers.html "previous page"){.left-prev}

::: prev-next-info
previous

Common Optimizers
:::

[](mlx.optimizers.RMSprop.html "next page"){.right-next}

::: prev-next-info
next

mlx.optimizers.RMSprop
:::
:::::
::::::::::::::::::::

:::::: {#pst-secondary-sidebar .bd-sidebar-secondary .bd-toc}
::::: {.sidebar-secondary-items .sidebar-secondary__inner}
:::: sidebar-secondary-item
::: {#pst-page-navigation-heading-2 .page-toc .tocsection .onthispage}
Contents
:::

- [[`SGD`{.docutils .literal
  .notranslate}]{.pre}](#mlx.optimizers.SGD){.reference .internal
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
