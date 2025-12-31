# Source: https://planetscale.com/docs/cli/service-token.md

# PlanetScale CLI commands: service-token

## Getting Started

Make sure to first [set up your PlanetScale developer environment](/docs/cli/planetscale-environment-setup). Once you've installed the `pscale` CLI, you can interact with PlanetScale and manage your databases straight from the command line.

## The `service-token` command

This command allows you to create, list, and manage access for service tokens.

**Usage:**

```bash  theme={null}
pscale service-token <SUB-COMMAND> <FLAG>
```

### Available sub-commands

| **Sub-command**                                      | **Sub-command flags**        | **Product**      | **Description**                                                               |
| :--------------------------------------------------- | :--------------------------- | :--------------- | :---------------------------------------------------------------------------- |
| `add-access <TOKEN_ID> <PERMISSION> <PERMISSION>`    | `--database <DATABASE_NAME>` | Postgres, Vitess | Add individual permissions to the specified service token in the organization |
| `create`                                             | `--name <NAME>`              | Postgres, Vitess | Create a service token for the organization                                   |
| `delete <TOKEN_ID>`                                  |                              | Postgres, Vitess | Delete an entire service token in an organization                             |
| `delete-access <TOKEN_ID> <PERMISSION> <PERMISSION>` | `--database <DATABASE_NAME>` | Postgres, Vitess | Delete individual permissions granted to a service token in the organization  |
| `list`                                               |                              | Postgres, Vitess | List the IDs and names of an organization's service tokens                    |
| `show-access`                                        |                              | Postgres, Vitess | Fetch a service token and its accesses                                        |

#### Sub-command flag descriptions

Some of the sub-commands have additional flags unique to the sub-command. This section covers what each of those does. See the above table for which context.

| **Sub-command flag**         | **Description**                     | **Applicable sub-commands**   |
| :--------------------------- | :---------------------------------- | :---------------------------- |
| `--database <DATABASE_NAME>` | The database this project is using. | `add-access`, `delete-access` |
| `--name <NAME>`              | The name for the service token.     | `create`                      |

### Available flags

| **Flag**                    | **Description**                       |
| :-------------------------- | :------------------------------------ |
| `-h`, `--help`              | View help for `service-token` command |
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

### Adding service token access for a database

**Command:**

```bash  theme={null}
pscale service-token add-access <TOKEN_ID> read_branch delete_branch create_branch --database <DATABASE_NAME>
```

This will add the following permissions to the specified access token: `read_branch`, `delete_branch`, `create_branch`. The output will show the updated permissions on all databases.

You can find a list of all permissions in the [PlanetScale API documentation](/docs/api/reference/service-tokens#access-permissions).

**Output:**

| RESOURCE NAME | RESOURCE TYPE | ACCESSES                                     |
| :------------ | :------------ | :------------------------------------------- |
| dbname        | Database      | read\_branch, delete\_branch, create\_branch |
| dbname2       | Database      | create\_branch                               |
| my-org        | Organization  | create\_databases, delete\_databases         |

### Adding service token access for an organization

**Command:**

```bash  theme={null}
pscale service-token add-access <TOKEN_ID> read_organization
```

This will grant the service token the `read_organization` access on the organization.

**Output:**

| RESOURCE NAME | RESOURCE TYPE | ACCESSES           |
| :------------ | :------------ | :----------------- |
| my-org        | Organization  | read\_organization |

## Need help?

Get help from [the PlanetScale Support team](https://support.planetscale.com/), or join our [GitHub discussion board](https://github.com/planetscale/discussion/discussions) to see how others are using PlanetScale.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://planetscale.com/llms.txt