# optuna.terminator.report_cross_validation_scores

optuna.terminator.report_cross_validation_scores(*trial*, *scores*)

A function to report cross-validation scores of a trial.

This function should be called within the objective function to report the cross-validation
scores. The reported scores are used to evaluate the statistical error for termination
judgement.

Parameters:

- 

**trial** (*Trial*) – A `Trial` object to report the cross-validation scores.

- 

**scores** (*list* [https://docs.python.org/3/library/stdtypes.html#list]*[**float* [https://docs.python.org/3/library/functions.html#float]*]*) – The cross-validation scores of the trial.

Return type:

None

Note

Added in v3.2.0 as an experimental feature. The interface may change in newer versions
without prior notice. See https://github.com/optuna/optuna/releases/tag/v3.2.0.