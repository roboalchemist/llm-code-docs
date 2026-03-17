# optuna.get_all_study_names

optuna.get_all_study_names(*storage*)

Get all study names stored in a specified storage.

Example

```
import optuna

def objective(trial):
    x = trial.suggest_float("x", -10, 10)
    return (x - 2) ** 2

study = optuna.create_study(study_name="example-study", storage="sqlite:///example.db")
study.optimize(objective, n_trials=3)

study_names = optuna.study.get_all_study_names(storage="sqlite:///example.db")
assert len(study_names) == 1

assert study_names[0] == "example-study"

```