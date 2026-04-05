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
  [.rst]{.btn__text-container}](../_sources/python/array.rst "Download source file"){.btn
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
# Array

:::: {#print-main-content}
::: {#jb-print-toc}
:::
::::
:::::

::: {#searchbox}
:::

:::: {#array .section}
[]{#id1}

# Array[\#](#array "Link to this heading"){.headerlink}

::: pst-scrollable-table-container
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [[`array`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.array.html#mlx.core.array "mlx.core.array"){.reference .internal}(\*args, \*\*kwargs)                                                                  An N-dimensional array object.
  [[`array.astype`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.array.astype.html#mlx.core.array.astype "mlx.core.array.astype"){.reference .internal}(self, dtype\[, stream\])                                 Cast the array to a specified type.
  [[`array.at`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.array.at.html#mlx.core.array.at "mlx.core.array.at"){.reference .internal}                                                                          Used to apply updates at the given indices.
  [[`array.item`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.array.item.html#mlx.core.array.item "mlx.core.array.item"){.reference .internal}(self)                                                            Access the value of a scalar array.
  [[`array.tolist`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.array.tolist.html#mlx.core.array.tolist "mlx.core.array.tolist"){.reference .internal}(self)                                                    Convert the array to a Python [[`list`{.xref .py .py-class .docutils .literal .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)"){.reference .external}.
  [[`array.dtype`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.array.dtype.html#mlx.core.array.dtype "mlx.core.array.dtype"){.reference .internal}                                                              The array\'s [[`Dtype`{.xref .py .py-class .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.Dtype.html#mlx.core.Dtype "mlx.core.Dtype"){.reference .internal}.
  [[`array.itemsize`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.array.itemsize.html#mlx.core.array.itemsize "mlx.core.array.itemsize"){.reference .internal}                                                  The size of the array\'s datatype in bytes.
  [[`array.nbytes`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.array.nbytes.html#mlx.core.array.nbytes "mlx.core.array.nbytes"){.reference .internal}                                                          The number of bytes in the array.
  [[`array.ndim`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.array.ndim.html#mlx.core.array.ndim "mlx.core.array.ndim"){.reference .internal}                                                                  The array\'s dimension.
  [[`array.shape`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.array.shape.html#mlx.core.array.shape "mlx.core.array.shape"){.reference .internal}                                                              The shape of the array as a Python tuple.
  [[`array.size`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.array.size.html#mlx.core.array.size "mlx.core.array.size"){.reference .internal}                                                                  Number of elements in the array.
  [[`array.real`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.array.real.html#mlx.core.array.real "mlx.core.array.real"){.reference .internal}                                                                  The real part of a complex array.
  [[`array.imag`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.array.imag.html#mlx.core.array.imag "mlx.core.array.imag"){.reference .internal}                                                                  The imaginary part of a complex array.
  [[`array.abs`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.array.abs.html#mlx.core.array.abs "mlx.core.array.abs"){.reference .internal}(self, \*\[, stream\])                                                See [[`abs()`{.xref .py .py-func .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.abs.html#mlx.core.abs "mlx.core.abs"){.reference .internal}.
  [[`array.all`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.array.all.html#mlx.core.array.all "mlx.core.array.all"){.reference .internal}(self\[, axis, keepdims, stream\])                                    See [[`all()`{.xref .py .py-func .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.all.html#mlx.core.all "mlx.core.all"){.reference .internal}.
  [[`array.any`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.array.any.html#mlx.core.array.any "mlx.core.array.any"){.reference .internal}(self\[, axis, keepdims, stream\])                                    See [[`any()`{.xref .py .py-func .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.any.html#mlx.core.any "mlx.core.any"){.reference .internal}.
  [[`array.argmax`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.array.argmax.html#mlx.core.array.argmax "mlx.core.array.argmax"){.reference .internal}(self\[, axis, keepdims, stream\])                        See [[`argmax()`{.xref .py .py-func .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.argmax.html#mlx.core.argmax "mlx.core.argmax"){.reference .internal}.
  [[`array.argmin`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.array.argmin.html#mlx.core.array.argmin "mlx.core.array.argmin"){.reference .internal}(self\[, axis, keepdims, stream\])                        See [[`argmin()`{.xref .py .py-func .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.argmin.html#mlx.core.argmin "mlx.core.argmin"){.reference .internal}.
  [[`array.conj`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.array.conj.html#mlx.core.array.conj "mlx.core.array.conj"){.reference .internal}(self, \*\[, stream\])                                            See [[`conj()`{.xref .py .py-func .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.conj.html#mlx.core.conj "mlx.core.conj"){.reference .internal}.
  [[`array.cos`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.array.cos.html#mlx.core.array.cos "mlx.core.array.cos"){.reference .internal}(self, \*\[, stream\])                                                See [[`cos()`{.xref .py .py-func .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.cos.html#mlx.core.cos "mlx.core.cos"){.reference .internal}.
  [[`array.cummax`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.array.cummax.html#mlx.core.array.cummax "mlx.core.array.cummax"){.reference .internal}(self\[, axis, reverse, \...\])                           See [[`cummax()`{.xref .py .py-func .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.cummax.html#mlx.core.cummax "mlx.core.cummax"){.reference .internal}.
  [[`array.cummin`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.array.cummin.html#mlx.core.array.cummin "mlx.core.array.cummin"){.reference .internal}(self\[, axis, reverse, \...\])                           See [[`cummin()`{.xref .py .py-func .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.cummin.html#mlx.core.cummin "mlx.core.cummin"){.reference .internal}.
  [[`array.cumprod`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.array.cumprod.html#mlx.core.array.cumprod "mlx.core.array.cumprod"){.reference .internal}(self\[, axis, reverse, \...\])                       See [[`cumprod()`{.xref .py .py-func .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.cumprod.html#mlx.core.cumprod "mlx.core.cumprod"){.reference .internal}.
  [[`array.cumsum`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.array.cumsum.html#mlx.core.array.cumsum "mlx.core.array.cumsum"){.reference .internal}(self\[, axis, reverse, \...\])                           See [[`cumsum()`{.xref .py .py-func .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.cumsum.html#mlx.core.cumsum "mlx.core.cumsum"){.reference .internal}.
  [[`array.diag`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.array.diag.html#mlx.core.array.diag "mlx.core.array.diag"){.reference .internal}(self\[, k, stream\])                                             Extract a diagonal or construct a diagonal matrix.
  [[`array.diagonal`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.array.diagonal.html#mlx.core.array.diagonal "mlx.core.array.diagonal"){.reference .internal}(self\[, offset, axis1, axis2, \...\])            See [[`diagonal()`{.xref .py .py-func .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.diagonal.html#mlx.core.diagonal "mlx.core.diagonal"){.reference .internal}.
  [[`array.exp`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.array.exp.html#mlx.core.array.exp "mlx.core.array.exp"){.reference .internal}(self, \*\[, stream\])                                                See [[`exp()`{.xref .py .py-func .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.exp.html#mlx.core.exp "mlx.core.exp"){.reference .internal}.
  [[`array.flatten`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.array.flatten.html#mlx.core.array.flatten "mlx.core.array.flatten"){.reference .internal}(self\[, start_axis, end_axis, \...\])                See [[`flatten()`{.xref .py .py-func .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.flatten.html#mlx.core.flatten "mlx.core.flatten"){.reference .internal}.
  [[`array.log`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.array.log.html#mlx.core.array.log "mlx.core.array.log"){.reference .internal}(self, \*\[, stream\])                                                See [[`log()`{.xref .py .py-func .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.log.html#mlx.core.log "mlx.core.log"){.reference .internal}.
  [[`array.log10`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.array.log10.html#mlx.core.array.log10 "mlx.core.array.log10"){.reference .internal}(self, \*\[, stream\])                                        See [[`log10()`{.xref .py .py-func .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.log10.html#mlx.core.log10 "mlx.core.log10"){.reference .internal}.
  [[`array.log1p`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.array.log1p.html#mlx.core.array.log1p "mlx.core.array.log1p"){.reference .internal}(self, \*\[, stream\])                                        See [[`log1p()`{.xref .py .py-func .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.log1p.html#mlx.core.log1p "mlx.core.log1p"){.reference .internal}.
  [[`array.log2`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.array.log2.html#mlx.core.array.log2 "mlx.core.array.log2"){.reference .internal}(self, \*\[, stream\])                                            See [[`log2()`{.xref .py .py-func .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.log2.html#mlx.core.log2 "mlx.core.log2"){.reference .internal}.
  [[`array.logcumsumexp`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.array.logcumsumexp.html#mlx.core.array.logcumsumexp "mlx.core.array.logcumsumexp"){.reference .internal}(self\[, axis, reverse, \...\])   See [[`logcumsumexp()`{.xref .py .py-func .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.logcumsumexp.html#mlx.core.logcumsumexp "mlx.core.logcumsumexp"){.reference .internal}.
  [[`array.logsumexp`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.array.logsumexp.html#mlx.core.array.logsumexp "mlx.core.array.logsumexp"){.reference .internal}(self\[, axis, keepdims, stream\])            See [[`logsumexp()`{.xref .py .py-func .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.logsumexp.html#mlx.core.logsumexp "mlx.core.logsumexp"){.reference .internal}.
  [[`array.max`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.array.max.html#mlx.core.array.max "mlx.core.array.max"){.reference .internal}(self\[, axis, keepdims, stream\])                                    See [[`max()`{.xref .py .py-func .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.max.html#mlx.core.max "mlx.core.max"){.reference .internal}.
  [[`array.mean`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.array.mean.html#mlx.core.array.mean "mlx.core.array.mean"){.reference .internal}(self\[, axis, keepdims, stream\])                                See [[`mean()`{.xref .py .py-func .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.mean.html#mlx.core.mean "mlx.core.mean"){.reference .internal}.
  [[`array.min`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.array.min.html#mlx.core.array.min "mlx.core.array.min"){.reference .internal}(self\[, axis, keepdims, stream\])                                    See [[`min()`{.xref .py .py-func .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.min.html#mlx.core.min "mlx.core.min"){.reference .internal}.
  [[`array.moveaxis`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.array.moveaxis.html#mlx.core.array.moveaxis "mlx.core.array.moveaxis"){.reference .internal}(self, source, destination, \*)                   See [[`moveaxis()`{.xref .py .py-func .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.moveaxis.html#mlx.core.moveaxis "mlx.core.moveaxis"){.reference .internal}.
  [[`array.prod`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.array.prod.html#mlx.core.array.prod "mlx.core.array.prod"){.reference .internal}(self\[, axis, keepdims, stream\])                                See [[`prod()`{.xref .py .py-func .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.prod.html#mlx.core.prod "mlx.core.prod"){.reference .internal}.
  [[`array.reciprocal`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.array.reciprocal.html#mlx.core.array.reciprocal "mlx.core.array.reciprocal"){.reference .internal}(self, \*\[, stream\])                    See [[`reciprocal()`{.xref .py .py-func .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.reciprocal.html#mlx.core.reciprocal "mlx.core.reciprocal"){.reference .internal}.
  [[`array.reshape`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.array.reshape.html#mlx.core.array.reshape "mlx.core.array.reshape"){.reference .internal}(self, \*shape\[, stream\])                           Equivalent to [[`reshape()`{.xref .py .py-func .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.reshape.html#mlx.core.reshape "mlx.core.reshape"){.reference .internal} but the shape can be passed either as a [[`tuple`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)"){.reference .external} or as separate arguments.
  [[`array.round`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.array.round.html#mlx.core.array.round "mlx.core.array.round"){.reference .internal}(self\[, decimals, stream\])                                  See [[`round()`{.xref .py .py-func .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.round.html#mlx.core.round "mlx.core.round"){.reference .internal}.
  [[`array.rsqrt`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.array.rsqrt.html#mlx.core.array.rsqrt "mlx.core.array.rsqrt"){.reference .internal}(self, \*\[, stream\])                                        See [[`rsqrt()`{.xref .py .py-func .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.rsqrt.html#mlx.core.rsqrt "mlx.core.rsqrt"){.reference .internal}.
  [[`array.sin`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.array.sin.html#mlx.core.array.sin "mlx.core.array.sin"){.reference .internal}(self, \*\[, stream\])                                                See [[`sin()`{.xref .py .py-func .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.sin.html#mlx.core.sin "mlx.core.sin"){.reference .internal}.
  [[`array.split`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.array.split.html#mlx.core.array.split "mlx.core.array.split"){.reference .internal}(self, indices_or_sections\[, \...\])                         See [[`split()`{.xref .py .py-func .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.split.html#mlx.core.split "mlx.core.split"){.reference .internal}.
  [[`array.sqrt`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.array.sqrt.html#mlx.core.array.sqrt "mlx.core.array.sqrt"){.reference .internal}(self, \*\[, stream\])                                            See [[`sqrt()`{.xref .py .py-func .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.sqrt.html#mlx.core.sqrt "mlx.core.sqrt"){.reference .internal}.
  [[`array.square`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.array.square.html#mlx.core.array.square "mlx.core.array.square"){.reference .internal}(self, \*\[, stream\])                                    See [[`square()`{.xref .py .py-func .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.square.html#mlx.core.square "mlx.core.square"){.reference .internal}.
  [[`array.squeeze`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.array.squeeze.html#mlx.core.array.squeeze "mlx.core.array.squeeze"){.reference .internal}(self\[, axis, stream\])                              See [[`squeeze()`{.xref .py .py-func .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.squeeze.html#mlx.core.squeeze "mlx.core.squeeze"){.reference .internal}.
  [[`array.std`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.array.std.html#mlx.core.array.std "mlx.core.array.std"){.reference .internal}(self\[, axis, keepdims, ddof, stream\])                              See [[`std()`{.xref .py .py-func .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.std.html#mlx.core.std "mlx.core.std"){.reference .internal}.
  [[`array.sum`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.array.sum.html#mlx.core.array.sum "mlx.core.array.sum"){.reference .internal}(self\[, axis, keepdims, stream\])                                    See [[`sum()`{.xref .py .py-func .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.sum.html#mlx.core.sum "mlx.core.sum"){.reference .internal}.
  [[`array.swapaxes`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.array.swapaxes.html#mlx.core.array.swapaxes "mlx.core.array.swapaxes"){.reference .internal}(self, axis1, axis2, \*\[, stream\])              See [[`swapaxes()`{.xref .py .py-func .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.swapaxes.html#mlx.core.swapaxes "mlx.core.swapaxes"){.reference .internal}.
  [[`array.transpose`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.array.transpose.html#mlx.core.array.transpose "mlx.core.array.transpose"){.reference .internal}(self, \*axes\[, stream\])                    Equivalent to [[`transpose()`{.xref .py .py-func .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.transpose.html#mlx.core.transpose "mlx.core.transpose"){.reference .internal} but the axes can be passed either as a tuple or as separate arguments.
  [[`array.T`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.array.T.html#mlx.core.array.T "mlx.core.array.T"){.reference .internal}                                                                              Equivalent to calling [`self.transpose()`{.docutils .literal .notranslate}]{.pre} with no arguments.
  [[`array.var`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.array.var.html#mlx.core.array.var "mlx.core.array.var"){.reference .internal}(self\[, axis, keepdims, ddof, stream\])                              See [[`var()`{.xref .py .py-func .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.var.html#mlx.core.var "mlx.core.var"){.reference .internal}.
  [[`array.view`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.array.view.html#mlx.core.array.view "mlx.core.array.view"){.reference .internal}(self, dtype, \*\[, stream\])                                     See [[`view()`{.xref .py .py-func .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.view.html#mlx.core.view "mlx.core.view"){.reference .internal}.
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
:::
::::

::::: prev-next-area
[](../examples/tensor_parallelism.html "previous page"){.left-prev}

::: prev-next-info
previous

Tensor Parallelism
:::

[](_autosummary/mlx.core.array.html "next page"){.right-next}

::: prev-next-info
next

mlx.core.array
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
