# optuna.storages.journal.JournalFileOpenLock

class optuna.storages.journal.JournalFileOpenLock(*filepath*, *grace_period=30*)

Lock class for synchronizing processes for NFSv3 or later.

On acquiring the lock, open system call is called with the O_EXCL option to create an exclusive
file. The file is deleted when the lock is released. This class is only supported when using
NFSv3 or later on kernel 2.6 or later. In prior NFS environments, use
`JournalFileSymlinkLock`.

Parameters:

- 

**filepath** (*str* [https://docs.python.org/3/library/stdtypes.html#str]) – The path of the file whose race condition must be protected.

- 

**grace_period** (*int* [https://docs.python.org/3/library/functions.html#int]* | **None*) – Grace period before an existing lock is forcibly released.

Methods

`acquire`()

Acquire a lock in a blocking way by creating a lock file.

`release`()

Release a lock by removing the created file.

acquire()

Acquire a lock in a blocking way by creating a lock file.

Returns:

`True` [https://docs.python.org/3/library/constants.html#True] if it succeeded in creating a `self._lock_file`.

Return type:

bool [https://docs.python.org/3/library/functions.html#bool]

release()

Release a lock by removing the created file.

Return type:

None