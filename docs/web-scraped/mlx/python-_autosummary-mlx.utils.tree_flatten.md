# Source: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.utils.tree_flatten.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../_sources/python/_autosummary/mlx.utils.tree_flatten.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.utils.tree_flatten

## Contents

- [[`tree_flatten()`]](#mlx.utils.tree_flatten)

# mlx.utils.tree_flatten[\#](#mlx-utils-tree-flatten "Link to this heading")

[[tree_flatten]][(]*[[tree]][[:]][ ][[[Any]](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")]*, *[[prefix]][[:]][ ][[[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")][ ][[=]][ ][[\'\']]*, *[[is_leaf]][[:]][ ][[[Callable]](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python v3.14)")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][ ][[=]][ ][[None]]*, *[[destination]][[:]][ ][[[List]](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[\[]][[Tuple]](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[\[]][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[,]][ ][[Any]](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")[[\]]][[\]]][ ][[\|]][ ][[Dict]](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[\[]][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[,]][ ][[Any]](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")[[\]]][ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][ ][[=]][ ][[None]]*[)] [[→] [[[List]](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[\[]][[Tuple]](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[\[]][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[,]][ ][[Any]](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")[[\]]][[\]]][ ][[\|]][ ][[Dict]](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[\[]][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[,]][ ][[Any]](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")[[\]]]]][\#](#mlx.utils.tree_flatten "Link to this definition")

:   Flattens a Python tree to a list of key, value tuples.

    The keys are using the dot notation to define trees of arbitrary depth and complexity.

    :::: 
    ::: highlight
        from mlx.utils import tree_flatten

        print(tree_flatten([[[0]]]))
        # [("0.0.0", 0)]

        print(tree_flatten([[[0]]], prefix=".hello"))
        # [("hello.0.0.0", 0)]

        tree_flatten(}, destination=)
        
    :::
    ::::

    ::: 
    Note

    Dictionaries should have keys that are valid Python identifiers.
    :::

    Parameters[:]

    :   - **tree** (*Any*) -- The Python tree to be flattened.

        - **prefix** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) -- A prefix to use for the keys. The first character is always discarded.

        - **is_leaf** (*callable*) -- An optional callable that returns True if the passed object is considered a leaf or False otherwise.

        - **destination** ([*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)") *or* [*dict*](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")*,* *optional*) -- A list or dictionary to store the flattened tree. If None an empty list will be used. Default: [`None`].

    Returns[:]

    :   

        The flat representation of

        :   the Python tree.

    Return type[:]

    :   *Union*\[*List*\[*Tuple*\[[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), *Any*\]\], *Dict*\[[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), *Any*\]\]

[](../tree_utils.html "previous page")

previous

Tree Utils

[](mlx.utils.tree_unflatten.html "next page")

next

mlx.utils.tree_unflatten

Contents

- [[`tree_flatten()`]](#mlx.utils.tree_flatten)

By MLX Contributors

© Copyright 2023, Apple.\