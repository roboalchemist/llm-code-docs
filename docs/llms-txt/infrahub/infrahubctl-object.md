# Source: https://docs.infrahub.app/infrahubctl/infrahubctl-object.md

# `infrahubctl object`

Manage objects in a remote Infrahub instance.

**Usage**:

```
$ infrahubctl object [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--install-completion`: Install completion for the current shell.
* `--show-completion`: Show completion for the current shell, to copy it or customize the installation.
* `--help`: Show this message and exit.

**Commands**:

* `load`: Load one or multiple objects files into...
* `validate`: Validate one or multiple objects files.

## `infrahubctl object load`[​](#infrahubctl-object-load "Direct link to infrahubctl-object-load")

Load one or multiple objects files into Infrahub.

**Usage**:

```
$ infrahubctl object load [OPTIONS] PATHS...
```

**Arguments**:

* `PATHS...`: \[required]

**Options**:

* `--debug / --no-debug`: \[default: no-debug]
* `--branch TEXT`: Branch on which to load the objects.
* `--config-file TEXT`: \[env var: INFRAHUBCTL\_CONFIG; default: infrahubctl.toml]
* `--help`: Show this message and exit.

## `infrahubctl object validate`[​](#infrahubctl-object-validate "Direct link to infrahubctl-object-validate")

Validate one or multiple objects files.

**Usage**:

```
$ infrahubctl object validate [OPTIONS] PATHS...
```

**Arguments**:

* `PATHS...`: \[required]

**Options**:

* `--debug / --no-debug`: \[default: no-debug]
* `--branch TEXT`: Branch on which to validate the objects.
* `--config-file TEXT`: \[env var: INFRAHUBCTL\_CONFIG; default: infrahubctl.toml]
* `--help`: Show this message and exit.
