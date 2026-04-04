# Source: https://www.aptible.com/docs/core-concepts/managed-databases/supported-databases/mysql.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.aptible.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# MySQL

> Learn about running secure, Managed MySQL Databases on Aptible

# Available Versions

The following versions of [MySQL](https://www.mysql.com/) are currently available:

| Version |   Status  | End-Of-Life Date | Deprecation Date |
| :-----: | :-------: | :--------------: | :--------------: |
|   8.0   | Available |    April 2026    |    August 2026   |
|   8.4   | Available |    April 2029    |    August 2029   |

MySQL releases LTS versions on a biyearly cadence and fully end-of-lifes (EOL) major versions after 8 years of extended support.

<Note>For databases on EOL versions, Aptible will prevent new databases from being provisioned and mark existing database as `DEPRECATED` on the deprecation date listed above. While existing databases will not be affected, we recommend end-of-life databases to be [upgraded](https://www.aptible.com/docs/core-concepts/managed-databases/managing-databases/database-upgrade-methods#database-upgrades). Restoring a database from a backup will provision a new database that matches the version associated with the backup, even if that version is EOL or Deprecated. The latest version offered on Aptible will always be available for provisioning, regardless of end-of-life date.</Note>

## Connecting with SSL

If you get the following error, you're probably not connecting over SSL:

```
ERROR 1045 (28000): Access denied for user 'aptible'@'ip-[IP_ADDRESS].ec2.internal' (using password: YES)
```

Some tools may require additional configuration to connect with SSL to MySQL:

* When connecting via the `mysql` command line client, add this option: `--ssl-cipher=DHE-RSA-AES256-SHA`.
* When connecting via JetBrains DataGrip (through [`aptible db:tunnel`](/reference/aptible-cli/cli-commands/cli-db-tunnel)), you'll need to set `useSSL` to `true` and `verifyServerCertificate` to `false` in the *Advanced* settings tab for the data source.

Most MySQL clients will *not* attempt verification of the server certificate by default; please consult your client's documentation to enable `verify-identity`, or your client's equivalent option. The relevant documentation for the MySQL command line utility is [here](https://dev.mysql.com/doc/refman/8.0/en/using-encrypted-connections.html#using-encrypted-connections-client-side-configuration).

By default, MySQL Databases on Aptible use a server certificate signed by Aptible for SSL / TLS termination. Databases that have been running since prior to Jan 15th, 2021, will only have a self-signed certificate. See [Database Encryption in Transit](/core-concepts/managed-databases/managing-databases/database-encryption/database-encryption-in-transit#self-signed-certificates) for more details.

## Connecting without SSL

<Warning>Never transmit sensitive or regulated information without SSL. Connecting without SSL should only be done for troubleshooting or debugging.</Warning>

For debugging purposes, you can connect to MySQL without SSL using the `aptible-nossl` user. As the name implies, this user does not require SSL to connect.

## Connecting as `root`

If needed, you can connect as `root` to your MySQL database. The password for `root` is the same as that of the `aptible` user.

# Creating More Databases

Aptible provides you with full access to a MySQL instance. If you'd like to add more databases, you can do so by [Connecting as `root`](/core-concepts/managed-databases/supported-databases/mysql#connecting-as-root), then using SQL to create the database:

```sql  theme={null}
/* Substitute NAME for the actual name you'd like to use */
CREATE DATABASE NAME;
GRANT ALL ON NAME.* to 'aptible'@'%';
```

# Replication

Source-replica [replication](/core-concepts/managed-databases/managing-databases/replication-clustering) is available for MySQL. Replicas can be created using the [`aptible db:replicate`](/reference/aptible-cli/cli-commands/cli-db-replicate) command.

## Failover

MySQL replicas can accept writes without being promoted. However, it should still be promoted to stop following the source Database so that it doesn't encounter issues when the source Database becomes available again. To do so, run the following commands on the Database:

1. `STOP REPLICA IO_THREAD`
2. Run `SHOW PROCESSLIST` until you see `Has read all relay log` in the output.
3. `STOP REPLICA`
4. `RESET MASTER`

After the replica has been promoted, you should update your [Apps](/core-concepts/apps/overview) to use the promoted replica as the primary Database. Once you start using the replica, you should not go back to using the original primary Database. Instead, continue using the promoted replica and create a new replica off it it.

Aptible maintains a link between replicas and their source Database to ensure the source Database cannot be deleted before the replica. To deprovision the source Database after you've failed over to a promoted replica, users with the appropriate [roles and permissions](/core-concepts/security-compliance/access-permissions#full-permission-type-matrix) can unlink the replica from the source Database. Navigate to the replica's settings page to complete the unlinking process. See the [Deprovisioning a Database documentation ](/core-concepts/managed-databases/managing-databases/overview#deprovisioning-databases)for considerations when deprovisioning a Database.

# Data Integrity and Durability

On Aptible, [binary logging](https://dev.mysql.com/doc/refman/8.4/en/binary-log.html) is enabled (i.e., MySQL is configured with `sync-binlog = 1`). Committed transactions are therefore guaranteed to be written to disk.

# Configuration

We strongly recommend against relying only on `SET GLOBAL` with Aptible MySQL Databases.

Any configuration parameters added using `SET GLOBAL` will be discarded if your Database is restarted (e.g. as a result of exceeding [Memory Limits](/core-concepts/scaling/memory-limits), the underlying hardware crashing, or simply as a result of a [Database Scaling](/core-concepts/scaling/database-scaling) operation). In this scenario, unless your App automatically detects this condition and uses `SET GLOBAL` again, your custom configuration will no longer be present.

However, Aptible Support can accommodate reasonable configuration changes so that they can be persisted across restarts (by adding them to a configuration file). If you're contemplating using `SET GLOBAL` (for enabling the [General Query Log](https://dev.mysql.com/doc/refman/8.4/en/query-log.html) as an example), please get in touch with [Aptible Support](/how-to-guides/troubleshooting/aptible-support) to apply the setting persistently.

MySQL Databases on Aptible autotune their buffer pool and chunk size based on the size of their container to improve performance. The `innodb_buffer_pool_size` setting will be set to half of the container memory, and `innodb_buffer_pool_chunk_size` and `innodb_buffer_pool_instances` will be set to approriate values.  You can view all buffer pool settings, including these autotuned values, with the following query: `SHOW VARIABLES LIKE 'innodb_buffer_pool_%'`.

# Connection Security

Aptible MySQL Databases support connections via the following protocols:

* For MySQL version 8.0 and 8.4: `TLSv1.2`, `TLSv1.3`
