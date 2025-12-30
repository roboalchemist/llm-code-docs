# Source: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.einsum_path.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../_sources/python/_autosummary/mlx.core.einsum_path.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.core.einsum_path

## Contents

- [[`einsum_path()`]](#mlx.core.einsum_path)

# mlx.core.einsum_path[\#](#mlx-core-einsum-path "Link to this heading")

[[einsum_path]][(]*[[subscripts]][[:]][ ][[[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]*, *[[\*]][[operands]]*[)][\#](#mlx.core.einsum_path "Link to this definition")

:   Compute the contraction order for the given Einstein summation.

    Parameters[:]

    :   - **subscripts** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) -- The Einstein summation convention equation.

        - **\*operands** ([*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")) -- The input arrays.

    Returns[:]

    :   The einsum path and a string containing information about the chosen path.

    Return type[:]

    :   [*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")([*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")([*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"))), [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"))

[](mlx.core.einsum.html "previous page")

previous

mlx.core.einsum

[](mlx.core.equal.html "next page")

next

mlx.core.equal

Contents

- [[`einsum_path()`]](#mlx.core.einsum_path)

By MLX Contributors

© Copyright 2023, Apple.\