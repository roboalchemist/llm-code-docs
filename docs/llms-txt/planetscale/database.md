# Source: https://planetscale.com/docs/cli/database.md

# PlanetScale CLI commands: database

## Getting Started

Make sure to first [set up your PlanetScale developer environment](/docs/cli/planetscale-environment-setup). Once you've installed the `pscale` CLI, you can interact with PlanetScale and manage your databases straight from the command line.

## The `database` command

This command allows you to create, read, delete, dump, and restore databases.

**Usage:**

```bash  theme={null}
pscale database <SUB-COMMAND> <FLAG>
```

### Available sub-commands

| **Sub-command**                              | **Sub-command flags**                                                                                                                                                                                                                                                                | **Description**                                            | **Product**      |
| :------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :--------------------------------------------------------- | :--------------- |
| `create <DATABASE_NAME>`                     | `--region <REGION_NAME>`, `--plan <PLAN>`, `--cluster_size <CLUSTER_SIZE>`                                                                                                                                                                                                           | Create a database with the specified name                  | Postgres, Vitess |
| `delete <DATABASE_NAME>`                     | `--force`                                                                                                                                                                                                                                                                            | Delete the specified database                              | Postgres, Vitess |
| `dump <DATABASE_NAME> <BRANCH_NAME>`         | `--local-addr <ADDRESS>`, `--output <DIRECTORY_NAME>`, `--tables <TABLES_LIST>`, `--threads <NUMBER_OF_THREADS> (defaults to 16)`                                                                                                                                                    | Backup and dump the specified database                     | Vitess           |
| `list <DATABASE_NAME>`                       |                                                                                                                                                                                                                                                                                      | List all databases in the current org                      | Postgres, Vitess |
| `restore-dump <DATABASE_NAME> <BRANCH_NAME>` | `--dir <DIRECTORY_NAME>`\*, `--local-addr <ADDRESS>`, `--overwrite-tables`, `--threads <NUMBER_OF_THREADS> (defaults to 1)`, `--allow-different-destination`, `--show-details`, `--schema-only`, `--data-only`, `--starting-table <STARTING_TABLE>`, `--ending-table <ENDING_TABLE>` | Restore the specified database from a local dump directory | Postgres, Vitess |
| `show <DATABASE_NAME>`                       | `--web`                                                                                                                                                                                                                                                                              | Retrieve information about a database                      | Postgres, Vitess |

> \* *Flag is required*

#### Sub-command flag descriptions

Some of the sub-commands have additional flags unique to the sub-command. This section covers what each of those does. See the above table for which context.

| **Sub-command flag**            | **Description**                                                                                                                       | **Applicable sub-commands** |
| :------------------------------ | :------------------------------------------------------------------------------------------------------------------------------------ | :-------------------------- |
| `--region`                      | Specify the [region](/docs/vitess/regions) of the new database. Default is `us-east`.                                                 | `create`                    |
| `--plan`                        | Specify the plan for the databas. Currently, `scaler_pro` is the only option and the default.                                         | `create`                    |
| `--cluster_size`                | For Scaler Pro databases, you may specify the cluster size. Default is `PS_10`                                                        | `create`                    |
| `--major-version`               | The major version of the database (Postgres only). Currently supports `17` or `18`.                                                   | `create`                    |
| `--force`                       | Delete a database without confirmation.                                                                                               | `delete`                    |
| `--local-addr <ADDRESS>`        | Local address to bind and listen for connections. By default the proxy binds to 127.0.0.1 with a random port.                         | `dump`, `restore-dump`      |
| `--threads`                     | Number of concurrent threads to use                                                                                                   | `dump`, `restore-dump`      |
| `--output <DIRECTORY_NAME>`     | Output directory of the dump. By default the dump is saved to a folder in the current directory.                                      | `dump`                      |
| `--tables <TABLES_LIST>`        | Comma separated string of tables to dump. By default, all tables are dumped.                                                          | `dump`                      |
| `--wheres string`               | Comma separated string of WHERE clauses to filter the tables to dump.                                                                 | `dump`                      |
| `--replica`                     | Dump from a replica (if available; will fail if not).                                                                                 | `dump`                      |
| `--rdonly`                      | Dump from a rdonly tablet (if available; will fail if not).                                                                           | `dump`                      |
| `--keyspace <KEYSPACE_NAME>`    | Optionally target a specific keyspace to be dumped. Useful for sharded databases.                                                     | `dump`                      |
| `--shard <SHARD_NAME>`          | Optional shard to target, must be used with keyspace                                                                                  | `dump`                      |
| `--output-format <FORMAT>`      | Output format for the dump. Options: `sql` (default), `json`, `csv`.                                                                  | `dump`                      |
| `--dir <DIRECTORY_NAME>`        | Directory containing the files to be used for the restore.                                                                            | `restore-dump`              |
| `--overwrite-tables`            | If true, will attempt to DROP TABLE before restoring.                                                                                 | `restore-dump`              |
| `--allow-different-destination` | If true, will allow you to restore the files to a database with a different name without needing to rename the existing dump's files. | `restore-dump`              |
| `--show-details`                | If true, will add extra output during the restore process.                                                                            | `restore-dump`              |
| `--schema-only`                 | If true, will only restore the schema files during the restore process.                                                               | `restore-dump`              |
| `--data-only`                   | If true, will only restore the data files during the restore process.                                                                 | `restore-dump`              |
| `--starting-table <TABLE_NAME>` | Table to start from for the restore (useful for restarting from a certain point)                                                      | `restore-dump`              |
| `--ending-table <TABLE_NAME>`   | Table to end at for the restore (useful for stopping restore at a certain point)                                                      | `restore-dump`              |
| `--web`                         | Perform the action in your web browser                                                                                                | `show`                      |

