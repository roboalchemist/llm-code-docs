# optuna.distributions.IntDistribution

class optuna.distributions.IntDistribution(*low*, *high*, *log=False*, *step=1*)

A distribution on integers.

This object is instantiated by `suggest_int()`, and passed to
`samplers` in general.

Note

When `step` is not `None` [https://docs.python.org/3/library/constants.html#None], if the range \([\mathsf{low}, \mathsf{high}]\)
is not divisible by \(\mathsf{step}\), \(\mathsf{high}\) will be replaced
with the maximum of \(k \times \mathsf{step} + \mathsf{low} < \mathsf{high}\),
where \(k\) is an integer.