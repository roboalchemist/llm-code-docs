# optuna.pruners.HyperbandPruner

class optuna.pruners.HyperbandPruner(*min_resource=1*, *max_resource='auto'*, *reduction_factor=3*, *bootstrap_count=0*)

Pruner using Hyperband.

As SuccessiveHalving (SHA) requires the number of configurations
\(n\) as its hyperparameter.  For a given finite budget \(B\),
all the configurations have the resources of \(B \over n\) on average.
As you can see, there will be a trade-off of \(B\) and \(B \over n\).
Hyperband [http://www.jmlr.org/papers/volume18/16-558/16-558.pdf] attacks this trade-off
by trying different \(n\) values for a fixed budget.

Note

- 

In the Hyperband paper, the counterpart of `RandomSampler`
is used.

- 

Optuna uses `TPESampler` by default.

- 

The benchmark result [https://github.com/optuna/optuna/pull/828#issuecomment-575457360]
shows that `optuna.pruners.HyperbandPruner` supports both samplers.