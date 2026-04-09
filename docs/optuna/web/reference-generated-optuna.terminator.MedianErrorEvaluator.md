# optuna.terminator.MedianErrorEvaluator

class optuna.terminator.MedianErrorEvaluator(*paired_improvement_evaluator*, *warm_up_trials=10*, *n_initial_trials=20*, *threshold_ratio=0.01*)

An error evaluator that returns the ratio to initial median.

This error evaluator is introduced as a heuristics in the following paper:

- 

A stopping criterion for Bayesian optimization by the gap of expected minimum simple
regrets [https://proceedings.mlr.press/v206/ishibashi23a.html]

Parameters:

- 

**paired_improvement_evaluator** (*BaseImprovementEvaluator*) – The `improvement_evaluator` instance which is set with this `error_evaluator`.

- 

**warm_up_trials** (*int* [https://docs.python.org/3/library/functions.html#int]) – A parameter specifies the number of initial trials to be discarded before
the calculation of median. Default to 10.
In optuna, the first 10 trials are often random sampling.
The `warm_up_trials` can exclude them from the calculation.

- 

**n_initial_trials** (*int* [https://docs.python.org/3/library/functions.html#int]) – A parameter specifies the number of initial trials considered in the calculation of
median after `warm_up_trials`. Default to 20.

- 

**threshold_ratio** (*float* [https://docs.python.org/3/library/functions.html#float]) – A parameter specifies the ratio between the threshold and initial median.
Default to 0.01.

Note

Added in v4.0.0 as an experimental feature. The interface may change in newer versions
without prior notice. See https://github.com/optuna/optuna/releases/tag/v4.0.0.