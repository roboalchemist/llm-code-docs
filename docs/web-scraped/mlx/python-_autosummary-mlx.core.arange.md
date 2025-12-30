# Source: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.arange.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../_sources/python/_autosummary/mlx.core.arange.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.core.arange

## Contents

- [[`arange()`]](#mlx.core.arange)

# mlx.core.arange[\#](#mlx-core-arange "Link to this heading")

[[arange]][(]*[[start]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[ ][[\|]][ ][[float]](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")]*, *[[stop]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[ ][[\|]][ ][[float]](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")]*, *[[step]][[:]][ ][[[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[ ][[\|]][ ][[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[ ][[\|]][ ][[float]](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")]*, *[[dtype]][[:]][ ][[[Dtype]](mlx.core.Dtype.html#mlx.core.Dtype "mlx.core.Dtype")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][ ][[=]][ ][[None]]*, *[[\*]]*, *[[stream]][[:]][ ][[[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[ ][[\|]][ ][[Stream]](stream_class.html#mlx.core.Stream "mlx.core.Stream")[ ][[\|]][ ][[Device]](mlx.core.Device.html#mlx.core.Device "mlx.core.Device")][ ][[=]][ ][[None]]*[)] [[→] [[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]][\#](#mlx.core.arange "Link to this definition")\
[[arange]][(]*[[stop]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[ ][[\|]][ ][[float]](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")]*, *[[step]][[:]][ ][[[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[ ][[\|]][ ][[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[ ][[\|]][ ][[float]](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")][ ][[=]][ ][[None]]*, *[[dtype]][[:]][ ][[[Dtype]](mlx.core.Dtype.html#mlx.core.Dtype "mlx.core.Dtype")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][ ][[=]][ ][[None]]*, *[[\*]]*, *[[stream]][[:]][ ][[[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[ ][[\|]][ ][[Stream]](stream_class.html#mlx.core.Stream "mlx.core.Stream")[ ][[\|]][ ][[Device]](mlx.core.Device.html#mlx.core.Device "mlx.core.Device")][ ][[=]][ ][[None]]*[)] [[→] [[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]]

:   Overloaded function.

    1.  [`arange(start`]` `[`:`]` `[`Union[int,`]` `[`float],`]` `[`stop`]` `[`:`]` `[`Union[int,`]` `[`float],`]` `[`step`]` `[`:`]` `[`Union[None,`]` `[`int,`]` `[`float],`]` `[`dtype:`]` `[`Optional[Dtype]`]` `[`=`]` `[`None,`]` `[`*,`]` `[`stream:`]` `[`Union[None,`]` `[`Stream,`]` `[`Device]`]` `[`=`]` `[`None)`]` `[`->`]` `[`array`]

        > ::: 
        > Generates ranges of numbers.
        >
        > Generate numbers in the half-open interval [`[start,`]` `[`stop)`] in increments of [`step`].
        >
        > Args:
        >
        > :   start (float or int, optional): Starting value which defaults to [`0`]. stop (float or int): Stopping value. step (float or int, optional): Increment which defaults to [`1`]. dtype (Dtype, optional): Specifies the data type of the output. If unspecified will default to [`float32`] if any of [`start`], [`stop`], or [`step`] are [`float`]. Otherwise will default to [`int32`].
        >
        > Returns:
        >
        > :   array: The range of values.
        >
        > Note:
        >
        > :   Following the Numpy convention the actual increment used to generate numbers is [`dtype(start`]` `[`+`]` `[`step)`]` `[`-`]` `[`dtype(start)`]. This can lead to unexpected results for example if start + step is a fractional value and the dtype is integral.
        > :::

    2.  [`arange(stop`]` `[`:`]` `[`Union[int,`]` `[`float],`]` `[`step`]` `[`:`]` `[`Union[None,`]` `[`int,`]` `[`float]`]` `[`=`]` `[`None,`]` `[`dtype:`]` `[`Optional[Dtype]`]` `[`=`]` `[`None,`]` `[`*,`]` `[`stream:`]` `[`Union[None,`]` `[`Stream,`]` `[`Device]`]` `[`=`]` `[`None)`]` `[`->`]` `[`array`]

[](mlx.core.any.html "previous page")

previous

mlx.core.any

[](mlx.core.arccos.html "next page")

next

mlx.core.arccos

Contents

- [[`arange()`]](#mlx.core.arange)

By MLX Contributors

© Copyright 2023, Apple.\