# optuna.trial.FrozenTrial

class optuna.trial.FrozenTrial(*number*, *state*, *value*, *datetime_start*, *datetime_complete*, *params*, *distributions*, *user_attrs*, *system_attrs*, *intermediate_values*, *trial_id*, ***, *values=None*)

Status and results of a `Trial`.

An object of this class has the same methods as `Trial`, but is not
associated with, nor has any references to a `Study`.

It is therefore not possible to make persistent changes to a storage from this object by
itself, for instance by using `set_user_attr()`.

It will suggest the parameter values stored in `params` and will not sample values from
any distributions.

It can be passed to objective functions (see `optimize()`) and is
useful for deploying optimization results.

Example

Re-evaluate an objective function with parameter values optimized study.

```
import optuna

def objective(trial):
    x = trial.suggest_float("x", -1, 1)
    return x**2

study = optuna.create_study()
study.optimize(objective, n_trials=3)

assert objective(study.best_trial) == study.best_value

```