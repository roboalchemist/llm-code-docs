# optuna.storages

The `storages` module defines a `BaseStorage` class which abstracts a backend database and provides library-internal interfaces to the read/write histories of the studies and trials. Library users who wish to use storage solutions other than the default `InMemoryStorage` should use one of the child classes of `BaseStorage` documented below.

`RDBStorage`

Storage class for RDB backend.

`RetryFailedTrialCallback`

Retry a failed trial up to a maximum number of times.

`fail_stale_trials`

Fail stale trials and run their failure callbacks.

`JournalStorage`

Storage class for Journal storage backend.

`InMemoryStorage`

Storage class that stores data in memory of the Python process.

`run_grpc_proxy_server`

Run a gRPC server for the given storage URL, host, and port.

`GrpcStorageProxy`

gRPC client for `run_grpc_proxy_server()`.

## optuna.storages.journal

`JournalStorage` requires its backend specification and here is the list of the supported backends:

Note

If users would like to use any backends not supported by Optuna, it is possible to do so by creating a customized class by inheriting `optuna.storages.journal.BaseJournalBackend`.