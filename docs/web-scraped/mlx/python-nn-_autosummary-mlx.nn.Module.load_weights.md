# Source: https://ml-explore.github.io/mlx/build/html/python/nn/_autosummary/mlx.nn.Module.load_weights.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../../_sources/python/nn/_autosummary/mlx.nn.Module.load_weights.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.nn.Module.load_weights

## Contents

- [[`Module.load_weights()`]](#mlx.nn.Module.load_weights)

# mlx.nn.Module.load_weights[\#](#mlx-nn-module-load-weights "Link to this heading")

[[Module.]][[load_weights]][(]*[[file_or_weights]][[:]][ ][[[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[ ][[\|]][ ][[List]](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[\[]][[Tuple]](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[\[]][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[,]][ ][[array]](../../_autosummary/mlx.core.array.html#mlx.core.array "mlx.core.array")[[\]]][[\]]]]*, *[[strict]][[:]][ ][[[bool]](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")][ ][[=]][ ][[True]]*[)] [[→] [[[Module]](../module.html#mlx.nn.Module "mlx.nn.layers.base.Module")]][\#](#mlx.nn.Module.load_weights "Link to this definition")

:   Update the model's weights from a [`.npz`], a [`.safetensors`] file, or a list.

    Parameters[:]

    :   - **file_or_weights** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") *or* [*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")*(*[*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")*(*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*,* *mx.array))*) -- The path to the weights [`.npz`] file ([`.npz`] or [`.safetensors`]) or a list of pairs of parameter names and arrays.

        - **strict** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*,* *optional*) -- If [`True`] then checks that the provided weights exactly match the parameters of the model. Otherwise, only the weights actually contained in the model are loaded and shapes are not checked. Default: [`True`].

    Returns[:]

    :   The module instance after updating the weights.

    Example

    :::: 
    ::: highlight
        import mlx.core as mx
        import mlx.nn as nn
        model = nn.Linear(10, 10)

        # Load from file
        model.load_weights("weights.npz")

        # Load from .safetensors file
        model.load_weights("weights.safetensors")

        # Load from list
        weights = [
            ("weight", mx.random.uniform(shape=(10, 10))),
            ("bias",  mx.zeros((10,))),
        ]
        model.load_weights(weights)

        # Missing weight
        weights = [
            ("weight", mx.random.uniform(shape=(10, 10))),
        ]

        # Raises a ValueError exception
        model.load_weights(weights)

        # Ok, only updates the weight but not the bias
        model.load_weights(weights, strict=False)
    :::
    ::::

[](mlx.nn.Module.leaf_modules.html "previous page")

previous

mlx.nn.Module.leaf_modules

[](mlx.nn.Module.modules.html "next page")

next

mlx.nn.Module.modules

Contents

- [[`Module.load_weights()`]](#mlx.nn.Module.load_weights)

By MLX Contributors

© Copyright 2023, Apple.\