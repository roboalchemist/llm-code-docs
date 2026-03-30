# optuna.trial

The `trial` module contains `Trial` related classes and functions.

A `Trial` instance represents a process of evaluating an objective function. This instance is passed to an objective function and provides interfaces to get parameter suggestion, manage the trial’s state, and set/get user-defined attributes of the trial, so that Optuna users can define a custom objective function through the interfaces. Basically, Optuna users only use it in their custom objective functions.

`Trial`

A trial is a process of evaluating an objective function.

`FixedTrial`

A trial class which suggests a fixed value for each parameter.

`FrozenTrial`

Status and results of a `Trial`.

`TrialState`

State of a `Trial`.

`create_trial`

Create a new `FrozenTrial`.