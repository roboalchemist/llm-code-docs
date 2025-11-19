# Source: https://www.aptible.com/docs/how-to-guides/database-guides/test-schema-new-version.md

# Test a PostgreSQL Database's schema on a new version

> The goal of this guide is to test the schema of an existing Database against another Database version in order to see if it's compatible with the desired version. The primary reason to do this is to ensure a Database's schema is compatible with a higher version before upgrading.

## Preparation

#### Step 0: Install the necessary tools

Install the [Aptible CLI](/reference/aptible-cli/cli-commands/overview) and [PostgreSQL Client Tools](https://www.postgresql.org/download/). This guide uses the `pg_dumpall` and `psql` client tools.

#### Step 1: Configuration

Collect information on the Database you'd like to test and store it in the following environment variables for use later in the guide:

* `SOURCE_HANDLE` - The handle (i.e. name) of the Database.

* `SOURCE_ENVIRONMENT` - The handle of the environment theDatabase belongs to.

Example:

```sql  theme={null}
SOURCE_HANDLE='source-db'
SOURCE_ENVIRONMENT='test-environment'
```

Collect information on the target Database and store it in in the following environment variables:

* `TARGET_HANDLE` - The handle (i.e. name) for the Database.

* `TARGET_VERSION` - The target PostgreSQL version. Run `aptible db:versions` to see a full list of options.

* `TARGET_ENVIRONMENT` - The handle of the environment to create the Database in.

Example:

```sql  theme={null}
TARGET_HANDLE='schema-test'
TARGET_VERSION='14'
TARGET_ENVIRONMENT='test-environment'
```

#### Step 2: Create the target Database

Create a new Database running the desired version. Assuming the environment variables above are set, this command can be copied and pasted as-is to create the Database.

```sql  theme={null}
aptible db:create "$TARGET_HANDLE" --type postgresql --version "$TARGET_VERSION" --environment "$TARGET_ENVIRONMENT"
```

By default, [`aptible db:create`](/reference/aptible-cli/cli-commands/cli-db-create) creates a Database with a 1 GB of memory and 10 GB of disk space. This should be sufficient for most schema tests but, if more memory or disk is required, the `--container-size` and `--disk-size` arguments can be used.

## Execution

#### Step 1: Dump the schema

Create a [Database Tunnel](/core-concepts/managed-databases/connecting-databases/database-tunnels) to the source Database using the Aptible CLI.

```sql  theme={null}
aptible db:tunnel "$SOURCE_HANDLE" --environment "$SOURCE_ENVIRONMENT"
```

The tunnel will block the current terminal until it's stopped. In another terminal, collect the tunnel's information, which is printed by [`aptible db:tunnel`](/reference/aptible-cli/cli-commands/cli-db-tunnel), and store it in the following environment variables:

* `SOURCE_URL` - The full URL of the Database tunnel.

* `SOURCE_PASSWORD` - The Database's password.

Example:

```sql  theme={null}
SOURCE_URL='postgresql://aptible:pa$word@localhost.aptible.in:5432/db'
SOURCE_PASSWORD='pa$word'
```

Dump the schema into a file. `schema.sql` in this case.

```sql  theme={null}
PGPASSWORD="$SOURCE_PASSWORD" pg_dumpall -d "$SOURCE_URL" --schema-only --no-password \
  | grep -E -i -v 'ALTER ROLE aptible .*PASSWORD' > schema.sql
```

The output of `pg_dumpall` is piped into `grep` in order to remove any SQL commands that may change the default `aptible` user's password. If these commands were to run on the target Database, it would be updated to match the source Database. This would result in the target Database's password no longer matching what's displayed in the [Aptible Dashboard](https://dashboard.aptible.com/) or printed by commands like [`aptible db:url`](/reference/aptible-cli/cli-commands/cli-db-url) or [`aptible db:tunnel`](/reference/aptible-cli/cli-commands/cli-db-tunnel) which could cause problems down the road.

You now have a copy of your Database's schema in `schema.sql`! The Database Tunnel can be closed by following the instructions that `aptible db:tunnel` printed when the tunnel started.

#### Step 2: Restore the schema

Create a [Database Tunnel](/core-concepts/managed-databases/connecting-databases/database-tunnels) to the target Database using the Aptible CLI.

```sql  theme={null}
aptible db:tunnel "$TARGET_HANDLE" --environment "$TARGET_ENVIRONMENT"
```

Again, the tunnel will block the current terminal until it's stopped. In another terminal, store the tunnel's full URL, which is printed by [`aptible db:tunnel`](/reference/aptible-cli/cli-commands/cli-db-tunnel), in the `TARGET_URL` environment variable.

Example:

```sql  theme={null}
TARGET_URL='postgresql://aptible:p@ssword@localhost.aptible.in:5432/db'
```

Apply the schema to the target Database.

```sql  theme={null}
psql $TARGET_URL -f schema.sql > /dev/null
```

The output of `psql` can be noisy depending on the complexity of the source Database's schema. In order to reduce the noise, the output is redirected to `/dev/null` so that only error messages are displayed.

The following errors may come up when restoring the schema:

```sql  theme={null}
ERROR:  role "aptible" already exists
ERROR:  role "postgres" already exists
ERROR:  database "db" already exists
```

These errors are expected because Aptible creates these resources on all PostgreSQL Databases when they are created. The errors are a result of the schema dump attempting to re-create the existing resources. If these are the only errors, the upgrade was successful!

If there are additional errors, they will need to be addressed in order to be able to upgrade the source Database to the desired version. Consult the [PostgreSQL Documentation](https://www.postgresql.org/docs/) for details about the errors you encounter.

Once you've updated the source Database's schema you can test the changes by deprovisioning the target Database, see the [Cleanup](/how-to-guides/database-guides/test-schema-new-version#cleanup) section, and starting from the [Create the target Database](/how-to-guides/database-guides/test-schema-new-version#create-the-target-database) step.

## Cleanup

#### Step 1: Deprovision the target Database

```sql  theme={null}
aptible db:deprovision "$TARGET_HANDLE" --environment "$TARGET_ENVIRONMENT"
```

#### Step 2: Delete Final Backups (Optional)

If the `$TARGET_ENVIRONMENT` is configured to [retain final Database Backups](/core-concepts/managed-databases/managing-databases/database-backups#retention-and-disposal), which is enabled by default, you may want to delete the final backups for all target Databases you created for this test.

You can obtain a list of final backups by running:

```sql  theme={null}
aptible backup:orphaned --environment "$TARGET_ENVIRONMENT"
```

Then, delete the backup(s) by ID using the [`aptible backup:purge`](/reference/aptible-cli/cli-commands/cli-backup-purge) command.
