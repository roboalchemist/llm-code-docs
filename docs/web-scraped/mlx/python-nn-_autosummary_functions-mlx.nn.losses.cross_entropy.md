# Source: https://ml-explore.github.io/mlx/build/html/python/nn/_autosummary_functions/mlx.nn.losses.cross_entropy.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../../_sources/python/nn/_autosummary_functions/mlx.nn.losses.cross_entropy.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.nn.losses.cross_entropy

## Contents

- [[`cross_entropy`]](#mlx.nn.losses.cross_entropy)

# mlx.nn.losses.cross_entropy[\#](#mlx-nn-losses-cross-entropy "Link to this heading")

*[class][ ]*[[cross_entropy]][(]*[[logits]][[:]][ ][[[array]](../../_autosummary/mlx.core.array.html#mlx.core.array "mlx.core.array")]*, *[[targets]][[:]][ ][[[array]](../../_autosummary/mlx.core.array.html#mlx.core.array "mlx.core.array")]*, *[[weights]][[:]][ ][[[array]](../../_autosummary/mlx.core.array.html#mlx.core.array "mlx.core.array")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][ ][[=]][ ][[None]]*, *[[axis]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")][ ][[=]][ ][[-1]]*, *[[label_smoothing]][[:]][ ][[[float]](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")][ ][[=]][ ][[0.0]]*, *[[reduction]][[:]][ ][[[Literal]](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.14)")[[\[]][[\'none\']][[,]][ ][[\'mean\']][[,]][ ][[\'sum\']][[\]]]][ ][[=]][ ][[\'none\']]*[)][\#](#mlx.nn.losses.cross_entropy "Link to this definition")

:   Computes the cross entropy loss.

    Parameters[:]

    :   - **logits** ([*array*](../../_autosummary/mlx.core.array.html#mlx.core.array "mlx.core.array")) -- The unnormalized logits.

        - **targets** ([*array*](../../_autosummary/mlx.core.array.html#mlx.core.array "mlx.core.array")) -- The ground truth values. These can be class indices or probabilities for each class. If the [`targets`] are class indices, then [`targets`] shape should match the [`logits`] shape with the [`axis`] dimension removed. If the [`targets`] are probabilities (or one-hot encoded), then the [`targets`] shape should be the same as the [`logits`] shape.

        - **weights** ([*array*](../../_autosummary/mlx.core.array.html#mlx.core.array "mlx.core.array")*,* *optional*) -- Optional weights for each target. Default: [`None`].

        - **axis** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*,* *optional*) -- The axis over which to compute softmax. Default: [`-1`].

        - **label_smoothing** ([*float*](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")*,* *optional*) -- Label smoothing factor. Default: [`0`].

        - **reduction** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*,* *optional*) -- Specifies the reduction to apply to the output: [`'none'`] \| [`'mean'`] \| [`'sum'`]. Default: [`'none'`].

    Returns[:]

    :   The computed cross entropy loss.

    Return type[:]

    :   [*array*](../../_autosummary/mlx.core.array.html#mlx.core.array "mlx.core.array")

    Examples

    :::: 
    ::: highlight
        >>> import mlx.core as mx
        >>> import mlx.nn as nn
        >>>
        >>> # Class indices as targets
        >>> logits = mx.array([[2.0, -1.0], [-1.0, 2.0]])
        >>> targets = mx.array([0, 1])
        >>> nn.losses.cross_entropy(logits, targets)
        array([0.0485873, 0.0485873], dtype=float32)
        >>>
        >>> # Probabilities (or one-hot vectors) as targets
        >>> logits = mx.array([[2.0, -1.0], [-1.0, 2.0]])
        >>> targets = mx.array([[0.9, 0.1], [0.1, 0.9]])
        >>> nn.losses.cross_entropy(logits, targets)
        array([0.348587, 0.348587], dtype=float32)
    :::
    ::::

[](mlx.nn.losses.cosine_similarity_loss.html "previous page")

previous

mlx.nn.losses.cosine_similarity_loss

[](mlx.nn.losses.gaussian_nll_loss.html "next page")

next

mlx.nn.losses.gaussian_nll_loss

Contents

- [[`cross_entropy`]](#mlx.nn.losses.cross_entropy)

By MLX Contributors

© Copyright 2023, Apple.\