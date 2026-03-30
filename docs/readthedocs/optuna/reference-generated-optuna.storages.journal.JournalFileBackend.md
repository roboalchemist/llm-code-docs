# optuna.storages.journal.JournalFileBackend

class optuna.storages.journal.JournalFileBackend(*file_path*, *lock_obj=None*)

File storage class for Journal log backend.

Compared to SQLite3, the benefit of this backend is that it is more suitable for
environments where the file system does not support `fcntl()` file locking.
For example, as written in the SQLite3 FAQ [https://www.sqlite.org/faq.html#q5],
SQLite3 might not work on NFS (Network File System) since `fcntl()` file locking
is broken on many NFS implementations. In such scenarios, this backend provides
several workarounds for locking files. For more details, refer to the Medium blog post [https://medium.com/optuna/distributed-optimization-via-nfs-using-optunas-new-operation-based-logging-storage-9815f9c3f932].

It’s important to note that, similar to SQLite3, this class doesn’t support a high
level of write concurrency, as outlined in the SQLAlchemy documentation [https://docs.sqlalchemy.org/en/20/dialects/sqlite.html#database-locking-behavior-concurrency]. However,
in typical situations where the objective function is computationally expensive, Optuna
users don’t need to be concerned about this limitation. The reason being, the write
operations are not the bottleneck as long as the objective function doesn’t invoke
`report()` and `set_user_attr()` excessively.

Parameters:

- 

**file_path** (*str* [https://docs.python.org/3/library/stdtypes.html#str]) – Path of file to persist the log to.

- 

**lock_obj** (*BaseJournalFileLock** | **None*) – Lock object for process exclusivity. An instance of
`JournalFileSymlinkLock` and
`JournalFileOpenLock` can be passed.

Methods

`append_logs`(logs)

Append logs to the backend.

`read_logs`(log_number_from)

Read logs with a log number greater than or equal to `log_number_from`.

append_logs(*logs*)

Append logs to the backend.

Parameters:

**logs** (*list* [https://docs.python.org/3/library/stdtypes.html#list]*[**dict* [https://docs.python.org/3/library/stdtypes.html#dict]*[**str* [https://docs.python.org/3/library/stdtypes.html#str]*, **Any* [https://docs.python.org/3/library/typing.html#typing.Any]*]**]*) – A list that contains json-serializable logs.

Return type:

None

read_logs(*log_number_from*)

Read logs with a log number greater than or equal to `log_number_from`.

If `log_number_from` is 0, read all the logs.

Parameters:

**log_number_from** (*int* [https://docs.python.org/3/library/functions.html#int]) – A non-negative integer value indicating which logs to read.

Returns:

Logs with log number greater than or equal to `log_number_from`.

Return type:

*Generator* [https://docs.python.org/3/library/collections.abc.html#collections.abc.Generator][dict [https://docs.python.org/3/library/stdtypes.html#dict][str [https://docs.python.org/3/library/stdtypes.html#str], *Any* [https://docs.python.org/3/library/typing.html#typing.Any]], None, None]