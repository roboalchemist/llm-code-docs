# Source: https://docs.infrahub.app/infrahubctl/infrahubctl-load.md

# `infrahubctl load`

Import nodes and their relationships into the database.

**Usage**:

```
$ infrahubctl load [OPTIONS]
```

**Options**:

* `--directory PATH`: Directory path of exported data \[default: (dynamic)]
* `--continue-on-error / --no-continue-on-error`: Allow exceptions during loading and display them when complete \[default: no-continue-on-error]
* `--quiet / --no-quiet`: No console output \[default: no-quiet]
* `--config-file TEXT`: \[env var: INFRAHUBCTL\_CONFIG; default: infrahubctl.toml]
* `--branch TEXT`: Branch from which to export
* `--concurrent INTEGER`: Maximum number of requests to execute at the same time. \[env var: INFRAHUB\_MAX\_CONCURRENT\_EXECUTION]
* `--timeout INTEGER`: Timeout in sec \[env var: INFRAHUB\_TIMEOUT; default: 60]
* `--install-completion`: Install completion for the current shell.
* `--show-completion`: Show completion for the current shell, to copy it or customize the installation.
* `--help`: Show this message and exit.
