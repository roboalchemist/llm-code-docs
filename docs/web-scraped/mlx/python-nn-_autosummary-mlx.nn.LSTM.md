# Source: https://ml-explore.github.io/mlx/build/html/python/nn/_autosummary/mlx.nn.LSTM.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../../_sources/python/nn/_autosummary/mlx.nn.LSTM.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.nn.LSTM

## Contents

- [[`LSTM`]](#mlx.nn.LSTM)

# mlx.nn.LSTM[\#](#mlx-nn-lstm "Link to this heading")

*[class][ ]*[[LSTM]][(]*[[input_size]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]*, *[[hidden_size]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]*, *[[bias]][[:]][ ][[[bool]](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")][ ][[=]][ ][[True]]*[)][\#](#mlx.nn.LSTM "Link to this definition")

:   An LSTM recurrent layer.

    The input has shape [`NLD`] or [`LD`] where:

    - [`N`] is the optional batch dimension

    - [`L`] is the sequence length

    - [`D`] is the input's feature dimension

    Concretely, for each element of the sequence, this layer computes:

    ::: 
    \\\[\\begin\\begin i_t &= \\sigma (W\_x_t + W\_h_t + b\_) \\\\ f_t &= \\sigma (W\_x_t + W\_h_t + b\_) \\\\ g_t &= \\text (W\_x_t + W\_h_t + b\_) \\\\ o_t &= \\sigma (W\_x_t + W\_h_t + b\_) \\\\ c\_ &= f_t \\odot c_t + i_t \\odot g_t \\\\ h\_ &= o_t \\text(c\_) \\end\\end\\\]
    :::

    The hidden state [\\(h\\)] and cell state [\\(c\\)] have shape [`NH`] or [`H`], depending on whether the input is batched or not.

    The layer returns two arrays, the hidden state and the cell state at each time step, both of shape [`NLH`] or [`LH`].

    Parameters[:]

    :   - **input_size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")) -- Dimension of the input, [`D`].

        - **hidden_size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")) -- Dimension of the hidden state, [`H`].

        - **bias** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")) -- Whether to use biases or not. Default: [`True`].

    Methods

    ::: pst-scrollable-table-container
    :::

[](mlx.nn.LogSoftmax.html "previous page")

previous

mlx.nn.LogSoftmax

[](mlx.nn.MaxPool1d.html "next page")

next

mlx.nn.MaxPool1d

Contents

- [[`LSTM`]](#mlx.nn.LSTM)

By MLX Contributors

© Copyright 2023, Apple.\