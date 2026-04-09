# optuna.storages.fail_stale_trials

optuna.storages.fail_stale_trials(*study*)

Fail stale trials and run their failure callbacks.

The running trials whose heartbeat has not been updated for a long time will be failed,
that is, those states will be changed to `FAIL`.

See also

See `RDBStorage`.