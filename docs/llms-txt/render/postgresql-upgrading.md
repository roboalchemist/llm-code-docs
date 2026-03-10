# Source: https://render.com/docs/postgresql-upgrading.md

# Upgrading Your Render Postgres Version — Move your database to a more recent version of PostgreSQL.


> *Upgrading your database requires downtime.* Schedule upgrades accordingly.

You can upgrade your Render Postgres database to a more recent major version of PostgreSQL in one of the following ways:

- Perform an [in-place upgrade](#upgrading-in-place)
  - This method always upgrades to the latest major version supported by Render (currently <latest-postgres></latest-postgres>).
- Create a _new_ database and [migrate your data](#migrating-to-a-new-instance)
  - This method enables you to upgrade to _any_ major version supported by Render.

## Version support

| Full support                                      | Legacy support\* | Not yet supported               |
| ------------------------------------------------- | ---------------- | ------------------------------- |
| <supported-postgres-csv></supported-postgres-csv> | 12, 11           | <next-postgres></next-postgres> |

<sup>\*Only workspaces with an _existing_ database on PostgreSQL 11 or 12 can create new databases on the corresponding version.</sup>

View your database's current version from its *Info* page in the [Render Dashboard](https://dashboard.render.com):

[image: Opening Postgres version config in the Render Dashboard]

## Upgrading in-place

Render supports in-place database upgrades to PostgreSQL <latest-postgres></latest-postgres> from any previous version.

### 1. Perform a test upgrade (recommended)

Before you upgrade, we strongly recommend creating a temporary copy of your database and performing a test upgrade on the copy. This way, you can:

- Confirm that your database will upgrade successfully
- Estimate how long your database upgrade will take

1. In the [Render Dashboard](https://dashboard.render.com), go to your database's *Info* page and click its current version:

   [image: Opening Postgres version config in the Render Dashboard]

   The following page appears with recommended upgrade steps:

   [image: Postgres upgrade flow in the Render Dashboard]

*Don't see the "Clone this database" button?*

This means that your database uses a legacy instance type that doesn't yet have [point-in-time recovery](postgresql-backups) (PITR) enabled. Render uses PITR to create your database copy.

   To enable PITR immediately, you can move your database to a new flexible PostgreSQL plan by [changing its instance type](postgresql-creating-connecting#changing-your-instance-type). Otherwise, PITR will be enabled during your database's next planned maintenance.

   We strongly recommend that you enable PITR for any database before you upgrade it in-place, so that you can copy it for testing.

2. Click *Clone this database*. Render immediately creates a new database and starts replicating the primary database's state from _ten minutes earlier_.

   - The clone will not reflect any changes made to the primary database after the restore point.

3. Click *View PostgreSQL clone* to jump to the clone's upgrade page:

   [image: A database clone still restoring in the Render Dashboard]

   You can't upgrade the clone until data replication completes.

4. When the *Upgrade to PostgreSQL <latest-postgres></latest-postgres>* button becomes active, click it to kick off the clone's in-place upgrade.

   A log explorer appears and displays log entries from the upgrade process. Depending on the size of your database, the upgrade process might take up to one hour.

> Note the total duration of the test upgrade, which provides a helpful estimate for the primary database upgrade.

5. When the upgrade completes, the clone's status changes from *Upgrading* to *Available*. You can now run commands on the upgraded clone to confirm that it behaves as expected.

> *If the upgrade fails, the clone remains on its original PostgreSQL version.*
>
>    Review the logs to identify any issues. If the underlying cause or resolution is unclear, reach out to support in the Render Dashboard.

6. When you're done testing the clone, you can delete it from its *Info* page.

### 2. Upgrade your database

After you perform a successful [test upgrade](#1-perform-a-test-upgrade-recommended), you can confidently upgrade your primary database.

> *Your database will be unavailable during the upgrade.*
>
> The upgrade might take up to an hour. If you ran a test upgrade, the duration of the primary database upgrade should be similar.

1. In the [Render Dashboard](https://dashboard.render.com), go to your database's *Info* page and click your current version to open the upgrade page:

   [image: Opening Postgres version config in the Render Dashboard]

   [image: Postgres upgrade flow in the Render Dashboard]

2. Click *Upgrade to PostgreSQL <latest-postgres></latest-postgres>* to start the upgrade process.

   A log explorer appears and displays log entries from the upgrade process.

3. When the upgrade completes, your database's status changes from *Upgrading* to *Available*.

> *If the upgrade fails, your database remains on its original PostgreSQL version.*
>
>    Review the logs to identify any issues. If the underlying cause or resolution is unclear, reach out to support in the Render Dashboard.

After the upgrade, your other apps and services resume connecting to your database using the same credentials and connection strings as before.

## Migrating to a new instance

These are the high-level steps for moving your data to a new Render Postgres database with a higher major version:

1. [Create a new database](https://dashboard.render.com/new/database) with the desired version.
2. Disable or suspend any applications that write to your existing database.
   - This guarantees that you can take an up-to-date backup of your existing database.
3. [Take a backup](#taking-a-backup) of your existing database.
4. Restore the backup to your _new_ database.
5. Point all of your applications at the new database. Re-enable the applications that perform writes.

*However*, before you complete the above, we recommend attempting a "dry run" by performing just _these_ steps:

1. [Create a new database](https://dashboard.render.com/new/database) with the desired version.
2. [Take a backup](#taking-a-backup) of your existing database.
3. Restore the backup to your _new_ database.

The dry run enables you to confirm whether a full migration will succeed, and it doesn't require suspending or modifying any of your applications.

### Taking a backup

If your existing database uses a *Standard* instance type or higher, you can trigger a backup directly from your database's *Recovery* page in the [Render Dashboard](https://dashboard.render.com):

[image: List of backups in the Render Dashboard]

Otherwise, you can take a backup using [`pg_dump`](https://www.postgresql.org/docs/current/backup-dump.html). This command dumps your database to a local file (make sure to swap out the appropriate database variables, as well as the hostname for Frankfurt region databases):

```bash
PGPASSWORD={PASSWORD} pg_dump -h oregon-postgres.render.com -U {DATABASE_USER} {DATABASE_NAME} \
   -n public --no-owner > database_dump.sql
```

You can then restore this data to your new database:

```bash
PGPASSWORD={PASSWORD} psql -h oregon-postgres.render.com -U {DATABASE_USER} {DATABASE_NAME} < database_dump.sql
```

If you have _multiple_ databases in your Render Postgres instance, repeat the steps above for each database you want to migrate. Alternatively, you can use [`pg_dumpall`](https://www.postgresql.org/docs/current/app-pg-dumpall.html) to automatically back up all databases in your instance.

For more details on this process, see [Render Postgres Backups and Recovery](postgresql-backups).

### Troubleshooting

If certain statements fail to execute due to a version incompatibility, you might need to manually modify your database dump to resolve these issues. Review the changelogs for each PostgreSQL version ahead of time to identify any such incompatibilities and their resolutions:

<supported-postgres-release-list-md></supported-postgres-release-list-md>

## Minor version updates

Render periodically upgrades your database's minor PostgreSQL version to apply the latest security fixes. Whenever one of these updates requires downtime, we notify you ahead of time via email. In the [Render Dashboard](https://dashboard.render.com), you can schedule your preferred maintenance window or trigger the maintenance manually.