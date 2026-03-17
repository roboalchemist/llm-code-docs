# optuna.logging.disable_propagation

optuna.logging.disable_propagation()

Disable propagation of the library log outputs.

Note that log propagation is disabled by default. You only need to use this function
to stop log propagation when you use `enable_propagation()`.

Example

Stop propagating logs to the root logger on the second optimize call.

```
import optuna
import logging

optuna.logging.disable_default_handler()  # Disable the default handler.
logger = logging.getLogger()

logger.setLevel(logging.INFO)  # Setup the root logger.
logger.addHandler(logging.FileHandler("foo.log", mode="w"))

optuna.logging.enable_propagation()  # Propagate logs to the root logger.

study = optuna.create_study()

logger.info("Logs from first optimize call")  # The logs are saved in the logs file.
study.optimize(objective, n_trials=10)

optuna.logging.disable_propagation()  # Stop propogating logs to the root logger.

logger.info("Logs from second optimize call")
# The new logs for second optimize call are not saved.
study.optimize(objective, n_trials=10)

with open("foo.log") as f:
    assert f.readline().startswith("A new study created")
    assert f.readline() == "Logs from first optimize call\n"
    # Check for logs after second optimize call.
    assert f.read().split("Logs from second optimize call\n")[-1] == ""

```