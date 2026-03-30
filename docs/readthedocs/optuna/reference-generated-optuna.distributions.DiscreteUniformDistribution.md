# optuna.distributions.DiscreteUniformDistribution

class optuna.distributions.DiscreteUniformDistribution(*low*, *high*, *q*)

A discretized uniform distribution in the linear domain.

This object is instantiated by `suggest_float()` with `step`
argument, and passed to `samplers` in general.

Note

If the range \([\mathsf{low}, \mathsf{high}]\) is not divisible by \(q\),
\(\mathsf{high}\) will be replaced with the maximum of \(k q + \mathsf{low}
< \mathsf{high}\), where \(k\) is an integer.