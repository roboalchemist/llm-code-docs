# optuna.importance

The `importance` module provides functionality for evaluating hyperparameter importances based on completed trials in a given study. The utility function `get_param_importances()` takes a `Study` and optional evaluator as two of its inputs. The evaluator must derive from `BaseImportanceEvaluator`, and is initialized as a `FanovaImportanceEvaluator` by default when not passed in. Users implementing custom evaluators should refer to either `FanovaImportanceEvaluator`, `MeanDecreaseImpurityImportanceEvaluator`, or `PedAnovaImportanceEvaluator` as a guide, paying close attention to the format of the return value from the Evaluator’s `evaluate` function.

Note

Although the default importance evaluator in Optuna is `FanovaImportanceEvaluator`, Optuna Dashboard uses a light-weight evaluator, i.e., `PedAnovaImportanceEvaluator`, for runtime performance purposes, yielding a different result.