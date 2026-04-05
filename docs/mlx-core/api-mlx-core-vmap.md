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
  [.rst]{.btn__text-container}](../../_sources/python/_autosummary/mlx.core.vmap.rst "Download source file"){.btn
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
# mlx.core.vmap

::::: {#print-main-content}
:::: {#jb-print-toc}
::: {}
## Contents
:::

- [[`vmap()`{.docutils .literal
  .notranslate}]{.pre}](#mlx.core.vmap){.reference .internal .nav-link}
::::
:::::
::::::

::: {#searchbox}
:::

::: {#mlx-core-vmap .section}
# mlx.core.vmap[\#](#mlx-core-vmap "Link to this heading"){.headerlink}

[[vmap]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[fun]{.pre}]{.n}[[:]{.pre}]{.p}[ ]{.w}[[Callable]{.pre}[[\[]{.pre}]{.p}[P]{.pre}[[,]{.pre}]{.p}[ ]{.w}[R]{.pre}[[\]]{.pre}]{.p}]{.n}*, *[[in_axes]{.pre}]{.n}[[:]{.pre}]{.p}[ ]{.w}[[[object]{.pre}](https://docs.python.org/3/library/functions.html#object "(in Python v3.14)"){.reference .external}]{.n}[ ]{.w}[[=]{.pre}]{.o}[ ]{.w}[[0]{.pre}]{.default_value}*, *[[out_axes]{.pre}]{.n}[[:]{.pre}]{.p}[ ]{.w}[[[object]{.pre}](https://docs.python.org/3/library/functions.html#object "(in Python v3.14)"){.reference .external}]{.n}[ ]{.w}[[=]{.pre}]{.o}[ ]{.w}[[0]{.pre}]{.default_value}*[)]{.sig-paren} [[→]{.sig-return-icon} [[Callable]{.pre}[[\[]{.pre}]{.p}[P]{.pre}[[,]{.pre}]{.p}[ ]{.w}[R]{.pre}[[\]]{.pre}]{.p}]{.sig-return-typehint}]{.sig-return}[\#](#mlx.core.vmap "Link to this definition"){.headerlink}

:   Returns a vectorized version of [`fun`{.docutils .literal
    .notranslate}]{.pre}.

    Parameters[:]{.colon}

    :   - **fun** (*Callable*) -- A function which takes a variable
          number of [[`array`{.xref .py .py-class .docutils .literal
          .notranslate}]{.pre}](mlx.core.array.html#mlx.core.array "mlx.core.array"){.reference
          .internal} or a tree of [[`array`{.xref .py .py-class
          .docutils .literal
          .notranslate}]{.pre}](mlx.core.array.html#mlx.core.array "mlx.core.array"){.reference
          .internal} and returns a variable number of [[`array`{.xref
          .py .py-class .docutils .literal
          .notranslate}]{.pre}](mlx.core.array.html#mlx.core.array "mlx.core.array"){.reference
          .internal} or a tree of [[`array`{.xref .py .py-class
          .docutils .literal
          .notranslate}]{.pre}](mlx.core.array.html#mlx.core.array "mlx.core.array"){.reference
          .internal}.

        - **in_axes**
          ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"){.reference
          .external}*,* *optional*) -- An integer or a valid prefix tree
          of the inputs to [`fun`{.docutils .literal
          .notranslate}]{.pre} where each node specifies the vmapped
          axis. If the value is [`None`{.docutils .literal
          .notranslate}]{.pre} then the corresponding input(s) are not
          vmapped. Defaults to [`0`{.docutils .literal
          .notranslate}]{.pre}.

        - **out_axes**
          ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"){.reference
          .external}*,* *optional*) -- An integer or a valid prefix tree
          of the outputs of [`fun`{.docutils .literal
          .notranslate}]{.pre} where each node specifies the vmapped
          axis. If the value is [`None`{.docutils .literal
          .notranslate}]{.pre} then the corresponding outputs(s) are not
          vmapped. Defaults to [`0`{.docutils .literal
          .notranslate}]{.pre}.

    Returns[:]{.colon}

    :   The vectorized function.

    Return type[:]{.colon}

    :   *Callable*
:::

::::: prev-next-area
[](mlx.core.vjp.html "previous page"){.left-prev}

::: prev-next-info
previous

mlx.core.vjp
:::

[](../fast.html "next page"){.right-next}

::: prev-next-info
next

Fast
:::
:::::
::::::::::::::::::::

:::::: {#pst-secondary-sidebar .bd-sidebar-secondary .bd-toc}
::::: {.sidebar-secondary-items .sidebar-secondary__inner}
:::: sidebar-secondary-item
::: {#pst-page-navigation-heading-2 .page-toc .tocsection .onthispage}
Contents
:::

- [[`vmap()`{.docutils .literal
  .notranslate}]{.pre}](#mlx.core.vmap){.reference .internal .nav-link}
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
