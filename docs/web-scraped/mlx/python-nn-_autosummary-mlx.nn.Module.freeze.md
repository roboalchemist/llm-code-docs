# Source: https://ml-explore.github.io/mlx/build/html/python/nn/_autosummary/mlx.nn.Module.freeze.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../../_sources/python/nn/_autosummary/mlx.nn.Module.freeze.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.nn.Module.freeze

## Contents

- [[`Module.freeze()`]](#mlx.nn.Module.freeze)

# mlx.nn.Module.freeze[\#](#mlx-nn-module-freeze "Link to this heading")

[[Module.]][[freeze]][(]*[[\*]]*, *[[recurse]][[:]][ ][[[bool]](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")][ ][[=]][ ][[True]]*, *[[keys]][[:]][ ][[[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[ ][[\|]][ ][[List]](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[\[]][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[\]]][ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][ ][[=]][ ][[None]]*, *[[strict]][[:]][ ][[[bool]](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")][ ][[=]][ ][[False]]*[)] [[→] [[[Module]](../module.html#mlx.nn.Module "mlx.nn.layers.base.Module")]][\#](#mlx.nn.Module.freeze "Link to this definition")

:   Freeze the Module's parameters or some of them. Freezing a parameter means not computing gradients for it.

    This function is idempotent i.e. freezing a frozen model is a no-op.

    Example

    For instance to only train the attention parameters from a Transformer:

    :::: 
    ::: highlight
        model = nn.Transformer()
        model.freeze()
        model.apply_to_modules(lambda k, v: v.unfreeze() if k.endswith("attention") else None)
    :::
    ::::

    Parameters[:]

    :   - **recurse** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*,* *optional*) -- If True then freeze the parameters of the submodules as well. Default: [`True`].

        - **keys** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") *or* [*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")*\[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*\],* *optional*) -- If provided then only these parameters will be frozen otherwise all the parameters of a module. For instance freeze all biases by calling [`module.freeze(keys="bias")`].

        - **strict** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*,* *optional*) -- If set to [`True`] validate that the passed keys exist. Default: [`False`].

    Returns[:]

    :   The module instance after freezing the parameters.

[](mlx.nn.Module.filter_and_map.html "previous page")

previous

mlx.nn.Module.filter_and_map

[](mlx.nn.Module.leaf_modules.html "next page")

next

mlx.nn.Module.leaf_modules

Contents

- [[`Module.freeze()`]](#mlx.nn.Module.freeze)

By MLX Contributors

© Copyright 2023, Apple.\