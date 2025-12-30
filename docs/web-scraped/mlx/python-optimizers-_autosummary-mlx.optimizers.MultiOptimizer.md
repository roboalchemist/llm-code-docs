# Source: https://ml-explore.github.io/mlx/build/html/python/optimizers/_autosummary/mlx.optimizers.MultiOptimizer.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../../_sources/python/optimizers/_autosummary/mlx.optimizers.MultiOptimizer.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.optimizers.MultiOptimizer

## Contents

- [[`MultiOptimizer`]](#mlx.optimizers.MultiOptimizer)

# mlx.optimizers.MultiOptimizer[\#](#mlx-optimizers-multioptimizer "Link to this heading")

*[class][ ]*[[MultiOptimizer]][(]*[[optimizers]]*, *[[filters]][[:]][ ][[[list]](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")][ ][[=]][ ][[\[\]]]*[)][\#](#mlx.optimizers.MultiOptimizer "Link to this definition")

:   Wraps a list of optimizers with corresponding weight predicates/filters to make it easy to use different optimizers for different weights.

    The predicates take the full "path" of the weight and the weight itself and return True if it should be considered for this optimizer. The last optimizer in the list is a fallback optimizer and no predicate should be given for it.

    Parameters[:]

    :   - **optimizers** ([*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")*\[*[*Optimizer*](../optimizer.html#mlx.optimizers.Optimizer "mlx.optimizers.Optimizer")*\]*) -- A list of optimizers to delegate to

        - **filters** ([*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")*\[Callable\[\[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*,* [*array*](../../_autosummary/mlx.core.array.html#mlx.core.array "mlx.core.array")*\],* [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*\]*) -- A list of predicates that should be one less than the provided optimizers.

    Methods

    ::: pst-scrollable-table-container
      ----------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------
      [`__init__`](optimizers\[, filters\])        
      [`apply_gradients`](gradients, parameters)   Apply the gradients to the parameters and return the updated parameters.
      [`init`](parameters)                         Initialize the optimizer\'s state
      ----------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------
    :::

[](mlx.optimizers.Lion.html "previous page")

previous

mlx.optimizers.Lion

[](mlx.optimizers.Muon.html "next page")

next

mlx.optimizers.Muon

Contents

- [[`MultiOptimizer`]](#mlx.optimizers.MultiOptimizer)

By MLX Contributors

© Copyright 2023, Apple.\