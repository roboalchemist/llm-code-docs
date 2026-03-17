# optuna.study.MaxTrialsCallback

class optuna.study.MaxTrialsCallback(*n_trials*, *states=(TrialState.COMPLETE,)*)

Set a maximum number of trials before ending the study.

While the `n_trials` argument of `optuna.study.Study.optimize()` sets the number of
trials that will be run, you may want to continue running until you have a certain number of
successfully completed trials or stop the study when you have a certain number of trials that
fail. This `MaxTrialsCallback` class allows you to set a maximum number of trials for a
particular `TrialState` before stopping the study.

Example

```
import optuna
from optuna.study import MaxTrialsCallback
from optuna.trial import TrialState

def objective(trial):
    x = trial.suggest_float("x", -1, 1)
    return x**2

study = optuna.create_study()
study.optimize(
    objective,
    callbacks=[MaxTrialsCallback(10, states=(TrialState.COMPLETE,))],
)

```