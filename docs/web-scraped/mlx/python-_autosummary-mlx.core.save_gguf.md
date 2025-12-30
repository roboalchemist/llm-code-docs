# Source: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.save_gguf.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../_sources/python/_autosummary/mlx.core.save_gguf.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.core.save_gguf

## Contents

- [[`save_gguf()`]](#mlx.core.save_gguf)

# mlx.core.save_gguf[\#](#mlx-core-save-gguf "Link to this heading")

[[save_gguf]][(]*[[file]][[:]][ ][[file][ ][[\|]][ ][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[ ][[\|]][ ][[Path]](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.14)")]*, *[[arrays]][[:]][ ][[[dict]](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")[[\[]][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[,]][ ][[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")[[\]]]]*, *[[metadata]][[:]][ ][[[dict]](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")[[\[]][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[,]][ ][[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")[ ][[\|]][ ][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[ ][[\|]][ ][[list]](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[\[]][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[\]]][[\]]]]*[)][\#](#mlx.core.save_gguf "Link to this definition")

:   Save array(s) to a binary file in [`.gguf`] format.

    See the [GGUF documentation](https://github.com/ggerganov/ggml/blob/master/docs/gguf.md) for more information on the format.

    Parameters[:]

    :   - **file** (*file,* [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*,* [*Path*](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.14)")) -- File in which the array is saved.

        - **arrays** ([*dict*](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")*(*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*,* [*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")*)*) -- The dictionary of names to arrays to be saved.

        - **metadata** ([*dict*](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")*(*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*,* *Union\[*[*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")*,* [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*,* [*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")*(*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*)\])*) -- The dictionary of metadata to be saved. The values can be a scalar or 1D obj:array, a [[`str`]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), or a [[`list`]](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)") of [[`str`]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)").

[](mlx.core.savez_compressed.html "previous page")

previous

mlx.core.savez_compressed

[](mlx.core.save_safetensors.html "next page")

next

mlx.core.save_safetensors

Contents

- [[`save_gguf()`]](#mlx.core.save_gguf)

By MLX Contributors

© Copyright 2023, Apple.\