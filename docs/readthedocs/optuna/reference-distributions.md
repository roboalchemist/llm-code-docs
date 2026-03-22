# optuna.distributions

The `distributions` module defines various classes representing probability distributions, mainly used to suggest initial hyperparameter values for an optimization trial. Distribution classes inherit from a library-internal `BaseDistribution`, and is initialized with specific parameters, such as the `low` and `high` endpoints for a `IntDistribution`.

Optuna users should not use distribution classes directly, but instead use utility functions provided by `Trial` such as `suggest_int()`.

`FloatDistribution`

A distribution on floats.

`IntDistribution`

A distribution on integers.

`CategoricalDistribution`

A categorical distribution.

`distribution_to_json`

Serialize a distribution to JSON format.

`json_to_distribution`

Deserialize a distribution in JSON format.

`check_distribution_compatibility`

A function to check compatibility of two distributions.

The following classes are deprecated and will be removed in the future.

`UniformDistribution`

A uniform distribution in the linear domain.

`LogUniformDistribution`

A uniform distribution in the log domain.

`DiscreteUniformDistribution`

A discretized uniform distribution in the linear domain.

`IntUniformDistribution`

A uniform distribution on integers.

`IntLogUniformDistribution`

A uniform distribution on integers in the log domain.