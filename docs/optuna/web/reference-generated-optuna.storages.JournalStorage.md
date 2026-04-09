# optuna.storages.JournalStorage

class optuna.storages.JournalStorage(*log_storage*)

Storage class for Journal storage backend.

Note that library users can instantiate this class, but the attributes
provided by this class are not supposed to be directly accessed by them.

Journal storage writes a record of every operation to the database as it is executed and
at the same time, keeps a latest snapshot of the database in-memory. If the database crashes
for any reason, the storage can re-establish the contents in memory by replaying the
operations stored from the beginning.

Journal storage has several benefits over the conventional value logging storages.

- 

The number of IOs can be reduced because of larger granularity of logs.

- 

Journal storage has simpler backend API than value logging storage.

- 

Journal storage keeps a snapshot in-memory so no need to add more cache.

Example

```
import optuna

def objective(trial): ...

storage = optuna.storages.JournalStorage(
    optuna.storages.journal.JournalFileBackend("./optuna_journal_storage.log")
)

study = optuna.create_study(storage=storage)
study.optimize(objective)

```