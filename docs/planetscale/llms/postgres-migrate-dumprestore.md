# Source: https://planetscale.com/docs/postgres/imports/postgres-migrate-dumprestore.md

# Postgres Imports - PGDump and Restore

The [pg\_dump](https://www.postgresql.org/docs/current/app-pgdump.html) and restore method is the simplest approach for migrating PostgreSQL databases to PlanetScale Postgres. This method is ideal for smaller databases that can tolerate downtime during the migration process.

## Overview

This migration method involves:

1. Creating a full backup of your source database using `pg_dump`
2. Transferring the dump file to your local environment or staging area
3. Restoring the database to PlanetScale Postgres using `pg_restore` or `psql`

## Prerequisites

Before starting the migration:

* Ensure you have PostgreSQL client tools installed (`pg_dump`, `pg_restore`, `psql`)
* Have read access to your source PostgreSQL database
* Have connection details for your PlanetScale Postgres database from the console
* Ensure the disk on your PlanetScale database has at least 150% of the capacity of your source database.
  If you are migrating to a PlanetScale database backed by network-attached storage, you can [resize](https://planetscale.com/docs/postgres/cluster-configuration/cluster-storage) your disk manually by setting the "Minimum disk size."
  If you are using Metal, you will need to select a size when first creating your database.
  For example, if your source database is 330GB, you should have at least 500GB of storage available on PlanetScale.
* Verify sufficient storage space for the dump file
* Plan for application downtime during the migration

## Step 1: Create Database Dump

### For a complete database dump:

```bash  theme={null}
pg_dump -h source-host \
        -p source-port \
        -U source-username \
        -d source-database \
        --verbose \
        --no-owner \
        --no-privileges \
        -f database_dump.sql
```

### For a custom format dump (recommended for large databases):

```bash  theme={null}
pg_dump -h source-host \
        -p source-port \
        -U source-username \
        -d source-database \
        --verbose \
        --no-owner \
        --no-privileges \
        -Fc \
        -f database_dump.dump
```

### Command options explained:

* `--verbose`: Provides detailed output during the dump process
* `--no-owner`: Excludes ownership information from the dump
* `--no-privileges`: Excludes privilege information from the dump
* `-Fc`: Creates a custom format dump (binary, compressed)
* `-f`: Specifies the output file name

## Step 2: Get PlanetScale Connection Details

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

## Step 3: Restore to PlanetScale Postgres

### For SQL format dumps:

```bash  theme={null}
psql -h planetscale-host \
     -p planetscale-port \
     -U planetscale-username \
     -d planetscale-database \
     -f database_dump.sql
```

### For custom format dumps:

```bash  theme={null}
pg_restore -h planetscale-host \
           -p planetscale-port \
           -U planetscale-username \
           -d planetscale-database \
           --verbose \
           --no-owner \
           --no-privileges \
           database_dump.dump
```

### For parallel restoration (faster for large databases):

```bash  theme={null}
pg_restore -h planetscale-host \
           -p planetscale-port \
           -U planetscale-username \
           -d planetscale-database \
           --verbose \
           --no-owner \
           --no-privileges \
           --jobs=4 \
           database_dump.dump
```

## Step 4: Verify Migration

After the restore completes, verify your migration:

### Check table counts:

```sql  theme={null}
SELECT schemaname, tablename, n_tup_ins as row_count
FROM pg_stat_user_tables
ORDER BY schemaname, tablename;
```

### Verify data integrity:

```sql  theme={null}
-- Check a few sample records from key tables
SELECT count(*) FROM your_main_table;
SELECT * FROM your_main_table LIMIT 5;
```

### Check for errors in logs:

Review the output from the pg\_restore command for any errors or warnings.

## Troubleshooting

### Common Issues:

**Permission errors:**

* Ensure your PlanetScale user has appropriate permissions
* Check that connection details are correct

**Extension errors:**

* Some PostgreSQL extensions may not be available in PlanetScale Postgres
* Review the [extension compatibility guide](/docs/vitess/imports/postgres#extension-support)

**Large object errors:**

* If using large objects (BLOBs), add `--blobs` flag to pg\_dump

```bash  theme={null}
pg_dump --blobs -h source-host -U source-username -d source-database -f database_dump.sql
```

**Timeout errors:**

* For large databases, consider breaking the dump into smaller chunks
* Use custom format with parallel restoration

### Performance Tips:

1. **Use custom format**: Binary format with compression is more efficient
2. **Parallel jobs**: Use `--jobs` parameter for faster restoration
3. **Network considerations**: Ensure stable network connection for large transfers
4. **Disk space**: Monitor available disk space during dump creation

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
    Update your application connection strings to point to PlanetScale Postgres
  </Step>

  <Step>
    Test your application thoroughly in a staging environment
  </Step>

  <Step>
    Plan your production cutover
  </Step>

  <Step>
    Monitor performance and optimize as needed
  </Step>
</Steps>

For more advanced migration scenarios or larger databases, consider [WAL streaming](./postgres-migrate-walstream) or [Amazon DMS](./postgres-migrate-dms) methods.

If you encounter issues during migration, please [reach out to support](https://planetscale.com/contact?initial=support) for assistance.

## Need help?

Get help from [the PlanetScale Support team](https://support.planetscale.com/), or join our [GitHub discussion board](https://github.com/planetscale/discussion/discussions) to see how others are using PlanetScale.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://planetscale.com/llms.txt