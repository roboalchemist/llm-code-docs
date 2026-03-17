# optuna.terminator.TerminatorCallback

class optuna.terminator.TerminatorCallback(*terminator=None*)

A callback that terminates the optimization using Terminator.

This class implements a callback which wraps `Terminator`
so that it can be used with the `optimize()` method.

Parameters:

**terminator** (*BaseTerminator** | **None*) – A terminator object which determines whether to terminate the optimization by
assessing the room for optimization and statistical error. Defaults to a
`Terminator` object with default
`improvement_evaluator` and `error_evaluator`.

Example

```
from sklearn.datasets import load_wine
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold

import optuna
from optuna.terminator import TerminatorCallback
from optuna.terminator import report_cross_validation_scores

def objective(trial):
    X, y = load_wine(return_X_y=True)

    clf = RandomForestClassifier(
        max_depth=trial.suggest_int("max_depth", 2, 32),
        min_samples_split=trial.suggest_float("min_samples_split", 0, 1),
        criterion=trial.suggest_categorical("criterion", ("gini", "entropy")),
    )

    scores = cross_val_score(clf, X, y, cv=KFold(n_splits=5, shuffle=True))
    report_cross_validation_scores(trial, scores)
    return scores.mean()

study = optuna.create_study(direction="maximize")
terminator = TerminatorCallback()
study.optimize(objective, n_trials=50, callbacks=[terminator])

```