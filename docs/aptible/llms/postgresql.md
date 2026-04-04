# Source: https://www.aptible.com/docs/core-concepts/managed-databases/supported-databases/postgresql.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.aptible.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# PostgreSQL

> Learn about running secure, Managed PostgreSQL Databases on Aptible

# Available Versions

The following versions of [PostgreSQL](https://www.postgresql.org/) are currently available:

| Version |   Status  | End-Of-Life Date | Deprecation Date |
| :-----: | :-------: | :--------------: | :--------------: |
|    13   | Available |   November 2025  |   February 2026  |
|    14   | Available |   November 2026  |   February 2027  |
|    15   | Available |   November 2027  |   February 2028  |
|    16   | Available |   November 2028  |   February 2029  |
|    17   | Available |   November 2029  |   February 2030  |

<Info>PostgreSQL releases new major versions annually, and supports major versions for 5 years before it is considered end-of-life and no longer maintained.</Info>

<Note>For databases on EOL versions, Aptible will prevent new databases from being provisioned and mark existing database as `DEPRECATED` on the deprecation date listed above. While existing databases will not be affected, we recommend end-of-life databases to be [upgraded](https://www.aptible.com/docs/core-concepts/managed-databases/managing-databases/database-upgrade-methods#database-upgrades). Restoring a database from a backup will provision a new database that matches the version associated with the backup, even if that version is EOL or Deprecated. The latest version offered on Aptible will always be available for provisioning, regardless of end-of-life date.</Note>

# Connecting to PostgreSQL

Aptible PostgreSQL [Databases](/core-concepts/managed-databases/overview) require authentication and SSL to connect.

## Connecting with SSL

Most PostgreSQL clients will attempt connection over SSL by default. If yours doesn't, try appending `?ssl=true` to your connection URL, or review your client's documentation.

Most PostgreSQL clients will *not* attempt verification of the server certificate by default, please consult your client's documentation to enable `verify-full`, or your client's equivalent option. The relevant documentation for libpq is [here](https://www.postgresql.org/docs/current/libpq-ssl.html#LIBQ-SSL-CERTIFICATES).

By default, PostgreSQL Databases on Aptible use a server certificate signed by Aptible for SSL / TLS termination. Databases that have been running since prior to Jan 15th, 2021 will only have a self-signed certificate. See [Database Encryption in Transit](/core-concepts/managed-databases/managing-databases/database-encryption/database-encryption-in-transit#self-signed-certificates) for more details.

# Extensions

Aptible supports two families of images for Postgres: default and contrib.

* The default images have a minimal number of extensions installed, but do include PostGIS.

* The alternative contrib images have a larger number of useful extensions installed. The list of available extensions is visible below.

* In PostgreSQL versions 14 and newer, there is no separate contrib image: the listed extensions are available in the default image.

| Extension     | Avaiable in versions |
| ------------- | -------------------- |
| plpythonu     | 9.5 - 11             |
| plpython2u    | 9.5 - 11             |
| plpython3u    | 9.5 - 12             |
| plperl        | 9.5 - 12             |
| plperlu       | 9.5 - 12             |
| mysql\_fdw    | 9.5 - 11             |
| PLV8          | 9.5 - 10             |
| multicorn     | 9.5 - 10             |
| wal2json      | 9.5 - 17             |
| pg-safeupdate | 9.5 - 11             |
| pg\_repack    | 9.5 - 17             |
| pgagent       | 9.5 - 13             |
| pgaudit       | 9.5 - 17             |
| pgcron        | 10                   |
| pgvector      | 15-17                |
| pg\_trgm      | 12 - 17              |

If you require a particular PostgreSQL plugin, contact [Aptible Support](/how-to-guides/troubleshooting/aptible-support) to identify whether a contrib image is a good fit. Alternatively, you can launch a new PostgreSQL database using a contrib image with the [`aptible db:create`](/reference/aptible-cli/cli-commands/cli-db-create) command.

# Replication

Primary-standby [replication](/core-concepts/managed-databases/managing-databases/replication-clustering) is available for PostgreSQL. Replicas can be created using the [`aptible db:replicate`](/reference/aptible-cli/cli-commands/cli-db-replicate) command.

## Failover

PostgreSQL replicas can be manually promoted to stop following the primary and start accepting writes. To do so, run one of the following commands depending on your Database's version:

PostgreSQL 12 and higher

```
SELECT pg_promote();
```

PostgreSQL 11 and lower

```
COPY (SELECT 'fast') TO '/var/db/pgsql.trigger';
```

After the replica has been promoted, you should update your [Apps](/core-concepts/apps/overview) to use the promoted replica as the primary Database. Once you start using the replica, you should not go back to using the original primary Database. Instead, continue using the promoted replica and create a new replica off of it.

Aptible maintains a link between replicas and their source Database to ensure the source Database cannot be deleted before the replica. To deprovision the source Database after you've failed over to a promoted replica, users with the appropriate [roles and permissions](/core-concepts/security-compliance/access-permissions#full-permission-type-matrix) can unlink the replica from the source Database. Navigate to the replica's settings page to complete the unlinking process. See the [Deprovisioning a Database](/how-to-guides/platform-guides/deprovision-resources) documentation for considerations when deprovisioning a Database.

# Data Integrity and Durability

On Aptible, PostgreSQL is configured with default settings for [write-ahead logging](https://www.postgresql.org/docs/current/static/wal-intro.html). Committed transactions are therefore guaranteed to be written to disk.

# Point-in-time Recovery

Point-in-time Recovery (PITR) is available for PostgreSQL 13 and newer. PITR lets you restore your database to any specific moment in time, protecting against accidental data deletions, corruptions, or other errors.

Aptible automatically enables PITR for new PostgreSQL 13+ databases if your Environment's backup retention policy has at least 1 day of recovery data retention configured.

For more details on configuring and using PITR, see [Point-in-time Recovery for PostgreSQL](/core-concepts/managed-databases/managing-databases/database-backups#point-in-time-recovery-for-postgresql).

# Configuration

A PostgreSQL database's [`pg_settings`](https://www.postgresql.org/docs/current/view-pg-settings.html) can be changed with [`ALTER SYSTEM`](https://www.postgresql.org/docs/current/sql-altersystem.html). Changes made this way are written to disk and will persist across database restarts.

PostgreSQL databases on Aptible autotune the size of their caches and working memory based on the size of their container in order to improve performance.

The following settings are autotuned:

* `shared_buffers`

* `effective_cache_size`

* `work_mem`

* `maintenance_work_mem`

* `checkpoint_completion_target`

* `default_statistics_target`

Modifying these settings is not recommended as the setting will no longer scale with the size of the database's container.

## Autovacuum

Postgres [Autovacuum](https://www.postgresql.org/docs/current/routine-vacuuming.html#AUTOVACUUM) is enabled by default on all supported Aptible PostgreSQL managed databases. Autovacuum is configured with
default settings related to [Vacuum](https://www.postgresql.org/docs/current/sql-vacuum.html), which can be inspected with:

```
SELECT * FROM pg_settings WHERE name LIKE '%autovacuum%;'
```

The settings associated with autovacuum can be adjusted with [ALTER SYSTEM](https://www.postgresql.org/docs/current/sql-altersystem.html)

# Connection Security

Aptible PostgreSQL Databases support connections via the following protocols:

* For PostgreSQL versions 9.6, 10, 11, and 12: `TLSv1.0`, `TLSv1.1`, `TLSv1.2`

* For PostgreSQL versions 13 and 14: `TLSv1.2`

* For PostgreSQL versions 15, 16, and 17: `TLSv1.2`, `TLSv1.3`
