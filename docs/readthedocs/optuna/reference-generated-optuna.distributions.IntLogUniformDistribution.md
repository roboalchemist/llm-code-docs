# optuna.distributions.IntLogUniformDistribution

class optuna.distributions.IntLogUniformDistribution(*low*, *high*, *step=1*)

A uniform distribution on integers in the log domain.

This object is instantiated by `suggest_int()`, and passed to
`samplers` in general.

Parameters:

- 

**low** (*int* [https://docs.python.org/3/library/functions.html#int])

- 

**high** (*int* [https://docs.python.org/3/library/functions.html#int])

- 

**step** (*int* [https://docs.python.org/3/library/functions.html#int])

low

Lower endpoint of the range of the distribution. `low` is included in the range
and must be larger than or equal to 1. `low` must be less than or equal to `high`.

high

Upper endpoint of the range of the distribution. `high` is included in the range.
`high` must be greater than or equal to `low`.

step

A discretization step. `step` must be a positive integer.

Warning

Deprecated in v3.0.0. This feature will be removed in the future. The removal of this
feature is currently scheduled for v6.0.0, but this schedule is subject to change.
See https://github.com/optuna/optuna/releases/tag/v3.0.0.

Use `IntDistribution` instead.