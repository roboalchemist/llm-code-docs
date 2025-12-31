# Source: https://www.aptible.com/docs/core-concepts/managed-databases/managing-databases/replication-clustering.md

# Database Replication and Clustering

<Info> Database Replication and Clustering is only available on [Production and Enterprise](https://www.aptible.com/pricing)[ plans.](https://www.aptible.com/pricing)</Info>

Aptible simplifies Database replication (PostgreSQL, MySQL, Redis) and clustering (MongoDB) databases in high-availability setups by automatically deploying the Database Containers across different Availability Zones (AZ).

# Support by Database Type

Aptible supports replication or clustering for a number of [Databases](/core-concepts/managed-databases/overview):

* [Redis:](/core-concepts/managed-databases/supported-databases/redis) Aptible supports creating read-only replicas for Redis.
* [PostgreSQL:](/core-concepts/managed-databases/supported-databases/postgresql) Aptible supports read-only hot standby replicas for PostgreSQL databases. PostgreSQL replicas utilize a [replication slot](https://www.postgresql.org/docs/current/warm-standby.html#STREAMING-REPLICATION-SLOTS) on the primary database which may increase WAL file retention on the primary. We recommend using a [Metric Drain](/core-concepts/observability/metrics/metrics-drains/overview) to monitor disk usage on the primary Database. PostgreSQL Databases support [Logical Replication](/how-to-guides/database-guides/upgrade-postgresql) using the [`aptible db:replicate`](/reference/aptible-cli/cli-commands/cli-db-replicate) CLI command with the `--logical` flag for the purpose of upgrading the Database with minimal downtime.
* [MySQL:](/core-concepts/managed-databases/supported-databases/mysql) Aptible supports creating replicas for MySQL Databases. While these replicas do not prevent writes from occurring, Aptible does not support writing to MySQL replicas. Any data written directly to a MySQL replica (and not the primary) may be lost.
* [MongoDB:](/core-concepts/managed-databases/supported-databases/mongodb) Aptible supports creating MongoDB replica sets. To ensure that your replica is fault-tolerant, you should follow the [MongoDB recommendations for a number of instances in a replica set](https://docs.mongodb.com/manual/core/replica-set-architectures/#consider-fault-tolerance) when creating a replica set. We also recommend that you review the [readConcern](https://docs.mongodb.com/manual/reference/read-concern/), [writeConcern](https://docs.mongodb.com/manual/reference/write-concern/) and [connection url](https://docs.mongodb.com/manual/reference/connection-string/#replica-set-option) documentation to ensure that you are taking advantage of useful features offered by running a MongoDB replica set.

# Creating Replicas

Replicas can be created for supported databases using the [`aptible db:replicate`](/reference/aptible-cli/cli-commands/cli-db-replicate) command. All new Replicas are created with General Purpose Container Profile, which is the [default Container Profile.](/core-concepts/scaling/container-profiles#default-container-profile)

<Warning> Creating a replica on Aptible has a 6 hour timeout. While most Databases can be replicated in under 6 hours, some very large databases may take longer than 6 hours to create a replica. If your attempt to create a replica fails after hitting the 6 hour timeout, reach out to [Aptible Support](/how-to-guides/troubleshooting/aptible-support). </Warning>
