# Source: https://www.aptible.com/docs/how-to-guides/database-guides/test-upgrade-incompatibiltiies.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.aptible.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Use mysqldump to test for upgrade incompatibilities

The goal of this guide is to use `mysqldump` to test the table definitions of an existing Database against another Database version in order to see if it's compatible with the desired version. The primary reason to do this is to ensure a Database is compatible with a higher version before upgrading without waiting for lengthy data-loading operations.

## Preparation

#### Step 0: Install the necessary tools

Install the [Aptible CLI](/reference/aptible-cli/cli-commands/overview) and [MySQL](https://dev.mysql.com/doc/refman/5.7/en/installing.html). This guide uses the `mysqldump` and `mysql` client tools.

#### Step 1: Configuration

Collect information on the Database you'd like to test and store it in the following environment variables for use later in the guide:

* `SOURCE_HANDLE` - The handle (i.e. name) of the Database.

* `SOURCE_ENVIRONMENT` - The handle of the environment the Database belongs to.

Example:

```sql  theme={null}
SOURCE_HANDLE='source-db'
SOURCE_ENVIRONMENT='test-environment'
```

Collect information on the target Database and store it in the following environment variables:

* `TARGET_HANDLE` - The handle (i.e., name) for the Database.

* `TARGET_VERSION` - The target MySQL version. Run `aptible db:versions` to see a full list of options. This must be within one General Availability version of the source Database.

* `TARGET_ENVIRONMENT` - The handle of the Environment to create the Database in.

Example:

```sql  theme={null}
TARGET_HANDLE='upgrade-test'
TARGET_VERSION='8.0'
TARGET_ENVIRONMENT='test-environment'
```

#### Step 2: Create the target Database

Create a new Database running the desired version. Assuming the environment variables above are set, this command can be copied and pasted as-is to create the Database.

```sql  theme={null}
aptible db:create "$TARGET_HANDLE" \
  --type mysql \
  --version "$TARGET_VERSION" \
  --environment "$TARGET_ENVIRONMENT"
```

By default, [`aptible db:create`](/reference/aptible-cli/cli-commands/cli-db-create) creates a Database with 1 GB of memory and 10 GB of disk space. This is typically sufficient for testing table definition compatibility, but if more memory or disk is required, the `--container-size` and `--disk-size` arguments can be used.

## Execution

#### Step 1: Dump the table definition

In a terminal, create a [Database Tunnel](/core-concepts/managed-databases/connecting-databases/database-tunnels) to the source Database using the Aptible CLI.

```sql  theme={null}
aptible db:tunnel "$SOURCE_HANDLE" --environment "$SOURCE_ENVIRONMENT" --port 5432
```

The tunnel will block the current terminal until it's stopped. In another terminal, collect the tunnel's [Database Credentials](/core-concepts/managed-databases/connecting-databases/database-credentials), which are printed by [`aptible db:tunnel`](/reference/aptible-cli/cli-commands/cli-db-tunnel). Then dump the database and database object definitions into a file. `defs.sql` in this case.

```sql  theme={null}
MYSQL_PWD="$PASSWORD" mysqldump  --user root --host localhost.aptible.in --port 5432 --all-databases --no-data --routines --events  > defs.sql
```

The following error may come up when dumping the table definitions:

```sql  theme={null}
Unknown table 'COLUMN_STATISTICS' in information_schema (1109)
```

This is due to a new flag that is enabled by default in `mysqldump 8`. You can disable this flag and resolve the error by adding `--column-statistics=0` to the above command.

You now have a copy of your Database's database object definitions in `defs.sql`! The Database Tunnel can be closed by following the instructions that `aptible db:tunnel` printed when the tunnel started.

#### Step 2: Restore the table definitions

Create a [Database Tunnel](/core-concepts/managed-databases/connecting-databases/database-tunnels) to the target Database using the Aptible CLI.

```sql  theme={null}
aptible db:tunnel "$TARGET_HANDLE" --environment "$TARGET_ENVIRONMENT" --port 5432
```

Again, the tunnel will block the current terminal until it's stopped. In another terminal, apply the table definitions to the target Database.

```sql  theme={null}
MYSQL_PWD="$PASSWORD" mysql --user aptible --host localhost.aptible.in --port 5432 < defs.sql
```

If there are any errors, they will need to be addressed in order to be able to upgrade the source Database to the desired version. Consult the [MySQL Documentation](https://dev.mysql.com/doc/) for details about the errors you encounter.

Once you've updated the source Database's table definitions, you can test the changes by deprovisioning the target Database, see the [Cleanup](/how-to-guides/database-guides/test-upgrade-incompatibiltiies#cleanup) section, and starting from the [Create the target Database](/how-to-guides/database-guides/test-upgrade-incompatibiltiies#create-the-target-database) step.

## Cleanup

#### Step 1: Deprovision the target Database

```sql  theme={null}
aptible db:deprovision "$TARGET_HANDLE" --environment "$TARGET_ENVIRONMENT"
```

#### Step 2: Delete Final Backups (Optional)

If the `$TARGET_ENVIRONMENT` is configured to [retain final Database Backups](/core-concepts/managed-databases/managing-databases/database-backups#retention-and-disposal), which is enabled by default, you may want to delete the final backups for all target Databases you created for this test.

You can obtain a list of final backups by running the following:

```sql  theme={null}
aptible backup:orphaned --environment "$TARGET_ENVIRONMENT"
```

Then, delete the backup(s) by ID using the [`aptible backup:purge`](/reference/aptible-cli/cli-commands/cli-backup-purge) command.
