# Source: https://www.aptible.com/docs/how-to-guides/database-guides/dump-restore-postgresql.md

# Dump and restore PostgreSQL

The goal of this guide is to dump the schema and data from one PostgreSQL [Database](/core-concepts/managed-databases/managing-databases/overview) and restore it to another. This is generally done to upgrade to a new PostgreSQL version but can be used in any situation where data needs to be migrated to a new Database instance.

## Preparation

## Workspace

The amount of time it takes to dump and restore a Database is directly related to the size of the Database and network bandwidth. If the Database being dumped is small (\< 10 GB) and bandwidth is decent, then dumping locally is usually fine. Otherwise, consider dumping and restoring from a server with more bandwidth, such as an AWS EC2 Instance.

Another thing to consider is available disk space. There should be at least as much space locally available as the Database is currently taking up on disk. See the Database's [metrics](/core-concepts/observability/metrics/overview) to determine the current amount of space it's taking up. If there isn't enough space locally, this would be another good indicator to dump and restore from a server with a large enough disk.

All of the following instructions should be completed on the selected machine.

## Test the schema

If data is being transferred to a Database running a different PostgreSQL version than the original, first check that the schema can be restored on the desired version by following the [How to test a PostgreSQL Database's schema on a new version](/how-to-guides/database-guides/test-schema-new-version) guide.

If the same PostgreSQL version is being used, this is not necessary.

## Test the upgrade

Testing the schema should catch most issues but it's also recommended to test the upgrade before performing it in production. The easiest way to do this is to restore the latest backup of the Database and performing the upgrade against the restored Database. The restored Database should have the same container size as the production Database.

Example:

```sql  theme={null}
aptible backup:restore 1234 --handle upgrade-test --container-size 4096
```

Note that if you're performing the test to get an estimate of how much downtime is required to perform the upgrade, you'll need to dump the restored Database twice in order to get an accurate time estimate. The first time will ensure that all of the backup data has been synced to the disk. The second backup will take approximately the same amount of time as the production dump.
Tools
Install the [Aptible CLI](/reference/aptible-cli/cli-commands/overview) and [PostgreSQL Client Tools](https://www.postgresql.org/download/). This guide uses the `pg_dumpall` and `psql` client tools.

## Configuration

Collect information on the Database you'd like to upgrade and store it in the following environment variables for use later in the guide:

* `SOURCE_HANDLE` - The handle (i.e. name) of the Database.

* `SOURCE_ENVIRONMENT` - The handle of the environment the Database belongs to.

Example:

```sql  theme={null}
SOURCE_HANDLE='source-db'
SOURCE_ENVIRONMENT='test-environment'
```

Collect information on the target Database and store it in in the following environment variables:

* `TARGET_HANDLE` - The handle (i.e. name) for the Database.

* `TARGET_VERSION` - The target PostgreSQL version. Run `aptible db:versions` to see a full list of options.

* `TARGET_ENVIRONMENT` - The handle of the environment to create the Database in.

* `TARGET_DISK_SIZE` - The size of the target Database's disk in GB. This must be at least be as large as the current Database takes up on disk but can be smaller than its overall disk size.

* `TARGET_CONTAINER_SIZE` (Optional) - The size of the target Database's container in MB. Having more memory and CPU available speeds up the dump and restore process, up to a certain point. See the [Database Scaling](/core-concepts/scaling/database-scaling#ram-scaling) documentation for a full list of supported container sizes.

Example:

```sql  theme={null}
TARGET_HANDLE='dump-test'
TARGET_VERSION='14'
TARGET_ENVIRONMENT='test-environment'
TARGET_DISK_SIZE=100
TARGET_CONTAINER_SIZE=4096
```

## Create the target Database

Create a new Database running the desired version. Assuming the environment variables above are set, this command can be copied and pasted as-is to create the Database.

```sql  theme={null}
aptible db:create "$TARGET_HANDLE" \
  --type postgresql \
  --version "$TARGET_VERSION" \
  --environment "$TARGET_ENVIRONMENT" \
  --disk-size "$TARGET_DISK_SIZE" \
  --container-size "${TARGET_CONTAINER_SIZE:-4096}"
```

## Execution

## Scale Services down

Scale all [Services](/core-concepts/apps/deploying-apps/services) that use the Database down to zero containers. It's usually easiest to prepare a script that scales all Services down and another that scales them back up to their current values once the upgrade has been complete. Current container counts can be found in the [Aptible Dashboard](https://dashboard.aptible.com/) or by running [`APTIBLE_OUTPUT_FORMAT=json aptible apps`](/reference/aptible-cli/cli-commands/cli-apps).

Example scale command:

```sql  theme={null}
aptible apps:scale --app my-app cmd --container-count 0
```

While this step is not strictly required, it ensures that the Services don't write to the Database during the upgrade and that its [HTTP(S) Endpoints](/core-concepts/apps/connecting-to-apps/app-endpoints/https-endpoints/overview) will show the App's [Maintenance Page](/core-concepts/apps/connecting-to-apps/app-endpoints/https-endpoints/maintenance-page) if anyone tries to access them.

## Dump the data

In a separate terminal, create a [Database Tunnel](/core-concepts/managed-databases/connecting-databases/database-tunnels) to the source Database using the Aptible CLI.

```sql  theme={null}
aptible db:tunnel "$SOURCE_HANDLE" --environment "$SOURCE_ENVIRONMENT"
```

The tunnel will block the current terminal until it's stopped. Collect the tunnel's information, which is printed by [`aptible db:tunnel`](/reference/aptible-cli/cli-commands/cli-db-tunnel), and store it in the following environment variables in the original terminal:

* `SOURCE_URL` - The full URL of the Database tunnel.

* `SOURCE_PASSWORD` - The Database's password.

Example:

```sql  theme={null}
SOURCE_URL='postgresql://aptible:pa$word@localhost.aptible.in:5432/db'
SOURCE_PASSWORD='pa$word'
```

Dump the data into a file. `dump.sql` in this case.

```sql  theme={null}
PGPASSWORD="$SOURCE_PASSWORD" pg_dumpall -d "$SOURCE_URL" --no-password \
  | grep -E -i -v 'ALTER ROLE aptible .*PASSWORD' > dump.sql
```

The output of `pg_dumpall` is piped into `grep` in order to remove any SQL commands that may change the default `aptible` user's password. If these commands were to run on the target Database, it would be updated to match the source Database. This would result in the target Database's password no longer matching what's displayed in the [Aptible Dashboard](https://dashboard.aptible.com/) or printed by commands like [`aptible db:url`](/reference/aptible-cli/cli-commands/cli-db-url) or [`aptible db:tunnel`](/reference/aptible-cli/cli-commands/cli-db-tunnel) which could cause problems down the road.

You now have a copy of your Database's schema and data in `dump.sql`! The Database Tunnel can be closed by following the instructions that `aptible db:tunnel` printed when the tunnel started.

## Restore the data

In a separate terminal, create a [Database Tunnel](/core-concepts/managed-databases/connecting-databases/database-tunnels) to the target Database using the Aptible CLI.

```sql  theme={null}
aptible db:tunnel "$TARGET_HANDLE" --environment "$TARGET_ENVIRONMENT"
```

Again, the tunnel will block the current terminal until it's stopped. Collect the tunnel's full URL, which is printed by [`aptible db:tunnel`](/reference/aptible-cli/cli-commands/cli-db-tunnel), and store it in the `TARGET_URL` environment variable in the original terminal.

Example:

```sql  theme={null}
TARGET_URL='postgresql://aptible:passw0rd@localhost.aptible.in:5432/db'
```

Apply the data to the target Database.

```sql  theme={null}
psql $TARGET_URL -f dump.sql > /dev/null
```

The output of `psql` can be noisy depending on the size of the source Database. In order to reduce the noise, the output is redirected to `/dev/null` so that only error messages are displayed.

The following errors may come up when restoring the Database:

```sql  theme={null}
ERROR:  role "aptible" already exists
ERROR:  role "postgres" already exists
ERROR:  database "db" already exists
```

These errors are expected because Aptible creates these resources on all PostgreSQL Databases when they are created. The errors are a result of the dump attempting to re-create the existing resources. If these are the only errors, the upgrade was successful!

### Errors

If there are additional errors, they will need to be addressed in order to be able to upgrade the source Database to the desired version. Consult the [PostgreSQL Documentation](https://www.postgresql.org/docs/) for details about the errors you encounter.

Once you've updated the source Database, you can try the dump again by deprovisioning the target Database and starting from the [Create the target Database](/how-to-guides/database-guides/dump-restore-postgresql#create-the-target-database) step.

```sql  theme={null}
aptible db:deprovision "$TARGET_HANDLE" --environment "$TARGET_ENVIRONMENT"
```

If the `$TARGET_ENVIRONMENT` is configured to [retain final Database Backups](/core-concepts/managed-databases/managing-databases/database-backups#retention-and-disposal), which is enabled by default, you may want to delete the final backup for the target Database.

You can obtain a list of final backups by running:

```sql  theme={null}
aptible backup:orphaned --environment "$TARGET_ENVIRONMENT"
```

Then, delete the backup(s) by ID using the [`aptible backup:purge`](/reference/aptible-cli/cli-commands/cli-backup-purge) command.

## Update Services

Once the upgrade is complete, any Services that use the existing Database need to be updated to use the upgraded target Database. Assuming you're supplying the [Database Credentials](/core-concepts/managed-databases/connecting-databases/database-credentials) through the App's [Configuration](/core-concepts/apps/deploying-apps/configuration), this can usually be easily done with the [`aptible config:set`](/reference/aptible-cli/cli-commands/cli-config-set) command.

Example config command:

```sql  theme={null}
aptible config:set --app my-app DB_URL='postgresql://user:passw0rd@db-stack-1234.aptible.in:5432/db'
```

## Scale Services back up

If Services were scaled down before performing the upgrade, they need to be scaled back up afterward. This would be the time to run the scale-up script that was mentioned in [Scale Services down](/how-to-guides/database-guides/dump-restore-postgresql#scale-services-down)

Example:

```sql  theme={null}
aptible apps:scale --app my-app cmd --container-count 2
```

## Cleanup

## Vacuum and Analyze

Vacuuming the target Database after upgrading reclaims space occupied by dead tuples and analyzing the tables collects information on the table's contents in order to improve query performance.

```sql  theme={null}
psql "$TARGET_URL" --tuples-only --no-align --command \
  'SELECT datname FROM pg_database WHERE datistemplate IS FALSE' |

while IFS= read -r db; do
  psql "$TARGET_URL" << EOF
    \connect "$db"

    VACUUM ANALYZE;
EOF
done
```

## Deprovision

Once the original Database is no longer necessary, it should be deprovisioned or it will continue to incur costs. Note that this will delete all automated Backups. If you'd like to retain the Backups, contact [Aptible Support](/how-to-guides/troubleshooting/aptible-support) to update them.

```sql  theme={null}
aptible db:deprovision "$SOURCE_HANDLE" --environment "$SOURCE_ENVIRONMENT"
```
