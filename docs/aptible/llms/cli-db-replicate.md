# Source: https://www.aptible.com/docs/reference/aptible-cli/cli-commands/cli-db-replicate.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.aptible.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# aptible db:replicate

This command creates a [Database Replica](/core-concepts/managed-databases/managing-databases/replication-clustering). All new Replicas are created with General Purpose Container Profile, which is the [default Container Profile.](/core-concepts/scaling/container-profiles#default-container-profile)

# Synopsis

```
Usage:
  aptible db:replicate HANDLE REPLICA_HANDLE [--container-size SIZE_MB] [--container-profile PROFILE]  [--disk-size SIZE_GB] [--iops IOPS] [--logical --version VERSION] [--key-arn KEY_ARN]

Options:
  --env, [--environment=ENVIRONMENT]
  [--container-size=N]
  [--container-profile PROFILE]
                               # Default: m
  [--size=N]
  [--disk-size=N]
  [--logical], [--no-logical]
  [--version=VERSION]
  [--iops=IOPS]
  [--key-arn=KEY_ARN]
```

> 📘 The `--version` option is only supported for postgresql logical replicas.

# Examples

#### Create a replica with a custom Disk Size

```shell  theme={null}
aptible db:replicate "$DB_HANDLE" "$REPLICA_HANDLE" \
            --disk-size 20
```

#### Create a replica with a custom Container Size

```shell  theme={null}
aptible db:replicate "$DB_HANDLE" "$REPLICA_HANDLE" \
            --container-size 2048
```

#### Create a replica with a custom Container and Disk Size

```shell  theme={null}
aptible db:replicate "$DB_HANDLE" "$REPLICA_HANDLE" \
            --container-size 2048 \
            --disk-size 20
```

#### Create an upgraded replica for logical replication

```shell  theme={null}
aptible db:replicate "$DB_HANDLE" "$REPLICA_HANDLE" \
            --logical --version 12
```

#### Container Sizes (MB)

**General Purpose(M)**: 512, 1024, 2048, 4096, 7168, 15360, 30720, 61440, 153600, 245760

#### Profiles

`m`: General purpose container \
`c`: Compute-optimized container \
`r`: Memory-optimized container

# How Logical Replication Works

[`aptible db:replicate --logical`](/reference/aptible-cli/cli-commands/cli-db-replicate) should work in most cases. This section provides additional details details on how the CLI command works for debugging or if you'd like to know more about what the command does for you.

The CLI command uses the `pglogical` extension to set up logical replication between the existing Database and the new replica Database. At a high level, these are the steps the CLI command takes to setup logical replication for you:

1. Update `max_worker_processes` on the replica based on the number of [PostgreSQL databases](https://www.postgresql.org/docs/current/managing-databases.html) being replicated. `pglogical` uses several worker processes per database so it can easily exhaust the default `max_worker_processes` if replicating more than a couple of databases.
2. Recreate all roles (users) on the replica. `pglogical`'s copy of the source database structure includes assigning the same owner to each table and granting the same permissions. The roles must exist on the replica in order for this to work.
3. For each PostgreSQL database on the source Database, excluding those that beginning with `template`:
   1. Create the database on the replica with the `aptible` user as the owner.
   2. Enable the `pglogical` extension on the source and replica database.
   3. Create a `pglogical` subscription between the source and replica database. This will copy the source database's structure (e.g. schemas, tables, permissions, extensions, etc.).
   4. Start the initial data sync. This will truncate and sync data for all tables in all schemas except for the `information_schema`, `pglogical`, and `pglogical_origin` schemas and schemas that begin with `pg_` (system schemas).

The replica does not wait for the initial data sync to complete before coming online. The time it takes to sync all of the data from the source Database depends on the size of the Database.

When run on the replica, the following query will list all tables that are not in the `replicating` state and, therefore, have not finished syncing the initial data from the source Database.

```postgresql  theme={null}
SELECT * FROM pglogical.local_sync_status WHERE NOT sync_status = 'r';
```
