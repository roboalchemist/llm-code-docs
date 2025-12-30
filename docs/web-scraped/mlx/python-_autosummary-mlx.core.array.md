# Source: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.array.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../_sources/python/_autosummary/mlx.core.array.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.core.array

## Contents

- [[`array`]](#mlx.core.array)
  - [[`array.__init__()`]](#mlx.core.array.__init__)

# mlx.core.array[\#](#mlx-core-array "Link to this heading")

*[class][ ]*[[array]][\#](#mlx.core.array "Link to this definition")

:   An N-dimensional array object.

    [[\_\_init\_\_]][(]*[[self]][[:]][ ][[[array]](#mlx.core.array "mlx.core.array")]*, *[[val]][[:]][ ][[scalar][ ][[\|]][ ][[list]](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[ ][[\|]][ ][[tuple]](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[ ][[\|]][ ][[ndarray]](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.3)")[ ][[\|]][ ][[array]](#mlx.core.array "mlx.core.array")]*, *[[dtype]][[:]][ ][[[Dtype]](mlx.core.Dtype.html#mlx.core.Dtype "mlx.core.Dtype")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][ ][[=]][ ][[None]]*[)][\#](#mlx.core.array.__init__ "Link to this definition")

    :   

    Methods

    ::: pst-scrollable-table-container
      ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
      [[`__init__`]](#mlx.core.array.__init__ "mlx.core.array.__init__")(self, val\[, dtype\])                                                        
      [[`abs`]](mlx.core.array.abs.html#mlx.core.array.abs "mlx.core.array.abs")(self, \*\[, stream\])                                                See [[`abs()`]](mlx.core.abs.html#mlx.core.abs "mlx.core.abs").
      [[`all`]](mlx.core.array.all.html#mlx.core.array.all "mlx.core.array.all")(self\[, axis, keepdims, stream\])                                    See [[`all()`]](mlx.core.all.html#mlx.core.all "mlx.core.all").
      [[`any`]](mlx.core.array.any.html#mlx.core.array.any "mlx.core.array.any")(self\[, axis, keepdims, stream\])                                    See [[`any()`]](mlx.core.any.html#mlx.core.any "mlx.core.any").
      [[`argmax`]](mlx.core.array.argmax.html#mlx.core.array.argmax "mlx.core.array.argmax")(self\[, axis, keepdims, stream\])                        See [[`argmax()`]](mlx.core.argmax.html#mlx.core.argmax "mlx.core.argmax").
      [[`argmin`]](mlx.core.array.argmin.html#mlx.core.array.argmin "mlx.core.array.argmin")(self\[, axis, keepdims, stream\])                        See [[`argmin()`]](mlx.core.argmin.html#mlx.core.argmin "mlx.core.argmin").
      [[`astype`]](mlx.core.array.astype.html#mlx.core.array.astype "mlx.core.array.astype")(self, dtype\[, stream\])                                 Cast the array to a specified type.
      [[`conj`]](mlx.core.array.conj.html#mlx.core.array.conj "mlx.core.array.conj")(self, \*\[, stream\])                                            See [[`conj()`]](mlx.core.conj.html#mlx.core.conj "mlx.core.conj").
      [[`cos`]](mlx.core.array.cos.html#mlx.core.array.cos "mlx.core.array.cos")(self, \*\[, stream\])                                                See [[`cos()`]](mlx.core.cos.html#mlx.core.cos "mlx.core.cos").
      [[`cummax`]](mlx.core.array.cummax.html#mlx.core.array.cummax "mlx.core.array.cummax")(self\[, axis, reverse, inclusive, stream\])              See [[`cummax()`]](mlx.core.cummax.html#mlx.core.cummax "mlx.core.cummax").
      [[`cummin`]](mlx.core.array.cummin.html#mlx.core.array.cummin "mlx.core.array.cummin")(self\[, axis, reverse, inclusive, stream\])              See [[`cummin()`]](mlx.core.cummin.html#mlx.core.cummin "mlx.core.cummin").
      [[`cumprod`]](mlx.core.array.cumprod.html#mlx.core.array.cumprod "mlx.core.array.cumprod")(self\[, axis, reverse, inclusive, stream\])          See [[`cumprod()`]](mlx.core.cumprod.html#mlx.core.cumprod "mlx.core.cumprod").
      [[`cumsum`]](mlx.core.array.cumsum.html#mlx.core.array.cumsum "mlx.core.array.cumsum")(self\[, axis, reverse, inclusive, stream\])              See [[`cumsum()`]](mlx.core.cumsum.html#mlx.core.cumsum "mlx.core.cumsum").
      [[`diag`]](mlx.core.array.diag.html#mlx.core.array.diag "mlx.core.array.diag")(self\[, k, stream\])                                             Extract a diagonal or construct a diagonal matrix.
      [[`diagonal`]](mlx.core.array.diagonal.html#mlx.core.array.diagonal "mlx.core.array.diagonal")(self\[, offset, axis1, axis2, stream\])          See [[`diagonal()`]](mlx.core.diagonal.html#mlx.core.diagonal "mlx.core.diagonal").
      [[`exp`]](mlx.core.array.exp.html#mlx.core.array.exp "mlx.core.array.exp")(self, \*\[, stream\])                                                See [[`exp()`]](mlx.core.exp.html#mlx.core.exp "mlx.core.exp").
      [[`flatten`]](mlx.core.array.flatten.html#mlx.core.array.flatten "mlx.core.array.flatten")(self\[, start_axis, end_axis, stream\])              See [[`flatten()`]](mlx.core.flatten.html#mlx.core.flatten "mlx.core.flatten").
      [[`item`]](mlx.core.array.item.html#mlx.core.array.item "mlx.core.array.item")(self)                                                            Access the value of a scalar array.
      [[`log`]](mlx.core.array.log.html#mlx.core.array.log "mlx.core.array.log")(self, \*\[, stream\])                                                See [[`log()`]](mlx.core.log.html#mlx.core.log "mlx.core.log").
      [[`log10`]](mlx.core.array.log10.html#mlx.core.array.log10 "mlx.core.array.log10")(self, \*\[, stream\])                                        See [[`log10()`]](mlx.core.log10.html#mlx.core.log10 "mlx.core.log10").
      [[`log1p`]](mlx.core.array.log1p.html#mlx.core.array.log1p "mlx.core.array.log1p")(self, \*\[, stream\])                                        See [[`log1p()`]](mlx.core.log1p.html#mlx.core.log1p "mlx.core.log1p").
      [[`log2`]](mlx.core.array.log2.html#mlx.core.array.log2 "mlx.core.array.log2")(self, \*\[, stream\])                                            See [[`log2()`]](mlx.core.log2.html#mlx.core.log2 "mlx.core.log2").
      [[`logcumsumexp`]](mlx.core.array.logcumsumexp.html#mlx.core.array.logcumsumexp "mlx.core.array.logcumsumexp")(self\[, axis, reverse, \...\])   See [[`logcumsumexp()`]](mlx.core.logcumsumexp.html#mlx.core.logcumsumexp "mlx.core.logcumsumexp").
      [[`logsumexp`]](mlx.core.array.logsumexp.html#mlx.core.array.logsumexp "mlx.core.array.logsumexp")(self\[, axis, keepdims, stream\])            See [[`logsumexp()`]](mlx.core.logsumexp.html#mlx.core.logsumexp "mlx.core.logsumexp").
      [[`max`]](mlx.core.array.max.html#mlx.core.array.max "mlx.core.array.max")(self\[, axis, keepdims, stream\])                                    See [[`max()`]](mlx.core.max.html#mlx.core.max "mlx.core.max").
      [[`mean`]](mlx.core.array.mean.html#mlx.core.array.mean "mlx.core.array.mean")(self\[, axis, keepdims, stream\])                                See [[`mean()`]](mlx.core.mean.html#mlx.core.mean "mlx.core.mean").
      [[`min`]](mlx.core.array.min.html#mlx.core.array.min "mlx.core.array.min")(self\[, axis, keepdims, stream\])                                    See [[`min()`]](mlx.core.min.html#mlx.core.min "mlx.core.min").
      [[`moveaxis`]](mlx.core.array.moveaxis.html#mlx.core.array.moveaxis "mlx.core.array.moveaxis")(self, source, destination, \*\[, stream\])       See [[`moveaxis()`]](mlx.core.moveaxis.html#mlx.core.moveaxis "mlx.core.moveaxis").
      [[`prod`]](mlx.core.array.prod.html#mlx.core.array.prod "mlx.core.array.prod")(self\[, axis, keepdims, stream\])                                See [[`prod()`]](mlx.core.prod.html#mlx.core.prod "mlx.core.prod").
      [[`reciprocal`]](mlx.core.array.reciprocal.html#mlx.core.array.reciprocal "mlx.core.array.reciprocal")(self, \*\[, stream\])                    See [[`reciprocal()`]](mlx.core.reciprocal.html#mlx.core.reciprocal "mlx.core.reciprocal").
      [[`reshape`]](mlx.core.array.reshape.html#mlx.core.array.reshape "mlx.core.array.reshape")(self, \*shape\[, stream\])                           Equivalent to [[`reshape()`]](mlx.core.reshape.html#mlx.core.reshape "mlx.core.reshape") but the shape can be passed either as a [[`tuple`]](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)") or as separate arguments.
      [[`round`]](mlx.core.array.round.html#mlx.core.array.round "mlx.core.array.round")(self\[, decimals, stream\])                                  See [[`round()`]](mlx.core.round.html#mlx.core.round "mlx.core.round").
      [[`rsqrt`]](mlx.core.array.rsqrt.html#mlx.core.array.rsqrt "mlx.core.array.rsqrt")(self, \*\[, stream\])                                        See [[`rsqrt()`]](mlx.core.rsqrt.html#mlx.core.rsqrt "mlx.core.rsqrt").
      [[`sin`]](mlx.core.array.sin.html#mlx.core.array.sin "mlx.core.array.sin")(self, \*\[, stream\])                                                See [[`sin()`]](mlx.core.sin.html#mlx.core.sin "mlx.core.sin").
      [[`split`]](mlx.core.array.split.html#mlx.core.array.split "mlx.core.array.split")(self, indices_or_sections\[, axis, stream\])                 See [[`split()`]](mlx.core.split.html#mlx.core.split "mlx.core.split").
      [[`sqrt`]](mlx.core.array.sqrt.html#mlx.core.array.sqrt "mlx.core.array.sqrt")(self, \*\[, stream\])                                            See [[`sqrt()`]](mlx.core.sqrt.html#mlx.core.sqrt "mlx.core.sqrt").
      [[`square`]](mlx.core.array.square.html#mlx.core.array.square "mlx.core.array.square")(self, \*\[, stream\])                                    See [[`square()`]](mlx.core.square.html#mlx.core.square "mlx.core.square").
      [[`squeeze`]](mlx.core.array.squeeze.html#mlx.core.array.squeeze "mlx.core.array.squeeze")(self\[, axis, stream\])                              See [[`squeeze()`]](mlx.core.squeeze.html#mlx.core.squeeze "mlx.core.squeeze").
      [[`std`]](mlx.core.array.std.html#mlx.core.array.std "mlx.core.array.std")(self\[, axis, keepdims, ddof, stream\])                              See [[`std()`]](mlx.core.std.html#mlx.core.std "mlx.core.std").
      [[`sum`]](mlx.core.array.sum.html#mlx.core.array.sum "mlx.core.array.sum")(self\[, axis, keepdims, stream\])                                    See [[`sum()`]](mlx.core.sum.html#mlx.core.sum "mlx.core.sum").
      [[`swapaxes`]](mlx.core.array.swapaxes.html#mlx.core.array.swapaxes "mlx.core.array.swapaxes")(self, axis1, axis2, \*\[, stream\])              See [[`swapaxes()`]](mlx.core.swapaxes.html#mlx.core.swapaxes "mlx.core.swapaxes").
      [[`tolist`]](mlx.core.array.tolist.html#mlx.core.array.tolist "mlx.core.array.tolist")(self)                                                    Convert the array to a Python [[`list`]](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)").
      [[`transpose`]](mlx.core.array.transpose.html#mlx.core.array.transpose "mlx.core.array.transpose")(self, \*axes\[, stream\])                    Equivalent to [[`transpose()`]](mlx.core.transpose.html#mlx.core.transpose "mlx.core.transpose") but the axes can be passed either as a tuple or as separate arguments.
      [[`var`]](mlx.core.array.var.html#mlx.core.array.var "mlx.core.array.var")(self\[, axis, keepdims, ddof, stream\])                              See [[`var()`]](mlx.core.var.html#mlx.core.var "mlx.core.var").
      [[`view`]](mlx.core.array.view.html#mlx.core.array.view "mlx.core.array.view")(self, dtype, \*\[, stream\])                                     See [[`view()`]](mlx.core.view.html#mlx.core.view "mlx.core.view").
      ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    :::

    Attributes

    ::: pst-scrollable-table-container
      ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------
      [[`T`]](mlx.core.array.T.html#mlx.core.array.T "mlx.core.array.T")                               Equivalent to calling [`self.transpose()`] with no arguments.
      [[`at`]](mlx.core.array.at.html#mlx.core.array.at "mlx.core.array.at")                           Used to apply updates at the given indices.
      [[`dtype`]](mlx.core.array.dtype.html#mlx.core.array.dtype "mlx.core.array.dtype")               The array\'s [[`Dtype`]](mlx.core.Dtype.html#mlx.core.Dtype "mlx.core.Dtype").
      [[`imag`]](mlx.core.array.imag.html#mlx.core.array.imag "mlx.core.array.imag")                   The imaginary part of a complex array.
      [[`itemsize`]](mlx.core.array.itemsize.html#mlx.core.array.itemsize "mlx.core.array.itemsize")   The size of the array\'s datatype in bytes.
      [[`nbytes`]](mlx.core.array.nbytes.html#mlx.core.array.nbytes "mlx.core.array.nbytes")           The number of bytes in the array.
      [[`ndim`]](mlx.core.array.ndim.html#mlx.core.array.ndim "mlx.core.array.ndim")                   The array\'s dimension.
      [[`real`]](mlx.core.array.real.html#mlx.core.array.real "mlx.core.array.real")                   The real part of a complex array.
      [[`shape`]](mlx.core.array.shape.html#mlx.core.array.shape "mlx.core.array.shape")               The shape of the array as a Python tuple.
      [[`size`]](mlx.core.array.size.html#mlx.core.array.size "mlx.core.array.size")                   Number of elements in the array.
      ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------
    :::

[](../array.html "previous page")

previous

Array

[](mlx.core.array.astype.html "next page")

next

mlx.core.array.astype

Contents

- [[`array`]](#mlx.core.array)
  - [[`array.__init__()`]](#mlx.core.array.__init__)

By MLX Contributors

© Copyright 2023, Apple.\