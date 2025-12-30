# Source: https://ml-explore.github.io/mlx/build/html/python/nn/_autosummary/mlx.nn.GRU.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../../_sources/python/nn/_autosummary/mlx.nn.GRU.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.nn.GRU

## Contents

- [[`GRU`]](#mlx.nn.GRU)

# mlx.nn.GRU[\#](#mlx-nn-gru "Link to this heading")

*[class][ ]*[[GRU]][(]*[[input_size]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]*, *[[hidden_size]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]*, *[[bias]][[:]][ ][[[bool]](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")][ ][[=]][ ][[True]]*[)][\#](#mlx.nn.GRU "Link to this definition")

:   A gated recurrent unit (GRU) RNN layer.

    The input has shape [`NLD`] or [`LD`] where:

    - [`N`] is the optional batch dimension

    - [`L`] is the sequence length

    - [`D`] is the input's feature dimension

    Concretely, for each element of the sequence, this layer computes:

    ::: 
    \\\[\\begin\\begin r_t &= \\sigma (W\_x_t + W\_h_t + b\_) \\\\ z_t &= \\sigma (W\_x_t + W\_h_t + b\_) \\\\ n_t &= \\text(W\_x_t + b\_ + r_t \\odot (W\_h_t + b\_)) \\\\ h\_ &= (1 - z_t) \\odot n_t + z_t \\odot h_t \\end\\end\\\]
    :::

    The hidden state [\\(h\\)] has shape [`NH`] or [`H`] depending on whether the input is batched or not. Returns the hidden state at each time step of shape [`NLH`] or [`LH`].

    Parameters[:]

    :   - **input_size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")) -- Dimension of the input, [`D`].

        - **hidden_size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")) -- Dimension of the hidden state, [`H`].

        - **bias** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")) -- Whether to use biases or not. Default: [`True`].

    Methods

    ::: pst-scrollable-table-container
    :::

[](mlx.nn.GroupNorm.html "previous page")

previous

mlx.nn.GroupNorm

[](mlx.nn.HardShrink.html "next page")

next

mlx.nn.HardShrink

Contents

- [[`GRU`]](#mlx.nn.GRU)

By MLX Contributors

© Copyright 2023, Apple.\