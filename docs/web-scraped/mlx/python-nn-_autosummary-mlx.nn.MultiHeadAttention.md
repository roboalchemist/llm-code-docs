# Source: https://ml-explore.github.io/mlx/build/html/python/nn/_autosummary/mlx.nn.MultiHeadAttention.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../../_sources/python/nn/_autosummary/mlx.nn.MultiHeadAttention.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.nn.MultiHeadAttention

## Contents

- [[`MultiHeadAttention`]](#mlx.nn.MultiHeadAttention)

# mlx.nn.MultiHeadAttention[\#](#mlx-nn-multiheadattention "Link to this heading")

*[class][ ]*[[MultiHeadAttention]][(]*[[dims]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]*, *[[num_heads]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]*, *[[query_input_dims]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][ ][[=]][ ][[None]]*, *[[key_input_dims]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][ ][[=]][ ][[None]]*, *[[value_input_dims]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][ ][[=]][ ][[None]]*, *[[value_dims]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][ ][[=]][ ][[None]]*, *[[value_output_dims]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][ ][[=]][ ][[None]]*, *[[bias]][[:]][ ][[[bool]](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")][ ][[=]][ ][[False]]*[)][\#](#mlx.nn.MultiHeadAttention "Link to this definition")

:   Implements the scaled dot product attention with multiple heads.

    Given inputs for queries, keys and values the [`MultiHeadAttention`] produces new values by aggregating information from the input values according to the similarities of the input queries and keys.

    All inputs as well as the output are linearly projected without biases by default.

    [`MultiHeadAttention`] also takes an optional additive attention mask that should be broadcastable with [`(batch,`]` `[`num_heads,`]` `[`#`]` `[`queries,`]` `[`#`]` `[`keys)`]. The mask should have [`-inf`] or very large negative numbers at the positions that should *not* be attended to.

    Parameters[:]

    :   - **dims** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")) -- The model dimensions. This is also the default value for the queries, keys, values, and the output.

        - **num_heads** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")) -- The number of attention heads to use.

        - **query_input_dims** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*,* *optional*) -- The input dimensions of the queries. Default: [`dims`].

        - **key_input_dims** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*,* *optional*) -- The input dimensions of the keys. Default: [`dims`].

        - **value_input_dims** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*,* *optional*) -- The input dimensions of the values. Default: [`key_input_dims`].

        - **value_dims** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*,* *optional*) -- The dimensions of the values after the projection. Default: [`dims`].

        - **value_output_dims** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*,* *optional*) -- The dimensions the new values will be projected to. Default: [`dims`].

        - **bias** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*,* *optional*) -- Whether or not to use a bias in the projections. Default: [`False`].

    Methods

    ::: pst-scrollable-table-container
      -------------------------------------------------------------------------------------------------------- --
      [`create_additive_causal_mask`](N\[, dtype\])   
      -------------------------------------------------------------------------------------------------------- --
    :::

[](mlx.nn.Mish.html "previous page")

previous

mlx.nn.Mish

[](mlx.nn.PReLU.html "next page")

next

mlx.nn.PReLU

Contents

- [[`MultiHeadAttention`]](#mlx.nn.MultiHeadAttention)

By MLX Contributors

© Copyright 2023, Apple.\