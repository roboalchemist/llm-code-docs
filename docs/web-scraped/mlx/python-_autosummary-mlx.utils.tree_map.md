# Source: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.utils.tree_map.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../_sources/python/_autosummary/mlx.utils.tree_map.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.utils.tree_map

## Contents

- [[`tree_map()`]](#mlx.utils.tree_map)

# mlx.utils.tree_map[\#](#mlx-utils-tree-map "Link to this heading")

[[tree_map]][(]*[[fn]][[:]][ ][[[Callable]](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python v3.14)")]*, *[[tree]][[:]][ ][[[Any]](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")]*, *[[\*]][[rest]][[:]][ ][[[Any]](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")]*, *[[is_leaf]][[:]][ ][[[Callable]](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python v3.14)")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][ ][[=]][ ][[None]]*[)] [[→] [[[Any]](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")]][\#](#mlx.utils.tree_map "Link to this definition")

:   Applies [`fn`] to the leaves of the Python tree [`tree`] and returns a new collection with the results.

    If [`rest`] is provided, every item is assumed to be a superset of [`tree`] and the corresponding leaves are provided as extra positional arguments to [`fn`]. In that respect, [[`tree_map()`]](#mlx.utils.tree_map "mlx.utils.tree_map") is closer to [[`itertools.starmap()`]](https://docs.python.org/3/library/itertools.html#itertools.starmap "(in Python v3.14)") than to [[`map()`]](https://docs.python.org/3/library/functions.html#map "(in Python v3.14)").

    The keyword argument [`is_leaf`] decides what constitutes a leaf from [`tree`] similar to [[`tree_flatten()`]](mlx.utils.tree_flatten.html#mlx.utils.tree_flatten "mlx.utils.tree_flatten").

    :::: 
    ::: highlight
        import mlx.nn as nn
        from mlx.utils import tree_map

        model = nn.Linear(10, 10)
        print(model.parameters().keys())
        # dict_keys(['weight', 'bias'])

        # square the parameters
        model.update(tree_map(lambda x: x*x, model.parameters()))
    :::
    ::::

    Parameters[:]

    :   - **fn** (*callable*) -- The function that processes the leaves of the tree.

        - **tree** (*Any*) -- The main Python tree that will be iterated upon.

        - **rest** ([*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")*\[Any\]*) -- Extra trees to be iterated together with [`tree`].

        - **is_leaf** (*callable,* *optional*) -- An optional callable that returns [`True`] if the passed object is considered a leaf or [`False`] otherwise.

    Returns[:]

    :   A Python tree with the new values returned by [`fn`].

[](mlx.utils.tree_unflatten.html "previous page")

previous

mlx.utils.tree_unflatten

[](mlx.utils.tree_map_with_path.html "next page")

next

mlx.utils.tree_map_with_path

Contents

- [[`tree_map()`]](#mlx.utils.tree_map)

By MLX Contributors

© Copyright 2023, Apple.\