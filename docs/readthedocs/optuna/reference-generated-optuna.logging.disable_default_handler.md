# optuna.logging.disable_default_handler

optuna.logging.disable_default_handler()

Disable the default handler of the Optuna’s root logger.

Example

Stop and then resume logging to `sys.stderr` [https://docs.python.org/3/library/sys.html#sys.stderr].

```
import optuna

study = optuna.create_study()

# There are no logs in sys.stderr.
optuna.logging.disable_default_handler()
study.optimize(objective, n_trials=10)

# There are logs in sys.stderr.
optuna.logging.enable_default_handler()
study.optimize(objective, n_trials=10)
# [I 2020-02-23 17:00:54,314] Trial 10 finished with value: ...
# [I 2020-02-23 17:00:54,356] Trial 11 finished with value: ...
# ...

```