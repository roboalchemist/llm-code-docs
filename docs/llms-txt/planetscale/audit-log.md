# Source: https://planetscale.com/docs/vitess/audit-log.md

# Source: https://planetscale.com/docs/security/audit-log.md

# Source: https://planetscale.com/docs/cli/audit-log.md

# PlanetScale CLI commands: audit log

## Getting Started

Make sure to first [set up your PlanetScale developer environment](/docs/cli/planetscale-environment-setup). Once you've installed the `pscale` CLI, you can interact with PlanetScale and manage your databases straight from the command line.

## The `audit log` command

Lists all [audit logs](/docs/security/audit-log) in an organization. The user running the command must have [Organization-level permissions](/docs/security/access-control), specifically `list_organization_audit_logs`.

**Usage:**

```bash  theme={null}
pscale audit-log <SUB-COMMAND> <FLAG>
```

### Available sub-commands

| **Sub-command** | **Description**                        | **Product**      |
| :-------------- | :------------------------------------- | :--------------- |
| `list`          | List all audit logs in an organization | Postgres, Vitess |

### Available flags

| **Flag**                    | **Description**                                         |
| :-------------------------- | :------------------------------------------------------ |
| `-h`, `--help`              | View help for `audit-log` command                       |
| `--action`                  | Filter based on action type                             |
| `--limit` int               | The number of events to return. Min: 1, Max: 100        |
| `--starting-after` string   | The ID of the audit log to start after (for pagination) |
| `--org <ORGANIZATION_NAME>` | The organization for the current user                   |

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
pscale audit-log list --org <ORGANIZATION_NAME>
```

**Output:**

```bash  theme={null}
 ID (25)      ACTOR (25)  ACTION                   EVENT                     REMOTE IP      LOCATION         CREATED AT
------------- ----------- ------------------------ ------------------------ --------------- ---------------- ------------
xxxxxxxxxx  Name        Open_web_console main    branch.open_web_console  xxx.xxx.xxx.x   Los Angeles, CA  1 day ago
```

### Pagination

Use the ID from the last result and pass it as the `--starting-after` to retrieve the next page of results.

```bash  theme={null}
pscale audit-log list --limit 5 --starting-after <ID>
```

## Need help?

Get help from [the PlanetScale Support team](https://support.planetscale.com/), or join our [GitHub discussion board](https://github.com/planetscale/discussion/discussions) to see how others are using PlanetScale.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://planetscale.com/llms.txt