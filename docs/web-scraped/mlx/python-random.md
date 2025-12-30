# Source: https://ml-explore.github.io/mlx/build/html/python/random.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../_sources/python/random.rst "Download source file")
- [ ] [.pdf]

[ ]

# Random

[]

# Random[\#](#random "Link to this heading")

Random sampling functions in MLX use an implicit global PRNG state by default. However, all function take an optional [`key`] keyword argument for when more fine-grained control or explicit state management is needed.

For example, you can generate random numbers with:

    for _ in range(3):
      print(mx.random.uniform())

which will print a sequence of unique pseudo random numbers. Alternatively you can explicitly set the key:

    key = mx.random.key(0)
    for _ in range(3):
      print(mx.random.uniform(key=key))

which will yield the same pseudo random number at each iteration.

Following [JAX's PRNG design](https://jax.readthedocs.io/en/latest/jep/263-prng.html) we use a splittable version of Threefry, which is a counter-based PRNG.

  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------
  [[`bernoulli`]](_autosummary/mlx.core.random.bernoulli.html#mlx.core.random.bernoulli "mlx.core.random.bernoulli")(\[p, shape, key, stream\])                                            Generate Bernoulli random values.
  [[`categorical`]](_autosummary/mlx.core.random.categorical.html#mlx.core.random.categorical "mlx.core.random.categorical")(logits\[, axis, shape, \...\])                                Sample from a categorical distribution.
  [[`gumbel`]](_autosummary/mlx.core.random.gumbel.html#mlx.core.random.gumbel "mlx.core.random.gumbel")(\[shape, dtype, key, stream\])                                                    Sample from the standard Gumbel distribution.
  [[`key`]](_autosummary/mlx.core.random.key.html#mlx.core.random.key "mlx.core.random.key")(seed)                                                                                         Get a PRNG key from a seed.
  [[`normal`]](_autosummary/mlx.core.random.normal.html#mlx.core.random.normal "mlx.core.random.normal")(\[shape, dtype, loc, scale, key, stream\])                                        Generate normally distributed random numbers.
  [[`multivariate_normal`]](_autosummary/mlx.core.random.multivariate_normal.html#mlx.core.random.multivariate_normal "mlx.core.random.multivariate_normal")(mean, cov\[, shape, \...\])   Generate jointly-normal random samples given a mean and covariance.
  [[`randint`]](_autosummary/mlx.core.random.randint.html#mlx.core.random.randint "mlx.core.random.randint")(low, high\[, shape, dtype, key, stream\])                                     Generate random integers from the given interval.
  [[`seed`]](_autosummary/mlx.core.random.seed.html#mlx.core.random.seed "mlx.core.random.seed")(seed)                                                                                     Seed the global PRNG.
  [[`split`]](_autosummary/mlx.core.random.split.html#mlx.core.random.split "mlx.core.random.split")(key\[, num, stream\])                                                                 Split a PRNG key into sub keys.
  [[`truncated_normal`]](_autosummary/mlx.core.random.truncated_normal.html#mlx.core.random.truncated_normal "mlx.core.random.truncated_normal")(lower, upper\[, shape, \...\])            Generate values from a truncated normal distribution.
  [[`uniform`]](_autosummary/mlx.core.random.uniform.html#mlx.core.random.uniform "mlx.core.random.uniform")(\[low, high, shape, dtype, key, stream\])                                     Generate uniformly distributed random numbers.
  [[`laplace`]](_autosummary/mlx.core.random.laplace.html#mlx.core.random.laplace "mlx.core.random.laplace")(\[shape, dtype, loc, scale, key, stream\])                                    Sample numbers from a Laplace distribution.
  [[`permutation`]](_autosummary/mlx.core.random.permutation.html#mlx.core.random.permutation "mlx.core.random.permutation")(x\[, axis, key, stream\])                                     Generate a random permutation or permute the entries of an array.
  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------

[](_autosummary/mlx.core.zeros_like.html "previous page")

previous

mlx.core.zeros_like

[](_autosummary/mlx.core.random.bernoulli.html "next page")

next

mlx.core.random.bernoulli

By MLX Contributors

© Copyright 2023, Apple.\