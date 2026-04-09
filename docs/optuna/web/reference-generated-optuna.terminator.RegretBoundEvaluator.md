# optuna.terminator.RegretBoundEvaluator

class optuna.terminator.RegretBoundEvaluator(*top_trials_ratio=0.5*, *min_n_trials=20*, *seed=None*)

An error evaluator for upper bound on the regret with high-probability confidence.

This evaluator evaluates the regret of current best solution, which defined as the difference
between the objective value of the best solution and of the global optimum. To be specific,
this evaluator calculates the upper bound on the regret based on the fact that empirical
estimator of the objective function is bounded by lower and upper confidence bounds with
high probability under the Gaussian process model assumption.

Parameters:

- 

**top_trials_ratio** (*float* [https://docs.python.org/3/library/functions.html#float]) – A ratio of top trials to be considered when estimating the regret. Default to 0.5.

- 

**min_n_trials** (*int* [https://docs.python.org/3/library/functions.html#int]) – A minimum number of complete trials to estimate the regret. Default to 20.

- 

**seed** (*int* [https://docs.python.org/3/library/functions.html#int]* | **None*) – Seed for random number generator.

For further information about this evaluator, please refer to the following paper:

- 

Automatic Termination for Hyperparameter Optimization [https://proceedings.mlr.press/v188/makarova22a.html]

Note

Added in v3.2.0 as an experimental feature. The interface may change in newer versions
without prior notice. See https://github.com/optuna/optuna/releases/tag/v3.2.0.