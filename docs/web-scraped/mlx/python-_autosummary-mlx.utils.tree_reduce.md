# Source: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.utils.tree_reduce.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../_sources/python/_autosummary/mlx.utils.tree_reduce.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.utils.tree_reduce

## Contents

- [[`tree_reduce()`]](#mlx.utils.tree_reduce)

# mlx.utils.tree_reduce[\#](#mlx-utils-tree-reduce "Link to this heading")

[[tree_reduce]][(]*[[fn]]*, *[[tree]]*, *[[initializer]][[=]][[None]]*, *[[is_leaf]][[=]][[None]]*[)][\#](#mlx.utils.tree_reduce "Link to this definition")

:   Applies a reduction to the leaves of a Python tree.

    This function reduces Python trees into an accumulated result by applying the provided function [`fn`] to the leaves of the tree.

    Example

    :::: 
    ::: highlight
        >>> from mlx.utils import tree_reduce
        >>> tree = 
        >>> tree_reduce(lambda acc, x: acc + x, tree, 0)
        15
    :::
    ::::

    Parameters[:]

    :   - **fn** (*callable*) -- The reducer function that takes two arguments (accumulator, current value) and returns the updated accumulator.

        - **tree** (*Any*) -- The Python tree to reduce. It can be any nested combination of lists, tuples, or dictionaries.

        - **initializer** (*Any,* *optional*) -- The initial value to start the reduction. If not provided, the first leaf value is used.

        - **is_leaf** (*callable,* *optional*) -- A function to determine if an object is a leaf, returning [`True`] for leaf nodes and [`False`] otherwise.

    Returns[:]

    :   The accumulated value.

    Return type[:]

    :   *Any*

[](mlx.utils.tree_map_with_path.html "previous page")

previous

mlx.utils.tree_map_with_path

[](../../cpp/ops.html "next page")

next

Operations

Contents

- [[`tree_reduce()`]](#mlx.utils.tree_reduce)

By MLX Contributors

© Copyright 2023, Apple.\