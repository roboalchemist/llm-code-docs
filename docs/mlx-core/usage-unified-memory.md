::::::::::::::::::::::::::::::::::::::::::: {#main-content .bd-main role="main"}
::: sbt-scroll-pixel-helper
:::

:::::::::::::::::::::::::::::::::::: bd-content
::::::::::::::::::::::::::::::: bd-article-container
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
  [.rst]{.btn__text-container}](../_sources/usage/unified_memory.rst "Download source file"){.btn
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

# Unified Memory

::::: {#print-main-content}
:::: {#jb-print-toc}
::: {}

## Contents

:::

- [A Simple Example](#a-simple-example){.reference .internal .nav-link}
::::
:::::
::::::

::: {#searchbox}
:::

:::::::::::::: {#unified-memory .section}
[]{#id1}

# Unified Memory[\#](#unified-memory "Link to this heading"){.headerlink}

Apple silicon has a unified memory architecture. The CPU and GPU have
direct access to the same memory pool. MLX is designed to take advantage
of that.

Concretely, when you make an array in MLX you don't have to specify its
location:

:::: {.highlight-python .notranslate}
::: highlight
    a = mx.random.normal((100,))
    b = mx.random.normal((100,))
:::
::::

Both [`a`{.docutils .literal .notranslate}]{.pre} and [`b`{.docutils
.literal .notranslate}]{.pre} live in unified memory.

In MLX, rather than moving arrays to devices, you specify the device
when you run the operation. Any device can perform any operation on
[`a`{.docutils .literal .notranslate}]{.pre} and [`b`{.docutils .literal
.notranslate}]{.pre} without needing to move them from one memory
location to another. For example:

:::: {.highlight-python .notranslate}
::: highlight
    mx.add(a, b, stream=mx.cpu)
    mx.add(a, b, stream=mx.gpu)
:::
::::

In the above, both the CPU and the GPU will perform the same add
operation. The operations can (and likely will) be run in parallel since
there are no dependencies between them. See [[Using Streams]{.std
.std-ref}](using_streams.html#using-streams){.reference .internal} for
more information the semantics of streams in MLX.

In the above [`add`{.docutils .literal .notranslate}]{.pre} example,
there are no dependencies between operations, so there is no possibility
for race conditions. If there are dependencies, the MLX scheduler will
automatically manage them. For example:

:::: {.highlight-python .notranslate}
::: highlight
    c = mx.add(a, b, stream=mx.cpu)
    d = mx.add(a, c, stream=mx.gpu)
:::
::::

In the above case, the second [`add`{.docutils .literal
.notranslate}]{.pre} runs on the GPU but it depends on the output of the
first [`add`{.docutils .literal .notranslate}]{.pre} which is running on
the CPU. MLX will automatically insert a dependency between the two
streams so that the second [`add`{.docutils .literal
.notranslate}]{.pre} only starts executing after the first is complete
and [`c`{.docutils .literal .notranslate}]{.pre} is available.

::::::: {#a-simple-example .section}

## A Simple Example[\#](#a-simple-example "Link to this heading"){.headerlink}

Here is a more interesting (albeit slightly contrived example) of how
unified memory can be helpful. Suppose we have the following
computation:

:::: {.highlight-python .notranslate}
::: highlight
    def fun(a, b, d1, d2):
      x = mx.matmul(a, b, stream=d1)
      for _ in range(500):
          b = mx.exp(b, stream=d2)
      return x, b
:::
::::

which we want to run with the following arguments:

:::: {.highlight-python .notranslate}
::: highlight
    a = mx.random.uniform(shape=(4096, 512))
    b = mx.random.uniform(shape=(512, 4))
:::
::::

The first [`matmul`{.docutils .literal .notranslate}]{.pre} operation is
a good fit for the GPU since it's more compute dense. The second
sequence of operations are a better fit for the CPU, since they are very
small and would probably be overhead bound on the GPU.

If we time the computation fully on the GPU, we get 2.8 milliseconds.
But if we run the computation with [`d1=mx.gpu`{.docutils .literal
.notranslate}]{.pre} and [`d2=mx.cpu`{.docutils .literal
.notranslate}]{.pre}, then the time is only about 1.4 milliseconds,
about twice as fast. These times were measured on an M1 Max.
:::::::
::::::::::::::

::::: prev-next-area
[](lazy_evaluation.html "previous page"){.left-prev}

::: prev-next-info
previous

Lazy Evaluation
:::

[](indexing.html "next page"){.right-next}

::: prev-next-info
next

Indexing Arrays
:::
:::::
:::::::::::::::::::::::::::::::

:::::: {#pst-secondary-sidebar .bd-sidebar-secondary .bd-toc}
::::: {.sidebar-secondary-items .sidebar-secondary__inner}
:::: sidebar-secondary-item
::: {#pst-page-navigation-heading-2 .page-toc .tocsection .onthispage}
Contents
:::

- [A Simple Example](#a-simple-example){.reference .internal .nav-link}
::::
:::::
::::::
::::::::::::::::::::::::::::::::::::

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
:::::::::::::::::::::::::::::::::::::::::::
