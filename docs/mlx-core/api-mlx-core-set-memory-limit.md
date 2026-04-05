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
  [.rst]{.btn__text-container}](../../_sources/python/_autosummary/mlx.core.set_memory_limit.rst "Download source file"){.btn
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
# mlx.core.set_memory_limit

::::: {#print-main-content}
:::: {#jb-print-toc}
::: {}
## Contents
:::

- [[`set_memory_limit()`{.docutils .literal
  .notranslate}]{.pre}](#mlx.core.set_memory_limit){.reference .internal
  .nav-link}
::::
:::::
::::::

::: {#searchbox}
:::

::: {#mlx-core-set-memory-limit .section}
# mlx.core.set_memory_limit[\#](#mlx-core-set-memory-limit "Link to this heading"){.headerlink}

[[set_memory_limit]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[limit]{.pre}]{.n}[[:]{.pre}]{.p}[ ]{.w}[[[int]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"){.reference .external}]{.n}*[)]{.sig-paren} [[→]{.sig-return-icon} [[[int]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"){.reference .external}]{.sig-return-typehint}]{.sig-return}[\#](#mlx.core.set_memory_limit "Link to this definition"){.headerlink}

:   Set the memory limit.

    The memory limit is a guideline for the maximum amount of memory to
    use during graph evaluation. If the memory limit is exceeded and
    there is no more RAM (including swap when available) allocations
    will result in an exception.

    When metal is available the memory limit defaults to 1.5 times the
    maximum recommended working set size reported by the device.

    Parameters[:]{.colon}

    :   **limit**
        ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"){.reference
        .external}) -- Memory limit in bytes.

    Returns[:]{.colon}

    :   The previous memory limit in bytes.

    Return type[:]{.colon}

    :   [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"){.reference
        .external}
:::

::::: prev-next-area
[](mlx.core.get_cache_memory.html "previous page"){.left-prev}

::: prev-next-info
previous

mlx.core.get_cache_memory
:::

[](mlx.core.set_cache_limit.html "next page"){.right-next}

::: prev-next-info
next

mlx.core.set_cache_limit
:::
:::::
::::::::::::::::::::

:::::: {#pst-secondary-sidebar .bd-sidebar-secondary .bd-toc}
::::: {.sidebar-secondary-items .sidebar-secondary__inner}
:::: sidebar-secondary-item
::: {#pst-page-navigation-heading-2 .page-toc .tocsection .onthispage}
Contents
:::

- [[`set_memory_limit()`{.docutils .literal
  .notranslate}]{.pre}](#mlx.core.set_memory_limit){.reference .internal
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
