# optuna.logging.set_verbosity

optuna.logging.set_verbosity(*verbosity*)

Set the level for the Optuna’s root logger.

Example

Set the logging level `optuna.logging.WARNING`.

```
import optuna

# There are INFO level logs.
study = optuna.create_study()
study.optimize(objective, n_trials=10)
# [I 2021-10-31 02:59:35,088] Trial 0 finished with value: 16.0 ...
# [I 2021-10-31 02:59:35,091] Trial 1 finished with value: 1.0 ...
# [I 2021-10-31 02:59:35,096] Trial 2 finished with value: 1.0 ...

# Setting the logging level WARNING, the INFO logs are suppressed.
optuna.logging.set_verbosity(optuna.logging.WARNING)
study.optimize(objective, n_trials=10)

```