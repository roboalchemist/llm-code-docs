# Source: https://ml-explore.github.io/mlx/build/html/python/nn/_autosummary/mlx.nn.Module.unfreeze.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../../_sources/python/nn/_autosummary/mlx.nn.Module.unfreeze.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.nn.Module.unfreeze

## Contents

- [[`Module.unfreeze()`]](#mlx.nn.Module.unfreeze)

# mlx.nn.Module.unfreeze[\#](#mlx-nn-module-unfreeze "Link to this heading")

[[Module.]][[unfreeze]][(]*[[\*]]*, *[[recurse]][[:]][ ][[[bool]](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")][ ][[=]][ ][[True]]*, *[[keys]][[:]][ ][[[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[ ][[\|]][ ][[List]](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[\[]][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[\]]][ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][ ][[=]][ ][[None]]*, *[[strict]][[:]][ ][[[bool]](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")][ ][[=]][ ][[False]]*[)] [[→] [[[Module]](../module.html#mlx.nn.Module "mlx.nn.layers.base.Module")]][\#](#mlx.nn.Module.unfreeze "Link to this definition")

:   Unfreeze the Module's parameters or some of them.

    This function is idempotent ie unfreezing a model that is not frozen is a noop.

    Example

    For instance to only train the biases of a Transformer one can do:

    :::: 
    ::: highlight
        model = nn.Transformer()
        model.freeze()
        model.unfreeze(keys="bias")
    :::
    ::::

    Parameters[:]

    :   - **recurse** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*,* *optional*) -- If True then unfreeze the parameters of the submodules as well. Default: [`True`].

        - **keys** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") *or* [*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")*\[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*\],* *optional*) -- If provided then only these parameters will be unfrozen otherwise all the parameters of a module. For instance unfreeze all biases by calling [`module.unfreeze(keys="bias")`].

        - **strict** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*,* *optional*) -- If set to [`True`] validate that the passed keys exist. Default: [`False`].

    Returns[:]

    :   The module instance after unfreezing the parameters.

[](mlx.nn.Module.trainable_parameters.html "previous page")

previous

mlx.nn.Module.trainable_parameters

[](mlx.nn.Module.update.html "next page")

next

mlx.nn.Module.update

Contents

- [[`Module.unfreeze()`]](#mlx.nn.Module.unfreeze)

By MLX Contributors

© Copyright 2023, Apple.\