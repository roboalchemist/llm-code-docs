# Source: https://ml-explore.github.io/mlx/build/html/python/nn/_autosummary/mlx.nn.SinusoidalPositionalEncoding.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../../_sources/python/nn/_autosummary/mlx.nn.SinusoidalPositionalEncoding.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.nn.SinusoidalPositionalEncoding

## Contents

- [[`SinusoidalPositionalEncoding`]](#mlx.nn.SinusoidalPositionalEncoding)

# mlx.nn.SinusoidalPositionalEncoding[\#](#mlx-nn-sinusoidalpositionalencoding "Link to this heading")

*[class][ ]*[[SinusoidalPositionalEncoding]][(]*[[dims]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]*, *[[min_freq]][[:]][ ][[[float]](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")][ ][[=]][ ][[0.0001]]*, *[[max_freq]][[:]][ ][[[float]](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")][ ][[=]][ ][[1]]*, *[[scale]][[:]][ ][[[float]](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][ ][[=]][ ][[None]]*, *[[cos_first]][[:]][ ][[[bool]](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")][ ][[=]][ ][[False]]*, *[[full_turns]][[:]][ ][[[bool]](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")][ ][[=]][ ][[False]]*[)][\#](#mlx.nn.SinusoidalPositionalEncoding "Link to this definition")

:   Implements sinusoidal positional encoding.

    For more details see the paper [Attention Is All You Need](https://arxiv.org/abs/1706.03762).

    Parameters[:]

    :   - **dims** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")) -- The dimensionality of the resulting positional embeddings.

        - **min_freq** ([*float*](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")*,* *optional*) -- The minimum frequency expected. Default: [`0.0001`].

        - **max_freq** ([*float*](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")*,* *optional*) -- The maximum frequency expected. Default: [`1`].

        - **scale** ([*float*](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")*,* *optional*) -- A multiplicative scale for the embeddings. Default: [`sqrt(2/dims)`].

        - **cos_first** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*,* *optional*) -- If [`True`] embed using [`[cos(x);`]` `[`sin(x)]`] instead of the reverse. Default: [`False`].

        - **full_turns** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*,* *optional*) -- If [`True`] multiply the frequencies with [\\(2\\pi\\)]. Default: [`False`].

    Methods

    ::: pst-scrollable-table-container
    :::

[](mlx.nn.SiLU.html "previous page")

previous

mlx.nn.SiLU

[](mlx.nn.Softmin.html "next page")

next

mlx.nn.Softmin

Contents

- [[`SinusoidalPositionalEncoding`]](#mlx.nn.SinusoidalPositionalEncoding)

By MLX Contributors

© Copyright 2023, Apple.\