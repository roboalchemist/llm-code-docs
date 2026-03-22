# optuna.trial.FixedTrial

class optuna.trial.FixedTrial(*params*, *number=0*)

A trial class which suggests a fixed value for each parameter.

This object has the same methods as `Trial`, and it suggests pre-defined
parameter values. The parameter values can be determined at the construction of the
`FixedTrial` object. In contrast to `Trial`,
`FixedTrial` does not depend on `Study`, and it is
useful for deploying optimization results.

Example

Evaluate an objective function with parameter values given by a user.

```
import optuna

def objective(trial):
    x = trial.suggest_float("x", -100, 100)
    y = trial.suggest_categorical("y", [-1, 0, 1])
    return x**2 + y

assert objective(optuna.trial.FixedTrial({"x": 1, "y": 0})) == 1

```