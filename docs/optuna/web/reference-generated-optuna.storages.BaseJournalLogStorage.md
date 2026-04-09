# optuna.storages.BaseJournalLogStorage

class optuna.storages.BaseJournalLogStorage(**args*, ***kwargs*)

Base class for Journal storages.

Storage classes implementing this base class must guarantee process safety. This means,
multiple processes might concurrently call `read_logs` and `append_logs`. If the
backend storage does not internally support mutual exclusion mechanisms, such as locks,
you might want to use `JournalFileSymlinkLock` or
`JournalFileOpenLock` for creating a critical section.

Warning

Deprecated in v4.0.0. This feature will be removed in the future. The removal of this
feature is currently scheduled for v6.0.0, but this schedule is subject to change.
See https://github.com/optuna/optuna/releases/tag/v4.0.0.

Use `BaseJournalBackend` instead.