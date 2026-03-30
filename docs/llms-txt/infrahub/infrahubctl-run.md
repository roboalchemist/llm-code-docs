# Source: https://docs.infrahub.app/infrahubctl/infrahubctl-run.md

# `infrahubctl run`

Execute a script.

**Usage**:

```
$ infrahubctl run [OPTIONS] SCRIPT [VARIABLES]...
```

**Arguments**:

* `SCRIPT`: \[required]
* `[VARIABLES]...`: Variables to pass along with the query. Format key=value key=value.

**Options**:

* `--method TEXT`: \[default: run]
* `--debug / --no-debug`: \[default: no-debug]
* `--config-file TEXT`: \[env var: INFRAHUBCTL\_CONFIG; default: infrahubctl.toml]
* `--branch TEXT`: Branch on which to run the script.
* `--concurrent INTEGER`: Maximum number of requests to execute at the same time. \[env var: INFRAHUB\_MAX\_CONCURRENT\_EXECUTION]
* `--timeout INTEGER`: Timeout in sec \[env var: INFRAHUB\_TIMEOUT; default: 60]
* `--install-completion`: Install completion for the current shell.
* `--show-completion`: Show completion for the current shell, to copy it or customize the installation.
* `--help`: Show this message and exit.
