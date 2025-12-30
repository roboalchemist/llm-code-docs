# Source: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.logsumexp.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../_sources/python/_autosummary/mlx.core.logsumexp.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.core.logsumexp

## Contents

- [[`logsumexp()`]](#mlx.core.logsumexp)

# mlx.core.logsumexp[\#](#mlx-core-logsumexp "Link to this heading")

[[logsumexp]][(]*[[a]][[:]][ ][[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]*, *[[/]]*, *[[axis]][[:]][ ][[[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[ ][[\|]][ ][[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[ ][[\|]][ ][Sequence][[\[]][[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[[\]]]][ ][[=]][ ][[None]]*, *[[keepdims]][[:]][ ][[[bool]](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")][ ][[=]][ ][[False]]*, *[[\*]]*, *[[stream]][[:]][ ][[[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[ ][[\|]][ ][[Stream]](stream_class.html#mlx.core.Stream "mlx.core.Stream")[ ][[\|]][ ][[Device]](mlx.core.Device.html#mlx.core.Device "mlx.core.Device")][ ][[=]][ ][[None]]*[)] [[→] [[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]][\#](#mlx.core.logsumexp "Link to this definition")

:   A log-sum-exp reduction over the given axes.

    The log-sum-exp reduction is a numerically stable version of:

    :::: 
    ::: highlight
        log(sum(exp(a), axis))
    :::
    ::::

    Parameters[:]

    :   - **a** ([*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")) -- Input array.

        - **axis** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") *or* [*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")*(*[*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*),* *optional*) -- Optional axis or axes to reduce over. If unspecified this defaults to reducing over the entire array.

        - **keepdims** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*,* *optional*) -- Keep reduced axes as singleton dimensions, defaults to False.

    Returns[:]

    :   The output array with the corresponding axes reduced.

    Return type[:]

    :   [*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")

[](mlx.core.logical_or.html "previous page")

previous

mlx.core.logical_or

[](mlx.core.matmul.html "next page")

next

mlx.core.matmul

Contents

- [[`logsumexp()`]](#mlx.core.logsumexp)

By MLX Contributors

© Copyright 2023, Apple.\