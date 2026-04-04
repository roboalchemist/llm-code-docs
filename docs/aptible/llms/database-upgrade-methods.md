# Source: https://www.aptible.com/docs/core-concepts/managed-databases/managing-databases/database-upgrade-methods.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.aptible.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Database Upgrades

There are three supported methods for upgrading [Databases](/core-concepts/managed-databases/overview):

* Dump and Restore
* Logical Replication
* Upgrading In-Place

<Tip> To review the available Database versions, use the [`aptible db:versions`](/reference/aptible-cli/cli-commands/cli-db-versions) command.</Tip>

# Dump and Restore

Dump and Restore works by dumping the data from the existing Database and restoring it to a target Database, running the desired version. This method tends to require the most downtime to complete.

**Supported Databases:**

* All Database types support this upgrade method.

<Tip> This upgrade method is relatively simple and reliable and often allows upgrades across multiple major versions at once.</Tip>

## Process

1. Create a new target Database running the desired version.
2. Scale [Services](/core-concepts/apps/deploying-apps/services) that use the existing Database down to zero containers. While this step is not strictly required, it ensures that the containers don't write to the Database during the upgrade.
3. Dump the data from the existing Database to the local filesystem.
4. Restore the data to the target Database from the local filesystem.
5. Update all of the Services that use the original Database to use the target Database.
6. Scale Services back up to their original container counts.

**Guides & Examples:**

* [How to dump and restore PostgreSQL](/how-to-guides/database-guides/dump-restore-postgresql)

# Logical Replication

Logical replication works by creating an upgrade replica of the existing Database and updating all Services that currently use the existing Database to use the replica.

**Supported Databases:** [PostgreSQL](/core-concepts/managed-databases/supported-databases/postgresql) Databases are currently the only ones that support this upgrade method.

<Tip> Upgrading using logical replication is a little more complex than the dump and restore method but only requires a fix amount of downtime regardless of the Database's size. This makes it is a good option for large, production [Databases](/core-concepts/managed-databases/overview) that cannot tolerate much downtime. </Tip>

**Guides & Examples:**

* [How to upgrade PostgreSQL with logical replication](/how-to-guides/database-guides/upgrade-postgresql)

# Upgrading In-Place

Upgrading Databases in-place works similarly to a "traditional" upgrade where, rather than replacing an existing Database instance with a new one, the existing instance is upgraded itself. This means that Services don't have to be updated to use the new instance, but it also makes it difficult or, in some cases, impossible to roll back if you find that a Service isn't compatible with the new version after upgrading.

Additionally, in-place upgrades generally don't work across multiple major versions, so the Database must be upgraded multiple times in situations like this.

Downtime for in-place upgrades varies.

In-place upgrades must be performed by [Aptible Support.](/how-to-guides/troubleshooting/aptible-support)

**Supported Databases:**

* [MongoDB](/core-concepts/managed-databases/supported-databases/mongodb) and [Redis](/core-concepts/managed-databases/supported-databases/redis) have good support for in-place upgrades and, as such, can be upgraded fairly quickly and easily using this method.
* [ElasticSearch](/core-concepts/managed-databases/supported-databases/elasticsearch) can generally be upgraded in-place but there are some exceptions:
  * ES 6.X and below can be upgraded up to ES 6.8
  * ES 7.X can be upgraded up to ES 7.10
    * ES 7 introduced breaking changes to the way the Database is hosted on Aptible so ES 6.X and below cannot be upgraded to ES 7.X in-place.
* [PostgreSQL](/core-concepts/managed-databases/supported-databases/postgresql) supports in-place upgrades but the process is much more involved. As such, in-place upgrades for PostgreSQL Databases are reserved for when none of the other upgrade methods are viable.
  * Aptible will not offer in-place upgrades crossing from pre-15 PostgreSQL versions to PostgreSQL 15+ because of a [dependent change in glibc on the underlying Debian operating system](https://wiki.postgresql.org/wiki/Locale_data_changes). Instead, the following options are available to migrate existing pre-15 PostgreSQL databases to PostgreSQL 15+:
    * [Dump and restore PostgreSQL](/how-to-guides/database-guides/dump-restore-postgresql)
    * [Upgrade PostgreSQL with logical replication](/how-to-guides/database-guides/upgrade-postgresql)

**Guides & Examples:**

* [How to upgrade Redis](/how-to-guides/database-guides/upgrade-redis)
* [How to upgrade MongoDB](/how-to-guides/database-guides/upgrade-mongodb)
