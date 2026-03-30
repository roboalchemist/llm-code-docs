# Source: https://docs.infrahub.app/infrahubctl/infrahubctl-schema.md

# `infrahubctl schema`

Manage the schema in a remote Infrahub instance.

**Usage**:

```
$ infrahubctl schema [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--install-completion`: Install completion for the current shell.
* `--show-completion`: Show completion for the current shell, to copy it or customize the installation.
* `--help`: Show this message and exit.

**Commands**:

* `check`: Check if schema files are valid and what...
* `export`: Export the schema from Infrahub as YAML...
* `load`: Load one or multiple schema files into...

## `infrahubctl schema check`[​](#infrahubctl-schema-check "Direct link to infrahubctl-schema-check")

Check if schema files are valid and what would be the impact of loading them with Infrahub.

**Usage**:

```
$ infrahubctl schema check [OPTIONS] SCHEMAS...
```

**Arguments**:

* `SCHEMAS...`: \[required]

**Options**:

* `--debug / --no-debug`: \[default: no-debug]
* `--branch TEXT`: Branch on which to check the schema.
* `--config-file TEXT`: \[env var: INFRAHUBCTL\_CONFIG; default: infrahubctl.toml]
* `--help`: Show this message and exit.

## `infrahubctl schema export`[​](#infrahubctl-schema-export "Direct link to infrahubctl-schema-export")

Export the schema from Infrahub as YAML files, one per namespace.

**Usage**:

```
$ infrahubctl schema export [OPTIONS]
```

**Options**:

* `--directory PATH`: Directory path to store schema files \[default: (dynamic)]
* `--branch TEXT`: Branch from which to export the schema
* `--namespaces TEXT`: Namespace(s) to export (default: all user-defined)
* `--debug / --no-debug`: \[default: no-debug]
* `--config-file TEXT`: \[env var: INFRAHUBCTL\_CONFIG; default: infrahubctl.toml]
* `--help`: Show this message and exit.

## `infrahubctl schema load`[​](#infrahubctl-schema-load "Direct link to infrahubctl-schema-load")

Load one or multiple schema files into Infrahub.

**Usage**:

```
$ infrahubctl schema load [OPTIONS] SCHEMAS...
```

**Arguments**:

* `SCHEMAS...`: \[required]

**Options**:

* `--debug / --no-debug`: \[default: no-debug]
* `--branch TEXT`: Branch on which to load the schema.
* `--wait INTEGER`: Time in seconds to wait until the schema has converged across all workers \[default: 0]
* `--config-file TEXT`: \[env var: INFRAHUBCTL\_CONFIG; default: infrahubctl.toml]
* `--help`: Show this message and exit.
