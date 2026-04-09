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
  [.rst]{.btn__text-container}](../../_sources/python/_autosummary/mlx.core.array.rst "Download source file"){.btn
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

# mlx.core.array

::::: {#print-main-content}
:::: {#jb-print-toc}
::: {}

## Contents

:::

- [[`array`{.docutils .literal
  .notranslate}]{.pre}](#mlx.core.array){.reference .internal .nav-link}
  - [[`array.__init__()`{.docutils .literal
    .notranslate}]{.pre}](#mlx.core.array.__init__){.reference .internal
    .nav-link}
::::
:::::
::::::

::: {#searchbox}
:::

::: {#mlx-core-array .section}

# mlx.core.array[\#](#mlx-core-array "Link to this heading"){.headerlink}

[[[class]{.pre}]{.k}[ ]{.w}]{.property}[[array]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[\*]{.pre}]{.o}[[args]{.pre}]{.n}*, *[[\*\*]{.pre}]{.o}[[kwargs]{.pre}]{.n}*[)]{.sig-paren}[\#](#mlx.core.array "Link to this definition"){.headerlink}

:   An N-dimensional array object.

    [[\_\_init\_\_]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[self]{.pre}]{.n}[[:]{.pre}]{.p}[ ]{.w}[[[array]{.pre}](#mlx.core.array "mlx.core.array"){.reference .internal}]{.n}*, *[[val]{.pre}]{.n}[[:]{.pre}]{.p}[ ]{.w}[[scalar]{.pre}[ ]{.w}[[\|]{.pre}]{.p}[ ]{.w}[[list]{.pre}](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)"){.reference .external}[ ]{.w}[[\|]{.pre}]{.p}[ ]{.w}[[tuple]{.pre}](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)"){.reference .external}[ ]{.w}[[\|]{.pre}]{.p}[ ]{.w}[[ndarray]{.pre}](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.4)"){.reference .external}[ ]{.w}[[\|]{.pre}]{.p}[ ]{.w}[[array]{.pre}](#mlx.core.array "mlx.core.array"){.reference .internal}]{.n}*, *[[dtype]{.pre}]{.n}[[:]{.pre}]{.p}[ ]{.w}[[[Dtype]{.pre}](mlx.core.Dtype.html#mlx.core.Dtype "mlx.core.Dtype"){.reference .internal}[ ]{.w}[[\|]{.pre}]{.p}[ ]{.w}[[None]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"){.reference .external}]{.n}[ ]{.w}[[=]{.pre}]{.o}[ ]{.w}[[None]{.pre}]{.default_value}*[)]{.sig-paren}[\#](#mlx.core.array.__init__ "Link to this definition"){.headerlink}

    :

    Methods

    ::: pst-scrollable-table-container
      ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
      [[`__init__`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#mlx.core.array.__init__ "mlx.core.array.__init__"){.reference .internal}(self, val\[, dtype\])
      [[`abs`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](mlx.core.array.abs.html#mlx.core.array.abs "mlx.core.array.abs"){.reference .internal}(self, \*\[, stream\])                                                See [[`abs()`{.xref .py .py-func .docutils .literal .notranslate}]{.pre}](mlx.core.abs.html#mlx.core.abs "mlx.core.abs"){.reference .internal}.
      [[`all`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](mlx.core.array.all.html#mlx.core.array.all "mlx.core.array.all"){.reference .internal}(self\[, axis, keepdims, stream\])                                    See [[`all()`{.xref .py .py-func .docutils .literal .notranslate}]{.pre}](mlx.core.all.html#mlx.core.all "mlx.core.all"){.reference .internal}.
      [[`any`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](mlx.core.array.any.html#mlx.core.array.any "mlx.core.array.any"){.reference .internal}(self\[, axis, keepdims, stream\])                                    See [[`any()`{.xref .py .py-func .docutils .literal .notranslate}]{.pre}](mlx.core.any.html#mlx.core.any "mlx.core.any"){.reference .internal}.
      [[`argmax`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](mlx.core.array.argmax.html#mlx.core.array.argmax "mlx.core.array.argmax"){.reference .internal}(self\[, axis, keepdims, stream\])                        See [[`argmax()`{.xref .py .py-func .docutils .literal .notranslate}]{.pre}](mlx.core.argmax.html#mlx.core.argmax "mlx.core.argmax"){.reference .internal}.
      [[`argmin`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](mlx.core.array.argmin.html#mlx.core.array.argmin "mlx.core.array.argmin"){.reference .internal}(self\[, axis, keepdims, stream\])                        See [[`argmin()`{.xref .py .py-func .docutils .literal .notranslate}]{.pre}](mlx.core.argmin.html#mlx.core.argmin "mlx.core.argmin"){.reference .internal}.
      [[`astype`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](mlx.core.array.astype.html#mlx.core.array.astype "mlx.core.array.astype"){.reference .internal}(self, dtype\[, stream\])                                 Cast the array to a specified type.
      [[`conj`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](mlx.core.array.conj.html#mlx.core.array.conj "mlx.core.array.conj"){.reference .internal}(self, \*\[, stream\])                                            See [[`conj()`{.xref .py .py-func .docutils .literal .notranslate}]{.pre}](mlx.core.conj.html#mlx.core.conj "mlx.core.conj"){.reference .internal}.
      [[`cos`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](mlx.core.array.cos.html#mlx.core.array.cos "mlx.core.array.cos"){.reference .internal}(self, \*\[, stream\])                                                See [[`cos()`{.xref .py .py-func .docutils .literal .notranslate}]{.pre}](mlx.core.cos.html#mlx.core.cos "mlx.core.cos"){.reference .internal}.
      [[`cummax`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](mlx.core.array.cummax.html#mlx.core.array.cummax "mlx.core.array.cummax"){.reference .internal}(self\[, axis, reverse, inclusive, stream\])              See [[`cummax()`{.xref .py .py-func .docutils .literal .notranslate}]{.pre}](mlx.core.cummax.html#mlx.core.cummax "mlx.core.cummax"){.reference .internal}.
      [[`cummin`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](mlx.core.array.cummin.html#mlx.core.array.cummin "mlx.core.array.cummin"){.reference .internal}(self\[, axis, reverse, inclusive, stream\])              See [[`cummin()`{.xref .py .py-func .docutils .literal .notranslate}]{.pre}](mlx.core.cummin.html#mlx.core.cummin "mlx.core.cummin"){.reference .internal}.
      [[`cumprod`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](mlx.core.array.cumprod.html#mlx.core.array.cumprod "mlx.core.array.cumprod"){.reference .internal}(self\[, axis, reverse, inclusive, stream\])          See [[`cumprod()`{.xref .py .py-func .docutils .literal .notranslate}]{.pre}](mlx.core.cumprod.html#mlx.core.cumprod "mlx.core.cumprod"){.reference .internal}.
      [[`cumsum`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](mlx.core.array.cumsum.html#mlx.core.array.cumsum "mlx.core.array.cumsum"){.reference .internal}(self\[, axis, reverse, inclusive, stream\])              See [[`cumsum()`{.xref .py .py-func .docutils .literal .notranslate}]{.pre}](mlx.core.cumsum.html#mlx.core.cumsum "mlx.core.cumsum"){.reference .internal}.
      [[`diag`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](mlx.core.array.diag.html#mlx.core.array.diag "mlx.core.array.diag"){.reference .internal}(self\[, k, stream\])                                             Extract a diagonal or construct a diagonal matrix.
      [[`diagonal`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](mlx.core.array.diagonal.html#mlx.core.array.diagonal "mlx.core.array.diagonal"){.reference .internal}(self\[, offset, axis1, axis2, stream\])          See [[`diagonal()`{.xref .py .py-func .docutils .literal .notranslate}]{.pre}](mlx.core.diagonal.html#mlx.core.diagonal "mlx.core.diagonal"){.reference .internal}.
      [[`exp`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](mlx.core.array.exp.html#mlx.core.array.exp "mlx.core.array.exp"){.reference .internal}(self, \*\[, stream\])                                                See [[`exp()`{.xref .py .py-func .docutils .literal .notranslate}]{.pre}](mlx.core.exp.html#mlx.core.exp "mlx.core.exp"){.reference .internal}.
      [[`flatten`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](mlx.core.array.flatten.html#mlx.core.array.flatten "mlx.core.array.flatten"){.reference .internal}(self\[, start_axis, end_axis, stream\])              See [[`flatten()`{.xref .py .py-func .docutils .literal .notranslate}]{.pre}](mlx.core.flatten.html#mlx.core.flatten "mlx.core.flatten"){.reference .internal}.
      [[`item`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](mlx.core.array.item.html#mlx.core.array.item "mlx.core.array.item"){.reference .internal}(self)                                                            Access the value of a scalar array.
      [[`log`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](mlx.core.array.log.html#mlx.core.array.log "mlx.core.array.log"){.reference .internal}(self, \*\[, stream\])                                                See [[`log()`{.xref .py .py-func .docutils .literal .notranslate}]{.pre}](mlx.core.log.html#mlx.core.log "mlx.core.log"){.reference .internal}.
      [[`log10`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](mlx.core.array.log10.html#mlx.core.array.log10 "mlx.core.array.log10"){.reference .internal}(self, \*\[, stream\])                                        See [[`log10()`{.xref .py .py-func .docutils .literal .notranslate}]{.pre}](mlx.core.log10.html#mlx.core.log10 "mlx.core.log10"){.reference .internal}.
      [[`log1p`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](mlx.core.array.log1p.html#mlx.core.array.log1p "mlx.core.array.log1p"){.reference .internal}(self, \*\[, stream\])                                        See [[`log1p()`{.xref .py .py-func .docutils .literal .notranslate}]{.pre}](mlx.core.log1p.html#mlx.core.log1p "mlx.core.log1p"){.reference .internal}.
      [[`log2`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](mlx.core.array.log2.html#mlx.core.array.log2 "mlx.core.array.log2"){.reference .internal}(self, \*\[, stream\])                                            See [[`log2()`{.xref .py .py-func .docutils .literal .notranslate}]{.pre}](mlx.core.log2.html#mlx.core.log2 "mlx.core.log2"){.reference .internal}.
      [[`logcumsumexp`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](mlx.core.array.logcumsumexp.html#mlx.core.array.logcumsumexp "mlx.core.array.logcumsumexp"){.reference .internal}(self\[, axis, reverse, \...\])   See [[`logcumsumexp()`{.xref .py .py-func .docutils .literal .notranslate}]{.pre}](mlx.core.logcumsumexp.html#mlx.core.logcumsumexp "mlx.core.logcumsumexp"){.reference .internal}.
      [[`logsumexp`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](mlx.core.array.logsumexp.html#mlx.core.array.logsumexp "mlx.core.array.logsumexp"){.reference .internal}(self\[, axis, keepdims, stream\])            See [[`logsumexp()`{.xref .py .py-func .docutils .literal .notranslate}]{.pre}](mlx.core.logsumexp.html#mlx.core.logsumexp "mlx.core.logsumexp"){.reference .internal}.
      [[`max`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](mlx.core.array.max.html#mlx.core.array.max "mlx.core.array.max"){.reference .internal}(self\[, axis, keepdims, stream\])                                    See [[`max()`{.xref .py .py-func .docutils .literal .notranslate}]{.pre}](mlx.core.max.html#mlx.core.max "mlx.core.max"){.reference .internal}.
      [[`mean`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](mlx.core.array.mean.html#mlx.core.array.mean "mlx.core.array.mean"){.reference .internal}(self\[, axis, keepdims, stream\])                                See [[`mean()`{.xref .py .py-func .docutils .literal .notranslate}]{.pre}](mlx.core.mean.html#mlx.core.mean "mlx.core.mean"){.reference .internal}.
      [[`min`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](mlx.core.array.min.html#mlx.core.array.min "mlx.core.array.min"){.reference .internal}(self\[, axis, keepdims, stream\])                                    See [[`min()`{.xref .py .py-func .docutils .literal .notranslate}]{.pre}](mlx.core.min.html#mlx.core.min "mlx.core.min"){.reference .internal}.
      [[`moveaxis`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](mlx.core.array.moveaxis.html#mlx.core.array.moveaxis "mlx.core.array.moveaxis"){.reference .internal}(self, source, destination, \*\[, stream\])       See [[`moveaxis()`{.xref .py .py-func .docutils .literal .notranslate}]{.pre}](mlx.core.moveaxis.html#mlx.core.moveaxis "mlx.core.moveaxis"){.reference .internal}.
      [[`prod`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](mlx.core.array.prod.html#mlx.core.array.prod "mlx.core.array.prod"){.reference .internal}(self\[, axis, keepdims, stream\])                                See [[`prod()`{.xref .py .py-func .docutils .literal .notranslate}]{.pre}](mlx.core.prod.html#mlx.core.prod "mlx.core.prod"){.reference .internal}.
      [[`reciprocal`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](mlx.core.array.reciprocal.html#mlx.core.array.reciprocal "mlx.core.array.reciprocal"){.reference .internal}(self, \*\[, stream\])                    See [[`reciprocal()`{.xref .py .py-func .docutils .literal .notranslate}]{.pre}](mlx.core.reciprocal.html#mlx.core.reciprocal "mlx.core.reciprocal"){.reference .internal}.
      [[`reshape`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](mlx.core.array.reshape.html#mlx.core.array.reshape "mlx.core.array.reshape"){.reference .internal}(self, \*shape\[, stream\])                           Equivalent to [[`reshape()`{.xref .py .py-func .docutils .literal .notranslate}]{.pre}](mlx.core.reshape.html#mlx.core.reshape "mlx.core.reshape"){.reference .internal} but the shape can be passed either as a [[`tuple`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)"){.reference .external} or as separate arguments.
      [[`round`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](mlx.core.array.round.html#mlx.core.array.round "mlx.core.array.round"){.reference .internal}(self\[, decimals, stream\])                                  See [[`round()`{.xref .py .py-func .docutils .literal .notranslate}]{.pre}](mlx.core.round.html#mlx.core.round "mlx.core.round"){.reference .internal}.
      [[`rsqrt`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](mlx.core.array.rsqrt.html#mlx.core.array.rsqrt "mlx.core.array.rsqrt"){.reference .internal}(self, \*\[, stream\])                                        See [[`rsqrt()`{.xref .py .py-func .docutils .literal .notranslate}]{.pre}](mlx.core.rsqrt.html#mlx.core.rsqrt "mlx.core.rsqrt"){.reference .internal}.
      [[`sin`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](mlx.core.array.sin.html#mlx.core.array.sin "mlx.core.array.sin"){.reference .internal}(self, \*\[, stream\])                                                See [[`sin()`{.xref .py .py-func .docutils .literal .notranslate}]{.pre}](mlx.core.sin.html#mlx.core.sin "mlx.core.sin"){.reference .internal}.
      [[`split`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](mlx.core.array.split.html#mlx.core.array.split "mlx.core.array.split"){.reference .internal}(self, indices_or_sections\[, axis, stream\])                 See [[`split()`{.xref .py .py-func .docutils .literal .notranslate}]{.pre}](mlx.core.split.html#mlx.core.split "mlx.core.split"){.reference .internal}.
      [[`sqrt`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](mlx.core.array.sqrt.html#mlx.core.array.sqrt "mlx.core.array.sqrt"){.reference .internal}(self, \*\[, stream\])                                            See [[`sqrt()`{.xref .py .py-func .docutils .literal .notranslate}]{.pre}](mlx.core.sqrt.html#mlx.core.sqrt "mlx.core.sqrt"){.reference .internal}.
      [[`square`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](mlx.core.array.square.html#mlx.core.array.square "mlx.core.array.square"){.reference .internal}(self, \*\[, stream\])                                    See [[`square()`{.xref .py .py-func .docutils .literal .notranslate}]{.pre}](mlx.core.square.html#mlx.core.square "mlx.core.square"){.reference .internal}.
      [[`squeeze`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](mlx.core.array.squeeze.html#mlx.core.array.squeeze "mlx.core.array.squeeze"){.reference .internal}(self\[, axis, stream\])                              See [[`squeeze()`{.xref .py .py-func .docutils .literal .notranslate}]{.pre}](mlx.core.squeeze.html#mlx.core.squeeze "mlx.core.squeeze"){.reference .internal}.
      [[`std`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](mlx.core.array.std.html#mlx.core.array.std "mlx.core.array.std"){.reference .internal}(self\[, axis, keepdims, ddof, stream\])                              See [[`std()`{.xref .py .py-func .docutils .literal .notranslate}]{.pre}](mlx.core.std.html#mlx.core.std "mlx.core.std"){.reference .internal}.
      [[`sum`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](mlx.core.array.sum.html#mlx.core.array.sum "mlx.core.array.sum"){.reference .internal}(self\[, axis, keepdims, stream\])                                    See [[`sum()`{.xref .py .py-func .docutils .literal .notranslate}]{.pre}](mlx.core.sum.html#mlx.core.sum "mlx.core.sum"){.reference .internal}.
      [[`swapaxes`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](mlx.core.array.swapaxes.html#mlx.core.array.swapaxes "mlx.core.array.swapaxes"){.reference .internal}(self, axis1, axis2, \*\[, stream\])              See [[`swapaxes()`{.xref .py .py-func .docutils .literal .notranslate}]{.pre}](mlx.core.swapaxes.html#mlx.core.swapaxes "mlx.core.swapaxes"){.reference .internal}.
      [[`tolist`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](mlx.core.array.tolist.html#mlx.core.array.tolist "mlx.core.array.tolist"){.reference .internal}(self)                                                    Convert the array to a Python [[`list`{.xref .py .py-class .docutils .literal .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)"){.reference .external}.
      [[`transpose`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](mlx.core.array.transpose.html#mlx.core.array.transpose "mlx.core.array.transpose"){.reference .internal}(self, \*axes\[, stream\])                    Equivalent to [[`transpose()`{.xref .py .py-func .docutils .literal .notranslate}]{.pre}](mlx.core.transpose.html#mlx.core.transpose "mlx.core.transpose"){.reference .internal} but the axes can be passed either as a tuple or as separate arguments.
      [[`var`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](mlx.core.array.var.html#mlx.core.array.var "mlx.core.array.var"){.reference .internal}(self\[, axis, keepdims, ddof, stream\])                              See [[`var()`{.xref .py .py-func .docutils .literal .notranslate}]{.pre}](mlx.core.var.html#mlx.core.var "mlx.core.var"){.reference .internal}.
      [[`view`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](mlx.core.array.view.html#mlx.core.array.view "mlx.core.array.view"){.reference .internal}(self, dtype, \*\[, stream\])                                     See [[`view()`{.xref .py .py-func .docutils .literal .notranslate}]{.pre}](mlx.core.view.html#mlx.core.view "mlx.core.view"){.reference .internal}.
      ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    :::

    Attributes

    ::: pst-scrollable-table-container
      ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------
      [[`T`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](mlx.core.array.T.html#mlx.core.array.T "mlx.core.array.T"){.reference .internal}                               Equivalent to calling [`self.transpose()`{.docutils .literal .notranslate}]{.pre} with no arguments.
      [[`at`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](mlx.core.array.at.html#mlx.core.array.at "mlx.core.array.at"){.reference .internal}                           Used to apply updates at the given indices.
      [[`dtype`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](mlx.core.array.dtype.html#mlx.core.array.dtype "mlx.core.array.dtype"){.reference .internal}               The array\'s [[`Dtype`{.xref .py .py-class .docutils .literal .notranslate}]{.pre}](mlx.core.Dtype.html#mlx.core.Dtype "mlx.core.Dtype"){.reference .internal}.
      [[`imag`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](mlx.core.array.imag.html#mlx.core.array.imag "mlx.core.array.imag"){.reference .internal}                   The imaginary part of a complex array.
      [[`itemsize`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](mlx.core.array.itemsize.html#mlx.core.array.itemsize "mlx.core.array.itemsize"){.reference .internal}   The size of the array\'s datatype in bytes.
      [[`nbytes`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](mlx.core.array.nbytes.html#mlx.core.array.nbytes "mlx.core.array.nbytes"){.reference .internal}           The number of bytes in the array.
      [[`ndim`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](mlx.core.array.ndim.html#mlx.core.array.ndim "mlx.core.array.ndim"){.reference .internal}                   The array\'s dimension.
      [[`real`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](mlx.core.array.real.html#mlx.core.array.real "mlx.core.array.real"){.reference .internal}                   The real part of a complex array.
      [[`shape`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](mlx.core.array.shape.html#mlx.core.array.shape "mlx.core.array.shape"){.reference .internal}               The shape of the array as a Python tuple.
      [[`size`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](mlx.core.array.size.html#mlx.core.array.size "mlx.core.array.size"){.reference .internal}                   Number of elements in the array.
      ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------
    :::
:::

::::: prev-next-area
[](../array.html "previous page"){.left-prev}

::: prev-next-info
previous

Array
:::

[](mlx.core.array.astype.html "next page"){.right-next}

::: prev-next-info
next

mlx.core.array.astype
:::
:::::
::::::::::::::::::::

:::::: {#pst-secondary-sidebar .bd-sidebar-secondary .bd-toc}
::::: {.sidebar-secondary-items .sidebar-secondary__inner}
:::: sidebar-secondary-item
::: {#pst-page-navigation-heading-2 .page-toc .tocsection .onthispage}
Contents
:::

- [[`array`{.docutils .literal
  .notranslate}]{.pre}](#mlx.core.array){.reference .internal .nav-link}
  - [[`array.__init__()`{.docutils .literal
    .notranslate}]{.pre}](#mlx.core.array.__init__){.reference .internal
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
