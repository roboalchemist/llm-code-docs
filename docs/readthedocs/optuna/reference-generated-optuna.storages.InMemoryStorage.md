# optuna.storages.InMemoryStorage

class optuna.storages.InMemoryStorage

Storage class that stores data in memory of the Python process.

Example

Create an `InMemoryStorage` instance.

```
import optuna

def objective(trial):
    x = trial.suggest_float("x", -100, 100)
    return x**2

storage = optuna.storages.InMemoryStorage()

study = optuna.create_study(storage=storage)
study.optimize(objective, n_trials=10)

```