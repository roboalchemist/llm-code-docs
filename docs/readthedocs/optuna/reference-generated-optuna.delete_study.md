# optuna.delete_study

optuna.delete_study(***, *study_name*, *storage*)

Delete a `Study` object.

Example

```
import optuna

def objective(trial):
    x = trial.suggest_float("x", -10, 10)
    return (x - 2) ** 2

study = optuna.create_study(study_name="example-study", storage="sqlite:///example.db")
study.optimize(objective, n_trials=3)

optuna.delete_study(study_name="example-study", storage="sqlite:///example.db")

```