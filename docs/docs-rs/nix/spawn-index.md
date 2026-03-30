nix

# Module spawn

Source Available on **crate feature `process`** only.

## Structs§

PosixSpawnAttrA spawn attributes object. See posix_spawnattr_t.PosixSpawnFileActionsA spawn file actions object. See posix_spawn_file_actions_t.PosixSpawnFlagsProcess attributes to be changed in the new process image when invoking `posix_spawn`
or `posix_spawnp`. See
posix_spawn.

## Functions§

posix_spawnCreate a new child process from the specified process image. See
posix_spawn.posix_spawnpCreate a new child process from the specified process image. See
posix_spawnp.
