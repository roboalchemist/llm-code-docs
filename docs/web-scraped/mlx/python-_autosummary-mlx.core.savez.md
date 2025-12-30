# Source: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.savez.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../_sources/python/_autosummary/mlx.core.savez.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.core.savez

## Contents

- [[`savez()`]](#mlx.core.savez)

# mlx.core.savez[\#](#mlx-core-savez "Link to this heading")

[[savez]][(]*[[file]][[:]][ ][[file][ ][[\|]][ ][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[ ][[\|]][ ][[Path]](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.14)")]*, *[[\*]][[args]]*, *[[\*\*]][[kwargs]]*[)][\#](#mlx.core.savez "Link to this definition")

:   Save several arrays to a binary file in uncompressed [`.npz`] format.

    :::: 
    ::: highlight
        import mlx.core as mx

        x = mx.ones((10, 10))
        mx.savez("my_path.npz", x=x)

        import mlx.nn as nn
        from mlx.utils import tree_flatten

        model = nn.TransformerEncoder(6, 128, 4)
        flat_params = tree_flatten(model.parameters())
        mx.savez("model.npz", **dict(flat_params))
    :::
    ::::

    Parameters[:]

    :   - **file** (*file,* [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*,* [*Path*](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.14)")) -- Path to file to which the arrays are saved.

        - **\*args** (*arrays*) -- Arrays to be saved.

        - **\*\*kwargs** (*arrays*) -- Arrays to be saved. Each array will be saved with the associated keyword as the output file name.

[](mlx.core.save.html "previous page")

previous

mlx.core.save

[](mlx.core.savez_compressed.html "next page")

next

mlx.core.savez_compressed

Contents

- [[`savez()`]](#mlx.core.savez)

By MLX Contributors

© Copyright 2023, Apple.\