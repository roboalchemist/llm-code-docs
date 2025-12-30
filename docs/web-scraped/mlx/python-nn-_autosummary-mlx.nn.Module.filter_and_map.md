# Source: https://ml-explore.github.io/mlx/build/html/python/nn/_autosummary/mlx.nn.Module.filter_and_map.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../../_sources/python/nn/_autosummary/mlx.nn.Module.filter_and_map.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.nn.Module.filter_and_map

## Contents

- [[`Module.filter_and_map()`]](#mlx.nn.Module.filter_and_map)

# mlx.nn.Module.filter_and_map[\#](#mlx-nn-module-filter-and-map "Link to this heading")

[[Module.]][[filter_and_map]][(]*[[filter_fn]][[:]][ ][[[Callable]](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python v3.14)")[[\[]][[\[]][[Module]](../module.html#mlx.nn.Module "mlx.nn.layers.base.Module")[[,]][ ][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[,]][ ][[Any]](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")[[\]]][[,]][ ][[bool]](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[\]]]]*, *[[map_fn]][[:]][ ][[[Callable]](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python v3.14)")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][ ][[=]][ ][[None]]*, *[[is_leaf_fn]][[:]][ ][[[Callable]](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python v3.14)")[[\[]][[\[]][[Module]](../module.html#mlx.nn.Module "mlx.nn.layers.base.Module")[[,]][ ][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[,]][ ][[Any]](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")[[\]]][[,]][ ][[bool]](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[\]]][ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][ ][[=]][ ][[None]]*[)][\#](#mlx.nn.Module.filter_and_map "Link to this definition")

:   Recursively filter the contents of the module using [`filter_fn`], namely only select keys and values where [`filter_fn`] returns true.

    This is used to implement [[`parameters()`]](mlx.nn.Module.parameters.html#mlx.nn.Module.parameters "mlx.nn.Module.parameters") and [[`trainable_parameters()`]](mlx.nn.Module.trainable_parameters.html#mlx.nn.Module.trainable_parameters "mlx.nn.Module.trainable_parameters") but it can also be used to extract any subset of the module's parameters.

    Parameters[:]

    :   - **filter_fn** (*Callable*) -- Given a value, the key in which it is found and the containing module, decide whether to keep the value or drop it.

        - **map_fn** (*Callable,* *optional*) -- Optionally transform the value before returning it.

        - **is_leaf_fn** (*Callable,* *optional*) -- Given a value, the key in which it is found and the containing module decide if it is a leaf.

    Returns[:]

    :   A dictionary containing the contents of the module recursively filtered

[](mlx.nn.Module.eval.html "previous page")

previous

mlx.nn.Module.eval

[](mlx.nn.Module.freeze.html "next page")

next

mlx.nn.Module.freeze

Contents

- [[`Module.filter_and_map()`]](#mlx.nn.Module.filter_and_map)

By MLX Contributors

© Copyright 2023, Apple.\