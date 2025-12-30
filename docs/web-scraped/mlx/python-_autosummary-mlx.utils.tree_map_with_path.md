# Source: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.utils.tree_map_with_path.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../_sources/python/_autosummary/mlx.utils.tree_map_with_path.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.utils.tree_map_with_path

## Contents

- [[`tree_map_with_path()`]](#mlx.utils.tree_map_with_path)

# mlx.utils.tree_map_with_path[\#](#mlx-utils-tree-map-with-path "Link to this heading")

[[tree_map_with_path]][(]*[[fn]][[:]][ ][[[Callable]](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python v3.14)")]*, *[[tree]][[:]][ ][[[Any]](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")]*, *[[\*]][[rest]][[:]][ ][[[Any]](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")]*, *[[is_leaf]][[:]][ ][[[Callable]](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python v3.14)")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][ ][[=]][ ][[None]]*, *[[path]][[:]][ ][[[Any]](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][ ][[=]][ ][[None]]*[)] [[→] [[[Any]](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")]][\#](#mlx.utils.tree_map_with_path "Link to this definition")

:   Applies [`fn`] to the path and leaves of the Python tree [`tree`] and returns a new collection with the results.

    This function is the same [[`tree_map()`]](mlx.utils.tree_map.html#mlx.utils.tree_map "mlx.utils.tree_map") but the [`fn`] takes the path as the first argument followed by the remaining tree nodes.

    Parameters[:]

    :   - **fn** (*callable*) -- The function that processes the leaves of the tree.

        - **tree** (*Any*) -- The main Python tree that will be iterated upon.

        - **rest** ([*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")*\[Any\]*) -- Extra trees to be iterated together with [`tree`].

        - **is_leaf** (*Optional\[Callable\]*) -- An optional callable that returns [`True`] if the passed object is considered a leaf or [`False`] otherwise.

        - **path** (*Optional\[Any\]*) -- Prefix will be added to the result.

    Returns[:]

    :   A Python tree with the new values returned by [`fn`].

    Example

    :::: 
    ::: highlight
        >>> from mlx.utils import tree_map_with_path
        >>> tree = , ]}
        >>> new_tree = tree_map_with_path(lambda path, _: print(path), tree)
        model.0.w
        model.0.b
        model.1.w
        model.1.b
    :::
    ::::

[](mlx.utils.tree_map.html "previous page")

previous

mlx.utils.tree_map

[](mlx.utils.tree_reduce.html "next page")

next

mlx.utils.tree_reduce

Contents

- [[`tree_map_with_path()`]](#mlx.utils.tree_map_with_path)

By MLX Contributors

© Copyright 2023, Apple.\