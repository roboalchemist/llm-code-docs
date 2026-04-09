nix

# Module fcntl

Source Available on **Unix** only.

## Re-exports§

`pub use self::FcntlArg::*;``fs`

## Structs§

AtFlags`fs` or `process`Flags that control how the various *at syscalls behave.FallocateFlags`fs`Mode argument flags for fallocate determining operation performed on a given range.FdFlag`fs`Additional configuration flags for `fcntl`’s `F_SETFD`.Flock`fs`Represents an owned flock, which unlocks on drop.OFlag`fs`, or `term`, or `fanotify` and LinuxConfiguration options for opened files.OpenHowSpecifies how `openat2()` should open a pathname.RenameFlags`fs`Flags for use with `renameat2`.ResolveFlagPath resolution flags.SealFlag`fs`Additional flags for file sealing, which allows for limiting operations on a file.SpliceFFlags`zerocopy`Additional flags to `splice` and friends.

## Enums§

FcntlArg`fs`Commands for use with `fcntl`.FlockArg`fs`Operations for use with `Flock::lock`.PosixFadviseAdvice(`linux_android` or Emscripten or Fuchsia or WASI or uClibc or FreeBSD) and `fs`The specific advice provided to `posix_fadvise`.

## Constants§

AT_FDCWDNon-RedoxA file descriptor referring to the working directory of the current process
**that should be ONLY passed to the `dirfd` argument of those `xxat()` functions**.

## Traits§

Flockable`fs`Represents valid types for flock.

## Functions§

copy_file_range`zerocopy`Copy a range of data from one file to anotherfallocate`fs`Manipulates file space.fcntl`fs`Perform various operations on open file descriptors.flockDeprecated`fs`open`fs`open or create a file for reading, writing or executingopenat`fs`open or create a file for reading, writing or executingopenat2Open or create a file for reading, writing or executing.posix_fadvise(`linux_android` or Emscripten or Fuchsia or WASI or uClibc or FreeBSD) and `fs`Allows a process to describe to the system its data access behavior for an open file
descriptor.posix_fallocate`fs`Pre-allocate storage for a range in a filereadlink`fs`Read value of a symbolic linkreadlinkat`fs`Read value of a symbolic link.renameat`fs`Change the name of a file.renameat2`fs`Like `renameat`, but with an additional `flags` argument.splice`zerocopy`Splice data to/from a pipetee`zerocopy`Duplicate pipe contentvmsplice`zerocopy`Splice user pages to/from a pipe
