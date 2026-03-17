# optuna.storages.RDBStorage

class optuna.storages.RDBStorage(*url*, *engine_kwargs=None*, *skip_compatibility_check=False*, ***, *heartbeat_interval=None*, *grace_period=None*, *failed_trial_callback=None*, *skip_table_creation=False*)

Storage class for RDB backend.

Note that library users can instantiate this class, but the attributes
provided by this class are not supposed to be directly accessed by them.

Example

Create an `RDBStorage` instance with customized
`pool_size` and `timeout` settings.

```
import optuna

def objective(trial):
    x = trial.suggest_float("x", -100, 100)
    return x**2

storage = optuna.storages.RDBStorage(
    url="sqlite:///:memory:",
    engine_kwargs={"pool_size": 20, "connect_args": {"timeout": 10}},
)

study = optuna.create_study(storage=storage)
study.optimize(objective, n_trials=10)

```