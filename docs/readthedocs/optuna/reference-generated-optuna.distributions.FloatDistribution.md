# optuna.distributions.FloatDistribution

class optuna.distributions.FloatDistribution(*low*, *high*, *log=False*, *step=None*)

A distribution on floats.

This object is instantiated by `suggest_float()`, and passed to
`samplers` in general.

Note

When `step` is not `None` [https://docs.python.org/3/library/constants.html#None], if the range \([\mathsf{low}, \mathsf{high}]\)
is not divisible by \(\mathsf{step}\), \(\mathsf{high}\) will be replaced
with the maximum of \(k \times \mathsf{step} + \mathsf{low} < \mathsf{high}\),
where \(k\) is an integer.