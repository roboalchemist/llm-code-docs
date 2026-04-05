::::::::::::::::::::::::::::::::: {#main-content .bd-main role="main"}
::: sbt-scroll-pixel-helper
:::

:::::::::::::::::::::::::: bd-content
::::::::::::::::::::: bd-article-container
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
  [.rst]{.btn__text-container}](../_sources/usage/using_streams.rst "Download source file"){.btn
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

# Using Streams

::::: {#print-main-content}
:::: {#jb-print-toc}
::: {}

## Contents

:::

- [Specifying the [`Stream`{.xref .py .py-obj .docutils .literal
  .notranslate}]{.pre}](#specifying-the-stream){.reference .internal
  .nav-link}
::::
:::::
::::::

::: {#searchbox}
:::

:::: {#using-streams .section}
[]{#id1}

# Using Streams[\#](#using-streams "Link to this heading"){.headerlink}

::: {#specifying-the-stream .section}

## Specifying the [[`Stream`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](../python/_autosummary/stream_class.html#mlx.core.Stream "mlx.core.Stream"){.reference .internal}[\#](#specifying-the-stream "Link to this heading"){.headerlink}

All operations (including random number generation) take an optional
keyword argument [`stream`{.docutils .literal .notranslate}]{.pre}. The
[`stream`{.docutils .literal .notranslate}]{.pre} kwarg specifies which
[[`Stream`{.xref .py .py-obj .docutils .literal
.notranslate}]{.pre}](../python/_autosummary/stream_class.html#mlx.core.Stream "mlx.core.Stream"){.reference
.internal} the operation should run on. If the stream is unspecified
then the operation is run on the default stream of the default device:
[`mx.default_stream(mx.default_device())`{.docutils .literal
.notranslate}]{.pre}. The [`stream`{.docutils .literal
.notranslate}]{.pre} kwarg can also be a [[`Device`{.xref .py .py-obj
.docutils .literal
.notranslate}]{.pre}](../python/_autosummary/mlx.core.Device.html#mlx.core.Device "mlx.core.Device"){.reference
.internal} (e.g. [`stream=my_device`{.docutils .literal
.notranslate}]{.pre}) in which case the operation is run on the default
stream of the provided device [`mx.default_stream(my_device)`{.docutils
.literal .notranslate}]{.pre}.
:::
::::

::::: prev-next-area
[](distributed.html "previous page"){.left-prev}

::: prev-next-info
previous

Distributed Communication
:::

[](export.html "next page"){.right-next}

::: prev-next-info
next

Exporting Functions
:::
:::::
:::::::::::::::::::::

:::::: {#pst-secondary-sidebar .bd-sidebar-secondary .bd-toc}
::::: {.sidebar-secondary-items .sidebar-secondary__inner}
:::: sidebar-secondary-item
::: {#pst-page-navigation-heading-2 .page-toc .tocsection .onthispage}
Contents
:::

- [Specifying the [`Stream`{.xref .py .py-obj .docutils .literal
  .notranslate}]{.pre}](#specifying-the-stream){.reference .internal
  .nav-link}
::::
:::::
::::::
::::::::::::::::::::::::::

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
:::::::::::::::::::::::::::::::::
