# Source: https://docs.datadoghq.com/security/workload_protection/linux_expressions.md

---
title: Linux Agent attributes and helpers
description: Linux Agent attributes and helpers for Workload Protection Rules
breadcrumbs: >-
  Docs > Datadog Security > Workload Protection > Linux Agent attributes and
  helpers
---

# Linux Agent attributes and helpers

## Linux Agent attributes and helpers{% #linux-agent-attributes-and-helpers %}

This documentation describes Linux attributes and helpers of the [Datadog's Security Language (SECL)](https://docs.datadoghq.com/security/threats/agent).

Rules using Linux attributes and helpers must include an OS rule filter field as follows.

```yaml
id: [...]
expression: [...]
filters:
  - os == "linux"
```

## Triggers{% #triggers %}

Triggers are events that correspond to types of activity seen by the system. The currently supported set of triggers is:

| SECL Event             | Type    | Definition                                                  | Agent Version |
| ---------------------- | ------- | ----------------------------------------------------------- | ------------- |
| `accept`               | Network | An accept was executed                                      | 7.63          |
| `bind`                 | Network | A bind was executed                                         | 7.37          |
| `bpf`                  | Kernel  | A BPF command was executed                                  | 7.33          |
| `capabilities`         | Process | [Experimental] A process used some capabilities             | 7.70          |
| `capset`               | Process | A process changed its capacity set                          | 7.27          |
| `cgroup_write`         | Kernel  | A process migrated another process to a cgroup              | 7.68          |
| `chdir`                | File    | [Experimental] A process changed the current directory      | 7.52          |
| `chmod`                | File    | A file's permissions were changed                           | 7.27          |
| `chown`                | File    | A file's owner was changed                                  | 7.27          |
| `connect`              | Network | A connect was executed                                      | 7.60          |
| `dns`                  | Network | A DNS request was sent                                      | 7.36          |
| `exec`                 | Process | A process was executed (does not trigger on fork syscalls). | 7.27          |
| `exit`                 | Process | A process was terminated                                    | 7.38          |
| `imds`                 | Network | An IMDS event was captured                                  | 7.55          |
| `link`                 | File    | Create a new name/alias for a file                          | 7.27          |
| `load_module`          | Kernel  | A new kernel module was loaded                              | 7.35          |
| `mkdir`                | File    | A directory was created                                     | 7.27          |
| `mmap`                 | Kernel  | A mmap command was executed                                 | 7.35          |
| `mount`                | File    | [Experimental] A filesystem was mounted                     | 7.42          |
| `mprotect`             | Kernel  | A mprotect command was executed                             | 7.35          |
| `network_flow_monitor` | Network | A network monitor event was sent                            | 7.63          |
| `open`                 | File    | A file was opened                                           | 7.27          |
| `packet`               | Network | A raw network packet was captured                           | 7.60          |
| `prctl`                | Process | A prctl command was executed                                | 7.71          |
| `ptrace`               | Kernel  | A ptrace command was executed                               | 7.35          |
| `removexattr`          | File    | Remove extended attributes                                  | 7.27          |
| `rename`               | File    | A file/directory was renamed                                | 7.27          |
| `rmdir`                | File    | A directory was removed                                     | 7.27          |
| `selinux`              | Kernel  | An SELinux operation was run                                | 7.30          |
| `setgid`               | Process | A process changed its effective gid                         | 7.27          |
| `setrlimit`            | Process | A setrlimit command was executed                            | 7.68          |
| `setsockopt`           | Network | A setsockopt was executed                                   | 7.68          |
| `setuid`               | Process | A process changed its effective uid                         | 7.27          |
| `setxattr`             | File    | Set exteneded attributes                                    | 7.27          |
| `signal`               | Process | A signal was sent                                           | 7.35          |
| `splice`               | File    | A splice command was executed                               | 7.36          |
| `sysctl`               | Kernel  | A sysctl parameter was read or modified                     | 7.65          |
| `unlink`               | File    | A file was deleted                                          | 7.27          |
| `unload_module`        | Kernel  | A kernel module was deleted                                 | 7.35          |
| `utimes`               | File    | Change file access/modification times                       | 7.27          |

## FIM triggers{% #fim-triggers %}

In addition to regular triggers, `fim.write.file.*` fields allow to write rules that fire on all file events.

For example, the following rule:

```javascript
(fim.write.file.path == "/tmp/test" || fim.write.file.name == "abc")
  && process.file.name == "def"
  && container.id != ""
```

will expand into the following rules under the hood:

```javascript
open: ((open.file.path == "/tmp/test" || open.file.name == "abc")
  && open.flags & (O_CREAT|O_TRUNC|O_APPEND|O_RDWR|O_WRONLY) > 0
  && process.file.name == "def"
  && container.id != "")

chmod: (chmod.file.path == "/tmp/test" || chmod.file.name == "abc")
  && process.file.name == "def"
  && container.id != ""

chown: (chown.file.path == "/tmp/test" || chown.file.name == "abc")
  && process.file.name == "def"
  && container.id != ""

link: (link.file.path == "/tmp/test" || link.file.name == "abc")
  && process.file.name == "def"
  && container.id != ""

rename: (rename.file.path == "/tmp/test" || rename.file.name == "abc")
  && process.file.name == "def"
  && container.id != ""

rename: (rename.file.destination.path == "/tmp/test" || rename.file.destination.name == "abc")
  && process.file.name == "def"
  && container.id != ""

unlink: (unlink.file.path == "/tmp/test" || unlink.file.name == "abc")
  && process.file.name == "def"
  && container.id != ""

utimes: (utimes.file.path == "/tmp/test" || utimes.file.name == "abc")
  && process.file.name == "def"
  && container.id != ""
```

and match on all file-related events matching the path provided in the rule. Common fields are retained across all expanded rules.

## Variables{% #variables %}

SECL variables are predefined variables that can be used as values or as part of values.

For example, rule using a `process.pid` variable looks like this:

```javascript
open.file.path == "/proc/${process.pid}/maps"
```

List of the available variables:

| SECL Variable | Definition  | Agent Version |
| ------------- | ----------- | ------------- |
| `process.pid` | Process PID | 7.33          |

## CIDR and IP range{% #cidr-and-ip-range %}

CIDR and IP matching is possible in SECL. One can use operators such as `in`, `not in`, or `allin` combined with CIDR or IP notations.

Such rules can be written as follows:

```javascript
dns.question.name == "example.com" && network.destination.ip in [192.168.1.25, 10.0.0.0/24]
```

## Helpers{% #helpers %}

Helpers exist in SECL that enable users to write advanced rules without needing to rely on generic techniques such as regex.

### Command line arguments{% #command-line-arguments %}

The *args\_flags* and *args\_options* are helpers to ease the writing of CSM Threats rules based on command line arguments.

*args\_flags* is used to catch arguments that start with either one or two hyphen characters but do not accept any associated value.

Examples:

- `version` is part of *args\_flags* for the command `cat --version`
- `l` and `n` both are in *args\_flags* for the command `netstat -ln`

*args\_options* is used to catch arguments that start with either one or two hyphen characters and accepts a value either specified as the same argument but separated by the '=' character or specified as the next argument.

Examples:

- `T=8` and `width=8` both are in *args\_options* for the command `ls -T 8 --width=8`
- `exec.args_options in [ r"s=.*\\" ]` can be used to detect `sudoedit` was launched with `-s` argument and a command that ends with a `\`

### File rights{% #file-rights %}

The *file.rights* attribute can now be used in addition to *file.mode*. *file.mode* can hold values set by the kernel, while the *file.rights* only holds the values set by the user. These rights may be more familiar because they are in the `chmod` commands.

## Event attributes{% #event-attributes %}

### Common to all event types{% #common-to-all-event-types %}

| Property                                                    | Definition                                                                                                                           |
| ----------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| `event.async`                                               | True if the syscall was asynchronous                                                                                                 |
| `event.hostname`                                            | Hostname associated with the event                                                                                                   |
| `event.origin`                                              | Origin of the event                                                                                                                  |
| `event.os`                                                  | Operating system of the event                                                                                                        |
| `event.rule.tags`                                           | Tags associated with the rule that's used to evaluate the event                                                                      |
| `event.service`                                             | Service associated with the event                                                                                                    |
| `event.signature`                                           | Signature of the process pid and its cgroup with agent secret key                                                                    |
| `event.source`                                              | [Experimental] Source of the event. Can be either 'runtime' or 'snapshot'.                                                           |
| `event.timestamp`                                           | Timestamp of the event                                                                                                               |
| `process.ancestors.args`                                    | Arguments of the process (as a string, excluding argv0)                                                                              |
| `process.ancestors.args_flags`                              | Flags in the process arguments                                                                                                       |
| `process.ancestors.args_options`                            | Argument of the process as options                                                                                                   |
| `process.ancestors.args_truncated`                          | Indicator of arguments truncation                                                                                                    |
| `process.ancestors.argv`                                    | Arguments of the process (as an array, excluding argv0)                                                                              |
| `process.ancestors.argv0`                                   | First argument of the process                                                                                                        |
| `process.ancestors.auid`                                    | Login UID of the process                                                                                                             |
| `process.ancestors.cap_effective`                           | Effective capability set of the process                                                                                              |
| `process.ancestors.cap_permitted`                           | Permitted capability set of the process                                                                                              |
| `process.ancestors.caps_attempted`                          | Bitmask of the capabilities that the process attempted to use                                                                        |
| `process.ancestors.caps_used`                               | Bitmask of the capabilities that the process successfully used                                                                       |
| `process.ancestors.cgroup.file.inode`                       | Inode of the file                                                                                                                    |
| `process.ancestors.cgroup.file.mount_id`                    | Mount ID of the file                                                                                                                 |
| `process.ancestors.cgroup.id`                               | ID of the cgroup                                                                                                                     |
| `process.ancestors.cgroup.version`                          | [Experimental] Version of the cgroup API                                                                                             |
| `process.ancestors.comm`                                    | Comm attribute of the process                                                                                                        |
| `process.ancestors.container.created_at`                    | Timestamp of the creation of the container                                                                                           |
| `process.ancestors.container.id`                            | ID of the container                                                                                                                  |
| `process.ancestors.container.tags`                          | Tags of the container                                                                                                                |
| `process.ancestors.created_at`                              | Timestamp of the creation of the process                                                                                             |
| `process.ancestors.egid`                                    | Effective GID of the process                                                                                                         |
| `process.ancestors.egroup`                                  | Effective group of the process                                                                                                       |
| `process.ancestors.envp`                                    | Environment variables of the process                                                                                                 |
| `process.ancestors.envs`                                    | Environment variable names of the process                                                                                            |
| `process.ancestors.envs_truncated`                          | Indicator of environment variables truncation                                                                                        |
| `process.ancestors.euid`                                    | Effective UID of the process                                                                                                         |
| `process.ancestors.euser`                                   | Effective user of the process                                                                                                        |
| `process.ancestors.file.change_time`                        | Change time (ctime) of the file                                                                                                      |
| `process.ancestors.file.extension`                          | File's extension                                                                                                                     |
| `process.ancestors.file.filesystem`                         | File's filesystem                                                                                                                    |
| `process.ancestors.file.gid`                                | GID of the file's owner                                                                                                              |
| `process.ancestors.file.group`                              | Group of the file's owner                                                                                                            |
| `process.ancestors.file.hashes`                             | [Experimental] List of cryptographic hashes computed for this file                                                                   |
| `process.ancestors.file.in_upper_layer`                     | Indicator of the file layer, for example, in an OverlayFS                                                                            |
| `process.ancestors.file.inode`                              | Inode of the file                                                                                                                    |
| `process.ancestors.file.mode`                               | Mode of the file                                                                                                                     |
| `process.ancestors.file.modification_time`                  | Modification time (mtime) of the file                                                                                                |
| `process.ancestors.file.mount_detached`                     | Indicates whether the file's mount is detached from the VFS                                                                          |
| `process.ancestors.file.mount_id`                           | Mount ID of the file                                                                                                                 |
| `process.ancestors.file.mount_visible`                      | Indicates whether the file's mount is visible in the VFS                                                                             |
| `process.ancestors.file.name`                               | File's basename                                                                                                                      |
| `process.ancestors.file.name.length`                        | Length of the corresponding element                                                                                                  |
| `process.ancestors.file.package.epoch`                      | [Experimental] Epoch of the package that provided this file                                                                          |
| `process.ancestors.file.package.name`                       | [Experimental] Name of the package that provided this file                                                                           |
| `process.ancestors.file.package.release`                    | [Experimental] Release of the package that provided this file                                                                        |
| `process.ancestors.file.package.source_epoch`               | [Experimental] Epoch of the source package of the package that provided this file                                                    |
| `process.ancestors.file.package.source_release`             | [Experimental] Release of the source package of the package that provided this file                                                  |
| `process.ancestors.file.package.source_version`             | [Experimental] Full version of the source package of the package that provided this file                                             |
| `process.ancestors.file.package.version`                    | [Experimental] Full version of the package that provided this file                                                                   |
| `process.ancestors.file.path`                               | File's path                                                                                                                          |
| `process.ancestors.file.path.length`                        | Length of the corresponding element                                                                                                  |
| `process.ancestors.file.rights`                             | Rights of the file                                                                                                                   |
| `process.ancestors.file.uid`                                | UID of the file's owner                                                                                                              |
| `process.ancestors.file.user`                               | User of the file's owner                                                                                                             |
| `process.ancestors.fsgid`                                   | FileSystem-gid of the process                                                                                                        |
| `process.ancestors.fsgroup`                                 | FileSystem-group of the process                                                                                                      |
| `process.ancestors.fsuid`                                   | FileSystem-uid of the process                                                                                                        |
| `process.ancestors.fsuser`                                  | FileSystem-user of the process                                                                                                       |
| `process.ancestors.gid`                                     | GID of the process                                                                                                                   |
| `process.ancestors.group`                                   | Group of the process                                                                                                                 |
| `process.ancestors.interpreter.file.change_time`            | Change time (ctime) of the file                                                                                                      |
| `process.ancestors.interpreter.file.extension`              | File's extension                                                                                                                     |
| `process.ancestors.interpreter.file.filesystem`             | File's filesystem                                                                                                                    |
| `process.ancestors.interpreter.file.gid`                    | GID of the file's owner                                                                                                              |
| `process.ancestors.interpreter.file.group`                  | Group of the file's owner                                                                                                            |
| `process.ancestors.interpreter.file.hashes`                 | [Experimental] List of cryptographic hashes computed for this file                                                                   |
| `process.ancestors.interpreter.file.in_upper_layer`         | Indicator of the file layer, for example, in an OverlayFS                                                                            |
| `process.ancestors.interpreter.file.inode`                  | Inode of the file                                                                                                                    |
| `process.ancestors.interpreter.file.mode`                   | Mode of the file                                                                                                                     |
| `process.ancestors.interpreter.file.modification_time`      | Modification time (mtime) of the file                                                                                                |
| `process.ancestors.interpreter.file.mount_detached`         | Indicates whether the file's mount is detached from the VFS                                                                          |
| `process.ancestors.interpreter.file.mount_id`               | Mount ID of the file                                                                                                                 |
| `process.ancestors.interpreter.file.mount_visible`          | Indicates whether the file's mount is visible in the VFS                                                                             |
| `process.ancestors.interpreter.file.name`                   | File's basename                                                                                                                      |
| `process.ancestors.interpreter.file.name.length`            | Length of the corresponding element                                                                                                  |
| `process.ancestors.interpreter.file.package.epoch`          | [Experimental] Epoch of the package that provided this file                                                                          |
| `process.ancestors.interpreter.file.package.name`           | [Experimental] Name of the package that provided this file                                                                           |
| `process.ancestors.interpreter.file.package.release`        | [Experimental] Release of the package that provided this file                                                                        |
| `process.ancestors.interpreter.file.package.source_epoch`   | [Experimental] Epoch of the source package of the package that provided this file                                                    |
| `process.ancestors.interpreter.file.package.source_release` | [Experimental] Release of the source package of the package that provided this file                                                  |
| `process.ancestors.interpreter.file.package.source_version` | [Experimental] Full version of the source package of the package that provided this file                                             |
| `process.ancestors.interpreter.file.package.version`        | [Experimental] Full version of the package that provided this file                                                                   |
| `process.ancestors.interpreter.file.path`                   | File's path                                                                                                                          |
| `process.ancestors.interpreter.file.path.length`            | Length of the corresponding element                                                                                                  |
| `process.ancestors.interpreter.file.rights`                 | Rights of the file                                                                                                                   |
| `process.ancestors.interpreter.file.uid`                    | UID of the file's owner                                                                                                              |
| `process.ancestors.interpreter.file.user`                   | User of the file's owner                                                                                                             |
| `process.ancestors.is_exec`                                 | Indicates whether the process entry is from a new binary execution                                                                   |
| `process.ancestors.is_kworker`                              | Indicates whether the process is a kworker                                                                                           |
| `process.ancestors.is_thread`                               | Indicates whether the process is considered a thread (that is, a child process that hasn't executed another program)                 |
| `process.ancestors.length`                                  | Length of the corresponding element                                                                                                  |
| `process.ancestors.pid`                                     | Process ID of the process (also called thread group ID)                                                                              |
| `process.ancestors.ppid`                                    | Parent process ID                                                                                                                    |
| `process.ancestors.tid`                                     | Thread ID of the thread                                                                                                              |
| `process.ancestors.tty_name`                                | Name of the TTY associated with the process                                                                                          |
| `process.ancestors.uid`                                     | UID of the process                                                                                                                   |
| `process.ancestors.user`                                    | User of the process                                                                                                                  |
| `process.ancestors.user_session.id`                         | Unique identifier of the user session, alias for either ssh_session_id or k8s_session_id, depending on the session type              |
| `process.ancestors.user_session.identity`                   | User identity of the user session, alias for either ssh_client_ip and ssh_client_port or k8s_username, depending on the session type |
| `process.ancestors.user_session.k8s_groups`                 | Kubernetes groups of the user that executed the process                                                                              |
| `process.ancestors.user_session.k8s_session_id`             | Unique identifier of the kubernetes session                                                                                          |
| `process.ancestors.user_session.k8s_uid`                    | Kubernetes UID of the user that executed the process                                                                                 |
| `process.ancestors.user_session.k8s_username`               | Kubernetes username of the user that executed the process                                                                            |
| `process.ancestors.user_session.session_type`               | Type of the user session                                                                                                             |
| `process.ancestors.user_session.ssh_auth_method`            | SSH authentication method used by the user                                                                                           |
| `process.ancestors.user_session.ssh_client_ip`              | SSH client IP of the user that executed the process                                                                                  |
| `process.ancestors.user_session.ssh_client_port`            | SSH client port of the user that executed the process                                                                                |
| `process.ancestors.user_session.ssh_public_key`             | SSH public key used for authentication (if applicable)                                                                               |
| `process.ancestors.user_session.ssh_session_id`             | Unique identifier of the SSH user session on the host                                                                                |
| `process.args`                                              | Arguments of the process (as a string, excluding argv0)                                                                              |
| `process.args_flags`                                        | Flags in the process arguments                                                                                                       |
| `process.args_options`                                      | Argument of the process as options                                                                                                   |
| `process.args_truncated`                                    | Indicator of arguments truncation                                                                                                    |
| `process.argv`                                              | Arguments of the process (as an array, excluding argv0)                                                                              |
| `process.argv0`                                             | First argument of the process                                                                                                        |
| `process.auid`                                              | Login UID of the process                                                                                                             |
| `process.cap_effective`                                     | Effective capability set of the process                                                                                              |
| `process.cap_permitted`                                     | Permitted capability set of the process                                                                                              |
| `process.caps_attempted`                                    | Bitmask of the capabilities that the process attempted to use                                                                        |
| `process.caps_used`                                         | Bitmask of the capabilities that the process successfully used                                                                       |
| `process.cgroup.file.inode`                                 | Inode of the file                                                                                                                    |
| `process.cgroup.file.mount_id`                              | Mount ID of the file                                                                                                                 |
| `process.cgroup.id`                                         | ID of the cgroup                                                                                                                     |
| `process.cgroup.version`                                    | [Experimental] Version of the cgroup API                                                                                             |
| `process.comm`                                              | Comm attribute of the process                                                                                                        |
| `process.container.created_at`                              | Timestamp of the creation of the container                                                                                           |
| `process.container.id`                                      | ID of the container                                                                                                                  |
| `process.container.tags`                                    | Tags of the container                                                                                                                |
| `process.created_at`                                        | Timestamp of the creation of the process                                                                                             |
| `process.egid`                                              | Effective GID of the process                                                                                                         |
| `process.egroup`                                            | Effective group of the process                                                                                                       |
| `process.envp`                                              | Environment variables of the process                                                                                                 |
| `process.envs`                                              | Environment variable names of the process                                                                                            |
| `process.envs_truncated`                                    | Indicator of environment variables truncation                                                                                        |
| `process.euid`                                              | Effective UID of the process                                                                                                         |
| `process.euser`                                             | Effective user of the process                                                                                                        |
| `process.file.change_time`                                  | Change time (ctime) of the file                                                                                                      |
| `process.file.extension`                                    | File's extension                                                                                                                     |
| `process.file.filesystem`                                   | File's filesystem                                                                                                                    |
| `process.file.gid`                                          | GID of the file's owner                                                                                                              |
| `process.file.group`                                        | Group of the file's owner                                                                                                            |
| `process.file.hashes`                                       | [Experimental] List of cryptographic hashes computed for this file                                                                   |
| `process.file.in_upper_layer`                               | Indicator of the file layer, for example, in an OverlayFS                                                                            |
| `process.file.inode`                                        | Inode of the file                                                                                                                    |
| `process.file.mode`                                         | Mode of the file                                                                                                                     |
| `process.file.modification_time`                            | Modification time (mtime) of the file                                                                                                |
| `process.file.mount_detached`                               | Indicates whether the file's mount is detached from the VFS                                                                          |
| `process.file.mount_id`                                     | Mount ID of the file                                                                                                                 |
| `process.file.mount_visible`                                | Indicates whether the file's mount is visible in the VFS                                                                             |
| `process.file.name`                                         | File's basename                                                                                                                      |
| `process.file.name.length`                                  | Length of the corresponding element                                                                                                  |
| `process.file.package.epoch`                                | [Experimental] Epoch of the package that provided this file                                                                          |
| `process.file.package.name`                                 | [Experimental] Name of the package that provided this file                                                                           |
| `process.file.package.release`                              | [Experimental] Release of the package that provided this file                                                                        |
| `process.file.package.source_epoch`                         | [Experimental] Epoch of the source package of the package that provided this file                                                    |
| `process.file.package.source_release`                       | [Experimental] Release of the source package of the package that provided this file                                                  |
| `process.file.package.source_version`                       | [Experimental] Full version of the source package of the package that provided this file                                             |
| `process.file.package.version`                              | [Experimental] Full version of the package that provided this file                                                                   |
| `process.file.path`                                         | File's path                                                                                                                          |
| `process.file.path.length`                                  | Length of the corresponding element                                                                                                  |
| `process.file.rights`                                       | Rights of the file                                                                                                                   |
| `process.file.uid`                                          | UID of the file's owner                                                                                                              |
| `process.file.user`                                         | User of the file's owner                                                                                                             |
| `process.fsgid`                                             | FileSystem-gid of the process                                                                                                        |
| `process.fsgroup`                                           | FileSystem-group of the process                                                                                                      |
| `process.fsuid`                                             | FileSystem-uid of the process                                                                                                        |
| `process.fsuser`                                            | FileSystem-user of the process                                                                                                       |
| `process.gid`                                               | GID of the process                                                                                                                   |
| `process.group`                                             | Group of the process                                                                                                                 |
| `process.interpreter.file.change_time`                      | Change time (ctime) of the file                                                                                                      |
| `process.interpreter.file.extension`                        | File's extension                                                                                                                     |
| `process.interpreter.file.filesystem`                       | File's filesystem                                                                                                                    |
| `process.interpreter.file.gid`                              | GID of the file's owner                                                                                                              |
| `process.interpreter.file.group`                            | Group of the file's owner                                                                                                            |
| `process.interpreter.file.hashes`                           | [Experimental] List of cryptographic hashes computed for this file                                                                   |
| `process.interpreter.file.in_upper_layer`                   | Indicator of the file layer, for example, in an OverlayFS                                                                            |
| `process.interpreter.file.inode`                            | Inode of the file                                                                                                                    |
| `process.interpreter.file.mode`                             | Mode of the file                                                                                                                     |
| `process.interpreter.file.modification_time`                | Modification time (mtime) of the file                                                                                                |
| `process.interpreter.file.mount_detached`                   | Indicates whether the file's mount is detached from the VFS                                                                          |
| `process.interpreter.file.mount_id`                         | Mount ID of the file                                                                                                                 |
| `process.interpreter.file.mount_visible`                    | Indicates whether the file's mount is visible in the VFS                                                                             |
| `process.interpreter.file.name`                             | File's basename                                                                                                                      |
| `process.interpreter.file.name.length`                      | Length of the corresponding element                                                                                                  |
| `process.interpreter.file.package.epoch`                    | [Experimental] Epoch of the package that provided this file                                                                          |
| `process.interpreter.file.package.name`                     | [Experimental] Name of the package that provided this file                                                                           |
| `process.interpreter.file.package.release`                  | [Experimental] Release of the package that provided this file                                                                        |
| `process.interpreter.file.package.source_epoch`             | [Experimental] Epoch of the source package of the package that provided this file                                                    |
| `process.interpreter.file.package.source_release`           | [Experimental] Release of the source package of the package that provided this file                                                  |
| `process.interpreter.file.package.source_version`           | [Experimental] Full version of the source package of the package that provided this file                                             |
| `process.interpreter.file.package.version`                  | [Experimental] Full version of the package that provided this file                                                                   |
| `process.interpreter.file.path`                             | File's path                                                                                                                          |
| `process.interpreter.file.path.length`                      | Length of the corresponding element                                                                                                  |
| `process.interpreter.file.rights`                           | Rights of the file                                                                                                                   |
| `process.interpreter.file.uid`                              | UID of the file's owner                                                                                                              |
| `process.interpreter.file.user`                             | User of the file's owner                                                                                                             |
| `process.is_exec`                                           | Indicates whether the process entry is from a new binary execution                                                                   |
| `process.is_kworker`                                        | Indicates whether the process is a kworker                                                                                           |
| `process.is_thread`                                         | Indicates whether the process is considered a thread (that is, a child process that hasn't executed another program)                 |
| `process.parent.args`                                       | Arguments of the process (as a string, excluding argv0)                                                                              |
| `process.parent.args_flags`                                 | Flags in the process arguments                                                                                                       |
| `process.parent.args_options`                               | Argument of the process as options                                                                                                   |
| `process.parent.args_truncated`                             | Indicator of arguments truncation                                                                                                    |
| `process.parent.argv`                                       | Arguments of the process (as an array, excluding argv0)                                                                              |
| `process.parent.argv0`                                      | First argument of the process                                                                                                        |
| `process.parent.auid`                                       | Login UID of the process                                                                                                             |
| `process.parent.cap_effective`                              | Effective capability set of the process                                                                                              |
| `process.parent.cap_permitted`                              | Permitted capability set of the process                                                                                              |
| `process.parent.caps_attempted`                             | Bitmask of the capabilities that the process attempted to use                                                                        |
| `process.parent.caps_used`                                  | Bitmask of the capabilities that the process successfully used                                                                       |
| `process.parent.cgroup.file.inode`                          | Inode of the file                                                                                                                    |
| `process.parent.cgroup.file.mount_id`                       | Mount ID of the file                                                                                                                 |
| `process.parent.cgroup.id`                                  | ID of the cgroup                                                                                                                     |
| `process.parent.cgroup.version`                             | [Experimental] Version of the cgroup API                                                                                             |
| `process.parent.comm`                                       | Comm attribute of the process                                                                                                        |
| `process.parent.container.created_at`                       | Timestamp of the creation of the container                                                                                           |
| `process.parent.container.id`                               | ID of the container                                                                                                                  |
| `process.parent.container.tags`                             | Tags of the container                                                                                                                |
| `process.parent.created_at`                                 | Timestamp of the creation of the process                                                                                             |
| `process.parent.egid`                                       | Effective GID of the process                                                                                                         |
| `process.parent.egroup`                                     | Effective group of the process                                                                                                       |
| `process.parent.envp`                                       | Environment variables of the process                                                                                                 |
| `process.parent.envs`                                       | Environment variable names of the process                                                                                            |
| `process.parent.envs_truncated`                             | Indicator of environment variables truncation                                                                                        |
| `process.parent.euid`                                       | Effective UID of the process                                                                                                         |
| `process.parent.euser`                                      | Effective user of the process                                                                                                        |
| `process.parent.file.change_time`                           | Change time (ctime) of the file                                                                                                      |
| `process.parent.file.extension`                             | File's extension                                                                                                                     |
| `process.parent.file.filesystem`                            | File's filesystem                                                                                                                    |
| `process.parent.file.gid`                                   | GID of the file's owner                                                                                                              |
| `process.parent.file.group`                                 | Group of the file's owner                                                                                                            |
| `process.parent.file.hashes`                                | [Experimental] List of cryptographic hashes computed for this file                                                                   |
| `process.parent.file.in_upper_layer`                        | Indicator of the file layer, for example, in an OverlayFS                                                                            |
| `process.parent.file.inode`                                 | Inode of the file                                                                                                                    |
| `process.parent.file.mode`                                  | Mode of the file                                                                                                                     |
| `process.parent.file.modification_time`                     | Modification time (mtime) of the file                                                                                                |
| `process.parent.file.mount_detached`                        | Indicates whether the file's mount is detached from the VFS                                                                          |
| `process.parent.file.mount_id`                              | Mount ID of the file                                                                                                                 |
| `process.parent.file.mount_visible`                         | Indicates whether the file's mount is visible in the VFS                                                                             |
| `process.parent.file.name`                                  | File's basename                                                                                                                      |
| `process.parent.file.name.length`                           | Length of the corresponding element                                                                                                  |
| `process.parent.file.package.epoch`                         | [Experimental] Epoch of the package that provided this file                                                                          |
| `process.parent.file.package.name`                          | [Experimental] Name of the package that provided this file                                                                           |
| `process.parent.file.package.release`                       | [Experimental] Release of the package that provided this file                                                                        |
| `process.parent.file.package.source_epoch`                  | [Experimental] Epoch of the source package of the package that provided this file                                                    |
| `process.parent.file.package.source_release`                | [Experimental] Release of the source package of the package that provided this file                                                  |
| `process.parent.file.package.source_version`                | [Experimental] Full version of the source package of the package that provided this file                                             |
| `process.parent.file.package.version`                       | [Experimental] Full version of the package that provided this file                                                                   |
| `process.parent.file.path`                                  | File's path                                                                                                                          |
| `process.parent.file.path.length`                           | Length of the corresponding element                                                                                                  |
| `process.parent.file.rights`                                | Rights of the file                                                                                                                   |
| `process.parent.file.uid`                                   | UID of the file's owner                                                                                                              |
| `process.parent.file.user`                                  | User of the file's owner                                                                                                             |
| `process.parent.fsgid`                                      | FileSystem-gid of the process                                                                                                        |
| `process.parent.fsgroup`                                    | FileSystem-group of the process                                                                                                      |
| `process.parent.fsuid`                                      | FileSystem-uid of the process                                                                                                        |
| `process.parent.fsuser`                                     | FileSystem-user of the process                                                                                                       |
| `process.parent.gid`                                        | GID of the process                                                                                                                   |
| `process.parent.group`                                      | Group of the process                                                                                                                 |
| `process.parent.interpreter.file.change_time`               | Change time (ctime) of the file                                                                                                      |
| `process.parent.interpreter.file.extension`                 | File's extension                                                                                                                     |
| `process.parent.interpreter.file.filesystem`                | File's filesystem                                                                                                                    |
| `process.parent.interpreter.file.gid`                       | GID of the file's owner                                                                                                              |
| `process.parent.interpreter.file.group`                     | Group of the file's owner                                                                                                            |
| `process.parent.interpreter.file.hashes`                    | [Experimental] List of cryptographic hashes computed for this file                                                                   |
| `process.parent.interpreter.file.in_upper_layer`            | Indicator of the file layer, for example, in an OverlayFS                                                                            |
| `process.parent.interpreter.file.inode`                     | Inode of the file                                                                                                                    |
| `process.parent.interpreter.file.mode`                      | Mode of the file                                                                                                                     |
| `process.parent.interpreter.file.modification_time`         | Modification time (mtime) of the file                                                                                                |
| `process.parent.interpreter.file.mount_detached`            | Indicates whether the file's mount is detached from the VFS                                                                          |
| `process.parent.interpreter.file.mount_id`                  | Mount ID of the file                                                                                                                 |
| `process.parent.interpreter.file.mount_visible`             | Indicates whether the file's mount is visible in the VFS                                                                             |
| `process.parent.interpreter.file.name`                      | File's basename                                                                                                                      |
| `process.parent.interpreter.file.name.length`               | Length of the corresponding element                                                                                                  |
| `process.parent.interpreter.file.package.epoch`             | [Experimental] Epoch of the package that provided this file                                                                          |
| `process.parent.interpreter.file.package.name`              | [Experimental] Name of the package that provided this file                                                                           |
| `process.parent.interpreter.file.package.release`           | [Experimental] Release of the package that provided this file                                                                        |
| `process.parent.interpreter.file.package.source_epoch`      | [Experimental] Epoch of the source package of the package that provided this file                                                    |
| `process.parent.interpreter.file.package.source_release`    | [Experimental] Release of the source package of the package that provided this file                                                  |
| `process.parent.interpreter.file.package.source_version`    | [Experimental] Full version of the source package of the package that provided this file                                             |
| `process.parent.interpreter.file.package.version`           | [Experimental] Full version of the package that provided this file                                                                   |
| `process.parent.interpreter.file.path`                      | File's path                                                                                                                          |
| `process.parent.interpreter.file.path.length`               | Length of the corresponding element                                                                                                  |
| `process.parent.interpreter.file.rights`                    | Rights of the file                                                                                                                   |
| `process.parent.interpreter.file.uid`                       | UID of the file's owner                                                                                                              |
| `process.parent.interpreter.file.user`                      | User of the file's owner                                                                                                             |
| `process.parent.is_exec`                                    | Indicates whether the process entry is from a new binary execution                                                                   |
| `process.parent.is_kworker`                                 | Indicates whether the process is a kworker                                                                                           |
| `process.parent.is_thread`                                  | Indicates whether the process is considered a thread (that is, a child process that hasn't executed another program)                 |
| `process.parent.pid`                                        | Process ID of the process (also called thread group ID)                                                                              |
| `process.parent.ppid`                                       | Parent process ID                                                                                                                    |
| `process.parent.tid`                                        | Thread ID of the thread                                                                                                              |
| `process.parent.tty_name`                                   | Name of the TTY associated with the process                                                                                          |
| `process.parent.uid`                                        | UID of the process                                                                                                                   |
| `process.parent.user`                                       | User of the process                                                                                                                  |
| `process.parent.user_session.id`                            | Unique identifier of the user session, alias for either ssh_session_id or k8s_session_id, depending on the session type              |
| `process.parent.user_session.identity`                      | User identity of the user session, alias for either ssh_client_ip and ssh_client_port or k8s_username, depending on the session type |
| `process.parent.user_session.k8s_groups`                    | Kubernetes groups of the user that executed the process                                                                              |
| `process.parent.user_session.k8s_session_id`                | Unique identifier of the kubernetes session                                                                                          |
| `process.parent.user_session.k8s_uid`                       | Kubernetes UID of the user that executed the process                                                                                 |
| `process.parent.user_session.k8s_username`                  | Kubernetes username of the user that executed the process                                                                            |
| `process.parent.user_session.session_type`                  | Type of the user session                                                                                                             |
| `process.parent.user_session.ssh_auth_method`               | SSH authentication method used by the user                                                                                           |
| `process.parent.user_session.ssh_client_ip`                 | SSH client IP of the user that executed the process                                                                                  |
| `process.parent.user_session.ssh_client_port`               | SSH client port of the user that executed the process                                                                                |
| `process.parent.user_session.ssh_public_key`                | SSH public key used for authentication (if applicable)                                                                               |
| `process.parent.user_session.ssh_session_id`                | Unique identifier of the SSH user session on the host                                                                                |
| `process.pid`                                               | Process ID of the process (also called thread group ID)                                                                              |
| `process.ppid`                                              | Parent process ID                                                                                                                    |
| `process.tid`                                               | Thread ID of the thread                                                                                                              |
| `process.tty_name`                                          | Name of the TTY associated with the process                                                                                          |
| `process.uid`                                               | UID of the process                                                                                                                   |
| `process.user`                                              | User of the process                                                                                                                  |
| `process.user_session.id`                                   | Unique identifier of the user session, alias for either ssh_session_id or k8s_session_id, depending on the session type              |
| `process.user_session.identity`                             | User identity of the user session, alias for either ssh_client_ip and ssh_client_port or k8s_username, depending on the session type |
| `process.user_session.k8s_groups`                           | Kubernetes groups of the user that executed the process                                                                              |
| `process.user_session.k8s_session_id`                       | Unique identifier of the kubernetes session                                                                                          |
| `process.user_session.k8s_uid`                              | Kubernetes UID of the user that executed the process                                                                                 |
| `process.user_session.k8s_username`                         | Kubernetes username of the user that executed the process                                                                            |
| `process.user_session.session_type`                         | Type of the user session                                                                                                             |
| `process.user_session.ssh_auth_method`                      | SSH authentication method used by the user                                                                                           |
| `process.user_session.ssh_client_ip`                        | SSH client IP of the user that executed the process                                                                                  |
| `process.user_session.ssh_client_port`                      | SSH client port of the user that executed the process                                                                                |
| `process.user_session.ssh_public_key`                       | SSH public key used for authentication (if applicable)                                                                               |
| `process.user_session.ssh_session_id`                       | Unique identifier of the SSH user session on the host                                                                                |

### Event `accept`{% #event-accept %}

An accept was executed

| Property                | Definition                                         |
| ----------------------- | -------------------------------------------------- |
| `accept.addr.family`    | Address family                                     |
| `accept.addr.hostname`  | Address hostname (if available)                    |
| `accept.addr.ip`        | IP address                                         |
| `accept.addr.is_public` | Whether the IP address belongs to a public network |
| `accept.addr.port`      | Port number                                        |
| `accept.retval`         | Return value of the syscall                        |

### Event `bind`{% #event-bind %}

A bind was executed

| Property              | Definition                                         |
| --------------------- | -------------------------------------------------- |
| `bind.addr.family`    | Address family                                     |
| `bind.addr.ip`        | IP address                                         |
| `bind.addr.is_public` | Whether the IP address belongs to a public network |
| `bind.addr.port`      | Port number                                        |
| `bind.protocol`       | Socket Protocol                                    |
| `bind.retval`         | Return value of the syscall                        |

### Event `bpf`{% #event-bpf %}

A BPF command was executed

| Property               | Definition                                            |
| ---------------------- | ----------------------------------------------------- |
| `bpf.cmd`              | BPF command name                                      |
| `bpf.map.name`         | Name of the eBPF map (added in 7.35)                  |
| `bpf.map.type`         | Type of the eBPF map                                  |
| `bpf.prog.attach_type` | Attach type of the eBPF program                       |
| `bpf.prog.helpers`     | eBPF helpers used by the eBPF program (added in 7.35) |
| `bpf.prog.name`        | Name of the eBPF program (added in 7.35)              |
| `bpf.prog.tag`         | Hash (sha1) of the eBPF program (added in 7.35)       |
| `bpf.prog.type`        | Type of the eBPF program                              |
| `bpf.retval`           | Return value of the syscall                           |

### Event `capabilities`{% #event-capabilities %}

*This event type is experimental and may change in the future.*

A process used some capabilities

| Property                 | Definition                                                                              |
| ------------------------ | --------------------------------------------------------------------------------------- |
| `capabilities.attempted` | Bitmask of the capabilities that the process attempted to use since it started running  |
| `capabilities.used`      | Bitmask of the capabilities that the process successfully used since it started running |

### Event `capset`{% #event-capset %}

A process changed its capacity set

| Property               | Definition                              |
| ---------------------- | --------------------------------------- |
| `capset.cap_effective` | Effective capability set of the process |
| `capset.cap_permitted` | Permitted capability set of the process |

### Event `cgroup_write`{% #event-cgroup_write %}

A process migrated another process to a cgroup

| Property                                   | Definition                                                                               |
| ------------------------------------------ | ---------------------------------------------------------------------------------------- |
| `cgroup_write.file.change_time`            | Change time (ctime) of the file                                                          |
| `cgroup_write.file.extension`              | File's extension                                                                         |
| `cgroup_write.file.filesystem`             | File's filesystem                                                                        |
| `cgroup_write.file.gid`                    | GID of the file's owner                                                                  |
| `cgroup_write.file.group`                  | Group of the file's owner                                                                |
| `cgroup_write.file.hashes`                 | [Experimental] List of cryptographic hashes computed for this file                       |
| `cgroup_write.file.in_upper_layer`         | Indicator of the file layer, for example, in an OverlayFS                                |
| `cgroup_write.file.inode`                  | Inode of the file                                                                        |
| `cgroup_write.file.mode`                   | Mode of the file                                                                         |
| `cgroup_write.file.modification_time`      | Modification time (mtime) of the file                                                    |
| `cgroup_write.file.mount_detached`         | Indicates whether the file's mount is detached from the VFS                              |
| `cgroup_write.file.mount_id`               | Mount ID of the file                                                                     |
| `cgroup_write.file.mount_visible`          | Indicates whether the file's mount is visible in the VFS                                 |
| `cgroup_write.file.name`                   | File's basename                                                                          |
| `cgroup_write.file.name.length`            | Length of the corresponding element                                                      |
| `cgroup_write.file.package.epoch`          | [Experimental] Epoch of the package that provided this file                              |
| `cgroup_write.file.package.name`           | [Experimental] Name of the package that provided this file                               |
| `cgroup_write.file.package.release`        | [Experimental] Release of the package that provided this file                            |
| `cgroup_write.file.package.source_epoch`   | [Experimental] Epoch of the source package of the package that provided this file        |
| `cgroup_write.file.package.source_release` | [Experimental] Release of the source package of the package that provided this file      |
| `cgroup_write.file.package.source_version` | [Experimental] Full version of the source package of the package that provided this file |
| `cgroup_write.file.package.version`        | [Experimental] Full version of the package that provided this file                       |
| `cgroup_write.file.path`                   | File's path                                                                              |
| `cgroup_write.file.path.length`            | Length of the corresponding element                                                      |
| `cgroup_write.file.rights`                 | Rights of the file                                                                       |
| `cgroup_write.file.uid`                    | UID of the file's owner                                                                  |
| `cgroup_write.file.user`                   | User of the file's owner                                                                 |
| `cgroup_write.pid`                         | PID of the process added to the cgroup                                                   |

### Event `chdir`{% #event-chdir %}

*This event type is experimental and may change in the future.*

A process changed the current directory

| Property                            | Definition                                                                               |
| ----------------------------------- | ---------------------------------------------------------------------------------------- |
| `chdir.file.change_time`            | Change time (ctime) of the file                                                          |
| `chdir.file.extension`              | File's extension                                                                         |
| `chdir.file.filesystem`             | File's filesystem                                                                        |
| `chdir.file.gid`                    | GID of the file's owner                                                                  |
| `chdir.file.group`                  | Group of the file's owner                                                                |
| `chdir.file.hashes`                 | [Experimental] List of cryptographic hashes computed for this file                       |
| `chdir.file.in_upper_layer`         | Indicator of the file layer, for example, in an OverlayFS                                |
| `chdir.file.inode`                  | Inode of the file                                                                        |
| `chdir.file.mode`                   | Mode of the file                                                                         |
| `chdir.file.modification_time`      | Modification time (mtime) of the file                                                    |
| `chdir.file.mount_detached`         | Indicates whether the file's mount is detached from the VFS                              |
| `chdir.file.mount_id`               | Mount ID of the file                                                                     |
| `chdir.file.mount_visible`          | Indicates whether the file's mount is visible in the VFS                                 |
| `chdir.file.name`                   | File's basename                                                                          |
| `chdir.file.name.length`            | Length of the corresponding element                                                      |
| `chdir.file.package.epoch`          | [Experimental] Epoch of the package that provided this file                              |
| `chdir.file.package.name`           | [Experimental] Name of the package that provided this file                               |
| `chdir.file.package.release`        | [Experimental] Release of the package that provided this file                            |
| `chdir.file.package.source_epoch`   | [Experimental] Epoch of the source package of the package that provided this file        |
| `chdir.file.package.source_release` | [Experimental] Release of the source package of the package that provided this file      |
| `chdir.file.package.source_version` | [Experimental] Full version of the source package of the package that provided this file |
| `chdir.file.package.version`        | [Experimental] Full version of the package that provided this file                       |
| `chdir.file.path`                   | File's path                                                                              |
| `chdir.file.path.length`            | Length of the corresponding element                                                      |
| `chdir.file.rights`                 | Rights of the file                                                                       |
| `chdir.file.uid`                    | UID of the file's owner                                                                  |
| `chdir.file.user`                   | User of the file's owner                                                                 |
| `chdir.retval`                      | Return value of the syscall                                                              |
| `chdir.syscall.path`                | path argument of the syscall                                                             |

### Event `chmod`{% #event-chmod %}

A file's permissions were changed

| Property                            | Definition                                                                               |
| ----------------------------------- | ---------------------------------------------------------------------------------------- |
| `chmod.file.change_time`            | Change time (ctime) of the file                                                          |
| `chmod.file.destination.mode`       | New mode of the chmod-ed file                                                            |
| `chmod.file.destination.rights`     | New rights of the chmod-ed file                                                          |
| `chmod.file.extension`              | File's extension                                                                         |
| `chmod.file.filesystem`             | File's filesystem                                                                        |
| `chmod.file.gid`                    | GID of the file's owner                                                                  |
| `chmod.file.group`                  | Group of the file's owner                                                                |
| `chmod.file.hashes`                 | [Experimental] List of cryptographic hashes computed for this file                       |
| `chmod.file.in_upper_layer`         | Indicator of the file layer, for example, in an OverlayFS                                |
| `chmod.file.inode`                  | Inode of the file                                                                        |
| `chmod.file.mode`                   | Mode of the file                                                                         |
| `chmod.file.modification_time`      | Modification time (mtime) of the file                                                    |
| `chmod.file.mount_detached`         | Indicates whether the file's mount is detached from the VFS                              |
| `chmod.file.mount_id`               | Mount ID of the file                                                                     |
| `chmod.file.mount_visible`          | Indicates whether the file's mount is visible in the VFS                                 |
| `chmod.file.name`                   | File's basename                                                                          |
| `chmod.file.name.length`            | Length of the corresponding element                                                      |
| `chmod.file.package.epoch`          | [Experimental] Epoch of the package that provided this file                              |
| `chmod.file.package.name`           | [Experimental] Name of the package that provided this file                               |
| `chmod.file.package.release`        | [Experimental] Release of the package that provided this file                            |
| `chmod.file.package.source_epoch`   | [Experimental] Epoch of the source package of the package that provided this file        |
| `chmod.file.package.source_release` | [Experimental] Release of the source package of the package that provided this file      |
| `chmod.file.package.source_version` | [Experimental] Full version of the source package of the package that provided this file |
| `chmod.file.package.version`        | [Experimental] Full version of the package that provided this file                       |
| `chmod.file.path`                   | File's path                                                                              |
| `chmod.file.path.length`            | Length of the corresponding element                                                      |
| `chmod.file.rights`                 | Rights of the file                                                                       |
| `chmod.file.uid`                    | UID of the file's owner                                                                  |
| `chmod.file.user`                   | User of the file's owner                                                                 |
| `chmod.retval`                      | Return value of the syscall                                                              |
| `chmod.syscall.mode`                | mode argument of the syscall                                                             |
| `chmod.syscall.path`                | path argument of the syscall                                                             |

### Event `chown`{% #event-chown %}

A file's owner was changed

| Property                            | Definition                                                                               |
| ----------------------------------- | ---------------------------------------------------------------------------------------- |
| `chown.file.change_time`            | Change time (ctime) of the file                                                          |
| `chown.file.destination.gid`        | New GID of the chown-ed file's owner                                                     |
| `chown.file.destination.group`      | New group of the chown-ed file's owner                                                   |
| `chown.file.destination.uid`        | New UID of the chown-ed file's owner                                                     |
| `chown.file.destination.user`       | New user of the chown-ed file's owner                                                    |
| `chown.file.extension`              | File's extension                                                                         |
| `chown.file.filesystem`             | File's filesystem                                                                        |
| `chown.file.gid`                    | GID of the file's owner                                                                  |
| `chown.file.group`                  | Group of the file's owner                                                                |
| `chown.file.hashes`                 | [Experimental] List of cryptographic hashes computed for this file                       |
| `chown.file.in_upper_layer`         | Indicator of the file layer, for example, in an OverlayFS                                |
| `chown.file.inode`                  | Inode of the file                                                                        |
| `chown.file.mode`                   | Mode of the file                                                                         |
| `chown.file.modification_time`      | Modification time (mtime) of the file                                                    |
| `chown.file.mount_detached`         | Indicates whether the file's mount is detached from the VFS                              |
| `chown.file.mount_id`               | Mount ID of the file                                                                     |
| `chown.file.mount_visible`          | Indicates whether the file's mount is visible in the VFS                                 |
| `chown.file.name`                   | File's basename                                                                          |
| `chown.file.name.length`            | Length of the corresponding element                                                      |
| `chown.file.package.epoch`          | [Experimental] Epoch of the package that provided this file                              |
| `chown.file.package.name`           | [Experimental] Name of the package that provided this file                               |
| `chown.file.package.release`        | [Experimental] Release of the package that provided this file                            |
| `chown.file.package.source_epoch`   | [Experimental] Epoch of the source package of the package that provided this file        |
| `chown.file.package.source_release` | [Experimental] Release of the source package of the package that provided this file      |
| `chown.file.package.source_version` | [Experimental] Full version of the source package of the package that provided this file |
| `chown.file.package.version`        | [Experimental] Full version of the package that provided this file                       |
| `chown.file.path`                   | File's path                                                                              |
| `chown.file.path.length`            | Length of the corresponding element                                                      |
| `chown.file.rights`                 | Rights of the file                                                                       |
| `chown.file.uid`                    | UID of the file's owner                                                                  |
| `chown.file.user`                   | User of the file's owner                                                                 |
| `chown.retval`                      | Return value of the syscall                                                              |
| `chown.syscall.gid`                 | GID argument of the syscall                                                              |
| `chown.syscall.path`                | Path argument of the syscall                                                             |
| `chown.syscall.uid`                 | UID argument of the syscall                                                              |

### Event `connect`{% #event-connect %}

A connect was executed

| Property                 | Definition                                         |
| ------------------------ | -------------------------------------------------- |
| `connect.addr.family`    | Address family                                     |
| `connect.addr.hostname`  | Address hostname (if available)                    |
| `connect.addr.ip`        | IP address                                         |
| `connect.addr.is_public` | Whether the IP address belongs to a public network |
| `connect.addr.port`      | Port number                                        |
| `connect.protocol`       | Socket Protocol                                    |
| `connect.retval`         | Return value of the syscall                        |

### Event `dns`{% #event-dns %}

A DNS request was sent

| Property                        | Definition                                              |
| ------------------------------- | ------------------------------------------------------- |
| `dns.id`                        | [Experimental] the DNS request ID                       |
| `dns.question.class`            | the class looked up by the DNS question                 |
| `dns.question.count`            | the total count of questions in the DNS request         |
| `dns.question.length`           | the total DNS request size in bytes                     |
| `dns.question.name`             | the queried domain name                                 |
| `dns.question.name.length`      | Length of the corresponding element                     |
| `dns.question.type`             | a two octet code which specifies the DNS question type  |
| `dns.response.code`             | Response code of the DNS response according to RFC 1035 |
| `network.destination.ip`        | IP address                                              |
| `network.destination.is_public` | Whether the IP address belongs to a public network      |
| `network.destination.port`      | Port number                                             |
| `network.device.ifname`         | Interface ifname                                        |
| `network.l3_protocol`           | L3 protocol of the network packet                       |
| `network.l4_protocol`           | L4 protocol of the network packet                       |
| `network.network_direction`     | Network direction of the network packet                 |
| `network.size`                  | Size in bytes of the network packet                     |
| `network.source.ip`             | IP address                                              |
| `network.source.is_public`      | Whether the IP address belongs to a public network      |
| `network.source.port`           | Port number                                             |
| `network.type`                  | Type of the network packet                              |

### Event `exec`{% #event-exec %}

A process was executed (does not trigger on fork syscalls).

| Property                                       | Definition                                                                                                                           |
| ---------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| `exec.args`                                    | Arguments of the process (as a string, excluding argv0)                                                                              |
| `exec.args_flags`                              | Flags in the process arguments                                                                                                       |
| `exec.args_options`                            | Argument of the process as options                                                                                                   |
| `exec.args_truncated`                          | Indicator of arguments truncation                                                                                                    |
| `exec.argv`                                    | Arguments of the process (as an array, excluding argv0)                                                                              |
| `exec.argv0`                                   | First argument of the process                                                                                                        |
| `exec.auid`                                    | Login UID of the process                                                                                                             |
| `exec.cap_effective`                           | Effective capability set of the process                                                                                              |
| `exec.cap_permitted`                           | Permitted capability set of the process                                                                                              |
| `exec.caps_attempted`                          | Bitmask of the capabilities that the process attempted to use                                                                        |
| `exec.caps_used`                               | Bitmask of the capabilities that the process successfully used                                                                       |
| `exec.cgroup.file.inode`                       | Inode of the file                                                                                                                    |
| `exec.cgroup.file.mount_id`                    | Mount ID of the file                                                                                                                 |
| `exec.cgroup.id`                               | ID of the cgroup                                                                                                                     |
| `exec.cgroup.version`                          | [Experimental] Version of the cgroup API                                                                                             |
| `exec.comm`                                    | Comm attribute of the process                                                                                                        |
| `exec.container.created_at`                    | Timestamp of the creation of the container                                                                                           |
| `exec.container.id`                            | ID of the container                                                                                                                  |
| `exec.container.tags`                          | Tags of the container                                                                                                                |
| `exec.created_at`                              | Timestamp of the creation of the process                                                                                             |
| `exec.egid`                                    | Effective GID of the process                                                                                                         |
| `exec.egroup`                                  | Effective group of the process                                                                                                       |
| `exec.envp`                                    | Environment variables of the process                                                                                                 |
| `exec.envs`                                    | Environment variable names of the process                                                                                            |
| `exec.envs_truncated`                          | Indicator of environment variables truncation                                                                                        |
| `exec.euid`                                    | Effective UID of the process                                                                                                         |
| `exec.euser`                                   | Effective user of the process                                                                                                        |
| `exec.file.change_time`                        | Change time (ctime) of the file                                                                                                      |
| `exec.file.extension`                          | File's extension                                                                                                                     |
| `exec.file.filesystem`                         | File's filesystem                                                                                                                    |
| `exec.file.gid`                                | GID of the file's owner                                                                                                              |
| `exec.file.group`                              | Group of the file's owner                                                                                                            |
| `exec.file.hashes`                             | [Experimental] List of cryptographic hashes computed for this file                                                                   |
| `exec.file.in_upper_layer`                     | Indicator of the file layer, for example, in an OverlayFS                                                                            |
| `exec.file.inode`                              | Inode of the file                                                                                                                    |
| `exec.file.metadata.abi`                       | [Experimental] ABI of the file (only for executable files)                                                                           |
| `exec.file.metadata.architecture`              | [Experimental] Architecture of the file (only for executable files)                                                                  |
| `exec.file.metadata.compression`               | [Experimental] Compression type of the file (only for compressed files)                                                              |
| `exec.file.metadata.is_executable`             | [Experimental] Tells if the file is executable or not                                                                                |
| `exec.file.metadata.is_garble_obfuscated`      | [Experimental] Tells if the binary has been obfuscated using garble                                                                  |
| `exec.file.metadata.is_upx_packed`             | [Experimental] Tells if the binary has been packed using UPX                                                                         |
| `exec.file.metadata.size`                      | [Experimental] Size of the file                                                                                                      |
| `exec.file.metadata.type`                      | [Experimental] Type of the file                                                                                                      |
| `exec.file.mode`                               | Mode of the file                                                                                                                     |
| `exec.file.modification_time`                  | Modification time (mtime) of the file                                                                                                |
| `exec.file.mount_detached`                     | Indicates whether the file's mount is detached from the VFS                                                                          |
| `exec.file.mount_id`                           | Mount ID of the file                                                                                                                 |
| `exec.file.mount_visible`                      | Indicates whether the file's mount is visible in the VFS                                                                             |
| `exec.file.name`                               | File's basename                                                                                                                      |
| `exec.file.name.length`                        | Length of the corresponding element                                                                                                  |
| `exec.file.package.epoch`                      | [Experimental] Epoch of the package that provided this file                                                                          |
| `exec.file.package.name`                       | [Experimental] Name of the package that provided this file                                                                           |
| `exec.file.package.release`                    | [Experimental] Release of the package that provided this file                                                                        |
| `exec.file.package.source_epoch`               | [Experimental] Epoch of the source package of the package that provided this file                                                    |
| `exec.file.package.source_release`             | [Experimental] Release of the source package of the package that provided this file                                                  |
| `exec.file.package.source_version`             | [Experimental] Full version of the source package of the package that provided this file                                             |
| `exec.file.package.version`                    | [Experimental] Full version of the package that provided this file                                                                   |
| `exec.file.path`                               | File's path                                                                                                                          |
| `exec.file.path.length`                        | Length of the corresponding element                                                                                                  |
| `exec.file.rights`                             | Rights of the file                                                                                                                   |
| `exec.file.uid`                                | UID of the file's owner                                                                                                              |
| `exec.file.user`                               | User of the file's owner                                                                                                             |
| `exec.fsgid`                                   | FileSystem-gid of the process                                                                                                        |
| `exec.fsgroup`                                 | FileSystem-group of the process                                                                                                      |
| `exec.fsuid`                                   | FileSystem-uid of the process                                                                                                        |
| `exec.fsuser`                                  | FileSystem-user of the process                                                                                                       |
| `exec.gid`                                     | GID of the process                                                                                                                   |
| `exec.group`                                   | Group of the process                                                                                                                 |
| `exec.interpreter.file.change_time`            | Change time (ctime) of the file                                                                                                      |
| `exec.interpreter.file.extension`              | File's extension                                                                                                                     |
| `exec.interpreter.file.filesystem`             | File's filesystem                                                                                                                    |
| `exec.interpreter.file.gid`                    | GID of the file's owner                                                                                                              |
| `exec.interpreter.file.group`                  | Group of the file's owner                                                                                                            |
| `exec.interpreter.file.hashes`                 | [Experimental] List of cryptographic hashes computed for this file                                                                   |
| `exec.interpreter.file.in_upper_layer`         | Indicator of the file layer, for example, in an OverlayFS                                                                            |
| `exec.interpreter.file.inode`                  | Inode of the file                                                                                                                    |
| `exec.interpreter.file.mode`                   | Mode of the file                                                                                                                     |
| `exec.interpreter.file.modification_time`      | Modification time (mtime) of the file                                                                                                |
| `exec.interpreter.file.mount_detached`         | Indicates whether the file's mount is detached from the VFS                                                                          |
| `exec.interpreter.file.mount_id`               | Mount ID of the file                                                                                                                 |
| `exec.interpreter.file.mount_visible`          | Indicates whether the file's mount is visible in the VFS                                                                             |
| `exec.interpreter.file.name`                   | File's basename                                                                                                                      |
| `exec.interpreter.file.name.length`            | Length of the corresponding element                                                                                                  |
| `exec.interpreter.file.package.epoch`          | [Experimental] Epoch of the package that provided this file                                                                          |
| `exec.interpreter.file.package.name`           | [Experimental] Name of the package that provided this file                                                                           |
| `exec.interpreter.file.package.release`        | [Experimental] Release of the package that provided this file                                                                        |
| `exec.interpreter.file.package.source_epoch`   | [Experimental] Epoch of the source package of the package that provided this file                                                    |
| `exec.interpreter.file.package.source_release` | [Experimental] Release of the source package of the package that provided this file                                                  |
| `exec.interpreter.file.package.source_version` | [Experimental] Full version of the source package of the package that provided this file                                             |
| `exec.interpreter.file.package.version`        | [Experimental] Full version of the package that provided this file                                                                   |
| `exec.interpreter.file.path`                   | File's path                                                                                                                          |
| `exec.interpreter.file.path.length`            | Length of the corresponding element                                                                                                  |
| `exec.interpreter.file.rights`                 | Rights of the file                                                                                                                   |
| `exec.interpreter.file.uid`                    | UID of the file's owner                                                                                                              |
| `exec.interpreter.file.user`                   | User of the file's owner                                                                                                             |
| `exec.is_exec`                                 | Indicates whether the process entry is from a new binary execution                                                                   |
| `exec.is_kworker`                              | Indicates whether the process is a kworker                                                                                           |
| `exec.is_thread`                               | Indicates whether the process is considered a thread (that is, a child process that hasn't executed another program)                 |
| `exec.pid`                                     | Process ID of the process (also called thread group ID)                                                                              |
| `exec.ppid`                                    | Parent process ID                                                                                                                    |
| `exec.syscall.path`                            | path argument of the syscall                                                                                                         |
| `exec.tid`                                     | Thread ID of the thread                                                                                                              |
| `exec.tty_name`                                | Name of the TTY associated with the process                                                                                          |
| `exec.uid`                                     | UID of the process                                                                                                                   |
| `exec.user`                                    | User of the process                                                                                                                  |
| `exec.user_session.id`                         | Unique identifier of the user session, alias for either ssh_session_id or k8s_session_id, depending on the session type              |
| `exec.user_session.identity`                   | User identity of the user session, alias for either ssh_client_ip and ssh_client_port or k8s_username, depending on the session type |
| `exec.user_session.k8s_groups`                 | Kubernetes groups of the user that executed the process                                                                              |
| `exec.user_session.k8s_session_id`             | Unique identifier of the kubernetes session                                                                                          |
| `exec.user_session.k8s_uid`                    | Kubernetes UID of the user that executed the process                                                                                 |
| `exec.user_session.k8s_username`               | Kubernetes username of the user that executed the process                                                                            |
| `exec.user_session.session_type`               | Type of the user session                                                                                                             |
| `exec.user_session.ssh_auth_method`            | SSH authentication method used by the user                                                                                           |
| `exec.user_session.ssh_client_ip`              | SSH client IP of the user that executed the process                                                                                  |
| `exec.user_session.ssh_client_port`            | SSH client port of the user that executed the process                                                                                |
| `exec.user_session.ssh_public_key`             | SSH public key used for authentication (if applicable)                                                                               |
| `exec.user_session.ssh_session_id`             | Unique identifier of the SSH user session on the host                                                                                |

### Event `exit`{% #event-exit %}

A process was terminated

| Property                                       | Definition                                                                                                                           |
| ---------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| `exit.args`                                    | Arguments of the process (as a string, excluding argv0)                                                                              |
| `exit.args_flags`                              | Flags in the process arguments                                                                                                       |
| `exit.args_options`                            | Argument of the process as options                                                                                                   |
| `exit.args_truncated`                          | Indicator of arguments truncation                                                                                                    |
| `exit.argv`                                    | Arguments of the process (as an array, excluding argv0)                                                                              |
| `exit.argv0`                                   | First argument of the process                                                                                                        |
| `exit.auid`                                    | Login UID of the process                                                                                                             |
| `exit.cap_effective`                           | Effective capability set of the process                                                                                              |
| `exit.cap_permitted`                           | Permitted capability set of the process                                                                                              |
| `exit.caps_attempted`                          | Bitmask of the capabilities that the process attempted to use                                                                        |
| `exit.caps_used`                               | Bitmask of the capabilities that the process successfully used                                                                       |
| `exit.cause`                                   | Cause of the process termination (one of EXITED, SIGNALED, COREDUMPED)                                                               |
| `exit.cgroup.file.inode`                       | Inode of the file                                                                                                                    |
| `exit.cgroup.file.mount_id`                    | Mount ID of the file                                                                                                                 |
| `exit.cgroup.id`                               | ID of the cgroup                                                                                                                     |
| `exit.cgroup.version`                          | [Experimental] Version of the cgroup API                                                                                             |
| `exit.code`                                    | Exit code of the process or number of the signal that caused the process to terminate                                                |
| `exit.comm`                                    | Comm attribute of the process                                                                                                        |
| `exit.container.created_at`                    | Timestamp of the creation of the container                                                                                           |
| `exit.container.id`                            | ID of the container                                                                                                                  |
| `exit.container.tags`                          | Tags of the container                                                                                                                |
| `exit.created_at`                              | Timestamp of the creation of the process                                                                                             |
| `exit.egid`                                    | Effective GID of the process                                                                                                         |
| `exit.egroup`                                  | Effective group of the process                                                                                                       |
| `exit.envp`                                    | Environment variables of the process                                                                                                 |
| `exit.envs`                                    | Environment variable names of the process                                                                                            |
| `exit.envs_truncated`                          | Indicator of environment variables truncation                                                                                        |
| `exit.euid`                                    | Effective UID of the process                                                                                                         |
| `exit.euser`                                   | Effective user of the process                                                                                                        |
| `exit.file.change_time`                        | Change time (ctime) of the file                                                                                                      |
| `exit.file.extension`                          | File's extension                                                                                                                     |
| `exit.file.filesystem`                         | File's filesystem                                                                                                                    |
| `exit.file.gid`                                | GID of the file's owner                                                                                                              |
| `exit.file.group`                              | Group of the file's owner                                                                                                            |
| `exit.file.hashes`                             | [Experimental] List of cryptographic hashes computed for this file                                                                   |
| `exit.file.in_upper_layer`                     | Indicator of the file layer, for example, in an OverlayFS                                                                            |
| `exit.file.inode`                              | Inode of the file                                                                                                                    |
| `exit.file.mode`                               | Mode of the file                                                                                                                     |
| `exit.file.modification_time`                  | Modification time (mtime) of the file                                                                                                |
| `exit.file.mount_detached`                     | Indicates whether the file's mount is detached from the VFS                                                                          |
| `exit.file.mount_id`                           | Mount ID of the file                                                                                                                 |
| `exit.file.mount_visible`                      | Indicates whether the file's mount is visible in the VFS                                                                             |
| `exit.file.name`                               | File's basename                                                                                                                      |
| `exit.file.name.length`                        | Length of the corresponding element                                                                                                  |
| `exit.file.package.epoch`                      | [Experimental] Epoch of the package that provided this file                                                                          |
| `exit.file.package.name`                       | [Experimental] Name of the package that provided this file                                                                           |
| `exit.file.package.release`                    | [Experimental] Release of the package that provided this file                                                                        |
| `exit.file.package.source_epoch`               | [Experimental] Epoch of the source package of the package that provided this file                                                    |
| `exit.file.package.source_release`             | [Experimental] Release of the source package of the package that provided this file                                                  |
| `exit.file.package.source_version`             | [Experimental] Full version of the source package of the package that provided this file                                             |
| `exit.file.package.version`                    | [Experimental] Full version of the package that provided this file                                                                   |
| `exit.file.path`                               | File's path                                                                                                                          |
| `exit.file.path.length`                        | Length of the corresponding element                                                                                                  |
| `exit.file.rights`                             | Rights of the file                                                                                                                   |
| `exit.file.uid`                                | UID of the file's owner                                                                                                              |
| `exit.file.user`                               | User of the file's owner                                                                                                             |
| `exit.fsgid`                                   | FileSystem-gid of the process                                                                                                        |
| `exit.fsgroup`                                 | FileSystem-group of the process                                                                                                      |
| `exit.fsuid`                                   | FileSystem-uid of the process                                                                                                        |
| `exit.fsuser`                                  | FileSystem-user of the process                                                                                                       |
| `exit.gid`                                     | GID of the process                                                                                                                   |
| `exit.group`                                   | Group of the process                                                                                                                 |
| `exit.interpreter.file.change_time`            | Change time (ctime) of the file                                                                                                      |
| `exit.interpreter.file.extension`              | File's extension                                                                                                                     |
| `exit.interpreter.file.filesystem`             | File's filesystem                                                                                                                    |
| `exit.interpreter.file.gid`                    | GID of the file's owner                                                                                                              |
| `exit.interpreter.file.group`                  | Group of the file's owner                                                                                                            |
| `exit.interpreter.file.hashes`                 | [Experimental] List of cryptographic hashes computed for this file                                                                   |
| `exit.interpreter.file.in_upper_layer`         | Indicator of the file layer, for example, in an OverlayFS                                                                            |
| `exit.interpreter.file.inode`                  | Inode of the file                                                                                                                    |
| `exit.interpreter.file.mode`                   | Mode of the file                                                                                                                     |
| `exit.interpreter.file.modification_time`      | Modification time (mtime) of the file                                                                                                |
| `exit.interpreter.file.mount_detached`         | Indicates whether the file's mount is detached from the VFS                                                                          |
| `exit.interpreter.file.mount_id`               | Mount ID of the file                                                                                                                 |
| `exit.interpreter.file.mount_visible`          | Indicates whether the file's mount is visible in the VFS                                                                             |
| `exit.interpreter.file.name`                   | File's basename                                                                                                                      |
| `exit.interpreter.file.name.length`            | Length of the corresponding element                                                                                                  |
| `exit.interpreter.file.package.epoch`          | [Experimental] Epoch of the package that provided this file                                                                          |
| `exit.interpreter.file.package.name`           | [Experimental] Name of the package that provided this file                                                                           |
| `exit.interpreter.file.package.release`        | [Experimental] Release of the package that provided this file                                                                        |
| `exit.interpreter.file.package.source_epoch`   | [Experimental] Epoch of the source package of the package that provided this file                                                    |
| `exit.interpreter.file.package.source_release` | [Experimental] Release of the source package of the package that provided this file                                                  |
| `exit.interpreter.file.package.source_version` | [Experimental] Full version of the source package of the package that provided this file                                             |
| `exit.interpreter.file.package.version`        | [Experimental] Full version of the package that provided this file                                                                   |
| `exit.interpreter.file.path`                   | File's path                                                                                                                          |
| `exit.interpreter.file.path.length`            | Length of the corresponding element                                                                                                  |
| `exit.interpreter.file.rights`                 | Rights of the file                                                                                                                   |
| `exit.interpreter.file.uid`                    | UID of the file's owner                                                                                                              |
| `exit.interpreter.file.user`                   | User of the file's owner                                                                                                             |
| `exit.is_exec`                                 | Indicates whether the process entry is from a new binary execution                                                                   |
| `exit.is_kworker`                              | Indicates whether the process is a kworker                                                                                           |
| `exit.is_thread`                               | Indicates whether the process is considered a thread (that is, a child process that hasn't executed another program)                 |
| `exit.pid`                                     | Process ID of the process (also called thread group ID)                                                                              |
| `exit.ppid`                                    | Parent process ID                                                                                                                    |
| `exit.tid`                                     | Thread ID of the thread                                                                                                              |
| `exit.tty_name`                                | Name of the TTY associated with the process                                                                                          |
| `exit.uid`                                     | UID of the process                                                                                                                   |
| `exit.user`                                    | User of the process                                                                                                                  |
| `exit.user_session.id`                         | Unique identifier of the user session, alias for either ssh_session_id or k8s_session_id, depending on the session type              |
| `exit.user_session.identity`                   | User identity of the user session, alias for either ssh_client_ip and ssh_client_port or k8s_username, depending on the session type |
| `exit.user_session.k8s_groups`                 | Kubernetes groups of the user that executed the process                                                                              |
| `exit.user_session.k8s_session_id`             | Unique identifier of the kubernetes session                                                                                          |
| `exit.user_session.k8s_uid`                    | Kubernetes UID of the user that executed the process                                                                                 |
| `exit.user_session.k8s_username`               | Kubernetes username of the user that executed the process                                                                            |
| `exit.user_session.session_type`               | Type of the user session                                                                                                             |
| `exit.user_session.ssh_auth_method`            | SSH authentication method used by the user                                                                                           |
| `exit.user_session.ssh_client_ip`              | SSH client IP of the user that executed the process                                                                                  |
| `exit.user_session.ssh_client_port`            | SSH client port of the user that executed the process                                                                                |
| `exit.user_session.ssh_public_key`             | SSH public key used for authentication (if applicable)                                                                               |
| `exit.user_session.ssh_session_id`             | Unique identifier of the SSH user session on the host                                                                                |

### Event `imds`{% #event-imds %}

An IMDS event was captured

| Property                             | Definition                                                                       |
| ------------------------------------ | -------------------------------------------------------------------------------- |
| `imds.aws.is_imds_v2`                | a boolean which specifies if the IMDS event follows IMDSv1 or IMDSv2 conventions |
| `imds.aws.security_credentials.type` | the security credentials type                                                    |
| `imds.cloud_provider`                | the intended cloud provider of the IMDS event                                    |
| `imds.host`                          | the host of the HTTP protocol                                                    |
| `imds.server`                        | the server header of a response                                                  |
| `imds.type`                          | the type of IMDS event                                                           |
| `imds.url`                           | the queried IMDS URL                                                             |
| `imds.user_agent`                    | the user agent of the HTTP client                                                |
| `network.destination.ip`             | IP address                                                                       |
| `network.destination.is_public`      | Whether the IP address belongs to a public network                               |
| `network.destination.port`           | Port number                                                                      |
| `network.device.ifname`              | Interface ifname                                                                 |
| `network.l3_protocol`                | L3 protocol of the network packet                                                |
| `network.l4_protocol`                | L4 protocol of the network packet                                                |
| `network.network_direction`          | Network direction of the network packet                                          |
| `network.size`                       | Size in bytes of the network packet                                              |
| `network.source.ip`                  | IP address                                                                       |
| `network.source.is_public`           | Whether the IP address belongs to a public network                               |
| `network.source.port`                | Port number                                                                      |
| `network.type`                       | Type of the network packet                                                       |

### Event `link`{% #event-link %}

Create a new name/alias for a file

| Property                                       | Definition                                                                               |
| ---------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `link.file.change_time`                        | Change time (ctime) of the file                                                          |
| `link.file.destination.change_time`            | Change time (ctime) of the file                                                          |
| `link.file.destination.extension`              | File's extension                                                                         |
| `link.file.destination.filesystem`             | File's filesystem                                                                        |
| `link.file.destination.gid`                    | GID of the file's owner                                                                  |
| `link.file.destination.group`                  | Group of the file's owner                                                                |
| `link.file.destination.hashes`                 | [Experimental] List of cryptographic hashes computed for this file                       |
| `link.file.destination.in_upper_layer`         | Indicator of the file layer, for example, in an OverlayFS                                |
| `link.file.destination.inode`                  | Inode of the file                                                                        |
| `link.file.destination.mode`                   | Mode of the file                                                                         |
| `link.file.destination.modification_time`      | Modification time (mtime) of the file                                                    |
| `link.file.destination.mount_detached`         | Indicates whether the file's mount is detached from the VFS                              |
| `link.file.destination.mount_id`               | Mount ID of the file                                                                     |
| `link.file.destination.mount_visible`          | Indicates whether the file's mount is visible in the VFS                                 |
| `link.file.destination.name`                   | File's basename                                                                          |
| `link.file.destination.name.length`            | Length of the corresponding element                                                      |
| `link.file.destination.package.epoch`          | [Experimental] Epoch of the package that provided this file                              |
| `link.file.destination.package.name`           | [Experimental] Name of the package that provided this file                               |
| `link.file.destination.package.release`        | [Experimental] Release of the package that provided this file                            |
| `link.file.destination.package.source_epoch`   | [Experimental] Epoch of the source package of the package that provided this file        |
| `link.file.destination.package.source_release` | [Experimental] Release of the source package of the package that provided this file      |
| `link.file.destination.package.source_version` | [Experimental] Full version of the source package of the package that provided this file |
| `link.file.destination.package.version`        | [Experimental] Full version of the package that provided this file                       |
| `link.file.destination.path`                   | File's path                                                                              |
| `link.file.destination.path.length`            | Length of the corresponding element                                                      |
| `link.file.destination.rights`                 | Rights of the file                                                                       |
| `link.file.destination.uid`                    | UID of the file's owner                                                                  |
| `link.file.destination.user`                   | User of the file's owner                                                                 |
| `link.file.extension`                          | File's extension                                                                         |
| `link.file.filesystem`                         | File's filesystem                                                                        |
| `link.file.gid`                                | GID of the file's owner                                                                  |
| `link.file.group`                              | Group of the file's owner                                                                |
| `link.file.hashes`                             | [Experimental] List of cryptographic hashes computed for this file                       |
| `link.file.in_upper_layer`                     | Indicator of the file layer, for example, in an OverlayFS                                |
| `link.file.inode`                              | Inode of the file                                                                        |
| `link.file.mode`                               | Mode of the file                                                                         |
| `link.file.modification_time`                  | Modification time (mtime) of the file                                                    |
| `link.file.mount_detached`                     | Indicates whether the file's mount is detached from the VFS                              |
| `link.file.mount_id`                           | Mount ID of the file                                                                     |
| `link.file.mount_visible`                      | Indicates whether the file's mount is visible in the VFS                                 |
| `link.file.name`                               | File's basename                                                                          |
| `link.file.name.length`                        | Length of the corresponding element                                                      |
| `link.file.package.epoch`                      | [Experimental] Epoch of the package that provided this file                              |
| `link.file.package.name`                       | [Experimental] Name of the package that provided this file                               |
| `link.file.package.release`                    | [Experimental] Release of the package that provided this file                            |
| `link.file.package.source_epoch`               | [Experimental] Epoch of the source package of the package that provided this file        |
| `link.file.package.source_release`             | [Experimental] Release of the source package of the package that provided this file      |
| `link.file.package.source_version`             | [Experimental] Full version of the source package of the package that provided this file |
| `link.file.package.version`                    | [Experimental] Full version of the package that provided this file                       |
| `link.file.path`                               | File's path                                                                              |
| `link.file.path.length`                        | Length of the corresponding element                                                      |
| `link.file.rights`                             | Rights of the file                                                                       |
| `link.file.uid`                                | UID of the file's owner                                                                  |
| `link.file.user`                               | User of the file's owner                                                                 |
| `link.retval`                                  | Return value of the syscall                                                              |
| `link.syscall.destination.path`                | Destination path argument of the syscall                                                 |
| `link.syscall.path`                            | Path argument of the syscall                                                             |

### Event `load_module`{% #event-load_module %}

A new kernel module was loaded

| Property                                  | Definition                                                                               |
| ----------------------------------------- | ---------------------------------------------------------------------------------------- |
| `load_module.args`                        | Parameters (as a string) of the new kernel module                                        |
| `load_module.args_truncated`              | Indicates if the arguments were truncated or not                                         |
| `load_module.argv`                        | Parameters (as an array) of the new kernel module                                        |
| `load_module.file.change_time`            | Change time (ctime) of the file                                                          |
| `load_module.file.extension`              | File's extension                                                                         |
| `load_module.file.filesystem`             | File's filesystem                                                                        |
| `load_module.file.gid`                    | GID of the file's owner                                                                  |
| `load_module.file.group`                  | Group of the file's owner                                                                |
| `load_module.file.hashes`                 | [Experimental] List of cryptographic hashes computed for this file                       |
| `load_module.file.in_upper_layer`         | Indicator of the file layer, for example, in an OverlayFS                                |
| `load_module.file.inode`                  | Inode of the file                                                                        |
| `load_module.file.mode`                   | Mode of the file                                                                         |
| `load_module.file.modification_time`      | Modification time (mtime) of the file                                                    |
| `load_module.file.mount_detached`         | Indicates whether the file's mount is detached from the VFS                              |
| `load_module.file.mount_id`               | Mount ID of the file                                                                     |
| `load_module.file.mount_visible`          | Indicates whether the file's mount is visible in the VFS                                 |
| `load_module.file.name`                   | File's basename                                                                          |
| `load_module.file.name.length`            | Length of the corresponding element                                                      |
| `load_module.file.package.epoch`          | [Experimental] Epoch of the package that provided this file                              |
| `load_module.file.package.name`           | [Experimental] Name of the package that provided this file                               |
| `load_module.file.package.release`        | [Experimental] Release of the package that provided this file                            |
| `load_module.file.package.source_epoch`   | [Experimental] Epoch of the source package of the package that provided this file        |
| `load_module.file.package.source_release` | [Experimental] Release of the source package of the package that provided this file      |
| `load_module.file.package.source_version` | [Experimental] Full version of the source package of the package that provided this file |
| `load_module.file.package.version`        | [Experimental] Full version of the package that provided this file                       |
| `load_module.file.path`                   | File's path                                                                              |
| `load_module.file.path.length`            | Length of the corresponding element                                                      |
| `load_module.file.rights`                 | Rights of the file                                                                       |
| `load_module.file.uid`                    | UID of the file's owner                                                                  |
| `load_module.file.user`                   | User of the file's owner                                                                 |
| `load_module.loaded_from_memory`          | Indicates if the kernel module was loaded from memory                                    |
| `load_module.name`                        | Name of the new kernel module                                                            |
| `load_module.retval`                      | Return value of the syscall                                                              |

### Event `mkdir`{% #event-mkdir %}

A directory was created

| Property                            | Definition                                                                               |
| ----------------------------------- | ---------------------------------------------------------------------------------------- |
| `mkdir.file.change_time`            | Change time (ctime) of the file                                                          |
| `mkdir.file.destination.mode`       | Mode of the new directory                                                                |
| `mkdir.file.destination.rights`     | Rights of the new directory                                                              |
| `mkdir.file.extension`              | File's extension                                                                         |
| `mkdir.file.filesystem`             | File's filesystem                                                                        |
| `mkdir.file.gid`                    | GID of the file's owner                                                                  |
| `mkdir.file.group`                  | Group of the file's owner                                                                |
| `mkdir.file.hashes`                 | [Experimental] List of cryptographic hashes computed for this file                       |
| `mkdir.file.in_upper_layer`         | Indicator of the file layer, for example, in an OverlayFS                                |
| `mkdir.file.inode`                  | Inode of the file                                                                        |
| `mkdir.file.mode`                   | Mode of the file                                                                         |
| `mkdir.file.modification_time`      | Modification time (mtime) of the file                                                    |
| `mkdir.file.mount_detached`         | Indicates whether the file's mount is detached from the VFS                              |
| `mkdir.file.mount_id`               | Mount ID of the file                                                                     |
| `mkdir.file.mount_visible`          | Indicates whether the file's mount is visible in the VFS                                 |
| `mkdir.file.name`                   | File's basename                                                                          |
| `mkdir.file.name.length`            | Length of the corresponding element                                                      |
| `mkdir.file.package.epoch`          | [Experimental] Epoch of the package that provided this file                              |
| `mkdir.file.package.name`           | [Experimental] Name of the package that provided this file                               |
| `mkdir.file.package.release`        | [Experimental] Release of the package that provided this file                            |
| `mkdir.file.package.source_epoch`   | [Experimental] Epoch of the source package of the package that provided this file        |
| `mkdir.file.package.source_release` | [Experimental] Release of the source package of the package that provided this file      |
| `mkdir.file.package.source_version` | [Experimental] Full version of the source package of the package that provided this file |
| `mkdir.file.package.version`        | [Experimental] Full version of the package that provided this file                       |
| `mkdir.file.path`                   | File's path                                                                              |
| `mkdir.file.path.length`            | Length of the corresponding element                                                      |
| `mkdir.file.rights`                 | Rights of the file                                                                       |
| `mkdir.file.uid`                    | UID of the file's owner                                                                  |
| `mkdir.file.user`                   | User of the file's owner                                                                 |
| `mkdir.retval`                      | Return value of the syscall                                                              |
| `mkdir.syscall.mode`                | Mode of the new directory                                                                |
| `mkdir.syscall.path`                | Path argument of the syscall                                                             |

### Event `mmap`{% #event-mmap %}

A mmap command was executed

| Property                           | Definition                                                                               |
| ---------------------------------- | ---------------------------------------------------------------------------------------- |
| `mmap.file.change_time`            | Change time (ctime) of the file                                                          |
| `mmap.file.extension`              | File's extension                                                                         |
| `mmap.file.filesystem`             | File's filesystem                                                                        |
| `mmap.file.gid`                    | GID of the file's owner                                                                  |
| `mmap.file.group`                  | Group of the file's owner                                                                |
| `mmap.file.hashes`                 | [Experimental] List of cryptographic hashes computed for this file                       |
| `mmap.file.in_upper_layer`         | Indicator of the file layer, for example, in an OverlayFS                                |
| `mmap.file.inode`                  | Inode of the file                                                                        |
| `mmap.file.mode`                   | Mode of the file                                                                         |
| `mmap.file.modification_time`      | Modification time (mtime) of the file                                                    |
| `mmap.file.mount_detached`         | Indicates whether the file's mount is detached from the VFS                              |
| `mmap.file.mount_id`               | Mount ID of the file                                                                     |
| `mmap.file.mount_visible`          | Indicates whether the file's mount is visible in the VFS                                 |
| `mmap.file.name`                   | File's basename                                                                          |
| `mmap.file.name.length`            | Length of the corresponding element                                                      |
| `mmap.file.package.epoch`          | [Experimental] Epoch of the package that provided this file                              |
| `mmap.file.package.name`           | [Experimental] Name of the package that provided this file                               |
| `mmap.file.package.release`        | [Experimental] Release of the package that provided this file                            |
| `mmap.file.package.source_epoch`   | [Experimental] Epoch of the source package of the package that provided this file        |
| `mmap.file.package.source_release` | [Experimental] Release of the source package of the package that provided this file      |
| `mmap.file.package.source_version` | [Experimental] Full version of the source package of the package that provided this file |
| `mmap.file.package.version`        | [Experimental] Full version of the package that provided this file                       |
| `mmap.file.path`                   | File's path                                                                              |
| `mmap.file.path.length`            | Length of the corresponding element                                                      |
| `mmap.file.rights`                 | Rights of the file                                                                       |
| `mmap.file.uid`                    | UID of the file's owner                                                                  |
| `mmap.file.user`                   | User of the file's owner                                                                 |
| `mmap.flags`                       | memory segment flags                                                                     |
| `mmap.protection`                  | memory segment protection                                                                |
| `mmap.retval`                      | Return value of the syscall                                                              |

### Event `mount`{% #event-mount %}

*This event type is experimental and may change in the future.*

A filesystem was mounted

| Property                        | Definition                               |
| ------------------------------- | ---------------------------------------- |
| `mount.detached`                | Mount is detached from the VFS           |
| `mount.fs_type`                 | Type of the mounted file system          |
| `mount.mountpoint.path`         | Path of the mount point                  |
| `mount.retval`                  | Return value of the syscall              |
| `mount.root.path`               | Root path of the mount                   |
| `mount.source.path`             | Source path of a bind mount              |
| `mount.syscall.fs_type`         | File system type argument of the syscall |
| `mount.syscall.mountpoint.path` | Mount point path argument of the syscall |
| `mount.syscall.source.path`     | Source path argument of the syscall      |
| `mount.visible`                 | Mount is not visible in the VFS          |

### Event `mprotect`{% #event-mprotect %}

A mprotect command was executed

| Property                  | Definition                        |
| ------------------------- | --------------------------------- |
| `mprotect.req_protection` | new memory segment protection     |
| `mprotect.retval`         | Return value of the syscall       |
| `mprotect.vm_protection`  | initial memory segment protection |

### Event `network_flow_monitor`{% #event-network_flow_monitor %}

A network monitor event was sent

| Property                                           | Definition                                         |
| -------------------------------------------------- | -------------------------------------------------- |
| `network_flow_monitor.device.ifname`               | Interface ifname                                   |
| `network_flow_monitor.flows.destination.ip`        | IP address                                         |
| `network_flow_monitor.flows.destination.is_public` | Whether the IP address belongs to a public network |
| `network_flow_monitor.flows.destination.port`      | Port number                                        |
| `network_flow_monitor.flows.egress.data_size`      | Amount of data transmitted or received             |
| `network_flow_monitor.flows.egress.packet_count`   | Count of network packets transmitted or received   |
| `network_flow_monitor.flows.ingress.data_size`     | Amount of data transmitted or received             |
| `network_flow_monitor.flows.ingress.packet_count`  | Count of network packets transmitted or received   |
| `network_flow_monitor.flows.l3_protocol`           | L3 protocol of the network packet                  |
| `network_flow_monitor.flows.l4_protocol`           | L4 protocol of the network packet                  |
| `network_flow_monitor.flows.length`                | Length of the corresponding element                |
| `network_flow_monitor.flows.source.ip`             | IP address                                         |
| `network_flow_monitor.flows.source.is_public`      | Whether the IP address belongs to a public network |
| `network_flow_monitor.flows.source.port`           | Port number                                        |

### Event `open`{% #event-open %}

A file was opened

| Property                           | Definition                                                                               |
| ---------------------------------- | ---------------------------------------------------------------------------------------- |
| `open.file.change_time`            | Change time (ctime) of the file                                                          |
| `open.file.destination.mode`       | Mode of the created file                                                                 |
| `open.file.extension`              | File's extension                                                                         |
| `open.file.filesystem`             | File's filesystem                                                                        |
| `open.file.gid`                    | GID of the file's owner                                                                  |
| `open.file.group`                  | Group of the file's owner                                                                |
| `open.file.hashes`                 | [Experimental] List of cryptographic hashes computed for this file                       |
| `open.file.in_upper_layer`         | Indicator of the file layer, for example, in an OverlayFS                                |
| `open.file.inode`                  | Inode of the file                                                                        |
| `open.file.mode`                   | Mode of the file                                                                         |
| `open.file.modification_time`      | Modification time (mtime) of the file                                                    |
| `open.file.mount_detached`         | Indicates whether the file's mount is detached from the VFS                              |
| `open.file.mount_id`               | Mount ID of the file                                                                     |
| `open.file.mount_visible`          | Indicates whether the file's mount is visible in the VFS                                 |
| `open.file.name`                   | File's basename                                                                          |
| `open.file.name.length`            | Length of the corresponding element                                                      |
| `open.file.package.epoch`          | [Experimental] Epoch of the package that provided this file                              |
| `open.file.package.name`           | [Experimental] Name of the package that provided this file                               |
| `open.file.package.release`        | [Experimental] Release of the package that provided this file                            |
| `open.file.package.source_epoch`   | [Experimental] Epoch of the source package of the package that provided this file        |
| `open.file.package.source_release` | [Experimental] Release of the source package of the package that provided this file      |
| `open.file.package.source_version` | [Experimental] Full version of the source package of the package that provided this file |
| `open.file.package.version`        | [Experimental] Full version of the package that provided this file                       |
| `open.file.path`                   | File's path                                                                              |
| `open.file.path.length`            | Length of the corresponding element                                                      |
| `open.file.rights`                 | Rights of the file                                                                       |
| `open.file.uid`                    | UID of the file's owner                                                                  |
| `open.file.user`                   | User of the file's owner                                                                 |
| `open.flags`                       | Flags used when opening the file                                                         |
| `open.retval`                      | Return value of the syscall                                                              |
| `open.syscall.flags`               | Flags argument of the syscall                                                            |
| `open.syscall.mode`                | Mode argument of the syscall                                                             |
| `open.syscall.path`                | Path argument of the syscall                                                             |

### Event `packet`{% #event-packet %}

A raw network packet was captured

| Property                        | Definition                                         |
| ------------------------------- | -------------------------------------------------- |
| `network.destination.ip`        | IP address                                         |
| `network.destination.is_public` | Whether the IP address belongs to a public network |
| `network.destination.port`      | Port number                                        |
| `network.device.ifname`         | Interface ifname                                   |
| `network.l3_protocol`           | L3 protocol of the network packet                  |
| `network.l4_protocol`           | L4 protocol of the network packet                  |
| `network.network_direction`     | Network direction of the network packet            |
| `network.size`                  | Size in bytes of the network packet                |
| `network.source.ip`             | IP address                                         |
| `network.source.is_public`      | Whether the IP address belongs to a public network |
| `network.source.port`           | Port number                                        |
| `network.type`                  | Type of the network packet                         |
| `packet.destination.ip`         | IP address                                         |
| `packet.destination.is_public`  | Whether the IP address belongs to a public network |
| `packet.destination.port`       | Port number                                        |
| `packet.device.ifname`          | Interface ifname                                   |
| `packet.filter`                 | pcap filter expression                             |
| `packet.l3_protocol`            | L3 protocol of the network packet                  |
| `packet.l4_protocol`            | L4 protocol of the network packet                  |
| `packet.network_direction`      | Network direction of the network packet            |
| `packet.size`                   | Size in bytes of the network packet                |
| `packet.source.ip`              | IP address                                         |
| `packet.source.is_public`       | Whether the IP address belongs to a public network |
| `packet.source.port`            | Port number                                        |
| `packet.tls.version`            | TLS version                                        |
| `packet.type`                   | Type of the network packet                         |

### Event `prctl`{% #event-prctl %}

A prctl command was executed

| Property                  | Definition                                 |
| ------------------------- | ------------------------------------------ |
| `prctl.is_name_truncated` | Indicates that the name field is truncated |
| `prctl.new_name`          | New name of the process                    |
| `prctl.option`            | prctl option                               |
| `prctl.retval`            | Return value of the syscall                |

### Event `ptrace`{% #event-ptrace %}

A ptrace command was executed

| Property                                                          | Definition                                                                                                                           |
| ----------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| `ptrace.request`                                                  | ptrace request                                                                                                                       |
| `ptrace.retval`                                                   | Return value of the syscall                                                                                                          |
| `ptrace.tracee.ancestors.args`                                    | Arguments of the process (as a string, excluding argv0)                                                                              |
| `ptrace.tracee.ancestors.args_flags`                              | Flags in the process arguments                                                                                                       |
| `ptrace.tracee.ancestors.args_options`                            | Argument of the process as options                                                                                                   |
| `ptrace.tracee.ancestors.args_truncated`                          | Indicator of arguments truncation                                                                                                    |
| `ptrace.tracee.ancestors.argv`                                    | Arguments of the process (as an array, excluding argv0)                                                                              |
| `ptrace.tracee.ancestors.argv0`                                   | First argument of the process                                                                                                        |
| `ptrace.tracee.ancestors.auid`                                    | Login UID of the process                                                                                                             |
| `ptrace.tracee.ancestors.cap_effective`                           | Effective capability set of the process                                                                                              |
| `ptrace.tracee.ancestors.cap_permitted`                           | Permitted capability set of the process                                                                                              |
| `ptrace.tracee.ancestors.caps_attempted`                          | Bitmask of the capabilities that the process attempted to use                                                                        |
| `ptrace.tracee.ancestors.caps_used`                               | Bitmask of the capabilities that the process successfully used                                                                       |
| `ptrace.tracee.ancestors.cgroup.file.inode`                       | Inode of the file                                                                                                                    |
| `ptrace.tracee.ancestors.cgroup.file.mount_id`                    | Mount ID of the file                                                                                                                 |
| `ptrace.tracee.ancestors.cgroup.id`                               | ID of the cgroup                                                                                                                     |
| `ptrace.tracee.ancestors.cgroup.version`                          | [Experimental] Version of the cgroup API                                                                                             |
| `ptrace.tracee.ancestors.comm`                                    | Comm attribute of the process                                                                                                        |
| `ptrace.tracee.ancestors.container.created_at`                    | Timestamp of the creation of the container                                                                                           |
| `ptrace.tracee.ancestors.container.id`                            | ID of the container                                                                                                                  |
| `ptrace.tracee.ancestors.container.tags`                          | Tags of the container                                                                                                                |
| `ptrace.tracee.ancestors.created_at`                              | Timestamp of the creation of the process                                                                                             |
| `ptrace.tracee.ancestors.egid`                                    | Effective GID of the process                                                                                                         |
| `ptrace.tracee.ancestors.egroup`                                  | Effective group of the process                                                                                                       |
| `ptrace.tracee.ancestors.envp`                                    | Environment variables of the process                                                                                                 |
| `ptrace.tracee.ancestors.envs`                                    | Environment variable names of the process                                                                                            |
| `ptrace.tracee.ancestors.envs_truncated`                          | Indicator of environment variables truncation                                                                                        |
| `ptrace.tracee.ancestors.euid`                                    | Effective UID of the process                                                                                                         |
| `ptrace.tracee.ancestors.euser`                                   | Effective user of the process                                                                                                        |
| `ptrace.tracee.ancestors.file.change_time`                        | Change time (ctime) of the file                                                                                                      |
| `ptrace.tracee.ancestors.file.extension`                          | File's extension                                                                                                                     |
| `ptrace.tracee.ancestors.file.filesystem`                         | File's filesystem                                                                                                                    |
| `ptrace.tracee.ancestors.file.gid`                                | GID of the file's owner                                                                                                              |
| `ptrace.tracee.ancestors.file.group`                              | Group of the file's owner                                                                                                            |
| `ptrace.tracee.ancestors.file.hashes`                             | [Experimental] List of cryptographic hashes computed for this file                                                                   |
| `ptrace.tracee.ancestors.file.in_upper_layer`                     | Indicator of the file layer, for example, in an OverlayFS                                                                            |
| `ptrace.tracee.ancestors.file.inode`                              | Inode of the file                                                                                                                    |
| `ptrace.tracee.ancestors.file.mode`                               | Mode of the file                                                                                                                     |
| `ptrace.tracee.ancestors.file.modification_time`                  | Modification time (mtime) of the file                                                                                                |
| `ptrace.tracee.ancestors.file.mount_detached`                     | Indicates whether the file's mount is detached from the VFS                                                                          |
| `ptrace.tracee.ancestors.file.mount_id`                           | Mount ID of the file                                                                                                                 |
| `ptrace.tracee.ancestors.file.mount_visible`                      | Indicates whether the file's mount is visible in the VFS                                                                             |
| `ptrace.tracee.ancestors.file.name`                               | File's basename                                                                                                                      |
| `ptrace.tracee.ancestors.file.name.length`                        | Length of the corresponding element                                                                                                  |
| `ptrace.tracee.ancestors.file.package.epoch`                      | [Experimental] Epoch of the package that provided this file                                                                          |
| `ptrace.tracee.ancestors.file.package.name`                       | [Experimental] Name of the package that provided this file                                                                           |
| `ptrace.tracee.ancestors.file.package.release`                    | [Experimental] Release of the package that provided this file                                                                        |
| `ptrace.tracee.ancestors.file.package.source_epoch`               | [Experimental] Epoch of the source package of the package that provided this file                                                    |
| `ptrace.tracee.ancestors.file.package.source_release`             | [Experimental] Release of the source package of the package that provided this file                                                  |
| `ptrace.tracee.ancestors.file.package.source_version`             | [Experimental] Full version of the source package of the package that provided this file                                             |
| `ptrace.tracee.ancestors.file.package.version`                    | [Experimental] Full version of the package that provided this file                                                                   |
| `ptrace.tracee.ancestors.file.path`                               | File's path                                                                                                                          |
| `ptrace.tracee.ancestors.file.path.length`                        | Length of the corresponding element                                                                                                  |
| `ptrace.tracee.ancestors.file.rights`                             | Rights of the file                                                                                                                   |
| `ptrace.tracee.ancestors.file.uid`                                | UID of the file's owner                                                                                                              |
| `ptrace.tracee.ancestors.file.user`                               | User of the file's owner                                                                                                             |
| `ptrace.tracee.ancestors.fsgid`                                   | FileSystem-gid of the process                                                                                                        |
| `ptrace.tracee.ancestors.fsgroup`                                 | FileSystem-group of the process                                                                                                      |
| `ptrace.tracee.ancestors.fsuid`                                   | FileSystem-uid of the process                                                                                                        |
| `ptrace.tracee.ancestors.fsuser`                                  | FileSystem-user of the process                                                                                                       |
| `ptrace.tracee.ancestors.gid`                                     | GID of the process                                                                                                                   |
| `ptrace.tracee.ancestors.group`                                   | Group of the process                                                                                                                 |
| `ptrace.tracee.ancestors.interpreter.file.change_time`            | Change time (ctime) of the file                                                                                                      |
| `ptrace.tracee.ancestors.interpreter.file.extension`              | File's extension                                                                                                                     |
| `ptrace.tracee.ancestors.interpreter.file.filesystem`             | File's filesystem                                                                                                                    |
| `ptrace.tracee.ancestors.interpreter.file.gid`                    | GID of the file's owner                                                                                                              |
| `ptrace.tracee.ancestors.interpreter.file.group`                  | Group of the file's owner                                                                                                            |
| `ptrace.tracee.ancestors.interpreter.file.hashes`                 | [Experimental] List of cryptographic hashes computed for this file                                                                   |
| `ptrace.tracee.ancestors.interpreter.file.in_upper_layer`         | Indicator of the file layer, for example, in an OverlayFS                                                                            |
| `ptrace.tracee.ancestors.interpreter.file.inode`                  | Inode of the file                                                                                                                    |
| `ptrace.tracee.ancestors.interpreter.file.mode`                   | Mode of the file                                                                                                                     |
| `ptrace.tracee.ancestors.interpreter.file.modification_time`      | Modification time (mtime) of the file                                                                                                |
| `ptrace.tracee.ancestors.interpreter.file.mount_detached`         | Indicates whether the file's mount is detached from the VFS                                                                          |
| `ptrace.tracee.ancestors.interpreter.file.mount_id`               | Mount ID of the file                                                                                                                 |
| `ptrace.tracee.ancestors.interpreter.file.mount_visible`          | Indicates whether the file's mount is visible in the VFS                                                                             |
| `ptrace.tracee.ancestors.interpreter.file.name`                   | File's basename                                                                                                                      |
| `ptrace.tracee.ancestors.interpreter.file.name.length`            | Length of the corresponding element                                                                                                  |
| `ptrace.tracee.ancestors.interpreter.file.package.epoch`          | [Experimental] Epoch of the package that provided this file                                                                          |
| `ptrace.tracee.ancestors.interpreter.file.package.name`           | [Experimental] Name of the package that provided this file                                                                           |
| `ptrace.tracee.ancestors.interpreter.file.package.release`        | [Experimental] Release of the package that provided this file                                                                        |
| `ptrace.tracee.ancestors.interpreter.file.package.source_epoch`   | [Experimental] Epoch of the source package of the package that provided this file                                                    |
| `ptrace.tracee.ancestors.interpreter.file.package.source_release` | [Experimental] Release of the source package of the package that provided this file                                                  |
| `ptrace.tracee.ancestors.interpreter.file.package.source_version` | [Experimental] Full version of the source package of the package that provided this file                                             |
| `ptrace.tracee.ancestors.interpreter.file.package.version`        | [Experimental] Full version of the package that provided this file                                                                   |
| `ptrace.tracee.ancestors.interpreter.file.path`                   | File's path                                                                                                                          |
| `ptrace.tracee.ancestors.interpreter.file.path.length`            | Length of the corresponding element                                                                                                  |
| `ptrace.tracee.ancestors.interpreter.file.rights`                 | Rights of the file                                                                                                                   |
| `ptrace.tracee.ancestors.interpreter.file.uid`                    | UID of the file's owner                                                                                                              |
| `ptrace.tracee.ancestors.interpreter.file.user`                   | User of the file's owner                                                                                                             |
| `ptrace.tracee.ancestors.is_exec`                                 | Indicates whether the process entry is from a new binary execution                                                                   |
| `ptrace.tracee.ancestors.is_kworker`                              | Indicates whether the process is a kworker                                                                                           |
| `ptrace.tracee.ancestors.is_thread`                               | Indicates whether the process is considered a thread (that is, a child process that hasn't executed another program)                 |
| `ptrace.tracee.ancestors.length`                                  | Length of the corresponding element                                                                                                  |
| `ptrace.tracee.ancestors.pid`                                     | Process ID of the process (also called thread group ID)                                                                              |
| `ptrace.tracee.ancestors.ppid`                                    | Parent process ID                                                                                                                    |
| `ptrace.tracee.ancestors.tid`                                     | Thread ID of the thread                                                                                                              |
| `ptrace.tracee.ancestors.tty_name`                                | Name of the TTY associated with the process                                                                                          |
| `ptrace.tracee.ancestors.uid`                                     | UID of the process                                                                                                                   |
| `ptrace.tracee.ancestors.user`                                    | User of the process                                                                                                                  |
| `ptrace.tracee.ancestors.user_session.id`                         | Unique identifier of the user session, alias for either ssh_session_id or k8s_session_id, depending on the session type              |
| `ptrace.tracee.ancestors.user_session.identity`                   | User identity of the user session, alias for either ssh_client_ip and ssh_client_port or k8s_username, depending on the session type |
| `ptrace.tracee.ancestors.user_session.k8s_groups`                 | Kubernetes groups of the user that executed the process                                                                              |
| `ptrace.tracee.ancestors.user_session.k8s_session_id`             | Unique identifier of the kubernetes session                                                                                          |
| `ptrace.tracee.ancestors.user_session.k8s_uid`                    | Kubernetes UID of the user that executed the process                                                                                 |
| `ptrace.tracee.ancestors.user_session.k8s_username`               | Kubernetes username of the user that executed the process                                                                            |
| `ptrace.tracee.ancestors.user_session.session_type`               | Type of the user session                                                                                                             |
| `ptrace.tracee.ancestors.user_session.ssh_auth_method`            | SSH authentication method used by the user                                                                                           |
| `ptrace.tracee.ancestors.user_session.ssh_client_ip`              | SSH client IP of the user that executed the process                                                                                  |
| `ptrace.tracee.ancestors.user_session.ssh_client_port`            | SSH client port of the user that executed the process                                                                                |
| `ptrace.tracee.ancestors.user_session.ssh_public_key`             | SSH public key used for authentication (if applicable)                                                                               |
| `ptrace.tracee.ancestors.user_session.ssh_session_id`             | Unique identifier of the SSH user session on the host                                                                                |
| `ptrace.tracee.args`                                              | Arguments of the process (as a string, excluding argv0)                                                                              |
| `ptrace.tracee.args_flags`                                        | Flags in the process arguments                                                                                                       |
| `ptrace.tracee.args_options`                                      | Argument of the process as options                                                                                                   |
| `ptrace.tracee.args_truncated`                                    | Indicator of arguments truncation                                                                                                    |
| `ptrace.tracee.argv`                                              | Arguments of the process (as an array, excluding argv0)                                                                              |
| `ptrace.tracee.argv0`                                             | First argument of the process                                                                                                        |
| `ptrace.tracee.auid`                                              | Login UID of the process                                                                                                             |
| `ptrace.tracee.cap_effective`                                     | Effective capability set of the process                                                                                              |
| `ptrace.tracee.cap_permitted`                                     | Permitted capability set of the process                                                                                              |
| `ptrace.tracee.caps_attempted`                                    | Bitmask of the capabilities that the process attempted to use                                                                        |
| `ptrace.tracee.caps_used`                                         | Bitmask of the capabilities that the process successfully used                                                                       |
| `ptrace.tracee.cgroup.file.inode`                                 | Inode of the file                                                                                                                    |
| `ptrace.tracee.cgroup.file.mount_id`                              | Mount ID of the file                                                                                                                 |
| `ptrace.tracee.cgroup.id`                                         | ID of the cgroup                                                                                                                     |
| `ptrace.tracee.cgroup.version`                                    | [Experimental] Version of the cgroup API                                                                                             |
| `ptrace.tracee.comm`                                              | Comm attribute of the process                                                                                                        |
| `ptrace.tracee.container.created_at`                              | Timestamp of the creation of the container                                                                                           |
| `ptrace.tracee.container.id`                                      | ID of the container                                                                                                                  |
| `ptrace.tracee.container.tags`                                    | Tags of the container                                                                                                                |
| `ptrace.tracee.created_at`                                        | Timestamp of the creation of the process                                                                                             |
| `ptrace.tracee.egid`                                              | Effective GID of the process                                                                                                         |
| `ptrace.tracee.egroup`                                            | Effective group of the process                                                                                                       |
| `ptrace.tracee.envp`                                              | Environment variables of the process                                                                                                 |
| `ptrace.tracee.envs`                                              | Environment variable names of the process                                                                                            |
| `ptrace.tracee.envs_truncated`                                    | Indicator of environment variables truncation                                                                                        |
| `ptrace.tracee.euid`                                              | Effective UID of the process                                                                                                         |
| `ptrace.tracee.euser`                                             | Effective user of the process                                                                                                        |
| `ptrace.tracee.file.change_time`                                  | Change time (ctime) of the file                                                                                                      |
| `ptrace.tracee.file.extension`                                    | File's extension                                                                                                                     |
| `ptrace.tracee.file.filesystem`                                   | File's filesystem                                                                                                                    |
| `ptrace.tracee.file.gid`                                          | GID of the file's owner                                                                                                              |
| `ptrace.tracee.file.group`                                        | Group of the file's owner                                                                                                            |
| `ptrace.tracee.file.hashes`                                       | [Experimental] List of cryptographic hashes computed for this file                                                                   |
| `ptrace.tracee.file.in_upper_layer`                               | Indicator of the file layer, for example, in an OverlayFS                                                                            |
| `ptrace.tracee.file.inode`                                        | Inode of the file                                                                                                                    |
| `ptrace.tracee.file.mode`                                         | Mode of the file                                                                                                                     |
| `ptrace.tracee.file.modification_time`                            | Modification time (mtime) of the file                                                                                                |
| `ptrace.tracee.file.mount_detached`                               | Indicates whether the file's mount is detached from the VFS                                                                          |
| `ptrace.tracee.file.mount_id`                                     | Mount ID of the file                                                                                                                 |
| `ptrace.tracee.file.mount_visible`                                | Indicates whether the file's mount is visible in the VFS                                                                             |
| `ptrace.tracee.file.name`                                         | File's basename                                                                                                                      |
| `ptrace.tracee.file.name.length`                                  | Length of the corresponding element                                                                                                  |
| `ptrace.tracee.file.package.epoch`                                | [Experimental] Epoch of the package that provided this file                                                                          |
| `ptrace.tracee.file.package.name`                                 | [Experimental] Name of the package that provided this file                                                                           |
| `ptrace.tracee.file.package.release`                              | [Experimental] Release of the package that provided this file                                                                        |
| `ptrace.tracee.file.package.source_epoch`                         | [Experimental] Epoch of the source package of the package that provided this file                                                    |
| `ptrace.tracee.file.package.source_release`                       | [Experimental] Release of the source package of the package that provided this file                                                  |
| `ptrace.tracee.file.package.source_version`                       | [Experimental] Full version of the source package of the package that provided this file                                             |
| `ptrace.tracee.file.package.version`                              | [Experimental] Full version of the package that provided this file                                                                   |
| `ptrace.tracee.file.path`                                         | File's path                                                                                                                          |
| `ptrace.tracee.file.path.length`                                  | Length of the corresponding element                                                                                                  |
| `ptrace.tracee.file.rights`                                       | Rights of the file                                                                                                                   |
| `ptrace.tracee.file.uid`                                          | UID of the file's owner                                                                                                              |
| `ptrace.tracee.file.user`                                         | User of the file's owner                                                                                                             |
| `ptrace.tracee.fsgid`                                             | FileSystem-gid of the process                                                                                                        |
| `ptrace.tracee.fsgroup`                                           | FileSystem-group of the process                                                                                                      |
| `ptrace.tracee.fsuid`                                             | FileSystem-uid of the process                                                                                                        |
| `ptrace.tracee.fsuser`                                            | FileSystem-user of the process                                                                                                       |
| `ptrace.tracee.gid`                                               | GID of the process                                                                                                                   |
| `ptrace.tracee.group`                                             | Group of the process                                                                                                                 |
| `ptrace.tracee.interpreter.file.change_time`                      | Change time (ctime) of the file                                                                                                      |
| `ptrace.tracee.interpreter.file.extension`                        | File's extension                                                                                                                     |
| `ptrace.tracee.interpreter.file.filesystem`                       | File's filesystem                                                                                                                    |
| `ptrace.tracee.interpreter.file.gid`                              | GID of the file's owner                                                                                                              |
| `ptrace.tracee.interpreter.file.group`                            | Group of the file's owner                                                                                                            |
| `ptrace.tracee.interpreter.file.hashes`                           | [Experimental] List of cryptographic hashes computed for this file                                                                   |
| `ptrace.tracee.interpreter.file.in_upper_layer`                   | Indicator of the file layer, for example, in an OverlayFS                                                                            |
| `ptrace.tracee.interpreter.file.inode`                            | Inode of the file                                                                                                                    |
| `ptrace.tracee.interpreter.file.mode`                             | Mode of the file                                                                                                                     |
| `ptrace.tracee.interpreter.file.modification_time`                | Modification time (mtime) of the file                                                                                                |
| `ptrace.tracee.interpreter.file.mount_detached`                   | Indicates whether the file's mount is detached from the VFS                                                                          |
| `ptrace.tracee.interpreter.file.mount_id`                         | Mount ID of the file                                                                                                                 |
| `ptrace.tracee.interpreter.file.mount_visible`                    | Indicates whether the file's mount is visible in the VFS                                                                             |
| `ptrace.tracee.interpreter.file.name`                             | File's basename                                                                                                                      |
| `ptrace.tracee.interpreter.file.name.length`                      | Length of the corresponding element                                                                                                  |
| `ptrace.tracee.interpreter.file.package.epoch`                    | [Experimental] Epoch of the package that provided this file                                                                          |
| `ptrace.tracee.interpreter.file.package.name`                     | [Experimental] Name of the package that provided this file                                                                           |
| `ptrace.tracee.interpreter.file.package.release`                  | [Experimental] Release of the package that provided this file                                                                        |
| `ptrace.tracee.interpreter.file.package.source_epoch`             | [Experimental] Epoch of the source package of the package that provided this file                                                    |
| `ptrace.tracee.interpreter.file.package.source_release`           | [Experimental] Release of the source package of the package that provided this file                                                  |
| `ptrace.tracee.interpreter.file.package.source_version`           | [Experimental] Full version of the source package of the package that provided this file                                             |
| `ptrace.tracee.interpreter.file.package.version`                  | [Experimental] Full version of the package that provided this file                                                                   |
| `ptrace.tracee.interpreter.file.path`                             | File's path                                                                                                                          |
| `ptrace.tracee.interpreter.file.path.length`                      | Length of the corresponding element                                                                                                  |
| `ptrace.tracee.interpreter.file.rights`                           | Rights of the file                                                                                                                   |
| `ptrace.tracee.interpreter.file.uid`                              | UID of the file's owner                                                                                                              |
| `ptrace.tracee.interpreter.file.user`                             | User of the file's owner                                                                                                             |
| `ptrace.tracee.is_exec`                                           | Indicates whether the process entry is from a new binary execution                                                                   |
| `ptrace.tracee.is_kworker`                                        | Indicates whether the process is a kworker                                                                                           |
| `ptrace.tracee.is_thread`                                         | Indicates whether the process is considered a thread (that is, a child process that hasn't executed another program)                 |
| `ptrace.tracee.parent.args`                                       | Arguments of the process (as a string, excluding argv0)                                                                              |
| `ptrace.tracee.parent.args_flags`                                 | Flags in the process arguments                                                                                                       |
| `ptrace.tracee.parent.args_options`                               | Argument of the process as options                                                                                                   |
| `ptrace.tracee.parent.args_truncated`                             | Indicator of arguments truncation                                                                                                    |
| `ptrace.tracee.parent.argv`                                       | Arguments of the process (as an array, excluding argv0)                                                                              |
| `ptrace.tracee.parent.argv0`                                      | First argument of the process                                                                                                        |
| `ptrace.tracee.parent.auid`                                       | Login UID of the process                                                                                                             |
| `ptrace.tracee.parent.cap_effective`                              | Effective capability set of the process                                                                                              |
| `ptrace.tracee.parent.cap_permitted`                              | Permitted capability set of the process                                                                                              |
| `ptrace.tracee.parent.caps_attempted`                             | Bitmask of the capabilities that the process attempted to use                                                                        |
| `ptrace.tracee.parent.caps_used`                                  | Bitmask of the capabilities that the process successfully used                                                                       |
| `ptrace.tracee.parent.cgroup.file.inode`                          | Inode of the file                                                                                                                    |
| `ptrace.tracee.parent.cgroup.file.mount_id`                       | Mount ID of the file                                                                                                                 |
| `ptrace.tracee.parent.cgroup.id`                                  | ID of the cgroup                                                                                                                     |
| `ptrace.tracee.parent.cgroup.version`                             | [Experimental] Version of the cgroup API                                                                                             |
| `ptrace.tracee.parent.comm`                                       | Comm attribute of the process                                                                                                        |
| `ptrace.tracee.parent.container.created_at`                       | Timestamp of the creation of the container                                                                                           |
| `ptrace.tracee.parent.container.id`                               | ID of the container                                                                                                                  |
| `ptrace.tracee.parent.container.tags`                             | Tags of the container                                                                                                                |
| `ptrace.tracee.parent.created_at`                                 | Timestamp of the creation of the process                                                                                             |
| `ptrace.tracee.parent.egid`                                       | Effective GID of the process                                                                                                         |
| `ptrace.tracee.parent.egroup`                                     | Effective group of the process                                                                                                       |
| `ptrace.tracee.parent.envp`                                       | Environment variables of the process                                                                                                 |
| `ptrace.tracee.parent.envs`                                       | Environment variable names of the process                                                                                            |
| `ptrace.tracee.parent.envs_truncated`                             | Indicator of environment variables truncation                                                                                        |
| `ptrace.tracee.parent.euid`                                       | Effective UID of the process                                                                                                         |
| `ptrace.tracee.parent.euser`                                      | Effective user of the process                                                                                                        |
| `ptrace.tracee.parent.file.change_time`                           | Change time (ctime) of the file                                                                                                      |
| `ptrace.tracee.parent.file.extension`                             | File's extension                                                                                                                     |
| `ptrace.tracee.parent.file.filesystem`                            | File's filesystem                                                                                                                    |
| `ptrace.tracee.parent.file.gid`                                   | GID of the file's owner                                                                                                              |
| `ptrace.tracee.parent.file.group`                                 | Group of the file's owner                                                                                                            |
| `ptrace.tracee.parent.file.hashes`                                | [Experimental] List of cryptographic hashes computed for this file                                                                   |
| `ptrace.tracee.parent.file.in_upper_layer`                        | Indicator of the file layer, for example, in an OverlayFS                                                                            |
| `ptrace.tracee.parent.file.inode`                                 | Inode of the file                                                                                                                    |
| `ptrace.tracee.parent.file.mode`                                  | Mode of the file                                                                                                                     |
| `ptrace.tracee.parent.file.modification_time`                     | Modification time (mtime) of the file                                                                                                |
| `ptrace.tracee.parent.file.mount_detached`                        | Indicates whether the file's mount is detached from the VFS                                                                          |
| `ptrace.tracee.parent.file.mount_id`                              | Mount ID of the file                                                                                                                 |
| `ptrace.tracee.parent.file.mount_visible`                         | Indicates whether the file's mount is visible in the VFS                                                                             |
| `ptrace.tracee.parent.file.name`                                  | File's basename                                                                                                                      |
| `ptrace.tracee.parent.file.name.length`                           | Length of the corresponding element                                                                                                  |
| `ptrace.tracee.parent.file.package.epoch`                         | [Experimental] Epoch of the package that provided this file                                                                          |
| `ptrace.tracee.parent.file.package.name`                          | [Experimental] Name of the package that provided this file                                                                           |
| `ptrace.tracee.parent.file.package.release`                       | [Experimental] Release of the package that provided this file                                                                        |
| `ptrace.tracee.parent.file.package.source_epoch`                  | [Experimental] Epoch of the source package of the package that provided this file                                                    |
| `ptrace.tracee.parent.file.package.source_release`                | [Experimental] Release of the source package of the package that provided this file                                                  |
| `ptrace.tracee.parent.file.package.source_version`                | [Experimental] Full version of the source package of the package that provided this file                                             |
| `ptrace.tracee.parent.file.package.version`                       | [Experimental] Full version of the package that provided this file                                                                   |
| `ptrace.tracee.parent.file.path`                                  | File's path                                                                                                                          |
| `ptrace.tracee.parent.file.path.length`                           | Length of the corresponding element                                                                                                  |
| `ptrace.tracee.parent.file.rights`                                | Rights of the file                                                                                                                   |
| `ptrace.tracee.parent.file.uid`                                   | UID of the file's owner                                                                                                              |
| `ptrace.tracee.parent.file.user`                                  | User of the file's owner                                                                                                             |
| `ptrace.tracee.parent.fsgid`                                      | FileSystem-gid of the process                                                                                                        |
| `ptrace.tracee.parent.fsgroup`                                    | FileSystem-group of the process                                                                                                      |
| `ptrace.tracee.parent.fsuid`                                      | FileSystem-uid of the process                                                                                                        |
| `ptrace.tracee.parent.fsuser`                                     | FileSystem-user of the process                                                                                                       |
| `ptrace.tracee.parent.gid`                                        | GID of the process                                                                                                                   |
| `ptrace.tracee.parent.group`                                      | Group of the process                                                                                                                 |
| `ptrace.tracee.parent.interpreter.file.change_time`               | Change time (ctime) of the file                                                                                                      |
| `ptrace.tracee.parent.interpreter.file.extension`                 | File's extension                                                                                                                     |
| `ptrace.tracee.parent.interpreter.file.filesystem`                | File's filesystem                                                                                                                    |
| `ptrace.tracee.parent.interpreter.file.gid`                       | GID of the file's owner                                                                                                              |
| `ptrace.tracee.parent.interpreter.file.group`                     | Group of the file's owner                                                                                                            |
| `ptrace.tracee.parent.interpreter.file.hashes`                    | [Experimental] List of cryptographic hashes computed for this file                                                                   |
| `ptrace.tracee.parent.interpreter.file.in_upper_layer`            | Indicator of the file layer, for example, in an OverlayFS                                                                            |
| `ptrace.tracee.parent.interpreter.file.inode`                     | Inode of the file                                                                                                                    |
| `ptrace.tracee.parent.interpreter.file.mode`                      | Mode of the file                                                                                                                     |
| `ptrace.tracee.parent.interpreter.file.modification_time`         | Modification time (mtime) of the file                                                                                                |
| `ptrace.tracee.parent.interpreter.file.mount_detached`            | Indicates whether the file's mount is detached from the VFS                                                                          |
| `ptrace.tracee.parent.interpreter.file.mount_id`                  | Mount ID of the file                                                                                                                 |
| `ptrace.tracee.parent.interpreter.file.mount_visible`             | Indicates whether the file's mount is visible in the VFS                                                                             |
| `ptrace.tracee.parent.interpreter.file.name`                      | File's basename                                                                                                                      |
| `ptrace.tracee.parent.interpreter.file.name.length`               | Length of the corresponding element                                                                                                  |
| `ptrace.tracee.parent.interpreter.file.package.epoch`             | [Experimental] Epoch of the package that provided this file                                                                          |
| `ptrace.tracee.parent.interpreter.file.package.name`              | [Experimental] Name of the package that provided this file                                                                           |
| `ptrace.tracee.parent.interpreter.file.package.release`           | [Experimental] Release of the package that provided this file                                                                        |
| `ptrace.tracee.parent.interpreter.file.package.source_epoch`      | [Experimental] Epoch of the source package of the package that provided this file                                                    |
| `ptrace.tracee.parent.interpreter.file.package.source_release`    | [Experimental] Release of the source package of the package that provided this file                                                  |
| `ptrace.tracee.parent.interpreter.file.package.source_version`    | [Experimental] Full version of the source package of the package that provided this file                                             |
| `ptrace.tracee.parent.interpreter.file.package.version`           | [Experimental] Full version of the package that provided this file                                                                   |
| `ptrace.tracee.parent.interpreter.file.path`                      | File's path                                                                                                                          |
| `ptrace.tracee.parent.interpreter.file.path.length`               | Length of the corresponding element                                                                                                  |
| `ptrace.tracee.parent.interpreter.file.rights`                    | Rights of the file                                                                                                                   |
| `ptrace.tracee.parent.interpreter.file.uid`                       | UID of the file's owner                                                                                                              |
| `ptrace.tracee.parent.interpreter.file.user`                      | User of the file's owner                                                                                                             |
| `ptrace.tracee.parent.is_exec`                                    | Indicates whether the process entry is from a new binary execution                                                                   |
| `ptrace.tracee.parent.is_kworker`                                 | Indicates whether the process is a kworker                                                                                           |
| `ptrace.tracee.parent.is_thread`                                  | Indicates whether the process is considered a thread (that is, a child process that hasn't executed another program)                 |
| `ptrace.tracee.parent.pid`                                        | Process ID of the process (also called thread group ID)                                                                              |
| `ptrace.tracee.parent.ppid`                                       | Parent process ID                                                                                                                    |
| `ptrace.tracee.parent.tid`                                        | Thread ID of the thread                                                                                                              |
| `ptrace.tracee.parent.tty_name`                                   | Name of the TTY associated with the process                                                                                          |
| `ptrace.tracee.parent.uid`                                        | UID of the process                                                                                                                   |
| `ptrace.tracee.parent.user`                                       | User of the process                                                                                                                  |
| `ptrace.tracee.parent.user_session.id`                            | Unique identifier of the user session, alias for either ssh_session_id or k8s_session_id, depending on the session type              |
| `ptrace.tracee.parent.user_session.identity`                      | User identity of the user session, alias for either ssh_client_ip and ssh_client_port or k8s_username, depending on the session type |
| `ptrace.tracee.parent.user_session.k8s_groups`                    | Kubernetes groups of the user that executed the process                                                                              |
| `ptrace.tracee.parent.user_session.k8s_session_id`                | Unique identifier of the kubernetes session                                                                                          |
| `ptrace.tracee.parent.user_session.k8s_uid`                       | Kubernetes UID of the user that executed the process                                                                                 |
| `ptrace.tracee.parent.user_session.k8s_username`                  | Kubernetes username of the user that executed the process                                                                            |
| `ptrace.tracee.parent.user_session.session_type`                  | Type of the user session                                                                                                             |
| `ptrace.tracee.parent.user_session.ssh_auth_method`               | SSH authentication method used by the user                                                                                           |
| `ptrace.tracee.parent.user_session.ssh_client_ip`                 | SSH client IP of the user that executed the process                                                                                  |
| `ptrace.tracee.parent.user_session.ssh_client_port`               | SSH client port of the user that executed the process                                                                                |
| `ptrace.tracee.parent.user_session.ssh_public_key`                | SSH public key used for authentication (if applicable)                                                                               |
| `ptrace.tracee.parent.user_session.ssh_session_id`                | Unique identifier of the SSH user session on the host                                                                                |
| `ptrace.tracee.pid`                                               | Process ID of the process (also called thread group ID)                                                                              |
| `ptrace.tracee.ppid`                                              | Parent process ID                                                                                                                    |
| `ptrace.tracee.tid`                                               | Thread ID of the thread                                                                                                              |
| `ptrace.tracee.tty_name`                                          | Name of the TTY associated with the process                                                                                          |
| `ptrace.tracee.uid`                                               | UID of the process                                                                                                                   |
| `ptrace.tracee.user`                                              | User of the process                                                                                                                  |
| `ptrace.tracee.user_session.id`                                   | Unique identifier of the user session, alias for either ssh_session_id or k8s_session_id, depending on the session type              |
| `ptrace.tracee.user_session.identity`                             | User identity of the user session, alias for either ssh_client_ip and ssh_client_port or k8s_username, depending on the session type |
| `ptrace.tracee.user_session.k8s_groups`                           | Kubernetes groups of the user that executed the process                                                                              |
| `ptrace.tracee.user_session.k8s_session_id`                       | Unique identifier of the kubernetes session                                                                                          |
| `ptrace.tracee.user_session.k8s_uid`                              | Kubernetes UID of the user that executed the process                                                                                 |
| `ptrace.tracee.user_session.k8s_username`                         | Kubernetes username of the user that executed the process                                                                            |
| `ptrace.tracee.user_session.session_type`                         | Type of the user session                                                                                                             |
| `ptrace.tracee.user_session.ssh_auth_method`                      | SSH authentication method used by the user                                                                                           |
| `ptrace.tracee.user_session.ssh_client_ip`                        | SSH client IP of the user that executed the process                                                                                  |
| `ptrace.tracee.user_session.ssh_client_port`                      | SSH client port of the user that executed the process                                                                                |
| `ptrace.tracee.user_session.ssh_public_key`                       | SSH public key used for authentication (if applicable)                                                                               |
| `ptrace.tracee.user_session.ssh_session_id`                       | Unique identifier of the SSH user session on the host                                                                                |

### Event `removexattr`{% #event-removexattr %}

Remove extended attributes

| Property                                  | Definition                                                                               |
| ----------------------------------------- | ---------------------------------------------------------------------------------------- |
| `removexattr.file.change_time`            | Change time (ctime) of the file                                                          |
| `removexattr.file.destination.name`       | Name of the extended attribute                                                           |
| `removexattr.file.destination.namespace`  | Namespace of the extended attribute                                                      |
| `removexattr.file.extension`              | File's extension                                                                         |
| `removexattr.file.filesystem`             | File's filesystem                                                                        |
| `removexattr.file.gid`                    | GID of the file's owner                                                                  |
| `removexattr.file.group`                  | Group of the file's owner                                                                |
| `removexattr.file.hashes`                 | [Experimental] List of cryptographic hashes computed for this file                       |
| `removexattr.file.in_upper_layer`         | Indicator of the file layer, for example, in an OverlayFS                                |
| `removexattr.file.inode`                  | Inode of the file                                                                        |
| `removexattr.file.mode`                   | Mode of the file                                                                         |
| `removexattr.file.modification_time`      | Modification time (mtime) of the file                                                    |
| `removexattr.file.mount_detached`         | Indicates whether the file's mount is detached from the VFS                              |
| `removexattr.file.mount_id`               | Mount ID of the file                                                                     |
| `removexattr.file.mount_visible`          | Indicates whether the file's mount is visible in the VFS                                 |
| `removexattr.file.name`                   | File's basename                                                                          |
| `removexattr.file.name.length`            | Length of the corresponding element                                                      |
| `removexattr.file.package.epoch`          | [Experimental] Epoch of the package that provided this file                              |
| `removexattr.file.package.name`           | [Experimental] Name of the package that provided this file                               |
| `removexattr.file.package.release`        | [Experimental] Release of the package that provided this file                            |
| `removexattr.file.package.source_epoch`   | [Experimental] Epoch of the source package of the package that provided this file        |
| `removexattr.file.package.source_release` | [Experimental] Release of the source package of the package that provided this file      |
| `removexattr.file.package.source_version` | [Experimental] Full version of the source package of the package that provided this file |
| `removexattr.file.package.version`        | [Experimental] Full version of the package that provided this file                       |
| `removexattr.file.path`                   | File's path                                                                              |
| `removexattr.file.path.length`            | Length of the corresponding element                                                      |
| `removexattr.file.rights`                 | Rights of the file                                                                       |
| `removexattr.file.uid`                    | UID of the file's owner                                                                  |
| `removexattr.file.user`                   | User of the file's owner                                                                 |
| `removexattr.retval`                      | Return value of the syscall                                                              |

### Event `rename`{% #event-rename %}

A file/directory was renamed

| Property                                         | Definition                                                                               |
| ------------------------------------------------ | ---------------------------------------------------------------------------------------- |
| `rename.file.change_time`                        | Change time (ctime) of the file                                                          |
| `rename.file.destination.change_time`            | Change time (ctime) of the file                                                          |
| `rename.file.destination.extension`              | File's extension                                                                         |
| `rename.file.destination.filesystem`             | File's filesystem                                                                        |
| `rename.file.destination.gid`                    | GID of the file's owner                                                                  |
| `rename.file.destination.group`                  | Group of the file's owner                                                                |
| `rename.file.destination.hashes`                 | [Experimental] List of cryptographic hashes computed for this file                       |
| `rename.file.destination.in_upper_layer`         | Indicator of the file layer, for example, in an OverlayFS                                |
| `rename.file.destination.inode`                  | Inode of the file                                                                        |
| `rename.file.destination.mode`                   | Mode of the file                                                                         |
| `rename.file.destination.modification_time`      | Modification time (mtime) of the file                                                    |
| `rename.file.destination.mount_detached`         | Indicates whether the file's mount is detached from the VFS                              |
| `rename.file.destination.mount_id`               | Mount ID of the file                                                                     |
| `rename.file.destination.mount_visible`          | Indicates whether the file's mount is visible in the VFS                                 |
| `rename.file.destination.name`                   | File's basename                                                                          |
| `rename.file.destination.name.length`            | Length of the corresponding element                                                      |
| `rename.file.destination.package.epoch`          | [Experimental] Epoch of the package that provided this file                              |
| `rename.file.destination.package.name`           | [Experimental] Name of the package that provided this file                               |
| `rename.file.destination.package.release`        | [Experimental] Release of the package that provided this file                            |
| `rename.file.destination.package.source_epoch`   | [Experimental] Epoch of the source package of the package that provided this file        |
| `rename.file.destination.package.source_release` | [Experimental] Release of the source package of the package that provided this file      |
| `rename.file.destination.package.source_version` | [Experimental] Full version of the source package of the package that provided this file |
| `rename.file.destination.package.version`        | [Experimental] Full version of the package that provided this file                       |
| `rename.file.destination.path`                   | File's path                                                                              |
| `rename.file.destination.path.length`            | Length of the corresponding element                                                      |
| `rename.file.destination.rights`                 | Rights of the file                                                                       |
| `rename.file.destination.uid`                    | UID of the file's owner                                                                  |
| `rename.file.destination.user`                   | User of the file's owner                                                                 |
| `rename.file.extension`                          | File's extension                                                                         |
| `rename.file.filesystem`                         | File's filesystem                                                                        |
| `rename.file.gid`                                | GID of the file's owner                                                                  |
| `rename.file.group`                              | Group of the file's owner                                                                |
| `rename.file.hashes`                             | [Experimental] List of cryptographic hashes computed for this file                       |
| `rename.file.in_upper_layer`                     | Indicator of the file layer, for example, in an OverlayFS                                |
| `rename.file.inode`                              | Inode of the file                                                                        |
| `rename.file.mode`                               | Mode of the file                                                                         |
| `rename.file.modification_time`                  | Modification time (mtime) of the file                                                    |
| `rename.file.mount_detached`                     | Indicates whether the file's mount is detached from the VFS                              |
| `rename.file.mount_id`                           | Mount ID of the file                                                                     |
| `rename.file.mount_visible`                      | Indicates whether the file's mount is visible in the VFS                                 |
| `rename.file.name`                               | File's basename                                                                          |
| `rename.file.name.length`                        | Length of the corresponding element                                                      |
| `rename.file.package.epoch`                      | [Experimental] Epoch of the package that provided this file                              |
| `rename.file.package.name`                       | [Experimental] Name of the package that provided this file                               |
| `rename.file.package.release`                    | [Experimental] Release of the package that provided this file                            |
| `rename.file.package.source_epoch`               | [Experimental] Epoch of the source package of the package that provided this file        |
| `rename.file.package.source_release`             | [Experimental] Release of the source package of the package that provided this file      |
| `rename.file.package.source_version`             | [Experimental] Full version of the source package of the package that provided this file |
| `rename.file.package.version`                    | [Experimental] Full version of the package that provided this file                       |
| `rename.file.path`                               | File's path                                                                              |
| `rename.file.path.length`                        | Length of the corresponding element                                                      |
| `rename.file.rights`                             | Rights of the file                                                                       |
| `rename.file.uid`                                | UID of the file's owner                                                                  |
| `rename.file.user`                               | User of the file's owner                                                                 |
| `rename.retval`                                  | Return value of the syscall                                                              |
| `rename.syscall.destination.path`                | Destination path argument of the syscall                                                 |
| `rename.syscall.path`                            | Path argument of the syscall                                                             |

### Event `rmdir`{% #event-rmdir %}

A directory was removed

| Property                            | Definition                                                                               |
| ----------------------------------- | ---------------------------------------------------------------------------------------- |
| `rmdir.file.change_time`            | Change time (ctime) of the file                                                          |
| `rmdir.file.extension`              | File's extension                                                                         |
| `rmdir.file.filesystem`             | File's filesystem                                                                        |
| `rmdir.file.gid`                    | GID of the file's owner                                                                  |
| `rmdir.file.group`                  | Group of the file's owner                                                                |
| `rmdir.file.hashes`                 | [Experimental] List of cryptographic hashes computed for this file                       |
| `rmdir.file.in_upper_layer`         | Indicator of the file layer, for example, in an OverlayFS                                |
| `rmdir.file.inode`                  | Inode of the file                                                                        |
| `rmdir.file.mode`                   | Mode of the file                                                                         |
| `rmdir.file.modification_time`      | Modification time (mtime) of the file                                                    |
| `rmdir.file.mount_detached`         | Indicates whether the file's mount is detached from the VFS                              |
| `rmdir.file.mount_id`               | Mount ID of the file                                                                     |
| `rmdir.file.mount_visible`          | Indicates whether the file's mount is visible in the VFS                                 |
| `rmdir.file.name`                   | File's basename                                                                          |
| `rmdir.file.name.length`            | Length of the corresponding element                                                      |
| `rmdir.file.package.epoch`          | [Experimental] Epoch of the package that provided this file                              |
| `rmdir.file.package.name`           | [Experimental] Name of the package that provided this file                               |
| `rmdir.file.package.release`        | [Experimental] Release of the package that provided this file                            |
| `rmdir.file.package.source_epoch`   | [Experimental] Epoch of the source package of the package that provided this file        |
| `rmdir.file.package.source_release` | [Experimental] Release of the source package of the package that provided this file      |
| `rmdir.file.package.source_version` | [Experimental] Full version of the source package of the package that provided this file |
| `rmdir.file.package.version`        | [Experimental] Full version of the package that provided this file                       |
| `rmdir.file.path`                   | File's path                                                                              |
| `rmdir.file.path.length`            | Length of the corresponding element                                                      |
| `rmdir.file.rights`                 | Rights of the file                                                                       |
| `rmdir.file.uid`                    | UID of the file's owner                                                                  |
| `rmdir.file.user`                   | User of the file's owner                                                                 |
| `rmdir.retval`                      | Return value of the syscall                                                              |
| `rmdir.syscall.path`                | Path argument of the syscall                                                             |

### Event `selinux`{% #event-selinux %}

An SELinux operation was run

| Property                    | Definition                                                                |
| --------------------------- | ------------------------------------------------------------------------- |
| `selinux.bool.name`         | SELinux boolean name                                                      |
| `selinux.bool.state`        | SELinux boolean new value                                                 |
| `selinux.bool_commit.state` | Indicator of a SELinux boolean commit operation                           |
| `selinux.enforce.status`    | SELinux enforcement status (one of "enforcing", "permissive", "disabled") |

### Event `setgid`{% #event-setgid %}

A process changed its effective gid

| Property         | Definition                          |
| ---------------- | ----------------------------------- |
| `setgid.egid`    | New effective GID of the process    |
| `setgid.egroup`  | New effective group of the process  |
| `setgid.fsgid`   | New FileSystem GID of the process   |
| `setgid.fsgroup` | New FileSystem group of the process |
| `setgid.gid`     | New GID of the process              |
| `setgid.group`   | New group of the process            |

### Event `setrlimit`{% #event-setrlimit %}

A setrlimit command was executed

| Property                                                             | Definition                                                                                                                           |
| -------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| `setrlimit.resource`                                                 | Resource type being limited                                                                                                          |
| `setrlimit.retval`                                                   | Return value of the syscall                                                                                                          |
| `setrlimit.rlim_cur`                                                 | Current (soft) limit value                                                                                                           |
| `setrlimit.rlim_max`                                                 | Maximum (hard) limit value                                                                                                           |
| `setrlimit.target.ancestors.args`                                    | Arguments of the process (as a string, excluding argv0)                                                                              |
| `setrlimit.target.ancestors.args_flags`                              | Flags in the process arguments                                                                                                       |
| `setrlimit.target.ancestors.args_options`                            | Argument of the process as options                                                                                                   |
| `setrlimit.target.ancestors.args_truncated`                          | Indicator of arguments truncation                                                                                                    |
| `setrlimit.target.ancestors.argv`                                    | Arguments of the process (as an array, excluding argv0)                                                                              |
| `setrlimit.target.ancestors.argv0`                                   | First argument of the process                                                                                                        |
| `setrlimit.target.ancestors.auid`                                    | Login UID of the process                                                                                                             |
| `setrlimit.target.ancestors.cap_effective`                           | Effective capability set of the process                                                                                              |
| `setrlimit.target.ancestors.cap_permitted`                           | Permitted capability set of the process                                                                                              |
| `setrlimit.target.ancestors.caps_attempted`                          | Bitmask of the capabilities that the process attempted to use                                                                        |
| `setrlimit.target.ancestors.caps_used`                               | Bitmask of the capabilities that the process successfully used                                                                       |
| `setrlimit.target.ancestors.cgroup.file.inode`                       | Inode of the file                                                                                                                    |
| `setrlimit.target.ancestors.cgroup.file.mount_id`                    | Mount ID of the file                                                                                                                 |
| `setrlimit.target.ancestors.cgroup.id`                               | ID of the cgroup                                                                                                                     |
| `setrlimit.target.ancestors.cgroup.version`                          | [Experimental] Version of the cgroup API                                                                                             |
| `setrlimit.target.ancestors.comm`                                    | Comm attribute of the process                                                                                                        |
| `setrlimit.target.ancestors.container.created_at`                    | Timestamp of the creation of the container                                                                                           |
| `setrlimit.target.ancestors.container.id`                            | ID of the container                                                                                                                  |
| `setrlimit.target.ancestors.container.tags`                          | Tags of the container                                                                                                                |
| `setrlimit.target.ancestors.created_at`                              | Timestamp of the creation of the process                                                                                             |
| `setrlimit.target.ancestors.egid`                                    | Effective GID of the process                                                                                                         |
| `setrlimit.target.ancestors.egroup`                                  | Effective group of the process                                                                                                       |
| `setrlimit.target.ancestors.envp`                                    | Environment variables of the process                                                                                                 |
| `setrlimit.target.ancestors.envs`                                    | Environment variable names of the process                                                                                            |
| `setrlimit.target.ancestors.envs_truncated`                          | Indicator of environment variables truncation                                                                                        |
| `setrlimit.target.ancestors.euid`                                    | Effective UID of the process                                                                                                         |
| `setrlimit.target.ancestors.euser`                                   | Effective user of the process                                                                                                        |
| `setrlimit.target.ancestors.file.change_time`                        | Change time (ctime) of the file                                                                                                      |
| `setrlimit.target.ancestors.file.extension`                          | File's extension                                                                                                                     |
| `setrlimit.target.ancestors.file.filesystem`                         | File's filesystem                                                                                                                    |
| `setrlimit.target.ancestors.file.gid`                                | GID of the file's owner                                                                                                              |
| `setrlimit.target.ancestors.file.group`                              | Group of the file's owner                                                                                                            |
| `setrlimit.target.ancestors.file.hashes`                             | [Experimental] List of cryptographic hashes computed for this file                                                                   |
| `setrlimit.target.ancestors.file.in_upper_layer`                     | Indicator of the file layer, for example, in an OverlayFS                                                                            |
| `setrlimit.target.ancestors.file.inode`                              | Inode of the file                                                                                                                    |
| `setrlimit.target.ancestors.file.mode`                               | Mode of the file                                                                                                                     |
| `setrlimit.target.ancestors.file.modification_time`                  | Modification time (mtime) of the file                                                                                                |
| `setrlimit.target.ancestors.file.mount_detached`                     | Indicates whether the file's mount is detached from the VFS                                                                          |
| `setrlimit.target.ancestors.file.mount_id`                           | Mount ID of the file                                                                                                                 |
| `setrlimit.target.ancestors.file.mount_visible`                      | Indicates whether the file's mount is visible in the VFS                                                                             |
| `setrlimit.target.ancestors.file.name`                               | File's basename                                                                                                                      |
| `setrlimit.target.ancestors.file.name.length`                        | Length of the corresponding element                                                                                                  |
| `setrlimit.target.ancestors.file.package.epoch`                      | [Experimental] Epoch of the package that provided this file                                                                          |
| `setrlimit.target.ancestors.file.package.name`                       | [Experimental] Name of the package that provided this file                                                                           |
| `setrlimit.target.ancestors.file.package.release`                    | [Experimental] Release of the package that provided this file                                                                        |
| `setrlimit.target.ancestors.file.package.source_epoch`               | [Experimental] Epoch of the source package of the package that provided this file                                                    |
| `setrlimit.target.ancestors.file.package.source_release`             | [Experimental] Release of the source package of the package that provided this file                                                  |
| `setrlimit.target.ancestors.file.package.source_version`             | [Experimental] Full version of the source package of the package that provided this file                                             |
| `setrlimit.target.ancestors.file.package.version`                    | [Experimental] Full version of the package that provided this file                                                                   |
| `setrlimit.target.ancestors.file.path`                               | File's path                                                                                                                          |
| `setrlimit.target.ancestors.file.path.length`                        | Length of the corresponding element                                                                                                  |
| `setrlimit.target.ancestors.file.rights`                             | Rights of the file                                                                                                                   |
| `setrlimit.target.ancestors.file.uid`                                | UID of the file's owner                                                                                                              |
| `setrlimit.target.ancestors.file.user`                               | User of the file's owner                                                                                                             |
| `setrlimit.target.ancestors.fsgid`                                   | FileSystem-gid of the process                                                                                                        |
| `setrlimit.target.ancestors.fsgroup`                                 | FileSystem-group of the process                                                                                                      |
| `setrlimit.target.ancestors.fsuid`                                   | FileSystem-uid of the process                                                                                                        |
| `setrlimit.target.ancestors.fsuser`                                  | FileSystem-user of the process                                                                                                       |
| `setrlimit.target.ancestors.gid`                                     | GID of the process                                                                                                                   |
| `setrlimit.target.ancestors.group`                                   | Group of the process                                                                                                                 |
| `setrlimit.target.ancestors.interpreter.file.change_time`            | Change time (ctime) of the file                                                                                                      |
| `setrlimit.target.ancestors.interpreter.file.extension`              | File's extension                                                                                                                     |
| `setrlimit.target.ancestors.interpreter.file.filesystem`             | File's filesystem                                                                                                                    |
| `setrlimit.target.ancestors.interpreter.file.gid`                    | GID of the file's owner                                                                                                              |
| `setrlimit.target.ancestors.interpreter.file.group`                  | Group of the file's owner                                                                                                            |
| `setrlimit.target.ancestors.interpreter.file.hashes`                 | [Experimental] List of cryptographic hashes computed for this file                                                                   |
| `setrlimit.target.ancestors.interpreter.file.in_upper_layer`         | Indicator of the file layer, for example, in an OverlayFS                                                                            |
| `setrlimit.target.ancestors.interpreter.file.inode`                  | Inode of the file                                                                                                                    |
| `setrlimit.target.ancestors.interpreter.file.mode`                   | Mode of the file                                                                                                                     |
| `setrlimit.target.ancestors.interpreter.file.modification_time`      | Modification time (mtime) of the file                                                                                                |
| `setrlimit.target.ancestors.interpreter.file.mount_detached`         | Indicates whether the file's mount is detached from the VFS                                                                          |
| `setrlimit.target.ancestors.interpreter.file.mount_id`               | Mount ID of the file                                                                                                                 |
| `setrlimit.target.ancestors.interpreter.file.mount_visible`          | Indicates whether the file's mount is visible in the VFS                                                                             |
| `setrlimit.target.ancestors.interpreter.file.name`                   | File's basename                                                                                                                      |
| `setrlimit.target.ancestors.interpreter.file.name.length`            | Length of the corresponding element                                                                                                  |
| `setrlimit.target.ancestors.interpreter.file.package.epoch`          | [Experimental] Epoch of the package that provided this file                                                                          |
| `setrlimit.target.ancestors.interpreter.file.package.name`           | [Experimental] Name of the package that provided this file                                                                           |
| `setrlimit.target.ancestors.interpreter.file.package.release`        | [Experimental] Release of the package that provided this file                                                                        |
| `setrlimit.target.ancestors.interpreter.file.package.source_epoch`   | [Experimental] Epoch of the source package of the package that provided this file                                                    |
| `setrlimit.target.ancestors.interpreter.file.package.source_release` | [Experimental] Release of the source package of the package that provided this file                                                  |
| `setrlimit.target.ancestors.interpreter.file.package.source_version` | [Experimental] Full version of the source package of the package that provided this file                                             |
| `setrlimit.target.ancestors.interpreter.file.package.version`        | [Experimental] Full version of the package that provided this file                                                                   |
| `setrlimit.target.ancestors.interpreter.file.path`                   | File's path                                                                                                                          |
| `setrlimit.target.ancestors.interpreter.file.path.length`            | Length of the corresponding element                                                                                                  |
| `setrlimit.target.ancestors.interpreter.file.rights`                 | Rights of the file                                                                                                                   |
| `setrlimit.target.ancestors.interpreter.file.uid`                    | UID of the file's owner                                                                                                              |
| `setrlimit.target.ancestors.interpreter.file.user`                   | User of the file's owner                                                                                                             |
| `setrlimit.target.ancestors.is_exec`                                 | Indicates whether the process entry is from a new binary execution                                                                   |
| `setrlimit.target.ancestors.is_kworker`                              | Indicates whether the process is a kworker                                                                                           |
| `setrlimit.target.ancestors.is_thread`                               | Indicates whether the process is considered a thread (that is, a child process that hasn't executed another program)                 |
| `setrlimit.target.ancestors.length`                                  | Length of the corresponding element                                                                                                  |
| `setrlimit.target.ancestors.pid`                                     | Process ID of the process (also called thread group ID)                                                                              |
| `setrlimit.target.ancestors.ppid`                                    | Parent process ID                                                                                                                    |
| `setrlimit.target.ancestors.tid`                                     | Thread ID of the thread                                                                                                              |
| `setrlimit.target.ancestors.tty_name`                                | Name of the TTY associated with the process                                                                                          |
| `setrlimit.target.ancestors.uid`                                     | UID of the process                                                                                                                   |
| `setrlimit.target.ancestors.user`                                    | User of the process                                                                                                                  |
| `setrlimit.target.ancestors.user_session.id`                         | Unique identifier of the user session, alias for either ssh_session_id or k8s_session_id, depending on the session type              |
| `setrlimit.target.ancestors.user_session.identity`                   | User identity of the user session, alias for either ssh_client_ip and ssh_client_port or k8s_username, depending on the session type |
| `setrlimit.target.ancestors.user_session.k8s_groups`                 | Kubernetes groups of the user that executed the process                                                                              |
| `setrlimit.target.ancestors.user_session.k8s_session_id`             | Unique identifier of the kubernetes session                                                                                          |
| `setrlimit.target.ancestors.user_session.k8s_uid`                    | Kubernetes UID of the user that executed the process                                                                                 |
| `setrlimit.target.ancestors.user_session.k8s_username`               | Kubernetes username of the user that executed the process                                                                            |
| `setrlimit.target.ancestors.user_session.session_type`               | Type of the user session                                                                                                             |
| `setrlimit.target.ancestors.user_session.ssh_auth_method`            | SSH authentication method used by the user                                                                                           |
| `setrlimit.target.ancestors.user_session.ssh_client_ip`              | SSH client IP of the user that executed the process                                                                                  |
| `setrlimit.target.ancestors.user_session.ssh_client_port`            | SSH client port of the user that executed the process                                                                                |
| `setrlimit.target.ancestors.user_session.ssh_public_key`             | SSH public key used for authentication (if applicable)                                                                               |
| `setrlimit.target.ancestors.user_session.ssh_session_id`             | Unique identifier of the SSH user session on the host                                                                                |
| `setrlimit.target.args`                                              | Arguments of the process (as a string, excluding argv0)                                                                              |
| `setrlimit.target.args_flags`                                        | Flags in the process arguments                                                                                                       |
| `setrlimit.target.args_options`                                      | Argument of the process as options                                                                                                   |
| `setrlimit.target.args_truncated`                                    | Indicator of arguments truncation                                                                                                    |
| `setrlimit.target.argv`                                              | Arguments of the process (as an array, excluding argv0)                                                                              |
| `setrlimit.target.argv0`                                             | First argument of the process                                                                                                        |
| `setrlimit.target.auid`                                              | Login UID of the process                                                                                                             |
| `setrlimit.target.cap_effective`                                     | Effective capability set of the process                                                                                              |
| `setrlimit.target.cap_permitted`                                     | Permitted capability set of the process                                                                                              |
| `setrlimit.target.caps_attempted`                                    | Bitmask of the capabilities that the process attempted to use                                                                        |
| `setrlimit.target.caps_used`                                         | Bitmask of the capabilities that the process successfully used                                                                       |
| `setrlimit.target.cgroup.file.inode`                                 | Inode of the file                                                                                                                    |
| `setrlimit.target.cgroup.file.mount_id`                              | Mount ID of the file                                                                                                                 |
| `setrlimit.target.cgroup.id`                                         | ID of the cgroup                                                                                                                     |
| `setrlimit.target.cgroup.version`                                    | [Experimental] Version of the cgroup API                                                                                             |
| `setrlimit.target.comm`                                              | Comm attribute of the process                                                                                                        |
| `setrlimit.target.container.created_at`                              | Timestamp of the creation of the container                                                                                           |
| `setrlimit.target.container.id`                                      | ID of the container                                                                                                                  |
| `setrlimit.target.container.tags`                                    | Tags of the container                                                                                                                |
| `setrlimit.target.created_at`                                        | Timestamp of the creation of the process                                                                                             |
| `setrlimit.target.egid`                                              | Effective GID of the process                                                                                                         |
| `setrlimit.target.egroup`                                            | Effective group of the process                                                                                                       |
| `setrlimit.target.envp`                                              | Environment variables of the process                                                                                                 |
| `setrlimit.target.envs`                                              | Environment variable names of the process                                                                                            |
| `setrlimit.target.envs_truncated`                                    | Indicator of environment variables truncation                                                                                        |
| `setrlimit.target.euid`                                              | Effective UID of the process                                                                                                         |
| `setrlimit.target.euser`                                             | Effective user of the process                                                                                                        |
| `setrlimit.target.file.change_time`                                  | Change time (ctime) of the file                                                                                                      |
| `setrlimit.target.file.extension`                                    | File's extension                                                                                                                     |
| `setrlimit.target.file.filesystem`                                   | File's filesystem                                                                                                                    |
| `setrlimit.target.file.gid`                                          | GID of the file's owner                                                                                                              |
| `setrlimit.target.file.group`                                        | Group of the file's owner                                                                                                            |
| `setrlimit.target.file.hashes`                                       | [Experimental] List of cryptographic hashes computed for this file                                                                   |
| `setrlimit.target.file.in_upper_layer`                               | Indicator of the file layer, for example, in an OverlayFS                                                                            |
| `setrlimit.target.file.inode`                                        | Inode of the file                                                                                                                    |
| `setrlimit.target.file.mode`                                         | Mode of the file                                                                                                                     |
| `setrlimit.target.file.modification_time`                            | Modification time (mtime) of the file                                                                                                |
| `setrlimit.target.file.mount_detached`                               | Indicates whether the file's mount is detached from the VFS                                                                          |
| `setrlimit.target.file.mount_id`                                     | Mount ID of the file                                                                                                                 |
| `setrlimit.target.file.mount_visible`                                | Indicates whether the file's mount is visible in the VFS                                                                             |
| `setrlimit.target.file.name`                                         | File's basename                                                                                                                      |
| `setrlimit.target.file.name.length`                                  | Length of the corresponding element                                                                                                  |
| `setrlimit.target.file.package.epoch`                                | [Experimental] Epoch of the package that provided this file                                                                          |
| `setrlimit.target.file.package.name`                                 | [Experimental] Name of the package that provided this file                                                                           |
| `setrlimit.target.file.package.release`                              | [Experimental] Release of the package that provided this file                                                                        |
| `setrlimit.target.file.package.source_epoch`                         | [Experimental] Epoch of the source package of the package that provided this file                                                    |
| `setrlimit.target.file.package.source_release`                       | [Experimental] Release of the source package of the package that provided this file                                                  |
| `setrlimit.target.file.package.source_version`                       | [Experimental] Full version of the source package of the package that provided this file                                             |
| `setrlimit.target.file.package.version`                              | [Experimental] Full version of the package that provided this file                                                                   |
| `setrlimit.target.file.path`                                         | File's path                                                                                                                          |
| `setrlimit.target.file.path.length`                                  | Length of the corresponding element                                                                                                  |
| `setrlimit.target.file.rights`                                       | Rights of the file                                                                                                                   |
| `setrlimit.target.file.uid`                                          | UID of the file's owner                                                                                                              |
| `setrlimit.target.file.user`                                         | User of the file's owner                                                                                                             |
| `setrlimit.target.fsgid`                                             | FileSystem-gid of the process                                                                                                        |
| `setrlimit.target.fsgroup`                                           | FileSystem-group of the process                                                                                                      |
| `setrlimit.target.fsuid`                                             | FileSystem-uid of the process                                                                                                        |
| `setrlimit.target.fsuser`                                            | FileSystem-user of the process                                                                                                       |
| `setrlimit.target.gid`                                               | GID of the process                                                                                                                   |
| `setrlimit.target.group`                                             | Group of the process                                                                                                                 |
| `setrlimit.target.interpreter.file.change_time`                      | Change time (ctime) of the file                                                                                                      |
| `setrlimit.target.interpreter.file.extension`                        | File's extension                                                                                                                     |
| `setrlimit.target.interpreter.file.filesystem`                       | File's filesystem                                                                                                                    |
| `setrlimit.target.interpreter.file.gid`                              | GID of the file's owner                                                                                                              |
| `setrlimit.target.interpreter.file.group`                            | Group of the file's owner                                                                                                            |
| `setrlimit.target.interpreter.file.hashes`                           | [Experimental] List of cryptographic hashes computed for this file                                                                   |
| `setrlimit.target.interpreter.file.in_upper_layer`                   | Indicator of the file layer, for example, in an OverlayFS                                                                            |
| `setrlimit.target.interpreter.file.inode`                            | Inode of the file                                                                                                                    |
| `setrlimit.target.interpreter.file.mode`                             | Mode of the file                                                                                                                     |
| `setrlimit.target.interpreter.file.modification_time`                | Modification time (mtime) of the file                                                                                                |
| `setrlimit.target.interpreter.file.mount_detached`                   | Indicates whether the file's mount is detached from the VFS                                                                          |
| `setrlimit.target.interpreter.file.mount_id`                         | Mount ID of the file                                                                                                                 |
| `setrlimit.target.interpreter.file.mount_visible`                    | Indicates whether the file's mount is visible in the VFS                                                                             |
| `setrlimit.target.interpreter.file.name`                             | File's basename                                                                                                                      |
| `setrlimit.target.interpreter.file.name.length`                      | Length of the corresponding element                                                                                                  |
| `setrlimit.target.interpreter.file.package.epoch`                    | [Experimental] Epoch of the package that provided this file                                                                          |
| `setrlimit.target.interpreter.file.package.name`                     | [Experimental] Name of the package that provided this file                                                                           |
| `setrlimit.target.interpreter.file.package.release`                  | [Experimental] Release of the package that provided this file                                                                        |
| `setrlimit.target.interpreter.file.package.source_epoch`             | [Experimental] Epoch of the source package of the package that provided this file                                                    |
| `setrlimit.target.interpreter.file.package.source_release`           | [Experimental] Release of the source package of the package that provided this file                                                  |
| `setrlimit.target.interpreter.file.package.source_version`           | [Experimental] Full version of the source package of the package that provided this file                                             |
| `setrlimit.target.interpreter.file.package.version`                  | [Experimental] Full version of the package that provided this file                                                                   |
| `setrlimit.target.interpreter.file.path`                             | File's path                                                                                                                          |
| `setrlimit.target.interpreter.file.path.length`                      | Length of the corresponding element                                                                                                  |
| `setrlimit.target.interpreter.file.rights`                           | Rights of the file                                                                                                                   |
| `setrlimit.target.interpreter.file.uid`                              | UID of the file's owner                                                                                                              |
| `setrlimit.target.interpreter.file.user`                             | User of the file's owner                                                                                                             |
| `setrlimit.target.is_exec`                                           | Indicates whether the process entry is from a new binary execution                                                                   |
| `setrlimit.target.is_kworker`                                        | Indicates whether the process is a kworker                                                                                           |
| `setrlimit.target.is_thread`                                         | Indicates whether the process is considered a thread (that is, a child process that hasn't executed another program)                 |
| `setrlimit.target.parent.args`                                       | Arguments of the process (as a string, excluding argv0)                                                                              |
| `setrlimit.target.parent.args_flags`                                 | Flags in the process arguments                                                                                                       |
| `setrlimit.target.parent.args_options`                               | Argument of the process as options                                                                                                   |
| `setrlimit.target.parent.args_truncated`                             | Indicator of arguments truncation                                                                                                    |
| `setrlimit.target.parent.argv`                                       | Arguments of the process (as an array, excluding argv0)                                                                              |
| `setrlimit.target.parent.argv0`                                      | First argument of the process                                                                                                        |
| `setrlimit.target.parent.auid`                                       | Login UID of the process                                                                                                             |
| `setrlimit.target.parent.cap_effective`                              | Effective capability set of the process                                                                                              |
| `setrlimit.target.parent.cap_permitted`                              | Permitted capability set of the process                                                                                              |
| `setrlimit.target.parent.caps_attempted`                             | Bitmask of the capabilities that the process attempted to use                                                                        |
| `setrlimit.target.parent.caps_used`                                  | Bitmask of the capabilities that the process successfully used                                                                       |
| `setrlimit.target.parent.cgroup.file.inode`                          | Inode of the file                                                                                                                    |
| `setrlimit.target.parent.cgroup.file.mount_id`                       | Mount ID of the file                                                                                                                 |
| `setrlimit.target.parent.cgroup.id`                                  | ID of the cgroup                                                                                                                     |
| `setrlimit.target.parent.cgroup.version`                             | [Experimental] Version of the cgroup API                                                                                             |
| `setrlimit.target.parent.comm`                                       | Comm attribute of the process                                                                                                        |
| `setrlimit.target.parent.container.created_at`                       | Timestamp of the creation of the container                                                                                           |
| `setrlimit.target.parent.container.id`                               | ID of the container                                                                                                                  |
| `setrlimit.target.parent.container.tags`                             | Tags of the container                                                                                                                |
| `setrlimit.target.parent.created_at`                                 | Timestamp of the creation of the process                                                                                             |
| `setrlimit.target.parent.egid`                                       | Effective GID of the process                                                                                                         |
| `setrlimit.target.parent.egroup`                                     | Effective group of the process                                                                                                       |
| `setrlimit.target.parent.envp`                                       | Environment variables of the process                                                                                                 |
| `setrlimit.target.parent.envs`                                       | Environment variable names of the process                                                                                            |
| `setrlimit.target.parent.envs_truncated`                             | Indicator of environment variables truncation                                                                                        |
| `setrlimit.target.parent.euid`                                       | Effective UID of the process                                                                                                         |
| `setrlimit.target.parent.euser`                                      | Effective user of the process                                                                                                        |
| `setrlimit.target.parent.file.change_time`                           | Change time (ctime) of the file                                                                                                      |
| `setrlimit.target.parent.file.extension`                             | File's extension                                                                                                                     |
| `setrlimit.target.parent.file.filesystem`                            | File's filesystem                                                                                                                    |
| `setrlimit.target.parent.file.gid`                                   | GID of the file's owner                                                                                                              |
| `setrlimit.target.parent.file.group`                                 | Group of the file's owner                                                                                                            |
| `setrlimit.target.parent.file.hashes`                                | [Experimental] List of cryptographic hashes computed for this file                                                                   |
| `setrlimit.target.parent.file.in_upper_layer`                        | Indicator of the file layer, for example, in an OverlayFS                                                                            |
| `setrlimit.target.parent.file.inode`                                 | Inode of the file                                                                                                                    |
| `setrlimit.target.parent.file.mode`                                  | Mode of the file                                                                                                                     |
| `setrlimit.target.parent.file.modification_time`                     | Modification time (mtime) of the file                                                                                                |
| `setrlimit.target.parent.file.mount_detached`                        | Indicates whether the file's mount is detached from the VFS                                                                          |
| `setrlimit.target.parent.file.mount_id`                              | Mount ID of the file                                                                                                                 |
| `setrlimit.target.parent.file.mount_visible`                         | Indicates whether the file's mount is visible in the VFS                                                                             |
| `setrlimit.target.parent.file.name`                                  | File's basename                                                                                                                      |
| `setrlimit.target.parent.file.name.length`                           | Length of the corresponding element                                                                                                  |
| `setrlimit.target.parent.file.package.epoch`                         | [Experimental] Epoch of the package that provided this file                                                                          |
| `setrlimit.target.parent.file.package.name`                          | [Experimental] Name of the package that provided this file                                                                           |
| `setrlimit.target.parent.file.package.release`                       | [Experimental] Release of the package that provided this file                                                                        |
| `setrlimit.target.parent.file.package.source_epoch`                  | [Experimental] Epoch of the source package of the package that provided this file                                                    |
| `setrlimit.target.parent.file.package.source_release`                | [Experimental] Release of the source package of the package that provided this file                                                  |
| `setrlimit.target.parent.file.package.source_version`                | [Experimental] Full version of the source package of the package that provided this file                                             |
| `setrlimit.target.parent.file.package.version`                       | [Experimental] Full version of the package that provided this file                                                                   |
| `setrlimit.target.parent.file.path`                                  | File's path                                                                                                                          |
| `setrlimit.target.parent.file.path.length`                           | Length of the corresponding element                                                                                                  |
| `setrlimit.target.parent.file.rights`                                | Rights of the file                                                                                                                   |
| `setrlimit.target.parent.file.uid`                                   | UID of the file's owner                                                                                                              |
| `setrlimit.target.parent.file.user`                                  | User of the file's owner                                                                                                             |
| `setrlimit.target.parent.fsgid`                                      | FileSystem-gid of the process                                                                                                        |
| `setrlimit.target.parent.fsgroup`                                    | FileSystem-group of the process                                                                                                      |
| `setrlimit.target.parent.fsuid`                                      | FileSystem-uid of the process                                                                                                        |
| `setrlimit.target.parent.fsuser`                                     | FileSystem-user of the process                                                                                                       |
| `setrlimit.target.parent.gid`                                        | GID of the process                                                                                                                   |
| `setrlimit.target.parent.group`                                      | Group of the process                                                                                                                 |
| `setrlimit.target.parent.interpreter.file.change_time`               | Change time (ctime) of the file                                                                                                      |
| `setrlimit.target.parent.interpreter.file.extension`                 | File's extension                                                                                                                     |
| `setrlimit.target.parent.interpreter.file.filesystem`                | File's filesystem                                                                                                                    |
| `setrlimit.target.parent.interpreter.file.gid`                       | GID of the file's owner                                                                                                              |
| `setrlimit.target.parent.interpreter.file.group`                     | Group of the file's owner                                                                                                            |
| `setrlimit.target.parent.interpreter.file.hashes`                    | [Experimental] List of cryptographic hashes computed for this file                                                                   |
| `setrlimit.target.parent.interpreter.file.in_upper_layer`            | Indicator of the file layer, for example, in an OverlayFS                                                                            |
| `setrlimit.target.parent.interpreter.file.inode`                     | Inode of the file                                                                                                                    |
| `setrlimit.target.parent.interpreter.file.mode`                      | Mode of the file                                                                                                                     |
| `setrlimit.target.parent.interpreter.file.modification_time`         | Modification time (mtime) of the file                                                                                                |
| `setrlimit.target.parent.interpreter.file.mount_detached`            | Indicates whether the file's mount is detached from the VFS                                                                          |
| `setrlimit.target.parent.interpreter.file.mount_id`                  | Mount ID of the file                                                                                                                 |
| `setrlimit.target.parent.interpreter.file.mount_visible`             | Indicates whether the file's mount is visible in the VFS                                                                             |
| `setrlimit.target.parent.interpreter.file.name`                      | File's basename                                                                                                                      |
| `setrlimit.target.parent.interpreter.file.name.length`               | Length of the corresponding element                                                                                                  |
| `setrlimit.target.parent.interpreter.file.package.epoch`             | [Experimental] Epoch of the package that provided this file                                                                          |
| `setrlimit.target.parent.interpreter.file.package.name`              | [Experimental] Name of the package that provided this file                                                                           |
| `setrlimit.target.parent.interpreter.file.package.release`           | [Experimental] Release of the package that provided this file                                                                        |
| `setrlimit.target.parent.interpreter.file.package.source_epoch`      | [Experimental] Epoch of the source package of the package that provided this file                                                    |
| `setrlimit.target.parent.interpreter.file.package.source_release`    | [Experimental] Release of the source package of the package that provided this file                                                  |
| `setrlimit.target.parent.interpreter.file.package.source_version`    | [Experimental] Full version of the source package of the package that provided this file                                             |
| `setrlimit.target.parent.interpreter.file.package.version`           | [Experimental] Full version of the package that provided this file                                                                   |
| `setrlimit.target.parent.interpreter.file.path`                      | File's path                                                                                                                          |
| `setrlimit.target.parent.interpreter.file.path.length`               | Length of the corresponding element                                                                                                  |
| `setrlimit.target.parent.interpreter.file.rights`                    | Rights of the file                                                                                                                   |
| `setrlimit.target.parent.interpreter.file.uid`                       | UID of the file's owner                                                                                                              |
| `setrlimit.target.parent.interpreter.file.user`                      | User of the file's owner                                                                                                             |
| `setrlimit.target.parent.is_exec`                                    | Indicates whether the process entry is from a new binary execution                                                                   |
| `setrlimit.target.parent.is_kworker`                                 | Indicates whether the process is a kworker                                                                                           |
| `setrlimit.target.parent.is_thread`                                  | Indicates whether the process is considered a thread (that is, a child process that hasn't executed another program)                 |
| `setrlimit.target.parent.pid`                                        | Process ID of the process (also called thread group ID)                                                                              |
| `setrlimit.target.parent.ppid`                                       | Parent process ID                                                                                                                    |
| `setrlimit.target.parent.tid`                                        | Thread ID of the thread                                                                                                              |
| `setrlimit.target.parent.tty_name`                                   | Name of the TTY associated with the process                                                                                          |
| `setrlimit.target.parent.uid`                                        | UID of the process                                                                                                                   |
| `setrlimit.target.parent.user`                                       | User of the process                                                                                                                  |
| `setrlimit.target.parent.user_session.id`                            | Unique identifier of the user session, alias for either ssh_session_id or k8s_session_id, depending on the session type              |
| `setrlimit.target.parent.user_session.identity`                      | User identity of the user session, alias for either ssh_client_ip and ssh_client_port or k8s_username, depending on the session type |
| `setrlimit.target.parent.user_session.k8s_groups`                    | Kubernetes groups of the user that executed the process                                                                              |
| `setrlimit.target.parent.user_session.k8s_session_id`                | Unique identifier of the kubernetes session                                                                                          |
| `setrlimit.target.parent.user_session.k8s_uid`                       | Kubernetes UID of the user that executed the process                                                                                 |
| `setrlimit.target.parent.user_session.k8s_username`                  | Kubernetes username of the user that executed the process                                                                            |
| `setrlimit.target.parent.user_session.session_type`                  | Type of the user session                                                                                                             |
| `setrlimit.target.parent.user_session.ssh_auth_method`               | SSH authentication method used by the user                                                                                           |
| `setrlimit.target.parent.user_session.ssh_client_ip`                 | SSH client IP of the user that executed the process                                                                                  |
| `setrlimit.target.parent.user_session.ssh_client_port`               | SSH client port of the user that executed the process                                                                                |
| `setrlimit.target.parent.user_session.ssh_public_key`                | SSH public key used for authentication (if applicable)                                                                               |
| `setrlimit.target.parent.user_session.ssh_session_id`                | Unique identifier of the SSH user session on the host                                                                                |
| `setrlimit.target.pid`                                               | Process ID of the process (also called thread group ID)                                                                              |
| `setrlimit.target.ppid`                                              | Parent process ID                                                                                                                    |
| `setrlimit.target.tid`                                               | Thread ID of the thread                                                                                                              |
| `setrlimit.target.tty_name`                                          | Name of the TTY associated with the process                                                                                          |
| `setrlimit.target.uid`                                               | UID of the process                                                                                                                   |
| `setrlimit.target.user`                                              | User of the process                                                                                                                  |
| `setrlimit.target.user_session.id`                                   | Unique identifier of the user session, alias for either ssh_session_id or k8s_session_id, depending on the session type              |
| `setrlimit.target.user_session.identity`                             | User identity of the user session, alias for either ssh_client_ip and ssh_client_port or k8s_username, depending on the session type |
| `setrlimit.target.user_session.k8s_groups`                           | Kubernetes groups of the user that executed the process                                                                              |
| `setrlimit.target.user_session.k8s_session_id`                       | Unique identifier of the kubernetes session                                                                                          |
| `setrlimit.target.user_session.k8s_uid`                              | Kubernetes UID of the user that executed the process                                                                                 |
| `setrlimit.target.user_session.k8s_username`                         | Kubernetes username of the user that executed the process                                                                            |
| `setrlimit.target.user_session.session_type`                         | Type of the user session                                                                                                             |
| `setrlimit.target.user_session.ssh_auth_method`                      | SSH authentication method used by the user                                                                                           |
| `setrlimit.target.user_session.ssh_client_ip`                        | SSH client IP of the user that executed the process                                                                                  |
| `setrlimit.target.user_session.ssh_client_port`                      | SSH client port of the user that executed the process                                                                                |
| `setrlimit.target.user_session.ssh_public_key`                       | SSH public key used for authentication (if applicable)                                                                               |
| `setrlimit.target.user_session.ssh_session_id`                       | Unique identifier of the SSH user session on the host                                                                                |

### Event `setsockopt`{% #event-setsockopt %}

A setsockopt was executed

| Property                         | Definition                                                                                                          |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| `setsockopt.filter_hash`         | Hash of the currently attached filter using sha256. Only available if the optname is `SO_ATTACH_FILTER`             |
| `setsockopt.filter_instructions` | Instructions of the currently attached filter. Only available if the optname is `SO_ATTACH_FILTER`                  |
| `setsockopt.filter_len`          | Length of the currently attached filter. Only available if the optname is `SO_ATTACH_FILTER`                        |
| `setsockopt.is_filter_truncated` | Indicates that the currently attached filter is truncated. Only available if the optname is `SO_ATTACH_FILTER`      |
| `setsockopt.level`               | Socket level                                                                                                        |
| `setsockopt.optname`             | Socket option name                                                                                                  |
| `setsockopt.retval`              | Return value of the syscall                                                                                         |
| `setsockopt.socket_family`       | Socket family                                                                                                       |
| `setsockopt.socket_protocol`     | Socket protocol                                                                                                     |
| `setsockopt.socket_type`         | Socket type                                                                                                         |
| `setsockopt.used_immediates`     | List of immediate values used in the currently attached filter. Only available if the optname is `SO_ATTACH_FILTER` |

### Event `setuid`{% #event-setuid %}

A process changed its effective uid

| Property        | Definition                         |
| --------------- | ---------------------------------- |
| `setuid.euid`   | New effective UID of the process   |
| `setuid.euser`  | New effective user of the process  |
| `setuid.fsuid`  | New FileSystem UID of the process  |
| `setuid.fsuser` | New FileSystem user of the process |
| `setuid.uid`    | New UID of the process             |
| `setuid.user`   | New user of the process            |

### Event `setxattr`{% #event-setxattr %}

Set exteneded attributes

| Property                               | Definition                                                                               |
| -------------------------------------- | ---------------------------------------------------------------------------------------- |
| `setxattr.file.change_time`            | Change time (ctime) of the file                                                          |
| `setxattr.file.destination.name`       | Name of the extended attribute                                                           |
| `setxattr.file.destination.namespace`  | Namespace of the extended attribute                                                      |
| `setxattr.file.extension`              | File's extension                                                                         |
| `setxattr.file.filesystem`             | File's filesystem                                                                        |
| `setxattr.file.gid`                    | GID of the file's owner                                                                  |
| `setxattr.file.group`                  | Group of the file's owner                                                                |
| `setxattr.file.hashes`                 | [Experimental] List of cryptographic hashes computed for this file                       |
| `setxattr.file.in_upper_layer`         | Indicator of the file layer, for example, in an OverlayFS                                |
| `setxattr.file.inode`                  | Inode of the file                                                                        |
| `setxattr.file.mode`                   | Mode of the file                                                                         |
| `setxattr.file.modification_time`      | Modification time (mtime) of the file                                                    |
| `setxattr.file.mount_detached`         | Indicates whether the file's mount is detached from the VFS                              |
| `setxattr.file.mount_id`               | Mount ID of the file                                                                     |
| `setxattr.file.mount_visible`          | Indicates whether the file's mount is visible in the VFS                                 |
| `setxattr.file.name`                   | File's basename                                                                          |
| `setxattr.file.name.length`            | Length of the corresponding element                                                      |
| `setxattr.file.package.epoch`          | [Experimental] Epoch of the package that provided this file                              |
| `setxattr.file.package.name`           | [Experimental] Name of the package that provided this file                               |
| `setxattr.file.package.release`        | [Experimental] Release of the package that provided this file                            |
| `setxattr.file.package.source_epoch`   | [Experimental] Epoch of the source package of the package that provided this file        |
| `setxattr.file.package.source_release` | [Experimental] Release of the source package of the package that provided this file      |
| `setxattr.file.package.source_version` | [Experimental] Full version of the source package of the package that provided this file |
| `setxattr.file.package.version`        | [Experimental] Full version of the package that provided this file                       |
| `setxattr.file.path`                   | File's path                                                                              |
| `setxattr.file.path.length`            | Length of the corresponding element                                                      |
| `setxattr.file.rights`                 | Rights of the file                                                                       |
| `setxattr.file.uid`                    | UID of the file's owner                                                                  |
| `setxattr.file.user`                   | User of the file's owner                                                                 |
| `setxattr.retval`                      | Return value of the syscall                                                              |

### Event `signal`{% #event-signal %}

A signal was sent

| Property                                                          | Definition                                                                                                                           |
| ----------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| `signal.pid`                                                      | Target PID                                                                                                                           |
| `signal.retval`                                                   | Return value of the syscall                                                                                                          |
| `signal.target.ancestors.args`                                    | Arguments of the process (as a string, excluding argv0)                                                                              |
| `signal.target.ancestors.args_flags`                              | Flags in the process arguments                                                                                                       |
| `signal.target.ancestors.args_options`                            | Argument of the process as options                                                                                                   |
| `signal.target.ancestors.args_truncated`                          | Indicator of arguments truncation                                                                                                    |
| `signal.target.ancestors.argv`                                    | Arguments of the process (as an array, excluding argv0)                                                                              |
| `signal.target.ancestors.argv0`                                   | First argument of the process                                                                                                        |
| `signal.target.ancestors.auid`                                    | Login UID of the process                                                                                                             |
| `signal.target.ancestors.cap_effective`                           | Effective capability set of the process                                                                                              |
| `signal.target.ancestors.cap_permitted`                           | Permitted capability set of the process                                                                                              |
| `signal.target.ancestors.caps_attempted`                          | Bitmask of the capabilities that the process attempted to use                                                                        |
| `signal.target.ancestors.caps_used`                               | Bitmask of the capabilities that the process successfully used                                                                       |
| `signal.target.ancestors.cgroup.file.inode`                       | Inode of the file                                                                                                                    |
| `signal.target.ancestors.cgroup.file.mount_id`                    | Mount ID of the file                                                                                                                 |
| `signal.target.ancestors.cgroup.id`                               | ID of the cgroup                                                                                                                     |
| `signal.target.ancestors.cgroup.version`                          | [Experimental] Version of the cgroup API                                                                                             |
| `signal.target.ancestors.comm`                                    | Comm attribute of the process                                                                                                        |
| `signal.target.ancestors.container.created_at`                    | Timestamp of the creation of the container                                                                                           |
| `signal.target.ancestors.container.id`                            | ID of the container                                                                                                                  |
| `signal.target.ancestors.container.tags`                          | Tags of the container                                                                                                                |
| `signal.target.ancestors.created_at`                              | Timestamp of the creation of the process                                                                                             |
| `signal.target.ancestors.egid`                                    | Effective GID of the process                                                                                                         |
| `signal.target.ancestors.egroup`                                  | Effective group of the process                                                                                                       |
| `signal.target.ancestors.envp`                                    | Environment variables of the process                                                                                                 |
| `signal.target.ancestors.envs`                                    | Environment variable names of the process                                                                                            |
| `signal.target.ancestors.envs_truncated`                          | Indicator of environment variables truncation                                                                                        |
| `signal.target.ancestors.euid`                                    | Effective UID of the process                                                                                                         |
| `signal.target.ancestors.euser`                                   | Effective user of the process                                                                                                        |
| `signal.target.ancestors.file.change_time`                        | Change time (ctime) of the file                                                                                                      |
| `signal.target.ancestors.file.extension`                          | File's extension                                                                                                                     |
| `signal.target.ancestors.file.filesystem`                         | File's filesystem                                                                                                                    |
| `signal.target.ancestors.file.gid`                                | GID of the file's owner                                                                                                              |
| `signal.target.ancestors.file.group`                              | Group of the file's owner                                                                                                            |
| `signal.target.ancestors.file.hashes`                             | [Experimental] List of cryptographic hashes computed for this file                                                                   |
| `signal.target.ancestors.file.in_upper_layer`                     | Indicator of the file layer, for example, in an OverlayFS                                                                            |
| `signal.target.ancestors.file.inode`                              | Inode of the file                                                                                                                    |
| `signal.target.ancestors.file.mode`                               | Mode of the file                                                                                                                     |
| `signal.target.ancestors.file.modification_time`                  | Modification time (mtime) of the file                                                                                                |
| `signal.target.ancestors.file.mount_detached`                     | Indicates whether the file's mount is detached from the VFS                                                                          |
| `signal.target.ancestors.file.mount_id`                           | Mount ID of the file                                                                                                                 |
| `signal.target.ancestors.file.mount_visible`                      | Indicates whether the file's mount is visible in the VFS                                                                             |
| `signal.target.ancestors.file.name`                               | File's basename                                                                                                                      |
| `signal.target.ancestors.file.name.length`                        | Length of the corresponding element                                                                                                  |
| `signal.target.ancestors.file.package.epoch`                      | [Experimental] Epoch of the package that provided this file                                                                          |
| `signal.target.ancestors.file.package.name`                       | [Experimental] Name of the package that provided this file                                                                           |
| `signal.target.ancestors.file.package.release`                    | [Experimental] Release of the package that provided this file                                                                        |
| `signal.target.ancestors.file.package.source_epoch`               | [Experimental] Epoch of the source package of the package that provided this file                                                    |
| `signal.target.ancestors.file.package.source_release`             | [Experimental] Release of the source package of the package that provided this file                                                  |
| `signal.target.ancestors.file.package.source_version`             | [Experimental] Full version of the source package of the package that provided this file                                             |
| `signal.target.ancestors.file.package.version`                    | [Experimental] Full version of the package that provided this file                                                                   |
| `signal.target.ancestors.file.path`                               | File's path                                                                                                                          |
| `signal.target.ancestors.file.path.length`                        | Length of the corresponding element                                                                                                  |
| `signal.target.ancestors.file.rights`                             | Rights of the file                                                                                                                   |
| `signal.target.ancestors.file.uid`                                | UID of the file's owner                                                                                                              |
| `signal.target.ancestors.file.user`                               | User of the file's owner                                                                                                             |
| `signal.target.ancestors.fsgid`                                   | FileSystem-gid of the process                                                                                                        |
| `signal.target.ancestors.fsgroup`                                 | FileSystem-group of the process                                                                                                      |
| `signal.target.ancestors.fsuid`                                   | FileSystem-uid of the process                                                                                                        |
| `signal.target.ancestors.fsuser`                                  | FileSystem-user of the process                                                                                                       |
| `signal.target.ancestors.gid`                                     | GID of the process                                                                                                                   |
| `signal.target.ancestors.group`                                   | Group of the process                                                                                                                 |
| `signal.target.ancestors.interpreter.file.change_time`            | Change time (ctime) of the file                                                                                                      |
| `signal.target.ancestors.interpreter.file.extension`              | File's extension                                                                                                                     |
| `signal.target.ancestors.interpreter.file.filesystem`             | File's filesystem                                                                                                                    |
| `signal.target.ancestors.interpreter.file.gid`                    | GID of the file's owner                                                                                                              |
| `signal.target.ancestors.interpreter.file.group`                  | Group of the file's owner                                                                                                            |
| `signal.target.ancestors.interpreter.file.hashes`                 | [Experimental] List of cryptographic hashes computed for this file                                                                   |
| `signal.target.ancestors.interpreter.file.in_upper_layer`         | Indicator of the file layer, for example, in an OverlayFS                                                                            |
| `signal.target.ancestors.interpreter.file.inode`                  | Inode of the file                                                                                                                    |
| `signal.target.ancestors.interpreter.file.mode`                   | Mode of the file                                                                                                                     |
| `signal.target.ancestors.interpreter.file.modification_time`      | Modification time (mtime) of the file                                                                                                |
| `signal.target.ancestors.interpreter.file.mount_detached`         | Indicates whether the file's mount is detached from the VFS                                                                          |
| `signal.target.ancestors.interpreter.file.mount_id`               | Mount ID of the file                                                                                                                 |
| `signal.target.ancestors.interpreter.file.mount_visible`          | Indicates whether the file's mount is visible in the VFS                                                                             |
| `signal.target.ancestors.interpreter.file.name`                   | File's basename                                                                                                                      |
| `signal.target.ancestors.interpreter.file.name.length`            | Length of the corresponding element                                                                                                  |
| `signal.target.ancestors.interpreter.file.package.epoch`          | [Experimental] Epoch of the package that provided this file                                                                          |
| `signal.target.ancestors.interpreter.file.package.name`           | [Experimental] Name of the package that provided this file                                                                           |
| `signal.target.ancestors.interpreter.file.package.release`        | [Experimental] Release of the package that provided this file                                                                        |
| `signal.target.ancestors.interpreter.file.package.source_epoch`   | [Experimental] Epoch of the source package of the package that provided this file                                                    |
| `signal.target.ancestors.interpreter.file.package.source_release` | [Experimental] Release of the source package of the package that provided this file                                                  |
| `signal.target.ancestors.interpreter.file.package.source_version` | [Experimental] Full version of the source package of the package that provided this file                                             |
| `signal.target.ancestors.interpreter.file.package.version`        | [Experimental] Full version of the package that provided this file                                                                   |
| `signal.target.ancestors.interpreter.file.path`                   | File's path                                                                                                                          |
| `signal.target.ancestors.interpreter.file.path.length`            | Length of the corresponding element                                                                                                  |
| `signal.target.ancestors.interpreter.file.rights`                 | Rights of the file                                                                                                                   |
| `signal.target.ancestors.interpreter.file.uid`                    | UID of the file's owner                                                                                                              |
| `signal.target.ancestors.interpreter.file.user`                   | User of the file's owner                                                                                                             |
| `signal.target.ancestors.is_exec`                                 | Indicates whether the process entry is from a new binary execution                                                                   |
| `signal.target.ancestors.is_kworker`                              | Indicates whether the process is a kworker                                                                                           |
| `signal.target.ancestors.is_thread`                               | Indicates whether the process is considered a thread (that is, a child process that hasn't executed another program)                 |
| `signal.target.ancestors.length`                                  | Length of the corresponding element                                                                                                  |
| `signal.target.ancestors.pid`                                     | Process ID of the process (also called thread group ID)                                                                              |
| `signal.target.ancestors.ppid`                                    | Parent process ID                                                                                                                    |
| `signal.target.ancestors.tid`                                     | Thread ID of the thread                                                                                                              |
| `signal.target.ancestors.tty_name`                                | Name of the TTY associated with the process                                                                                          |
| `signal.target.ancestors.uid`                                     | UID of the process                                                                                                                   |
| `signal.target.ancestors.user`                                    | User of the process                                                                                                                  |
| `signal.target.ancestors.user_session.id`                         | Unique identifier of the user session, alias for either ssh_session_id or k8s_session_id, depending on the session type              |
| `signal.target.ancestors.user_session.identity`                   | User identity of the user session, alias for either ssh_client_ip and ssh_client_port or k8s_username, depending on the session type |
| `signal.target.ancestors.user_session.k8s_groups`                 | Kubernetes groups of the user that executed the process                                                                              |
| `signal.target.ancestors.user_session.k8s_session_id`             | Unique identifier of the kubernetes session                                                                                          |
| `signal.target.ancestors.user_session.k8s_uid`                    | Kubernetes UID of the user that executed the process                                                                                 |
| `signal.target.ancestors.user_session.k8s_username`               | Kubernetes username of the user that executed the process                                                                            |
| `signal.target.ancestors.user_session.session_type`               | Type of the user session                                                                                                             |
| `signal.target.ancestors.user_session.ssh_auth_method`            | SSH authentication method used by the user                                                                                           |
| `signal.target.ancestors.user_session.ssh_client_ip`              | SSH client IP of the user that executed the process                                                                                  |
| `signal.target.ancestors.user_session.ssh_client_port`            | SSH client port of the user that executed the process                                                                                |
| `signal.target.ancestors.user_session.ssh_public_key`             | SSH public key used for authentication (if applicable)                                                                               |
| `signal.target.ancestors.user_session.ssh_session_id`             | Unique identifier of the SSH user session on the host                                                                                |
| `signal.target.args`                                              | Arguments of the process (as a string, excluding argv0)                                                                              |
| `signal.target.args_flags`                                        | Flags in the process arguments                                                                                                       |
| `signal.target.args_options`                                      | Argument of the process as options                                                                                                   |
| `signal.target.args_truncated`                                    | Indicator of arguments truncation                                                                                                    |
| `signal.target.argv`                                              | Arguments of the process (as an array, excluding argv0)                                                                              |
| `signal.target.argv0`                                             | First argument of the process                                                                                                        |
| `signal.target.auid`                                              | Login UID of the process                                                                                                             |
| `signal.target.cap_effective`                                     | Effective capability set of the process                                                                                              |
| `signal.target.cap_permitted`                                     | Permitted capability set of the process                                                                                              |
| `signal.target.caps_attempted`                                    | Bitmask of the capabilities that the process attempted to use                                                                        |
| `signal.target.caps_used`                                         | Bitmask of the capabilities that the process successfully used                                                                       |
| `signal.target.cgroup.file.inode`                                 | Inode of the file                                                                                                                    |
| `signal.target.cgroup.file.mount_id`                              | Mount ID of the file                                                                                                                 |
| `signal.target.cgroup.id`                                         | ID of the cgroup                                                                                                                     |
| `signal.target.cgroup.version`                                    | [Experimental] Version of the cgroup API                                                                                             |
| `signal.target.comm`                                              | Comm attribute of the process                                                                                                        |
| `signal.target.container.created_at`                              | Timestamp of the creation of the container                                                                                           |
| `signal.target.container.id`                                      | ID of the container                                                                                                                  |
| `signal.target.container.tags`                                    | Tags of the container                                                                                                                |
| `signal.target.created_at`                                        | Timestamp of the creation of the process                                                                                             |
| `signal.target.egid`                                              | Effective GID of the process                                                                                                         |
| `signal.target.egroup`                                            | Effective group of the process                                                                                                       |
| `signal.target.envp`                                              | Environment variables of the process                                                                                                 |
| `signal.target.envs`                                              | Environment variable names of the process                                                                                            |
| `signal.target.envs_truncated`                                    | Indicator of environment variables truncation                                                                                        |
| `signal.target.euid`                                              | Effective UID of the process                                                                                                         |
| `signal.target.euser`                                             | Effective user of the process                                                                                                        |
| `signal.target.file.change_time`                                  | Change time (ctime) of the file                                                                                                      |
| `signal.target.file.extension`                                    | File's extension                                                                                                                     |
| `signal.target.file.filesystem`                                   | File's filesystem                                                                                                                    |
| `signal.target.file.gid`                                          | GID of the file's owner                                                                                                              |
| `signal.target.file.group`                                        | Group of the file's owner                                                                                                            |
| `signal.target.file.hashes`                                       | [Experimental] List of cryptographic hashes computed for this file                                                                   |
| `signal.target.file.in_upper_layer`                               | Indicator of the file layer, for example, in an OverlayFS                                                                            |
| `signal.target.file.inode`                                        | Inode of the file                                                                                                                    |
| `signal.target.file.mode`                                         | Mode of the file                                                                                                                     |
| `signal.target.file.modification_time`                            | Modification time (mtime) of the file                                                                                                |
| `signal.target.file.mount_detached`                               | Indicates whether the file's mount is detached from the VFS                                                                          |
| `signal.target.file.mount_id`                                     | Mount ID of the file                                                                                                                 |
| `signal.target.file.mount_visible`                                | Indicates whether the file's mount is visible in the VFS                                                                             |
| `signal.target.file.name`                                         | File's basename                                                                                                                      |
| `signal.target.file.name.length`                                  | Length of the corresponding element                                                                                                  |
| `signal.target.file.package.epoch`                                | [Experimental] Epoch of the package that provided this file                                                                          |
| `signal.target.file.package.name`                                 | [Experimental] Name of the package that provided this file                                                                           |
| `signal.target.file.package.release`                              | [Experimental] Release of the package that provided this file                                                                        |
| `signal.target.file.package.source_epoch`                         | [Experimental] Epoch of the source package of the package that provided this file                                                    |
| `signal.target.file.package.source_release`                       | [Experimental] Release of the source package of the package that provided this file                                                  |
| `signal.target.file.package.source_version`                       | [Experimental] Full version of the source package of the package that provided this file                                             |
| `signal.target.file.package.version`                              | [Experimental] Full version of the package that provided this file                                                                   |
| `signal.target.file.path`                                         | File's path                                                                                                                          |
| `signal.target.file.path.length`                                  | Length of the corresponding element                                                                                                  |
| `signal.target.file.rights`                                       | Rights of the file                                                                                                                   |
| `signal.target.file.uid`                                          | UID of the file's owner                                                                                                              |
| `signal.target.file.user`                                         | User of the file's owner                                                                                                             |
| `signal.target.fsgid`                                             | FileSystem-gid of the process                                                                                                        |
| `signal.target.fsgroup`                                           | FileSystem-group of the process                                                                                                      |
| `signal.target.fsuid`                                             | FileSystem-uid of the process                                                                                                        |
| `signal.target.fsuser`                                            | FileSystem-user of the process                                                                                                       |
| `signal.target.gid`                                               | GID of the process                                                                                                                   |
| `signal.target.group`                                             | Group of the process                                                                                                                 |
| `signal.target.interpreter.file.change_time`                      | Change time (ctime) of the file                                                                                                      |
| `signal.target.interpreter.file.extension`                        | File's extension                                                                                                                     |
| `signal.target.interpreter.file.filesystem`                       | File's filesystem                                                                                                                    |
| `signal.target.interpreter.file.gid`                              | GID of the file's owner                                                                                                              |
| `signal.target.interpreter.file.group`                            | Group of the file's owner                                                                                                            |
| `signal.target.interpreter.file.hashes`                           | [Experimental] List of cryptographic hashes computed for this file                                                                   |
| `signal.target.interpreter.file.in_upper_layer`                   | Indicator of the file layer, for example, in an OverlayFS                                                                            |
| `signal.target.interpreter.file.inode`                            | Inode of the file                                                                                                                    |
| `signal.target.interpreter.file.mode`                             | Mode of the file                                                                                                                     |
| `signal.target.interpreter.file.modification_time`                | Modification time (mtime) of the file                                                                                                |
| `signal.target.interpreter.file.mount_detached`                   | Indicates whether the file's mount is detached from the VFS                                                                          |
| `signal.target.interpreter.file.mount_id`                         | Mount ID of the file                                                                                                                 |
| `signal.target.interpreter.file.mount_visible`                    | Indicates whether the file's mount is visible in the VFS                                                                             |
| `signal.target.interpreter.file.name`                             | File's basename                                                                                                                      |
| `signal.target.interpreter.file.name.length`                      | Length of the corresponding element                                                                                                  |
| `signal.target.interpreter.file.package.epoch`                    | [Experimental] Epoch of the package that provided this file                                                                          |
| `signal.target.interpreter.file.package.name`                     | [Experimental] Name of the package that provided this file                                                                           |
| `signal.target.interpreter.file.package.release`                  | [Experimental] Release of the package that provided this file                                                                        |
| `signal.target.interpreter.file.package.source_epoch`             | [Experimental] Epoch of the source package of the package that provided this file                                                    |
| `signal.target.interpreter.file.package.source_release`           | [Experimental] Release of the source package of the package that provided this file                                                  |
| `signal.target.interpreter.file.package.source_version`           | [Experimental] Full version of the source package of the package that provided this file                                             |
| `signal.target.interpreter.file.package.version`                  | [Experimental] Full version of the package that provided this file                                                                   |
| `signal.target.interpreter.file.path`                             | File's path                                                                                                                          |
| `signal.target.interpreter.file.path.length`                      | Length of the corresponding element                                                                                                  |
| `signal.target.interpreter.file.rights`                           | Rights of the file                                                                                                                   |
| `signal.target.interpreter.file.uid`                              | UID of the file's owner                                                                                                              |
| `signal.target.interpreter.file.user`                             | User of the file's owner                                                                                                             |
| `signal.target.is_exec`                                           | Indicates whether the process entry is from a new binary execution                                                                   |
| `signal.target.is_kworker`                                        | Indicates whether the process is a kworker                                                                                           |
| `signal.target.is_thread`                                         | Indicates whether the process is considered a thread (that is, a child process that hasn't executed another program)                 |
| `signal.target.parent.args`                                       | Arguments of the process (as a string, excluding argv0)                                                                              |
| `signal.target.parent.args_flags`                                 | Flags in the process arguments                                                                                                       |
| `signal.target.parent.args_options`                               | Argument of the process as options                                                                                                   |
| `signal.target.parent.args_truncated`                             | Indicator of arguments truncation                                                                                                    |
| `signal.target.parent.argv`                                       | Arguments of the process (as an array, excluding argv0)                                                                              |
| `signal.target.parent.argv0`                                      | First argument of the process                                                                                                        |
| `signal.target.parent.auid`                                       | Login UID of the process                                                                                                             |
| `signal.target.parent.cap_effective`                              | Effective capability set of the process                                                                                              |
| `signal.target.parent.cap_permitted`                              | Permitted capability set of the process                                                                                              |
| `signal.target.parent.caps_attempted`                             | Bitmask of the capabilities that the process attempted to use                                                                        |
| `signal.target.parent.caps_used`                                  | Bitmask of the capabilities that the process successfully used                                                                       |
| `signal.target.parent.cgroup.file.inode`                          | Inode of the file                                                                                                                    |
| `signal.target.parent.cgroup.file.mount_id`                       | Mount ID of the file                                                                                                                 |
| `signal.target.parent.cgroup.id`                                  | ID of the cgroup                                                                                                                     |
| `signal.target.parent.cgroup.version`                             | [Experimental] Version of the cgroup API                                                                                             |
| `signal.target.parent.comm`                                       | Comm attribute of the process                                                                                                        |
| `signal.target.parent.container.created_at`                       | Timestamp of the creation of the container                                                                                           |
| `signal.target.parent.container.id`                               | ID of the container                                                                                                                  |
| `signal.target.parent.container.tags`                             | Tags of the container                                                                                                                |
| `signal.target.parent.created_at`                                 | Timestamp of the creation of the process                                                                                             |
| `signal.target.parent.egid`                                       | Effective GID of the process                                                                                                         |
| `signal.target.parent.egroup`                                     | Effective group of the process                                                                                                       |
| `signal.target.parent.envp`                                       | Environment variables of the process                                                                                                 |
| `signal.target.parent.envs`                                       | Environment variable names of the process                                                                                            |
| `signal.target.parent.envs_truncated`                             | Indicator of environment variables truncation                                                                                        |
| `signal.target.parent.euid`                                       | Effective UID of the process                                                                                                         |
| `signal.target.parent.euser`                                      | Effective user of the process                                                                                                        |
| `signal.target.parent.file.change_time`                           | Change time (ctime) of the file                                                                                                      |
| `signal.target.parent.file.extension`                             | File's extension                                                                                                                     |
| `signal.target.parent.file.filesystem`                            | File's filesystem                                                                                                                    |
| `signal.target.parent.file.gid`                                   | GID of the file's owner                                                                                                              |
| `signal.target.parent.file.group`                                 | Group of the file's owner                                                                                                            |
| `signal.target.parent.file.hashes`                                | [Experimental] List of cryptographic hashes computed for this file                                                                   |
| `signal.target.parent.file.in_upper_layer`                        | Indicator of the file layer, for example, in an OverlayFS                                                                            |
| `signal.target.parent.file.inode`                                 | Inode of the file                                                                                                                    |
| `signal.target.parent.file.mode`                                  | Mode of the file                                                                                                                     |
| `signal.target.parent.file.modification_time`                     | Modification time (mtime) of the file                                                                                                |
| `signal.target.parent.file.mount_detached`                        | Indicates whether the file's mount is detached from the VFS                                                                          |
| `signal.target.parent.file.mount_id`                              | Mount ID of the file                                                                                                                 |
| `signal.target.parent.file.mount_visible`                         | Indicates whether the file's mount is visible in the VFS                                                                             |
| `signal.target.parent.file.name`                                  | File's basename                                                                                                                      |
| `signal.target.parent.file.name.length`                           | Length of the corresponding element                                                                                                  |
| `signal.target.parent.file.package.epoch`                         | [Experimental] Epoch of the package that provided this file                                                                          |
| `signal.target.parent.file.package.name`                          | [Experimental] Name of the package that provided this file                                                                           |
| `signal.target.parent.file.package.release`                       | [Experimental] Release of the package that provided this file                                                                        |
| `signal.target.parent.file.package.source_epoch`                  | [Experimental] Epoch of the source package of the package that provided this file                                                    |
| `signal.target.parent.file.package.source_release`                | [Experimental] Release of the source package of the package that provided this file                                                  |
| `signal.target.parent.file.package.source_version`                | [Experimental] Full version of the source package of the package that provided this file                                             |
| `signal.target.parent.file.package.version`                       | [Experimental] Full version of the package that provided this file                                                                   |
| `signal.target.parent.file.path`                                  | File's path                                                                                                                          |
| `signal.target.parent.file.path.length`                           | Length of the corresponding element                                                                                                  |
| `signal.target.parent.file.rights`                                | Rights of the file                                                                                                                   |
| `signal.target.parent.file.uid`                                   | UID of the file's owner                                                                                                              |
| `signal.target.parent.file.user`                                  | User of the file's owner                                                                                                             |
| `signal.target.parent.fsgid`                                      | FileSystem-gid of the process                                                                                                        |
| `signal.target.parent.fsgroup`                                    | FileSystem-group of the process                                                                                                      |
| `signal.target.parent.fsuid`                                      | FileSystem-uid of the process                                                                                                        |
| `signal.target.parent.fsuser`                                     | FileSystem-user of the process                                                                                                       |
| `signal.target.parent.gid`                                        | GID of the process                                                                                                                   |
| `signal.target.parent.group`                                      | Group of the process                                                                                                                 |
| `signal.target.parent.interpreter.file.change_time`               | Change time (ctime) of the file                                                                                                      |
| `signal.target.parent.interpreter.file.extension`                 | File's extension                                                                                                                     |
| `signal.target.parent.interpreter.file.filesystem`                | File's filesystem                                                                                                                    |
| `signal.target.parent.interpreter.file.gid`                       | GID of the file's owner                                                                                                              |
| `signal.target.parent.interpreter.file.group`                     | Group of the file's owner                                                                                                            |
| `signal.target.parent.interpreter.file.hashes`                    | [Experimental] List of cryptographic hashes computed for this file                                                                   |
| `signal.target.parent.interpreter.file.in_upper_layer`            | Indicator of the file layer, for example, in an OverlayFS                                                                            |
| `signal.target.parent.interpreter.file.inode`                     | Inode of the file                                                                                                                    |
| `signal.target.parent.interpreter.file.mode`                      | Mode of the file                                                                                                                     |
| `signal.target.parent.interpreter.file.modification_time`         | Modification time (mtime) of the file                                                                                                |
| `signal.target.parent.interpreter.file.mount_detached`            | Indicates whether the file's mount is detached from the VFS                                                                          |
| `signal.target.parent.interpreter.file.mount_id`                  | Mount ID of the file                                                                                                                 |
| `signal.target.parent.interpreter.file.mount_visible`             | Indicates whether the file's mount is visible in the VFS                                                                             |
| `signal.target.parent.interpreter.file.name`                      | File's basename                                                                                                                      |
| `signal.target.parent.interpreter.file.name.length`               | Length of the corresponding element                                                                                                  |
| `signal.target.parent.interpreter.file.package.epoch`             | [Experimental] Epoch of the package that provided this file                                                                          |
| `signal.target.parent.interpreter.file.package.name`              | [Experimental] Name of the package that provided this file                                                                           |
| `signal.target.parent.interpreter.file.package.release`           | [Experimental] Release of the package that provided this file                                                                        |
| `signal.target.parent.interpreter.file.package.source_epoch`      | [Experimental] Epoch of the source package of the package that provided this file                                                    |
| `signal.target.parent.interpreter.file.package.source_release`    | [Experimental] Release of the source package of the package that provided this file                                                  |
| `signal.target.parent.interpreter.file.package.source_version`    | [Experimental] Full version of the source package of the package that provided this file                                             |
| `signal.target.parent.interpreter.file.package.version`           | [Experimental] Full version of the package that provided this file                                                                   |
| `signal.target.parent.interpreter.file.path`                      | File's path                                                                                                                          |
| `signal.target.parent.interpreter.file.path.length`               | Length of the corresponding element                                                                                                  |
| `signal.target.parent.interpreter.file.rights`                    | Rights of the file                                                                                                                   |
| `signal.target.parent.interpreter.file.uid`                       | UID of the file's owner                                                                                                              |
| `signal.target.parent.interpreter.file.user`                      | User of the file's owner                                                                                                             |
| `signal.target.parent.is_exec`                                    | Indicates whether the process entry is from a new binary execution                                                                   |
| `signal.target.parent.is_kworker`                                 | Indicates whether the process is a kworker                                                                                           |
| `signal.target.parent.is_thread`                                  | Indicates whether the process is considered a thread (that is, a child process that hasn't executed another program)                 |
| `signal.target.parent.pid`                                        | Process ID of the process (also called thread group ID)                                                                              |
| `signal.target.parent.ppid`                                       | Parent process ID                                                                                                                    |
| `signal.target.parent.tid`                                        | Thread ID of the thread                                                                                                              |
| `signal.target.parent.tty_name`                                   | Name of the TTY associated with the process                                                                                          |
| `signal.target.parent.uid`                                        | UID of the process                                                                                                                   |
| `signal.target.parent.user`                                       | User of the process                                                                                                                  |
| `signal.target.parent.user_session.id`                            | Unique identifier of the user session, alias for either ssh_session_id or k8s_session_id, depending on the session type              |
| `signal.target.parent.user_session.identity`                      | User identity of the user session, alias for either ssh_client_ip and ssh_client_port or k8s_username, depending on the session type |
| `signal.target.parent.user_session.k8s_groups`                    | Kubernetes groups of the user that executed the process                                                                              |
| `signal.target.parent.user_session.k8s_session_id`                | Unique identifier of the kubernetes session                                                                                          |
| `signal.target.parent.user_session.k8s_uid`                       | Kubernetes UID of the user that executed the process                                                                                 |
| `signal.target.parent.user_session.k8s_username`                  | Kubernetes username of the user that executed the process                                                                            |
| `signal.target.parent.user_session.session_type`                  | Type of the user session                                                                                                             |
| `signal.target.parent.user_session.ssh_auth_method`               | SSH authentication method used by the user                                                                                           |
| `signal.target.parent.user_session.ssh_client_ip`                 | SSH client IP of the user that executed the process                                                                                  |
| `signal.target.parent.user_session.ssh_client_port`               | SSH client port of the user that executed the process                                                                                |
| `signal.target.parent.user_session.ssh_public_key`                | SSH public key used for authentication (if applicable)                                                                               |
| `signal.target.parent.user_session.ssh_session_id`                | Unique identifier of the SSH user session on the host                                                                                |
| `signal.target.pid`                                               | Process ID of the process (also called thread group ID)                                                                              |
| `signal.target.ppid`                                              | Parent process ID                                                                                                                    |
| `signal.target.tid`                                               | Thread ID of the thread                                                                                                              |
| `signal.target.tty_name`                                          | Name of the TTY associated with the process                                                                                          |
| `signal.target.uid`                                               | UID of the process                                                                                                                   |
| `signal.target.user`                                              | User of the process                                                                                                                  |
| `signal.target.user_session.id`                                   | Unique identifier of the user session, alias for either ssh_session_id or k8s_session_id, depending on the session type              |
| `signal.target.user_session.identity`                             | User identity of the user session, alias for either ssh_client_ip and ssh_client_port or k8s_username, depending on the session type |
| `signal.target.user_session.k8s_groups`                           | Kubernetes groups of the user that executed the process                                                                              |
| `signal.target.user_session.k8s_session_id`                       | Unique identifier of the kubernetes session                                                                                          |
| `signal.target.user_session.k8s_uid`                              | Kubernetes UID of the user that executed the process                                                                                 |
| `signal.target.user_session.k8s_username`                         | Kubernetes username of the user that executed the process                                                                            |
| `signal.target.user_session.session_type`                         | Type of the user session                                                                                                             |
| `signal.target.user_session.ssh_auth_method`                      | SSH authentication method used by the user                                                                                           |
| `signal.target.user_session.ssh_client_ip`                        | SSH client IP of the user that executed the process                                                                                  |
| `signal.target.user_session.ssh_client_port`                      | SSH client port of the user that executed the process                                                                                |
| `signal.target.user_session.ssh_public_key`                       | SSH public key used for authentication (if applicable)                                                                               |
| `signal.target.user_session.ssh_session_id`                       | Unique identifier of the SSH user session on the host                                                                                |
| `signal.type`                                                     | Signal type (ex: SIGHUP, SIGINT, SIGQUIT, etc)                                                                                       |

### Event `splice`{% #event-splice %}

A splice command was executed

| Property                             | Definition                                                                               |
| ------------------------------------ | ---------------------------------------------------------------------------------------- |
| `splice.file.change_time`            | Change time (ctime) of the file                                                          |
| `splice.file.extension`              | File's extension                                                                         |
| `splice.file.filesystem`             | File's filesystem                                                                        |
| `splice.file.gid`                    | GID of the file's owner                                                                  |
| `splice.file.group`                  | Group of the file's owner                                                                |
| `splice.file.hashes`                 | [Experimental] List of cryptographic hashes computed for this file                       |
| `splice.file.in_upper_layer`         | Indicator of the file layer, for example, in an OverlayFS                                |
| `splice.file.inode`                  | Inode of the file                                                                        |
| `splice.file.mode`                   | Mode of the file                                                                         |
| `splice.file.modification_time`      | Modification time (mtime) of the file                                                    |
| `splice.file.mount_detached`         | Indicates whether the file's mount is detached from the VFS                              |
| `splice.file.mount_id`               | Mount ID of the file                                                                     |
| `splice.file.mount_visible`          | Indicates whether the file's mount is visible in the VFS                                 |
| `splice.file.name`                   | File's basename                                                                          |
| `splice.file.name.length`            | Length of the corresponding element                                                      |
| `splice.file.package.epoch`          | [Experimental] Epoch of the package that provided this file                              |
| `splice.file.package.name`           | [Experimental] Name of the package that provided this file                               |
| `splice.file.package.release`        | [Experimental] Release of the package that provided this file                            |
| `splice.file.package.source_epoch`   | [Experimental] Epoch of the source package of the package that provided this file        |
| `splice.file.package.source_release` | [Experimental] Release of the source package of the package that provided this file      |
| `splice.file.package.source_version` | [Experimental] Full version of the source package of the package that provided this file |
| `splice.file.package.version`        | [Experimental] Full version of the package that provided this file                       |
| `splice.file.path`                   | File's path                                                                              |
| `splice.file.path.length`            | Length of the corresponding element                                                      |
| `splice.file.rights`                 | Rights of the file                                                                       |
| `splice.file.uid`                    | UID of the file's owner                                                                  |
| `splice.file.user`                   | User of the file's owner                                                                 |
| `splice.pipe_entry_flag`             | Entry flag of the "fd_out" pipe passed to the splice syscall                             |
| `splice.pipe_exit_flag`              | Exit flag of the "fd_out" pipe passed to the splice syscall                              |
| `splice.retval`                      | Return value of the syscall                                                              |

### Event `sysctl`{% #event-sysctl %}

A sysctl parameter was read or modified

| Property                     | Definition                                                                             |
| ---------------------------- | -------------------------------------------------------------------------------------- |
| `sysctl.action`              | Action performed on the system control parameter                                       |
| `sysctl.file_position`       | Position in the sysctl control parameter file at which the action occurred             |
| `sysctl.name`                | Name of the system control parameter                                                   |
| `sysctl.name_truncated`      | Indicates that the name field is truncated                                             |
| `sysctl.old_value`           | Old value of the system control parameter                                              |
| `sysctl.old_value_truncated` | Indicates that the old value field is truncated                                        |
| `sysctl.value`               | New and/or current value for the system control parameter depending on the action type |
| `sysctl.value_truncated`     | Indicates that the value field is truncated                                            |

### Event `unlink`{% #event-unlink %}

A file was deleted

| Property                             | Definition                                                                               |
| ------------------------------------ | ---------------------------------------------------------------------------------------- |
| `unlink.file.change_time`            | Change time (ctime) of the file                                                          |
| `unlink.file.extension`              | File's extension                                                                         |
| `unlink.file.filesystem`             | File's filesystem                                                                        |
| `unlink.file.gid`                    | GID of the file's owner                                                                  |
| `unlink.file.group`                  | Group of the file's owner                                                                |
| `unlink.file.hashes`                 | [Experimental] List of cryptographic hashes computed for this file                       |
| `unlink.file.in_upper_layer`         | Indicator of the file layer, for example, in an OverlayFS                                |
| `unlink.file.inode`                  | Inode of the file                                                                        |
| `unlink.file.mode`                   | Mode of the file                                                                         |
| `unlink.file.modification_time`      | Modification time (mtime) of the file                                                    |
| `unlink.file.mount_detached`         | Indicates whether the file's mount is detached from the VFS                              |
| `unlink.file.mount_id`               | Mount ID of the file                                                                     |
| `unlink.file.mount_visible`          | Indicates whether the file's mount is visible in the VFS                                 |
| `unlink.file.name`                   | File's basename                                                                          |
| `unlink.file.name.length`            | Length of the corresponding element                                                      |
| `unlink.file.package.epoch`          | [Experimental] Epoch of the package that provided this file                              |
| `unlink.file.package.name`           | [Experimental] Name of the package that provided this file                               |
| `unlink.file.package.release`        | [Experimental] Release of the package that provided this file                            |
| `unlink.file.package.source_epoch`   | [Experimental] Epoch of the source package of the package that provided this file        |
| `unlink.file.package.source_release` | [Experimental] Release of the source package of the package that provided this file      |
| `unlink.file.package.source_version` | [Experimental] Full version of the source package of the package that provided this file |
| `unlink.file.package.version`        | [Experimental] Full version of the package that provided this file                       |
| `unlink.file.path`                   | File's path                                                                              |
| `unlink.file.path.length`            | Length of the corresponding element                                                      |
| `unlink.file.rights`                 | Rights of the file                                                                       |
| `unlink.file.uid`                    | UID of the file's owner                                                                  |
| `unlink.file.user`                   | User of the file's owner                                                                 |
| `unlink.flags`                       | Flags of the unlink syscall                                                              |
| `unlink.retval`                      | Return value of the syscall                                                              |
| `unlink.syscall.dirfd`               | Directory file descriptor argument of the syscall                                        |
| `unlink.syscall.flags`               | Flags argument of the syscall                                                            |
| `unlink.syscall.path`                | Path argument of the syscall                                                             |

### Event `unload_module`{% #event-unload_module %}

A kernel module was deleted

| Property               | Definition                                 |
| ---------------------- | ------------------------------------------ |
| `unload_module.name`   | Name of the kernel module that was deleted |
| `unload_module.retval` | Return value of the syscall                |

### Event `utimes`{% #event-utimes %}

Change file access/modification times

| Property                             | Definition                                                                               |
| ------------------------------------ | ---------------------------------------------------------------------------------------- |
| `utimes.file.change_time`            | Change time (ctime) of the file                                                          |
| `utimes.file.extension`              | File's extension                                                                         |
| `utimes.file.filesystem`             | File's filesystem                                                                        |
| `utimes.file.gid`                    | GID of the file's owner                                                                  |
| `utimes.file.group`                  | Group of the file's owner                                                                |
| `utimes.file.hashes`                 | [Experimental] List of cryptographic hashes computed for this file                       |
| `utimes.file.in_upper_layer`         | Indicator of the file layer, for example, in an OverlayFS                                |
| `utimes.file.inode`                  | Inode of the file                                                                        |
| `utimes.file.mode`                   | Mode of the file                                                                         |
| `utimes.file.modification_time`      | Modification time (mtime) of the file                                                    |
| `utimes.file.mount_detached`         | Indicates whether the file's mount is detached from the VFS                              |
| `utimes.file.mount_id`               | Mount ID of the file                                                                     |
| `utimes.file.mount_visible`          | Indicates whether the file's mount is visible in the VFS                                 |
| `utimes.file.name`                   | File's basename                                                                          |
| `utimes.file.name.length`            | Length of the corresponding element                                                      |
| `utimes.file.package.epoch`          | [Experimental] Epoch of the package that provided this file                              |
| `utimes.file.package.name`           | [Experimental] Name of the package that provided this file                               |
| `utimes.file.package.release`        | [Experimental] Release of the package that provided this file                            |
| `utimes.file.package.source_epoch`   | [Experimental] Epoch of the source package of the package that provided this file        |
| `utimes.file.package.source_release` | [Experimental] Release of the source package of the package that provided this file      |
| `utimes.file.package.source_version` | [Experimental] Full version of the source package of the package that provided this file |
| `utimes.file.package.version`        | [Experimental] Full version of the package that provided this file                       |
| `utimes.file.path`                   | File's path                                                                              |
| `utimes.file.path.length`            | Length of the corresponding element                                                      |
| `utimes.file.rights`                 | Rights of the file                                                                       |
| `utimes.file.uid`                    | UID of the file's owner                                                                  |
| `utimes.file.user`                   | User of the file's owner                                                                 |
| `utimes.retval`                      | Return value of the syscall                                                              |
| `utimes.syscall.path`                | Path argument of the syscall                                                             |

## Attributes documentation{% #attributes-documentation %}

### `*.args`{% #common-process-args-doc %}

Type: string

Definition: Arguments of the process (as a string, excluding argv0)

`*.args` has 14 possible prefixes: `exec` `exit` `process` `process.ancestors` `process.parent` `ptrace.tracee` `ptrace.tracee.ancestors` `ptrace.tracee.parent` `setrlimit.target` `setrlimit.target.ancestors` `setrlimit.target.parent` `signal.target` `signal.target.ancestors` `signal.target.parent`

Example:

```javascript
exec.args == "-sV -p 22,53,110,143,4564 198.116.0-255.1-127"
```

Matches any process with these exact arguments.

Example:

```javascript
exec.args =~ "* -F * http*"
```

Matches any process that has the "-F" argument anywhere before an argument starting with "http".

### `*.args_flags`{% #common-process-args_flags-doc %}

Type: string

Definition: Flags in the process arguments

`*.args_flags` has 14 possible prefixes: `exec` `exit` `process` `process.ancestors` `process.parent` `ptrace.tracee` `ptrace.tracee.ancestors` `ptrace.tracee.parent` `setrlimit.target` `setrlimit.target.ancestors` `setrlimit.target.parent` `signal.target` `signal.target.ancestors` `signal.target.parent`

Example:

```javascript
exec.args_flags in ["s"] && exec.args_flags in ["V"]
```

Matches any process with both "-s" and "-V" flags in its arguments. Also matches "-sV".

### `*.args_options`{% #common-process-args_options-doc %}

Type: string

Definition: Argument of the process as options

`*.args_options` has 14 possible prefixes: `exec` `exit` `process` `process.ancestors` `process.parent` `ptrace.tracee` `ptrace.tracee.ancestors` `ptrace.tracee.parent` `setrlimit.target` `setrlimit.target.ancestors` `setrlimit.target.parent` `signal.target` `signal.target.ancestors` `signal.target.parent`

Example:

```javascript
exec.args_options in ["p=0-1024"]
```

Matches any process that has either "-p 0-1024" or "âp=0-1024" in its arguments.

### `*.args_truncated`{% #common-process-args_truncated-doc %}

Type: bool

Definition: Indicator of arguments truncation

`*.args_truncated` has 14 possible prefixes: `exec` `exit` `process` `process.ancestors` `process.parent` `ptrace.tracee` `ptrace.tracee.ancestors` `ptrace.tracee.parent` `setrlimit.target` `setrlimit.target.ancestors` `setrlimit.target.parent` `signal.target` `signal.target.ancestors` `signal.target.parent`

### `*.argv`{% #common-process-argv-doc %}

Type: string

Definition: Arguments of the process (as an array, excluding argv0)

`*.argv` has 14 possible prefixes: `exec` `exit` `process` `process.ancestors` `process.parent` `ptrace.tracee` `ptrace.tracee.ancestors` `ptrace.tracee.parent` `setrlimit.target` `setrlimit.target.ancestors` `setrlimit.target.parent` `signal.target` `signal.target.ancestors` `signal.target.parent`

Example:

```javascript
exec.argv in ["127.0.0.1"]
```

Matches any process that has this IP address as one of its arguments.

### `*.argv0`{% #common-process-argv0-doc %}

Type: string

Definition: First argument of the process

`*.argv0` has 14 possible prefixes: `exec` `exit` `process` `process.ancestors` `process.parent` `ptrace.tracee` `ptrace.tracee.ancestors` `ptrace.tracee.parent` `setrlimit.target` `setrlimit.target.ancestors` `setrlimit.target.parent` `signal.target` `signal.target.ancestors` `signal.target.parent`

### `*.auid`{% #common-credentials-auid-doc %}

Type: int

Definition: Login UID of the process

`*.auid` has 14 possible prefixes: `exec` `exit` `process` `process.ancestors` `process.parent` `ptrace.tracee` `ptrace.tracee.ancestors` `ptrace.tracee.parent` `setrlimit.target` `setrlimit.target.ancestors` `setrlimit.target.parent` `signal.target` `signal.target.ancestors` `signal.target.parent`

### `*.cap_effective`{% #common-credentials-cap_effective-doc %}

Type: int

Definition: Effective capability set of the process

`*.cap_effective` has 14 possible prefixes: `exec` `exit` `process` `process.ancestors` `process.parent` `ptrace.tracee` `ptrace.tracee.ancestors` `ptrace.tracee.parent` `setrlimit.target` `setrlimit.target.ancestors` `setrlimit.target.parent` `signal.target` `signal.target.ancestors` `signal.target.parent`

Constants: Kernel Capability constants

### `*.cap_permitted`{% #common-credentials-cap_permitted-doc %}

Type: int

Definition: Permitted capability set of the process

`*.cap_permitted` has 14 possible prefixes: `exec` `exit` `process` `process.ancestors` `process.parent` `ptrace.tracee` `ptrace.tracee.ancestors` `ptrace.tracee.parent` `setrlimit.target` `setrlimit.target.ancestors` `setrlimit.target.parent` `signal.target` `signal.target.ancestors` `signal.target.parent`

Constants: Kernel Capability constants

### `*.caps_attempted`{% #common-process-caps_attempted-doc %}

Type: int

Definition: Bitmask of the capabilities that the process attempted to use

`*.caps_attempted` has 14 possible prefixes: `exec` `exit` `process` `process.ancestors` `process.parent` `ptrace.tracee` `ptrace.tracee.ancestors` `ptrace.tracee.parent` `setrlimit.target` `setrlimit.target.ancestors` `setrlimit.target.parent` `signal.target` `signal.target.ancestors` `signal.target.parent`

Constants: Kernel Capability constants

### `*.caps_used`{% #common-process-caps_used-doc %}

Type: int

Definition: Bitmask of the capabilities that the process successfully used

`*.caps_used` has 14 possible prefixes: `exec` `exit` `process` `process.ancestors` `process.parent` `ptrace.tracee` `ptrace.tracee.ancestors` `ptrace.tracee.parent` `setrlimit.target` `setrlimit.target.ancestors` `setrlimit.target.parent` `signal.target` `signal.target.ancestors` `signal.target.parent`

Constants: Kernel Capability constants

### `*.change_time`{% #common-filefields-change_time-doc %}

Type: int

Definition: Change time (ctime) of the file

`*.change_time` has 46 possible prefixes: `cgroup_write.file` `chdir.file` `chmod.file` `chown.file` `exec.file` `exec.interpreter.file` `exit.file` `exit.interpreter.file` `link.file` `link.file.destination` `load_module.file` `mkdir.file` `mmap.file` `open.file` `process.ancestors.file` `process.ancestors.interpreter.file` `process.file` `process.interpreter.file` `process.parent.file` `process.parent.interpreter.file` `ptrace.tracee.ancestors.file` `ptrace.tracee.ancestors.interpreter.file` `ptrace.tracee.file` `ptrace.tracee.interpreter.file` `ptrace.tracee.parent.file` `ptrace.tracee.parent.interpreter.file` `removexattr.file` `rename.file` `rename.file.destination` `rmdir.file` `setrlimit.target.ancestors.file` `setrlimit.target.ancestors.interpreter.file` `setrlimit.target.file` `setrlimit.target.interpreter.file` `setrlimit.target.parent.file` `setrlimit.target.parent.interpreter.file` `setxattr.file` `signal.target.ancestors.file` `signal.target.ancestors.interpreter.file` `signal.target.file` `signal.target.interpreter.file` `signal.target.parent.file` `signal.target.parent.interpreter.file` `splice.file` `unlink.file` `utimes.file`

### `*.comm`{% #common-process-comm-doc %}

Type: string

Definition: Comm attribute of the process

`*.comm` has 14 possible prefixes: `exec` `exit` `process` `process.ancestors` `process.parent` `ptrace.tracee` `ptrace.tracee.ancestors` `ptrace.tracee.parent` `setrlimit.target` `setrlimit.target.ancestors` `setrlimit.target.parent` `signal.target` `signal.target.ancestors` `signal.target.parent`

### `*.created_at`{% #common-containercontext-created_at-doc %}

Type: int

Definition: Timestamp of the creation of the container

`*.created_at` has 14 possible prefixes: `exec.container` `exit.container` `process.ancestors.container` `process.container` `process.parent.container` `ptrace.tracee.ancestors.container` `ptrace.tracee.container` `ptrace.tracee.parent.container` `setrlimit.target.ancestors.container` `setrlimit.target.container` `setrlimit.target.parent.container` `signal.target.ancestors.container` `signal.target.container` `signal.target.parent.container`

### `*.created_at`{% #common-process-created_at-doc %}

Type: int

Definition: Timestamp of the creation of the process

`*.created_at` has 14 possible prefixes: `exec` `exit` `process` `process.ancestors` `process.parent` `ptrace.tracee` `ptrace.tracee.ancestors` `ptrace.tracee.parent` `setrlimit.target` `setrlimit.target.ancestors` `setrlimit.target.parent` `signal.target` `signal.target.ancestors` `signal.target.parent`

### `*.data_size`{% #common-networkstats-data_size-doc %}

Type: int

Definition: Amount of data transmitted or received

`*.data_size` has 2 possible prefixes: `network_flow_monitor.flows.egress` `network_flow_monitor.flows.ingress`

### `*.egid`{% #common-credentials-egid-doc %}

Type: int

Definition: Effective GID of the process

`*.egid` has 14 possible prefixes: `exec` `exit` `process` `process.ancestors` `process.parent` `ptrace.tracee` `ptrace.tracee.ancestors` `ptrace.tracee.parent` `setrlimit.target` `setrlimit.target.ancestors` `setrlimit.target.parent` `signal.target` `signal.target.ancestors` `signal.target.parent`

### `*.egroup`{% #common-credentials-egroup-doc %}

Type: string

Definition: Effective group of the process

`*.egroup` has 14 possible prefixes: `exec` `exit` `process` `process.ancestors` `process.parent` `ptrace.tracee` `ptrace.tracee.ancestors` `ptrace.tracee.parent` `setrlimit.target` `setrlimit.target.ancestors` `setrlimit.target.parent` `signal.target` `signal.target.ancestors` `signal.target.parent`

### `*.envp`{% #common-process-envp-doc %}

Type: string

Definition: Environment variables of the process

`*.envp` has 14 possible prefixes: `exec` `exit` `process` `process.ancestors` `process.parent` `ptrace.tracee` `ptrace.tracee.ancestors` `ptrace.tracee.parent` `setrlimit.target` `setrlimit.target.ancestors` `setrlimit.target.parent` `signal.target` `signal.target.ancestors` `signal.target.parent`

### `*.envs`{% #common-process-envs-doc %}

Type: string

Definition: Environment variable names of the process

`*.envs` has 14 possible prefixes: `exec` `exit` `process` `process.ancestors` `process.parent` `ptrace.tracee` `ptrace.tracee.ancestors` `ptrace.tracee.parent` `setrlimit.target` `setrlimit.target.ancestors` `setrlimit.target.parent` `signal.target` `signal.target.ancestors` `signal.target.parent`

### `*.envs_truncated`{% #common-process-envs_truncated-doc %}

Type: bool

Definition: Indicator of environment variables truncation

`*.envs_truncated` has 14 possible prefixes: `exec` `exit` `process` `process.ancestors` `process.parent` `ptrace.tracee` `ptrace.tracee.ancestors` `ptrace.tracee.parent` `setrlimit.target` `setrlimit.target.ancestors` `setrlimit.target.parent` `signal.target` `signal.target.ancestors` `signal.target.parent`

### `*.euid`{% #common-credentials-euid-doc %}

Type: int

Definition: Effective UID of the process

`*.euid` has 14 possible prefixes: `exec` `exit` `process` `process.ancestors` `process.parent` `ptrace.tracee` `ptrace.tracee.ancestors` `ptrace.tracee.parent` `setrlimit.target` `setrlimit.target.ancestors` `setrlimit.target.parent` `signal.target` `signal.target.ancestors` `signal.target.parent`

### `*.euser`{% #common-credentials-euser-doc %}

Type: string

Definition: Effective user of the process

`*.euser` has 14 possible prefixes: `exec` `exit` `process` `process.ancestors` `process.parent` `ptrace.tracee` `ptrace.tracee.ancestors` `ptrace.tracee.parent` `setrlimit.target` `setrlimit.target.ancestors` `setrlimit.target.parent` `signal.target` `signal.target.ancestors` `signal.target.parent`

### `*.extension`{% #common-fileevent-extension-doc %}

Type: string

Definition: File's extension

`*.extension` has 46 possible prefixes: `cgroup_write.file` `chdir.file` `chmod.file` `chown.file` `exec.file` `exec.interpreter.file` `exit.file` `exit.interpreter.file` `link.file` `link.file.destination` `load_module.file` `mkdir.file` `mmap.file` `open.file` `process.ancestors.file` `process.ancestors.interpreter.file` `process.file` `process.interpreter.file` `process.parent.file` `process.parent.interpreter.file` `ptrace.tracee.ancestors.file` `ptrace.tracee.ancestors.interpreter.file` `ptrace.tracee.file` `ptrace.tracee.interpreter.file` `ptrace.tracee.parent.file` `ptrace.tracee.parent.interpreter.file` `removexattr.file` `rename.file` `rename.file.destination` `rmdir.file` `setrlimit.target.ancestors.file` `setrlimit.target.ancestors.interpreter.file` `setrlimit.target.file` `setrlimit.target.interpreter.file` `setrlimit.target.parent.file` `setrlimit.target.parent.interpreter.file` `setxattr.file` `signal.target.ancestors.file` `signal.target.ancestors.interpreter.file` `signal.target.file` `signal.target.interpreter.file` `signal.target.parent.file` `signal.target.parent.interpreter.file` `splice.file` `unlink.file` `utimes.file`

### `*.file.destination.name`{% #common-setxattrevent-file-destination-name-doc %}

Type: string

Definition: Name of the extended attribute

`*.file.destination.name` has 2 possible prefixes: `removexattr` `setxattr`

### `*.file.destination.namespace`{% #common-setxattrevent-file-destination-namespace-doc %}

Type: string

Definition: Namespace of the extended attribute

`*.file.destination.namespace` has 2 possible prefixes: `removexattr` `setxattr`

### `*.filesystem`{% #common-fileevent-filesystem-doc %}

Type: string

Definition: File's filesystem

`*.filesystem` has 46 possible prefixes: `cgroup_write.file` `chdir.file` `chmod.file` `chown.file` `exec.file` `exec.interpreter.file` `exit.file` `exit.interpreter.file` `link.file` `link.file.destination` `load_module.file` `mkdir.file` `mmap.file` `open.file` `process.ancestors.file` `process.ancestors.interpreter.file` `process.file` `process.interpreter.file` `process.parent.file` `process.parent.interpreter.file` `ptrace.tracee.ancestors.file` `ptrace.tracee.ancestors.interpreter.file` `ptrace.tracee.file` `ptrace.tracee.interpreter.file` `ptrace.tracee.parent.file` `ptrace.tracee.parent.interpreter.file` `removexattr.file` `rename.file` `rename.file.destination` `rmdir.file` `setrlimit.target.ancestors.file` `setrlimit.target.ancestors.interpreter.file` `setrlimit.target.file` `setrlimit.target.interpreter.file` `setrlimit.target.parent.file` `setrlimit.target.parent.interpreter.file` `setxattr.file` `signal.target.ancestors.file` `signal.target.ancestors.interpreter.file` `signal.target.file` `signal.target.interpreter.file` `signal.target.parent.file` `signal.target.parent.interpreter.file` `splice.file` `unlink.file` `utimes.file`

### `*.fsgid`{% #common-credentials-fsgid-doc %}

Type: int

Definition: FileSystem-gid of the process

`*.fsgid` has 14 possible prefixes: `exec` `exit` `process` `process.ancestors` `process.parent` `ptrace.tracee` `ptrace.tracee.ancestors` `ptrace.tracee.parent` `setrlimit.target` `setrlimit.target.ancestors` `setrlimit.target.parent` `signal.target` `signal.target.ancestors` `signal.target.parent`

### `*.fsgroup`{% #common-credentials-fsgroup-doc %}

Type: string

Definition: FileSystem-group of the process

`*.fsgroup` has 14 possible prefixes: `exec` `exit` `process` `process.ancestors` `process.parent` `ptrace.tracee` `ptrace.tracee.ancestors` `ptrace.tracee.parent` `setrlimit.target` `setrlimit.target.ancestors` `setrlimit.target.parent` `signal.target` `signal.target.ancestors` `signal.target.parent`

### `*.fsuid`{% #common-credentials-fsuid-doc %}

Type: int

Definition: FileSystem-uid of the process

`*.fsuid` has 14 possible prefixes: `exec` `exit` `process` `process.ancestors` `process.parent` `ptrace.tracee` `ptrace.tracee.ancestors` `ptrace.tracee.parent` `setrlimit.target` `setrlimit.target.ancestors` `setrlimit.target.parent` `signal.target` `signal.target.ancestors` `signal.target.parent`

### `*.fsuser`{% #common-credentials-fsuser-doc %}

Type: string

Definition: FileSystem-user of the process

`*.fsuser` has 14 possible prefixes: `exec` `exit` `process` `process.ancestors` `process.parent` `ptrace.tracee` `ptrace.tracee.ancestors` `ptrace.tracee.parent` `setrlimit.target` `setrlimit.target.ancestors` `setrlimit.target.parent` `signal.target` `signal.target.ancestors` `signal.target.parent`

### `*.gid`{% #common-credentials-gid-doc %}

Type: int

Definition: GID of the process

`*.gid` has 14 possible prefixes: `exec` `exit` `process` `process.ancestors` `process.parent` `ptrace.tracee` `ptrace.tracee.ancestors` `ptrace.tracee.parent` `setrlimit.target` `setrlimit.target.ancestors` `setrlimit.target.parent` `signal.target` `signal.target.ancestors` `signal.target.parent`

### `*.gid`{% #common-filefields-gid-doc %}

Type: int

Definition: GID of the file's owner

`*.gid` has 46 possible prefixes: `cgroup_write.file` `chdir.file` `chmod.file` `chown.file` `exec.file` `exec.interpreter.file` `exit.file` `exit.interpreter.file` `link.file` `link.file.destination` `load_module.file` `mkdir.file` `mmap.file` `open.file` `process.ancestors.file` `process.ancestors.interpreter.file` `process.file` `process.interpreter.file` `process.parent.file` `process.parent.interpreter.file` `ptrace.tracee.ancestors.file` `ptrace.tracee.ancestors.interpreter.file` `ptrace.tracee.file` `ptrace.tracee.interpreter.file` `ptrace.tracee.parent.file` `ptrace.tracee.parent.interpreter.file` `removexattr.file` `rename.file` `rename.file.destination` `rmdir.file` `setrlimit.target.ancestors.file` `setrlimit.target.ancestors.interpreter.file` `setrlimit.target.file` `setrlimit.target.interpreter.file` `setrlimit.target.parent.file` `setrlimit.target.parent.interpreter.file` `setxattr.file` `signal.target.ancestors.file` `signal.target.ancestors.interpreter.file` `signal.target.file` `signal.target.interpreter.file` `signal.target.parent.file` `signal.target.parent.interpreter.file` `splice.file` `unlink.file` `utimes.file`

### `*.group`{% #common-credentials-group-doc %}

Type: string

Definition: Group of the process

`*.group` has 14 possible prefixes: `exec` `exit` `process` `process.ancestors` `process.parent` `ptrace.tracee` `ptrace.tracee.ancestors` `ptrace.tracee.parent` `setrlimit.target` `setrlimit.target.ancestors` `setrlimit.target.parent` `signal.target` `signal.target.ancestors` `signal.target.parent`

### `*.group`{% #common-filefields-group-doc %}

Type: string

Definition: Group of the file's owner

`*.group` has 46 possible prefixes: `cgroup_write.file` `chdir.file` `chmod.file` `chown.file` `exec.file` `exec.interpreter.file` `exit.file` `exit.interpreter.file` `link.file` `link.file.destination` `load_module.file` `mkdir.file` `mmap.file` `open.file` `process.ancestors.file` `process.ancestors.interpreter.file` `process.file` `process.interpreter.file` `process.parent.file` `process.parent.interpreter.file` `ptrace.tracee.ancestors.file` `ptrace.tracee.ancestors.interpreter.file` `ptrace.tracee.file` `ptrace.tracee.interpreter.file` `ptrace.tracee.parent.file` `ptrace.tracee.parent.interpreter.file` `removexattr.file` `rename.file` `rename.file.destination` `rmdir.file` `setrlimit.target.ancestors.file` `setrlimit.target.ancestors.interpreter.file` `setrlimit.target.file` `setrlimit.target.interpreter.file` `setrlimit.target.parent.file` `setrlimit.target.parent.interpreter.file` `setxattr.file` `signal.target.ancestors.file` `signal.target.ancestors.interpreter.file` `signal.target.file` `signal.target.interpreter.file` `signal.target.parent.file` `signal.target.parent.interpreter.file` `splice.file` `unlink.file` `utimes.file`

### `*.hashes`{% #common-fileevent-hashes-doc %}

Type: string

Definition: [Experimental] List of cryptographic hashes computed for this file

`*.hashes` has 46 possible prefixes: `cgroup_write.file` `chdir.file` `chmod.file` `chown.file` `exec.file` `exec.interpreter.file` `exit.file` `exit.interpreter.file` `link.file` `link.file.destination` `load_module.file` `mkdir.file` `mmap.file` `open.file` `process.ancestors.file` `process.ancestors.interpreter.file` `process.file` `process.interpreter.file` `process.parent.file` `process.parent.interpreter.file` `ptrace.tracee.ancestors.file` `ptrace.tracee.ancestors.interpreter.file` `ptrace.tracee.file` `ptrace.tracee.interpreter.file` `ptrace.tracee.parent.file` `ptrace.tracee.parent.interpreter.file` `removexattr.file` `rename.file` `rename.file.destination` `rmdir.file` `setrlimit.target.ancestors.file` `setrlimit.target.ancestors.interpreter.file` `setrlimit.target.file` `setrlimit.target.interpreter.file` `setrlimit.target.parent.file` `setrlimit.target.parent.interpreter.file` `setxattr.file` `signal.target.ancestors.file` `signal.target.ancestors.interpreter.file` `signal.target.file` `signal.target.interpreter.file` `signal.target.parent.file` `signal.target.parent.interpreter.file` `splice.file` `unlink.file` `utimes.file`

### `*.id`{% #common-cgroupcontext-id-doc %}

Type: string

Definition: ID of the cgroup

`*.id` has 14 possible prefixes: `exec.cgroup` `exit.cgroup` `process.ancestors.cgroup` `process.cgroup` `process.parent.cgroup` `ptrace.tracee.ancestors.cgroup` `ptrace.tracee.cgroup` `ptrace.tracee.parent.cgroup` `setrlimit.target.ancestors.cgroup` `setrlimit.target.cgroup` `setrlimit.target.parent.cgroup` `signal.target.ancestors.cgroup` `signal.target.cgroup` `signal.target.parent.cgroup`

### `*.id`{% #common-containercontext-id-doc %}

Type: string

Definition: ID of the container

`*.id` has 14 possible prefixes: `exec.container` `exit.container` `process.ancestors.container` `process.container` `process.parent.container` `ptrace.tracee.ancestors.container` `ptrace.tracee.container` `ptrace.tracee.parent.container` `setrlimit.target.ancestors.container` `setrlimit.target.container` `setrlimit.target.parent.container` `signal.target.ancestors.container` `signal.target.container` `signal.target.parent.container`

### `*.id`{% #common-usersessioncontext-id-doc %}

Type: string

Definition: Unique identifier of the user session, alias for either ssh_session_id or k8s_session_id, depending on the session type

`*.id` has 14 possible prefixes: `exec.user_session` `exit.user_session` `process.ancestors.user_session` `process.parent.user_session` `process.user_session` `ptrace.tracee.ancestors.user_session` `ptrace.tracee.parent.user_session` `ptrace.tracee.user_session` `setrlimit.target.ancestors.user_session` `setrlimit.target.parent.user_session` `setrlimit.target.user_session` `signal.target.ancestors.user_session` `signal.target.parent.user_session` `signal.target.user_session`

### `*.identity`{% #common-usersessioncontext-identity-doc %}

Type: string

Definition: User identity of the user session, alias for either ssh_client_ip and ssh_client_port or k8s_username, depending on the session type

`*.identity` has 14 possible prefixes: `exec.user_session` `exit.user_session` `process.ancestors.user_session` `process.parent.user_session` `process.user_session` `ptrace.tracee.ancestors.user_session` `ptrace.tracee.parent.user_session` `ptrace.tracee.user_session` `setrlimit.target.ancestors.user_session` `setrlimit.target.parent.user_session` `setrlimit.target.user_session` `signal.target.ancestors.user_session` `signal.target.parent.user_session` `signal.target.user_session`

### `*.ifname`{% #common-networkdevicecontext-ifname-doc %}

Type: string

Definition: Interface ifname

`*.ifname` has 3 possible prefixes: `network.device` `network_flow_monitor.device` `packet.device`

### `*.in_upper_layer`{% #common-filefields-in_upper_layer-doc %}

Type: bool

Definition: Indicator of the file layer, for example, in an OverlayFS

`*.in_upper_layer` has 46 possible prefixes: `cgroup_write.file` `chdir.file` `chmod.file` `chown.file` `exec.file` `exec.interpreter.file` `exit.file` `exit.interpreter.file` `link.file` `link.file.destination` `load_module.file` `mkdir.file` `mmap.file` `open.file` `process.ancestors.file` `process.ancestors.interpreter.file` `process.file` `process.interpreter.file` `process.parent.file` `process.parent.interpreter.file` `ptrace.tracee.ancestors.file` `ptrace.tracee.ancestors.interpreter.file` `ptrace.tracee.file` `ptrace.tracee.interpreter.file` `ptrace.tracee.parent.file` `ptrace.tracee.parent.interpreter.file` `removexattr.file` `rename.file` `rename.file.destination` `rmdir.file` `setrlimit.target.ancestors.file` `setrlimit.target.ancestors.interpreter.file` `setrlimit.target.file` `setrlimit.target.interpreter.file` `setrlimit.target.parent.file` `setrlimit.target.parent.interpreter.file` `setxattr.file` `signal.target.ancestors.file` `signal.target.ancestors.interpreter.file` `signal.target.file` `signal.target.interpreter.file` `signal.target.parent.file` `signal.target.parent.interpreter.file` `splice.file` `unlink.file` `utimes.file`

### `*.inode`{% #common-pathkey-inode-doc %}

Type: int

Definition: Inode of the file

`*.inode` has 60 possible prefixes: `cgroup_write.file` `chdir.file` `chmod.file` `chown.file` `exec.cgroup.file` `exec.file` `exec.interpreter.file` `exit.cgroup.file` `exit.file` `exit.interpreter.file` `link.file` `link.file.destination` `load_module.file` `mkdir.file` `mmap.file` `open.file` `process.ancestors.cgroup.file` `process.ancestors.file` `process.ancestors.interpreter.file` `process.cgroup.file` `process.file` `process.interpreter.file` `process.parent.cgroup.file` `process.parent.file` `process.parent.interpreter.file` `ptrace.tracee.ancestors.cgroup.file` `ptrace.tracee.ancestors.file` `ptrace.tracee.ancestors.interpreter.file` `ptrace.tracee.cgroup.file` `ptrace.tracee.file` `ptrace.tracee.interpreter.file` `ptrace.tracee.parent.cgroup.file` `ptrace.tracee.parent.file` `ptrace.tracee.parent.interpreter.file` `removexattr.file` `rename.file` `rename.file.destination` `rmdir.file` `setrlimit.target.ancestors.cgroup.file` `setrlimit.target.ancestors.file` `setrlimit.target.ancestors.interpreter.file` `setrlimit.target.cgroup.file` `setrlimit.target.file` `setrlimit.target.interpreter.file` `setrlimit.target.parent.cgroup.file` `setrlimit.target.parent.file` `setrlimit.target.parent.interpreter.file` `setxattr.file` `signal.target.ancestors.cgroup.file` `signal.target.ancestors.file` `signal.target.ancestors.interpreter.file` `signal.target.cgroup.file` `signal.target.file` `signal.target.interpreter.file` `signal.target.parent.cgroup.file` `signal.target.parent.file` `signal.target.parent.interpreter.file` `splice.file` `unlink.file` `utimes.file`

### `*.ip`{% #common-ipportcontext-ip-doc %}

Type: IP/CIDR

Definition: IP address

`*.ip` has 9 possible prefixes: `accept.addr` `bind.addr` `connect.addr` `network.destination` `network.source` `network_flow_monitor.flows.destination` `network_flow_monitor.flows.source` `packet.destination` `packet.source`

### `*.is_exec`{% #common-process-is_exec-doc %}

Type: bool

Definition: Indicates whether the process entry is from a new binary execution

`*.is_exec` has 14 possible prefixes: `exec` `exit` `process` `process.ancestors` `process.parent` `ptrace.tracee` `ptrace.tracee.ancestors` `ptrace.tracee.parent` `setrlimit.target` `setrlimit.target.ancestors` `setrlimit.target.parent` `signal.target` `signal.target.ancestors` `signal.target.parent`

### `*.is_kworker`{% #common-pidcontext-is_kworker-doc %}

Type: bool

Definition: Indicates whether the process is a kworker

`*.is_kworker` has 14 possible prefixes: `exec` `exit` `process` `process.ancestors` `process.parent` `ptrace.tracee` `ptrace.tracee.ancestors` `ptrace.tracee.parent` `setrlimit.target` `setrlimit.target.ancestors` `setrlimit.target.parent` `signal.target` `signal.target.ancestors` `signal.target.parent`

### `*.is_public`{% #common-ipportcontext-is_public-doc %}

Type: bool

Definition: Whether the IP address belongs to a public network

`*.is_public` has 9 possible prefixes: `accept.addr` `bind.addr` `connect.addr` `network.destination` `network.source` `network_flow_monitor.flows.destination` `network_flow_monitor.flows.source` `packet.destination` `packet.source`

### `*.is_thread`{% #common-process-is_thread-doc %}

Type: bool

Definition: Indicates whether the process is considered a thread (that is, a child process that hasn't executed another program)

`*.is_thread` has 14 possible prefixes: `exec` `exit` `process` `process.ancestors` `process.parent` `ptrace.tracee` `ptrace.tracee.ancestors` `ptrace.tracee.parent` `setrlimit.target` `setrlimit.target.ancestors` `setrlimit.target.parent` `signal.target` `signal.target.ancestors` `signal.target.parent`

### `*.k8s_groups`{% #common-k8ssessioncontext-k8s_groups-doc %}

Type: string

Definition: Kubernetes groups of the user that executed the process

`*.k8s_groups` has 14 possible prefixes: `exec.user_session` `exit.user_session` `process.ancestors.user_session` `process.parent.user_session` `process.user_session` `ptrace.tracee.ancestors.user_session` `ptrace.tracee.parent.user_session` `ptrace.tracee.user_session` `setrlimit.target.ancestors.user_session` `setrlimit.target.parent.user_session` `setrlimit.target.user_session` `signal.target.ancestors.user_session` `signal.target.parent.user_session` `signal.target.user_session`

### `*.k8s_session_id`{% #common-k8ssessioncontext-k8s_session_id-doc %}

Type: int

Definition: Unique identifier of the kubernetes session

`*.k8s_session_id` has 14 possible prefixes: `exec.user_session` `exit.user_session` `process.ancestors.user_session` `process.parent.user_session` `process.user_session` `ptrace.tracee.ancestors.user_session` `ptrace.tracee.parent.user_session` `ptrace.tracee.user_session` `setrlimit.target.ancestors.user_session` `setrlimit.target.parent.user_session` `setrlimit.target.user_session` `signal.target.ancestors.user_session` `signal.target.parent.user_session` `signal.target.user_session`

### `*.k8s_uid`{% #common-k8ssessioncontext-k8s_uid-doc %}

Type: string

Definition: Kubernetes UID of the user that executed the process

`*.k8s_uid` has 14 possible prefixes: `exec.user_session` `exit.user_session` `process.ancestors.user_session` `process.parent.user_session` `process.user_session` `ptrace.tracee.ancestors.user_session` `ptrace.tracee.parent.user_session` `ptrace.tracee.user_session` `setrlimit.target.ancestors.user_session` `setrlimit.target.parent.user_session` `setrlimit.target.user_session` `signal.target.ancestors.user_session` `signal.target.parent.user_session` `signal.target.user_session`

### `*.k8s_username`{% #common-k8ssessioncontext-k8s_username-doc %}

Type: string

Definition: Kubernetes username of the user that executed the process

`*.k8s_username` has 14 possible prefixes: `exec.user_session` `exit.user_session` `process.ancestors.user_session` `process.parent.user_session` `process.user_session` `ptrace.tracee.ancestors.user_session` `ptrace.tracee.parent.user_session` `ptrace.tracee.user_session` `setrlimit.target.ancestors.user_session` `setrlimit.target.parent.user_session` `setrlimit.target.user_session` `signal.target.ancestors.user_session` `signal.target.parent.user_session` `signal.target.user_session`

### `*.l3_protocol`{% #common-networkcontext-l3_protocol-doc %}

Type: int

Definition: L3 protocol of the network packet

`*.l3_protocol` has 2 possible prefixes: `network` `packet`

Constants: L3 protocols

### `*.l4_protocol`{% #common-networkcontext-l4_protocol-doc %}

Type: int

Definition: L4 protocol of the network packet

`*.l4_protocol` has 2 possible prefixes: `network` `packet`

Constants: L4 protocols

### `*.length`{% #common-string-length-doc %}

Type: int

Definition: Length of the corresponding element

`*.length` has 98 possible prefixes: `cgroup_write.file.name` `cgroup_write.file.path` `chdir.file.name` `chdir.file.path` `chmod.file.name` `chmod.file.path` `chown.file.name` `chown.file.path` `dns.question.name` `exec.file.name` `exec.file.path` `exec.interpreter.file.name` `exec.interpreter.file.path` `exit.file.name` `exit.file.path` `exit.interpreter.file.name` `exit.interpreter.file.path` `link.file.destination.name` `link.file.destination.path` `link.file.name` `link.file.path` `load_module.file.name` `load_module.file.path` `mkdir.file.name` `mkdir.file.path` `mmap.file.name` `mmap.file.path` `network_flow_monitor.flows` `open.file.name` `open.file.path` `process.ancestors` `process.ancestors.file.name` `process.ancestors.file.path` `process.ancestors.interpreter.file.name` `process.ancestors.interpreter.file.path` `process.file.name` `process.file.path` `process.interpreter.file.name` `process.interpreter.file.path` `process.parent.file.name` `process.parent.file.path` `process.parent.interpreter.file.name` `process.parent.interpreter.file.path` `ptrace.tracee.ancestors` `ptrace.tracee.ancestors.file.name` `ptrace.tracee.ancestors.file.path` `ptrace.tracee.ancestors.interpreter.file.name` `ptrace.tracee.ancestors.interpreter.file.path` `ptrace.tracee.file.name` `ptrace.tracee.file.path` `ptrace.tracee.interpreter.file.name` `ptrace.tracee.interpreter.file.path` `ptrace.tracee.parent.file.name` `ptrace.tracee.parent.file.path` `ptrace.tracee.parent.interpreter.file.name` `ptrace.tracee.parent.interpreter.file.path` `removexattr.file.name` `removexattr.file.path` `rename.file.destination.name` `rename.file.destination.path` `rename.file.name` `rename.file.path` `rmdir.file.name` `rmdir.file.path` `setrlimit.target.ancestors` `setrlimit.target.ancestors.file.name` `setrlimit.target.ancestors.file.path` `setrlimit.target.ancestors.interpreter.file.name` `setrlimit.target.ancestors.interpreter.file.path` `setrlimit.target.file.name` `setrlimit.target.file.path` `setrlimit.target.interpreter.file.name` `setrlimit.target.interpreter.file.path` `setrlimit.target.parent.file.name` `setrlimit.target.parent.file.path` `setrlimit.target.parent.interpreter.file.name` `setrlimit.target.parent.interpreter.file.path` `setxattr.file.name` `setxattr.file.path` `signal.target.ancestors` `signal.target.ancestors.file.name` `signal.target.ancestors.file.path` `signal.target.ancestors.interpreter.file.name` `signal.target.ancestors.interpreter.file.path` `signal.target.file.name` `signal.target.file.path` `signal.target.interpreter.file.name` `signal.target.interpreter.file.path` `signal.target.parent.file.name` `signal.target.parent.file.path` `signal.target.parent.interpreter.file.name` `signal.target.parent.interpreter.file.path` `splice.file.name` `splice.file.path` `unlink.file.name` `unlink.file.path` `utimes.file.name` `utimes.file.path`

### `*.mode`{% #common-filefields-mode-doc %}

Type: int

Definition: Mode of the file

`*.mode` has 46 possible prefixes: `cgroup_write.file` `chdir.file` `chmod.file` `chown.file` `exec.file` `exec.interpreter.file` `exit.file` `exit.interpreter.file` `link.file` `link.file.destination` `load_module.file` `mkdir.file` `mmap.file` `open.file` `process.ancestors.file` `process.ancestors.interpreter.file` `process.file` `process.interpreter.file` `process.parent.file` `process.parent.interpreter.file` `ptrace.tracee.ancestors.file` `ptrace.tracee.ancestors.interpreter.file` `ptrace.tracee.file` `ptrace.tracee.interpreter.file` `ptrace.tracee.parent.file` `ptrace.tracee.parent.interpreter.file` `removexattr.file` `rename.file` `rename.file.destination` `rmdir.file` `setrlimit.target.ancestors.file` `setrlimit.target.ancestors.interpreter.file` `setrlimit.target.file` `setrlimit.target.interpreter.file` `setrlimit.target.parent.file` `setrlimit.target.parent.interpreter.file` `setxattr.file` `signal.target.ancestors.file` `signal.target.ancestors.interpreter.file` `signal.target.file` `signal.target.interpreter.file` `signal.target.parent.file` `signal.target.parent.interpreter.file` `splice.file` `unlink.file` `utimes.file`

Constants: Inode mode constants

### `*.modification_time`{% #common-filefields-modification_time-doc %}

Type: int

Definition: Modification time (mtime) of the file

`*.modification_time` has 46 possible prefixes: `cgroup_write.file` `chdir.file` `chmod.file` `chown.file` `exec.file` `exec.interpreter.file` `exit.file` `exit.interpreter.file` `link.file` `link.file.destination` `load_module.file` `mkdir.file` `mmap.file` `open.file` `process.ancestors.file` `process.ancestors.interpreter.file` `process.file` `process.interpreter.file` `process.parent.file` `process.parent.interpreter.file` `ptrace.tracee.ancestors.file` `ptrace.tracee.ancestors.interpreter.file` `ptrace.tracee.file` `ptrace.tracee.interpreter.file` `ptrace.tracee.parent.file` `ptrace.tracee.parent.interpreter.file` `removexattr.file` `rename.file` `rename.file.destination` `rmdir.file` `setrlimit.target.ancestors.file` `setrlimit.target.ancestors.interpreter.file` `setrlimit.target.file` `setrlimit.target.interpreter.file` `setrlimit.target.parent.file` `setrlimit.target.parent.interpreter.file` `setxattr.file` `signal.target.ancestors.file` `signal.target.ancestors.interpreter.file` `signal.target.file` `signal.target.interpreter.file` `signal.target.parent.file` `signal.target.parent.interpreter.file` `splice.file` `unlink.file` `utimes.file`

### `*.mount_detached`{% #common-fileevent-mount_detached-doc %}

Type: bool

Definition: Indicates whether the file's mount is detached from the VFS

`*.mount_detached` has 46 possible prefixes: `cgroup_write.file` `chdir.file` `chmod.file` `chown.file` `exec.file` `exec.interpreter.file` `exit.file` `exit.interpreter.file` `link.file` `link.file.destination` `load_module.file` `mkdir.file` `mmap.file` `open.file` `process.ancestors.file` `process.ancestors.interpreter.file` `process.file` `process.interpreter.file` `process.parent.file` `process.parent.interpreter.file` `ptrace.tracee.ancestors.file` `ptrace.tracee.ancestors.interpreter.file` `ptrace.tracee.file` `ptrace.tracee.interpreter.file` `ptrace.tracee.parent.file` `ptrace.tracee.parent.interpreter.file` `removexattr.file` `rename.file` `rename.file.destination` `rmdir.file` `setrlimit.target.ancestors.file` `setrlimit.target.ancestors.interpreter.file` `setrlimit.target.file` `setrlimit.target.interpreter.file` `setrlimit.target.parent.file` `setrlimit.target.parent.interpreter.file` `setxattr.file` `signal.target.ancestors.file` `signal.target.ancestors.interpreter.file` `signal.target.file` `signal.target.interpreter.file` `signal.target.parent.file` `signal.target.parent.interpreter.file` `splice.file` `unlink.file` `utimes.file`

### `*.mount_id`{% #common-pathkey-mount_id-doc %}

Type: int

Definition: Mount ID of the file

`*.mount_id` has 60 possible prefixes: `cgroup_write.file` `chdir.file` `chmod.file` `chown.file` `exec.cgroup.file` `exec.file` `exec.interpreter.file` `exit.cgroup.file` `exit.file` `exit.interpreter.file` `link.file` `link.file.destination` `load_module.file` `mkdir.file` `mmap.file` `open.file` `process.ancestors.cgroup.file` `process.ancestors.file` `process.ancestors.interpreter.file` `process.cgroup.file` `process.file` `process.interpreter.file` `process.parent.cgroup.file` `process.parent.file` `process.parent.interpreter.file` `ptrace.tracee.ancestors.cgroup.file` `ptrace.tracee.ancestors.file` `ptrace.tracee.ancestors.interpreter.file` `ptrace.tracee.cgroup.file` `ptrace.tracee.file` `ptrace.tracee.interpreter.file` `ptrace.tracee.parent.cgroup.file` `ptrace.tracee.parent.file` `ptrace.tracee.parent.interpreter.file` `removexattr.file` `rename.file` `rename.file.destination` `rmdir.file` `setrlimit.target.ancestors.cgroup.file` `setrlimit.target.ancestors.file` `setrlimit.target.ancestors.interpreter.file` `setrlimit.target.cgroup.file` `setrlimit.target.file` `setrlimit.target.interpreter.file` `setrlimit.target.parent.cgroup.file` `setrlimit.target.parent.file` `setrlimit.target.parent.interpreter.file` `setxattr.file` `signal.target.ancestors.cgroup.file` `signal.target.ancestors.file` `signal.target.ancestors.interpreter.file` `signal.target.cgroup.file` `signal.target.file` `signal.target.interpreter.file` `signal.target.parent.cgroup.file` `signal.target.parent.file` `signal.target.parent.interpreter.file` `splice.file` `unlink.file` `utimes.file`

### `*.mount_visible`{% #common-fileevent-mount_visible-doc %}

Type: bool

Definition: Indicates whether the file's mount is visible in the VFS

`*.mount_visible` has 46 possible prefixes: `cgroup_write.file` `chdir.file` `chmod.file` `chown.file` `exec.file` `exec.interpreter.file` `exit.file` `exit.interpreter.file` `link.file` `link.file.destination` `load_module.file` `mkdir.file` `mmap.file` `open.file` `process.ancestors.file` `process.ancestors.interpreter.file` `process.file` `process.interpreter.file` `process.parent.file` `process.parent.interpreter.file` `ptrace.tracee.ancestors.file` `ptrace.tracee.ancestors.interpreter.file` `ptrace.tracee.file` `ptrace.tracee.interpreter.file` `ptrace.tracee.parent.file` `ptrace.tracee.parent.interpreter.file` `removexattr.file` `rename.file` `rename.file.destination` `rmdir.file` `setrlimit.target.ancestors.file` `setrlimit.target.ancestors.interpreter.file` `setrlimit.target.file` `setrlimit.target.interpreter.file` `setrlimit.target.parent.file` `setrlimit.target.parent.interpreter.file` `setxattr.file` `signal.target.ancestors.file` `signal.target.ancestors.interpreter.file` `signal.target.file` `signal.target.interpreter.file` `signal.target.parent.file` `signal.target.parent.interpreter.file` `splice.file` `unlink.file` `utimes.file`

### `*.name`{% #common-fileevent-name-doc %}

Type: string

Definition: File's basename

`*.name` has 46 possible prefixes: `cgroup_write.file` `chdir.file` `chmod.file` `chown.file` `exec.file` `exec.interpreter.file` `exit.file` `exit.interpreter.file` `link.file` `link.file.destination` `load_module.file` `mkdir.file` `mmap.file` `open.file` `process.ancestors.file` `process.ancestors.interpreter.file` `process.file` `process.interpreter.file` `process.parent.file` `process.parent.interpreter.file` `ptrace.tracee.ancestors.file` `ptrace.tracee.ancestors.interpreter.file` `ptrace.tracee.file` `ptrace.tracee.interpreter.file` `ptrace.tracee.parent.file` `ptrace.tracee.parent.interpreter.file` `removexattr.file` `rename.file` `rename.file.destination` `rmdir.file` `setrlimit.target.ancestors.file` `setrlimit.target.ancestors.interpreter.file` `setrlimit.target.file` `setrlimit.target.interpreter.file` `setrlimit.target.parent.file` `setrlimit.target.parent.interpreter.file` `setxattr.file` `signal.target.ancestors.file` `signal.target.ancestors.interpreter.file` `signal.target.file` `signal.target.interpreter.file` `signal.target.parent.file` `signal.target.parent.interpreter.file` `splice.file` `unlink.file` `utimes.file`

Example:

```javascript
exec.file.name == "apt"
```

Matches the execution of any file named apt.

### `*.network_direction`{% #common-networkcontext-network_direction-doc %}

Type: int

Definition: Network direction of the network packet

`*.network_direction` has 2 possible prefixes: `network` `packet`

Constants: Network directions

### `*.package.epoch`{% #common-fileevent-package-epoch-doc %}

Type: int

Definition: [Experimental] Epoch of the package that provided this file

`*.package.epoch` has 46 possible prefixes: `cgroup_write.file` `chdir.file` `chmod.file` `chown.file` `exec.file` `exec.interpreter.file` `exit.file` `exit.interpreter.file` `link.file` `link.file.destination` `load_module.file` `mkdir.file` `mmap.file` `open.file` `process.ancestors.file` `process.ancestors.interpreter.file` `process.file` `process.interpreter.file` `process.parent.file` `process.parent.interpreter.file` `ptrace.tracee.ancestors.file` `ptrace.tracee.ancestors.interpreter.file` `ptrace.tracee.file` `ptrace.tracee.interpreter.file` `ptrace.tracee.parent.file` `ptrace.tracee.parent.interpreter.file` `removexattr.file` `rename.file` `rename.file.destination` `rmdir.file` `setrlimit.target.ancestors.file` `setrlimit.target.ancestors.interpreter.file` `setrlimit.target.file` `setrlimit.target.interpreter.file` `setrlimit.target.parent.file` `setrlimit.target.parent.interpreter.file` `setxattr.file` `signal.target.ancestors.file` `signal.target.ancestors.interpreter.file` `signal.target.file` `signal.target.interpreter.file` `signal.target.parent.file` `signal.target.parent.interpreter.file` `splice.file` `unlink.file` `utimes.file`

### `*.package.name`{% #common-fileevent-package-name-doc %}

Type: string

Definition: [Experimental] Name of the package that provided this file

`*.package.name` has 46 possible prefixes: `cgroup_write.file` `chdir.file` `chmod.file` `chown.file` `exec.file` `exec.interpreter.file` `exit.file` `exit.interpreter.file` `link.file` `link.file.destination` `load_module.file` `mkdir.file` `mmap.file` `open.file` `process.ancestors.file` `process.ancestors.interpreter.file` `process.file` `process.interpreter.file` `process.parent.file` `process.parent.interpreter.file` `ptrace.tracee.ancestors.file` `ptrace.tracee.ancestors.interpreter.file` `ptrace.tracee.file` `ptrace.tracee.interpreter.file` `ptrace.tracee.parent.file` `ptrace.tracee.parent.interpreter.file` `removexattr.file` `rename.file` `rename.file.destination` `rmdir.file` `setrlimit.target.ancestors.file` `setrlimit.target.ancestors.interpreter.file` `setrlimit.target.file` `setrlimit.target.interpreter.file` `setrlimit.target.parent.file` `setrlimit.target.parent.interpreter.file` `setxattr.file` `signal.target.ancestors.file` `signal.target.ancestors.interpreter.file` `signal.target.file` `signal.target.interpreter.file` `signal.target.parent.file` `signal.target.parent.interpreter.file` `splice.file` `unlink.file` `utimes.file`

### `*.package.release`{% #common-fileevent-package-release-doc %}

Type: string

Definition: [Experimental] Release of the package that provided this file

`*.package.release` has 46 possible prefixes: `cgroup_write.file` `chdir.file` `chmod.file` `chown.file` `exec.file` `exec.interpreter.file` `exit.file` `exit.interpreter.file` `link.file` `link.file.destination` `load_module.file` `mkdir.file` `mmap.file` `open.file` `process.ancestors.file` `process.ancestors.interpreter.file` `process.file` `process.interpreter.file` `process.parent.file` `process.parent.interpreter.file` `ptrace.tracee.ancestors.file` `ptrace.tracee.ancestors.interpreter.file` `ptrace.tracee.file` `ptrace.tracee.interpreter.file` `ptrace.tracee.parent.file` `ptrace.tracee.parent.interpreter.file` `removexattr.file` `rename.file` `rename.file.destination` `rmdir.file` `setrlimit.target.ancestors.file` `setrlimit.target.ancestors.interpreter.file` `setrlimit.target.file` `setrlimit.target.interpreter.file` `setrlimit.target.parent.file` `setrlimit.target.parent.interpreter.file` `setxattr.file` `signal.target.ancestors.file` `signal.target.ancestors.interpreter.file` `signal.target.file` `signal.target.interpreter.file` `signal.target.parent.file` `signal.target.parent.interpreter.file` `splice.file` `unlink.file` `utimes.file`

### `*.package.source_epoch`{% #common-fileevent-package-source_epoch-doc %}

Type: int

Definition: [Experimental] Epoch of the source package of the package that provided this file

`*.package.source_epoch` has 46 possible prefixes: `cgroup_write.file` `chdir.file` `chmod.file` `chown.file` `exec.file` `exec.interpreter.file` `exit.file` `exit.interpreter.file` `link.file` `link.file.destination` `load_module.file` `mkdir.file` `mmap.file` `open.file` `process.ancestors.file` `process.ancestors.interpreter.file` `process.file` `process.interpreter.file` `process.parent.file` `process.parent.interpreter.file` `ptrace.tracee.ancestors.file` `ptrace.tracee.ancestors.interpreter.file` `ptrace.tracee.file` `ptrace.tracee.interpreter.file` `ptrace.tracee.parent.file` `ptrace.tracee.parent.interpreter.file` `removexattr.file` `rename.file` `rename.file.destination` `rmdir.file` `setrlimit.target.ancestors.file` `setrlimit.target.ancestors.interpreter.file` `setrlimit.target.file` `setrlimit.target.interpreter.file` `setrlimit.target.parent.file` `setrlimit.target.parent.interpreter.file` `setxattr.file` `signal.target.ancestors.file` `signal.target.ancestors.interpreter.file` `signal.target.file` `signal.target.interpreter.file` `signal.target.parent.file` `signal.target.parent.interpreter.file` `splice.file` `unlink.file` `utimes.file`

### `*.package.source_release`{% #common-fileevent-package-source_release-doc %}

Type: string

Definition: [Experimental] Release of the source package of the package that provided this file

`*.package.source_release` has 46 possible prefixes: `cgroup_write.file` `chdir.file` `chmod.file` `chown.file` `exec.file` `exec.interpreter.file` `exit.file` `exit.interpreter.file` `link.file` `link.file.destination` `load_module.file` `mkdir.file` `mmap.file` `open.file` `process.ancestors.file` `process.ancestors.interpreter.file` `process.file` `process.interpreter.file` `process.parent.file` `process.parent.interpreter.file` `ptrace.tracee.ancestors.file` `ptrace.tracee.ancestors.interpreter.file` `ptrace.tracee.file` `ptrace.tracee.interpreter.file` `ptrace.tracee.parent.file` `ptrace.tracee.parent.interpreter.file` `removexattr.file` `rename.file` `rename.file.destination` `rmdir.file` `setrlimit.target.ancestors.file` `setrlimit.target.ancestors.interpreter.file` `setrlimit.target.file` `setrlimit.target.interpreter.file` `setrlimit.target.parent.file` `setrlimit.target.parent.interpreter.file` `setxattr.file` `signal.target.ancestors.file` `signal.target.ancestors.interpreter.file` `signal.target.file` `signal.target.interpreter.file` `signal.target.parent.file` `signal.target.parent.interpreter.file` `splice.file` `unlink.file` `utimes.file`

### `*.package.source_version`{% #common-fileevent-package-source_version-doc %}

Type: string

Definition: [Experimental] Full version of the source package of the package that provided this file

`*.package.source_version` has 46 possible prefixes: `cgroup_write.file` `chdir.file` `chmod.file` `chown.file` `exec.file` `exec.interpreter.file` `exit.file` `exit.interpreter.file` `link.file` `link.file.destination` `load_module.file` `mkdir.file` `mmap.file` `open.file` `process.ancestors.file` `process.ancestors.interpreter.file` `process.file` `process.interpreter.file` `process.parent.file` `process.parent.interpreter.file` `ptrace.tracee.ancestors.file` `ptrace.tracee.ancestors.interpreter.file` `ptrace.tracee.file` `ptrace.tracee.interpreter.file` `ptrace.tracee.parent.file` `ptrace.tracee.parent.interpreter.file` `removexattr.file` `rename.file` `rename.file.destination` `rmdir.file` `setrlimit.target.ancestors.file` `setrlimit.target.ancestors.interpreter.file` `setrlimit.target.file` `setrlimit.target.interpreter.file` `setrlimit.target.parent.file` `setrlimit.target.parent.interpreter.file` `setxattr.file` `signal.target.ancestors.file` `signal.target.ancestors.interpreter.file` `signal.target.file` `signal.target.interpreter.file` `signal.target.parent.file` `signal.target.parent.interpreter.file` `splice.file` `unlink.file` `utimes.file`

### `*.package.version`{% #common-fileevent-package-version-doc %}

Type: string

Definition: [Experimental] Full version of the package that provided this file

`*.package.version` has 46 possible prefixes: `cgroup_write.file` `chdir.file` `chmod.file` `chown.file` `exec.file` `exec.interpreter.file` `exit.file` `exit.interpreter.file` `link.file` `link.file.destination` `load_module.file` `mkdir.file` `mmap.file` `open.file` `process.ancestors.file` `process.ancestors.interpreter.file` `process.file` `process.interpreter.file` `process.parent.file` `process.parent.interpreter.file` `ptrace.tracee.ancestors.file` `ptrace.tracee.ancestors.interpreter.file` `ptrace.tracee.file` `ptrace.tracee.interpreter.file` `ptrace.tracee.parent.file` `ptrace.tracee.parent.interpreter.file` `removexattr.file` `rename.file` `rename.file.destination` `rmdir.file` `setrlimit.target.ancestors.file` `setrlimit.target.ancestors.interpreter.file` `setrlimit.target.file` `setrlimit.target.interpreter.file` `setrlimit.target.parent.file` `setrlimit.target.parent.interpreter.file` `setxattr.file` `signal.target.ancestors.file` `signal.target.ancestors.interpreter.file` `signal.target.file` `signal.target.interpreter.file` `signal.target.parent.file` `signal.target.parent.interpreter.file` `splice.file` `unlink.file` `utimes.file`

### `*.packet_count`{% #common-networkstats-packet_count-doc %}

Type: int

Definition: Count of network packets transmitted or received

`*.packet_count` has 2 possible prefixes: `network_flow_monitor.flows.egress` `network_flow_monitor.flows.ingress`

### `*.path`{% #common-fileevent-path-doc %}

Type: string

Definition: File's path

`*.path` has 46 possible prefixes: `cgroup_write.file` `chdir.file` `chmod.file` `chown.file` `exec.file` `exec.interpreter.file` `exit.file` `exit.interpreter.file` `link.file` `link.file.destination` `load_module.file` `mkdir.file` `mmap.file` `open.file` `process.ancestors.file` `process.ancestors.interpreter.file` `process.file` `process.interpreter.file` `process.parent.file` `process.parent.interpreter.file` `ptrace.tracee.ancestors.file` `ptrace.tracee.ancestors.interpreter.file` `ptrace.tracee.file` `ptrace.tracee.interpreter.file` `ptrace.tracee.parent.file` `ptrace.tracee.parent.interpreter.file` `removexattr.file` `rename.file` `rename.file.destination` `rmdir.file` `setrlimit.target.ancestors.file` `setrlimit.target.ancestors.interpreter.file` `setrlimit.target.file` `setrlimit.target.interpreter.file` `setrlimit.target.parent.file` `setrlimit.target.parent.interpreter.file` `setxattr.file` `signal.target.ancestors.file` `signal.target.ancestors.interpreter.file` `signal.target.file` `signal.target.interpreter.file` `signal.target.parent.file` `signal.target.parent.interpreter.file` `splice.file` `unlink.file` `utimes.file`

Example:

```javascript
exec.file.path == "/usr/bin/apt"
```

Matches the execution of the file located at /usr/bin/apt

Example:

```javascript
open.file.path == "/etc/passwd"
```

Matches any process opening the /etc/passwd file.

### `*.pid`{% #common-pidcontext-pid-doc %}

Type: int

Definition: Process ID of the process (also called thread group ID)

`*.pid` has 14 possible prefixes: `exec` `exit` `process` `process.ancestors` `process.parent` `ptrace.tracee` `ptrace.tracee.ancestors` `ptrace.tracee.parent` `setrlimit.target` `setrlimit.target.ancestors` `setrlimit.target.parent` `signal.target` `signal.target.ancestors` `signal.target.parent`

### `*.port`{% #common-ipportcontext-port-doc %}

Type: int

Definition: Port number

`*.port` has 9 possible prefixes: `accept.addr` `bind.addr` `connect.addr` `network.destination` `network.source` `network_flow_monitor.flows.destination` `network_flow_monitor.flows.source` `packet.destination` `packet.source`

### `*.ppid`{% #common-process-ppid-doc %}

Type: int

Definition: Parent process ID

`*.ppid` has 14 possible prefixes: `exec` `exit` `process` `process.ancestors` `process.parent` `ptrace.tracee` `ptrace.tracee.ancestors` `ptrace.tracee.parent` `setrlimit.target` `setrlimit.target.ancestors` `setrlimit.target.parent` `signal.target` `signal.target.ancestors` `signal.target.parent`

### `*.retval`{% #common-syscallevent-retval-doc %}

Type: int

Definition: Return value of the syscall

`*.retval` has 27 possible prefixes: `accept` `bind` `bpf` `chdir` `chmod` `chown` `connect` `link` `load_module` `mkdir` `mmap` `mount` `mprotect` `open` `prctl` `ptrace` `removexattr` `rename` `rmdir` `setrlimit` `setsockopt` `setxattr` `signal` `splice` `unlink` `unload_module` `utimes`

Constants: Error constants

### `*.rights`{% #common-filefields-rights-doc %}

Type: int

Definition: Rights of the file

`*.rights` has 46 possible prefixes: `cgroup_write.file` `chdir.file` `chmod.file` `chown.file` `exec.file` `exec.interpreter.file` `exit.file` `exit.interpreter.file` `link.file` `link.file.destination` `load_module.file` `mkdir.file` `mmap.file` `open.file` `process.ancestors.file` `process.ancestors.interpreter.file` `process.file` `process.interpreter.file` `process.parent.file` `process.parent.interpreter.file` `ptrace.tracee.ancestors.file` `ptrace.tracee.ancestors.interpreter.file` `ptrace.tracee.file` `ptrace.tracee.interpreter.file` `ptrace.tracee.parent.file` `ptrace.tracee.parent.interpreter.file` `removexattr.file` `rename.file` `rename.file.destination` `rmdir.file` `setrlimit.target.ancestors.file` `setrlimit.target.ancestors.interpreter.file` `setrlimit.target.file` `setrlimit.target.interpreter.file` `setrlimit.target.parent.file` `setrlimit.target.parent.interpreter.file` `setxattr.file` `signal.target.ancestors.file` `signal.target.ancestors.interpreter.file` `signal.target.file` `signal.target.interpreter.file` `signal.target.parent.file` `signal.target.parent.interpreter.file` `splice.file` `unlink.file` `utimes.file`

Constants: File mode constants

### `*.session_type`{% #common-usersessioncontext-session_type-doc %}

Type: int

Definition: Type of the user session

`*.session_type` has 14 possible prefixes: `exec.user_session` `exit.user_session` `process.ancestors.user_session` `process.parent.user_session` `process.user_session` `ptrace.tracee.ancestors.user_session` `ptrace.tracee.parent.user_session` `ptrace.tracee.user_session` `setrlimit.target.ancestors.user_session` `setrlimit.target.parent.user_session` `setrlimit.target.user_session` `signal.target.ancestors.user_session` `signal.target.parent.user_session` `signal.target.user_session`

### `*.size`{% #common-networkcontext-size-doc %}

Type: int

Definition: Size in bytes of the network packet

`*.size` has 2 possible prefixes: `network` `packet`

### `*.ssh_auth_method`{% #common-sshsessioncontext-ssh_auth_method-doc %}

Type: int

Definition: SSH authentication method used by the user

`*.ssh_auth_method` has 14 possible prefixes: `exec.user_session` `exit.user_session` `process.ancestors.user_session` `process.parent.user_session` `process.user_session` `ptrace.tracee.ancestors.user_session` `ptrace.tracee.parent.user_session` `ptrace.tracee.user_session` `setrlimit.target.ancestors.user_session` `setrlimit.target.parent.user_session` `setrlimit.target.user_session` `signal.target.ancestors.user_session` `signal.target.parent.user_session` `signal.target.user_session`

Constants: SSHAuthMethod

### `*.ssh_client_ip`{% #common-sshsessioncontext-ssh_client_ip-doc %}

Type: IP/CIDR

Definition: SSH client IP of the user that executed the process

`*.ssh_client_ip` has 14 possible prefixes: `exec.user_session` `exit.user_session` `process.ancestors.user_session` `process.parent.user_session` `process.user_session` `ptrace.tracee.ancestors.user_session` `ptrace.tracee.parent.user_session` `ptrace.tracee.user_session` `setrlimit.target.ancestors.user_session` `setrlimit.target.parent.user_session` `setrlimit.target.user_session` `signal.target.ancestors.user_session` `signal.target.parent.user_session` `signal.target.user_session`

### `*.ssh_client_port`{% #common-sshsessioncontext-ssh_client_port-doc %}

Type: int

Definition: SSH client port of the user that executed the process

`*.ssh_client_port` has 14 possible prefixes: `exec.user_session` `exit.user_session` `process.ancestors.user_session` `process.parent.user_session` `process.user_session` `ptrace.tracee.ancestors.user_session` `ptrace.tracee.parent.user_session` `ptrace.tracee.user_session` `setrlimit.target.ancestors.user_session` `setrlimit.target.parent.user_session` `setrlimit.target.user_session` `signal.target.ancestors.user_session` `signal.target.parent.user_session` `signal.target.user_session`

### `*.ssh_public_key`{% #common-sshsessioncontext-ssh_public_key-doc %}

Type: string

Definition: SSH public key used for authentication (if applicable)

`*.ssh_public_key` has 14 possible prefixes: `exec.user_session` `exit.user_session` `process.ancestors.user_session` `process.parent.user_session` `process.user_session` `ptrace.tracee.ancestors.user_session` `ptrace.tracee.parent.user_session` `ptrace.tracee.user_session` `setrlimit.target.ancestors.user_session` `setrlimit.target.parent.user_session` `setrlimit.target.user_session` `signal.target.ancestors.user_session` `signal.target.parent.user_session` `signal.target.user_session`

### `*.ssh_session_id`{% #common-sshsessioncontext-ssh_session_id-doc %}

Type: int

Definition: Unique identifier of the SSH user session on the host

`*.ssh_session_id` has 14 possible prefixes: `exec.user_session` `exit.user_session` `process.ancestors.user_session` `process.parent.user_session` `process.user_session` `ptrace.tracee.ancestors.user_session` `ptrace.tracee.parent.user_session` `ptrace.tracee.user_session` `setrlimit.target.ancestors.user_session` `setrlimit.target.parent.user_session` `setrlimit.target.user_session` `signal.target.ancestors.user_session` `signal.target.parent.user_session` `signal.target.user_session`

### `*.tags`{% #common-containercontext-tags-doc %}

Type: string

Definition: Tags of the container

`*.tags` has 14 possible prefixes: `exec.container` `exit.container` `process.ancestors.container` `process.container` `process.parent.container` `ptrace.tracee.ancestors.container` `ptrace.tracee.container` `ptrace.tracee.parent.container` `setrlimit.target.ancestors.container` `setrlimit.target.container` `setrlimit.target.parent.container` `signal.target.ancestors.container` `signal.target.container` `signal.target.parent.container`

### `*.tid`{% #common-pidcontext-tid-doc %}

Type: int

Definition: Thread ID of the thread

`*.tid` has 14 possible prefixes: `exec` `exit` `process` `process.ancestors` `process.parent` `ptrace.tracee` `ptrace.tracee.ancestors` `ptrace.tracee.parent` `setrlimit.target` `setrlimit.target.ancestors` `setrlimit.target.parent` `signal.target` `signal.target.ancestors` `signal.target.parent`

### `*.tty_name`{% #common-process-tty_name-doc %}

Type: string

Definition: Name of the TTY associated with the process

`*.tty_name` has 14 possible prefixes: `exec` `exit` `process` `process.ancestors` `process.parent` `ptrace.tracee` `ptrace.tracee.ancestors` `ptrace.tracee.parent` `setrlimit.target` `setrlimit.target.ancestors` `setrlimit.target.parent` `signal.target` `signal.target.ancestors` `signal.target.parent`

### `*.type`{% #common-networkcontext-type-doc %}

Type: int

Definition: Type of the network packet

`*.type` has 2 possible prefixes: `network` `packet`

Constants: Network Protocol Types

### `*.uid`{% #common-credentials-uid-doc %}

Type: int

Definition: UID of the process

`*.uid` has 14 possible prefixes: `exec` `exit` `process` `process.ancestors` `process.parent` `ptrace.tracee` `ptrace.tracee.ancestors` `ptrace.tracee.parent` `setrlimit.target` `setrlimit.target.ancestors` `setrlimit.target.parent` `signal.target` `signal.target.ancestors` `signal.target.parent`

### `*.uid`{% #common-filefields-uid-doc %}

Type: int

Definition: UID of the file's owner

`*.uid` has 46 possible prefixes: `cgroup_write.file` `chdir.file` `chmod.file` `chown.file` `exec.file` `exec.interpreter.file` `exit.file` `exit.interpreter.file` `link.file` `link.file.destination` `load_module.file` `mkdir.file` `mmap.file` `open.file` `process.ancestors.file` `process.ancestors.interpreter.file` `process.file` `process.interpreter.file` `process.parent.file` `process.parent.interpreter.file` `ptrace.tracee.ancestors.file` `ptrace.tracee.ancestors.interpreter.file` `ptrace.tracee.file` `ptrace.tracee.interpreter.file` `ptrace.tracee.parent.file` `ptrace.tracee.parent.interpreter.file` `removexattr.file` `rename.file` `rename.file.destination` `rmdir.file` `setrlimit.target.ancestors.file` `setrlimit.target.ancestors.interpreter.file` `setrlimit.target.file` `setrlimit.target.interpreter.file` `setrlimit.target.parent.file` `setrlimit.target.parent.interpreter.file` `setxattr.file` `signal.target.ancestors.file` `signal.target.ancestors.interpreter.file` `signal.target.file` `signal.target.interpreter.file` `signal.target.parent.file` `signal.target.parent.interpreter.file` `splice.file` `unlink.file` `utimes.file`

### `*.user`{% #common-credentials-user-doc %}

Type: string

Definition: User of the process

`*.user` has 14 possible prefixes: `exec` `exit` `process` `process.ancestors` `process.parent` `ptrace.tracee` `ptrace.tracee.ancestors` `ptrace.tracee.parent` `setrlimit.target` `setrlimit.target.ancestors` `setrlimit.target.parent` `signal.target` `signal.target.ancestors` `signal.target.parent`

Example:

```javascript
process.user == "root"
```

Constrain an event to be triggered by a process running as the root user.

### `*.user`{% #common-filefields-user-doc %}

Type: string

Definition: User of the file's owner

`*.user` has 46 possible prefixes: `cgroup_write.file` `chdir.file` `chmod.file` `chown.file` `exec.file` `exec.interpreter.file` `exit.file` `exit.interpreter.file` `link.file` `link.file.destination` `load_module.file` `mkdir.file` `mmap.file` `open.file` `process.ancestors.file` `process.ancestors.interpreter.file` `process.file` `process.interpreter.file` `process.parent.file` `process.parent.interpreter.file` `ptrace.tracee.ancestors.file` `ptrace.tracee.ancestors.interpreter.file` `ptrace.tracee.file` `ptrace.tracee.interpreter.file` `ptrace.tracee.parent.file` `ptrace.tracee.parent.interpreter.file` `removexattr.file` `rename.file` `rename.file.destination` `rmdir.file` `setrlimit.target.ancestors.file` `setrlimit.target.ancestors.interpreter.file` `setrlimit.target.file` `setrlimit.target.interpreter.file` `setrlimit.target.parent.file` `setrlimit.target.parent.interpreter.file` `setxattr.file` `signal.target.ancestors.file` `signal.target.ancestors.interpreter.file` `signal.target.file` `signal.target.interpreter.file` `signal.target.parent.file` `signal.target.parent.interpreter.file` `splice.file` `unlink.file` `utimes.file`

### `*.version`{% #common-cgroupcontext-version-doc %}

Type: int

Definition: [Experimental] Version of the cgroup API

`*.version` has 14 possible prefixes: `exec.cgroup` `exit.cgroup` `process.ancestors.cgroup` `process.cgroup` `process.parent.cgroup` `ptrace.tracee.ancestors.cgroup` `ptrace.tracee.cgroup` `ptrace.tracee.parent.cgroup` `setrlimit.target.ancestors.cgroup` `setrlimit.target.cgroup` `setrlimit.target.parent.cgroup` `signal.target.ancestors.cgroup` `signal.target.cgroup` `signal.target.parent.cgroup`

### `accept.addr.family`{% #accept-addr-family-doc %}

Type: int

Definition: Address family

### `accept.addr.hostname`{% #accept-addr-hostname-doc %}

Type: string

Definition: Address hostname (if available)

### `bind.addr.family`{% #bind-addr-family-doc %}

Type: int

Definition: Address family

### `bind.protocol`{% #bind-protocol-doc %}

Type: int

Definition: Socket Protocol

### `bpf.cmd`{% #bpf-cmd-doc %}

Type: int

Definition: BPF command name

Constants: BPF commands

### `bpf.map.name`{% #bpf-map-name-doc %}

Type: string

Definition: Name of the eBPF map (added in 7.35)

### `bpf.map.type`{% #bpf-map-type-doc %}

Type: int

Definition: Type of the eBPF map

Constants: BPF map types

### `bpf.prog.attach_type`{% #bpf-prog-attach_type-doc %}

Type: int

Definition: Attach type of the eBPF program

Constants: BPF attach types

### `bpf.prog.helpers`{% #bpf-prog-helpers-doc %}

Type: int

Definition: eBPF helpers used by the eBPF program (added in 7.35)

Constants: BPF helper functions

### `bpf.prog.name`{% #bpf-prog-name-doc %}

Type: string

Definition: Name of the eBPF program (added in 7.35)

### `bpf.prog.tag`{% #bpf-prog-tag-doc %}

Type: string

Definition: Hash (sha1) of the eBPF program (added in 7.35)

### `bpf.prog.type`{% #bpf-prog-type-doc %}

Type: int

Definition: Type of the eBPF program

Constants: BPF program types

### `capabilities.attempted`{% #capabilities-attempted-doc %}

Type: int

Definition: Bitmask of the capabilities that the process attempted to use since it started running

Constants: Kernel Capability constants

### `capabilities.used`{% #capabilities-used-doc %}

Type: int

Definition: Bitmask of the capabilities that the process successfully used since it started running

Constants: Kernel Capability constants

### `capset.cap_effective`{% #capset-cap_effective-doc %}

Type: int

Definition: Effective capability set of the process

Constants: Kernel Capability constants

### `capset.cap_permitted`{% #capset-cap_permitted-doc %}

Type: int

Definition: Permitted capability set of the process

Constants: Kernel Capability constants

### `cgroup_write.pid`{% #cgroup_write-pid-doc %}

Type: int

Definition: PID of the process added to the cgroup

### `chdir.syscall.path`{% #chdir-syscall-path-doc %}

Type: string

Definition: path argument of the syscall

### `chmod.file.destination.mode`{% #chmod-file-destination-mode-doc %}

Type: int

Definition: New mode of the chmod-ed file

Constants: File mode constants

### `chmod.file.destination.rights`{% #chmod-file-destination-rights-doc %}

Type: int

Definition: New rights of the chmod-ed file

Constants: File mode constants

### `chmod.syscall.mode`{% #chmod-syscall-mode-doc %}

Type: int

Definition: mode argument of the syscall

### `chmod.syscall.path`{% #chmod-syscall-path-doc %}

Type: string

Definition: path argument of the syscall

### `chown.file.destination.gid`{% #chown-file-destination-gid-doc %}

Type: int

Definition: New GID of the chown-ed file's owner

### `chown.file.destination.group`{% #chown-file-destination-group-doc %}

Type: string

Definition: New group of the chown-ed file's owner

### `chown.file.destination.uid`{% #chown-file-destination-uid-doc %}

Type: int

Definition: New UID of the chown-ed file's owner

### `chown.file.destination.user`{% #chown-file-destination-user-doc %}

Type: string

Definition: New user of the chown-ed file's owner

### `chown.syscall.gid`{% #chown-syscall-gid-doc %}

Type: int

Definition: GID argument of the syscall

### `chown.syscall.path`{% #chown-syscall-path-doc %}

Type: string

Definition: Path argument of the syscall

### `chown.syscall.uid`{% #chown-syscall-uid-doc %}

Type: int

Definition: UID argument of the syscall

### `connect.addr.family`{% #connect-addr-family-doc %}

Type: int

Definition: Address family

### `connect.addr.hostname`{% #connect-addr-hostname-doc %}

Type: string

Definition: Address hostname (if available)

### `connect.protocol`{% #connect-protocol-doc %}

Type: int

Definition: Socket Protocol

### `dns.id`{% #dns-id-doc %}

Type: int

Definition: [Experimental] the DNS request ID

### `dns.question.class`{% #dns-question-class-doc %}

Type: int

Definition: the class looked up by the DNS question

Constants: DNS qclasses

### `dns.question.count`{% #dns-question-count-doc %}

Type: int

Definition: the total count of questions in the DNS request

### `dns.question.length`{% #dns-question-length-doc %}

Type: int

Definition: the total DNS request size in bytes

### `dns.question.name`{% #dns-question-name-doc %}

Type: string

Definition: the queried domain name

### `dns.question.type`{% #dns-question-type-doc %}

Type: int

Definition: a two octet code which specifies the DNS question type

Constants: DNS qtypes

### `dns.response.code`{% #dns-response-code-doc %}

Type: int

Definition: Response code of the DNS response according to RFC 1035

Constants: DNS Responses

### `event.async`{% #event-async-doc %}

Type: bool

Definition: True if the syscall was asynchronous

### `event.hostname`{% #event-hostname-doc %}

Type: string

Definition: Hostname associated with the event

### `event.origin`{% #event-origin-doc %}

Type: string

Definition: Origin of the event

### `event.os`{% #event-os-doc %}

Type: string

Definition: Operating system of the event

### `event.rule.tags`{% #event-rule-tags-doc %}

Type: string

Definition: Tags associated with the rule that's used to evaluate the event

### `event.service`{% #event-service-doc %}

Type: string

Definition: Service associated with the event

### `event.signature`{% #event-signature-doc %}

Type: string

Definition: Signature of the process pid and its cgroup with agent secret key

### `event.source`{% #event-source-doc %}

Type: string

Definition: [Experimental] Source of the event. Can be either 'runtime' or 'snapshot'.

### `event.timestamp`{% #event-timestamp-doc %}

Type: int

Definition: Timestamp of the event

### `exec.file.metadata.abi`{% #exec-file-metadata-abi-doc %}

Type: int

Definition: [Experimental] ABI of the file (only for executable files)

Constants: ABI

### `exec.file.metadata.architecture`{% #exec-file-metadata-architecture-doc %}

Type: int

Definition: [Experimental] Architecture of the file (only for executable files)

Constants: Architecture

### `exec.file.metadata.compression`{% #exec-file-metadata-compression-doc %}

Type: int

Definition: [Experimental] Compression type of the file (only for compressed files)

Constants: CompressionType

### `exec.file.metadata.is_executable`{% #exec-file-metadata-is_executable-doc %}

Type: bool

Definition: [Experimental] Tells if the file is executable or not

### `exec.file.metadata.is_garble_obfuscated`{% #exec-file-metadata-is_garble_obfuscated-doc %}

Type: bool

Definition: [Experimental] Tells if the binary has been obfuscated using garble

### `exec.file.metadata.is_upx_packed`{% #exec-file-metadata-is_upx_packed-doc %}

Type: bool

Definition: [Experimental] Tells if the binary has been packed using UPX

### `exec.file.metadata.size`{% #exec-file-metadata-size-doc %}

Type: int

Definition: [Experimental] Size of the file

### `exec.file.metadata.type`{% #exec-file-metadata-type-doc %}

Type: int

Definition: [Experimental] Type of the file

Constants: FileType

### `exec.syscall.path`{% #exec-syscall-path-doc %}

Type: string

Definition: path argument of the syscall

### `exit.cause`{% #exit-cause-doc %}

Type: int

Definition: Cause of the process termination (one of EXITED, SIGNALED, COREDUMPED)

### `exit.code`{% #exit-code-doc %}

Type: int

Definition: Exit code of the process or number of the signal that caused the process to terminate

### `imds.aws.is_imds_v2`{% #imds-aws-is_imds_v2-doc %}

Type: bool

Definition: a boolean which specifies if the IMDS event follows IMDSv1 or IMDSv2 conventions

### `imds.aws.security_credentials.type`{% #imds-aws-security_credentials-type-doc %}

Type: string

Definition: the security credentials type

### `imds.cloud_provider`{% #imds-cloud_provider-doc %}

Type: string

Definition: the intended cloud provider of the IMDS event

### `imds.host`{% #imds-host-doc %}

Type: string

Definition: the host of the HTTP protocol

### `imds.server`{% #imds-server-doc %}

Type: string

Definition: the server header of a response

### `imds.type`{% #imds-type-doc %}

Type: string

Definition: the type of IMDS event

### `imds.url`{% #imds-url-doc %}

Type: string

Definition: the queried IMDS URL

### `imds.user_agent`{% #imds-user_agent-doc %}

Type: string

Definition: the user agent of the HTTP client

### `link.syscall.destination.path`{% #link-syscall-destination-path-doc %}

Type: string

Definition: Destination path argument of the syscall

### `link.syscall.path`{% #link-syscall-path-doc %}

Type: string

Definition: Path argument of the syscall

### `load_module.args`{% #load_module-args-doc %}

Type: string

Definition: Parameters (as a string) of the new kernel module

### `load_module.args_truncated`{% #load_module-args_truncated-doc %}

Type: bool

Definition: Indicates if the arguments were truncated or not

### `load_module.argv`{% #load_module-argv-doc %}

Type: string

Definition: Parameters (as an array) of the new kernel module

### `load_module.loaded_from_memory`{% #load_module-loaded_from_memory-doc %}

Type: bool

Definition: Indicates if the kernel module was loaded from memory

### `load_module.name`{% #load_module-name-doc %}

Type: string

Definition: Name of the new kernel module

### `mkdir.file.destination.mode`{% #mkdir-file-destination-mode-doc %}

Type: int

Definition: Mode of the new directory

Constants: File mode constants

### `mkdir.file.destination.rights`{% #mkdir-file-destination-rights-doc %}

Type: int

Definition: Rights of the new directory

Constants: File mode constants

### `mkdir.syscall.mode`{% #mkdir-syscall-mode-doc %}

Type: int

Definition: Mode of the new directory

### `mkdir.syscall.path`{% #mkdir-syscall-path-doc %}

Type: string

Definition: Path argument of the syscall

### `mmap.flags`{% #mmap-flags-doc %}

Type: int

Definition: memory segment flags

Constants: MMap flags

### `mmap.protection`{% #mmap-protection-doc %}

Type: int

Definition: memory segment protection

Constants: Protection constants

### `mount.detached`{% #mount-detached-doc %}

Type: bool

Definition: Mount is detached from the VFS

### `mount.fs_type`{% #mount-fs_type-doc %}

Type: string

Definition: Type of the mounted file system

### `mount.mountpoint.path`{% #mount-mountpoint-path-doc %}

Type: string

Definition: Path of the mount point

### `mount.root.path`{% #mount-root-path-doc %}

Type: string

Definition: Root path of the mount

### `mount.source.path`{% #mount-source-path-doc %}

Type: string

Definition: Source path of a bind mount

### `mount.syscall.fs_type`{% #mount-syscall-fs_type-doc %}

Type: string

Definition: File system type argument of the syscall

### `mount.syscall.mountpoint.path`{% #mount-syscall-mountpoint-path-doc %}

Type: string

Definition: Mount point path argument of the syscall

### `mount.syscall.source.path`{% #mount-syscall-source-path-doc %}

Type: string

Definition: Source path argument of the syscall

### `mount.visible`{% #mount-visible-doc %}

Type: bool

Definition: Mount is not visible in the VFS

### `mprotect.req_protection`{% #mprotect-req_protection-doc %}

Type: int

Definition: new memory segment protection

Constants: Virtual Memory flags

### `mprotect.vm_protection`{% #mprotect-vm_protection-doc %}

Type: int

Definition: initial memory segment protection

Constants: Virtual Memory flags

### `network_flow_monitor.flows.l3_protocol`{% #network_flow_monitor-flows-l3_protocol-doc %}

Type: int

Definition: L3 protocol of the network packet

Constants: L3 protocols

### `network_flow_monitor.flows.l4_protocol`{% #network_flow_monitor-flows-l4_protocol-doc %}

Type: int

Definition: L4 protocol of the network packet

Constants: L4 protocols

### `open.file.destination.mode`{% #open-file-destination-mode-doc %}

Type: int

Definition: Mode of the created file

Constants: File mode constants

### `open.flags`{% #open-flags-doc %}

Type: int

Definition: Flags used when opening the file

Constants: Open flags

### `open.syscall.flags`{% #open-syscall-flags-doc %}

Type: int

Definition: Flags argument of the syscall

### `open.syscall.mode`{% #open-syscall-mode-doc %}

Type: int

Definition: Mode argument of the syscall

### `open.syscall.path`{% #open-syscall-path-doc %}

Type: string

Definition: Path argument of the syscall

### `packet.filter`{% #packet-filter-doc %}

Type: string

Definition: pcap filter expression

### `packet.tls.version`{% #packet-tls-version-doc %}

Type: int

Definition: TLS version

### `prctl.is_name_truncated`{% #prctl-is_name_truncated-doc %}

Type: bool

Definition: Indicates that the name field is truncated

### `prctl.new_name`{% #prctl-new_name-doc %}

Type: string

Definition: New name of the process

### `prctl.option`{% #prctl-option-doc %}

Type: int

Definition: prctl option

### `ptrace.request`{% #ptrace-request-doc %}

Type: int

Definition: ptrace request

Constants: Ptrace constants

### `rename.syscall.destination.path`{% #rename-syscall-destination-path-doc %}

Type: string

Definition: Destination path argument of the syscall

### `rename.syscall.path`{% #rename-syscall-path-doc %}

Type: string

Definition: Path argument of the syscall

### `rmdir.syscall.path`{% #rmdir-syscall-path-doc %}

Type: string

Definition: Path argument of the syscall

### `selinux.bool.name`{% #selinux-bool-name-doc %}

Type: string

Definition: SELinux boolean name

### `selinux.bool.state`{% #selinux-bool-state-doc %}

Type: string

Definition: SELinux boolean new value

### `selinux.bool_commit.state`{% #selinux-bool_commit-state-doc %}

Type: bool

Definition: Indicator of a SELinux boolean commit operation

### `selinux.enforce.status`{% #selinux-enforce-status-doc %}

Type: string

Definition: SELinux enforcement status (one of "enforcing", "permissive", "disabled")

### `setgid.egid`{% #setgid-egid-doc %}

Type: int

Definition: New effective GID of the process

### `setgid.egroup`{% #setgid-egroup-doc %}

Type: string

Definition: New effective group of the process

### `setgid.fsgid`{% #setgid-fsgid-doc %}

Type: int

Definition: New FileSystem GID of the process

### `setgid.fsgroup`{% #setgid-fsgroup-doc %}

Type: string

Definition: New FileSystem group of the process

### `setgid.gid`{% #setgid-gid-doc %}

Type: int

Definition: New GID of the process

### `setgid.group`{% #setgid-group-doc %}

Type: string

Definition: New group of the process

### `setrlimit.resource`{% #setrlimit-resource-doc %}

Type: int

Definition: Resource type being limited

Constants: Resource limit types

### `setrlimit.rlim_cur`{% #setrlimit-rlim_cur-doc %}

Type: int

Definition: Current (soft) limit value

### `setrlimit.rlim_max`{% #setrlimit-rlim_max-doc %}

Type: int

Definition: Maximum (hard) limit value

### `setsockopt.filter_hash`{% #setsockopt-filter_hash-doc %}

Type: string

Definition: Hash of the currently attached filter using sha256. Only available if the optname is `SO_ATTACH_FILTER`

### `setsockopt.filter_instructions`{% #setsockopt-filter_instructions-doc %}

Type: string

Definition: Instructions of the currently attached filter. Only available if the optname is `SO_ATTACH_FILTER`

### `setsockopt.filter_len`{% #setsockopt-filter_len-doc %}

Type: int

Definition: Length of the currently attached filter. Only available if the optname is `SO_ATTACH_FILTER`

### `setsockopt.is_filter_truncated`{% #setsockopt-is_filter_truncated-doc %}

Type: bool

Definition: Indicates that the currently attached filter is truncated. Only available if the optname is `SO_ATTACH_FILTER`

### `setsockopt.level`{% #setsockopt-level-doc %}

Type: int

Definition: Socket level

### `setsockopt.optname`{% #setsockopt-optname-doc %}

Type: int

Definition: Socket option name

### `setsockopt.socket_family`{% #setsockopt-socket_family-doc %}

Type: int

Definition: Socket family

### `setsockopt.socket_protocol`{% #setsockopt-socket_protocol-doc %}

Type: int

Definition: Socket protocol

### `setsockopt.socket_type`{% #setsockopt-socket_type-doc %}

Type: int

Definition: Socket type

### `setsockopt.used_immediates`{% #setsockopt-used_immediates-doc %}

Type: int

Definition: List of immediate values used in the currently attached filter. Only available if the optname is `SO_ATTACH_FILTER`

### `setuid.euid`{% #setuid-euid-doc %}

Type: int

Definition: New effective UID of the process

### `setuid.euser`{% #setuid-euser-doc %}

Type: string

Definition: New effective user of the process

### `setuid.fsuid`{% #setuid-fsuid-doc %}

Type: int

Definition: New FileSystem UID of the process

### `setuid.fsuser`{% #setuid-fsuser-doc %}

Type: string

Definition: New FileSystem user of the process

### `setuid.uid`{% #setuid-uid-doc %}

Type: int

Definition: New UID of the process

### `setuid.user`{% #setuid-user-doc %}

Type: string

Definition: New user of the process

### `signal.pid`{% #signal-pid-doc %}

Type: int

Definition: Target PID

### `signal.type`{% #signal-type-doc %}

Type: int

Definition: Signal type (ex: SIGHUP, SIGINT, SIGQUIT, etc)

Constants: Signal constants

### `splice.pipe_entry_flag`{% #splice-pipe_entry_flag-doc %}

Type: int

Definition: Entry flag of the "fd_out" pipe passed to the splice syscall

Constants: Pipe buffer flags

### `splice.pipe_exit_flag`{% #splice-pipe_exit_flag-doc %}

Type: int

Definition: Exit flag of the "fd_out" pipe passed to the splice syscall

Constants: Pipe buffer flags

### `sysctl.action`{% #sysctl-action-doc %}

Type: int

Definition: Action performed on the system control parameter

Constants: SysCtl Actions

### `sysctl.file_position`{% #sysctl-file_position-doc %}

Type: int

Definition: Position in the sysctl control parameter file at which the action occurred

### `sysctl.name`{% #sysctl-name-doc %}

Type: string

Definition: Name of the system control parameter

### `sysctl.name_truncated`{% #sysctl-name_truncated-doc %}

Type: bool

Definition: Indicates that the name field is truncated

### `sysctl.old_value`{% #sysctl-old_value-doc %}

Type: string

Definition: Old value of the system control parameter

### `sysctl.old_value_truncated`{% #sysctl-old_value_truncated-doc %}

Type: bool

Definition: Indicates that the old value field is truncated

### `sysctl.value`{% #sysctl-value-doc %}

Type: string

Definition: New and/or current value for the system control parameter depending on the action type

### `sysctl.value_truncated`{% #sysctl-value_truncated-doc %}

Type: bool

Definition: Indicates that the value field is truncated

### `unlink.flags`{% #unlink-flags-doc %}

Type: int

Definition: Flags of the unlink syscall

Constants: Unlink flags

### `unlink.syscall.dirfd`{% #unlink-syscall-dirfd-doc %}

Type: int

Definition: Directory file descriptor argument of the syscall

### `unlink.syscall.flags`{% #unlink-syscall-flags-doc %}

Type: int

Definition: Flags argument of the syscall

### `unlink.syscall.path`{% #unlink-syscall-path-doc %}

Type: string

Definition: Path argument of the syscall

### `unload_module.name`{% #unload_module-name-doc %}

Type: string

Definition: Name of the kernel module that was deleted

### `utimes.syscall.path`{% #utimes-syscall-path-doc %}

Type: string

Definition: Path argument of the syscall

## Constants{% #constants %}

Constants are used to improve the readability of your rules. Some constants are common to all architectures, others are specific to some architectures.

### `ABI`{% #abi %}

ABI used for binary compilation.

| Name          | Architectures |
| ------------- | ------------- |
| `BIT32`       | all           |
| `BIT64`       | all           |
| `UNKNOWN_ABI` | all           |

### `Architecture`{% #architecture %}

Architecture of the binary.

| Name                   | Architectures |
| ---------------------- | ------------- |
| `X86`                  | all           |
| `X86_64`               | all           |
| `ARM`                  | all           |
| `ARM64`                | all           |
| `UNKNOWN_ARCHITECTURE` | all           |

### `BPF attach types`{% #bpf-attach-types %}

BPF attach types are the supported eBPF program attach types.

| Name                           | Architectures |
| ------------------------------ | ------------- |
| `BPF_CGROUP_INET_INGRESS`      | all           |
| `BPF_CGROUP_INET_EGRESS`       | all           |
| `BPF_CGROUP_INET_SOCK_CREATE`  | all           |
| `BPF_CGROUP_SOCK_OPS`          | all           |
| `BPF_SK_SKB_STREAM_PARSER`     | all           |
| `BPF_SK_SKB_STREAM_VERDICT`    | all           |
| `BPF_CGROUP_DEVICE`            | all           |
| `BPF_SK_MSG_VERDICT`           | all           |
| `BPF_CGROUP_INET4_BIND`        | all           |
| `BPF_CGROUP_INET6_BIND`        | all           |
| `BPF_CGROUP_INET4_CONNECT`     | all           |
| `BPF_CGROUP_INET6_CONNECT`     | all           |
| `BPF_CGROUP_INET4_POST_BIND`   | all           |
| `BPF_CGROUP_INET6_POST_BIND`   | all           |
| `BPF_CGROUP_UDP4_SENDMSG`      | all           |
| `BPF_CGROUP_UDP6_SENDMSG`      | all           |
| `BPF_LIRC_MODE2`               | all           |
| `BPF_FLOW_DISSECTOR`           | all           |
| `BPF_CGROUP_SYSCTL`            | all           |
| `BPF_CGROUP_UDP4_RECVMSG`      | all           |
| `BPF_CGROUP_UDP6_RECVMSG`      | all           |
| `BPF_CGROUP_GETSOCKOPT`        | all           |
| `BPF_CGROUP_SETSOCKOPT`        | all           |
| `BPF_TRACE_RAW_TP`             | all           |
| `BPF_TRACE_FENTRY`             | all           |
| `BPF_TRACE_FEXIT`              | all           |
| `BPF_MODIFY_RETURN`            | all           |
| `BPF_LSM_MAC`                  | all           |
| `BPF_TRACE_ITER`               | all           |
| `BPF_CGROUP_INET4_GETPEERNAME` | all           |
| `BPF_CGROUP_INET6_GETPEERNAME` | all           |
| `BPF_CGROUP_INET4_GETSOCKNAME` | all           |
| `BPF_CGROUP_INET6_GETSOCKNAME` | all           |
| `BPF_XDP_DEVMAP`               | all           |
| `BPF_CGROUP_INET_SOCK_RELEASE` | all           |
| `BPF_XDP_CPUMAP`               | all           |
| `BPF_SK_LOOKUP`                | all           |
| `BPF_XDP`                      | all           |
| `BPF_SK_SKB_VERDICT`           | all           |

### `BPF commands`{% #bpf-commands %}

BPF commands are used to specify a command to a bpf syscall.

| Name                              | Architectures |
| --------------------------------- | ------------- |
| `BPF_MAP_CREATE`                  | all           |
| `BPF_MAP_LOOKUP_ELEM`             | all           |
| `BPF_MAP_UPDATE_ELEM`             | all           |
| `BPF_MAP_DELETE_ELEM`             | all           |
| `BPF_MAP_GET_NEXT_KEY`            | all           |
| `BPF_PROG_LOAD`                   | all           |
| `BPF_OBJ_PIN`                     | all           |
| `BPF_OBJ_GET`                     | all           |
| `BPF_PROG_ATTACH`                 | all           |
| `BPF_PROG_DETACH`                 | all           |
| `BPF_PROG_TEST_RUN`               | all           |
| `BPF_PROG_RUN`                    | all           |
| `BPF_PROG_GET_NEXT_ID`            | all           |
| `BPF_MAP_GET_NEXT_ID`             | all           |
| `BPF_PROG_GET_FD_BY_ID`           | all           |
| `BPF_MAP_GET_FD_BY_ID`            | all           |
| `BPF_OBJ_GET_INFO_BY_FD`          | all           |
| `BPF_PROG_QUERY`                  | all           |
| `BPF_RAW_TRACEPOINT_OPEN`         | all           |
| `BPF_BTF_LOAD`                    | all           |
| `BPF_BTF_GET_FD_BY_ID`            | all           |
| `BPF_TASK_FD_QUERY`               | all           |
| `BPF_MAP_LOOKUP_AND_DELETE_ELEM`  | all           |
| `BPF_MAP_FREEZE`                  | all           |
| `BPF_BTF_GET_NEXT_ID`             | all           |
| `BPF_MAP_LOOKUP_BATCH`            | all           |
| `BPF_MAP_LOOKUP_AND_DELETE_BATCH` | all           |
| `BPF_MAP_UPDATE_BATCH`            | all           |
| `BPF_MAP_DELETE_BATCH`            | all           |
| `BPF_LINK_CREATE`                 | all           |
| `BPF_LINK_UPDATE`                 | all           |
| `BPF_LINK_GET_FD_BY_ID`           | all           |
| `BPF_LINK_GET_NEXT_ID`            | all           |
| `BPF_ENABLE_STATS`                | all           |
| `BPF_ITER_CREATE`                 | all           |
| `BPF_LINK_DETACH`                 | all           |
| `BPF_PROG_BIND_MAP`               | all           |

### `BPF helper functions`{% #bpf-helper-functions %}

BPF helper functions are the supported BPF helper functions.

| Name                                 | Architectures |
| ------------------------------------ | ------------- |
| `BPF_UNSPEC`                         | all           |
| `BPF_MAP_LOOKUP_ELEM`                | all           |
| `BPF_MAP_UPDATE_ELEM`                | all           |
| `BPF_MAP_DELETE_ELEM`                | all           |
| `BPF_PROBE_READ`                     | all           |
| `BPF_KTIME_GET_NS`                   | all           |
| `BPF_TRACE_PRINTK`                   | all           |
| `BPF_GET_PRANDOM_U32`                | all           |
| `BPF_GET_SMP_PROCESSOR_ID`           | all           |
| `BPF_SKB_STORE_BYTES`                | all           |
| `BPF_L3_CSUM_REPLACE`                | all           |
| `BPF_L4_CSUM_REPLACE`                | all           |
| `BPF_TAIL_CALL`                      | all           |
| `BPF_CLONE_REDIRECT`                 | all           |
| `BPF_GET_CURRENT_PID_TGID`           | all           |
| `BPF_GET_CURRENT_UID_GID`            | all           |
| `BPF_GET_CURRENT_COMM`               | all           |
| `BPF_GET_CGROUP_CLASSID`             | all           |
| `BPF_SKB_VLAN_PUSH`                  | all           |
| `BPF_SKB_VLAN_POP`                   | all           |
| `BPF_SKB_GET_TUNNEL_KEY`             | all           |
| `BPF_SKB_SET_TUNNEL_KEY`             | all           |
| `BPF_PERF_EVENT_READ`                | all           |
| `BPF_REDIRECT`                       | all           |
| `BPF_GET_ROUTE_REALM`                | all           |
| `BPF_PERF_EVENT_OUTPUT`              | all           |
| `BPF_SKB_LOAD_BYTES`                 | all           |
| `BPF_GET_STACKID`                    | all           |
| `BPF_CSUM_DIFF`                      | all           |
| `BPF_SKB_GET_TUNNEL_OPT`             | all           |
| `BPF_SKB_SET_TUNNEL_OPT`             | all           |
| `BPF_SKB_CHANGE_PROTO`               | all           |
| `BPF_SKB_CHANGE_TYPE`                | all           |
| `BPF_SKB_UNDER_CGROUP`               | all           |
| `BPF_GET_HASH_RECALC`                | all           |
| `BPF_GET_CURRENT_TASK`               | all           |
| `BPF_PROBE_WRITE_USER`               | all           |
| `BPF_CURRENT_TASK_UNDER_CGROUP`      | all           |
| `BPF_SKB_CHANGE_TAIL`                | all           |
| `BPF_SKB_PULL_DATA`                  | all           |
| `BPF_CSUM_UPDATE`                    | all           |
| `BPF_SET_HASH_INVALID`               | all           |
| `BPF_GET_NUMA_NODE_ID`               | all           |
| `BPF_SKB_CHANGE_HEAD`                | all           |
| `BPF_XDP_ADJUST_HEAD`                | all           |
| `BPF_PROBE_READ_STR`                 | all           |
| `BPF_GET_SOCKET_COOKIE`              | all           |
| `BPF_GET_SOCKET_UID`                 | all           |
| `BPF_SET_HASH`                       | all           |
| `BPF_SETSOCKOPT`                     | all           |
| `BPF_SKB_ADJUST_ROOM`                | all           |
| `BPF_REDIRECT_MAP`                   | all           |
| `BPF_SK_REDIRECT_MAP`                | all           |
| `BPF_SOCK_MAP_UPDATE`                | all           |
| `BPF_XDP_ADJUST_META`                | all           |
| `BPF_PERF_EVENT_READ_VALUE`          | all           |
| `BPF_PERF_PROG_READ_VALUE`           | all           |
| `BPF_GETSOCKOPT`                     | all           |
| `BPF_OVERRIDE_RETURN`                | all           |
| `BPF_SOCK_OPS_CB_FLAGS_SET`          | all           |
| `BPF_MSG_REDIRECT_MAP`               | all           |
| `BPF_MSG_APPLY_BYTES`                | all           |
| `BPF_MSG_CORK_BYTES`                 | all           |
| `BPF_MSG_PULL_DATA`                  | all           |
| `BPF_BIND`                           | all           |
| `BPF_XDP_ADJUST_TAIL`                | all           |
| `BPF_SKB_GET_XFRM_STATE`             | all           |
| `BPF_GET_STACK`                      | all           |
| `BPF_SKB_LOAD_BYTES_RELATIVE`        | all           |
| `BPF_FIB_LOOKUP`                     | all           |
| `BPF_SOCK_HASH_UPDATE`               | all           |
| `BPF_MSG_REDIRECT_HASH`              | all           |
| `BPF_SK_REDIRECT_HASH`               | all           |
| `BPF_LWT_PUSH_ENCAP`                 | all           |
| `BPF_LWT_SEG6_STORE_BYTES`           | all           |
| `BPF_LWT_SEG6_ADJUST_SRH`            | all           |
| `BPF_LWT_SEG6_ACTION`                | all           |
| `BPF_RC_REPEAT`                      | all           |
| `BPF_RC_KEYDOWN`                     | all           |
| `BPF_SKB_CGROUP_ID`                  | all           |
| `BPF_GET_CURRENT_CGROUP_ID`          | all           |
| `BPF_GET_LOCAL_STORAGE`              | all           |
| `BPF_SK_SELECT_REUSEPORT`            | all           |
| `BPF_SKB_ANCESTOR_CGROUP_ID`         | all           |
| `BPF_SK_LOOKUP_TCP`                  | all           |
| `BPF_SK_LOOKUP_UDP`                  | all           |
| `BPF_SK_RELEASE`                     | all           |
| `BPF_MAP_PUSH_ELEM`                  | all           |
| `BPF_MAP_POP_ELEM`                   | all           |
| `BPF_MAP_PEEK_ELEM`                  | all           |
| `BPF_MSG_PUSH_DATA`                  | all           |
| `BPF_MSG_POP_DATA`                   | all           |
| `BPF_RC_POINTER_REL`                 | all           |
| `BPF_SPIN_LOCK`                      | all           |
| `BPF_SPIN_UNLOCK`                    | all           |
| `BPF_SK_FULLSOCK`                    | all           |
| `BPF_TCP_SOCK`                       | all           |
| `BPF_SKB_ECN_SET_CE`                 | all           |
| `BPF_GET_LISTENER_SOCK`              | all           |
| `BPF_SKC_LOOKUP_TCP`                 | all           |
| `BPF_TCP_CHECK_SYNCOOKIE`            | all           |
| `BPF_SYSCTL_GET_NAME`                | all           |
| `BPF_SYSCTL_GET_CURRENT_VALUE`       | all           |
| `BPF_SYSCTL_GET_NEW_VALUE`           | all           |
| `BPF_SYSCTL_SET_NEW_VALUE`           | all           |
| `BPF_STRTOL`                         | all           |
| `BPF_STRTOUL`                        | all           |
| `BPF_SK_STORAGE_GET`                 | all           |
| `BPF_SK_STORAGE_DELETE`              | all           |
| `BPF_SEND_SIGNAL`                    | all           |
| `BPF_TCP_GEN_SYNCOOKIE`              | all           |
| `BPF_SKB_OUTPUT`                     | all           |
| `BPF_PROBE_READ_USER`                | all           |
| `BPF_PROBE_READ_KERNEL`              | all           |
| `BPF_PROBE_READ_USER_STR`            | all           |
| `BPF_PROBE_READ_KERNEL_STR`          | all           |
| `BPF_TCP_SEND_ACK`                   | all           |
| `BPF_SEND_SIGNAL_THREAD`             | all           |
| `BPF_JIFFIES64`                      | all           |
| `BPF_READ_BRANCH_RECORDS`            | all           |
| `BPF_GET_NS_CURRENT_PID_TGID`        | all           |
| `BPF_XDP_OUTPUT`                     | all           |
| `BPF_GET_NETNS_COOKIE`               | all           |
| `BPF_GET_CURRENT_ANCESTOR_CGROUP_ID` | all           |
| `BPF_SK_ASSIGN`                      | all           |
| `BPF_KTIME_GET_BOOT_NS`              | all           |
| `BPF_SEQ_PRINTF`                     | all           |
| `BPF_SEQ_WRITE`                      | all           |
| `BPF_SK_CGROUP_ID`                   | all           |
| `BPF_SK_ANCESTOR_CGROUP_ID`          | all           |
| `BPF_RINGBUF_OUTPUT`                 | all           |
| `BPF_RINGBUF_RESERVE`                | all           |
| `BPF_RINGBUF_SUBMIT`                 | all           |
| `BPF_RINGBUF_DISCARD`                | all           |
| `BPF_RINGBUF_QUERY`                  | all           |
| `BPF_CSUM_LEVEL`                     | all           |
| `BPF_SKC_TO_TCP6_SOCK`               | all           |
| `BPF_SKC_TO_TCP_SOCK`                | all           |
| `BPF_SKC_TO_TCP_TIMEWAIT_SOCK`       | all           |
| `BPF_SKC_TO_TCP_REQUEST_SOCK`        | all           |
| `BPF_SKC_TO_UDP6_SOCK`               | all           |
| `BPF_GET_TASK_STACK`                 | all           |
| `BPF_LOAD_HDR_OPT`                   | all           |
| `BPF_STORE_HDR_OPT`                  | all           |
| `BPF_RESERVE_HDR_OPT`                | all           |
| `BPF_INODE_STORAGE_GET`              | all           |
| `BPF_INODE_STORAGE_DELETE`           | all           |
| `BPF_D_PATH`                         | all           |
| `BPF_COPY_FROM_USER`                 | all           |
| `BPF_SNPRINTF_BTF`                   | all           |
| `BPF_SEQ_PRINTF_BTF`                 | all           |
| `BPF_SKB_CGROUP_CLASSID`             | all           |
| `BPF_REDIRECT_NEIGH`                 | all           |
| `BPF_PER_CPU_PTR`                    | all           |
| `BPF_THIS_CPU_PTR`                   | all           |
| `BPF_REDIRECT_PEER`                  | all           |
| `BPF_TASK_STORAGE_GET`               | all           |
| `BPF_TASK_STORAGE_DELETE`            | all           |
| `BPF_GET_CURRENT_TASK_BTF`           | all           |
| `BPF_BPRM_OPTS_SET`                  | all           |
| `BPF_KTIME_GET_COARSE_NS`            | all           |
| `BPF_IMA_INODE_HASH`                 | all           |
| `BPF_SOCK_FROM_FILE`                 | all           |
| `BPF_CHECK_MTU`                      | all           |
| `BPF_FOR_EACH_MAP_ELEM`              | all           |
| `BPF_SNPRINTF`                       | all           |

### `BPF map types`{% #bpf-map-types %}

BPF map types are the supported eBPF map types.

| Name                                 | Architectures |
| ------------------------------------ | ------------- |
| `BPF_MAP_TYPE_UNSPEC`                | all           |
| `BPF_MAP_TYPE_HASH`                  | all           |
| `BPF_MAP_TYPE_ARRAY`                 | all           |
| `BPF_MAP_TYPE_PROG_ARRAY`            | all           |
| `BPF_MAP_TYPE_PERF_EVENT_ARRAY`      | all           |
| `BPF_MAP_TYPE_PERCPU_HASH`           | all           |
| `BPF_MAP_TYPE_PERCPU_ARRAY`          | all           |
| `BPF_MAP_TYPE_STACK_TRACE`           | all           |
| `BPF_MAP_TYPE_CGROUP_ARRAY`          | all           |
| `BPF_MAP_TYPE_LRU_HASH`              | all           |
| `BPF_MAP_TYPE_LRU_PERCPU_HASH`       | all           |
| `BPF_MAP_TYPE_LPM_TRIE`              | all           |
| `BPF_MAP_TYPE_ARRAY_OF_MAPS`         | all           |
| `BPF_MAP_TYPE_HASH_OF_MAPS`          | all           |
| `BPF_MAP_TYPE_DEVMAP`                | all           |
| `BPF_MAP_TYPE_SOCKMAP`               | all           |
| `BPF_MAP_TYPE_CPUMAP`                | all           |
| `BPF_MAP_TYPE_XSKMAP`                | all           |
| `BPF_MAP_TYPE_SOCKHASH`              | all           |
| `BPF_MAP_TYPE_CGROUP_STORAGE`        | all           |
| `BPF_MAP_TYPE_REUSEPORT_SOCKARRAY`   | all           |
| `BPF_MAP_TYPE_PERCPU_CGROUP_STORAGE` | all           |
| `BPF_MAP_TYPE_QUEUE`                 | all           |
| `BPF_MAP_TYPE_STACK`                 | all           |
| `BPF_MAP_TYPE_SK_STORAGE`            | all           |
| `BPF_MAP_TYPE_DEVMAP_HASH`           | all           |
| `BPF_MAP_TYPE_STRUCT_OPS`            | all           |
| `BPF_MAP_TYPE_RINGBUF`               | all           |
| `BPF_MAP_TYPE_INODE_STORAGE`         | all           |
| `BPF_MAP_TYPE_TASK_STORAGE`          | all           |

### `BPF program types`{% #bpf-program-types %}

BPF program types are the supported eBPF program types.

| Name                                    | Architectures |
| --------------------------------------- | ------------- |
| `BPF_PROG_TYPE_UNSPEC`                  | all           |
| `BPF_PROG_TYPE_SOCKET_FILTER`           | all           |
| `BPF_PROG_TYPE_KPROBE`                  | all           |
| `BPF_PROG_TYPE_SCHED_CLS`               | all           |
| `BPF_PROG_TYPE_SCHED_ACT`               | all           |
| `BPF_PROG_TYPE_TRACEPOINT`              | all           |
| `BPF_PROG_TYPE_XDP`                     | all           |
| `BPF_PROG_TYPE_PERF_EVENT`              | all           |
| `BPF_PROG_TYPE_CGROUP_SKB`              | all           |
| `BPF_PROG_TYPE_CGROUP_SOCK`             | all           |
| `BPF_PROG_TYPE_LWT_IN`                  | all           |
| `BPF_PROG_TYPE_LWT_OUT`                 | all           |
| `BPF_PROG_TYPE_LWT_XMIT`                | all           |
| `BPF_PROG_TYPE_SOCK_OPS`                | all           |
| `BPF_PROG_TYPE_SK_SKB`                  | all           |
| `BPF_PROG_TYPE_CGROUP_DEVICE`           | all           |
| `BPF_PROG_TYPE_SK_MSG`                  | all           |
| `BPF_PROG_TYPE_RAW_TRACEPOINT`          | all           |
| `BPF_PROG_TYPE_CGROUP_SOCK_ADDR`        | all           |
| `BPF_PROG_TYPE_LWT_SEG6LOCAL`           | all           |
| `BPF_PROG_TYPE_LIRC_MODE2`              | all           |
| `BPF_PROG_TYPE_SK_REUSEPORT`            | all           |
| `BPF_PROG_TYPE_FLOW_DISSECTOR`          | all           |
| `BPF_PROG_TYPE_CGROUP_SYSCTL`           | all           |
| `BPF_PROG_TYPE_RAW_TRACEPOINT_WRITABLE` | all           |
| `BPF_PROG_TYPE_CGROUP_SOCKOPT`          | all           |
| `BPF_PROG_TYPE_TRACING`                 | all           |
| `BPF_PROG_TYPE_STRUCT_OPS`              | all           |
| `BPF_PROG_TYPE_EXT`                     | all           |
| `BPF_PROG_TYPE_LSM`                     | all           |
| `BPF_PROG_TYPE_SK_LOOKUP`               | all           |

### `Boolean constants`{% #boolean-constants %}

Boolean constants are the supported boolean constants.

| Name    | Architectures |
| ------- | ------------- |
| `true`  | all           |
| `false` | all           |

### `CompressionType`{% #compressiontype %}

Compression algorithm.

| Name    | Architectures |
| ------- | ------------- |
| `NONE`  | all           |
| `GZIP`  | all           |
| `ZIP`   | all           |
| `ZSTD`  | all           |
| `7Z`    | all           |
| `BZIP2` | all           |
| `XZ`    | all           |

### `DNS Responses`{% #dns-responses %}

DNS Responses are the supported response codes

| Name       | Architectures |
| ---------- | ------------- |
| `NOERROR`  | all           |
| `FORMERR`  | all           |
| `SERVFAIL` | all           |
| `NXDOMAIN` | all           |
| `NOTIMP`   | all           |
| `REFUSED`  | all           |
| `YXDOMAIN` | all           |
| `YXRRSET`  | all           |
| `NXRRSET`  | all           |
| `NOTAUTH`  | all           |
| `NOTZONE`  | all           |
| `BADVERS`  | all           |
| `BADSIG`   | all           |
| `BADKEY`   | all           |
| `BADTIME`  | all           |
| `BADMODE`  | all           |
| `BADNAME`  | all           |
| `BADALG`   | all           |

### `DNS qclasses`{% #dns-qclasses %}

DNS qclasses are the supported DNS query classes.

| Name           | Architectures |
| -------------- | ------------- |
| `CLASS_INET`   | all           |
| `CLASS_CSNET`  | all           |
| `CLASS_CHAOS`  | all           |
| `CLASS_HESIOD` | all           |
| `CLASS_NONE`   | all           |
| `CLASS_ANY`    | all           |

### `DNS qtypes`{% #dns-qtypes %}

DNS qtypes are the supported DNS query types.

| Name         | Architectures |
| ------------ | ------------- |
| `None`       | all           |
| `A`          | all           |
| `NS`         | all           |
| `MD`         | all           |
| `MF`         | all           |
| `CNAME`      | all           |
| `SOA`        | all           |
| `MB`         | all           |
| `MG`         | all           |
| `MR`         | all           |
| `NULL`       | all           |
| `PTR`        | all           |
| `HINFO`      | all           |
| `MINFO`      | all           |
| `MX`         | all           |
| `TXT`        | all           |
| `RP`         | all           |
| `AFSDB`      | all           |
| `X25`        | all           |
| `ISDN`       | all           |
| `RT`         | all           |
| `NSAPPTR`    | all           |
| `SIG`        | all           |
| `KEY`        | all           |
| `PX`         | all           |
| `GPOS`       | all           |
| `AAAA`       | all           |
| `LOC`        | all           |
| `NXT`        | all           |
| `EID`        | all           |
| `NIMLOC`     | all           |
| `SRV`        | all           |
| `ATMA`       | all           |
| `NAPTR`      | all           |
| `KX`         | all           |
| `CERT`       | all           |
| `DNAME`      | all           |
| `OPT`        | all           |
| `APL`        | all           |
| `DS`         | all           |
| `SSHFP`      | all           |
| `RRSIG`      | all           |
| `NSEC`       | all           |
| `DNSKEY`     | all           |
| `DHCID`      | all           |
| `NSEC3`      | all           |
| `NSEC3PARAM` | all           |
| `TLSA`       | all           |
| `SMIMEA`     | all           |
| `HIP`        | all           |
| `NINFO`      | all           |
| `RKEY`       | all           |
| `TALINK`     | all           |
| `CDS`        | all           |
| `CDNSKEY`    | all           |
| `OPENPGPKEY` | all           |
| `CSYNC`      | all           |
| `ZONEMD`     | all           |
| `SVCB`       | all           |
| `HTTPS`      | all           |
| `SPF`        | all           |
| `UINFO`      | all           |
| `UID`        | all           |
| `GID`        | all           |
| `UNSPEC`     | all           |
| `NID`        | all           |
| `L32`        | all           |
| `L64`        | all           |
| `LP`         | all           |
| `EUI48`      | all           |
| `EUI64`      | all           |
| `URI`        | all           |
| `CAA`        | all           |
| `AVC`        | all           |
| `TKEY`       | all           |
| `TSIG`       | all           |
| `IXFR`       | all           |
| `AXFR`       | all           |
| `MAILB`      | all           |
| `MAILA`      | all           |
| `ANY`        | all           |
| `TA`         | all           |
| `DLV`        | all           |
| `Reserved`   | all           |

### `Error constants`{% #error-constants %}

Error constants are the supported error constants.

| Name              | Architectures |
| ----------------- | ------------- |
| `E2BIG`           | all           |
| `EACCES`          | all           |
| `EADDRINUSE`      | all           |
| `EADDRNOTAVAIL`   | all           |
| `EADV`            | all           |
| `EAFNOSUPPORT`    | all           |
| `EAGAIN`          | all           |
| `EALREADY`        | all           |
| `EBADE`           | all           |
| `EBADF`           | all           |
| `EBADFD`          | all           |
| `EBADMSG`         | all           |
| `EBADR`           | all           |
| `EBADRQC`         | all           |
| `EBADSLT`         | all           |
| `EBFONT`          | all           |
| `EBUSY`           | all           |
| `ECANCELED`       | all           |
| `ECHILD`          | all           |
| `ECHRNG`          | all           |
| `ECOMM`           | all           |
| `ECONNABORTED`    | all           |
| `ECONNREFUSED`    | all           |
| `ECONNRESET`      | all           |
| `EDEADLK`         | all           |
| `EDEADLOCK`       | all           |
| `EDESTADDRREQ`    | all           |
| `EDOM`            | all           |
| `EDOTDOT`         | all           |
| `EDQUOT`          | all           |
| `EEXIST`          | all           |
| `EFAULT`          | all           |
| `EFBIG`           | all           |
| `EHOSTDOWN`       | all           |
| `EHOSTUNREACH`    | all           |
| `EIDRM`           | all           |
| `EILSEQ`          | all           |
| `EINPROGRESS`     | all           |
| `EINTR`           | all           |
| `EINVAL`          | all           |
| `EIO`             | all           |
| `EISCONN`         | all           |
| `EISDIR`          | all           |
| `EISNAM`          | all           |
| `EKEYEXPIRED`     | all           |
| `EKEYREJECTED`    | all           |
| `EKEYREVOKED`     | all           |
| `EL2HLT`          | all           |
| `EL2NSYNC`        | all           |
| `EL3HLT`          | all           |
| `EL3RST`          | all           |
| `ELIBACC`         | all           |
| `ELIBBAD`         | all           |
| `ELIBEXEC`        | all           |
| `ELIBMAX`         | all           |
| `ELIBSCN`         | all           |
| `ELNRNG`          | all           |
| `ELOOP`           | all           |
| `EMEDIUMTYPE`     | all           |
| `EMFILE`          | all           |
| `EMLINK`          | all           |
| `EMSGSIZE`        | all           |
| `EMULTIHOP`       | all           |
| `ENAMETOOLONG`    | all           |
| `ENAVAIL`         | all           |
| `ENETDOWN`        | all           |
| `ENETRESET`       | all           |
| `ENETUNREACH`     | all           |
| `ENFILE`          | all           |
| `ENOANO`          | all           |
| `ENOBUFS`         | all           |
| `ENOCSI`          | all           |
| `ENODATA`         | all           |
| `ENODEV`          | all           |
| `ENOENT`          | all           |
| `ENOEXEC`         | all           |
| `ENOKEY`          | all           |
| `ENOLCK`          | all           |
| `ENOLINK`         | all           |
| `ENOMEDIUM`       | all           |
| `ENOMEM`          | all           |
| `ENOMSG`          | all           |
| `ENONET`          | all           |
| `ENOPKG`          | all           |
| `ENOPROTOOPT`     | all           |
| `ENOSPC`          | all           |
| `ENOSR`           | all           |
| `ENOSTR`          | all           |
| `ENOSYS`          | all           |
| `ENOTBLK`         | all           |
| `ENOTCONN`        | all           |
| `ENOTDIR`         | all           |
| `ENOTEMPTY`       | all           |
| `ENOTNAM`         | all           |
| `ENOTRECOVERABLE` | all           |
| `ENOTSOCK`        | all           |
| `ENOTSUP`         | all           |
| `ENOTTY`          | all           |
| `ENOTUNIQ`        | all           |
| `ENXIO`           | all           |
| `EOPNOTSUPP`      | all           |
| `EOVERFLOW`       | all           |
| `EOWNERDEAD`      | all           |
| `EPERM`           | all           |
| `EPFNOSUPPORT`    | all           |
| `EPIPE`           | all           |
| `EPROTO`          | all           |
| `EPROTONOSUPPORT` | all           |
| `EPROTOTYPE`      | all           |
| `ERANGE`          | all           |
| `EREMCHG`         | all           |
| `EREMOTE`         | all           |
| `EREMOTEIO`       | all           |
| `ERESTART`        | all           |
| `ERFKILL`         | all           |
| `EROFS`           | all           |
| `ESHUTDOWN`       | all           |
| `ESOCKTNOSUPPORT` | all           |
| `ESPIPE`          | all           |
| `ESRCH`           | all           |
| `ESRMNT`          | all           |
| `ESTALE`          | all           |
| `ESTRPIPE`        | all           |
| `ETIME`           | all           |
| `ETIMEDOUT`       | all           |
| `ETOOMANYREFS`    | all           |
| `ETXTBSY`         | all           |
| `EUCLEAN`         | all           |
| `EUNATCH`         | all           |
| `EUSERS`          | all           |
| `EWOULDBLOCK`     | all           |
| `EXDEV`           | all           |
| `EXFULL`          | all           |

### `File mode constants`{% #file-mode-constants %}

File mode constants are the supported file permissions as well as constants for the set-user-ID, set-group-ID, and sticky bits.

| Name      | Architectures |
| --------- | ------------- |
| `S_ISUID` | all           |
| `S_ISGID` | all           |
| `S_ISVTX` | all           |
| `S_IRWXU` | all           |
| `S_IRUSR` | all           |
| `S_IWUSR` | all           |
| `S_IXUSR` | all           |
| `S_IRWXG` | all           |
| `S_IRGRP` | all           |
| `S_IWGRP` | all           |
| `S_IXGRP` | all           |
| `S_IRWXO` | all           |
| `S_IROTH` | all           |
| `S_IWOTH` | all           |
| `S_IXOTH` | all           |

### `FileType`{% #filetype %}

File types.

| Name                 | Architectures |
| -------------------- | ------------- |
| `EMPTY`              | all           |
| `SHELL_SCRIPT`       | all           |
| `TEXT`               | all           |
| `COMPRESSED`         | all           |
| `ENCRYPTED`          | all           |
| `BINARY`             | all           |
| `LINUX_EXECUTABLE`   | all           |
| `WINDOWS_EXECUTABLE` | all           |
| `MACOS_EXECUTABLE`   | all           |
| `FILE_LESS`          | all           |

### `Inode mode constants`{% #inode-mode-constants %}

Inode mode constants are the supported file type constants as well as the file mode constants.

| Name       | Architectures |
| ---------- | ------------- |
| `S_IFMT`   | all           |
| `S_IFSOCK` | all           |
| `S_IFLNK`  | all           |
| `S_IFREG`  | all           |
| `S_IFBLK`  | all           |
| `S_IFDIR`  | all           |
| `S_IFCHR`  | all           |
| `S_IFIFO`  | all           |
| `S_ISUID`  | all           |
| `S_ISGID`  | all           |
| `S_ISVTX`  | all           |
| `S_IRWXU`  | all           |
| `S_IRUSR`  | all           |
| `S_IWUSR`  | all           |
| `S_IXUSR`  | all           |
| `S_IRWXG`  | all           |
| `S_IRGRP`  | all           |
| `S_IWGRP`  | all           |
| `S_IXGRP`  | all           |
| `S_IRWXO`  | all           |
| `S_IROTH`  | all           |
| `S_IWOTH`  | all           |
| `S_IXOTH`  | all           |

### `Kernel Capability constants`{% #kernel-capability-constants %}

Kernel Capability constants are the supported Linux Kernel Capability.

| Name                     | Architectures |
| ------------------------ | ------------- |
| `CAP_AUDIT_CONTROL`      | all           |
| `CAP_AUDIT_READ`         | all           |
| `CAP_AUDIT_WRITE`        | all           |
| `CAP_BLOCK_SUSPEND`      | all           |
| `CAP_BPF`                | all           |
| `CAP_CHECKPOINT_RESTORE` | all           |
| `CAP_CHOWN`              | all           |
| `CAP_DAC_OVERRIDE`       | all           |
| `CAP_DAC_READ_SEARCH`    | all           |
| `CAP_FOWNER`             | all           |
| `CAP_FSETID`             | all           |
| `CAP_IPC_LOCK`           | all           |
| `CAP_IPC_OWNER`          | all           |
| `CAP_KILL`               | all           |
| `CAP_LEASE`              | all           |
| `CAP_LINUX_IMMUTABLE`    | all           |
| `CAP_MAC_ADMIN`          | all           |
| `CAP_MAC_OVERRIDE`       | all           |
| `CAP_MKNOD`              | all           |
| `CAP_NET_ADMIN`          | all           |
| `CAP_NET_BIND_SERVICE`   | all           |
| `CAP_NET_BROADCAST`      | all           |
| `CAP_NET_RAW`            | all           |
| `CAP_PERFMON`            | all           |
| `CAP_SETFCAP`            | all           |
| `CAP_SETGID`             | all           |
| `CAP_SETPCAP`            | all           |
| `CAP_SETUID`             | all           |
| `CAP_SYSLOG`             | all           |
| `CAP_SYS_ADMIN`          | all           |
| `CAP_SYS_BOOT`           | all           |
| `CAP_SYS_CHROOT`         | all           |
| `CAP_SYS_MODULE`         | all           |
| `CAP_SYS_NICE`           | all           |
| `CAP_SYS_PACCT`          | all           |
| `CAP_SYS_PTRACE`         | all           |
| `CAP_SYS_RAWIO`          | all           |
| `CAP_SYS_RESOURCE`       | all           |
| `CAP_SYS_TIME`           | all           |
| `CAP_SYS_TTY_CONFIG`     | all           |
| `CAP_WAKE_ALARM`         | all           |

### `L3 protocols`{% #l3-protocols %}

L3 protocols are the supported Layer 3 protocols.

| Name                    | Architectures |
| ----------------------- | ------------- |
| `ETH_P_LOOP`            | all           |
| `ETH_P_PUP`             | all           |
| `ETH_P_PUPAT`           | all           |
| `ETH_P_TSN`             | all           |
| `ETH_P_IP`              | all           |
| `ETH_P_X25`             | all           |
| `ETH_P_ARP`             | all           |
| `ETH_P_BPQ`             | all           |
| `ETH_P_IEEEPUP`         | all           |
| `ETH_P_IEEEPUPAT`       | all           |
| `ETH_P_BATMAN`          | all           |
| `ETH_P_DEC`             | all           |
| `ETH_P_DNADL`           | all           |
| `ETH_P_DNARC`           | all           |
| `ETH_P_DNART`           | all           |
| `ETH_P_LAT`             | all           |
| `ETH_P_DIAG`            | all           |
| `ETH_P_CUST`            | all           |
| `ETH_P_SCA`             | all           |
| `ETH_P_TEB`             | all           |
| `ETH_P_RARP`            | all           |
| `ETH_P_ATALK`           | all           |
| `ETH_P_AARP`            | all           |
| `ETH_P_8021_Q`          | all           |
| `ETH_P_ERSPAN`          | all           |
| `ETH_P_IPX`             | all           |
| `ETH_P_IPV6`            | all           |
| `ETH_P_PAUSE`           | all           |
| `ETH_P_SLOW`            | all           |
| `ETH_P_WCCP`            | all           |
| `ETH_P_MPLSUC`          | all           |
| `ETH_P_MPLSMC`          | all           |
| `ETH_P_ATMMPOA`         | all           |
| `ETH_P_PPPDISC`         | all           |
| `ETH_P_PPPSES`          | all           |
| `ETH_P__LINK_CTL`       | all           |
| `ETH_P_ATMFATE`         | all           |
| `ETH_P_PAE`             | all           |
| `ETH_P_AOE`             | all           |
| `ETH_P_8021_AD`         | all           |
| `ETH_P_802_EX1`         | all           |
| `ETH_P_TIPC`            | all           |
| `ETH_P_MACSEC`          | all           |
| `ETH_P_8021_AH`         | all           |
| `ETH_P_MVRP`            | all           |
| `ETH_P_1588`            | all           |
| `ETH_P_NCSI`            | all           |
| `ETH_P_PRP`             | all           |
| `ETH_P_FCOE`            | all           |
| `ETH_P_IBOE`            | all           |
| `ETH_P_TDLS`            | all           |
| `ETH_P_FIP`             | all           |
| `ETH_P_80221`           | all           |
| `ETH_P_HSR`             | all           |
| `ETH_P_NSH`             | all           |
| `ETH_P_LOOPBACK`        | all           |
| `ETH_P_QINQ1`           | all           |
| `ETH_P_QINQ2`           | all           |
| `ETH_P_QINQ3`           | all           |
| `ETH_P_EDSA`            | all           |
| `ETH_P_IFE`             | all           |
| `ETH_P_AFIUCV`          | all           |
| `ETH_P_8023_MIN`        | all           |
| `ETH_P_IPV6_HOP_BY_HOP` | all           |
| `ETH_P_8023`            | all           |
| `ETH_P_AX25`            | all           |
| `ETH_P_ALL`             | all           |
| `ETH_P_8022`            | all           |
| `ETH_P_SNAP`            | all           |
| `ETH_P_DDCMP`           | all           |
| `ETH_P_WANPPP`          | all           |
| `ETH_P_PPPMP`           | all           |
| `ETH_P_LOCALTALK`       | all           |
| `ETH_P_CAN`             | all           |
| `ETH_P_CANFD`           | all           |
| `ETH_P_PPPTALK`         | all           |
| `ETH_P_TR8022`          | all           |
| `ETH_P_MOBITEX`         | all           |
| `ETH_P_CONTROL`         | all           |
| `ETH_P_IRDA`            | all           |
| `ETH_P_ECONET`          | all           |
| `ETH_P_HDLC`            | all           |
| `ETH_P_ARCNET`          | all           |
| `ETH_P_DSA`             | all           |
| `ETH_P_TRAILER`         | all           |
| `ETH_P_PHONET`          | all           |
| `ETH_P_IEEE802154`      | all           |
| `ETH_P_CAIF`            | all           |
| `ETH_P_XDSA`            | all           |
| `ETH_P_MAP`             | all           |

### `L4 protocols`{% #l4-protocols %}

L4 protocols are the supported Layer 4 protocols.

| Name               | Architectures |
| ------------------ | ------------- |
| `IP_PROTO_IP`      | all           |
| `IP_PROTO_ICMP`    | all           |
| `IP_PROTO_IGMP`    | all           |
| `IP_PROTO_IPIP`    | all           |
| `IP_PROTO_TCP`     | all           |
| `IP_PROTO_EGP`     | all           |
| `IP_PROTO_IGP`     | all           |
| `IP_PROTO_PUP`     | all           |
| `IP_PROTO_UDP`     | all           |
| `IP_PROTO_IDP`     | all           |
| `IP_PROTO_TP`      | all           |
| `IP_PROTO_DCCP`    | all           |
| `IP_PROTO_IPV6`    | all           |
| `IP_PROTO_RSVP`    | all           |
| `IP_PROTO_GRE`     | all           |
| `IP_PROTO_ESP`     | all           |
| `IP_PROTO_AH`      | all           |
| `IP_PROTO_ICMPV6`  | all           |
| `IP_PROTO_MTP`     | all           |
| `IP_PROTO_BEETPH`  | all           |
| `IP_PROTO_ENCAP`   | all           |
| `IP_PROTO_PIM`     | all           |
| `IP_PROTO_COMP`    | all           |
| `IP_PROTO_SCTP`    | all           |
| `IP_PROTO_UDPLITE` | all           |
| `IP_PROTO_MPLS`    | all           |
| `IP_PROTO_RAW`     | all           |

### `LinkageType`{% #linkagetype %}

Linkage types.

| Name      | Architectures |
| --------- | ------------- |
| `NONE`    | all           |
| `STATIC`  | all           |
| `DYNAMIC` | all           |

### `MMap flags`{% #mmap-flags %}

MMap flags are the supported flags for the mmap syscall.

| Name                  | Architectures |
| --------------------- | ------------- |
| `MAP_SHARED`          | all           |
| `MAP_PRIVATE`         | all           |
| `MAP_SHARED_VALIDATE` | all           |
| `MAP_ANON`            | all           |
| `MAP_ANONYMOUS`       | all           |
| `MAP_DENYWRITE`       | all           |
| `MAP_EXECUTABLE`      | all           |
| `MAP_FIXED`           | all           |
| `MAP_FIXED_NOREPLACE` | all           |
| `MAP_GROWSDOWN`       | all           |
| `MAP_HUGETLB`         | all           |
| `MAP_LOCKED`          | all           |
| `MAP_NONBLOCK`        | all           |
| `MAP_NORESERVE`       | all           |
| `MAP_POPULATE`        | all           |
| `MAP_STACK`           | all           |
| `MAP_SYNC`            | all           |
| `MAP_UNINITIALIZED`   | all           |
| `MAP_HUGE_16KB`       | all           |
| `MAP_HUGE_64KB`       | all           |
| `MAP_HUGE_512KB`      | all           |
| `MAP_HUGE_1MB`        | all           |
| `MAP_HUGE_2MB`        | all           |
| `MAP_HUGE_8MB`        | all           |
| `MAP_HUGE_16MB`       | all           |
| `MAP_HUGE_32MB`       | all           |
| `MAP_HUGE_256MB`      | all           |
| `MAP_HUGE_512MB`      | all           |
| `MAP_HUGE_1GB`        | all           |
| `MAP_HUGE_2GB`        | all           |
| `MAP_HUGE_16GB`       | all           |
| `MAP_32BIT`           | amd64         |

### `Network Address Family constants`{% #network-address-family-constants %}

Network Address Family constants are the supported network address families.

| Name            | Architectures |
| --------------- | ------------- |
| `AF_UNSPEC`     | all           |
| `AF_LOCAL`      | all           |
| `AF_UNIX`       | all           |
| `AF_FILE`       | all           |
| `AF_INET`       | all           |
| `AF_AX25`       | all           |
| `AF_IPX`        | all           |
| `AF_APPLETALK`  | all           |
| `AF_NETROM`     | all           |
| `AF_BRIDGE`     | all           |
| `AF_ATMPVC`     | all           |
| `AF_X25`        | all           |
| `AF_INET6`      | all           |
| `AF_ROSE`       | all           |
| `AF_DECnet`     | all           |
| `AF_NETBEUI`    | all           |
| `AF_SECURITY`   | all           |
| `AF_KEY`        | all           |
| `AF_NETLINK`    | all           |
| `AF_ROUTE`      | all           |
| `AF_PACKET`     | all           |
| `AF_ASH`        | all           |
| `AF_ECONET`     | all           |
| `AF_ATMSVC`     | all           |
| `AF_RDS`        | all           |
| `AF_SNA`        | all           |
| `AF_IRDA`       | all           |
| `AF_PPPOX`      | all           |
| `AF_WANPIPE`    | all           |
| `AF_LLC`        | all           |
| `AF_IB`         | all           |
| `AF_MPLS`       | all           |
| `AF_CAN`        | all           |
| `AF_TIPC`       | all           |
| `AF_BLUETOOTH`  | all           |
| `AF_IUCV`       | all           |
| `AF_RXRPC`      | all           |
| `AF_ISDN`       | all           |
| `AF_PHONET`     | all           |
| `AF_IEEE802154` | all           |
| `AF_CAIF`       | all           |
| `AF_ALG`        | all           |
| `AF_NFC`        | all           |
| `AF_VSOCK`      | all           |
| `AF_KCM`        | all           |
| `AF_QIPCRTR`    | all           |
| `AF_SMC`        | all           |
| `AF_XDP`        | all           |
| `AF_MAX`        | all           |

### `Network Protocol Types`{% #network-protocol-types %}

Types of specific network protocols.

| Name                             | Architectures |
| -------------------------------- | ------------- |
| `ICMP_ECHO_REQUEST`              | all           |
| `ICMP_ECHO_REPLY`                | all           |
| `ICMP_ROUTER_SOLICITATION`       | all           |
| `ICMP_ROUTER_ADVERTISEMENT`      | all           |
| `ICMP_NEIGHBOR_SOLICITATION`     | all           |
| `ICMP_NEIGHBOR_ADVERTISEMENT`    | all           |
| `ICMP_V6_ECHO_REQUEST`           | all           |
| `ICMP_V6_ECHO_REPLY`             | all           |
| `ICMP_V6_ROUTER_SOLICITATION`    | all           |
| `ICMP_V6_ROUTER_ADVERTISEMENT`   | all           |
| `ICMP_V6_NEIGHBOR_SOLICITATION`  | all           |
| `ICMP_V6_NEIGHBOR_ADVERTISEMENT` | all           |

### `Network directions`{% #network-directions %}

Network directions are the supported directions of network packets.

| Name      | Architectures |
| --------- | ------------- |
| `INGRESS` | all           |
| `EGRESS`  | all           |

### `Open flags`{% #open-flags %}

Open flags are the supported flags for the open syscall.

| Name          | Architectures |
| ------------- | ------------- |
| `O_RDONLY`    | all           |
| `O_WRONLY`    | all           |
| `O_RDWR`      | all           |
| `O_APPEND`    | all           |
| `O_CREAT`     | all           |
| `O_EXCL`      | all           |
| `O_SYNC`      | all           |
| `O_TRUNC`     | all           |
| `O_ACCMODE`   | all           |
| `O_ASYNC`     | all           |
| `O_CLOEXEC`   | all           |
| `O_DIRECT`    | all           |
| `O_DIRECTORY` | all           |
| `O_DSYNC`     | all           |
| `O_FSYNC`     | all           |
| `O_NDELAY`    | all           |
| `O_NOATIME`   | all           |
| `O_NOCTTY`    | all           |
| `O_NOFOLLOW`  | all           |
| `O_NONBLOCK`  | all           |
| `O_RSYNC`     | all           |

### `Pipe buffer flags`{% #pipe-buffer-flags %}

Pipe buffer flags are the supported flags for a pipe buffer.

| Name                      | Architectures |
| ------------------------- | ------------- |
| `PIPE_BUF_FLAG_LRU`       | all           |
| `PIPE_BUF_FLAG_ATOMIC`    | all           |
| `PIPE_BUF_FLAG_GIFT`      | all           |
| `PIPE_BUF_FLAG_PACKET`    | all           |
| `PIPE_BUF_FLAG_CAN_MERGE` | all           |
| `PIPE_BUF_FLAG_WHOLE`     | all           |
| `PIPE_BUF_FLAG_LOSS`      | all           |

### `PrCtl Options`{% #prctl-options %}

PrCtl Options are the supported options for the prctl event

| Name                            | Architectures |
| ------------------------------- | ------------- |
| `PR_CAP_AMBIENT`                | all           |
| `PR_CAPBSET_READ`               | all           |
| `PR_CAPBSET_DROP`               | all           |
| `PR_SET_CHILD_SUBREAPER`        | all           |
| `PR_GET_CHILD_SUBREAPER`        | all           |
| `PR_SET_DUMPABLE`               | all           |
| `PR_GET_DUMPABLE`               | all           |
| `PR_SET_ENDIAN`                 | all           |
| `PR_GET_ENDIAN`                 | all           |
| `PR_SET_FP_MODE`                | all           |
| `PR_GET_FP_MODE`                | all           |
| `PR_SET_FPEMU`                  | all           |
| `PR_GET_FPEMU`                  | all           |
| `PR_SET_FPEXC`                  | all           |
| `PR_GET_FPEXC`                  | all           |
| `PR_SET_IO_FLUSHER`             | all           |
| `PR_GET_IO_FLUSHER`             | all           |
| `PR_SET_KEEPCAPS`               | all           |
| `PR_GET_KEEPCAPS`               | all           |
| `PR_MCE_KILL`                   | all           |
| `PR_MCE_KILL_GET`               | all           |
| `PR_SET_MM`                     | all           |
| `PR_SET_VMA`                    | all           |
| `PR_MPX_ENABLE_MANAGEMENT`      | all           |
| `PR_MPX_DISABLE_MANAGEMENT`     | all           |
| `PR_SET_NAME`                   | all           |
| `PR_GET_NAME`                   | all           |
| `PR_SET_NO_NEW_PRIVS`           | all           |
| `PR_GET_NO_NEW_PRIVS`           | all           |
| `PR_PAC_RESET_KEYS`             | all           |
| `PR_SET_PDEATHSIG`              | all           |
| `PR_GET_PDEATHSIG`              | all           |
| `PR_SET_PTRACER`                | all           |
| `PR_SET_SECCOMP`                | all           |
| `PR_GET_SECCOMP`                | all           |
| `PR_SET_SECUREBITS`             | all           |
| `PR_GET_SECUREBITS`             | all           |
| `PR_GET_SPECULATION_CTRL`       | all           |
| `PR_SET_SPECULATION_CTRL`       | all           |
| `PR_SVE_SET_VL`                 | all           |
| `PR_SVE_GET_VL`                 | all           |
| `PR_SET_SYSCALL_USER_DISPATCH`  | all           |
| `PR_SET_TAGGED_ADDR_CTRL`       | all           |
| `PR_GET_TAGGED_ADDR_CTRL`       | all           |
| `PR_TASK_PERF_EVENTS_DISABLE`   | all           |
| `PR_TASK_PERF_EVENTS_ENABLE`    | all           |
| `PR_SET_THP_DISABLE`            | all           |
| `PR_GET_THP_DISABLE`            | all           |
| `PR_GET_TID_ADDRESS`            | all           |
| `PR_SET_TIMERSLACK`             | all           |
| `PR_GET_TIMERSLACK`             | all           |
| `PR_SET_TIMING`                 | all           |
| `PR_GET_TIMING`                 | all           |
| `PR_SET_TSC`                    | all           |
| `PR_GET_TSC`                    | all           |
| `PR_SET_UNALIGN`                | all           |
| `PR_GET_UNALIGN`                | all           |
| `PR_GET_AUXV`                   | all           |
| `PR_SET_MDWE`                   | all           |
| `PR_GET_MDWE`                   | all           |
| `PR_RISCV_SET_ICACHE_FLUSH_CTX` | all           |

### `Protection constants`{% #protection-constants %}

Protection constants are the supported protections for the mmap syscall.

| Name             | Architectures |
| ---------------- | ------------- |
| `PROT_NONE`      | all           |
| `PROT_READ`      | all           |
| `PROT_WRITE`     | all           |
| `PROT_EXEC`      | all           |
| `PROT_GROWSDOWN` | all           |
| `PROT_GROWSUP`   | all           |

### `Ptrace constants`{% #ptrace-constants %}

Ptrace constants are the supported ptrace commands for the ptrace syscall.

| Name                          | Architectures |
| ----------------------------- | ------------- |
| `PTRACE_TRACEME`              | all           |
| `PTRACE_PEEKTEXT`             | all           |
| `PTRACE_PEEKDATA`             | all           |
| `PTRACE_PEEKUSR`              | all           |
| `PTRACE_POKETEXT`             | all           |
| `PTRACE_POKEDATA`             | all           |
| `PTRACE_POKEUSR`              | all           |
| `PTRACE_CONT`                 | all           |
| `PTRACE_KILL`                 | all           |
| `PTRACE_SINGLESTEP`           | all           |
| `PTRACE_ATTACH`               | all           |
| `PTRACE_DETACH`               | all           |
| `PTRACE_SYSCALL`              | all           |
| `PTRACE_SETOPTIONS`           | all           |
| `PTRACE_GETEVENTMSG`          | all           |
| `PTRACE_GETSIGINFO`           | all           |
| `PTRACE_SETSIGINFO`           | all           |
| `PTRACE_GETREGSET`            | all           |
| `PTRACE_SETREGSET`            | all           |
| `PTRACE_SEIZE`                | all           |
| `PTRACE_INTERRUPT`            | all           |
| `PTRACE_LISTEN`               | all           |
| `PTRACE_PEEKSIGINFO`          | all           |
| `PTRACE_GETSIGMASK`           | all           |
| `PTRACE_SETSIGMASK`           | all           |
| `PTRACE_SECCOMP_GET_FILTER`   | all           |
| `PTRACE_SECCOMP_GET_METADATA` | all           |
| `PTRACE_GET_SYSCALL_INFO`     | all           |
| `PTRACE_GETFPREGS`            | amd64, arm    |
| `PTRACE_SETFPREGS`            | amd64, arm    |
| `PTRACE_GETFPXREGS`           | amd64         |
| `PTRACE_SETFPXREGS`           | amd64         |
| `PTRACE_OLDSETOPTIONS`        | amd64, arm    |
| `PTRACE_GET_THREAD_AREA`      | amd64, arm    |
| `PTRACE_SET_THREAD_AREA`      | amd64         |
| `PTRACE_ARCH_PRCTL`           | amd64         |
| `PTRACE_SYSEMU`               | amd64, arm64  |
| `PTRACE_SYSEMU_SINGLESTEP`    | amd64, arm64  |
| `PTRACE_SINGLEBLOCK`          | amd64         |
| `PTRACE_GETCRUNCHREGS`        | arm           |
| `PTRACE_GETFDPIC`             | arm           |
| `PTRACE_GETFDPIC_EXEC`        | arm           |
| `PTRACE_GETFDPIC_INTERP`      | arm           |
| `PTRACE_GETHBPREGS`           | arm           |
| `PTRACE_GETVFPREGS`           | arm           |
| `PTRACE_GETWMMXREGS`          | arm           |
| `PTRACE_SETCRUNCHREGS`        | arm           |
| `PTRACE_SETHBPREGS`           | arm           |
| `PTRACE_SETVFPREGS`           | arm           |
| `PTRACE_SETWMMXREGS`          | arm           |
| `PTRACE_SET_SYSCALL`          | arm           |
| `PTRACE_PEEKMTETAGS`          | arm64         |
| `PTRACE_POKEMTETAGS`          | arm64         |

### `Resource limit types`{% #resource-limit-types %}

Resource limit types are the supported resource types for setrlimit syscall.

| Name                | Architectures |
| ------------------- | ------------- |
| `RLIMIT_CPU`        | all           |
| `RLIMIT_FSIZE`      | all           |
| `RLIMIT_DATA`       | all           |
| `RLIMIT_STACK`      | all           |
| `RLIMIT_CORE`       | all           |
| `RLIMIT_RSS`        | all           |
| `RLIMIT_NPROC`      | all           |
| `RLIMIT_NOFILE`     | all           |
| `RLIMIT_MEMLOCK`    | all           |
| `RLIMIT_AS`         | all           |
| `RLIMIT_LOCKS`      | all           |
| `RLIMIT_SIGPENDING` | all           |
| `RLIMIT_MSGQUEUE`   | all           |
| `RLIMIT_NICE`       | all           |
| `RLIMIT_RTPRIO`     | all           |
| `RLIMIT_RTTIME`     | all           |

### `SSHAuthMethod`{% #sshauthmethod %}

SSH authentication methods.

| Name         | Architectures |
| ------------ | ------------- |
| `password`   | all           |
| `public_key` | all           |
| `unknown`    | all           |

### `SetSockopt Levels`{% #setsockopt-levels %}

SetSockopt Levels are the supported levels for the setsockopt event.

| Name             | Architectures |
| ---------------- | ------------- |
| `IPPROTO_IP`     | all           |
| `SOL_SOCKET`     | all           |
| `IPPROTO_TCP`    | all           |
| `IPPROTO_UDP`    | all           |
| `IPPROTO_IPV6`   | all           |
| `IPPROTO_ICMPV6` | all           |

### `SetSockopt Options`{% #setsockopt-options %}

SetSockopt Options are the supported options for the setsockopt event when the level is IPPROTO_IP.

| Name                               | Architectures |
| ---------------------------------- | ------------- |
| `IP_TOS`                           | all           |
| `IP_TTL`                           | all           |
| `IP_HDRINCL`                       | all           |
| `IP_OPTIONS`                       | all           |
| `IP_ROUTER_ALERT`                  | all           |
| `IP_RECVOPTS`                      | all           |
| `IP_RETOPTS`                       | all           |
| `IP_PKTINFO`                       | all           |
| `IP_PKTOPTIONS`                    | all           |
| `IP_MTU_DISCOVER`                  | all           |
| `IP_RECVERR`                       | all           |
| `IP_RECVTTL`                       | all           |
| `IP_RECVTOS`                       | all           |
| `IP_MTU`                           | all           |
| `IP_FREEBIND`                      | all           |
| `IP_IPSEC_POLICY`                  | all           |
| `IP_XFRM_POLICY`                   | all           |
| `IP_PASSSEC`                       | all           |
| `IP_TRANSPARENT`                   | all           |
| `IP_ORIGDSTADDR`                   | all           |
| `IP_MINTTL`                        | all           |
| `IP_NODEFRAG`                      | all           |
| `IP_CHECKSUM`                      | all           |
| `IP_BIND_ADDRESS_NO_PORT`          | all           |
| `IP_RECVFRAGSIZE`                  | all           |
| `IP_RECVERR_RFC4884`               | all           |
| `IP_MULTICAST_IF`                  | all           |
| `IP_MULTICAST_TTL`                 | all           |
| `IP_MULTICAST_LOOP`                | all           |
| `IP_ADD_MEMBERSHIP`                | all           |
| `IP_DROP_MEMBERSHIP`               | all           |
| `IP_UNBLOCK_SOURCE`                | all           |
| `IP_BLOCK_SOURCE`                  | all           |
| `IP_ADD_SOURCE_MEMBERSHIP`         | all           |
| `IP_DROP_SOURCE_MEMBERSHIP`        | all           |
| `IP_MSFILTER`                      | all           |
| `MCAST_JOIN_GROUP`                 | all           |
| `MCAST_BLOCK_SOURCE`               | all           |
| `MCAST_UNBLOCK_SOURCE`             | all           |
| `MCAST_LEAVE_GROUP`                | all           |
| `MCAST_JOIN_SOURCE_GROUP`          | all           |
| `MCAST_LEAVE_SOURCE_GROUP`         | all           |
| `MCAST_MSFILTER`                   | all           |
| `IP_MULTICAST_ALL`                 | all           |
| `IP_UNICAST_IF`                    | all           |
| `SO_DEBUG`                         | all           |
| `SO_REUSEADDR`                     | all           |
| `SO_TYPE`                          | all           |
| `SO_ERROR`                         | all           |
| `SO_DONTROUTE`                     | all           |
| `SO_BROADCAST`                     | all           |
| `SO_SNDBUF`                        | all           |
| `SO_RCVBUF`                        | all           |
| `SO_KEEPALIVE`                     | all           |
| `SO_OOBINLINE`                     | all           |
| `SO_NO_CHECK`                      | all           |
| `SO_PRIORITY`                      | all           |
| `SO_LINGER`                        | all           |
| `SO_BSDCOMPAT`                     | all           |
| `SO_REUSEPORT`                     | all           |
| `SO_PASSCRED`                      | all           |
| `SO_PEERCRED`                      | all           |
| `SO_RCVLOWAT`                      | all           |
| `SO_SNDLOWAT`                      | all           |
| `SO_RCVTIMEO_OLD`                  | all           |
| `SO_SNDTIMEO_OLD`                  | all           |
| `SO_SECURITY_AUTHENTICATION`       | all           |
| `SO_SECURITY_ENCRYPTION_TRANSPORT` | all           |
| `SO_SECURITY_ENCRYPTION_NETWORK`   | all           |
| `SO_BINDTODEVICE`                  | all           |
| `SO_ATTACH_FILTER`                 | all           |
| `SO_DETACH_FILTER`                 | all           |
| `SO_PEERNAME`                      | all           |
| `SO_TIMESTAMP_OLD`                 | all           |
| `SO_ACCEPTCONN`                    | all           |
| `SO_PEERSEC`                       | all           |
| `SO_SNDBUFFORCE`                   | all           |
| `SO_RCVBUFFORCE`                   | all           |
| `SO_PASSSEC`                       | all           |
| `SO_TIMESTAMPNS_OLD`               | all           |
| `SO_MARK`                          | all           |
| `SO_TIMESTAMPING_OLD`              | all           |
| `SO_PROTOCOL`                      | all           |
| `SO_DOMAIN`                        | all           |
| `SO_RXQ_OVFL`                      | all           |
| `SO_WIFI_STATUS`                   | all           |
| `SO_PEEK_OFF`                      | all           |
| `SO_NOFCS`                         | all           |
| `SO_LOCK_FILTER`                   | all           |
| `SO_SELECT_ERR_QUEUE`              | all           |
| `SO_BUSY_POLL`                     | all           |
| `SO_MAX_PACING_RATE`               | all           |
| `SO_BPF_EXTENSIONS`                | all           |
| `SO_INCOMING_CPU`                  | all           |
| `SO_ATTACH_BPF`                    | all           |
| `SO_ATTACH_REUSEPORT_CBPF`         | all           |
| `SO_ATTACH_REUSEPORT_EBPF`         | all           |
| `SO_CNX_ADVICE`                    | all           |
| `SCM_TIMESTAMPING_OPT_STATS`       | all           |
| `SO_MEMINFO`                       | all           |
| `SO_INCOMING_NAPI_ID`              | all           |
| `SO_COOKIE`                        | all           |
| `SCM_TIMESTAMPING_PKTINFO`         | all           |
| `SO_PEERGROUPS`                    | all           |
| `SO_ZEROCOPY`                      | all           |
| `SO_TXTIME`                        | all           |
| `SO_BINDTOIFINDEX`                 | all           |
| `SO_TIMESTAMP_NEW`                 | all           |
| `SO_TIMESTAMPNS_NEW`               | all           |
| `SO_TIMESTAMPING_NEW`              | all           |
| `SO_RCVTIMEO_NEW`                  | all           |
| `SO_SNDTIMEO_NEW`                  | all           |
| `SO_DETACH_REUSEPORT_BPF`          | all           |
| `SO_PREFER_BUSY_POLL`              | all           |
| `SO_BUSY_POLL_BUDGET`              | all           |
| `SO_NETNS_COOKIE`                  | all           |
| `SO_BUF_LOCK`                      | all           |
| `SO_RESERVE_MEM`                   | all           |
| `SO_TXREHASH`                      | all           |
| `SO_RCVMARK`                       | all           |
| `SO_PASSPIDFD`                     | all           |
| `SO_PEERPIDFD`                     | all           |
| `SO_DEVMEM_LINEAR`                 | all           |
| `SO_DEVMEM_DMABUF`                 | all           |
| `SO_DEVMEM_DONTNEED`               | all           |
| `SCM_TS_OPT_ID`                    | all           |
| `SO_RCVPRIORITY`                   | all           |
| `TCP_NODELAY`                      | all           |
| `TCP_MAXSEG`                       | all           |
| `TCP_CORK`                         | all           |
| `TCP_KEEPIDLE`                     | all           |
| `TCP_KEEPINTVL`                    | all           |
| `TCP_KEEPCNT`                      | all           |
| `TCP_SYNCNT`                       | all           |
| `TCP_LINGER2`                      | all           |
| `TCP_DEFER_ACCEPT`                 | all           |
| `TCP_WINDOW_CLAMP`                 | all           |
| `TCP_INFO`                         | all           |
| `TCP_QUICKACK`                     | all           |
| `TCP_CONGESTION`                   | all           |
| `TCP_MD5SIG`                       | all           |
| `TCP_THIN_LINEAR_TIMEOUTS`         | all           |
| `TCP_THIN_DUPACK`                  | all           |
| `TCP_USER_TIMEOUT`                 | all           |
| `TCP_REPAIR`                       | all           |
| `TCP_REPAIR_QUEUE`                 | all           |
| `TCP_QUEUE_SEQ`                    | all           |
| `TCP_REPAIR_OPTIONS`               | all           |
| `TCP_FASTOPEN`                     | all           |
| `TCP_TIMESTAMP`                    | all           |
| `TCP_NOTSENT_LOWAT`                | all           |
| `TCP_CC_INFO`                      | all           |
| `TCP_SAVE_SYN`                     | all           |
| `TCP_SAVED_SYN`                    | all           |
| `TCP_REPAIR_WINDOW`                | all           |
| `TCP_FASTOPEN_CONNECT`             | all           |
| `TCP_ULP`                          | all           |
| `TCP_MD5SIG_EXT`                   | all           |
| `TCP_FASTOPEN_KEY`                 | all           |
| `TCP_FASTOPEN_NO_COOKIE`           | all           |
| `TCP_ZEROCOPY_RECEIVE`             | all           |
| `TCP_INQ`                          | all           |
| `TCP_TX_DELAY`                     | all           |
| `IPV6_ADDRFORM`                    | all           |
| `IPV6_2292PKTINFO`                 | all           |
| `IPV6_2292HOPOPTS`                 | all           |
| `IPV6_2292DSTOPTS`                 | all           |
| `IPV6_2292RTHDR`                   | all           |
| `IPV6_2292PKTOPTIONS`              | all           |
| `IPV6_2292HOPLIMIT`                | all           |
| `IPV6_FLOWINFO`                    | all           |
| `IPV6_UNICAST_HOPS`                | all           |
| `IPV6_MULTICAST_IF`                | all           |
| `IPV6_MULTICAST_HOPS`              | all           |
| `IPV6_MULTICAST_LOOP`              | all           |
| `IPV6_ADD_MEMBERSHIP`              | all           |
| `IPV6_DROP_MEMBERSHIP`             | all           |
| `IPV6_ROUTER_ALERT`                | all           |
| `IPV6_MTU_DISCOVER`                | all           |
| `IPV6_MTU`                         | all           |
| `IPV6_RECVERR`                     | all           |
| `IPV6_V6ONLY`                      | all           |
| `IPV6_JOIN_ANYCAST`                | all           |
| `IPV6_LEAVE_ANYCAST`               | all           |
| `IPV6_MULTICAST_ALL`               | all           |
| `IPV6_ROUTER_ALERT_ISOLATE`        | all           |
| `IPV6_RECVERR_RFC4884`             | all           |
| `IPV6_FLOWLABEL_MGR`               | all           |
| `IPV6_FLOWINFO_SEND`               | all           |
| `IPV6_IPSEC_POLICY`                | all           |
| `IPV6_XFRM_POLICY`                 | all           |
| `IPV6_HDRINCL`                     | all           |
| `IPV6_RECVPKTINFO`                 | all           |
| `IPV6_PKTINFO`                     | all           |
| `IPV6_RECVHOPLIMIT`                | all           |
| `IPV6_HOPLIMIT`                    | all           |
| `IPV6_RECVHOPOPTS`                 | all           |
| `IPV6_HOPOPTS`                     | all           |
| `IPV6_RTHDRDSTOPTS`                | all           |
| `IPV6_RECVRTHDR`                   | all           |
| `IPV6_RTHDR`                       | all           |
| `IPV6_RECVDSTOPTS`                 | all           |
| `IPV6_DSTOPTS`                     | all           |
| `IPV6_RECVPATHMTU`                 | all           |
| `IPV6_PATHMTU`                     | all           |
| `IPV6_DONTFRAG`                    | all           |
| `IPV6_RECVTCLASS`                  | all           |
| `IPV6_TCLASS`                      | all           |
| `IPV6_AUTOFLOWLABEL`               | all           |
| `IPV6_ADDR_PREFERENCES`            | all           |
| `IPV6_MINHOPCOUNT`                 | all           |
| `IPV6_ORIGDSTADDR`                 | all           |
| `IPV6_TRANSPARENT`                 | all           |
| `IPV6_UNICAST_IF`                  | all           |
| `IPV6_RECVFRAGSIZE`                | all           |
| `IPV6_FREEBIND`                    | all           |

### `Signal constants`{% #signal-constants %}

Signal constants are the supported signals for the kill syscall.

| Name        | Architectures |
| ----------- | ------------- |
| `SIGHUP`    | all           |
| `SIGINT`    | all           |
| `SIGQUIT`   | all           |
| `SIGILL`    | all           |
| `SIGTRAP`   | all           |
| `SIGABRT`   | all           |
| `SIGIOT`    | all           |
| `SIGBUS`    | all           |
| `SIGFPE`    | all           |
| `SIGKILL`   | all           |
| `SIGUSR1`   | all           |
| `SIGSEGV`   | all           |
| `SIGUSR2`   | all           |
| `SIGPIPE`   | all           |
| `SIGALRM`   | all           |
| `SIGTERM`   | all           |
| `SIGSTKFLT` | all           |
| `SIGCHLD`   | all           |
| `SIGCONT`   | all           |
| `SIGSTOP`   | all           |
| `SIGTSTP`   | all           |
| `SIGTTIN`   | all           |
| `SIGTTOU`   | all           |
| `SIGURG`    | all           |
| `SIGXCPU`   | all           |
| `SIGXFSZ`   | all           |
| `SIGVTALRM` | all           |
| `SIGPROF`   | all           |
| `SIGWINCH`  | all           |
| `SIGIO`     | all           |
| `SIGPOLL`   | all           |
| `SIGPWR`    | all           |
| `SIGSYS`    | all           |

### `Socket types`{% #socket-types %}

Socket types are the supported socket types.

| Name             | Architectures |
| ---------------- | ------------- |
| `SOCK_STREAM`    | all           |
| `SOCK_DGRAM`     | all           |
| `SOCK_RAW`       | all           |
| `SOCK_RDM`       | all           |
| `SOCK_SEQPACKET` | all           |
| `SOCK_DCCP`      | all           |
| `SOCK_PACKET`    | all           |

### `SysCtl Actions`{% #sysctl-actions %}

SysCtl Actions are the supported actions for the sysctl event.

| Name           | Architectures |
| -------------- | ------------- |
| `SYSCTL_READ`  | all           |
| `SYSCTL_WRITE` | all           |

### `Unlink flags`{% #unlink-flags %}

Unlink flags are the supported flags for the unlink syscall.

| Name           | Architectures |
| -------------- | ------------- |
| `AT_REMOVEDIR` | all           |

### `UserSessionTypes`{% #usersessiontypes %}

UserSessionTypes are the supported user session types.

| Name      | Architectures |
| --------- | ------------- |
| `unknown` | all           |
| `k8s`     | all           |
| `ssh`     | all           |

### `Virtual Memory flags`{% #virtual-memory-flags %}

Virtual Memory flags define the protection of a virtual memory segment.

| Name              | Architectures |
| ----------------- | ------------- |
| `VM_NONE`         | all           |
| `VM_READ`         | all           |
| `VM_WRITE`        | all           |
| `VM_EXEC`         | all           |
| `VM_SHARED`       | all           |
| `VM_MAYREAD`      | all           |
| `VM_MAYWRITE`     | all           |
| `VM_MAYEXEC`      | all           |
| `VM_MAYSHARE`     | all           |
| `VM_GROWSDOWN`    | all           |
| `VM_UFFD_MISSING` | all           |
| `VM_PFNMAP`       | all           |
| `VM_UFFD_WP`      | all           |
| `VM_LOCKED`       | all           |
| `VM_IO`           | all           |
| `VM_SEQ_READ`     | all           |
| `VM_RAND_READ`    | all           |
| `VM_DONTCOPY`     | all           |
| `VM_DONTEXPAND`   | all           |
| `VM_LOCKONFAULT`  | all           |
| `VM_ACCOUNT`      | all           |
| `VM_NORESERVE`    | all           |
| `VM_HUGETLB`      | all           |
| `VM_SYNC`         | all           |
| `VM_ARCH_1`       | all           |
| `VM_WIPEONFORK`   | all           |
| `VM_DONTDUMP`     | all           |
| `VM_SOFTDIRTY`    | all           |
| `VM_MIXEDMAP`     | all           |
| `VM_HUGEPAGE`     | all           |
| `VM_NOHUGEPAGE`   | all           |
| `VM_MERGEABLE`    | all           |

- [Get started with Datadog Workload Protection](https://docs.datadoghq.com/security/cloud_workload_security/getting_started/)
