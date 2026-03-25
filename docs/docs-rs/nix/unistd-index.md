nix

# Module unistd

Source Available on **Unix** only.

## Modules§

acct`acct`Process accountingalarm`signal`Alarm signal scheduling.

## Structs§

AccessFlags`fs`Options for access()Gid`user`Group identifierGroup`user`Representation of a Group, based on `libc::group`Pid`process`Process identifierResGid`user`Real, effective and saved group IDs.ResUid`user`Real, effective and saved user IDs.Uid`user`User identifierUser`user`Representation of a User, based on `libc::passwd`

## Enums§

ForkResult`process`Represents the successful result of calling `fork`PathconfVar`fs` and `feature`Variable names for `pathconf`SysconfVar`feature`Variable names for `sysconf`UnlinkatFlags`fs`Flags for `unlinkat` function.Whence`fs`Directive that tells `lseek` and `lseek64` what the offset is relative to.

## Constants§

ROOT`user`Constant for UID = 0

## Functions§

access`fs`Checks the file named by `path` for accessibility according to the flags given by `amode`
See access(2)chdir`fs`Change the current working directory of the calling process (see
chdir(2)).chown`user` and `fs`Change the ownership of the file at `path` to be owned by the specified
`owner` (user) and `group` (see
chown(2)).chroot`fs`Change a process’s root directorycloseClose a file descriptor.daemon`process`Daemonize this process by detaching from the controlling terminal (see
daemon(3)).dup`fs`Create a copy of the specified file descriptor.dup2`fs`Create a copy of `oldfd` using `newfd`.dup3`fs`Create a new copy of the specified file descriptor using the specified fd
and flags.dup2_raw⚠`fs`Create a copy of `oldfd` with any fd value you want.dup2_stderr`fs`Duplicate `fd` with Stderr, i.e., Stderr redirection.dup2_stdin`fs`Duplicate `fd` with Stdin, i.e., Stdin redirection.dup2_stdout`fs`Duplicate `fd` with Stdout, i.e., Stdout redirection.dup3_raw⚠`fs`Create a new copy of the specified file descriptor using the specified fd
and flags.eaccess`fs`Checks the file named by `path` for accessibility according to the flags given
by `mode` using effective UID, effective GID and supplementary group lists.execv`process`Replace the current process image with a new one (see
exec(3)).execve`process`Replace the current process image with a new one (see
execve(2)).execveat`process`Execute program relative to a directory file descriptor (see
execveat(2)).execvp`process`Replace the current process image with a new one and replicate shell `PATH`
searching behavior (see
exec(3)).execvpe`process`Replace the current process image with a new one and replicate shell `PATH`
searching behavior (see
`execvpe(3)`).faccessat`fs`Checks the file named by `dirfd` and `path` for accessibility according to
the flags given by `mode`fchdir`fs`Change the current working directory of the process to the one
given as an open file descriptor (see
fchdir(2)).fchown`user` and `fs`Change the ownership of the file referred to by the open file descriptor
`fd` to be owned by the specified `owner` (user) and `group`.fchownat`user` and `fs`Change the ownership of the file at `path` to be owned by the specified
`owner` (user) and `group`.fdatasync`fs`Synchronize the data of a filefexecve`process`Replace the current process image with a new one (see
fexecve(2)).fork⚠`process`Create a new child process duplicating the parent process (see
fork(2)).fpathconf`fs` and `feature`Like `pathconf`, but works with file descriptors instead of paths (see
fpathconf(2))fsync`fs`Synchronize changes to a fileftruncate`fs`Truncate a file to a specified lengthgetcwd`fs`Returns the current directory as a `PathBuf`getegid`user`Get the effective group IDgeteuid`user`Get the effective user IDgetgid`user`Get the real group IDgetgrouplist`user`Calculate the supplementary group access list.getgroups`user`Get the list of supplementary group IDs of the calling process.gethostname`hostname`Get the host name and store it in an internally allocated buffer, returning an
`OsString` on success.getpgid`process`Get process groupgetpgrp`process`Get the group id of the calling process (see
getpgrp(3)).getpid`process`Get the pid of this process (see
getpid(2)).getppid`process`Get the pid of this processes’ parent (see
getpid(2)).getresgid`user`Gets the real, effective, and saved group IDs.getresuid`user`Gets the real, effective, and saved user IDs.getsid`process`Get the process group ID of a session leader
getsid(2).gettid`process`Get the caller’s thread ID (see
gettid(2).getuid`user`Get a real user IDinitgroups`user`Initialize the supplementary group access list.isatty`fs`Determines if the file descriptor refers to a valid terminal type device.linkat`fs`Link one file to another filelseek`fs`Move the read/write file offset.lseek64`fs`Move the read/write file offset.mkdir`fs`Creates new directory `path` with access rights `mode`.  (see mkdir(2))mkdtemp`fs` and `feature`Creates a directory which persists even after process terminationmkfifo`fs`Creates new FIFO special file (named pipe) with path `path` and access rights `mode`.mkfifoat`fs`Creates new FIFO special file (named pipe) with access rights set to `mode`
in the path specified by `dirfd` and `path`.mkstemp`fs`Creates a regular file which persists even after process terminationpathconf`fs` and `feature`Get path-dependent configurable system variables (see
pathconf(2))pause`signal`Suspend the thread until a signal is received.pipeCreate an interprocess channel.pipe2`fs`Like `pipe`, but allows setting certain file descriptor flags.pivot_root`fs`Change the root file system.readRead from a raw file descriptor.setegid`user`Set the effective group IDseteuid`user`Set the effective user IDsetfsgid`fs` and `user`Set the group identity used for filesystem checks per-thread.
On both success and failure, this call returns the previous filesystem group
ID of the caller.setfsuid`fs` and `user`Set the user identity used for filesystem checks per-thread.
On both success and failure, this call returns the previous filesystem user
ID of the caller.setgid`user`Set the group IDsetgroups`user`Set the list of supplementary group IDs for the calling process.sethostname`hostname`Set the system host name (see
sethostname(2)).setpgid`process`Set a process group ID (see
setpgid(2)).setresgid`user`Sets the real, effective, and saved gid.
(see setresuid(2))setresuid`user`Sets the real, effective, and saved uid.
(see setresuid(2))setsid`process`Create new session and set process group id (see
setsid(2)).setuid`user`Set the user IDsleepSuspend execution for an interval of timesymlinkat`fs`Creates a symbolic link to `path1` in the path specified by `dirfd` and
`path2`.sync`fs`Commit filesystem caches to disksyncfs`fs`Commit filesystem caches containing file referred to by the open file
descriptor `fd` to disksysconf`feature`Get configurable system variables (see
sysconf(3))tcgetpgrp`process` and `term`Get the terminal foreground process group (see
tcgetpgrp(3)).tcsetpgrp`process` and `term`Set the terminal foreground process group (see
tcsetpgrp(3)).truncate`fs`Truncate a file to a specified lengthttyname`term`Get the name of the terminal device that is open on file descriptor fd
(see `ttyname(3)`).unlink`fs`Remove a directory entryunlinkat`fs`Remove a directory entrywriteWrite to a raw file descriptor.

## Type Aliases§

FchownatFlags`user` and `fs`LinkatFlags`fs`
