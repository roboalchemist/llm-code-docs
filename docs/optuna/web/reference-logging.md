# optuna.logging

The `logging` module implements logging using the Python `logging` package. Library users may be especially interested in setting verbosity levels using `set_verbosity()` to one of `optuna.logging.CRITICAL` (aka `optuna.logging.FATAL`), `optuna.logging.ERROR`, `optuna.logging.WARNING` (aka `optuna.logging.WARN`), `optuna.logging.INFO`, or `optuna.logging.DEBUG`.

`get_verbosity`

Return the current level for the Optuna's root logger.

`set_verbosity`

Set the level for the Optuna's root logger.

`disable_default_handler`

Disable the default handler of the Optuna's root logger.

`enable_default_handler`

Enable the default handler of the Optuna's root logger.

`disable_propagation`

Disable propagation of the library log outputs.

`enable_propagation`

Enable propagation of the library log outputs.