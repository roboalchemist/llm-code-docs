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
  [.rst]{.btn__text-container}](../../_sources/python/_autosummary/mlx.core.grad.rst "Download source file"){.btn
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
# mlx.core.grad

::::: {#print-main-content}
:::: {#jb-print-toc}
::: {}
## Contents
:::

- [[`grad()`{.docutils .literal
  .notranslate}]{.pre}](#mlx.core.grad){.reference .internal .nav-link}
::::
:::::
::::::

::: {#searchbox}
:::

::: {#mlx-core-grad .section}
# mlx.core.grad[\#](#mlx-core-grad "Link to this heading"){.headerlink}

[[grad]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[fun]{.pre}]{.n}[[:]{.pre}]{.p}[ ]{.w}[[Callable]{.pre}[[\[]{.pre}]{.p}[P]{.pre}[[,]{.pre}]{.p}[ ]{.w}[R]{.pre}[[\]]{.pre}]{.p}]{.n}*, *[[argnums]{.pre}]{.n}[[:]{.pre}]{.p}[ ]{.w}[[[int]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"){.reference .external}[ ]{.w}[[\|]{.pre}]{.p}[ ]{.w}[Sequence]{.pre}[[\[]{.pre}]{.p}[[int]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"){.reference .external}[[\]]{.pre}]{.p}[ ]{.w}[[\|]{.pre}]{.p}[ ]{.w}[[None]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"){.reference .external}]{.n}[ ]{.w}[[=]{.pre}]{.o}[ ]{.w}[[None]{.pre}]{.default_value}*, *[[argnames]{.pre}]{.n}[[:]{.pre}]{.p}[ ]{.w}[[[str]{.pre}](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"){.reference .external}[ ]{.w}[[\|]{.pre}]{.p}[ ]{.w}[Sequence]{.pre}[[\[]{.pre}]{.p}[[str]{.pre}](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"){.reference .external}[[\]]{.pre}]{.p}]{.n}[ ]{.w}[[=]{.pre}]{.o}[ ]{.w}[[\[\]]{.pre}]{.default_value}*[)]{.sig-paren} [[→]{.sig-return-icon} [[Callable]{.pre}[[\[]{.pre}]{.p}[P]{.pre}[[,]{.pre}]{.p}[ ]{.w}[Any]{.pre}[[\]]{.pre}]{.p}]{.sig-return-typehint}]{.sig-return}[\#](#mlx.core.grad "Link to this definition"){.headerlink}

:   Returns a function which computes the gradient of [`fun`{.docutils
    .literal .notranslate}]{.pre}.

    Parameters[:]{.colon}

    :   - **fun** (*Callable*) -- A function which takes a variable
          number of [[`array`{.xref .py .py-class .docutils .literal
          .notranslate}]{.pre}](mlx.core.array.html#mlx.core.array "mlx.core.array"){.reference
          .internal} or trees of [[`array`{.xref .py .py-class .docutils
          .literal
          .notranslate}]{.pre}](mlx.core.array.html#mlx.core.array "mlx.core.array"){.reference
          .internal} and returns a scalar output [[`array`{.xref .py
          .py-class .docutils .literal
          .notranslate}]{.pre}](mlx.core.array.html#mlx.core.array "mlx.core.array"){.reference
          .internal}.

        - **argnums**
          ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"){.reference
          .external} *or*
          [*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)"){.reference
          .external}*(*[*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"){.reference
          .external}*),* *optional*) -- Specify the index (or indices)
          of the positional arguments of [`fun`{.docutils .literal
          .notranslate}]{.pre} to compute the gradient with respect to.
          If neither [`argnums`{.docutils .literal .notranslate}]{.pre}
          nor [`argnames`{.docutils .literal .notranslate}]{.pre} are
          provided [`argnums`{.docutils .literal .notranslate}]{.pre}
          defaults to [`0`{.docutils .literal .notranslate}]{.pre}
          indicating [`fun`{.docutils .literal .notranslate}]{.pre}'s
          first argument.

        - **argnames**
          ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"){.reference
          .external} *or*
          [*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)"){.reference
          .external}*(*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"){.reference
          .external}*),* *optional*) -- Specify keyword arguments of
          [`fun`{.docutils .literal .notranslate}]{.pre} to compute
          gradients with respect to. It defaults to \[\] so no gradients
          for keyword arguments by default.

    Returns[:]{.colon}

    :   A function which has the same input arguments as
        [`fun`{.docutils .literal .notranslate}]{.pre} and returns the
        gradient(s).

    Return type[:]{.colon}

    :   *Callable*
:::

::::: prev-next-area
[](mlx.core.enable_compile.html "previous page"){.left-prev}

::: prev-next-info
previous

mlx.core.enable_compile
:::

[](mlx.core.value_and_grad.html "next page"){.right-next}

::: prev-next-info
next

mlx.core.value_and_grad
:::
:::::
::::::::::::::::::::

:::::: {#pst-secondary-sidebar .bd-sidebar-secondary .bd-toc}
::::: {.sidebar-secondary-items .sidebar-secondary__inner}
:::: sidebar-secondary-item
::: {#pst-page-navigation-heading-2 .page-toc .tocsection .onthispage}
Contents
:::

- [[`grad()`{.docutils .literal
  .notranslate}]{.pre}](#mlx.core.grad){.reference .internal .nav-link}
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
