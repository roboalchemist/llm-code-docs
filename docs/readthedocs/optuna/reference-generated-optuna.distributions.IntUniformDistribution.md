# optuna.distributions.IntUniformDistribution

class optuna.distributions.IntUniformDistribution(*low*, *high*, *step=1*)

A uniform distribution on integers.

This object is instantiated by `suggest_int()`, and passed to
`samplers` in general.

Note

If the range \([\mathsf{low}, \mathsf{high}]\) is not divisible by
\(\mathsf{step}\), \(\mathsf{high}\) will be replaced with the maximum of
\(k \times \mathsf{step} + \mathsf{low} < \mathsf{high}\), where \(k\) is
an integer.