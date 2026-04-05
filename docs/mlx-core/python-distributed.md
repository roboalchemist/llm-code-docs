:::::::::::::::::::::::::::: {#main-content .bd-main role="main"}
::: sbt-scroll-pixel-helper
:::

::::::::::::::::::::: bd-content
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
  [.rst]{.btn__text-container}](../_sources/python/distributed.rst "Download source file"){.btn
  .btn-sm .btn-download-source-button .dropdown-item target="_blank"
  bs-placement="left" bs-toggle="tooltip"}
- [ ]{.btn__icon-container} [.pdf]{.btn__text-container}
:::

[ ]{.btn__icon-container}
::::
:::::
::::::
:::::::::
::::::::::

::::: {#jb-print-docs-body .onlyprint}
# Distributed Communication

:::: {#print-main-content}
::: {#jb-print-toc}
:::
::::
:::::

::: {#searchbox}
:::

:::: {#distributed-communication .section}
[]{#distributed}

# Distributed Communication[\#](#distributed-communication "Link to this heading"){.headerlink}

MLX provides a distributed communication package using MPI. The MPI
library is loaded at runtime; if MPI is available then distributed
communication is also made available.

::: pst-scrollable-table-container
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [[`Group`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.distributed.Group.html#mlx.core.distributed.Group "mlx.core.distributed.Group"){.reference .internal}                                                  An [[`mlx.core.distributed.Group`{.xref .py .py-class .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.distributed.Group.html#mlx.core.distributed.Group "mlx.core.distributed.Group"){.reference .internal} represents a group of independent mlx processes that can communicate.
  [[`is_available`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.distributed.is_available.html#mlx.core.distributed.is_available "mlx.core.distributed.is_available"){.reference .internal}(\[backend\])         Check if a communication backend is available.
  [[`init`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.distributed.init.html#mlx.core.distributed.init "mlx.core.distributed.init"){.reference .internal}(\[strict, backend\])                                 Initialize the communication backend and create the global communication group.
  [[`all_sum`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.distributed.all_sum.html#mlx.core.distributed.all_sum "mlx.core.distributed.all_sum"){.reference .internal}(x, \*\[, group, stream\])                All reduce sum.
  [[`all_gather`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.distributed.all_gather.html#mlx.core.distributed.all_gather "mlx.core.distributed.all_gather"){.reference .internal}(x, \*\[, group, stream\])    Gather arrays from all processes.
  [[`send`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.distributed.send.html#mlx.core.distributed.send "mlx.core.distributed.send"){.reference .internal}(x, dst, \*\[, group, stream\])                       Send an array from the current process to the process that has rank [`dst`{.docutils .literal .notranslate}]{.pre} in the group.
  [[`recv`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.distributed.recv.html#mlx.core.distributed.recv "mlx.core.distributed.recv"){.reference .internal}(shape, dtype, src, \*\[, group, stream\])            Recv an array with shape [`shape`{.docutils .literal .notranslate}]{.pre} and dtype [`dtype`{.docutils .literal .notranslate}]{.pre} from process with rank [`src`{.docutils .literal .notranslate}]{.pre}.
  [[`recv_like`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.distributed.recv_like.html#mlx.core.distributed.recv_like "mlx.core.distributed.recv_like"){.reference .internal}(x, src, \*\[, group, stream\])   Recv an array with shape and type like [`x`{.docutils .literal .notranslate}]{.pre} from process with rank [`src`{.docutils .literal .notranslate}]{.pre}.
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
:::
::::

::::: prev-next-area
[](_autosummary/mlx.optimizers.clip_grad_norm.html "previous page"){.left-prev}

::: prev-next-info
previous

mlx.optimizers.clip_grad_norm
:::

[](_autosummary/mlx.core.distributed.Group.html "next page"){.right-next}

::: prev-next-info
next

mlx.core.distributed.Group
:::
:::::
::::::::::::::::::::
:::::::::::::::::::::

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
::::::::::::::::::::::::::::
