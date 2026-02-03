# Source: https://www.aptible.com/docs/core-concepts/managed-databases/supported-databases/redis.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.aptible.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Redis

> Learn about running secure, Managed Redis Databases on Aptible

## Available Versions

The following versions of [Redis](https://redis.io/) are currently available:

| Version |   Status   | End-Of-Life Date | Deprecation Date |
| :-----: | :--------: | :--------------: | :--------------: |
|   6.2   |  Available |        N/A       |        N/A       |
|   7.0   | Deprecated |     July 2024    |     Dec 2025     |
|   7.2   |  Available |   February 2026  |     May 2026     |
|   8.0   |  Available |        N/A       |        N/A       |
|   8.2   |  Available |        N/A       |        N/A       |

<Info>Redis typically releases new major versions annually with a minor version release 6 months after. The latest major version is fully maintained and supported by Redis, while the previous major version and minor version receive security fixes only. All other versions are considered end-of-life.</Info>

<Note>For databases on EOL versions, Aptible will prevent new databases from being provisioned and mark existing database as `DEPRECATED` on the deprecation date listed above. While existing databases will not be affected, we recommend end-of-life databases to be [upgraded](https://www.aptible.com/docs/core-concepts/managed-databases/managing-databases/database-upgrade-methods#database-upgrades). Restoring a database from a backup will provision a new database that matches the version associated with the backup, even if that version is EOL or Deprecated. The latest version offered on Aptible will always be available for provisioning, regardless of end-of-life date.</Note>

# Connecting to Redis

Aptible Redis [Databases](/core-concepts/managed-databases/overview) expose two [Database Credentials](/core-concepts/managed-databases/connecting-databases/database-credentials):

* A `redis` credential. This is for plaintext connections, so you shouldn't use it for sensitive or regulated information.
* A `redis+ssl` credential. This accepts connections over TLS, and it's the one you should use for regulated or sensitive information.

<Tip> The SSL port uses a valid certificate for its host, so you’re encouraged to verify the certificate when connecting.</Tip>

# Replication

Master-replica [replication](/core-concepts/managed-databases/managing-databases/replication-clustering) is available for Redis. Replicas can be created using the [`aptible db:replicate`](/reference/aptible-cli/cli-commands/cli-db-replicate) command.

## Failover

Redis replicas can be manually promoted to stop following the primary and start accepting writes. To do so, run the following command on the Database:

```
REPLICAOF NO ONE
```

After the replica has been promoted, you should update your [Apps](/core-concepts/apps/overview) to use the promoted replica as the primary Database. Once you start using the replica, you should not go back to using the original primary Database. Instead, continue using the promoted replica and create a new replica off of it.

The effects of `REPLICAOF NO ONE` are not persisted to the Database's filesystem, so the next time the Database starts, it will attempt to replicate the source Database again. In order to persist this change, contact [Aptible Support](/how-to-guides/troubleshooting/aptible-support) with the name of the Database and request that it be permanently promoted.

Aptible maintains a link between replicas and their source Database to ensure the source Database cannot be deleted before the replica. To deprovision the source Database after you've failed over to a promoted replica, users with the appropriate [roles and permissions](/core-concepts/security-compliance/access-permissions#full-permission-type-matrix) can unlink the replica from the source database. Navigate to the replica's settings page to complete the unlinking process. See the [Deprovisioning a Database](/how-to-guides/platform-guides/deprovision-resources) documentation for considerations when deprovisioning a Database.

# Data Integrity and Durability

On Aptible, Redis is by default configured to use both Append-only file and RDB backups. This means your data is stored in two formats on disk. Redis on Aptible uses the every-second fsync policy for AOF, and the following configuration for RDB backups:

```
save 900 1
save 300 10
save 60 10000
```

This configuration means Redis performs an RDB backup every 900 seconds at most, every 300 seconds if 10 keys are changed, and every 60 seconds if 10000 keys are changed. Additionally, each time a write operation is performed, it is immediately written to the append-only file and flushed from the kernel to the disk (using fsync) one time every second.

Broadly speaking, Redis is not designed to be a durable data store. We do not recommend using Redis in cases where durability is required.

## RDB-only flavors

If you'd like to use Redis with AOF disabled and RDB persistence enabled, we provide Redis images in this configuration that you can elect to use.

One of the benefits of RDB-only persistence is the fact that for a given database size, the number of I/O operations is bound by the above configuration, whatever the activity on the database is. However, if Redis crashes or runs out of memory between RDB backups, data might be lost.

Note that an RDB backup means Redis is writing data to disk and is not the same thing as an Aptible [Database Backups](/core-concepts/managed-databases/managing-databases/database-backups). Aptible Database Backups are daily snapshots of your Database's disk. In other words: Redis periodically commits data to disk (according to the above schedule), and Aptible periodically makes a snapshot of the disk (which includes the data).

These database types are displayed as `RDB-Only Persistence` on the Dashboard.

## Memory-only flavors

If you'd like to use Redis as a memory-only store (i.e., without any persistence), we provide Redis images with AOF and RDB persistence disabled.

If you use one of those (they aren't the default), make sure you understand that\*\* all data in Redis will be lost upon restarting or resizing your memory-only instance or upon your memory-only instance running out of memory.\*\*

If you'd like to use a memory-only flavor, provision it using the [`aptible db:create`](/reference/aptible-cli/cli-commands/cli-db-create) command (substitute `$HANDLE` with your desired handle for this Database). Since the disk will only be used to store configuration files, use the minimum size (with the `--disk-size` parameter as listed below):

```shell  theme={null}
aptible db:create \
        --type redis \
        --version 4.0-nordb \
        --disk-size 1 \
        "$HANDLE"
```

These database types are displayed as `NO PERSISTENCE` on the Dashboard.

## Specifying a flavor

When creating a Redis database from the Aptible Dashboard, you only have the option of version with both AOF and RDB enabled.

To list available Redis flavors that can be passed to [`aptible db:create`](/reference/aptible-cli/cli-commands/cli-db-create) via the `--version` option, use the [`aptible db:versions`](/reference/aptible-cli/cli-commands/cli-db-versions) command:

* `..-aof` are the AOF + RDB ones.
* `..-nordb` are the memory-only ones.
* The unadorned versions are RDB-Only.

# Configuration

Contact [Aptible Support](/how-to-guides/troubleshooting/aptible-support) if you have a need to change the configuration of a Redis database on Aptible.

# Connection Security

Aptible Redis databases support connections via the following protocols:

* For Redis versions 2.8, 3.0, 3.2, 4.0, and 5.0: `TLSv1.0`, `TLSv1.1`, `TLSv1.2`
* For Redis versions 6.0, 6.2, and 7.0: `TLSv1.2`
