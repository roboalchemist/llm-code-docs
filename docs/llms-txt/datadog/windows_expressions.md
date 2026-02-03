# Source: https://docs.datadoghq.com/security/workload_protection/windows_expressions.md

---
title: Windows Agent attributes and helpers
description: Windows Agent attributes and helpers for Workload Protection Rules
breadcrumbs: >-
  Docs > Datadog Security > Workload Protection > Windows Agent attributes and
  helpers
---

# Windows Agent attributes and helpers

## Windows Agent attributes and helpers{% #windows-agent-attributes-and-helpers %}

This documentation describes Windows attributes and helpers of the [Datadog's Security Language (SECL)](https://docs.datadoghq.com/security/threats/agent).

Rules using Windows attributes and helpers must include an OS rule filter field as follows.

```yaml
id: [...]
expression: [...]
filters:
  - os == "windows"
```

## Triggers{% #triggers %}

Triggers are events that correspond to types of activity seen by the system. The currently supported set of triggers is:

| SECL Event          | Type     | Definition                       | Agent Version |
| ------------------- | -------- | -------------------------------- | ------------- |
| `change_permission` | Registry | A permission change was made     | 7.55          |
| `create`            | File     | A file was created               | 7.52          |
| `create_key`        | Registry | A registry key was created       | 7.52          |
| `delete`            | File     | A file was deleted               | 7.54          |
| `delete_key`        | Registry | A registry key was deleted       | 7.52          |
| `exec`              | Process  | A process was executed or forked | 7.27          |
| `exit`              | Process  | A process was terminated         | 7.38          |
| `open_key`          | Registry | A registry key was opened        | 7.52          |
| `rename`            | File     | A file was renamed               | 7.54          |
| `set_key_value`     | Registry | A registry key value was set     | 7.52          |
| `write`             | File     | A file was written               | 7.54          |

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

## Event attributes{% #event-attributes %}

### Common to all event types{% #common-to-all-event-types %}

| Property                                 | Definition                                                                 |
| ---------------------------------------- | -------------------------------------------------------------------------- |
| `event.hostname`                         | Hostname associated with the event                                         |
| `event.origin`                           | Origin of the event                                                        |
| `event.os`                               | Operating system of the event                                              |
| `event.rule.tags`                        | Tags associated with the rule that's used to evaluate the event            |
| `event.service`                          | Service associated with the event                                          |
| `event.source`                           | [Experimental] Source of the event. Can be either 'runtime' or 'snapshot'. |
| `event.timestamp`                        | Timestamp of the event                                                     |
| `process.ancestors.cmdline`              | Command line of the process                                                |
| `process.ancestors.container.created_at` | Timestamp of the creation of the container                                 |
| `process.ancestors.container.id`         | ID of the container                                                        |
| `process.ancestors.container.tags`       | Tags of the container                                                      |
| `process.ancestors.created_at`           | Timestamp of the creation of the process                                   |
| `process.ancestors.envp`                 | Environment variables of the process                                       |
| `process.ancestors.envs`                 | Environment variable names of the process                                  |
| `process.ancestors.file.extension`       | File's extension                                                           |
| `process.ancestors.file.name`            | File's basename                                                            |
| `process.ancestors.file.name.length`     | Length of the corresponding element                                        |
| `process.ancestors.file.path`            | File's path                                                                |
| `process.ancestors.file.path.length`     | Length of the corresponding element                                        |
| `process.ancestors.length`               | Length of the corresponding element                                        |
| `process.ancestors.pid`                  | Process ID of the process (also called thread group ID)                    |
| `process.ancestors.ppid`                 | Parent process ID                                                          |
| `process.ancestors.user`                 | User name                                                                  |
| `process.ancestors.user_sid`             | Sid of the user of the process                                             |
| `process.cmdline`                        | Command line of the process                                                |
| `process.container.created_at`           | Timestamp of the creation of the container                                 |
| `process.container.id`                   | ID of the container                                                        |
| `process.container.tags`                 | Tags of the container                                                      |
| `process.created_at`                     | Timestamp of the creation of the process                                   |
| `process.envp`                           | Environment variables of the process                                       |
| `process.envs`                           | Environment variable names of the process                                  |
| `process.file.extension`                 | File's extension                                                           |
| `process.file.name`                      | File's basename                                                            |
| `process.file.name.length`               | Length of the corresponding element                                        |
| `process.file.path`                      | File's path                                                                |
| `process.file.path.length`               | Length of the corresponding element                                        |
| `process.parent.cmdline`                 | Command line of the process                                                |
| `process.parent.container.created_at`    | Timestamp of the creation of the container                                 |
| `process.parent.container.id`            | ID of the container                                                        |
| `process.parent.container.tags`          | Tags of the container                                                      |
| `process.parent.created_at`              | Timestamp of the creation of the process                                   |
| `process.parent.envp`                    | Environment variables of the process                                       |
| `process.parent.envs`                    | Environment variable names of the process                                  |
| `process.parent.file.extension`          | File's extension                                                           |
| `process.parent.file.name`               | File's basename                                                            |
| `process.parent.file.name.length`        | Length of the corresponding element                                        |
| `process.parent.file.path`               | File's path                                                                |
| `process.parent.file.path.length`        | Length of the corresponding element                                        |
| `process.parent.pid`                     | Process ID of the process (also called thread group ID)                    |
| `process.parent.ppid`                    | Parent process ID                                                          |
| `process.parent.user`                    | User name                                                                  |
| `process.parent.user_sid`                | Sid of the user of the process                                             |
| `process.pid`                            | Process ID of the process (also called thread group ID)                    |
| `process.ppid`                           | Parent process ID                                                          |
| `process.user`                           | User name                                                                  |
| `process.user_sid`                       | Sid of the user of the process                                             |

### Event `change_permission`{% #event-change_permission %}

A permission change was made

| Property                        | Definition                                                                 |
| ------------------------------- | -------------------------------------------------------------------------- |
| `change_permission.new_sd`      | New Security Descriptor of the object of which permission was changed      |
| `change_permission.old_sd`      | Original Security Descriptor of the object of which permission was changed |
| `change_permission.path`        | Name of the object of which permission was changed                         |
| `change_permission.type`        | Type of the object of which permission was changed                         |
| `change_permission.user_domain` | Domain name of the permission change author                                |
| `change_permission.username`    | Username of the permission change author                                   |

### Event `create`{% #event-create %}

A file was created

| Property                         | Definition                          |
| -------------------------------- | ----------------------------------- |
| `create.file.device_path`        | File's path                         |
| `create.file.device_path.length` | Length of the corresponding element |
| `create.file.extension`          | File's extension                    |
| `create.file.name`               | File's basename                     |
| `create.file.name.length`        | Length of the corresponding element |
| `create.file.path`               | File's path                         |
| `create.file.path.length`        | Length of the corresponding element |

### Event `create_key`{% #event-create_key %}

A registry key was created

| Property                              | Definition                          |
| ------------------------------------- | ----------------------------------- |
| `create.registry.key_name`            | Registry's name                     |
| `create.registry.key_name.length`     | Length of the corresponding element |
| `create.registry.key_path`            | Registry's path                     |
| `create.registry.key_path.length`     | Length of the corresponding element |
| `create_key.registry.key_name`        | Registry's name                     |
| `create_key.registry.key_name.length` | Length of the corresponding element |
| `create_key.registry.key_path`        | Registry's path                     |
| `create_key.registry.key_path.length` | Length of the corresponding element |

### Event `delete`{% #event-delete %}

A file was deleted

| Property                         | Definition                          |
| -------------------------------- | ----------------------------------- |
| `delete.file.device_path`        | File's path                         |
| `delete.file.device_path.length` | Length of the corresponding element |
| `delete.file.extension`          | File's extension                    |
| `delete.file.name`               | File's basename                     |
| `delete.file.name.length`        | Length of the corresponding element |
| `delete.file.path`               | File's path                         |
| `delete.file.path.length`        | Length of the corresponding element |

### Event `delete_key`{% #event-delete_key %}

A registry key was deleted

| Property                              | Definition                          |
| ------------------------------------- | ----------------------------------- |
| `delete.registry.key_name`            | Registry's name                     |
| `delete.registry.key_name.length`     | Length of the corresponding element |
| `delete.registry.key_path`            | Registry's path                     |
| `delete.registry.key_path.length`     | Length of the corresponding element |
| `delete_key.registry.key_name`        | Registry's name                     |
| `delete_key.registry.key_name.length` | Length of the corresponding element |
| `delete_key.registry.key_path`        | Registry's path                     |
| `delete_key.registry.key_path.length` | Length of the corresponding element |

### Event `exec`{% #event-exec %}

A process was executed or forked

| Property                    | Definition                                              |
| --------------------------- | ------------------------------------------------------- |
| `exec.cmdline`              | Command line of the process                             |
| `exec.container.created_at` | Timestamp of the creation of the container              |
| `exec.container.id`         | ID of the container                                     |
| `exec.container.tags`       | Tags of the container                                   |
| `exec.created_at`           | Timestamp of the creation of the process                |
| `exec.envp`                 | Environment variables of the process                    |
| `exec.envs`                 | Environment variable names of the process               |
| `exec.file.extension`       | File's extension                                        |
| `exec.file.name`            | File's basename                                         |
| `exec.file.name.length`     | Length of the corresponding element                     |
| `exec.file.path`            | File's path                                             |
| `exec.file.path.length`     | Length of the corresponding element                     |
| `exec.pid`                  | Process ID of the process (also called thread group ID) |
| `exec.ppid`                 | Parent process ID                                       |
| `exec.user`                 | User name                                               |
| `exec.user_sid`             | Sid of the user of the process                          |

### Event `exit`{% #event-exit %}

A process was terminated

| Property                    | Definition                                                                            |
| --------------------------- | ------------------------------------------------------------------------------------- |
| `exit.cause`                | Cause of the process termination (one of EXITED, SIGNALED, COREDUMPED)                |
| `exit.cmdline`              | Command line of the process                                                           |
| `exit.code`                 | Exit code of the process or number of the signal that caused the process to terminate |
| `exit.container.created_at` | Timestamp of the creation of the container                                            |
| `exit.container.id`         | ID of the container                                                                   |
| `exit.container.tags`       | Tags of the container                                                                 |
| `exit.created_at`           | Timestamp of the creation of the process                                              |
| `exit.envp`                 | Environment variables of the process                                                  |
| `exit.envs`                 | Environment variable names of the process                                             |
| `exit.file.extension`       | File's extension                                                                      |
| `exit.file.name`            | File's basename                                                                       |
| `exit.file.name.length`     | Length of the corresponding element                                                   |
| `exit.file.path`            | File's path                                                                           |
| `exit.file.path.length`     | Length of the corresponding element                                                   |
| `exit.pid`                  | Process ID of the process (also called thread group ID)                               |
| `exit.ppid`                 | Parent process ID                                                                     |
| `exit.user`                 | User name                                                                             |
| `exit.user_sid`             | Sid of the user of the process                                                        |

### Event `open_key`{% #event-open_key %}

A registry key was opened

| Property                            | Definition                          |
| ----------------------------------- | ----------------------------------- |
| `open.registry.key_name`            | Registry's name                     |
| `open.registry.key_name.length`     | Length of the corresponding element |
| `open.registry.key_path`            | Registry's path                     |
| `open.registry.key_path.length`     | Length of the corresponding element |
| `open_key.registry.key_name`        | Registry's name                     |
| `open_key.registry.key_name.length` | Length of the corresponding element |
| `open_key.registry.key_path`        | Registry's path                     |
| `open_key.registry.key_path.length` | Length of the corresponding element |

### Event `rename`{% #event-rename %}

A file was renamed

| Property                                     | Definition                          |
| -------------------------------------------- | ----------------------------------- |
| `rename.file.destination.device_path`        | File's path                         |
| `rename.file.destination.device_path.length` | Length of the corresponding element |
| `rename.file.destination.extension`          | File's extension                    |
| `rename.file.destination.name`               | File's basename                     |
| `rename.file.destination.name.length`        | Length of the corresponding element |
| `rename.file.destination.path`               | File's path                         |
| `rename.file.destination.path.length`        | Length of the corresponding element |
| `rename.file.device_path`                    | File's path                         |
| `rename.file.device_path.length`             | Length of the corresponding element |
| `rename.file.extension`                      | File's extension                    |
| `rename.file.name`                           | File's basename                     |
| `rename.file.name.length`                    | Length of the corresponding element |
| `rename.file.path`                           | File's path                         |
| `rename.file.path.length`                    | Length of the corresponding element |

### Event `set_key_value`{% #event-set_key_value %}

A registry key value was set

| Property                                   | Definition                          |
| ------------------------------------------ | ----------------------------------- |
| `set.registry.key_name`                    | Registry's name                     |
| `set.registry.key_name.length`             | Length of the corresponding element |
| `set.registry.key_path`                    | Registry's path                     |
| `set.registry.key_path.length`             | Length of the corresponding element |
| `set.registry.value_name`                  | Registry's value name               |
| `set.registry.value_name.length`           | Length of the corresponding element |
| `set.value_name`                           | Registry's value name               |
| `set_key_value.registry.key_name`          | Registry's name                     |
| `set_key_value.registry.key_name.length`   | Length of the corresponding element |
| `set_key_value.registry.key_path`          | Registry's path                     |
| `set_key_value.registry.key_path.length`   | Length of the corresponding element |
| `set_key_value.registry.value_name`        | Registry's value name               |
| `set_key_value.registry.value_name.length` | Length of the corresponding element |
| `set_key_value.value_name`                 | Registry's value name               |

### Event `write`{% #event-write %}

A file was written

| Property                        | Definition                          |
| ------------------------------- | ----------------------------------- |
| `write.file.device_path`        | File's path                         |
| `write.file.device_path.length` | Length of the corresponding element |
| `write.file.extension`          | File's extension                    |
| `write.file.name`               | File's basename                     |
| `write.file.name.length`        | Length of the corresponding element |
| `write.file.path`               | File's path                         |
| `write.file.path.length`        | Length of the corresponding element |

## Attributes documentation{% #attributes-documentation %}

### `*.cmdline`{% #common-process-cmdline-doc %}

Type: string

Definition: Command line of the process

`*.cmdline` has 5 possible prefixes: `exec` `exit` `process` `process.ancestors` `process.parent`

Example:

```javascript
exec.cmdline == "-sV -p 22,53,110,143,4564 198.116.0-255.1-127"
```

Matches any process with these exact arguments.

Example:

```javascript
exec.cmdline =~ "* -F * http*"
```

Matches any process that has the "-F" argument anywhere before an argument starting with "http".

### `*.created_at`{% #common-containercontext-created_at-doc %}

Type: int

Definition: Timestamp of the creation of the container

`*.created_at` has 5 possible prefixes: `exec.container` `exit.container` `process.ancestors.container` `process.container` `process.parent.container`

### `*.created_at`{% #common-process-created_at-doc %}

Type: int

Definition: Timestamp of the creation of the process

`*.created_at` has 5 possible prefixes: `exec` `exit` `process` `process.ancestors` `process.parent`

### `*.device_path`{% #common-fimfileevent-device_path-doc %}

Type: string

Definition: File's path

`*.device_path` has 5 possible prefixes: `create.file` `delete.file` `rename.file` `rename.file.destination` `write.file`

Example:

```javascript
create.file.device_path == "\device\harddisk1\cmd.bat"
```

Matches the creation of the file located at c:\cmd.bat

### `*.envp`{% #common-process-envp-doc %}

Type: string

Definition: Environment variables of the process

`*.envp` has 5 possible prefixes: `exec` `exit` `process` `process.ancestors` `process.parent`

### `*.envs`{% #common-process-envs-doc %}

Type: string

Definition: Environment variable names of the process

`*.envs` has 5 possible prefixes: `exec` `exit` `process` `process.ancestors` `process.parent`

### `*.extension`{% #common-fileevent-extension-doc %}

Type: string

Definition: File's extension

`*.extension` has 5 possible prefixes: `exec.file` `exit.file` `process.ancestors.file` `process.file` `process.parent.file`

### `*.extension`{% #common-fimfileevent-extension-doc %}

Type: string

Definition: File's extension

`*.extension` has 5 possible prefixes: `create.file` `delete.file` `rename.file` `rename.file.destination` `write.file`

### `*.id`{% #common-containercontext-id-doc %}

Type: string

Definition: ID of the container

`*.id` has 5 possible prefixes: `exec.container` `exit.container` `process.ancestors.container` `process.container` `process.parent.container`

### `*.key_name`{% #common-registryevent-key_name-doc %}

Type: string

Definition: Registry's name

`*.key_name` has 8 possible prefixes: `create.registry` `create_key.registry` `delete.registry` `delete_key.registry` `open.registry` `open_key.registry` `set.registry` `set_key_value.registry`

### `*.key_path`{% #common-registryevent-key_path-doc %}

Type: string

Definition: Registry's path

`*.key_path` has 8 possible prefixes: `create.registry` `create_key.registry` `delete.registry` `delete_key.registry` `open.registry` `open_key.registry` `set.registry` `set_key_value.registry`

### `*.length`{% #common-string-length-doc %}

Type: int

Definition: Length of the corresponding element

`*.length` has 44 possible prefixes: `create.file.device_path` `create.file.name` `create.file.path` `create.registry.key_name` `create.registry.key_path` `create_key.registry.key_name` `create_key.registry.key_path` `delete.file.device_path` `delete.file.name` `delete.file.path` `delete.registry.key_name` `delete.registry.key_path` `delete_key.registry.key_name` `delete_key.registry.key_path` `exec.file.name` `exec.file.path` `exit.file.name` `exit.file.path` `open.registry.key_name` `open.registry.key_path` `open_key.registry.key_name` `open_key.registry.key_path` `process.ancestors` `process.ancestors.file.name` `process.ancestors.file.path` `process.file.name` `process.file.path` `process.parent.file.name` `process.parent.file.path` `rename.file.destination.device_path` `rename.file.destination.name` `rename.file.destination.path` `rename.file.device_path` `rename.file.name` `rename.file.path` `set.registry.key_name` `set.registry.key_path` `set.registry.value_name` `set_key_value.registry.key_name` `set_key_value.registry.key_path` `set_key_value.registry.value_name` `write.file.device_path` `write.file.name` `write.file.path`

### `*.name`{% #common-fileevent-name-doc %}

Type: string

Definition: File's basename

`*.name` has 5 possible prefixes: `exec.file` `exit.file` `process.ancestors.file` `process.file` `process.parent.file`

Example:

```javascript
exec.file.name == "cmd.bat"
```

Matches the execution of any file named cmd.bat.

### `*.name`{% #common-fimfileevent-name-doc %}

Type: string

Definition: File's basename

`*.name` has 5 possible prefixes: `create.file` `delete.file` `rename.file` `rename.file.destination` `write.file`

Example:

```javascript
create.file.name == "cmd.bat"
```

Matches the creation of any file named cmd.bat.

### `*.path`{% #common-fileevent-path-doc %}

Type: string

Definition: File's path

`*.path` has 5 possible prefixes: `exec.file` `exit.file` `process.ancestors.file` `process.file` `process.parent.file`

Example:

```javascript
exec.file.path == "c:\cmd.bat"
```

Matches the execution of the file located at c:\cmd.bat

### `*.path`{% #common-fimfileevent-path-doc %}

Type: string

Definition: File's path

`*.path` has 5 possible prefixes: `create.file` `delete.file` `rename.file` `rename.file.destination` `write.file`

Example:

```javascript
create.file.path == "c:\cmd.bat"
```

Matches the creation of the file located at c:\cmd.bat

### `*.pid`{% #common-pidcontext-pid-doc %}

Type: int

Definition: Process ID of the process (also called thread group ID)

`*.pid` has 5 possible prefixes: `exec` `exit` `process` `process.ancestors` `process.parent`

### `*.ppid`{% #common-process-ppid-doc %}

Type: int

Definition: Parent process ID

`*.ppid` has 5 possible prefixes: `exec` `exit` `process` `process.ancestors` `process.parent`

### `*.registry.value_name`{% #common-setregistrykeyvalueevent-registry-value_name-doc %}

Type: string

Definition: Registry's value name

`*.registry.value_name` has 2 possible prefixes: `set` `set_key_value`

### `*.tags`{% #common-containercontext-tags-doc %}

Type: string

Definition: Tags of the container

`*.tags` has 5 possible prefixes: `exec.container` `exit.container` `process.ancestors.container` `process.container` `process.parent.container`

### `*.user`{% #common-process-user-doc %}

Type: string

Definition: User name

`*.user` has 5 possible prefixes: `exec` `exit` `process` `process.ancestors` `process.parent`

### `*.user_sid`{% #common-process-user_sid-doc %}

Type: string

Definition: Sid of the user of the process

`*.user_sid` has 5 possible prefixes: `exec` `exit` `process` `process.ancestors` `process.parent`

### `*.value_name`{% #common-setregistrykeyvalueevent-value_name-doc %}

Type: string

Definition: Registry's value name

`*.value_name` has 2 possible prefixes: `set` `set_key_value`

### `change_permission.new_sd`{% #change_permission-new_sd-doc %}

Type: string

Definition: New Security Descriptor of the object of which permission was changed

### `change_permission.old_sd`{% #change_permission-old_sd-doc %}

Type: string

Definition: Original Security Descriptor of the object of which permission was changed

### `change_permission.path`{% #change_permission-path-doc %}

Type: string

Definition: Name of the object of which permission was changed

### `change_permission.type`{% #change_permission-type-doc %}

Type: string

Definition: Type of the object of which permission was changed

### `change_permission.user_domain`{% #change_permission-user_domain-doc %}

Type: string

Definition: Domain name of the permission change author

### `change_permission.username`{% #change_permission-username-doc %}

Type: string

Definition: Username of the permission change author

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

### `event.source`{% #event-source-doc %}

Type: string

Definition: [Experimental] Source of the event. Can be either 'runtime' or 'snapshot'.

### `event.timestamp`{% #event-timestamp-doc %}

Type: int

Definition: Timestamp of the event

### `exit.cause`{% #exit-cause-doc %}

Type: int

Definition: Cause of the process termination (one of EXITED, SIGNALED, COREDUMPED)

### `exit.code`{% #exit-code-doc %}

Type: int

Definition: Exit code of the process or number of the signal that caused the process to terminate

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

### `SSHAuthMethod`{% #sshauthmethod %}

SSH authentication methods.

| Name         | Architectures |
| ------------ | ------------- |
| `password`   | all           |
| `public_key` | all           |
| `unknown`    | all           |

### `UserSessionTypes`{% #usersessiontypes %}

UserSessionTypes are the supported user session types.

| Name      | Architectures |
| --------- | ------------- |
| `unknown` | all           |
| `k8s`     | all           |
| `ssh`     | all           |

- [Get started with Datadog Workload Protection](https://docs.datadoghq.com/security/cloud_workload_security/getting_started/)
