# optuna.storages.journal.JournalRedisBackend

class optuna.storages.journal.JournalRedisBackend(*url*, *use_cluster=False*, *prefix=''*)

Redis storage class for Journal log backend.

Parameters:

- 

**url** (*str* [https://docs.python.org/3/library/stdtypes.html#str]) – URL of the redis storage, password and db are optional.
(ie: `redis://localhost:6379`)

- 

**use_cluster** (*bool* [https://docs.python.org/3/library/functions.html#bool]) – Flag whether you use the Redis cluster. If this is `False` [https://docs.python.org/3/library/constants.html#False], it is assumed that
you use the standalone Redis server and ensured that a write operation is atomic. This
provides the consistency of the preserved logs. If this is `True` [https://docs.python.org/3/library/constants.html#True], it is assumed
that you use the Redis cluster and not ensured that a write operation is atomic. This
means the preserved logs can be inconsistent due to network errors, and may
cause errors.

- 

**prefix** (*str* [https://docs.python.org/3/library/stdtypes.html#str]) – Prefix of the preserved key of logs. This is useful when multiple users work on one
Redis server.

Note

Added in v3.1.0 as an experimental feature. The interface may change in newer versions
without prior notice. See https://github.com/optuna/optuna/releases/tag/v3.1.0.