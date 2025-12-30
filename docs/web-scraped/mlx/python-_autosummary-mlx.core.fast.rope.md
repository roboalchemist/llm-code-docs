# Source: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.fast.rope.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../_sources/python/_autosummary/mlx.core.fast.rope.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.core.fast.rope

## Contents

- [[`rope()`]](#mlx.core.fast.rope)

# mlx.core.fast.rope[\#](#mlx-core-fast-rope "Link to this heading")

[[rope]][(]*[[a]][[:]][ ][[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]*, *[[dims]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]*, *[[\*]]*, *[[traditional]][[:]][ ][[[bool]](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")]*, *[[base]][[:]][ ][[[float]](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")]*, *[[scale]][[:]][ ][[[float]](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")]*, *[[offset]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[ ][[\|]][ ][[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]*, *[[freqs]][[:]][ ][[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][ ][[=]][ ][[None]]*, *[[stream]][[:]][ ][[[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[ ][[\|]][ ][[Stream]](stream_class.html#mlx.core.Stream "mlx.core.Stream")[ ][[\|]][ ][[Device]](mlx.core.Device.html#mlx.core.Device "mlx.core.Device")][ ][[=]][ ][[None]]*[)] [[→] [[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]][\#](#mlx.core.fast.rope "Link to this definition")

:   Apply rotary positional encoding to the input.

    The input is expected to be at least 3D with shape [`(B,`]` `[`*,`]` `[`T,`]` `[`D)`] where:

    :   - [`B`] is the batch size.

        - [`T`] is the sequence length.

        - [`D`] is the feature dimension.

    Parameters[:]

    :   - **a** ([*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")) -- The input array.

        - **dims** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")) -- The feature dimensions to be rotated. If the input feature is larger than dims then the rest is left unchanged.

        - **traditional** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")) -- If set to [`True`] choose the traditional implementation which rotates consecutive dimensions.

        - **base** ([*float*](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")*,* *optional*) -- The base used to compute angular frequency for each dimension in the positional encodings. Exactly one of [`base`] and [`freqs`] must be [`None`].

        - **scale** ([*float*](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")) -- The scale used to scale the positions.

        - **offset** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") *or* [*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")) -- The position offset to start at. If an [[`array`]](https://docs.python.org/3/library/array.html#module-array "(in Python v3.14)") is given it can be a scalar or vector of [`B`] offsets for each example in the batch.

        - **freqs** ([*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")*,* *optional*) -- Optional frequencies to use with RoPE. If set, the [`base`] parameter must be [`None`]. Default: [`None`].

    Returns[:]

    :   The output array.

    Return type[:]

    :   [*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")

[](mlx.core.fast.layer_norm.html "previous page")

previous

mlx.core.fast.layer_norm

[](mlx.core.fast.scaled_dot_product_attention.html "next page")

next

mlx.core.fast.scaled_dot_product_attention

Contents

- [[`rope()`]](#mlx.core.fast.rope)

By MLX Contributors

© Copyright 2023, Apple.\