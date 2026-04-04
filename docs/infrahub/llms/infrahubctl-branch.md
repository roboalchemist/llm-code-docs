# Source: https://docs.infrahub.app/infrahubctl/infrahubctl-branch.md

# `infrahubctl branch`

Manage the branches in a remote Infrahub instance.

List, create, merge, rebase ..

**Usage**:

```
$ infrahubctl branch [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--install-completion`: Install completion for the current shell.
* `--show-completion`: Show completion for the current shell, to copy it or customize the installation.
* `--help`: Show this message and exit.

**Commands**:

* `create`: Create a new branch.
* `delete`: Delete a branch.
* `list`: List all existing branches.
* `merge`: Merge a Branch with main.
* `rebase`: Rebase a Branch with main.
* `report`: Generate branch cleanup status report.
* `validate`: Validate if a branch has some conflict and...

## `infrahubctl branch create`[​](#infrahubctl-branch-create "Direct link to infrahubctl-branch-create")

Create a new branch.

**Usage**:

```
$ infrahubctl branch create [OPTIONS] BRANCH_NAME
```

**Arguments**:

* `BRANCH_NAME`: Name of the branch to create \[required]

**Options**:

* `--description TEXT`: Description of the branch
* `--sync-with-git / --no-sync-with-git`: Extend the branch to Git and have Infrahub create the branch in connected repositories. \[default: no-sync-with-git]
* `--config-file TEXT`: \[env var: INFRAHUBCTL\_CONFIG; default: infrahubctl.toml]
* `--help`: Show this message and exit.

## `infrahubctl branch delete`[​](#infrahubctl-branch-delete "Direct link to infrahubctl-branch-delete")

Delete a branch.

**Usage**:

```
$ infrahubctl branch delete [OPTIONS] BRANCH_NAME
```

**Arguments**:

* `BRANCH_NAME`: \[required]

**Options**:

* `--config-file TEXT`: \[env var: INFRAHUBCTL\_CONFIG; default: infrahubctl.toml]
* `--help`: Show this message and exit.

## `infrahubctl branch list`[​](#infrahubctl-branch-list "Direct link to infrahubctl-branch-list")

List all existing branches.

**Usage**:

```
$ infrahubctl branch list [OPTIONS]
```

**Options**:

* `--config-file TEXT`: \[env var: INFRAHUBCTL\_CONFIG; default: infrahubctl.toml]
* `--help`: Show this message and exit.

## `infrahubctl branch merge`[​](#infrahubctl-branch-merge "Direct link to infrahubctl-branch-merge")

Merge a Branch with main.

**Usage**:

```
$ infrahubctl branch merge [OPTIONS] BRANCH_NAME
```

**Arguments**:

* `BRANCH_NAME`: \[required]

**Options**:

* `--config-file TEXT`: \[env var: INFRAHUBCTL\_CONFIG; default: infrahubctl.toml]
* `--help`: Show this message and exit.

## `infrahubctl branch rebase`[​](#infrahubctl-branch-rebase "Direct link to infrahubctl-branch-rebase")

Rebase a Branch with main.

**Usage**:

```
$ infrahubctl branch rebase [OPTIONS] BRANCH_NAME
```

**Arguments**:

* `BRANCH_NAME`: \[required]

**Options**:

* `--config-file TEXT`: \[env var: INFRAHUBCTL\_CONFIG; default: infrahubctl.toml]
* `--help`: Show this message and exit.

## `infrahubctl branch report`[​](#infrahubctl-branch-report "Direct link to infrahubctl-branch-report")

Generate branch cleanup status report.

**Usage**:

```
$ infrahubctl branch report [OPTIONS] BRANCH_NAME
```

**Arguments**:

* `BRANCH_NAME`: Branch name to generate report for \[required]

**Options**:

* `--update-diff`: Update diff before generating report
* `--config-file TEXT`: \[env var: INFRAHUBCTL\_CONFIG; default: infrahubctl.toml]
* `--help`: Show this message and exit.

## `infrahubctl branch validate`[​](#infrahubctl-branch-validate "Direct link to infrahubctl-branch-validate")

Validate if a branch has some conflict and is passing all the tests (NOT IMPLEMENTED YET).

**Usage**:

```
$ infrahubctl branch validate [OPTIONS] BRANCH_NAME
```

**Arguments**:

* `BRANCH_NAME`: \[required]

**Options**:

* `--config-file TEXT`: \[env var: INFRAHUBCTL\_CONFIG; default: infrahubctl.toml]
* `--help`: Show this message and exit.
