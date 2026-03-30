# optuna.importance.get_param_importances

optuna.importance.get_param_importances(*study*, ***, *evaluator=None*, *params=None*, *target=None*, *normalize=True*)

Evaluate parameter importances based on completed trials in the given study.

The parameter importances are returned as a dictionary where the keys consist of parameter
names and their values importances.
The importances are represented by non-negative floating point numbers, where higher values
mean that the parameters are more important.
The returned dictionary is ordered by its values in a descending order.
By default, the sum of the importance values are normalized to 1.0.

If `params` is `None` [https://docs.python.org/3/library/constants.html#None], all parameter that are present in all of the completed trials are
assessed.
This implies that conditional parameters will be excluded from the evaluation.
To assess the importances of conditional parameters, a `list` [https://docs.python.org/3/library/stdtypes.html#list] of parameter names can be
specified via `params`.
If specified, only completed trials that contain all of the parameters will be considered.
If no such trials are found, an error will be raised.

If the given study does not contain completed trials, an error will be raised.

Note

If `params` is specified as an empty list, an empty dictionary is returned.