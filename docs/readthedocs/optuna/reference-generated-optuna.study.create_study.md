# optuna.study.create_study

optuna.study.create_study(***, *storage=None*, *sampler=None*, *pruner=None*, *study_name=None*, *direction=None*, *load_if_exists=False*, *directions=None*)

Create a new `Study`.

Example

```
import optuna

def objective(trial):
    x = trial.suggest_float("x", 0, 10)
    return x**2

study = optuna.create_study()
study.optimize(objective, n_trials=3)

```