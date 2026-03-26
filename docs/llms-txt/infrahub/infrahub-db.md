# Source: https://docs.infrahub.app/reference/infrahub-cli/infrahub-db.md

# `infrahub db`

Manage the graph in the database.

**Usage**:

```
$ infrahub db [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--install-completion`: Install completion for the current shell.
* `--show-completion`: Show completion for the current shell, to copy it or customize the installation.
* `--help`: Show this message and exit.

**Commands**:

* `migrate`: Check the current format of the internal...
* `check-inheritance`: Check the database for any vertices with...
* `check-duplicate-schema-fields`: Check for any duplicate schema attributes...
* `update-core-schema`: Check the current format of the internal...
* `constraint`: Manage Database Constraints
* `index`: Manage Database Indexes
* `selected-export`: Export database structure of selected...
* `load-export`: Cannot be used for backup/restore...
* `check`: Run database sanity checks and output the...
* `patch`: Commands for planning, applying, and...

## `infrahub db migrate`[​](#infrahub-db-migrate "Direct link to infrahub-db-migrate")

Check the current format of the internal graph and apply the necessary migrations

**Usage**:

```
$ infrahub db migrate [OPTIONS] [CONFIG_FILE]
```

**Arguments**:

* `[CONFIG_FILE]`: \[env var: INFRAHUB\_CONFIG; default: infrahub.toml]

**Options**:

* `--check / --no-check`: Check the state of the database without applying the migrations. \[default: no-check]
* `--migration-number INTEGER`: Apply a specific migration by number, regardless of current database version
* `--help`: Show this message and exit.

## `infrahub db check-inheritance`[​](#infrahub-db-check-inheritance "Direct link to infrahub-db-check-inheritance")

Check the database for any vertices with incorrect inheritance

**Usage**:

```
$ infrahub db check-inheritance [OPTIONS] [CONFIG_FILE]
```

**Arguments**:

* `[CONFIG_FILE]`: \[env var: INFRAHUB\_CONFIG; default: infrahub.toml]

**Options**:

* `--fix / --no-fix`: Fix the inheritance of any invalid nodes. \[default: no-fix]
* `--help`: Show this message and exit.

## `infrahub db check-duplicate-schema-fields`[​](#infrahub-db-check-duplicate-schema-fields "Direct link to infrahub-db-check-duplicate-schema-fields")

Check for any duplicate schema attributes or relationships on the default branch

**Usage**:

```
$ infrahub db check-duplicate-schema-fields [OPTIONS] [CONFIG_FILE]
```

**Arguments**:

* `[CONFIG_FILE]`: \[env var: INFRAHUB\_CONFIG; default: infrahub.toml]

**Options**:

* `--fix / --no-fix`: Fix the duplicate schema fields on the default branch. \[default: no-fix]
* `--help`: Show this message and exit.

## `infrahub db update-core-schema`[​](#infrahub-db-update-core-schema "Direct link to infrahub-db-update-core-schema")

Check the current format of the internal graph and apply the necessary migrations

**Usage**:

```
$ infrahub db update-core-schema [OPTIONS] [CONFIG_FILE]
```

**Arguments**:

* `[CONFIG_FILE]`: \[env var: INFRAHUB\_CONFIG; default: infrahub.toml]

**Options**:

* `--debug / --no-debug`: Enable advanced logging and troubleshooting \[default: no-debug]
* `--help`: Show this message and exit.

## `infrahub db constraint`[​](#infrahub-db-constraint "Direct link to infrahub-db-constraint")

Manage Database Constraints

**Usage**:

```
$ infrahub db constraint [OPTIONS] [ACTION]:[show|add|drop] [CONFIG_FILE]
```

**Arguments**:

* `[ACTION]:[show|add|drop]`: \[default: show]
* `[CONFIG_FILE]`: \[env var: INFRAHUB\_CONFIG; default: infrahub.toml]

**Options**:

* `--help`: Show this message and exit.

## `infrahub db index`[​](#infrahub-db-index "Direct link to infrahub-db-index")

Manage Database Indexes

**Usage**:

```
$ infrahub db index [OPTIONS] [ACTION]:[show|add|drop] [CONFIG_FILE]
```

**Arguments**:

* `[ACTION]:[show|add|drop]`: \[default: show]
* `[CONFIG_FILE]`: \[env var: INFRAHUB\_CONFIG; default: infrahub.toml]

