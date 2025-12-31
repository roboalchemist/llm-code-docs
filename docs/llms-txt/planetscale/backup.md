# Source: https://planetscale.com/docs/cli/backup.md

# PlanetScale CLI commands: backup

## Getting Started

Make sure to first [set up your PlanetScale developer environment](/docs/cli/planetscale-environment-setup). Once you've installed the `pscale` CLI, you can interact with PlanetScale and manage your databases straight from the command line.

## The `backup` command

This command allows you to create, list, show, and delete [branch backups](/docs/vitess/backups).

**Usage:**

```bash  theme={null}
pscale backup <SUB-COMMAND> <FLAG>
```

### Available sub-commands

| **Sub-command**                                     | **Description**                    | **Product**      |
| :-------------------------------------------------- | :--------------------------------- | :--------------- |
| `create <DATABASE_NAME> <BRANCH_NAME>`              | Backup a branch's data and schema  | Postgres, Vitess |
| `delete <DATABASE_NAME> <BRANCH_NAME> <BACKUP_ID>`  | Delete a branch backup             | Postgres, Vitess |
| `list <DATABASE_NAME> <BRANCH_NAME>`                | List all backups of a branch       | Postgres, Vitess |
| `restore <DATABASE_NAME> <BRANCH_NAME> <BACKUP_ID>` | Restore a backup to a new branch   | Postgres, Vitess |
| `show <DATABASE_NAME> <BRANCH_NAME> <BACKUP_ID>`    | Show a specific backup of a branch | Postgres, Vitess |

### Available flags

| **Flag**                    | **Description**                       |
| :-------------------------- | :------------------------------------ |
| `-h`, `--help`              | View help for `backup` command        |
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

### The `list` sub-command with `--org` flag

**Command:**

```bash  theme={null}
pscale backup list <DATABASE_NAME> <BRANCH_NAME> --org <ORGANIZATION_NAME>
```

**Output:**

```bash  theme={null}
ID             NAME                  STATE     SIZE    CREATED AT    UPDATED AT    STARTED AT    EXPIRES AT          COMPLETED AT
-------------- --------------------- --------- ------- ------------- ------------- ------------- ------------------- --------------
xxxxxxxx   2022.02.11 16:01:03   success   24.1M   3 hours ago   3 hours ago   3 hours ago   1 day from now      3 hours ago
xxxxxxxx   2022.02.10 16:01:03   success   23.2M   1 day ago     1 day ago     1 day ago     20 hours from now   1 day ago
```

### The `show` sub-command

**Command:**

```bash  theme={null}
pscale backup list <DATABASE_NAME> <BRANCH_NAME> <BACKUP_ID>
```

You can find the `<BACKUP_ID>` by running the `pscale backup list <DATABASE_NAME> <BRANCH_NAME>` command.

**Output:**

```bash  theme={null}
ID             NAME                  STATE     SIZE    CREATED AT    UPDATED AT    STARTED AT    EXPIRES AT          COMPLETED AT
-------------- --------------------- --------- ------- ------------- ------------- ------------- ------------------- --------------
xxxxxxxx   2022.02.11 16:01:03   success   24.1M   3 hours ago   3 hours ago   3 hours ago   1 day from now      3 hours ago
```

## Need help?

Get help from [the PlanetScale Support team](https://support.planetscale.com/), or join our [GitHub discussion board](https://github.com/planetscale/discussion/discussions) to see how others are using PlanetScale.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://planetscale.com/llms.txt