### Available flags

| **Flag**                    | **Description**                                              |
| :-------------------------- | :----------------------------------------------------------- |
| `-h`, `--help`              | Get help with the `database` command                         |
| `--org <ORGANIZATION_NAME>` | Specify the organization for the database you're acting upon |

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

<Note>
  The `--format` flag does not apply to the database dump files created by the `dump` subcommand. However, you can control the output format using the `--output-format` flag, which supports SQL (default), JSON, and CSV formats. When using SQL format, dumps are compatible with [mydumper](https://github.com/mydumper/mydumper).
</Note>

## Examples

### Create a new `scaler_pro` database

**Command:**

```bash  theme={null}
pscale database create new-database --region <REGION_NAME> --plan scaler_pro --cluster_size PS_80
```

**Output:**

Database `new-database` was successfully created.

### Create a dump of an existing branch:

This command is only available for Vitess databases. For Postgres databases, use the [pg\_dump](https://www.postgresql.org/docs/current/app-pgdump.html) command instead.

**Command:**

```bash  theme={null}
pscale database dump <CURRENT_DATABASE_NAME> <BRANCH_NAME> --output="<DIRECTORY_FOR_BACKUP>" --org="<ORIGINAL_ORGANIZATION>"
```

**Output:**

A local export of your database will be generated within the current directory by default but since we are providing an `--output` location above that will be used instead.

### Export data in different formats:

You can specify the output format when dumping your Vitess database using the `--output-format` flag:

**Export as JSON:**

```bash  theme={null}
pscale database dump <DATABASE_NAME> <BRANCH_NAME> --output-format=json
```

**Export as CSV:**

```bash  theme={null}
pscale database dump <DATABASE_NAME> <BRANCH_NAME> --output-format=csv
```

**Export as SQL (default):**

```bash  theme={null}
pscale database dump <DATABASE_NAME> <BRANCH_NAME> --output-format=sql
```

### Restore a backup to an existing branch:

**Command:**

```bash  theme={null}
pscale database restore-dump <DESTINATION_DATABASE_NAME> <BRANCH_NAME> --dir="<DIRECTORY_FOR_BACKUP>" --org="<DESTINATION_ORGANIZATION>"
```

**Output:**

You should receive output indicating the restore is progressing until it completes successfully.

The command above will allow you to restore an existing backup to another branch located either within the same organization/database as the original, or within a completely different organization/database.

As of `pscale` v0.218.0 or newer the `--allow-different-destination` flag is now available. If this flag is provided it will make the steps below about renaming the files unnecessary.

If you opt to import into a database with a different name you will have to make sure you rename the files from your backup beforehand.

For example, the files will be named something like this:

```bash  theme={null}
<CURRENT_DATABASE_NAME>.<TABLE_NAME>-schema.sql
```

And you will want to rename all of the files in the dump folder to have the new database name if it is not the same as the existing one:

```bash  theme={null}
<DESTINATION_DATABASE_NAME>.<TABLE_NAME>-schema.sql
```

If importing into a branch that already contains table definitions that you want to overwrite, you may also be required to pass in the optional `--overwrite-tables` flag.

## Need help?

Get help from [the PlanetScale Support team](https://support.planetscale.com/), or join our [GitHub discussion board](https://github.com/planetscale/discussion/discussions) to see how others are using PlanetScale.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://planetscale.com/llms.txt