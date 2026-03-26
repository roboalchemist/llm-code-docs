# Source: https://docs.infrahub.app/infrahubctl/infrahubctl-task.md

# `infrahubctl task`

Manage Infrahub tasks.

**Usage**:

```
$ infrahubctl task [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--install-completion`: Install completion for the current shell.
* `--show-completion`: Show completion for the current shell, to copy it or customize the installation.
* `--help`: Show this message and exit.

**Commands**:

* `list`: List Infrahub tasks.

## `infrahubctl task list`[​](#infrahubctl-task-list "Direct link to infrahubctl-task-list")

List Infrahub tasks.

**Usage**:

```
$ infrahubctl task list [OPTIONS]
```

**Options**:

* `-s, --state TEXT`: Filter by task state. Can be provided multiple times.
* `--limit INTEGER`: Maximum number of tasks to retrieve.
* `--offset INTEGER`: Offset for pagination.
* `--include-related-nodes / --no-include-related-nodes`: Include related nodes in the output. \[default: no-include-related-nodes]
* `--include-logs / --no-include-logs`: Include task logs in the output. \[default: no-include-logs]
* `--json`: Output the result as JSON.
* `--debug / --no-debug`: \[default: no-debug]
* `--config-file TEXT`: \[env var: INFRAHUBCTL\_CONFIG; default: infrahubctl.toml]
* `--help`: Show this message and exit.