**Options**:

* `--help`: Show this message and exit.

## `infrahub db selected-export`[​](#infrahub-db-selected-export "Direct link to infrahub-db-selected-export")

Export database structure of selected nodes from the database without any actual data

**Usage**:

```
$ infrahub db selected-export [OPTIONS] [CONFIG_FILE]
```

**Arguments**:

* `[CONFIG_FILE]`: \[env var: INFRAHUB\_CONFIG; default: infrahub.toml]

**Options**:

* `--kinds TEXT`: Node kinds to export
* `--uuids TEXT`: UUIDs of nodes to export
* `--query-limit INTEGER`: Maximum batch size of export query \[default: 1000]
* `--export-dir PATH`: Path of directory to save exports \[default: infrahub-exports]
* `--help`: Show this message and exit.

## `infrahub db load-export`[​](#infrahub-db-load-export "Direct link to infrahub-db-load-export")

Cannot be used for backup/restore functionality. Loads an anonymized export into Neo4j. Only used for analysis of output of the selected-export command.

**Usage**:

```
$ infrahub db load-export [OPTIONS] EXPORT_DIR [CONFIG_FILE]
```

**Arguments**:

* `EXPORT_DIR`: Path to export directory \[required]
* `[CONFIG_FILE]`: \[env var: INFRAHUB\_CONFIG; default: infrahub.toml]

**Options**:

* `--query-limit INTEGER`: Maximum batch size of import query \[default: 1000]
* `--help`: Show this message and exit.

## `infrahub db check`[​](#infrahub-db-check "Direct link to infrahub-db-check")

Run database sanity checks and output the results to the CSV files.

**Usage**:

```
$ infrahub db check [OPTIONS]
```

**Options**:

* `--output-dir PATH`: Directory to save detailed check results (defaults to infrahub\_db\_check\_YYYYMMDD-HHMMSS)
* `--config-file TEXT`: Location of the configuration file to use for Infrahub \[env var: INFRAHUB\_CONFIG; default: infrahub.toml]
* `--help`: Show this message and exit.

## `infrahub db patch`[​](#infrahub-db-patch "Direct link to infrahub-db-patch")

Commands for planning, applying, and reverting database patches

**Usage**:

```
$ infrahub db patch [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `plan`: Create a plan for a given patch and save...
* `apply`: Apply a given patch plan
* `revert`: Revert a given patch plan

### `infrahub db patch plan`[​](#infrahub-db-patch-plan "Direct link to infrahub-db-patch-plan")

Create a plan for a given patch and save it in the patch plans directory to be applied/reverted

**Usage**:

```
$ infrahub db patch plan [OPTIONS] PATCH_PATH [CONFIG_FILE]
```

**Arguments**:

* `PATCH_PATH`: Path to the file containing the PatchQuery instance to run. Use Python-style dot paths, such as infrahub.cli.patch.queries.base \[required]
* `[CONFIG_FILE]`: \[env var: INFRAHUB\_CONFIG; default: infrahub.toml]

**Options**:

* `--patch-plans-dir PATH`: Path to patch plans directory \[default: infrahub-patches]
* `--apply / --no-apply`: Apply the patch immediately after creating it \[default: no-apply]
* `--help`: Show this message and exit.

### `infrahub db patch apply`[​](#infrahub-db-patch-apply "Direct link to infrahub-db-patch-apply")

Apply a given patch plan

**Usage**:

```
$ infrahub db patch apply [OPTIONS] PATCH_PLAN_DIR [CONFIG_FILE]
```

**Arguments**:

* `PATCH_PLAN_DIR`: Path to the directory containing a patch plan \[required]
* `[CONFIG_FILE]`: \[env var: INFRAHUB\_CONFIG; default: infrahub.toml]

**Options**:

* `--help`: Show this message and exit.

### `infrahub db patch revert`[​](#infrahub-db-patch-revert "Direct link to infrahub-db-patch-revert")

Revert a given patch plan

**Usage**:

```
$ infrahub db patch revert [OPTIONS] PATCH_PLAN_DIR [CONFIG_FILE]
```

**Arguments**:

* `PATCH_PLAN_DIR`: Path to the directory containing a patch plan \[required]
* `[CONFIG_FILE]`: \[env var: INFRAHUB\_CONFIG; default: infrahub.toml]

**Options**:

* `--help`: Show this message and exit.
