# Source: https://planetscale.com/docs/cli/branch.md

# PlanetScale CLI commands: branch

## Getting Started

Make sure to first [set up your PlanetScale developer environment](/docs/cli/planetscale-environment-setup). Once you've installed the `pscale` CLI, you can interact with PlanetScale and manage your databases straight from the command line.

## The `branch` command

This command allows you to create, delete, diff, and manage [branches](/docs/vitess/schema-changes/branching).

**Usage:**

```bash  theme={null}
pscale branch <SUB-COMMAND> <FLAG>
```

### Available sub-commands

| **Sub-command**                                         | **Sub-command flags**                                                                                    | **Description**                                                  | **Product**      |
| :------------------------------------------------------ | :------------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------- | :--------------- |
| `create <DATABASE_NAME> <BRANCH_NAME>`                  | `--from <SOURCE_BRANCH>`, `--region <BRANCH_REGION>`, `--restore <BACKUP_NAME>`, `--seed-data`, `--wait` | Create a new branch on the specified database                    | Postgres, Vitess |
| `delete <DATABASE_NAME> <BRANCH_NAME>`                  | `--force`                                                                                                | Delete the specified branch from the a database                  | Postgres, Vitess |
| `diff <DATABASE_NAME> <BRANCH_NAME>`                    | `--web`                                                                                                  | Show the diff of the specified branch against the parent branch. | Vitess           |
| `list <DATABASE_NAME>`                                  | `--web`                                                                                                  | List all branches of a database                                  | Postgres, Vitess |
| `promote <DATABASE_NAME> <BRANCH_NAME>`                 |                                                                                                          | Promote a database branch to production                          | Vitess           |
| `refresh-schema <DATABASE_NAME> <BRANCH_NAME>`          |                                                                                                          | Refresh the schema for a database branch                         | Vitess           |
| `safe-migrations enable <DATABASE_NAME> <BRANCH_NAME>`  |                                                                                                          | Enables safe migrations for a database branch                    | Vitess           |
| `safe-migrations disable <DATABASE_NAME> <BRANCH_NAME>` |                                                                                                          | Disables safe migrations for a database branch                   | Vitess           |
| `schema <DATABASE_NAME> <BRANCH_NAME>`                  | `--web`                                                                                                  | Show the schema of a branch                                      | Vitess           |
| `show <DATABASE_NAME> <BRANCH_NAME>`                    | `--web`                                                                                                  | Show a specific backup of a branch                               | Postgres, Vitess |
| `switch <BRANCH_NAME> --database <DATABASE_NAME>`       | `--database <DATABASE_NAME>`\*, `--create`, `parent-branch <BRANCH_NAME>`                                | Switch to the specified branch                                   | Postgres, Vitess |

> \* *Flag is required*

#### Sub-command flag descriptions

Some of the sub-commands have additional flags unique to the sub-command. This section covers what each of those does. See the above table for which context.

| **Sub-command flag**            | **Description**                                                                                                   | **Applicable sub-commands**                |
| :------------------------------ | :---------------------------------------------------------------------------------------------------------------- | :----------------------------------------- |
| `--from <SOURCE_BRANCH>`        | Parent branch that you want to create a new branch off of                                                         | `create`                                   |
| `--region <BRANCH_REGION>`      | Region where database should be created                                                                           | `create`                                   |
| `--restore <BACKUP_NAME>`       | Create a new branch from a specified backup                                                                       | `create`                                   |
| `--seed-data`                   | Create a new branch and seed data using the [Data Branching® feature](/docs/vitess/schema-changes/data-branching) | `create`                                   |
| `--web`                         | Perform the action in your web browser                                                                            | `create`, `diff`, `list`, `schema`, `show` |
| `--wait`                        | Wait until the branch is ready                                                                                    | `create`                                   |
| `--major-version`               | The major version of the branch (Postgres only). Currently supports `17` or `18`.                                 | `create`                                   |
| `--database <DATABASE_NAME>`    | Specify the database name                                                                                         | `switch`                                   |
| `--create`                      | Create a new branch if it does not exist                                                                          | `switch`                                   |
| `--parent-branch <BRANCH_NAME>` | If a new branch is being created, use this to specify a parent branch. Default is `main`.                         | `switch`                                   |

<Note>
  The `--region` flag can not be used with `--restore` when creating a branch. Branch backups will be restored to their original region.
</Note>

### Available flags

| **Flag**                    | **Description**                       |
| :-------------------------- | :------------------------------------ |
| `-h`, `--help`              | View help for auth command            |
| `--org <ORGANIZATION_NAME>` | The organization for the current user |

### Global flags

| **Command**                     | **Description**                                                                      |
| :------------------------------ | :----------------------------------------------------------------------------------- |
| `--api-token <TOKEN>`           | The API token to use for authenticating against the PlanetScale API.                 |
| `--api-url <URL>`               | The base URL for the PlanetScale API. Default is `https://api.planetscale.com/`.     |
| `--config <CONFIG_FILE>`        | Config file. Default is `$HOME/.config/planetscale/pscale.yml`.                      |
| `--debug`                       | Enable debug mode.                                                                   |
| `-f`, `--format <FORMAT>`       | Show output in a specific format. Possible values: `human` (default), `json`, `csv`. |
| `--no-color`                    | Disable color output.                                                                |
| `--service-token <TOKEN>`       | The service token for authenticating.                                                |
| `--service-token-id <TOKEN_ID>` | The service token ID for authenticating.                                             |

## Examples

### The `list` sub-command with `--web` flag

**Command:**

```bash  theme={null}
pscale branch list <DATABASE_NAME> --web
```

**Output:**

Opens the Branches page, `<https://app.planetscale.com/org/database/branches>`, in browser.

### The `diff` sub-command

**Command:**

```bash  theme={null}
pscale branch diff <DATABASE_NAME> <BRANCH_NAME>
```

**Output:**

```sql  theme={null}
-- users --
+CREATE TABLE `users` (
+  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
+  `name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
+  PRIMARY KEY (`id`)
+) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
```

This will return the diff against the parent branch.

## Need help?

Get help from [the PlanetScale Support team](https://support.planetscale.com/), or join our [GitHub discussion board](https://github.com/planetscale/discussion/discussions) to see how others are using PlanetScale.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://planetscale.com/llms.txt