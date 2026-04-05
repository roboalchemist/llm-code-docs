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
  [.rst]{.btn__text-container}](../_sources/python/ops.rst "Download source file"){.btn
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
# Operations

:::: {#print-main-content}
::: {#jb-print-toc}
:::
::::
:::::

::: {#searchbox}
:::

:::: {#operations .section}
[]{#ops}

# Operations[\#](#operations "Link to this heading"){.headerlink}

::: pst-scrollable-table-container
  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [[`abs`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.abs.html#mlx.core.abs "mlx.core.abs"){.reference .internal}(a, /, \*\[, stream\])                                                                     Element-wise absolute value.
  [[`add`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.add.html#mlx.core.add "mlx.core.add"){.reference .internal}(a, b\[, stream\])                                                                         Element-wise addition.
  [[`addmm`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.addmm.html#mlx.core.addmm "mlx.core.addmm"){.reference .internal}(c, a, b, /\[, alpha, beta, stream\])                                              Matrix multiplication with addition and optional scaling.
  [[`all`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.all.html#mlx.core.all "mlx.core.all"){.reference .internal}(a, /\[, axis, keepdims, stream\])                                                         An and reduction over the given axes.
  [[`allclose`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.allclose.html#mlx.core.allclose "mlx.core.allclose"){.reference .internal}(a, b, /\[, rtol, atol, equal_nan, \...\])                             Approximate comparison of two arrays.
  [[`any`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.any.html#mlx.core.any "mlx.core.any"){.reference .internal}(a, /\[, axis, keepdims, stream\])                                                         An or reduction over the given axes.
  [[`arange`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.arange.html#mlx.core.arange "mlx.core.arange"){.reference .internal}(-\> array)                                                                    Overloaded function.
  [[`arccos`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.arccos.html#mlx.core.arccos "mlx.core.arccos"){.reference .internal}(a, /, \*\[, stream\])                                                         Element-wise inverse cosine.
  [[`arccosh`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.arccosh.html#mlx.core.arccosh "mlx.core.arccosh"){.reference .internal}(a, /, \*\[, stream\])                                                     Element-wise inverse hyperbolic cosine.
  [[`arcsin`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.arcsin.html#mlx.core.arcsin "mlx.core.arcsin"){.reference .internal}(a, /, \*\[, stream\])                                                         Element-wise inverse sine.
  [[`arcsinh`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.arcsinh.html#mlx.core.arcsinh "mlx.core.arcsinh"){.reference .internal}(a, /, \*\[, stream\])                                                     Element-wise inverse hyperbolic sine.
  [[`arctan`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.arctan.html#mlx.core.arctan "mlx.core.arctan"){.reference .internal}(a, /, \*\[, stream\])                                                         Element-wise inverse tangent.
  [[`arctan2`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.arctan2.html#mlx.core.arctan2 "mlx.core.arctan2"){.reference .internal}(a, b, /, \*\[, stream\])                                                  Element-wise inverse tangent of the ratio of two arrays.
  [[`arctanh`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.arctanh.html#mlx.core.arctanh "mlx.core.arctanh"){.reference .internal}(a, /, \*\[, stream\])                                                     Element-wise inverse hyperbolic tangent.
  [[`argmax`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.argmax.html#mlx.core.argmax "mlx.core.argmax"){.reference .internal}(a, /\[, axis, keepdims, stream\])                                             Indices of the maximum values along the axis.
  [[`argmin`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.argmin.html#mlx.core.argmin "mlx.core.argmin"){.reference .internal}(a, /\[, axis, keepdims, stream\])                                             Indices of the minimum values along the axis.
  [[`argpartition`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.argpartition.html#mlx.core.argpartition "mlx.core.argpartition"){.reference .internal}(a, /, kth\[, axis, stream\])                          Returns the indices that partition the array.
  [[`argsort`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.argsort.html#mlx.core.argsort "mlx.core.argsort"){.reference .internal}(a, /\[, axis, stream\])                                                   Returns the indices that sort the array.
  [[`array_equal`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.array_equal.html#mlx.core.array_equal "mlx.core.array_equal"){.reference .internal}(a, b\[, equal_nan, stream\])                              Array equality check.
  [[`as_strided`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.as_strided.html#mlx.core.as_strided "mlx.core.as_strided"){.reference .internal}(a, /\[, shape, strides, offset, \...\])                       Create a view into the array with the given shape and strides.
  [[`atleast_1d`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.atleast_1d.html#mlx.core.atleast_1d "mlx.core.atleast_1d"){.reference .internal}(\*arys\[, stream\])                                           Convert all arrays to have at least one dimension.
  [[`atleast_2d`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.atleast_2d.html#mlx.core.atleast_2d "mlx.core.atleast_2d"){.reference .internal}(\*arys\[, stream\])                                           Convert all arrays to have at least two dimensions.
  [[`atleast_3d`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.atleast_3d.html#mlx.core.atleast_3d "mlx.core.atleast_3d"){.reference .internal}(\*arys\[, stream\])                                           Convert all arrays to have at least three dimensions.
  [[`bitwise_and`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.bitwise_and.html#mlx.core.bitwise_and "mlx.core.bitwise_and"){.reference .internal}(a, b\[, stream\])                                         Element-wise bitwise and.
  [[`bitwise_invert`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.bitwise_invert.html#mlx.core.bitwise_invert "mlx.core.bitwise_invert"){.reference .internal}(a\[, stream\])                                Element-wise bitwise inverse.
  [[`bitwise_or`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.bitwise_or.html#mlx.core.bitwise_or "mlx.core.bitwise_or"){.reference .internal}(a, b\[, stream\])                                             Element-wise bitwise or.
  [[`bitwise_xor`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.bitwise_xor.html#mlx.core.bitwise_xor "mlx.core.bitwise_xor"){.reference .internal}(a, b\[, stream\])                                         Element-wise bitwise xor.
  [[`block_masked_mm`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.block_masked_mm.html#mlx.core.block_masked_mm "mlx.core.block_masked_mm"){.reference .internal}(a, b, /\[, block_size, \...\])            Matrix multiplication with block masking.
  [[`broadcast_arrays`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.broadcast_arrays.html#mlx.core.broadcast_arrays "mlx.core.broadcast_arrays"){.reference .internal}(\*arrays\[, stream\])                 Broadcast arrays against one another.
  [[`broadcast_to`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.broadcast_to.html#mlx.core.broadcast_to "mlx.core.broadcast_to"){.reference .internal}(a, /, shape, \*\[, stream\])                          Broadcast an array to the given shape.
  [[`ceil`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.ceil.html#mlx.core.ceil "mlx.core.ceil"){.reference .internal}(a, /, \*\[, stream\])                                                                 Element-wise ceil.
  [[`clip`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.clip.html#mlx.core.clip "mlx.core.clip"){.reference .internal}(a, /, a_min, a_max, \*\[, stream\])                                                   Clip the values of the array between the given minimum and maximum.
  [[`concatenate`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.concatenate.html#mlx.core.concatenate "mlx.core.concatenate"){.reference .internal}(arrays\[, axis, stream\])                                 Concatenate the arrays along the given axis.
  [[`contiguous`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.contiguous.html#mlx.core.contiguous "mlx.core.contiguous"){.reference .internal}(a, /\[, allow_col_major, stream\])                            Force an array to be row contiguous.
  [[`conj`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.conj.html#mlx.core.conj "mlx.core.conj"){.reference .internal}(a, \*\[, stream\])                                                                    Return the elementwise complex conjugate of the input.
  [[`conjugate`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.conjugate.html#mlx.core.conjugate "mlx.core.conjugate"){.reference .internal}(a, \*\[, stream\])                                                Return the elementwise complex conjugate of the input.
  [[`convolve`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.convolve.html#mlx.core.convolve "mlx.core.convolve"){.reference .internal}(a, v, /\[, mode, stream\])                                            The discrete convolution of 1D arrays.
  [[`conv1d`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.conv1d.html#mlx.core.conv1d "mlx.core.conv1d"){.reference .internal}(input, weight, /\[, stride, padding, \...\])                                  1D convolution over an input with several channels
  [[`conv2d`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.conv2d.html#mlx.core.conv2d "mlx.core.conv2d"){.reference .internal}(input, weight, /\[, stride, padding, \...\])                                  2D convolution over an input with several channels
  [[`conv3d`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.conv3d.html#mlx.core.conv3d "mlx.core.conv3d"){.reference .internal}(input, weight, /\[, stride, padding, \...\])                                  3D convolution over an input with several channels
  [[`conv_transpose1d`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.conv_transpose1d.html#mlx.core.conv_transpose1d "mlx.core.conv_transpose1d"){.reference .internal}(input, weight, /\[, stride, \...\])   1D transposed convolution over an input with several channels
  [[`conv_transpose2d`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.conv_transpose2d.html#mlx.core.conv_transpose2d "mlx.core.conv_transpose2d"){.reference .internal}(input, weight, /\[, stride, \...\])   2D transposed convolution over an input with several channels
  [[`conv_transpose3d`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.conv_transpose3d.html#mlx.core.conv_transpose3d "mlx.core.conv_transpose3d"){.reference .internal}(input, weight, /\[, stride, \...\])   3D transposed convolution over an input with several channels
  [[`conv_general`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.conv_general.html#mlx.core.conv_general "mlx.core.conv_general"){.reference .internal}(input, weight, /\[, stride, \...\])                   General convolution over an input with several channels
  [[`cos`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.cos.html#mlx.core.cos "mlx.core.cos"){.reference .internal}(a, /, \*\[, stream\])                                                                     Element-wise cosine.
  [[`cosh`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.cosh.html#mlx.core.cosh "mlx.core.cosh"){.reference .internal}(a, /, \*\[, stream\])                                                                 Element-wise hyperbolic cosine.
  [[`cummax`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.cummax.html#mlx.core.cummax "mlx.core.cummax"){.reference .internal}(a, /\[, axis, reverse, inclusive, stream\])                                   Return the cumulative maximum of the elements along the given axis.
  [[`cummin`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.cummin.html#mlx.core.cummin "mlx.core.cummin"){.reference .internal}(a, /\[, axis, reverse, inclusive, stream\])                                   Return the cumulative minimum of the elements along the given axis.
  [[`cumprod`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.cumprod.html#mlx.core.cumprod "mlx.core.cumprod"){.reference .internal}(a, /\[, axis, reverse, inclusive, stream\])                               Return the cumulative product of the elements along the given axis.
  [[`cumsum`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.cumsum.html#mlx.core.cumsum "mlx.core.cumsum"){.reference .internal}(a, /\[, axis, reverse, inclusive, stream\])                                   Return the cumulative sum of the elements along the given axis.
  [[`degrees`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.degrees.html#mlx.core.degrees "mlx.core.degrees"){.reference .internal}(a, /, \*\[, stream\])                                                     Convert angles from radians to degrees.
  [[`dequantize`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.dequantize.html#mlx.core.dequantize "mlx.core.dequantize"){.reference .internal}(w, /, scales\[, biases, \...\])                               Dequantize the matrix [`w`{.docutils .literal .notranslate}]{.pre} using quantization parameters.
  [[`diag`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.diag.html#mlx.core.diag "mlx.core.diag"){.reference .internal}(a, /\[, k, stream\])                                                                  Extract a diagonal or construct a diagonal matrix.
  [[`diagonal`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.diagonal.html#mlx.core.diagonal "mlx.core.diagonal"){.reference .internal}(a\[, offset, axis1, axis2, stream\])                                  Return specified diagonals.
  [[`divide`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.divide.html#mlx.core.divide "mlx.core.divide"){.reference .internal}(a, b\[, stream\])                                                             Element-wise division.
  [[`divmod`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.divmod.html#mlx.core.divmod "mlx.core.divmod"){.reference .internal}(a, b\[, stream\])                                                             Element-wise quotient and remainder.
  [[`einsum`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.einsum.html#mlx.core.einsum "mlx.core.einsum"){.reference .internal}(subscripts, \*operands\[, stream\])                                           Perform the Einstein summation convention on the operands.
  [[`einsum_path`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.einsum_path.html#mlx.core.einsum_path "mlx.core.einsum_path"){.reference .internal}(subscripts, \*operands)                                   Compute the contraction order for the given Einstein summation.
  [[`equal`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.equal.html#mlx.core.equal "mlx.core.equal"){.reference .internal}(a, b\[, stream\])                                                                 Element-wise equality.
  [[`erf`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.erf.html#mlx.core.erf "mlx.core.erf"){.reference .internal}(a, /, \*\[, stream\])                                                                     Element-wise error function.
  [[`erfinv`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.erfinv.html#mlx.core.erfinv "mlx.core.erfinv"){.reference .internal}(a, /, \*\[, stream\])                                                         Element-wise inverse of [[`erf()`{.xref .py .py-func .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.erf.html#mlx.core.erf "mlx.core.erf"){.reference .internal}.
  [[`exp`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.exp.html#mlx.core.exp "mlx.core.exp"){.reference .internal}(a, /, \*\[, stream\])                                                                     Element-wise exponential.
  [[`expm1`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.expm1.html#mlx.core.expm1 "mlx.core.expm1"){.reference .internal}(a, /, \*\[, stream\])                                                             Element-wise exponential minus 1.
  [[`expand_dims`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.expand_dims.html#mlx.core.expand_dims "mlx.core.expand_dims"){.reference .internal}(a, /, axis, \*\[, stream\])                               Add a size one dimension at the given axis.
  [[`eye`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.eye.html#mlx.core.eye "mlx.core.eye"){.reference .internal}(n\[, m, k, dtype, stream\])                                                               Create an identity matrix or a general diagonal matrix.
  [[`flatten`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.flatten.html#mlx.core.flatten "mlx.core.flatten"){.reference .internal}(a, /\[, start_axis, end_axis, stream\])                                   Flatten an array.
  [[`floor`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.floor.html#mlx.core.floor "mlx.core.floor"){.reference .internal}(a, /, \*\[, stream\])                                                             Element-wise floor.
  [[`floor_divide`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.floor_divide.html#mlx.core.floor_divide "mlx.core.floor_divide"){.reference .internal}(a, b\[, stream\])                                     Element-wise integer division.
  [[`full`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.full.html#mlx.core.full "mlx.core.full"){.reference .internal}(shape, vals\[, dtype, stream\])                                                       Construct an array with the given value.
  [[`gather_mm`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.gather_mm.html#mlx.core.gather_mm "mlx.core.gather_mm"){.reference .internal}(a, b, /, lhs_indices, rhs_indices, \*)                            Matrix multiplication with matrix-level gather.
  [[`gather_qmm`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.gather_qmm.html#mlx.core.gather_qmm "mlx.core.gather_qmm"){.reference .internal}(x, w, /, scales\[, biases, \...\])                            Perform quantized matrix multiplication with matrix-level gather.
  [[`greater`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.greater.html#mlx.core.greater "mlx.core.greater"){.reference .internal}(a, b\[, stream\])                                                         Element-wise greater than.
  [[`greater_equal`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.greater_equal.html#mlx.core.greater_equal "mlx.core.greater_equal"){.reference .internal}(a, b\[, stream\])                                 Element-wise greater or equal.
  [[`hadamard_transform`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.hadamard_transform.html#mlx.core.hadamard_transform "mlx.core.hadamard_transform"){.reference .internal}(a\[, scale, stream\])         Perform the Walsh-Hadamard transform along the final axis.
  [[`identity`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.identity.html#mlx.core.identity "mlx.core.identity"){.reference .internal}(n\[, dtype, stream\])                                                 Create a square identity matrix.
  [[`imag`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.imag.html#mlx.core.imag "mlx.core.imag"){.reference .internal}(a, /, \*\[, stream\])                                                                 Returns the imaginary part of a complex array.
  [[`inner`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.inner.html#mlx.core.inner "mlx.core.inner"){.reference .internal}(a, b, /, \*\[, stream\])                                                          Ordinary inner product of vectors for 1-D arrays, in higher dimensions a sum product over the last axes.
  [[`isfinite`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.isfinite.html#mlx.core.isfinite "mlx.core.isfinite"){.reference .internal}(a\[, stream\])                                                        Return a boolean array indicating which elements are finite.
  [[`isclose`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.isclose.html#mlx.core.isclose "mlx.core.isclose"){.reference .internal}(a, b, /\[, rtol, atol, equal_nan, stream\])                               Returns a boolean array where two arrays are element-wise equal within a tolerance.
  [[`isinf`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.isinf.html#mlx.core.isinf "mlx.core.isinf"){.reference .internal}(a\[, stream\])                                                                    Return a boolean array indicating which elements are +/- inifnity.
  [[`isnan`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.isnan.html#mlx.core.isnan "mlx.core.isnan"){.reference .internal}(a\[, stream\])                                                                    Return a boolean array indicating which elements are NaN.
  [[`isneginf`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.isneginf.html#mlx.core.isneginf "mlx.core.isneginf"){.reference .internal}(a\[, stream\])                                                        Return a boolean array indicating which elements are negative infinity.
  [[`isposinf`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.isposinf.html#mlx.core.isposinf "mlx.core.isposinf"){.reference .internal}(a\[, stream\])                                                        Return a boolean array indicating which elements are positive infinity.
  [[`issubdtype`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.issubdtype.html#mlx.core.issubdtype "mlx.core.issubdtype"){.reference .internal}(arg1, arg2)                                                   Check if a [[`Dtype`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.Dtype.html#mlx.core.Dtype "mlx.core.Dtype"){.reference .internal} or [[`DtypeCategory`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.DtypeCategory.html#mlx.core.DtypeCategory "mlx.core.DtypeCategory"){.reference .internal} is a subtype of another.
  [[`kron`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.kron.html#mlx.core.kron "mlx.core.kron"){.reference .internal}(a, b, \*\[, stream\])                                                                 Compute the Kronecker product of two arrays [`a`{.docutils .literal .notranslate}]{.pre} and [`b`{.docutils .literal .notranslate}]{.pre}.
  [[`left_shift`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.left_shift.html#mlx.core.left_shift "mlx.core.left_shift"){.reference .internal}(a, b\[, stream\])                                             Element-wise left shift.
  [[`less`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.less.html#mlx.core.less "mlx.core.less"){.reference .internal}(a, b\[, stream\])                                                                     Element-wise less than.
  [[`less_equal`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.less_equal.html#mlx.core.less_equal "mlx.core.less_equal"){.reference .internal}(a, b\[, stream\])                                             Element-wise less than or equal.
  [[`linspace`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.linspace.html#mlx.core.linspace "mlx.core.linspace"){.reference .internal}(start, stop\[, num, dtype, stream\])                                  Generate [`num`{.docutils .literal .notranslate}]{.pre} evenly spaced numbers over interval [`[start,`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`stop]`{.docutils .literal .notranslate}]{.pre}.
  [[`load`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.load.html#mlx.core.load "mlx.core.load"){.reference .internal}(file, /\[, format, return_metadata, stream\])                                         Load array(s) from a binary file.
  [[`log`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.log.html#mlx.core.log "mlx.core.log"){.reference .internal}(a, /, \*\[, stream\])                                                                     Element-wise natural logarithm.
  [[`log2`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.log2.html#mlx.core.log2 "mlx.core.log2"){.reference .internal}(a, /, \*\[, stream\])                                                                 Element-wise base-2 logarithm.
  [[`log10`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.log10.html#mlx.core.log10 "mlx.core.log10"){.reference .internal}(a, /, \*\[, stream\])                                                             Element-wise base-10 logarithm.
  [[`log1p`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.log1p.html#mlx.core.log1p "mlx.core.log1p"){.reference .internal}(a, /, \*\[, stream\])                                                             Element-wise natural log of one plus the array.
  [[`logaddexp`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.logaddexp.html#mlx.core.logaddexp "mlx.core.logaddexp"){.reference .internal}(a, b, /, \*\[, stream\])                                          Element-wise log-add-exp.
  [[`logcumsumexp`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.logcumsumexp.html#mlx.core.logcumsumexp "mlx.core.logcumsumexp"){.reference .internal}(a, /\[, axis, reverse, \...\])                        Return the cumulative logsumexp of the elements along the given axis.
  [[`logical_not`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.logical_not.html#mlx.core.logical_not "mlx.core.logical_not"){.reference .internal}(a, /, \*\[, stream\])                                     Element-wise logical not.
  [[`logical_and`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.logical_and.html#mlx.core.logical_and "mlx.core.logical_and"){.reference .internal}(a, b, /, \*\[, stream\])                                  Element-wise logical and.
  [[`logical_or`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.logical_or.html#mlx.core.logical_or "mlx.core.logical_or"){.reference .internal}(a, b, /, \*\[, stream\])                                      Element-wise logical or.
  [[`logsumexp`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.logsumexp.html#mlx.core.logsumexp "mlx.core.logsumexp"){.reference .internal}(a, /\[, axis, keepdims, stream\])                                 A log-sum-exp reduction over the given axes.
  [[`matmul`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.matmul.html#mlx.core.matmul "mlx.core.matmul"){.reference .internal}(a, b, /, \*\[, stream\])                                                      Matrix multiplication.
  [[`max`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.max.html#mlx.core.max "mlx.core.max"){.reference .internal}(a, /\[, axis, keepdims, stream\])                                                         A max reduction over the given axes.
  [[`maximum`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.maximum.html#mlx.core.maximum "mlx.core.maximum"){.reference .internal}(a, b, /, \*\[, stream\])                                                  Element-wise maximum.
  [[`mean`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.mean.html#mlx.core.mean "mlx.core.mean"){.reference .internal}(a, /\[, axis, keepdims, stream\])                                                     Compute the mean(s) over the given axes.
  [[`median`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.median.html#mlx.core.median "mlx.core.median"){.reference .internal}(a, /\[, axis, keepdims, stream\])                                             Compute the median(s) over the given axes.
  [[`meshgrid`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.meshgrid.html#mlx.core.meshgrid "mlx.core.meshgrid"){.reference .internal}(\*arrays\[, sparse, indexing, stream\])                               Generate multidimensional coordinate grids from 1-D coordinate arrays
  [[`min`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.min.html#mlx.core.min "mlx.core.min"){.reference .internal}(a, /\[, axis, keepdims, stream\])                                                         A min reduction over the given axes.
  [[`minimum`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.minimum.html#mlx.core.minimum "mlx.core.minimum"){.reference .internal}(a, b, /, \*\[, stream\])                                                  Element-wise minimum.
  [[`moveaxis`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.moveaxis.html#mlx.core.moveaxis "mlx.core.moveaxis"){.reference .internal}(a, /, source, destination, \*\[, stream\])                            Move an axis to a new position.
  [[`multiply`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.multiply.html#mlx.core.multiply "mlx.core.multiply"){.reference .internal}(a, b\[, stream\])                                                     Element-wise multiplication.
  [[`nan_to_num`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.nan_to_num.html#mlx.core.nan_to_num "mlx.core.nan_to_num"){.reference .internal}(a\[, nan, posinf, neginf, stream\])                           Replace NaN and Inf values with finite numbers.
  [[`negative`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.negative.html#mlx.core.negative "mlx.core.negative"){.reference .internal}(a, /, \*\[, stream\])                                                 Element-wise negation.
  [[`not_equal`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.not_equal.html#mlx.core.not_equal "mlx.core.not_equal"){.reference .internal}(a, b\[, stream\])                                                 Element-wise not equal.
  [[`ones`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.ones.html#mlx.core.ones "mlx.core.ones"){.reference .internal}(shape\[, dtype, stream\])                                                             Construct an array of ones.
  [[`ones_like`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.ones_like.html#mlx.core.ones_like "mlx.core.ones_like"){.reference .internal}(a, /, \*\[, stream\])                                             An array of ones like the input.
  [[`outer`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.outer.html#mlx.core.outer "mlx.core.outer"){.reference .internal}(a, b, /, \*\[, stream\])                                                          Compute the outer product of two 1-D arrays, if the array\'s passed are not 1-D a flatten op will be run beforehand.
  [[`partition`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.partition.html#mlx.core.partition "mlx.core.partition"){.reference .internal}(a, /, kth\[, axis, stream\])                                      Returns a partitioned copy of the array such that the smaller [`kth`{.docutils .literal .notranslate}]{.pre} elements are first.
  [[`pad`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.pad.html#mlx.core.pad "mlx.core.pad"){.reference .internal}(a, pad_width\[, mode, constant_values, \...\])                                            Pad an array with a constant value
  [[`power`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.power.html#mlx.core.power "mlx.core.power"){.reference .internal}(a, b, /, \*\[, stream\])                                                          Element-wise power operation.
  [[`prod`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.prod.html#mlx.core.prod "mlx.core.prod"){.reference .internal}(a, /\[, axis, keepdims, stream\])                                                     An product reduction over the given axes.
  [[`put_along_axis`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.put_along_axis.html#mlx.core.put_along_axis "mlx.core.put_along_axis"){.reference .internal}(a, /, indices, values\[, \...\])              Put values along an axis at the specified indices.
  [[`quantize`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.quantize.html#mlx.core.quantize "mlx.core.quantize"){.reference .internal}(w, /\[, group_size, bits, mode, \...\])                               Quantize the array [`w`{.docutils .literal .notranslate}]{.pre}.
  [[`quantized_matmul`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.quantized_matmul.html#mlx.core.quantized_matmul "mlx.core.quantized_matmul"){.reference .internal}(x, w, /, scales\[, biases, \...\])    Perform the matrix multiplication with the quantized matrix [`w`{.docutils .literal .notranslate}]{.pre}.
  [[`radians`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.radians.html#mlx.core.radians "mlx.core.radians"){.reference .internal}(a, /, \*\[, stream\])                                                     Convert angles from degrees to radians.
  [[`real`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.real.html#mlx.core.real "mlx.core.real"){.reference .internal}(a, /, \*\[, stream\])                                                                 Returns the real part of a complex array.
  [[`reciprocal`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.reciprocal.html#mlx.core.reciprocal "mlx.core.reciprocal"){.reference .internal}(a, /, \*\[, stream\])                                         Element-wise reciprocal.
  [[`remainder`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.remainder.html#mlx.core.remainder "mlx.core.remainder"){.reference .internal}(a, b\[, stream\])                                                 Element-wise remainder of division.
  [[`repeat`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.repeat.html#mlx.core.repeat "mlx.core.repeat"){.reference .internal}(array, repeats\[, axis, stream\])                                             Repeat an array along a specified axis.
  [[`reshape`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.reshape.html#mlx.core.reshape "mlx.core.reshape"){.reference .internal}(a, /, shape, \*\[, stream\])                                              Reshape an array while preserving the size.
  [[`right_shift`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.right_shift.html#mlx.core.right_shift "mlx.core.right_shift"){.reference .internal}(a, b\[, stream\])                                         Element-wise right shift.
  [[`roll`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.roll.html#mlx.core.roll "mlx.core.roll"){.reference .internal}(a, shift\[, axis, stream\])                                                           Roll array elements along a given axis.
  [[`round`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.round.html#mlx.core.round "mlx.core.round"){.reference .internal}(a, /\[, decimals, stream\])                                                       Round to the given number of decimals.
  [[`rsqrt`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.rsqrt.html#mlx.core.rsqrt "mlx.core.rsqrt"){.reference .internal}(a, /, \*\[, stream\])                                                             Element-wise reciprocal and square root.
  [[`save`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.save.html#mlx.core.save "mlx.core.save"){.reference .internal}(file, arr)                                                                            Save the array to a binary file in [`.npy`{.docutils .literal .notranslate}]{.pre} format.
  [[`savez`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.savez.html#mlx.core.savez "mlx.core.savez"){.reference .internal}(file, \*args, \*\*kwargs)                                                         Save several arrays to a binary file in uncompressed [`.npz`{.docutils .literal .notranslate}]{.pre} format.
  [[`savez_compressed`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.savez_compressed.html#mlx.core.savez_compressed "mlx.core.savez_compressed"){.reference .internal}(file, \*args, \*\*kwargs)             Save several arrays to a binary file in compressed [`.npz`{.docutils .literal .notranslate}]{.pre} format.
  [[`save_gguf`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.save_gguf.html#mlx.core.save_gguf "mlx.core.save_gguf"){.reference .internal}(file, arrays, metadata)                                           Save array(s) to a binary file in [`.gguf`{.docutils .literal .notranslate}]{.pre} format.
  [[`save_safetensors`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.save_safetensors.html#mlx.core.save_safetensors "mlx.core.save_safetensors"){.reference .internal}(file, arrays\[, metadata\])           Save array(s) to a binary file in [`.safetensors`{.docutils .literal .notranslate}]{.pre} format.
  [[`sigmoid`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.sigmoid.html#mlx.core.sigmoid "mlx.core.sigmoid"){.reference .internal}(a, /, \*\[, stream\])                                                     Element-wise logistic sigmoid.
  [[`sign`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.sign.html#mlx.core.sign "mlx.core.sign"){.reference .internal}(a, /, \*\[, stream\])                                                                 Element-wise sign.
  [[`sin`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.sin.html#mlx.core.sin "mlx.core.sin"){.reference .internal}(a, /, \*\[, stream\])                                                                     Element-wise sine.
  [[`sinh`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.sinh.html#mlx.core.sinh "mlx.core.sinh"){.reference .internal}(a, /, \*\[, stream\])                                                                 Element-wise hyperbolic sine.
  [[`slice`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.slice.html#mlx.core.slice "mlx.core.slice"){.reference .internal}(a, start_indices, axes, slice_size, \*)                                           Extract a sub-array from the input array.
  [[`slice_update`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.slice_update.html#mlx.core.slice_update "mlx.core.slice_update"){.reference .internal}(a, update, start_indices, axes, \*)                   Update a sub-array of the input array.
  [[`softmax`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.softmax.html#mlx.core.softmax "mlx.core.softmax"){.reference .internal}(a, /\[, axis, stream\])                                                   Perform the softmax along the given axis.
  [[`sort`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.sort.html#mlx.core.sort "mlx.core.sort"){.reference .internal}(a, /\[, axis, stream\])                                                               Returns a sorted copy of the array.
  [[`split`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.split.html#mlx.core.split "mlx.core.split"){.reference .internal}(a, /, indices_or_sections\[, axis, stream\])                                      Split an array along a given axis.
  [[`sqrt`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.sqrt.html#mlx.core.sqrt "mlx.core.sqrt"){.reference .internal}(a, /, \*\[, stream\])                                                                 Element-wise square root.
  [[`square`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.square.html#mlx.core.square "mlx.core.square"){.reference .internal}(a, /, \*\[, stream\])                                                         Element-wise square.
  [[`squeeze`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.squeeze.html#mlx.core.squeeze "mlx.core.squeeze"){.reference .internal}(a, /\[, axis, stream\])                                                   Remove length one axes from an array.
  [[`stack`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.stack.html#mlx.core.stack "mlx.core.stack"){.reference .internal}(arrays\[, axis, stream\])                                                         Stacks the arrays along a new axis.
  [[`std`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.std.html#mlx.core.std "mlx.core.std"){.reference .internal}(a, /\[, axis, keepdims, ddof, stream\])                                                   Compute the standard deviation(s) over the given axes.
  [[`stop_gradient`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.stop_gradient.html#mlx.core.stop_gradient "mlx.core.stop_gradient"){.reference .internal}(a, /, \*\[, stream\])                             Stop gradients from being computed.
  [[`subtract`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.subtract.html#mlx.core.subtract "mlx.core.subtract"){.reference .internal}(a, b\[, stream\])                                                     Element-wise subtraction.
  [[`sum`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.sum.html#mlx.core.sum "mlx.core.sum"){.reference .internal}(a, /\[, axis, keepdims, stream\])                                                         Sum reduce the array over the given axes.
  [[`swapaxes`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.swapaxes.html#mlx.core.swapaxes "mlx.core.swapaxes"){.reference .internal}(a, /, axis1, axis2, \*\[, stream\])                                   Swap two axes of an array.
  [[`take`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.take.html#mlx.core.take "mlx.core.take"){.reference .internal}(a, /, indices\[, axis, stream\])                                                      Take elements along an axis.
  [[`take_along_axis`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.take_along_axis.html#mlx.core.take_along_axis "mlx.core.take_along_axis"){.reference .internal}(a, /, indices\[, axis, stream\])          Take values along an axis at the specified indices.
  [[`tan`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.tan.html#mlx.core.tan "mlx.core.tan"){.reference .internal}(a, /, \*\[, stream\])                                                                     Element-wise tangent.
  [[`tanh`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.tanh.html#mlx.core.tanh "mlx.core.tanh"){.reference .internal}(a, /, \*\[, stream\])                                                                 Element-wise hyperbolic tangent.
  [[`tensordot`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.tensordot.html#mlx.core.tensordot "mlx.core.tensordot"){.reference .internal}(a, b, /\[, axes, stream\])                                        Compute the tensor dot product along the specified axes.
  [[`tile`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.tile.html#mlx.core.tile "mlx.core.tile"){.reference .internal}(a, reps, /, \*\[, stream\])                                                           Construct an array by repeating [`a`{.docutils .literal .notranslate}]{.pre} the number of times given by [`reps`{.docutils .literal .notranslate}]{.pre}.
  [[`topk`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.topk.html#mlx.core.topk "mlx.core.topk"){.reference .internal}(a, /, k\[, axis, stream\])                                                            Returns the [`k`{.docutils .literal .notranslate}]{.pre} largest elements from the input along a given axis.
  [[`trace`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.trace.html#mlx.core.trace "mlx.core.trace"){.reference .internal}(a, /\[, offset, axis1, axis2, dtype, \...\])                                      Return the sum along a specified diagonal in the given array.
  [[`transpose`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.transpose.html#mlx.core.transpose "mlx.core.transpose"){.reference .internal}(a, /\[, axes, stream\])                                           Transpose the dimensions of the array.
  [[`tri`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.tri.html#mlx.core.tri "mlx.core.tri"){.reference .internal}(n, m, k\[, dtype, stream\])                                                               An array with ones at and below the given diagonal and zeros elsewhere.
  [[`tril`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.tril.html#mlx.core.tril "mlx.core.tril"){.reference .internal}(x, k, \*\[, stream\])                                                                 Zeros the array above the given diagonal.
  [[`triu`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.triu.html#mlx.core.triu "mlx.core.triu"){.reference .internal}(x, k, \*\[, stream\])                                                                 Zeros the array below the given diagonal.
  [[`unflatten`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.unflatten.html#mlx.core.unflatten "mlx.core.unflatten"){.reference .internal}(a, /, axis, shape, \*\[, stream\])                                Unflatten an axis of an array to a shape.
  [[`var`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.var.html#mlx.core.var "mlx.core.var"){.reference .internal}(a, /\[, axis, keepdims, ddof, stream\])                                                   Compute the variance(s) over the given axes.
  [[`view`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.view.html#mlx.core.view "mlx.core.view"){.reference .internal}(a, dtype\[, stream\])                                                                 View the array as a different type.
  [[`where`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.where.html#mlx.core.where "mlx.core.where"){.reference .internal}(condition, x, y, /, \*\[, stream\])                                               Select from [`x`{.docutils .literal .notranslate}]{.pre} or [`y`{.docutils .literal .notranslate}]{.pre} according to [`condition`{.docutils .literal .notranslate}]{.pre}.
  [[`zeros`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.zeros.html#mlx.core.zeros "mlx.core.zeros"){.reference .internal}(shape\[, dtype, stream\])                                                         Construct an array of zeros.
  [[`zeros_like`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.zeros_like.html#mlx.core.zeros_like "mlx.core.zeros_like"){.reference .internal}(a, /, \*\[, stream\])                                         An array of zeros like the input.
  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
:::
::::

::::: prev-next-area
[](_autosummary/mlx.core.export_to_dot.html "previous page"){.left-prev}

::: prev-next-info
previous

mlx.core.export_to_dot
:::

[](_autosummary/mlx.core.abs.html "next page"){.right-next}

::: prev-next-info
next

mlx.core.abs
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
