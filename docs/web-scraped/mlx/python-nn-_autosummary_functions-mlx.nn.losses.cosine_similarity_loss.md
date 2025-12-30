# Source: https://ml-explore.github.io/mlx/build/html/python/nn/_autosummary_functions/mlx.nn.losses.cosine_similarity_loss.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../../_sources/python/nn/_autosummary_functions/mlx.nn.losses.cosine_similarity_loss.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.nn.losses.cosine_similarity_loss

## Contents

- [[`cosine_similarity_loss`]](#mlx.nn.losses.cosine_similarity_loss)

# mlx.nn.losses.cosine_similarity_loss[\#](#mlx-nn-losses-cosine-similarity-loss "Link to this heading")

*[class][ ]*[[cosine_similarity_loss]][(]*[[x1]][[:]][ ][[[array]](../../_autosummary/mlx.core.array.html#mlx.core.array "mlx.core.array")]*, *[[x2]][[:]][ ][[[array]](../../_autosummary/mlx.core.array.html#mlx.core.array "mlx.core.array")]*, *[[axis]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")][ ][[=]][ ][[1]]*, *[[eps]][[:]][ ][[[float]](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")][ ][[=]][ ][[1e-08]]*, *[[reduction]][[:]][ ][[[Literal]](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.14)")[[\[]][[\'none\']][[,]][ ][[\'mean\']][[,]][ ][[\'sum\']][[\]]]][ ][[=]][ ][[\'none\']]*[)][\#](#mlx.nn.losses.cosine_similarity_loss "Link to this definition")

:   Computes the cosine similarity between the two inputs.

    The cosine similarity loss is given by

    ::: 
    \\\[\\frac\\\]
    :::

    Parameters[:]

    :   - **x1** (*mx.array*) -- The first set of inputs.

        - **x2** (*mx.array*) -- The second set of inputs.

        - **axis** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*,* *optional*) -- The embedding axis. Default: [`1`].

        - **eps** ([*float*](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")*,* *optional*) -- The minimum value of the denominator used for numerical stability. Default: [`1e-8`].

        - **reduction** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*,* *optional*) -- Specifies the reduction to apply to the output: [`'none'`] \| [`'mean'`] \| [`'sum'`]. Default: [`'none'`].

    Returns[:]

    :   The computed cosine similarity loss.

    Return type[:]

    :   mx.array

[](mlx.nn.losses.binary_cross_entropy.html "previous page")

previous

mlx.nn.losses.binary_cross_entropy

[](mlx.nn.losses.cross_entropy.html "next page")

next

mlx.nn.losses.cross_entropy

Contents

- [[`cosine_similarity_loss`]](#mlx.nn.losses.cosine_similarity_loss)

By MLX Contributors

© Copyright 2023, Apple.\