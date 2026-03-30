# Source: https://docs.infrahub.app/infrahubctl/infrahubctl-repository.md

# `infrahubctl repository`

Manage the repositories in a remote Infrahub instance.

List, create, delete ..

**Usage**:

```
$ infrahubctl repository [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--install-completion`: Install completion for the current shell.
* `--show-completion`: Show completion for the current shell, to copy it or customize the installation.
* `--help`: Show this message and exit.

**Commands**:

* `add`: Add a new repository.
* `init`: Initialize a new Infrahub repository.
* `list`

## `infrahubctl repository add`[​](#infrahubctl-repository-add "Direct link to infrahubctl-repository-add")

Add a new repository.

**Usage**:

```
$ infrahubctl repository add [OPTIONS] NAME LOCATION
```

**Arguments**:

* `NAME`: \[required]
* `LOCATION`: \[required]

**Options**:

* `--description TEXT`
* `--username TEXT`
* `--password TEXT`
* `--ref TEXT`
* `--read-only / --no-read-only`: \[default: no-read-only]
* `--debug / --no-debug`: \[default: no-debug]
* `--config-file TEXT`: \[env var: INFRAHUBCTL\_CONFIG; default: infrahubctl.toml]
* `--help`: Show this message and exit.

## `infrahubctl repository init`[​](#infrahubctl-repository-init "Direct link to infrahubctl-repository-init")

Initialize a new Infrahub repository.

**Usage**:

```
$ infrahubctl repository init [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.

## `infrahubctl repository list`[​](#infrahubctl-repository-list "Direct link to infrahubctl-repository-list")

**Usage**:

```
$ infrahubctl repository list [OPTIONS]
```

**Options**:

* `--branch TEXT`: Branch on which to list repositories.
* `--debug / --no-debug`: \[default: no-debug]
* `--config-file TEXT`: \[env var: INFRAHUBCTL\_CONFIG; default: infrahubctl.toml]
* `--help`: Show this message and exit.
