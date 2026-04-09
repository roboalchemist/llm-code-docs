# optuna.logging.get_verbosity

optuna.logging.get_verbosity()

Return the current level for the Optuna’s root logger.

Example

Get the default verbosity level.

```
import optuna

# The default verbosity level of Optuna is `optuna.logging.INFO`.
print(optuna.logging.get_verbosity())
# 20
print(optuna.logging.INFO)
# 20

# There are logs of the INFO level.
study = optuna.create_study()
study.optimize(objective, n_trials=5)
# [I 2021-10-31 05:35:17,232] A new study created ...
# [I 2021-10-31 05:35:17,238] Trial 0 finished with value: ...
# [I 2021-10-31 05:35:17,245] Trial 1 finished with value: ...
# ...

```