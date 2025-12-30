# Source: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.utils.tree_unflatten.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../_sources/python/_autosummary/mlx.utils.tree_unflatten.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.utils.tree_unflatten

## Contents

- [[`tree_unflatten()`]](#mlx.utils.tree_unflatten)

# mlx.utils.tree_unflatten[\#](#mlx-utils-tree-unflatten "Link to this heading")

[[tree_unflatten]][(]*[[tree]][[:]][ ][[[List]](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[\[]][[Tuple]](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[\[]][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[,]][ ][[Any]](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")[[\]]][[\]]][ ][[\|]][ ][[Dict]](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[\[]][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[,]][ ][[Any]](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")[[\]]]]*[)] [[→] [[[Any]](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")]][\#](#mlx.utils.tree_unflatten "Link to this definition")

:   Recreate a Python tree from its flat representation.

    :::: 
    ::: highlight
        from mlx.utils import tree_unflatten

        d = tree_unflatten([("hello.world", 42)])
        print(d)
        # }

        d = tree_unflatten()
        print(d)
        # }
    :::
    ::::

    Parameters[:]

    :   **tree** ([*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")*\[*[*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")*\[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*,* *Any\]\] or* [*dict*](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")*\[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*,* *Any\]*) -- The flat representation of a Python tree. For instance as returned by [[`tree_flatten()`]](mlx.utils.tree_flatten.html#mlx.utils.tree_flatten "mlx.utils.tree_flatten").

    Returns[:]

    :   A Python tree.

[](mlx.utils.tree_flatten.html "previous page")

previous

mlx.utils.tree_flatten

[](mlx.utils.tree_map.html "next page")

next

mlx.utils.tree_map

Contents

- [[`tree_unflatten()`]](#mlx.utils.tree_unflatten)

By MLX Contributors

© Copyright 2023, Apple.\