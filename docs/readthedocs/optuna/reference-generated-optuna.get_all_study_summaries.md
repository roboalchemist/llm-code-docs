# optuna.get_all_study_summaries

optuna.get_all_study_summaries(*storage*, *include_best_trial=True*)

Get all history of studies stored in a specified storage.

Example

```
import optuna

def objective(trial):
    x = trial.suggest_float("x", -10, 10)
    return (x - 2) ** 2

study = optuna.create_study(study_name="example-study", storage="sqlite:///example.db")
study.optimize(objective, n_trials=3)

study_summaries = optuna.study.get_all_study_summaries(storage="sqlite:///example.db")
assert len(study_summaries) == 1

study_summary = study_summaries[0]
assert study_summary.study_name == "example-study"

```