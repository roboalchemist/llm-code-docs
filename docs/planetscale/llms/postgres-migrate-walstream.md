# Source: https://planetscale.com/docs/postgres/imports/postgres-migrate-walstream.md

# Postgres Imports - WAL Streaming

[Write-Ahead Logging (WAL)](https://www.postgresql.org/docs/current/wal-intro.html) streaming provides a near-zero downtime migration method by continuously replicating changes from your source PostgreSQL database to PlanetScale Postgres using [logical replication](https://www.postgresql.org/docs/current/logical-replication.html).

## Overview

This migration method involves:

<Steps>
  <Step>
    Setting up logical replication from your source database
  </Step>

  <Step>
    Creating an initial data snapshot
  </Step>

  <Step>
    Continuously streaming WAL changes to keep databases synchronized
  </Step>

  <Step>
    Performing a quick cutover when ready
  </Step>
</Steps>

<Warning>
  This method requires administrative access to your source PostgreSQL database to configure replication settings.
</Warning>

## Prerequisites

Before starting the migration:

* PostgreSQL 10+ on the source database (logical replication support)
* Administrative access to source database configuration
* Network connectivity between source and PlanetScale Postgres
* Connection details for your PlanetScale Postgres database from the console
* Ensure the disk on your PlanetScale database has at least 150% of the capacity of your source database.
  If you are migrating to a PlanetScale database backed by network-attached storage, you can [resize](https://planetscale.com/docs/postgres/cluster-configuration/cluster-storage) your disk manually by setting the "Minimum disk size."
  If you are using Metal, you will need to select a size when first creating your database.
  For example, if your source database is 330GB, you should have at least 500GB of storage available on PlanetScale.
* Understanding of your application's write patterns for cutover planning

## Step 1: Configure Source Database

### Enable logical replication on source database:

Edit your PostgreSQL configuration (`postgresql.conf`):

```ini  theme={null}
# Enable logical replication
wal_level = logical

# Set maximum replication slots
max_replication_slots = 10

# Set maximum WAL senders
max_wal_senders = 10

# Enable logical replication workers
max_logical_replication_workers = 10
```

### Configure authentication (`pg_hba.conf`):

Add an entry to allow replication connections:

```ini  theme={null}
# Allow replication connections
host replication replication_user source_ip/32 md5
```

### Restart PostgreSQL service:

```bash  theme={null}
# On systemd systems
sudo systemctl restart postgresql

# On older systems
sudo service postgresql restart
```

## Step 2: Create Replication User

Connect to your source database and create a replication user:

```sql  theme={null}
-- Create replication user
CREATE USER replication_user WITH REPLICATION LOGIN;

-- Grant necessary permissions
GRANT CONNECT ON DATABASE your_database TO replication_user;
GRANT USAGE ON SCHEMA public TO replication_user;
GRANT SELECT ON ALL TABLES IN SCHEMA public TO replication_user;

-- Grant permissions for future tables
ALTER DEFAULT PRIVILEGES IN SCHEMA public
    GRANT SELECT ON TABLES TO replication_user;
```

## Step 3: Create Publication on Source

Create a publication for the tables you want to replicate:

```sql  theme={null}
-- Create publication for all tables
CREATE PUBLICATION planetscale_migration FOR ALL TABLES;

-- Or create publication for specific tables
CREATE PUBLICATION planetscale_migration FOR TABLE
    table1, table2, table3;

-- Verify publication
SELECT * FROM pg_publication;
```

## Step 4: Get PlanetScale Connection Details

From your PlanetScale console:

<Steps>
  <Step>
    Navigate to your PlanetScale Postgres database
  </Step>

  <Step>
    Go to the "Connect" section
  </Step>

  <Step>
    Copy the connection details including:

    * Host
    * Port
    * Database name
    * Username
    * Password
  </Step>
</Steps>

## Step 5: Create Initial Schema on PlanetScale

Export and import the schema structure:

```bash  theme={null}
# Export schema from source
pg_dump -h source-host \
        -p source-port \
        -U source-username \
        -d source-database \
        --schema-only \
        --no-owner \
        --no-privileges \
        -f schema.sql

# Import schema to PlanetScale
psql -h planetscale-host \
     -p planetscale-port \
     -U planetscale-username \
     -d planetscale-database \
     -f schema.sql
```

## Step 6: Create Initial Data Copy

Create an initial data snapshot:

```bash  theme={null}
# Export data from source
pg_dump -h source-host \
        -p source-port \
        -U source-username \
        -d source-database \
        --data-only \
        --no-owner \
        --no-privileges \
        -f data.sql

# Import data to PlanetScale
psql -h planetscale-host \
     -p planetscale-port \
     -U planetscale-username \
     -d planetscale-database \
     -f data.sql
```

## Step 7: Set Up Logical Replication

Connect to PlanetScale Postgres and create subscription:

```sql  theme={null}
-- Create subscription to source database
CREATE SUBSCRIPTION planetscale_subscription
    CONNECTION 'host=source-host port=source-port
                dbname=source-database user=replication_user
                password=replication-password'
    PUBLICATION planetscale_migration;

-- Check subscription status
SELECT * FROM pg_subscription;

-- Monitor replication status
SELECT * FROM pg_stat_subscription;
```

## Step 8: Monitor Replication

### Check replication lag:

```sql  theme={null}
-- On source database
SELECT * FROM pg_replication_slots;

-- On PlanetScale database
SELECT
    subname,
    received_lsn,
    latest_end_lsn,
    latest_end_time
FROM pg_stat_subscription;
```

### Monitor for conflicts:

```sql  theme={null}
-- Check for subscription errors
SELECT * FROM pg_stat_subscription
WHERE last_msg_failure_time IS NOT NULL;
```

## Step 9: Prepare for Cutover

### Verify data consistency:

```sql  theme={null}
-- Compare row counts between source and target
-- Run on both databases
SELECT
    schemaname,
    tablename,
    n_tup_ins as estimated_rows
FROM pg_stat_user_tables
ORDER BY schemaname, tablename;
```

### Check replication lag:

Ensure replication lag is minimal (ideally under 1 second) before cutover.

## Step 10: Perform Cutover

When ready to switch to PlanetScale Postgres:

<Steps>
  <Step>
    **Stop application writes** to the source database
  </Step>

  <Step>
    **Wait for replication to catch up** (monitor lag)
  </Step>

  <Step>
    **Update application connection strings** to point to PlanetScale
  </Step>

  <Step>
    **Start application** with new connection
  </Step>

  <Step>
    **Monitor** for any issues
  </Step>
</Steps>

### Verify cutover success:

```sql  theme={null}
-- Check that latest data is present
SELECT count(*), max(updated_at) FROM your_main_table;
```

## Step 11: Cleanup (After Successful Cutover)

### Drop subscription on PlanetScale:

```sql  theme={null}
DROP SUBSCRIPTION planetscale_subscription;
```

### Drop publication on source:

```sql  theme={null}
DROP PUBLICATION planetscale_migration;
```

## Troubleshooting

### Common Issues:

**Replication slot conflicts:**

```sql  theme={null}
-- Check existing slots
SELECT * FROM pg_replication_slots;

-- Drop unused slots
SELECT pg_drop_replication_slot('slot_name');
```

**Permission errors:**

* Verify replication user has correct permissions
* Check pg\_hba.conf configuration
* Ensure network connectivity

**Large transaction delays:**

* Monitor for long-running transactions on source
* Consider breaking large operations into smaller batches

**Subscription conflicts:**

```sql  theme={null}
-- Check subscription worker status
SELECT * FROM pg_stat_subscription;

-- Restart subscription if needed
ALTER SUBSCRIPTION planetscale_subscription DISABLE;
ALTER SUBSCRIPTION planetscale_subscription ENABLE;
```

## Performance Considerations

1. **Network bandwidth**: Ensure sufficient bandwidth for initial sync and ongoing replication
2. **Disk I/O**: Monitor disk usage on both source and target during replication
3. **Replication lag**: Keep lag minimal by optimizing source database performance
4. **Conflict resolution**: Understand how PostgreSQL handles replication conflicts

## Schema Considerations

Before migration, review:

<Columns cols={2}>
  <Card title="PostgreSQL version compatibility" icon="database" horizontal href="/docs/vitess/imports/postgres#postgresql-version-compatibility" />

  <Card title="Extension support limitations" icon="battery-exclamation" horizontal href="/docs/vitess/imports/postgres#extension-support" />

  <Card title="Third-party enhancement restrictions" icon="circle-xmark" horizontal href="/docs/vitess/imports/postgres#third-party-enhancements-and-tools" />
</Columns>

## Next Steps

After successful migration:

<Steps>
  <Step>
    Monitor replication performance and lag
  </Step>

  <Step>
    Test application functionality thoroughly
  </Step>

  <Step>
    Set up monitoring and alerting for the new database
  </Step>

  <Step>
    Plan for ongoing maintenance and optimization
  </Step>
</Steps>

For simpler migrations or if you don't have administrative access to your source database, consider the [pg\_dump/restore method](./postgres-migrate-dumprestore). For more complex scenarios, explore [Amazon DMS](./postgres-migrate-dms).

If you encounter issues during migration, please [reach out to support](https://planetscale.com/contact?initial=support) for assistance.

## Need help?

Get help from [the PlanetScale Support team](https://support.planetscale.com/), or join our [GitHub discussion board](https://github.com/planetscale/discussion/discussions) to see how others are using PlanetScale.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://planetscale.com/llms.txt