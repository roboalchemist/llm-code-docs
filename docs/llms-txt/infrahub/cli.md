# Source: https://docs.infrahub.app/sync/reference/cli.md

# `infrahub-sync`

**Usage**:

```
$ infrahub-sync [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--install-completion`: Install completion for the current shell.
* `--show-completion`: Show completion for the current shell, to copy it or customize the installation.
* `--help`: Show this message and exit.

**Commands**:

* `diff`: Calculate and print the differences...
* `generate`: Generate all the Python files for a given...
* `list`: List all available SYNC projects.
* `sync`: Synchronize the data between source and...

## `infrahub-sync diff`[​](#infrahub-sync-diff "Direct link to infrahub-sync-diff")

Calculate and print the differences between the source and the destination systems for a given project.

**Usage**:

```
$ infrahub-sync diff [OPTIONS]
```

**Options**:

* `--name TEXT`: Name of the sync to use
* `--config-file TEXT`: File path to the sync configuration YAML file
* `--directory TEXT`: Base directory to search for sync configurations
* `--branch TEXT`: Branch to use for the diff.
* `--show-progress / --no-show-progress`: Show a progress bar during diff \[default: show-progress]
* `--adapter-path TEXT`: Paths to look for adapters. Can be specified multiple times.
* `--help`: Show this message and exit.

## `infrahub-sync generate`[​](#infrahub-sync-generate "Direct link to infrahub-sync-generate")

Generate all the Python files for a given sync based on the configuration.

**Usage**:

```
$ infrahub-sync generate [OPTIONS]
```

**Options**:

* `--name TEXT`: Name of the sync to use
* `--config-file TEXT`: File path to the sync configuration YAML file
* `--directory TEXT`: Base directory to search for sync configurations
* `--branch TEXT`: Branch to use for the sync.
* `--adapter-path TEXT`: Paths to look for adapters. Can be specified multiple times.
* `--help`: Show this message and exit.

## `infrahub-sync list`[​](#infrahub-sync-list "Direct link to infrahub-sync-list")

List all available SYNC projects.

**Usage**:

```
$ infrahub-sync list [OPTIONS]
```

**Options**:

* `--directory TEXT`: Base directory to search for sync configurations
* `--help`: Show this message and exit.

## `infrahub-sync sync`[​](#infrahub-sync-sync "Direct link to infrahub-sync-sync")

Synchronize the data between source and the destination systems for a given project or configuration file.

**Usage**:

```
$ infrahub-sync sync [OPTIONS]
```

**Options**:

* `--name TEXT`: Name of the sync to use
* `--config-file TEXT`: File path to the sync configuration YAML file
* `--directory TEXT`: Base directory to search for sync configurations
* `--branch TEXT`: Branch to use for the sync.
* `--diff / --no-diff`: Print the differences between the source and the destination before syncing \[default: diff]
* `--show-progress / --no-show-progress`: Show a progress bar during syncing \[default: show-progress]
* `--adapter-path TEXT`: Paths to look for adapters. Can be specified multiple times.
* `--help`: Show this message and exit.
