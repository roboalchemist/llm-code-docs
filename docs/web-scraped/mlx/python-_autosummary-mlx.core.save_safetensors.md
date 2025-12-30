# Source: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.save_safetensors.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../_sources/python/_autosummary/mlx.core.save_safetensors.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.core.save_safetensors

## Contents

- [[`save_safetensors()`]](#mlx.core.save_safetensors)

# mlx.core.save_safetensors[\#](#mlx-core-save-safetensors "Link to this heading")

[[save_safetensors]][(]*[[file]][[:]][ ][[file][ ][[\|]][ ][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[ ][[\|]][ ][[Path]](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.14)")]*, *[[arrays]][[:]][ ][[[dict]](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")[[\[]][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[,]][ ][[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")[[\]]]]*, *[[metadata]][[:]][ ][[[dict]](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")[[\[]][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[,]][ ][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[\]]][ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][ ][[=]][ ][[None]]*[)][\#](#mlx.core.save_safetensors "Link to this definition")

:   Save array(s) to a binary file in [`.safetensors`] format.

    See the [Safetensors documentation](https://huggingface.co/docs/safetensors/index) for more information on the format.

    Parameters[:]

    :   - **file** (*file,* [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*,* [*Path*](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.14)")) -- File in which the array is saved.

        - **arrays** ([*dict*](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")*(*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*,* [*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")*)*) -- The dictionary of names to arrays to be saved.

        - **metadata** ([*dict*](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")*(*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*,* [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*),* *optional*) -- The dictionary of metadata to be saved.

[](mlx.core.save_gguf.html "previous page")

previous

mlx.core.save_gguf

[](mlx.core.sigmoid.html "next page")

next

mlx.core.sigmoid

Contents

- [[`save_safetensors()`]](#mlx.core.save_safetensors)

By MLX Contributors

© Copyright 2023, Apple.\