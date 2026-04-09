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
  [.rst]{.btn__text-container}](../_sources/python/fast.rst "Download source file"){.btn
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

# Fast

:::: {#print-main-content}
::: {#jb-print-toc}
:::
::::
:::::

::: {#searchbox}
:::

:::: {#fast .section}
[]{#id1}

# Fast[\#](#fast "Link to this heading"){.headerlink}

::: pst-scrollable-table-container
  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [[`rms_norm`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.fast.rms_norm.html#mlx.core.fast.rms_norm "mlx.core.fast.rms_norm"){.reference .internal}(x, weight, eps, \*\[, stream\])                                                                       Root Mean Square normalization (RMS norm).
  [[`layer_norm`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.fast.layer_norm.html#mlx.core.fast.layer_norm "mlx.core.fast.layer_norm"){.reference .internal}(x, weight, bias, eps, \*\[, stream\])                                                         Layer normalization.
  [[`rope`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.fast.rope.html#mlx.core.fast.rope "mlx.core.fast.rope"){.reference .internal}(a, dims, \*, traditional, base, scale, \...)                                                                          Apply rotary positional encoding to the input.
  [[`scaled_dot_product_attention`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.fast.scaled_dot_product_attention.html#mlx.core.fast.scaled_dot_product_attention "mlx.core.fast.scaled_dot_product_attention"){.reference .internal}(q, k, v, \*, scale)   A fast implementation of multi-head attention: [`O`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`=`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`softmax(Q`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`@`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`K.T,`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`dim=-1)`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`@`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`V`{.docutils .literal .notranslate}]{.pre}.
  [[`metal_kernel`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.fast.metal_kernel.html#mlx.core.fast.metal_kernel "mlx.core.fast.metal_kernel"){.reference .internal}(name, input_names, \...\[, \...\])                                                    A jit-compiled custom Metal kernel defined from a source string.
  [[`cuda_kernel`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.fast.cuda_kernel.html#mlx.core.fast.cuda_kernel "mlx.core.fast.cuda_kernel"){.reference .internal}(name, input_names, output_names, \...)                                                    A jit-compiled custom CUDA kernel defined from a source string.
  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
:::
::::

::::: prev-next-area
[](_autosummary/mlx.core.vmap.html "previous page"){.left-prev}

::: prev-next-info
previous

mlx.core.vmap
:::

[](_autosummary/mlx.core.fast.rms_norm.html "next page"){.right-next}

::: prev-next-info
next

mlx.core.fast.rms_norm
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
