# Source: https://www.aptible.com/docs/how-to-guides/database-guides/dump-restore-mysql.md

# Dump and restore MySQL

The goal of this guide is to dump the data from one MySQL [Database](/core-concepts/managed-databases/managing-databases/overview) and restore it to another. This is generally done to upgrade to a new MySQL version but can be used in any situation where data needs to be migrated to a new Database instance.

> 📘 MySQL only supports upgrade between General Availability releases, so upgrading multiple versions (i.e. 5.6 => 8.0) requires going through the upgrade process multiple times.

## Preparation

#### Step 0: Install the necessary tools

Install the [Aptible CLI](/reference/aptible-cli/cli-commands/overview) and [MySQL](https://dev.mysql.com/doc/refman/5.7/en/installing.html). This guide uses the `mysqldump` and `mysql` client tools.

#### Step 1: Workspace

The amount of time it takes to dump and restore a Database is directly related to the size of the Database and network bandwidth. If the Database being dumped is small (\< 10 GB) and bandwidth is decent, then dumping locally is usually fine. Otherwise, consider dumping and restoring from a server with more bandwidth, such as an AWS EC2 Instance.

Another thing to consider is available disk space. There should be at least as much space locally available as the Database is currently taking up on disk. See the Database's [metrics](/core-concepts/observability/metrics/overview) to determine the current amount of space it's taking up. If there isn't enough space locally, this would be another good indicator to dump and restore from a server with a large enough disk.

All of the following instructions should be completed on the selected machine.

#### Step 2: Test the table definitions

If data is being transferred to a Database running a different MySQL version than the original, first check that the table definitions can be restored on the desired version by following the [How](/how-to-guides/database-guides/test-upgrade-incompatibiltiies) [to use mysqldump to test for upgrade incompatibilities](/how-to-guides/database-guides/test-upgrade-incompatibiltiies) guide.

If the same MySQL version is being used, this is not necessary.

#### Step 3: Test the upgrade

It's recommended to test the upgrade before performing it in production. The easiest way to do this is to restore the latest backup of the Database and perform the upgrade against the restored Database. The restored Database should have the same container size as the production Database.

Example:

```sql  theme={null}
aptible backup:restore 1234 --handle upgrade-test --container-size 4096
```

> 📘 If you're performing the test to get an estimate of how much downtime is required to perform the upgrade, you'll need to dump the restored Database twice in order to get an accurate time estimate. The first time will ensure that all of the backup data has been synced to the disk. The second backup will take approximately the same amount of time as the production dump.

#### Step 4: Configuration

Collect information on the Database you'd like to test and store it in the following environment variables for use later in the guide:

* `SOURCE_HANDLE` - The handle (i.e., name) of the Database.

* `SOURCE_ENVIRONMENT` - The handle of the environment the Database belongs to.

Example:

```sql  theme={null}
SOURCE_HANDLE='source-db'
SOURCE_ENVIRONMENT='test-environment'
```

Collect information on the target Database and store it in the following environment variables:

* `TARGET_HANDLE` - The handle (i.e., name) for the Database.

* `TARGET_VERSION` - The target MySQL version. Run `aptible db:versions` to see a full list of options. This must be within one General Availability version of the source Database.

* `TARGET_ENVIRONMENT` - The handle of the environment to create the Database in.

Example:

```sql  theme={null}
TARGET_HANDLE='upgrade-test'
TARGET_VERSION='8.0'
TARGET_ENVIRONMENT='test-environment'
```

#### Step 5: Create the target Database

Create a new Database running the desired version. Assuming the environment variables above are set, this command can be copied and pasted as-is to create the Database.

```sql  theme={null}
aptible db:create "$TARGET_HANDLE" \
  --type mysql \
  --version "$TARGET_VERSION" \
  --environment "$TARGET_ENVIRONMENT"
```

## Execution

#### Step 1: Scale Services down

Scale all [Services](/core-concepts/apps/deploying-apps/services) that use the Database down to zero Containers. It's usually easiest to prepare a script that scales all Services down and another that scales them back up to their current values once the upgrade has been completed. Current Container counts can be found in the [Aptible Dashboard](https://dashboard.aptible.com/) or by running [`APTIBLE_OUTPUT_FORMAT=json aptible apps`](/reference/aptible-cli/cli-commands/cli-apps).

Example:

```sql  theme={null}
aptible apps:scale --app my-app cmd --container-count 0
```

While this step is not strictly required, it ensures that the Services don't write to the Database during the upgrade and that its [HTTP(S) Endpoints](/core-concepts/apps/connecting-to-apps/app-endpoints/https-endpoints/overview) will show the App's [Maintenance Page](/core-concepts/apps/connecting-to-apps/app-endpoints/https-endpoints/maintenance-page) if anyone tries to access them.

#### Step 2: Dump the data

In a terminal, create a [Database Tunnel](/core-concepts/managed-databases/connecting-databases/database-tunnels) to the source Database using the Aptible CLI.

```sql  theme={null}
aptible db:tunnel "$SOURCE_HANDLE" --environment "$SOURCE_ENVIRONMENT" --port 5432
```

The tunnel will block the current terminal until it's stopped. In another terminal, collect the tunnel's [Database Credentials](/core-concepts/managed-databases/connecting-databases/database-credentials), which is printed by [`aptible db:tunnel`](/reference/aptible-cli/cli-commands/cli-db-tunnel). Then dump the database and database object definitions into a file. `dump.sql` in this case.

```sql  theme={null}
MYSQL_PWD="$PASSWORD" mysqldump  --user root --host localhost.aptible.in --port 5432 --all-databases --routines --events  > dump.sql
```

The following error may come up when dumping:

```sql  theme={null}
Unknown table 'COLUMN_STATISTICS' in information_schema (1109)
```

This is due to a new flag that is enabled by default in `mysqldump 8`. You can disable this flag and resolve the error by adding `--column-statistics=0` to the above command.

You now have a copy of your Database's database object definitions in `dump.sql`! The Database Tunnel can be closed by following the instructions that `aptible db:tunnel` printed when the tunnel started.

#### Step 3: Restore the data

Create a [Database Tunnel](/core-concepts/managed-databases/connecting-databases/database-tunnels) to the target Database using the Aptible CLI.

```sql  theme={null}
aptible db:tunnel "$TARGET_HANDLE" --environment "$TARGET_ENVIRONMENT" --port 5432
```

Again, the tunnel will block the current terminal until it's stopped. In another terminal, apply the table definitions to the target Database.

```sql  theme={null}
MYSQL_PWD="$PASSWORD" mysql --user root --host localhost.aptible.in --port 5432 < dump.sql
```

> 📘 If there are any errors, they will need to be addressed in order to be able to upgrade the source Database to the desired version. Consult the [MySQL Documentation](https://dev.mysql.com/doc/) for details about the errors you encounter.

#### Step 4: Deprovision target Database

Once you've updated the source Database, you can try the dump again by deprovisioning the target Database and starting from the [Create the target Database](/how-to-guides/database-guides/dump-restore-mysql#create-the-target-database) step.

```sql  theme={null}
aptible db:deprovision "$TARGET_HANDLE" --environment "$TARGET_ENVIRONMENT"
```

#### Step 5: Delete Final Backups (Optional)

If the `$TARGET_ENVIRONMENT` is configured to [retain final Database Backups](/core-concepts/managed-databases/managing-databases/database-backups#retention-and-disposal), which is enabled by default, you may want to delete the final backup for the target Database.

You can obtain a list of final backups by running the following:

```sql  theme={null}
aptible backup:orphaned --environment "$TARGET_ENVIRONMENT"
```

Then, delete the backup(s) by ID using the [`aptible backup:purge`](/reference/aptible-cli/cli-commands/cli-backup-purge) command.

#### Step 6: Update Services

Once the upgrade is complete, any Services that use the existing Database need to be updated to use the upgraded target Database. Assuming you're supplying the [Database Credentials](/core-concepts/managed-databases/connecting-databases/database-credentials) through the App's [Configuration](/core-concepts/apps/deploying-apps/configuration), this can usually be easily done with the [`aptible config:set`](/reference/aptible-cli/cli-commands/cli-config-set) command.

Example:

```sql  theme={null}
aptible config:set --app my-app DB_URL='mysql://aptible:pa$word@db-stack-1234.aptible.in:5432/db'
```

#### Step 7: Scale Services back up

If Services were scaled down before performing the upgrade, they need to be scaled back up afterward. This would be the time to run the scale-up script that was mentioned in [Scale Services down](/how-to-guides/database-guides/dump-restore-mysql#scale-services-down)

Example:

```sql  theme={null}
aptible apps:scale --app my-app cmd --container-count 2
```

## Cleanup

Once the original Database is no longer necessary, it should be deprovisioned, or it will continue to incur costs. Note that this will delete all automated Backups. If you'd like to retain the Backups, contact [Aptible Support](/how-to-guides/troubleshooting/aptible-support) to update them.

```sql  theme={null}
aptible db:deprovision "$SOURCE_HANDLE" --environment "$SOURCE_ENVIRONMENT"
```
