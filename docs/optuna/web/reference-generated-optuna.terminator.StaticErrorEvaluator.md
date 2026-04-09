# optuna.terminator.StaticErrorEvaluator

class optuna.terminator.StaticErrorEvaluator(*constant*)

An error evaluator that always returns a constant value.

This evaluator can be used to terminate the optimization when the evaluated improvement
potential is below the fixed threshold.

Parameters:

**constant** (*float* [https://docs.python.org/3/library/functions.html#float]) – A user-specified constant value to always return as an error estimate.

Note

Added in v3.2.0 as an experimental feature. The interface may change in newer versions
without prior notice. See https://github.com/optuna/optuna/releases/tag/v3.2.0.