# optuna.pruners.PatientPruner

class optuna.pruners.PatientPruner(*wrapped_pruner*, *patience*, *min_delta=0.0*)

Pruner which wraps another pruner with tolerance.

This pruner monitors intermediate values in a trial and prunes the trial if the improvement in
the intermediate values after a patience period is less than a threshold.

The pruner handles NaN values in the following manner:

1. If all intermediate values before or during the patient period are NaN, the trial will
not be pruned
2. During the pruning calculations, NaN values are ignored. Only valid numeric values are
considered.

Example

```
import numpy as np
from sklearn.datasets import load_iris
from sklearn.linear_model import SGDClassifier
from sklearn.model_selection import train_test_split

import optuna

X, y = load_iris(return_X_y=True)
X_train, X_valid, y_train, y_valid = train_test_split(X, y)
classes = np.unique(y)

def objective(trial):
    alpha = trial.suggest_float("alpha", 0.0, 1.0)
    clf = SGDClassifier(alpha=alpha)
    n_train_iter = 100

    for step in range(n_train_iter):
        clf.partial_fit(X_train, y_train, classes=classes)

        intermediate_value = clf.score(X_valid, y_valid)
        trial.report(intermediate_value, step)

        if trial.should_prune():
            raise optuna.TrialPruned()

    return clf.score(X_valid, y_valid)

study = optuna.create_study(
    direction="maximize",
    pruner=optuna.pruners.PatientPruner(optuna.pruners.MedianPruner(), patience=1),
)
study.optimize(objective, n_trials=20)

```