# Source: https://ml-explore.github.io/mlx/build/html/python/nn/_autosummary_functions/mlx.nn.losses.binary_cross_entropy.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../../_sources/python/nn/_autosummary_functions/mlx.nn.losses.binary_cross_entropy.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.nn.losses.binary_cross_entropy

## Contents

- [[`binary_cross_entropy`]](#mlx.nn.losses.binary_cross_entropy)

# mlx.nn.losses.binary_cross_entropy[\#](#mlx-nn-losses-binary-cross-entropy "Link to this heading")

*[class][ ]*[[binary_cross_entropy]][(]*[[inputs]][[:]][ ][[[array]](../../_autosummary/mlx.core.array.html#mlx.core.array "mlx.core.array")]*, *[[targets]][[:]][ ][[[array]](../../_autosummary/mlx.core.array.html#mlx.core.array "mlx.core.array")]*, *[[weights]][[:]][ ][[[array]](../../_autosummary/mlx.core.array.html#mlx.core.array "mlx.core.array")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][ ][[=]][ ][[None]]*, *[[with_logits]][[:]][ ][[[bool]](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")][ ][[=]][ ][[True]]*, *[[reduction]][[:]][ ][[[Literal]](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.14)")[[\[]][[\'none\']][[,]][ ][[\'mean\']][[,]][ ][[\'sum\']][[\]]]][ ][[=]][ ][[\'mean\']]*[)][\#](#mlx.nn.losses.binary_cross_entropy "Link to this definition")

:   Computes the binary cross entropy loss.

    By default, this function takes the pre-sigmoid logits, which results in a faster and more precise loss. For improved numerical stability when [`with_logits=False`], the loss calculation clips the input probabilities (in log-space) to a minimum value of [`-100`].

    Parameters[:]

    :   - **inputs** ([*array*](../../_autosummary/mlx.core.array.html#mlx.core.array "mlx.core.array")) -- The predicted values. If [`with_logits`] is [`True`], then [`inputs`] are unnormalized logits. Otherwise, [`inputs`] are probabilities.

        - **targets** ([*array*](../../_autosummary/mlx.core.array.html#mlx.core.array "mlx.core.array")) -- The binary target values in .

        - **with_logits** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*,* *optional*) -- Whether [`inputs`] are logits. Default: [`True`].

        - **weights** ([*array*](../../_autosummary/mlx.core.array.html#mlx.core.array "mlx.core.array")*,* *optional*) -- Optional weights for each target. Default: [`None`].

        - **reduction** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*,* *optional*) -- Specifies the reduction to apply to the output: [`'none'`] \| [`'mean'`] \| [`'sum'`]. Default: [`'mean'`].

    Returns[:]

    :   The computed binary cross entropy loss.

    Return type[:]

    :   [*array*](../../_autosummary/mlx.core.array.html#mlx.core.array "mlx.core.array")

    Examples

    :::: 
    ::: highlight
        >>> import mlx.core as mx
        >>> import mlx.nn as nn
    :::
    ::::

    :::: 
    ::: highlight
        >>> logits = mx.array([0.105361, 0.223144, 1.20397, 0.916291])
        >>> targets = mx.array([0, 0, 1, 1])
        >>> loss = nn.losses.binary_cross_entropy(logits, targets, reduction="mean")
        >>> loss
        array(0.539245, dtype=float32)
    :::
    ::::

    :::: 
    ::: highlight
        >>> probs = mx.array([0.1, 0.1, 0.4, 0.4])
        >>> targets = mx.array([0, 0, 1, 1])
        >>> loss = nn.losses.binary_cross_entropy(probs, targets, with_logits=False, reduction="mean")
        >>> loss
        array(0.510826, dtype=float32)
    :::
    ::::

[](../losses.html "previous page")

previous

Loss Functions

[](mlx.nn.losses.cosine_similarity_loss.html "next page")

next

mlx.nn.losses.cosine_similarity_loss

Contents

- [[`binary_cross_entropy`]](#mlx.nn.losses.binary_cross_entropy)

By MLX Contributors

© Copyright 2023, Apple.\