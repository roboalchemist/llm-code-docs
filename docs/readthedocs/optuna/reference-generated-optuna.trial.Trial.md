# optuna.trial.Trial

class optuna.trial.Trial(*study*, *trial_id*)

A trial is a process of evaluating an objective function.

This object is passed to an objective function and provides interfaces to get parameter
suggestion, manage the trial’s state, and set/get user-defined attributes of the trial.

Note that the direct use of this constructor is not recommended.
This object is seamlessly instantiated and passed to the objective function behind
the `optuna.study.Study.optimize()` method; hence library users do not care about
instantiation of this object.

Parameters:

- 

**study** (*Study*) – A `Study` object.

- 

**trial_id** (*int* [https://docs.python.org/3/library/functions.html#int]) – A trial ID that is automatically generated.

Methods

`report`(value, step)

Report an objective function value for a given step.

`set_system_attr`(key, value)

Set system attributes to the trial.

`set_user_attr`(key, value)

Set user attributes to the trial.

`should_prune`()

Suggest whether the trial should be pruned or not.

`suggest_categorical`(...)

Suggest a value for the categorical parameter.

`suggest_discrete_uniform`(name, low, high, q)

Suggest a value for the discrete parameter.

`suggest_float`(name, low, high, *[, step, log])

Suggest a value for the floating point parameter.

`suggest_int`(name, low, high, *[, step, log])

Suggest a value for the integer parameter.

`suggest_loguniform`(name, low, high)

Suggest a value for the continuous parameter.

`suggest_uniform`(name, low, high)

Suggest a value for the continuous parameter.

Attributes

`datetime_start`

Return start datetime.

`distributions`

Return distributions of parameters to be optimized.

`number`

Return trial's number which is consecutive and unique in a study.

`params`

Return parameters to be optimized.

`relative_params`

`system_attrs`

Return system attributes.

`user_attrs`

Return user attributes.

property datetime_start: datetime.datetime [https://docs.python.org/3/library/datetime.html#datetime.datetime] | None [https://docs.python.org/3/library/constants.html#None]

Return start datetime.

Returns:

Datetime where the `Trial` started.

property distributions: dict [https://docs.python.org/3/library/stdtypes.html#dict][str [https://docs.python.org/3/library/stdtypes.html#str], BaseDistribution]

Return distributions of parameters to be optimized.

Returns:

A dictionary containing all distributions.

property number: int [https://docs.python.org/3/library/functions.html#int]

Return trial’s number which is consecutive and unique in a study.

Returns:

A trial number.

property params: dict [https://docs.python.org/3/library/stdtypes.html#dict][str [https://docs.python.org/3/library/stdtypes.html#str], Any [https://docs.python.org/3/library/typing.html#typing.Any]]

Return parameters to be optimized.

Returns:

A dictionary containing all parameters.

report(*value*, *step*)

Report an objective function value for a given step.

The reported values are used by the pruners to determine whether this trial should be
pruned.

See also

Please refer to `BasePruner`.