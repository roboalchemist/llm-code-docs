# Source: https://render.com/docs/postgresql-backups.md

# Render Postgres Recovery and Backups — Restore your database to a previous state and export logical backups.


> *Need to recover lost data? [*Start here.*](#perform-a-recovery)*
>
> We're happy to help with restores and disaster recovery. Reach out to our support team in the [Render Dashboard](https://dashboard.render.com).

Render continually backs up paid Render Postgres databases to provide *point-in-time recovery* (PITR). This enables you to restore your database to any previous state from the past few days, so you can recover from an accidental table drop or other data loss.

Your database's available recovery window depends on your [workspace plan](/pricing):

| Workspace plan | Recovery window |
| --- | --- |
| Hobby | Past 3 days |
| Professional or higher | Past 7 days |

> *Upgrading from Hobby does not retroactively "backfill" your recovery window.*
>
> Instead, your existing 3-day window extends to 7 days going forward.

When you trigger PITR, Render spins up a _new_ database instance that reflects your original instance's state at a specified time in the past. This enables you to validate the new instance in isolation before updating your services to use it.

[diagram]

- *If your recovery instance reflects the state you expect,* you can then configure your other services to use it instead of the original instance.
- *Otherwise,* you can delete the recovery instance and initiate a new recovery using a different point in time.

## Perform a recovery

> *Render does not provide recovery capabilities for the Free Render Postgres instance type.*
>
> To enable these capabilities, [upgrade your instance type](postgresql-creating-connecting#changing-your-instance-type).

1. In the [Render Dashboard](https://dashboard.render.com), select your database from the service list and open its *Recovery* page.

2. Scroll down to the *Point-in-Time Recovery* section and click *Restore Database*:

   [image: Triggering PITR in the Render Dashboard]

3. The following form appears:

   [image: PITR restore modal in the Render Dashboard]

4. Provide a name for the new database instance.
5. Specify an available date and time to restore to.

   - You can't restore to a time that's within ten minutes of the current time.

6. Select whether to *Copy Existing Settings*.
   - If you select *No*, you'll have the option to specify a different instance type, Datadog API key, and/or project for the recovery instance.
   - The recovery instance _always_ copies the [IP address allow list](postgresql-creating-connecting#restricting-external-access) from the original instance.
7. Click *Start Recovery* to initiate the restore.

   - If you selected *No* in the previous step, click *Customize Recovery* and then provide your new settings for the recovery instance.

8. In your service list, the recovery instance's status will advance from *Recovery In Progress* to *Creating*, and then to *Available* when it's ready to accept connections.

9. Validate that the data in the recovery instance is what you expect.

   - You can connect to the recovery instance from your terminal using the *PSQL Command* provided on the database's *Info* page.

10. Update your services and other tools to connect to the recovery instance instead of the original instance.

    - The recovery instance's name and connection strings are available in the Render Dashboard.
    - [Environment groups](configure-environment-variables#environment-groups) enable you to update the connection string for multiple services in one place.

11. After verifying that all systems are successfully connected to the recovery instance, you can delete or suspend the original instance.

The recovery is complete. Your recovery instance is now your primary instance.

## Logical backups

You can create and export logical backups of your database in the [Render Dashboard](https://dashboard.render.com). Download these backups for long-term retention or to restore into a new database instance.

Render retains logical backups for seven days after creation, regardless of your workspace plan.

> *Render does not create logical backups for the Free Render Postgres instance type.*
>
> To create a logical backup for a free instance, do one of the following:
>
> - [Upgrade your instance type.](postgresql-creating-connecting#changing-your-instance-type)
> - Use the `pg_dump` utility from your local machine.

### Trigger a backup

From your database's *Recovery* page, click *Create export*:

[image: Creating a database export in the Render Dashboard]

> You can't trigger an export if _another_ export is in progress for the same database.

When it's ready, your database's new export appears in the table on its *Recovery* page. Each export is provided as a compressed directory file (`.dir.tar.gz`). Click any export's download link to save it to your local machine.

> *Interested in automating logical backup retention?*
>
> See [Backup Render Postgres to Amazon S3](backup-postgresql-to-s3). This guide walks through creating a [cron job](cronjobs) that uploads SQL backups from `pg_dump` to S3.

### Restoring from a backup file

> *Read this before you proceed:*
>
> - The commands below include flags to _drop_ relevant databases and then recreate them.
>   - Do not restore into a database that contains important data in the same schema as the export.
> - In the event of data loss, we recommend instead using [*point-in-time recovery*](#perform-a-recovery) to restore your database.
>   - PITR almost always enables you to recover more recent data than what's available in your latest export.

You can use an exported backup to restore your data into a PostgreSQL instance running on Render or your local machine:

1. Go to your database's *Recovery* page and click the `.dir.tar.gz` download link for any available export.
   - The downloaded export's filename indicates its time of creation (e.g., `2025-02-03T19_21Z.dir.tar.gz`).
2. If you're restoring into a Render-hosted database, obtain its [external database URL](postgresql-creating-connecting#external-connections).
3. Install [pg_restore](https://www.postgresql.org/docs/current/app-pgrestore.html) for the major version of the PostgreSQL instance you are restoring into.
4. Run the following commands, providing your export file and the target database URL where indicated:

   ```shell{outputLines:1,3-4}
   # Extract the export
   tar -zxvf 2025-02-03T19_21Z.dir.tar.gz

   # Restore the export to your database using its external connection string (available in the dashboard)
   pg_restore --dbname=$external_database_url --verbose --clean --if-exists --no-owner --no-privileges --format=directory 2025-02-03T19:21Z/my_render_database_name
   ```