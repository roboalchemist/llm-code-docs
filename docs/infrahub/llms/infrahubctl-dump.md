# Source: https://docs.infrahub.app/infrahubctl/infrahubctl-dump.md

# `infrahubctl dump`

Export nodes and their relationships out of the database.

**Usage**:

```
$ infrahubctl dump [OPTIONS]
```

**Options**:

* `--namespace TEXT`: Namespace(s) to export
* `--directory PATH`: Directory path to store export \[default: (dynamic)]
* `--quiet / --no-quiet`: No console output \[default: no-quiet]
* `--config-file TEXT`: \[env var: INFRAHUBCTL\_CONFIG; default: infrahubctl.toml]
* `--branch TEXT`: Branch from which to export
* `--concurrent INTEGER`: Maximum number of requests to execute at the same time. \[env var: INFRAHUB\_MAX\_CONCURRENT\_EXECUTION; default: 4]
* `--timeout INTEGER`: Timeout in sec \[env var: INFRAHUB\_TIMEOUT; default: 60]
* `--exclude TEXT`: Prevent node kind(s) from being exported, CoreAccount is excluded by default \[default: CoreAccount]
* `--install-completion`: Install completion for the current shell.
* `--show-completion`: Show completion for the current shell, to copy it or customize the installation.
* `--help`: Show this message and exit.
