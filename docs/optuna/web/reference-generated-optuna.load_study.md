# optuna.load_study

optuna.load_study(***, *study_name*, *storage*, *sampler=None*, *pruner=None*)

Load the existing `Study` that has the specified name.

Example

```
import optuna

def objective(trial):
    x = trial.suggest_float("x", 0, 10)
    return x**2

study = optuna.create_study(storage="sqlite:///example.db", study_name="my_study")
study.optimize(objective, n_trials=3)

loaded_study = optuna.load_study(study_name="my_study", storage="sqlite:///example.db")
assert len(loaded_study.trials) == len(study.trials)

```