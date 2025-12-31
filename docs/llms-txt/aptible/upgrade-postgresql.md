# Source: https://www.aptible.com/docs/how-to-guides/database-guides/upgrade-postgresql.md

# Upgrade PostgreSQL with logical replication

The goal of this guide is to [upgrade a PostgreSQL Database](/core-concepts/managed-databases/managing-databases/database-upgrade-methods) to a newer version by means of [logical replication](/core-concepts/managed-databases/managing-databases/database-upgrade-methods#logical-replication). Aptible uses [pglogical](https://github.com/2ndQuadrant/pglogical) to create logical replicas.

> 📘 The main benefit of using logical replication is that the replica can be created beforehand and will stay up-to-date with the source Database until it's time to cut over to the new Database. This allows for upgrades to be performed with minimal downtime.

## Preparation

#### **Step 0: Prerequisites**

Install [Aptible CLI](/reference/aptible-cli/cli-commands/overview) and the [PostgreSQL Client Tools,](https://www.postgresql.org/download/) `psql`.

#### **Step 1: Test the schema**

If data is being transferred to a Database running a different PostgreSQL version than the original, first check that the schema can be restored on the desired version by following the [How to test a PostgreSQL Database's schema on a new version](/how-to-guides/database-guides/test-schema-new-version) guide.

#### **Step 2: Test the upgrade**

Testing the schema should catch a number of issues, but it's also recommended to test the upgrade before performing it in production. The easiest way to do this is to restore the latest backup of the Database and perform the upgrade against the restored Database. The restored Database should have the same Container size as the production Database.

Example:

```sql  theme={null}
aptible backup:restore 1234
--handle upgrade-test
--container- size 4096
```

#### **Step 3: Configuration**

Collect information on the Database you'd like to upgrade and store it in the following environment variables for use later in the guide:

* `SOURCE_HANDLE` - The handle (i.e. name) of the Database.

* `ENVIRONMENT` - The handle of the Environment the Database belongs to.

Example:

```sql  theme={null}
SOURCE_HANDLE = 'source-db'
ENVIRONMENT = 'test-environment'
```

Collect information on the replica and store it in the following environment variables:

* `REPLICA_HANDLE` - The handle (i.e., name) for the Database.

* `REPLICA_VERSION` - The desired PostgreSQL version. Run `aptible db:versions` to see a full list of options.

* `REPLICA_CONTAINER_SIZE` (Optional) - The size of the replica's container in MB. Having more memory and CPU available speeds up the initialization process up to a certain point. See the [Database Scaling](/core-concepts/scaling/database-scaling#ram-scaling) documentation for a full list of supported container sizes.

Example:

```sql  theme={null}
REPLICA_HANDLE = 'upgrade-test'
REPLICA_VERSION = '14'
REPLICA_CONTAINER_SIZE = 4096
```

#### **Step 4: Tunnel into the source Database**

In a separate terminal, create a [Database Tunnel](/core-concepts/managed-databases/connecting-databases/database-tunnels) to the source Database using the `aptible db:tunnel` command.

Example:

```sql  theme={null}
aptible db:tunnel "$SOURCE_HANDLE" --environment "$ENVIRONMENT"
```

The tunnel will block the current terminal until it's stopped. Collect the tunnel's full URL, which is printed by [`aptible db:tunnel`](/reference/aptible-cli/cli-commands/cli-db-tunnel), and store it in the `SOURCE_URL` environment variable in the original terminal.

Example:

```sql  theme={null}
SOURCE_URL = 'postgresql://aptible:pa$word@localhost.aptible.in:5432/db'
```

#### **Step 5: Check for existing pglogical nodes**

Each PostgreSQL database on the server can only have a single `pglogical` node. If there's already an existing node, the replica will fail setup. The following script will check for existing pglogical nodes.

```sql  theme={null}
psql "$SOURCE_URL" --tuples-only --no-align --command \
  'SELECT datname FROM pg_database WHERE datistemplate IS FALSE' |

while IFS= read -r db; do
  psql "$SOURCE_URL" -v ON_ERROR_STOP=1 << EOF &> /dev/null
    \connect "$db"
    SELECT pglogical.pglogical_node_info();
EOF

  if [ $? -eq 0 ]; then
    echo "pglogical node found on $db"
  fi
done
```

If the command does not report any nodes, no action is necessary. If it does, either replication will have to be set up manually instead of using `aptible db:replicate --logical`, or the node will have to be dropped.

Note that if logical replication was previously attempted, but failed, then the node could be left behind from the previous attempt. See the [Cleanup](/how-to-guides/database-guides/upgrade-postgresql#cleanup) section and follow the instructions for cleaning up the source Database.

#### **Step 6: Check for tables without a primary key**

Logical replication requires that rows be uniquely identifiable in order to function properly. This is most easily accomplished by ensuring all tables have a primary key.

The following script will iterate over all PostgreSQL databases on the Database server and list tables that do not have a primary key:

```sql  theme={null}
psql "$SOURCE_URL" --tuples-only --no-align --command \
'SELECT datname FROM pg_database WHERE datistemplate IS FALSE' |

while IFS= read -r db; do
  echo "Database: $db"
  psql "$SOURCE_URL" << EOF
\connect "$db";

    SELECT tab.table_schema, tab.table_name
    FROM information_schema.tables tab
    LEFT JOIN information_schema.table_constraints tco
              ON tab.table_schema = tco.table_schema
              AND tab.table_name = tco.table_name
              AND tco.constraint_type = 'PRIMARY KEY'
    WHERE tab.table_type = 'BASE TABLE'
          AND tab.table_schema NOT IN('pg_catalog', 'information_schema', 'pglogical')
          AND tco.constraint_name IS NULL
    ORDER BY table_schema, table_name;
EOF
done
```

If all of the databases return `(0 rows)` then no action is necessary.

Example output:

```sql  theme={null}
Database: db
You are now connected to database "db" as user "aptible".
 table_schema | table_name
--------------+------------
(0 rows)

Database: postgres
You are now connected to database "postgres" as user "aptible".
 table_schema | table_name
--------------+------------
(0 rows)
```

If any tables come back without a primary key, one can be added to an existing column or a new column with [`ALTER TABLE`](https://www.postgresql.org/docs/current/sql-altertable.html).

#### **Step 7: Create the replica**

The upgraded replica can be created ahead of the actual upgrade as it will stay up-to-date with the source Database.

```sql  theme={null}
aptible db:replicate "$SOURCE_HANDLE" "$REPLICA_HANDLE" \
  --logical \
  --version "$REPLICA_VERSION" \
  --environment "$ENVIRONMENT" \
  --container-size "${REPLICA_CONTAINER_SIZE:-4096}"
```

If the command raises errors, review the operation logs output by the command for an explanation as to why the error occurred. In order to attempt logical replication after the issue(s) have been addressed, the source Database will need to be cleaned up. See the [Cleanup](/how-to-guides/database-guides/upgrade-postgresql#cleanup) section and follow the instructions for cleaning up the source Database. The broken replica also needs to be deprovisioned in order to free up its handle to be used by the new replica:

```sql  theme={null}
aptible db:deprovision "$REPLICA_HANDLE" --environment "$ENVIRONMENT"
```

If the operation is successful, then the replica has been successfully set up. All that remains is for it to finish initializing (i.e. pulling all existing data), then it will be ready to be cut over to.

> 📘 `pglogical` will copy the source Database's structure at the time the subscription is created. However, subsequent changes to the Database structure, a.k.a. Data Definition Language (DDL) commands, are not included in logical replication. These commands need to be applied to the replica as well as the source Database to ensure that changes to the data are properly replicated.

> `pglogical` provides a convenient `replicate_ddl_command` function that, when run on the source Database, applies a DDL command to the source Database then queues the statement to be applied to the replica. For example, to add a column to a table:

```sql  theme={null}
SELECT pglogical.replicate_ddl_command('ALTER TABLE public.foo ADD COLUMN bar TEXT;');
```

> ❗️ `pglogical` creates temporary replication slots that may show up inactive at times, theses temporary slots must not be deleted. Deleting these slots will disrupt `pglogical`

## Execution

#### **Step 1: Tunnel into the replica**

In a separate terminal, create a [Database Tunnel](/core-concepts/managed-databases/connecting-databases/database-tunnels) to the replica using the Aptible CLI.

```sql  theme={null}
aptible db:tunnel "$REPLICA_HANDLE" --environment "$ENVIRONMENT"
```

The tunnel will block the current terminal until it's stopped. Collect the tunnel's full URL, which is printed by [`aptible db:tunnel`](/reference/aptible-cli/cli-commands/cli-db-tunnel), and store it in the `REPLICA_URL` environment variable in the original terminal.

Example:

```sql  theme={null}
REPLICA_URL='postgresql://aptible:passw0rd@localhost.aptible.in:5432/db'
```

#### **Step 2: Wait for initialization to complete**

While replicas are usually created very quickly, it can take some time to pull all of the data from the source Database depending on its disk footprint. The replica can be queried to see what tables still need to be initialized.

```sql  theme={null}
SELECT * FROM pglogical.local_sync_status WHERE NOT sync_status = 'r';
```

If any rows are returned, the replica is still initializing. This query can be used in a short script to test and wait for initialization to complete on all databases on the replica:

```sql  theme={null}
psql "$REPLICA_URL" --tuples-only --no-align --command \
  'SELECT datname FROM pg_database WHERE datistemplate IS FALSE' |

while IFS= read -r db; do
  while psql "$REPLICA_URL" --tuples-only --quiet << EOF | grep -E '.+'; do
    \connect "$db"
    SELECT * FROM pglogical.local_sync_status WHERE NOT sync_status = 'r';
EOF
    sleep 3
  done
done
```

There is a [known issue](https://github.com/2ndQuadrant/pglogical/issues/337) with `pglogical` in which, during replica initialization, replication may pause until the next time the source Database is written to. For production Databases, this usually isn't an issue since it's being actively used, but for Databases that aren't used much, like Databases that may have been restored to test logical replication, this issue can arise.

The following script works similarly to the one above, but it also creates a table, writes to it, then drops the table in order to ensure that initialization continues even if the source Database is idle:

```sql  theme={null}
psql "$REPLICA_URL" --tuples-only --no-align --command \
  'SELECT datname FROM pg_database WHERE datistemplate IS FALSE' |

while IFS= read -r db; do
  while psql "$REPLICA_URL" --tuples-only --quiet << EOF | grep -E '.+'; do
    \connect "$db"
    SELECT * FROM pglogical.local_sync_status WHERE NOT sync_status = 'r';
EOF
    psql "$SOURCE_URL" -v ON_ERROR_STOP=1 --quiet << EOF
      \connect "$db"
      CREATE TABLE _aptible_logical_sync (col INT);
      INSERT INTO _aptible_logical_sync VALUES (1);
      DROP TABLE _aptible_logical_sync;
EOF

    sleep 3
  done
done
```

Once the query returns zero rows from the replica or one of the scripts completes, the replica has finished initializing, which means it's ready to be cut over to.

#### **Optional: Speeding Up Initialization**

Each index on a table adds overhead to inserting rows, so the more indexes a table has, the longer it will take to be copied over. This can cause large Databases or those with many indexes to take much longer to initialize. If the initialization process appears to be going slowly, all of the indexes (except for primary keys) can be disabled:

```sql  theme={null}
psql "$REPLICA_URL" --tuples-only --no-align --command \
  'SELECT datname FROM pg_database WHERE datistemplate IS FALSE' |

while IFS= read -r db; do
  echo "Database: $db"
  psql "$REPLICA_URL" << EOF
    \connect "$db"

    UPDATE pg_index SET indisready = FALSE WHERE indexrelid IN (
      SELECT idx.indexrelid FROM pg_index idx
      INNER JOIN pg_class cls ON idx.indexrelid = cls.oid
      INNER JOIN pg_namespace nsp ON cls.relnamespace = nsp.oid
      WHERE nsp.nspname !~ '^pg_'
      AND nsp.nspname NOT IN ('information_schema', 'pglogical')
      AND idx.indisprimary IS FALSE
    );
EOF
done

# Reload in order to restart the current COPY operation without indexes
aptible db:reload "$REPLICA_HANDLE" --environment "$ENVIRONMENT"
```

After the replica has been initialized, the indexes will need to be rebuilt. This can still take some time for large tables but is much faster than the indexes being evaluated each time a row is inserted:

```sql  theme={null}
psql "$REPLICA_URL" --tuples-only --no-align --command \
  'SELECT datname FROM pg_database WHERE datistemplate IS FALSE' |

while IFS= read -r db; do
  echo "Database: $db"
  psql "$REPLICA_URL" --tuples-only --no-align --quiet << EOF |
    \connect "$db"

    SELECT CONCAT('"', nsp.nspname, '"."', cls.relname, '"') FROM pg_index idx
      INNER JOIN pg_class cls ON idx.indexrelid = cls.oid
      INNER JOIN pg_namespace nsp ON cls.relnamespace = nsp.oid
      WHERE nsp.nspname !~ '^pg_'
      AND nsp.nspname NOT IN ('information_schema', 'pglogical')
      AND idx.indisprimary IS FALSE
      AND idx.indisready IS FALSE;
EOF

  while IFS= read -r index; do
    echo "Reindexing: $index"
    psql "$REPLICA_URL" --quiet << EOF
      \connect "$db"

      REINDEX INDEX CONCURRENTLY $index;
EOF
  done
done
```

If any indexes have issues reindexing `CONCURRENTLY` this keyword can be removed, but note that when not indexing concurrently, the table the index belongs to will be locked, which will prevent writes while indexing.

#### **Step 3: Enable synchronous replication**

Enabling synchronous replication ensures that all data that is written to the source Database is also written to the replica:

```sql  theme={null}
psql "$SOURCE_URL" << EOF
  ALTER SYSTEM SET synchronous_standby_names=aptible_subscription;
  SELECT pg_reload_conf();
EOF
```

> ❗️ Performance Alert: synchronous replication ensures that transactions are committed on both the primary and replica databases simultaneously, which can introduce noticable latency on commit times, especially on databases with higher relative volumes of changes. In this case, you may want to ensure that you wait to enable synchronous replication until you are close to performing the cutover in order to minimize the impact of slower commits on the primary database.

#### **Step 4: Scale Services down**

This step is optional. Scaling all [Services](/core-concepts/apps/deploying-apps/services) that use the source Database to zero containers ensures that they can’t write to the Database during the cutover. This will result in some downtime in exchange for preventing replication conflicts that can result from Services writing to both the source and replica Databases at the same time.

It's usually easiest to prepare a script that scales all Services down and another that scales them back up to their current values once the upgrade has been completed. Current container counts can be found in the [Aptible Dashboard](https://dashboard.aptible.com/) or by running [`APTIBLE_OUTPUT_FORMAT=json aptible apps`](/reference/aptible-cli/cli-commands/cli-apps).

Example scale command:

```
aptible apps:scale --app my-app cmd --container-count 0
```

#### **Step 5: Update all Apps to use the replica**

Assuming [Database's Credentials](/core-concepts/managed-databases/connecting-databases/database-credentials) are provided to Apps via the [App's Configuration](/core-concepts/apps/deploying-apps/configuration), this can be done relatively easily using the [`aptible config:set`](/reference/aptible-cli/cli-commands/cli-config-set) command. This step is also usually easiest to complete by preparing a script that updates all relevant Apps.

Example config command:

```sql  theme={null}
aptible config:set --app my-app DB_URL='postgresql://user:passw0rd@db-stack-1234.aptible.in:5432/db'
```

#### **Step 6: Sync sequences**

Ensure that the sequences on the replica are up-to-date with the source Database:

```sql  theme={null}
psql "$SOURCE_URL" --tuples-only --no-align --command \
  'SELECT datname FROM pg_database WHERE datistemplate IS FALSE' |

while IFS= read -r db; do
  psql "$SOURCE_URL" << EOF
    \connect "$db"
    SELECT pglogical.synchronize_sequence( seqoid ) FROM pglogical.sequence_state;
EOF
done
```

#### **Step 7: Stop replication**

Now that all the Apps have been updated to use the new replica, there is no need to replicate changes from the source Database.

Drop the `pglogical` subscriptions, nodes, and extensions from the replica:

```sql  theme={null}
psql "$REPLICA_URL" --tuples-only --no-align --command \
  'SELECT datname FROM pg_database WHERE datistemplate IS FALSE' |

while IFS= read -r db; do
  psql "$REPLICA_URL" << EOF
    \connect "$db"
    SELECT pglogical.drop_subscription('aptible_subscription');
    SELECT pglogical.drop_node('aptible_subscriber');
    DROP EXTENSION pglogical;
EOF
done
```

Clear `synchronous_standby_names` on the source Database:

```sql  theme={null}
psql "$SOURCE_URL" << EOF
  ALTER SYSTEM RESET synchronous_standby_names;
  SELECT pg_reload_conf();
EOF
```

#### **Step 8: Scale Services up**

Scale any Services that were scaled down to zero Containers back to their original number of Containers. If a script was created to do this, now is the time to run it.

Example scale command:

```sql  theme={null}
aptible apps:scale --app my-app cmd --container-count 2
```

Once all of the Services have come back up, the upgrade is complete!

## Cleanup

#### Step 1: Vacuum and Analyze

Vacuuming the target Database after upgrading reclaims space occupied by dead tuples and analyzing the tables collects information on the table's contents in order to improve query performance.

```sql  theme={null}
psql "$REPLICA_URL" --tuples-only --no-align --command \
  'SELECT datname FROM pg_database WHERE datistemplate IS FALSE' |

while IFS= read -r db; do
  psql "$REPLICA_URL" << EOF
    \connect "$db"

    VACUUM ANALYZE;
EOF
done
```

#### Step 2: Source Database

> 🚧 Caution: If you're cleaning up from a failed replication attempt and you're not sure if `pglogical` was being used previously, check with other members of your organization before performing cleanup as this may break existing `pglogical` subscribers.

Drop the `pglogical` replication slots (if they exist), nodes, and extensions:

```sql  theme={null}
psql "$SOURCE_URL" --tuples-only --no-align --command \
  'SELECT datname FROM pg_database WHERE datistemplate IS FALSE' |

while IFS= read -r db; do
  psql "$SOURCE_URL" << EOF
    \connect "$db"

    SELECT pg_drop_replication_slot((
      SELECT pglogical.pglogical_gen_slot_name(
        '$db',
        'aptible_publisher_$REPLICA_ID',
        'aptible_subscription'
      )
    ));

    \set ON_ERROR_STOP 1

    SELECT pglogical.drop_node('aptible_publisher_$REPLICA_ID');
    DROP EXTENSION pglogical;
EOF
done
```

Note that you'll need to substitute `REPLICA_ID` into the script for it to properly run! If you don't remember what it is, you can always also run:

```sql  theme={null}
SELECT pglogical.pglogical_node_info();
```

from a `psql` client to discover what the pglogical publisher is named.

If the script above raises errors about replication slots being active, then replication was not stopped properly. Ensure that the instructions in the [Stop replication](/how-to-guides/database-guides/upgrade-postgresql#stop-replication) section have been completed.

#### Step 3: Reset max\_worker\_processes

[`aptible db:replicate --logical`](/reference/aptible-cli/cli-commands/cli-db-replicate) may have increased the `max_worker_processes` on the replica to ensure that it has enough to support replication. Now that replication has been terminated, the setting can be set back to the default by running the following command:

```sql  theme={null}
psql "$REPLICA_URL" --command "ALTER SYSTEM RESET max_worker_processes;"
```

See [How Logical Replication Works](/reference/aptible-cli/cli-commands/cli-db-replicate#how-logical-replication-works) in the command documentation for more details.

#### **Step 4: Unlink the Databases**

Aptible maintains a link between replicas and their source Database to ensure the source Database cannot be deleted before the replica. To deprovision the source Database after switching to the replica, users with the appropriate [roles and permissions](/core-concepts/security-compliance/access-permissions#full-permission-type-matrix) can unlink the replica from the source database. Navigate to the replica's settings page to complete the unlinking process.

#### **Step 5: Deprovision**

Once the original Database is no longer necessary, it should be deprovisioned, or it will continue to incur costs. Note that this will delete all automated Backups. If you'd like to retain the Backups, contact [Aptible Support](/how-to-guides/troubleshooting/aptible-support) to update them.

```sql  theme={null}
aptible db:deprovision "$SOURCE_HANDLE" --environment "$SOURCE_ENVIRONMENT"
```
