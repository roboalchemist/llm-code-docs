# Source: https://planetscale.com/docs/cli/role.md

# PlanetScale CLI commands: role

## Getting Started

Make sure to first [set up your PlanetScale developer environment](/docs/cli/planetscale-environment-setup). Once you've installed the `pscale` CLI, you can interact with PlanetScale and manage your databases straight from the command line.

## The `role` command

Manage database roles for a Postgres database branch. This command is only supported for Postgres databases.

**Usage:**

```bash  theme={null}
pscale role [command]
```

### Available sub-commands

| **Sub-Command** | **Product** | **Description**                                       |
| :-------------- | :---------- | :---------------------------------------------------- |
| `create`        | Postgres    | Create a new role for a Postgres database branch      |
| `delete`        | Postgres    | Delete a role                                         |
| `get`           | Postgres    | Retrieve information about a specific role            |
| `list`          | Postgres    | List all roles for a Postgres database branch         |
| `reassign`      | Postgres    | Reassign objects owned by a role to another role      |
| `renew`         | Postgres    | Renew a role's expiration                             |
| `reset`         | Postgres    | Reset a role's password                               |
| `reset-default` | Postgres    | Reset the credentials for the default `postgres` role |
| `update`        | Postgres    | Update a role's name                                  |

### Available flags

| **Flag**       | **Description**                       |
| :------------- | :------------------------------------ |
| `-h`, `--help` | View help for `role` command          |
| `--org string` | The organization for the current user |

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

### The `create` sub-command

Create a new role for a Postgres database branch:

**Usage:**

```bash  theme={null}
pscale role create <database> <branch> <name> [flags]
```

**Available flags:**

* `--inherited-roles string` - Comma-separated list of role names to inherit privileges from. Common values are 'pg\_read\_all\_data' for read access, 'pg\_write\_all\_data' for write access, and 'postgres' for admin access.
* `--ttl duration` - TTL defines the time to live for the role. Durations such as "30m", "24h", or bare integers such as "3600" (seconds) are accepted. The default TTL is 0s, which means the role will never expire.

**Example:**

```bash  theme={null}
pscale role create my-database main api-user --inherited-roles pg_read_all_data --ttl 24h
```

### The `delete` sub-command

Delete a role:

**Usage:**

```bash  theme={null}
pscale role delete <database> <branch> <role-id> [flags]
```

**Available flags:**

* `--force` - Delete a role without confirmation
* `--successor string` - Role to transfer ownership to before deletion. Usually 'postgres'.

**Aliases:** `delete`, `rm`

**Example:**

```bash  theme={null}
pscale role delete my-database main role-123 --successor postgres
```

### The `get` sub-command

Retrieve information about a specific role:

**Usage:**

```bash  theme={null}
pscale role get <database> <branch> <role-id> [flags]
```

**Example:**

```bash  theme={null}
pscale role get my-database main role-123
```

### The `list` sub-command

List all roles for a Postgres database branch:

**Usage:**

```bash  theme={null}
pscale role list <database> <branch> [flags]
```

**Available flags:**

* `-w`, `--web` - List roles in your web browser.

**Aliases:** `list`, `ls`

**Example:**

```bash  theme={null}
pscale role list my-database main
```

### The `reassign` sub-command

Reassign objects owned by one role to any other role:

<Warning>
  Be careful with this command. Reassigning objects like databases, tables, or schemas will change who is able to write to them, alter them, or delete them.
</Warning>

**Usage:**

```bash  theme={null}
pscale role reassign <database> <branch> <role-id> --successor <role-id>
```

**Available flags:**

* `--force` - Force reset without confirmation

**Example:**

```bash  theme={null}
pscale role reassign my-database main role-123 --successor postgres
```

### The `renew` sub-command

Renew a role's expiration:

**Usage:**

```bash  theme={null}
pscale role renew <database> <branch> <role-id> [flags]
```

**Example:**

```bash  theme={null}
pscale role renew my-database main role-123
```

### The `reset` sub-command

Reset the credentials for any API-created role:

<Warning>
  Be careful with this command. If you are currently using the affected role's credentials for connecting to your database, running this command will reset the password, and new connections using the old password will not work.
</Warning>

**Usage:**

```bash  theme={null}
pscale role reset <database> <branch> <role-id> [flags]
```

**Available flags:**

* `--force` - Force reset without confirmation

**Example:**

```bash  theme={null}
pscale role reset my-database main role-123
```

### The `reset-default` sub-command

Reset the credentials for the default `postgres` role:

<Warning>
  Be careful with this command. If you are currently using the default `postgres` role credentials for connecting to your database, running this command will reset the password, and new connections using the old password will not work.
</Warning>

**Usage:**

```bash  theme={null}
pscale role reset-default <database> <branch> [flags]
```

**Available flags:**

* `--force` - Force reset without confirmation

**Example:**

```bash  theme={null}
pscale role reset-default my-database main
```

### The `update` sub-command

Update a role's name:

**Usage:**

```bash  theme={null}
pscale role update <database> <branch> <role-id> [flags]
```

**Available flags:**

* `--name string` - New name for the role

**Example:**

```bash  theme={null}
pscale role update my-database main role-123 --name new-role-name
```

## Related documentation

<CardGroup>
  <Card title="Managing Postgres roles" href="/docs/postgres/connecting/roles" icon="angles-right" horizontal />

  <Card title="Postgres roles API documentation" href="/docs/api/reference/list_roles" icon="angles-right" horizontal />
</CardGroup>

## Need help?

Get help from [the PlanetScale Support team](https://support.planetscale.com/), or join our [GitHub discussion board](https://github.com/planetscale/discussion/discussions) to see how others are using PlanetScale.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://planetscale.com/llms.txt