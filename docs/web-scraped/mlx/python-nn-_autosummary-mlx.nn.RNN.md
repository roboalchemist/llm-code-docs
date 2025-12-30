# Source: https://ml-explore.github.io/mlx/build/html/python/nn/_autosummary/mlx.nn.RNN.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../../_sources/python/nn/_autosummary/mlx.nn.RNN.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.nn.RNN

## Contents

- [[`RNN`]](#mlx.nn.RNN)

# mlx.nn.RNN[\#](#mlx-nn-rnn "Link to this heading")

*[class][ ]*[[RNN]][(]*[[input_size]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]*, *[[hidden_size]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]*, *[[bias]][[:]][ ][[[bool]](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")][ ][[=]][ ][[True]]*, *[[nonlinearity]][[:]][ ][[[Callable]](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python v3.14)")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][ ][[=]][ ][[None]]*[)][\#](#mlx.nn.RNN "Link to this definition")

:   An Elman recurrent layer.

    The input is a sequence of shape [`NLD`] or [`LD`] where:

    - [`N`] is the optional batch dimension

    - [`L`] is the sequence length

    - [`D`] is the input's feature dimension

    Concretely, for each element along the sequence length axis, this layer applies the function:

    ::: 
    \\\[h\_ = \\text (W\_x_t + W\_h_t + b)\\\]
    :::

    The hidden state [\\(h\\)] has shape [`NH`] or [`H`], depending on whether the input is batched or not. Returns the hidden state at each time step, of shape [`NLH`] or [`LH`].

    Parameters[:]

    :   - **input_size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")) -- Dimension of the input, [`D`].

        - **hidden_size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")) -- Dimension of the hidden state, [`H`].

        - **bias** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*,* *optional*) -- Whether to use a bias. Default: [`True`].

        - **nonlinearity** (*callable,* *optional*) -- Non-linearity to use. If [`None`], then func:tanh is used. Default: [`None`].

    Methods

    ::: pst-scrollable-table-container
    :::

[](mlx.nn.ReLU6.html "previous page")

previous

mlx.nn.ReLU6

[](mlx.nn.RoPE.html "next page")

next

mlx.nn.RoPE

Contents

- [[`RNN`]](#mlx.nn.RNN)

By MLX Contributors

© Copyright 2023, Apple.\