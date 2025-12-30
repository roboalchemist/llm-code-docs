# Source: https://ml-explore.github.io/mlx/build/html/python/nn/_autosummary/mlx.nn.Module.apply.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../../_sources/python/nn/_autosummary/mlx.nn.Module.apply.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.nn.Module.apply

## Contents

- [[`Module.apply()`]](#mlx.nn.Module.apply)

# mlx.nn.Module.apply[\#](#mlx-nn-module-apply "Link to this heading")

[[Module.]][[apply]][(]*[[map_fn]][[:]][ ][[[Callable]](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python v3.14)")[[\[]][[\[]][[array]](../../_autosummary/mlx.core.array.html#mlx.core.array "mlx.core.array")[[\]]][[,]][ ][[array]](../../_autosummary/mlx.core.array.html#mlx.core.array "mlx.core.array")[[\]]]]*, *[[filter_fn]][[:]][ ][[[Callable]](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python v3.14)")[[\[]][[\[]][[Module]](../module.html#mlx.nn.Module "mlx.nn.layers.base.Module")[[,]][ ][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[,]][ ][[Any]](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")[[\]]][[,]][ ][[bool]](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[\]]][ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][ ][[=]][ ][[None]]*[)] [[→] [[[Module]](../module.html#mlx.nn.Module "mlx.nn.layers.base.Module")]][\#](#mlx.nn.Module.apply "Link to this definition")

:   Map all the parameters using the provided [`map_fn`] and immediately update the module with the mapped parameters.

    For instance running [`model.apply(lambda`]` `[`x:`]` `[`x.astype(mx.float16))`] casts all parameters to 16 bit floats.

    Parameters[:]

    :   - **map_fn** (*Callable*) -- Maps an array to another array

        - **filter_fn** (*Callable,* *optional*) -- Filter to select which arrays to map (default: [`Module.valid_parameter_filter()`]).

    Returns[:]

    :   The module instance after updating the parameters.

[](mlx.nn.Module.state.html "previous page")

previous

mlx.nn.Module.state

[](mlx.nn.Module.apply_to_modules.html "next page")

next

mlx.nn.Module.apply_to_modules

Contents

- [[`Module.apply()`]](#mlx.nn.Module.apply)

By MLX Contributors

© Copyright 2023, Apple.\