# Source: https://ml-explore.github.io/mlx/build/html/python/tree_utils.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../_sources/python/tree_utils.rst "Download source file")
- [ ] [.pdf]

[ ]

# Tree Utils

[]

# Tree Utils[\#](#tree-utils "Link to this heading")

In MLX we consider a python tree to be an arbitrarily nested collection of dictionaries, lists and tuples without cycles. Functions in this module that return python trees will be using the default python [`dict`], [`list`] and [`tuple`] but they can usually process objects that inherit from any of these.

Note

Dictionaries should have keys that are valid python identifiers.

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [[`tree_flatten`]](_autosummary/mlx.utils.tree_flatten.html#mlx.utils.tree_flatten "mlx.utils.tree_flatten")(tree\[, prefix, is_leaf, \...\])                      Flattens a Python tree to a list of key, value tuples.
  [[`tree_unflatten`]](_autosummary/mlx.utils.tree_unflatten.html#mlx.utils.tree_unflatten "mlx.utils.tree_unflatten")(tree)                                         Recreate a Python tree from its flat representation.
  [[`tree_map`]](_autosummary/mlx.utils.tree_map.html#mlx.utils.tree_map "mlx.utils.tree_map")(fn, tree, \*rest\[, is_leaf\])                                        Applies [`fn`] to the leaves of the Python tree [`tree`] and returns a new collection with the results.
  [[`tree_map_with_path`]](_autosummary/mlx.utils.tree_map_with_path.html#mlx.utils.tree_map_with_path "mlx.utils.tree_map_with_path")(fn, tree, \*rest\[, \...\])   Applies [`fn`] to the path and leaves of the Python tree [`tree`] and returns a new collection with the results.
  [[`tree_reduce`]](_autosummary/mlx.utils.tree_reduce.html#mlx.utils.tree_reduce "mlx.utils.tree_reduce")(fn, tree\[, initializer, is_leaf\])                       Applies a reduction to the leaves of a Python tree.
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[](_autosummary/mlx.core.distributed.recv_like.html "previous page")

previous

mlx.core.distributed.recv_like

[](_autosummary/mlx.utils.tree_flatten.html "next page")

next

mlx.utils.tree_flatten

By MLX Contributors

© Copyright 2023, Apple.\