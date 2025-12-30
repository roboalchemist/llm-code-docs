# Source: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.load.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../_sources/python/_autosummary/mlx.core.load.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.core.load

## Contents

- [[`load()`]](#mlx.core.load)

# mlx.core.load[\#](#mlx-core-load "Link to this heading")

[[load]][(]*[[file]][[:]][ ][[file][ ][[\|]][ ][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[ ][[\|]][ ][[Path]](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.14)")]*, *[[/]]*, *[[format]][[:]][ ][[[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][ ][[=]][ ][[None]]*, *[[return_metadata]][[:]][ ][[[bool]](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")][ ][[=]][ ][[False]]*, *[[\*]]*, *[[stream]][[:]][ ][[[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[ ][[\|]][ ][[Stream]](stream_class.html#mlx.core.Stream "mlx.core.Stream")[ ][[\|]][ ][[Device]](mlx.core.Device.html#mlx.core.Device "mlx.core.Device")][ ][[=]][ ][[None]]*[)] [[→] [[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")[ ][[\|]][ ][[dict]](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")[[\[]][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[,]][ ][[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")[[\]]][ ][[\|]][ ][Tuple][[\[]][[dict]](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")[[\[]][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[,]][ ][[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")[[\]]][[,]][ ][[dict]](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")[[\[]][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[,]][ ][Any][[\]]][[\]]]]][\#](#mlx.core.load "Link to this definition")

:   Load array(s) from a binary file.

    The supported formats are [`.npy`], [`.npz`], [`.safetensors`], and [`.gguf`].

    Parameters[:]

    :   - **file** (*file,* [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*,* [*Path*](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.14)")) -- File in which the array is saved.

        - **format** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*,* *optional*) -- Format of the file. If [`None`], the format is inferred from the file extension. Supported formats: [`npy`], [`npz`], and [`safetensors`]. Default: [`None`].

        - **return_metadata** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*,* *optional*) -- Load the metadata for formats which support matadata. The metadata will be returned as an additional dictionary. Default: [`False`].

    Returns[:]

    :   A single array if loading from a [`.npy`] file or a dict mapping names to arrays if loading from a [`.npz`] or [`.safetensors`] file. If [`return_metadata`] is [`True`] a tuple [`(arrays,`]` `[`metadata)`] will be returned where the second element is a dictionary containing the metadata.

    Return type[:]

    :   [*array*](mlx.core.array.html#mlx.core.array "mlx.core.array"), [*dict*](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)"), or [*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")

    ::: 
    Warning

    When loading unsupported quantization formats from GGUF, tensors will automatically cast to [`mx.float16`]
    :::

[](mlx.core.linspace.html "previous page")

previous

mlx.core.linspace

[](mlx.core.log.html "next page")

next

mlx.core.log

Contents

- [[`load()`]](#mlx.core.load)

By MLX Contributors

© Copyright 2023, Apple.\