# optuna.storages.journal.JournalFileSymlinkLock

class optuna.storages.journal.JournalFileSymlinkLock(*filepath*, *grace_period=30*)

Lock class for synchronizing processes for NFSv2 or later.

On acquiring the lock, link system call is called to create an exclusive file. The file is
deleted when the lock is released. In NFS environments prior to NFSv3, use this instead of
`JournalFileOpenLock`.

Parameters:

- 

**filepath** (*str* [https://docs.python.org/3/library/stdtypes.html#str]) – The path of the file whose race condition must be protected.

- 

**grace_period** (*int* [https://docs.python.org/3/library/functions.html#int]* | **None*) – Grace period before an existing lock is forcibly released.

Methods

`acquire`()

Acquire a lock in a blocking way by creating a symbolic link of a file.

`release`()

Release a lock by removing the symbolic link.

acquire()

Acquire a lock in a blocking way by creating a symbolic link of a file.

Returns:

`True` [https://docs.python.org/3/library/constants.html#True] if it succeeded in creating a symbolic link of `self._lock_target_file`.

Return type:

bool [https://docs.python.org/3/library/functions.html#bool]

release()

Release a lock by removing the symbolic link.

Return type:

None