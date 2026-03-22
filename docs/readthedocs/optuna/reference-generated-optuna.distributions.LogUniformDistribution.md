# optuna.distributions.LogUniformDistribution

class optuna.distributions.LogUniformDistribution(*low*, *high*)

A uniform distribution in the log domain.

This object is instantiated by `suggest_float()` with `log=True`,
and passed to `samplers` in general.

Parameters:

- 

**low** (*float* [https://docs.python.org/3/library/functions.html#float])

- 

**high** (*float* [https://docs.python.org/3/library/functions.html#float])

low

Lower endpoint of the range of the distribution. `low` is included in the range.
`low` must be larger than 0. `low` must be less than or equal to `high`.

high

Upper endpoint of the range of the distribution. `high` is included in the range.
`high` must be greater than or equal to `low`.

Warning

Deprecated in v3.0.0. This feature will be removed in the future. The removal of this
feature is currently scheduled for v6.0.0, but this schedule is subject to change.
See https://github.com/optuna/optuna/releases/tag/v3.0.0.

Use `FloatDistribution` instead.