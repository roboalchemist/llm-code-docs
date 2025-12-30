# Source: https://ml-explore.github.io/mlx/build/html/python/nn/_autosummary/mlx.nn.Module.apply_to_modules.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../../_sources/python/nn/_autosummary/mlx.nn.Module.apply_to_modules.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.nn.Module.apply_to_modules

## Contents

- [[`Module.apply_to_modules()`]](#mlx.nn.Module.apply_to_modules)

# mlx.nn.Module.apply_to_modules[\#](#mlx-nn-module-apply-to-modules "Link to this heading")

[[Module.]][[apply_to_modules]][(]*[[apply_fn]][[:]][ ][[[Callable]](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python v3.14)")[[\[]][[\[]][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[,]][ ][[Module]](../module.html#mlx.nn.Module "mlx.nn.layers.base.Module")[[\]]][[,]][ ][[Any]](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")[[\]]]]*[)] [[→] [[[Module]](../module.html#mlx.nn.Module "mlx.nn.layers.base.Module")]][\#](#mlx.nn.Module.apply_to_modules "Link to this definition")

:   Apply a function to all the modules in this instance (including this instance).

    Parameters[:]

    :   **apply_fn** (*Callable*) -- The function to apply to the modules which takes two parameters. The first parameter is the string path of the module (e.g. [`"model.layers.0.linear"`]). The second parameter is the module object.

    Returns[:]

    :   The module instance after updating submodules.

[](mlx.nn.Module.apply.html "previous page")

previous

mlx.nn.Module.apply

[](mlx.nn.Module.children.html "next page")

next

mlx.nn.Module.children

Contents

- [[`Module.apply_to_modules()`]](#mlx.nn.Module.apply_to_modules)

By MLX Contributors

© Copyright 2023, Apple.\