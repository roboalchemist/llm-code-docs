# Source: https://ml-explore.github.io/mlx/build/html/python/nn/_autosummary/mlx.nn.Module.update.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../../_sources/python/nn/_autosummary/mlx.nn.Module.update.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.nn.Module.update

## Contents

- [[`Module.update()`]](#mlx.nn.Module.update)

# mlx.nn.Module.update[\#](#mlx-nn-module-update "Link to this heading")

[[Module.]][[update]][(]*[[parameters]][[:]][ ][[[dict]](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")]*, *[[strict]][[:]][ ][[[bool]](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")][ ][[=]][ ][[True]]*[)] [[→] [[[Module]](../module.html#mlx.nn.Module "mlx.nn.layers.base.Module")]][\#](#mlx.nn.Module.update "Link to this definition")

:   Replace the parameters of this Module with the provided ones in the dict of dicts and lists.

    Commonly used by the optimizer to change the model to the updated (optimized) parameters. Also used by the [[`mlx.nn.value_and_grad()`]](../../_autosummary/mlx.nn.value_and_grad.html#mlx.nn.value_and_grad "mlx.nn.value_and_grad") to set the tracers in the model in order to compute gradients.

    The passed in parameters dictionary need not be a full dictionary similar to [[`parameters()`]](mlx.nn.Module.parameters.html#mlx.nn.Module.parameters "mlx.nn.Module.parameters"). Only the provided locations will be updated.

    Parameters[:]

    :   - **parameters** ([*dict*](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")) -- A complete or partial dictionary of the modules parameters.

        - **strict** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")) -- If [`True`] checks that [`parameters`] is a subset of the module's parameters. Default: [`True`].

    Returns[:]

    :   The module instance after updating the parameters.

[](mlx.nn.Module.unfreeze.html "previous page")

previous

mlx.nn.Module.unfreeze

[](mlx.nn.Module.update_modules.html "next page")

next

mlx.nn.Module.update_modules

Contents

- [[`Module.update()`]](#mlx.nn.Module.update)

By MLX Contributors

© Copyright 2023, Apple.\