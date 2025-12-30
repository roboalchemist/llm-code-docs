# Source: https://ml-explore.github.io/mlx/build/html/python/nn/_autosummary/mlx.nn.Module.update_modules.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../../_sources/python/nn/_autosummary/mlx.nn.Module.update_modules.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.nn.Module.update_modules

## Contents

- [[`Module.update_modules()`]](#mlx.nn.Module.update_modules)

# mlx.nn.Module.update_modules[\#](#mlx-nn-module-update-modules "Link to this heading")

[[Module.]][[update_modules]][(]*[[modules]][[:]][ ][[[dict]](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")]*, *[[strict]][[:]][ ][[[bool]](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")][ ][[=]][ ][[True]]*[)] [[→] [[[Module]](../module.html#mlx.nn.Module "mlx.nn.layers.base.Module")]][\#](#mlx.nn.Module.update_modules "Link to this definition")

:   Replace the child modules of this [[`Module`]](../module.html#mlx.nn.Module "mlx.nn.Module") instance with the provided ones in the dict of dicts and lists.

    It is the equivalent of [[`Module.update()`]](mlx.nn.Module.update.html#mlx.nn.Module.update "mlx.nn.Module.update") but for modules instead of parameters and allows us to flexibly edit complex architectures by programmatically swapping layers.

    The passed in parameters dictionary need not be a full dictionary similar to [[`modules()`]](mlx.nn.Module.modules.html#mlx.nn.Module.modules "mlx.nn.Module.modules"). Only the provided locations will be updated.

    Parameters[:]

    :   - **modules** ([*dict*](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")) -- A complete or partial dictionary of the module's submodules.

        - **strict** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")) -- If [`True`] checks that [`modules`] is a subset of the child modules of this instance. Default: [`True`].

    Returns[:]

    :   The module instance after updating the submodules.

[](mlx.nn.Module.update.html "previous page")

previous

mlx.nn.Module.update

[](../layers.html "next page")

next

Layers

Contents

- [[`Module.update_modules()`]](#mlx.nn.Module.update_modules)

By MLX Contributors

© Copyright 2023, Apple.\