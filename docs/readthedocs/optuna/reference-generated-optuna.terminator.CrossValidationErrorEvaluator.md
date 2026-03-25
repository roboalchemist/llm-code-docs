# optuna.terminator.CrossValidationErrorEvaluator

class optuna.terminator.CrossValidationErrorEvaluator(**args*, ***kwargs*)

An error evaluator for objective functions based on cross-validation.

This evaluator evaluates the objective function’s statistical error, which comes from the
randomness of dataset. This evaluator assumes that the objective function is the average of
the cross-validation and uses the scaled variance of the cross-validation scores in the best
trial at the moment as the statistical error.

Note

Added in v3.2.0 as an experimental feature. The interface may change in newer versions
without prior notice. See https://github.com/optuna/optuna/releases/tag/v3.2.0.