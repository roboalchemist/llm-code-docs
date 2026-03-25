# optuna.study.Study

class optuna.study.Study(*study_name*, *storage*, *sampler=None*, *pruner=None*)

A study corresponds to an optimization task, i.e., a set of trials.

This object provides interfaces to run a new `Trial`, access trials’
history, set/get user-defined attributes of the study itself.

Note that the direct use of this constructor is not recommended.
To create and load a study, please refer to the documentation of
`create_study()` and `load_study()` respectively.

Methods

`add_trial`(trial)

Add trial to study.

`add_trials`(trials)

Add trials to study.

`ask`([fixed_distributions])

Create a new trial from which hyperparameters can be suggested.

`enqueue_trial`(params[, user_attrs, ...])

Enqueue a trial with given parameter values.

`get_trials`([deepcopy, states])

Return all trials in the study.

`optimize`(func[, n_trials, timeout, n_jobs, ...])

Optimize an objective function.

`set_metric_names`(metric_names)

Set metric names.

`set_system_attr`(key, value)

Set a system attribute to the study.

`set_user_attr`(key, value)

Set a user attribute to the study.

`stop`()

Exit from the current optimization loop after the running trials finish.

`tell`(trial[, values, state, skip_if_finished])

Finish a trial created with `ask()`.

`trials_dataframe`([attrs, multi_index])

Export trials as a pandas DataFrame [http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.html].

Attributes

`best_params`

Return parameters of the best trial in the study.

`best_trial`

Return the best trial in the study.

`best_trials`

Return trials located at the Pareto front in the study.

`best_value`

Return the best objective value in the study.

`direction`

Return the direction of the study.

`directions`

Return the directions of the study.

`metric_names`

Return metric names.

`system_attrs`

Return system attributes.

`trials`

Return all trials in the study.

`user_attrs`

Return user attributes.

Parameters:

- 

**study_name** (*str* [https://docs.python.org/3/library/stdtypes.html#str])

- 

**storage** (*str* [https://docs.python.org/3/library/stdtypes.html#str]* | **storages.BaseStorage*)

- 

**sampler** (*'samplers.BaseSampler'** | **None*)

- 

**pruner** (*pruners.BasePruner** | **None*)

add_trial(*trial*)

Add trial to study.

The trial is validated before being added.

Example

```
import optuna
from optuna.distributions import FloatDistribution

def objective(trial):
    x = trial.suggest_float("x", 0, 10)
    return x**2

study = optuna.create_study()
assert len(study.trials) == 0

trial = optuna.trial.create_trial(
    params={"x": 2.0},
    distributions={"x": FloatDistribution(0, 10)},
    value=4.0,
)

study.add_trial(trial)
assert len(study.trials) == 1

study.optimize(objective, n_trials=3)
assert len(study.trials) == 4

other_study = optuna.create_study()

for trial in study.trials:
    other_study.add_trial(trial)
assert len(other_study.trials) == len(study.trials)

other_study.optimize(objective, n_trials=2)
assert len(other_study.trials) == len(study.trials) + 2

```