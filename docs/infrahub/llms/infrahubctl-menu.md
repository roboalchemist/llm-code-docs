# Source: https://docs.infrahub.app/infrahubctl/infrahubctl-menu.md

# `infrahubctl menu`

Manage the menu in a remote Infrahub instance.

**Usage**:

```
$ infrahubctl menu [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--install-completion`: Install completion for the current shell.
* `--show-completion`: Show completion for the current shell, to copy it or customize the installation.
* `--help`: Show this message and exit.

**Commands**:

* `load`: Load one or multiple menu files into...
* `validate`: Validate one or multiple menu files.

## `infrahubctl menu load`[​](#infrahubctl-menu-load "Direct link to infrahubctl-menu-load")

Load one or multiple menu files into Infrahub.

**Usage**:

```
$ infrahubctl menu load [OPTIONS] MENUS...
```

**Arguments**:

* `MENUS...`: \[required]

**Options**:

* `--debug / --no-debug`: \[default: no-debug]
* `--branch TEXT`: Branch on which to load the menu.
* `--config-file TEXT`: \[env var: INFRAHUBCTL\_CONFIG; default: infrahubctl.toml]
* `--help`: Show this message and exit.

## `infrahubctl menu validate`[​](#infrahubctl-menu-validate "Direct link to infrahubctl-menu-validate")

Validate one or multiple menu files.

**Usage**:

```
$ infrahubctl menu validate [OPTIONS] PATHS...
```

**Arguments**:

* `PATHS...`: \[required]

**Options**:

* `--debug / --no-debug`: \[default: no-debug]
* `--branch TEXT`: Branch on which to validate the objects.
* `--config-file TEXT`: \[env var: INFRAHUBCTL\_CONFIG; default: infrahubctl.toml]
* `--help`: Show this message and exit.
