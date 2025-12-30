# Source: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.nn.quantize.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../_sources/python/_autosummary/mlx.nn.quantize.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.nn.quantize

## Contents

- [[`quantize()`]](#mlx.nn.quantize)

# mlx.nn.quantize[\#](#mlx-nn-quantize "Link to this heading")

[[quantize]][(]*[[model]][[:]][ ][[[Module]](../nn/module.html#mlx.nn.Module "mlx.nn.layers.base.Module")]*, *[[group_size]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")][ ][[=]][ ][[64]]*, *[[bits]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")][ ][[=]][ ][[4]]*, *[[\*]]*, *[[mode]][[:]][ ][[[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")][ ][[=]][ ][[\'affine\']]*, *[[class_predicate]][[:]][ ][[[Callable]](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python v3.14)")[[\[]][[\[]][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[,]][ ][[Module]](../nn/module.html#mlx.nn.Module "mlx.nn.layers.base.Module")[[\]]][[,]][ ][[bool]](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[ ][[\|]][ ][[dict]](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")[[\]]][ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][ ][[=]][ ][[None]]*[)][\#](#mlx.nn.quantize "Link to this definition")

:   Quantize the sub-modules of a module according to a predicate.

    By default all layers that define a [`to_quantized(group_size,`]` `[`bits)`] method will be quantized. Both [[`Linear`]](../nn/_autosummary/mlx.nn.Linear.html#mlx.nn.Linear "mlx.nn.Linear") and [[`Embedding`]](../nn/_autosummary/mlx.nn.Embedding.html#mlx.nn.Embedding "mlx.nn.Embedding") layers will be quantized. Note also, the module is updated in-place.

    Parameters[:]

    :   - **model** ([*Module*](../nn/module.html#mlx.nn.Module "mlx.nn.Module")) -- The model whose leaf modules may be quantized.

        - **group_size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")) -- The quantization group size (see [[`mlx.core.quantize()`]](mlx.core.quantize.html#mlx.core.quantize "mlx.core.quantize")). Default: [`64`].

        - **bits** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")) -- The number of bits per parameter (see [[`mlx.core.quantize()`]](mlx.core.quantize.html#mlx.core.quantize "mlx.core.quantize")). Default: [`4`].

        - **mode** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) -- The quantization method to use (see [[`mlx.core.quantize()`]](mlx.core.quantize.html#mlx.core.quantize "mlx.core.quantize")). Default: [`"affine"`].

        - **class_predicate** (*Optional\[Callable\]*) -- A callable which receives the [[`Module`]](../nn/module.html#mlx.nn.Module "mlx.nn.Module") path and [[`Module`]](../nn/module.html#mlx.nn.Module "mlx.nn.Module") itself and returns [`True`] or a dict of params for to_quantized if it should be quantized and [`False`] otherwise. If [`None`], then all layers that define a [`to_quantized(group_size,`]` `[`bits)`] method are quantized. Default: [`None`].

[](mlx.nn.value_and_grad.html "previous page")

previous

mlx.nn.value_and_grad

[](mlx.nn.average_gradients.html "next page")

next

mlx.nn.average_gradients

Contents

- [[`quantize()`]](#mlx.nn.quantize)

By MLX Contributors

© Copyright 2023, Apple.\