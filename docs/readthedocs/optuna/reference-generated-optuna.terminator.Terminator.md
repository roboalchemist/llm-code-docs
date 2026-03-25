# optuna.terminator.Terminator

class optuna.terminator.Terminator(*improvement_evaluator=None*, *error_evaluator=None*, *min_n_trials=20*)

Automatic stopping mechanism for Optuna studies.

This class implements an automatic stopping mechanism for Optuna studies, aiming to prevent
unnecessary computation. The study is terminated when the statistical error, e.g.
cross-validation error, exceeds the room left for optimization.

For further information about the algorithm, please refer to the following paper:

- 

A. Makarova et al. Automatic termination for hyperparameter optimization. [https://proceedings.mlr.press/v188/makarova22a.html]

Parameters:

- 

**improvement_evaluator** (*BaseImprovementEvaluator** | **None*) – An evaluator object for assessing the room left for optimization. Defaults to a
`RegretBoundEvaluator` object.

- 

**error_evaluator** (*BaseErrorEvaluator** | **None*) – An evaluator for calculating the statistical error, e.g. cross-validation error.
Defaults to a `CrossValidationErrorEvaluator`
object.

- 

**min_n_trials** (*int* [https://docs.python.org/3/library/functions.html#int]) – The minimum number of trials before termination is considered. Defaults to `20`.

Raises:

**ValueError** [https://docs.python.org/3/library/exceptions.html#ValueError] – If `min_n_trials` is not a positive integer.

Example

```
import logging
import sys

from sklearn.datasets import load_wine
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold

import optuna
from optuna.terminator import Terminator
from optuna.terminator import report_cross_validation_scores

study = optuna.create_study(direction="maximize")
terminator = Terminator()
min_n_trials = 20

while True:
    trial = study.ask()

    X, y = load_wine(return_X_y=True)

    clf = RandomForestClassifier(
        max_depth=trial.suggest_int("max_depth", 2, 32),
        min_samples_split=trial.suggest_float("min_samples_split", 0, 1),
        criterion=trial.suggest_categorical("criterion", ("gini", "entropy")),
    )

    scores = cross_val_score(clf, X, y, cv=KFold(n_splits=5, shuffle=True))
    report_cross_validation_scores(trial, scores)

    value = scores.mean()
    logging.info(f"Trial #{trial.number} finished with value {value}.")
    study.tell(trial, value)

    if trial.number > min_n_trials and terminator.should_terminate(study):
        logging.info("Terminated by Optuna Terminator!")
        break

```