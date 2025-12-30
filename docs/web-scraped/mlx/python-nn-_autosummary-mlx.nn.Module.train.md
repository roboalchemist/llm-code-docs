# Source: https://ml-explore.github.io/mlx/build/html/python/nn/_autosummary/mlx.nn.Module.train.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../../_sources/python/nn/_autosummary/mlx.nn.Module.train.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.nn.Module.train

## Contents

- [[`Module.train()`]](#mlx.nn.Module.train)

# mlx.nn.Module.train[\#](#mlx-nn-module-train "Link to this heading")

[[Module.]][[train]][(]*[[mode]][[:]][ ][[[bool]](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")][ ][[=]][ ][[True]]*[)] [[→] [[[Module]](../module.html#mlx.nn.Module "mlx.nn.layers.base.Module")]][\#](#mlx.nn.Module.train "Link to this definition")

:   Set the model in or out of training mode.

    Training mode only applies to certain layers. For example [[`Dropout`]](mlx.nn.Dropout.html#mlx.nn.Dropout "mlx.nn.Dropout") applies a random mask in training mode, but is the identity in evaluation mode.

    Parameters[:]

    :   **mode** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")) -- Indicate if the model should be in training or evaluation mode. Default: [`True`].

    Returns[:]

    :   The module instance after updating the training mode.

[](mlx.nn.Module.set_dtype.html "previous page")

previous

mlx.nn.Module.set_dtype

[](mlx.nn.Module.trainable_parameters.html "next page")

next

mlx.nn.Module.trainable_parameters

Contents

- [[`Module.train()`]](#mlx.nn.Module.train)

By MLX Contributors

© Copyright 2023, Apple.\