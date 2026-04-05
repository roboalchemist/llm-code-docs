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
  [.rst]{.btn__text-container}](../_sources/python/transforms.rst "Download source file"){.btn
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
# Transforms

:::: {#print-main-content}
::: {#jb-print-toc}
:::
::::
:::::

::: {#searchbox}
:::

:::: {#transforms .section}
[]{#id1}

# Transforms[\#](#transforms "Link to this heading"){.headerlink}

::: pst-scrollable-table-container
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [[`eval`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.eval.html#mlx.core.eval "mlx.core.eval"){.reference .internal}(\*args)                                                               Evaluate an [[`array`{.xref .py .py-class .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.array.html#mlx.core.array "mlx.core.array"){.reference .internal} or tree of [[`array`{.xref .py .py-class .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.array.html#mlx.core.array "mlx.core.array"){.reference .internal}.
  [[`async_eval`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.async_eval.html#mlx.core.async_eval "mlx.core.async_eval"){.reference .internal}(\*args)                                       Asynchronously evaluate an [[`array`{.xref .py .py-class .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.array.html#mlx.core.array "mlx.core.array"){.reference .internal} or tree of [[`array`{.xref .py .py-class .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.array.html#mlx.core.array "mlx.core.array"){.reference .internal}.
  [[`compile`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.compile.html#mlx.core.compile "mlx.core.compile"){.reference .internal}(fun\[, inputs, outputs, shapeless\])                      Returns a compiled function which produces the same output as [`fun`{.docutils .literal .notranslate}]{.pre}.
  [[`checkpoint`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.checkpoint.html#mlx.core.checkpoint "mlx.core.checkpoint"){.reference .internal}(fun)                                          Transform the passed callable to one that performs gradient checkpointing with respect to the inputs of the callable.
  [[`custom_function`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.custom_function.html#mlx.core.custom_function "mlx.core.custom_function"){.reference .internal}(\*args, \*\*kwargs)       Set up a function for custom gradient and vmap definitions.
  [[`disable_compile`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.disable_compile.html#mlx.core.disable_compile "mlx.core.disable_compile"){.reference .internal}()                         Globally disable compilation.
  [[`enable_compile`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.enable_compile.html#mlx.core.enable_compile "mlx.core.enable_compile"){.reference .internal}()                             Globally enable compilation.
  [[`grad`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.grad.html#mlx.core.grad "mlx.core.grad"){.reference .internal}(fun\[, argnums, argnames\])                                           Returns a function which computes the gradient of [`fun`{.docutils .literal .notranslate}]{.pre}.
  [[`value_and_grad`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.value_and_grad.html#mlx.core.value_and_grad "mlx.core.value_and_grad"){.reference .internal}(fun\[, argnums, argnames\])   Returns a function which computes the value and gradient of [`fun`{.docutils .literal .notranslate}]{.pre}.
  [[`jvp`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.jvp.html#mlx.core.jvp "mlx.core.jvp"){.reference .internal}(fun, primals, tangents)                                                   Compute the Jacobian-vector product.
  [[`vjp`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.vjp.html#mlx.core.vjp "mlx.core.vjp"){.reference .internal}(fun, primals, cotangents)                                                 Compute the vector-Jacobian product.
  [[`vmap`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.vmap.html#mlx.core.vmap "mlx.core.vmap"){.reference .internal}(fun\[, in_axes, out_axes\])                                           Returns a vectorized version of [`fun`{.docutils .literal .notranslate}]{.pre}.
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
:::
::::

::::: prev-next-area
[](_autosummary/mlx.core.random.permutation.html "previous page"){.left-prev}

::: prev-next-info
previous

mlx.core.random.permutation
:::

[](_autosummary/mlx.core.eval.html "next page"){.right-next}

::: prev-next-info
next

mlx.core.eval
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
