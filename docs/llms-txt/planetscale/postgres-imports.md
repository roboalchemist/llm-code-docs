# Source: https://planetscale.com/docs/postgres/imports/postgres-imports.md

# Postgres Imports

> For customers looking to migrate their Postgres databases to PlanetScale Postgres, you have several options for how to make this the smoothest event for your business.

Use this guide if you are importing from platforms like Aurora Postgres, RDS Postgres, Neon, Supabase, and other Postgres instances.

<Note>
  If you have IP restrictions in place on our source database and need to grant a set of IP addresses access, see our [Import public IP addresses documentation](/docs/postgres/imports/import-ips).
</Note>

## Migration Options Overview

PlanetScale Postgres provides three primary migration approaches to suit different business requirements, database sizes, and downtime tolerances:

<Columns cols={2}>
  <Card title="Migrate using pgdump/restore" icon="recycle" horizontal href="/docs/postgres/imports/postgres-migrate-dumprestore" />

  <Card title="Migrate using logical replication" icon="laptop" horizontal href="/docs/postgres/imports/postgres-migrate-walstream" />

  <Card title="Migrate using Amazon DMS" icon="aws" horizontal href="/docs/postgres/imports/postgres-migrate-dms" />
</Columns>

You can also utilize our [migration scripts](https://github.com/planetscale/migration-scripts/tree/main/postgres-direct) directly if you prefer. These scripts can be used to migrate straight from any Postgres source that supports logical replication into PlanetScale Postgres.

### 1. pg\_dump and Restore

The [pg\_dump](https://www.postgresql.org/docs/current/app-pgdump.html) method is the simplest approach for migrating smaller PostgreSQL databases. This method involves creating a full backup of your source database using PostgreSQL's built-in `pg_dump` utility and then restoring it to your PlanetScale Postgres database.

**How it works:**

* Export your entire database schema and data using [`pg_dump`](https://www.postgresql.org/docs/current/app-pgdump.html)
* Transfer the dump file to PlanetScale Postgres
* Restore the database using [`pg_restore`](https://www.postgresql.org/docs/current/app-pgrestore.html) or [`psql`](https://www.postgresql.org/docs/current/app-psql.html)

This approach is straightforward and doesn't require additional infrastructure, making it ideal for databases that can tolerate some downtime during the migration process.

### 2. WAL Log Replication

[Write-Ahead Logging (WAL)](https://www.postgresql.org/docs/current/wal-intro.html) replication provides a near-zero downtime migration by continuously streaming transaction logs from your source PostgreSQL database to PlanetScale Postgres.

**How it works:**

* Set up [logical replication](https://www.postgresql.org/docs/current/logical-replication.html) between your source database and PlanetScale Postgres
* Stream [WAL logs](https://www.postgresql.org/docs/current/wal-intro.html) in real-time to keep the target database synchronized
* Perform a quick cutover when ready to switch to the new database

This method is ideal for production databases that require minimal downtime and need to maintain data consistency during the migration process.

### 3. Amazon Database Migration Service (DMS)

[Amazon Database Migration Service (DMS)](https://aws.amazon.com/dms/) provides a managed migration service that can handle complex database migrations with built-in monitoring, error handling, and data validation.

**How it works:**

* Configure [DMS replication instance](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_ReplicationInstance.html) and [endpoints](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Endpoints.html) for source and target databases
* Set up full load and [change data capture (CDC)](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Task.CDC.html) for ongoing replication
* Monitor the migration process through the [AWS console](https://console.aws.amazon.com/dms/)
* Perform cutover when the target database is fully synchronized

DMS is particularly useful for large, complex databases that require robust error handling, [data transformation](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.CustomizingTasks.TableMapping.SelectionTransformation.Transformations.html), and detailed migration monitoring.

## Migration Method Comparison

| Feature                             | pg\_dump & Restore                                                                 | WAL Log Replication                             | Amazon DMS                                                                                                                                                               |
| :---------------------------------- | :--------------------------------------------------------------------------------- | :---------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Best For**                        | Small to medium databases                                                          | Production databases requiring minimal downtime | Large, complex databases with transformation needs                                                                                                                       |
| **Downtime**                        | High (hours to days)                                                               | Minimal (minutes)                               | Minimal to none                                                                                                                                                          |
| **Setup Complexity**                | Low                                                                                | Medium                                          | High                                                                                                                                                                     |
| **Infrastructure Requirements**     | None (built-in tools)                                                              | Source DB configuration changes                 | AWS DMS resources                                                                                                                                                        |
| **Data Consistency**                | [Point-in-time snapshot](https://www.postgresql.org/docs/current/backup-dump.html) | Real-time sync                                  | Real-time sync with [validation](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Validating.html)                                                                  |
| **Cost**                            | Free (built-in tools)                                                              | Low (minimal resources)                         | Medium (AWS DMS charges)                                                                                                                                                 |
| **Database Size Limit**             | Limited by storage/time                                                            | No practical limit                              | No practical limit                                                                                                                                                       |
| **Schema Changes During Migration** | Not supported                                                                      | Limited support                                 | Full support                                                                                                                                                             |
| **Data Transformation**             | None                                                                               | Limited                                         | Extensive [transformation rules](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.CustomizingTasks.TableMapping.SelectionTransformation.Transformations.html) |
| **Error Handling**                  | Manual intervention required                                                       | Basic retry mechanisms                          | Automated error handling and recovery                                                                                                                                    |
| **Rollback Options**                | Manual restore from backup                                                         | Stop replication, switch back                   | Stop [DMS task](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.html), failback procedures                                                                   |

## Migration Considerations

Before migrating your PostgreSQL database to PlanetScale Postgres, there are several important factors to consider to ensure a smooth migration process.

### PostgreSQL Version Compatibility

PlanetScale Postgres supports [PostgreSQL 18](https://www.postgresql.org/docs/18/index.html) and [PostgreSQL 17](https://www.postgresql.org/docs/17/index.html). If your source database is running an older version of PostgreSQL, you should verify compatibility and consider upgrading your source database before migration, or plan for potential compatibility issues during the migration process.

**Version considerations:**

* **PostgreSQL 18**: Fully supported
* **PostgreSQL 17**: Fully supported
* **Earlier versions**: May require additional testing and validation
* **Version-specific features**: Newer features may not be available in older versions

For detailed information about PostgreSQL version differences, refer to the [PostgreSQL 18 release notes](https://www.postgresql.org/docs/18/release.html) and [PostgreSQL 17 release notes](https://www.postgresql.org/docs/17/release.html).

### Upgrading from PostgreSQL 17 to 18 on PlanetScale

We don't currently offer an automated in-place major version upgrade from PostgreSQL 17 to 18.

You can perform an online upgrade by migrating from your existing PlanetScale Postgres 17 database to a new PostgreSQL 18 database using our import guides:

* For near-zero downtime with logical replication: follow the [WAL replication guide](/docs/postgres/imports/postgres-migrate-walstream)
* For simpler/smaller databases: use [pg\_dump/restore](/docs/postgres/imports/postgres-migrate-dumprestore)
* If you prefer a managed migration service: use [Amazon DMS](/docs/postgres/imports/postgres-migrate-dms)

At a high level, the process is:

1. Create a new PostgreSQL 18 database (same region and similar configuration).
2. Use one of the import methods above to sync data from your PostgreSQL 17 database.
3. Validate data and application behavior, then update your application connection string to the new database.
4. Decommission the old PostgreSQL 17 database when you're ready.

### Extension Support

PlanetScale Postgres will have **limited extension support** at launch. Many PostgreSQL databases rely on extensions to provide additional functionality, and not all extensions will be available initially.

**Important notes about extensions:**

* Review your current database's installed extensions using `\dx` in psql or by querying `pg_extension`
* Identify which extensions are critical to your application's functionality
* Plan for alternative approaches if critical extensions are not supported
* Test your application thoroughly in a staging environment before migrating production data

Common extensions that may require attention:

* [PostGIS](https://postgis.net/) for geospatial data
* [pg\_stat\_statements](https://www.postgresql.org/docs/current/pgstatstatements.html) for query statistics
* [UUID extensions](https://www.postgresql.org/docs/current/uuid-ossp.html)
* [Full-text search extensions](https://www.postgresql.org/docs/current/textsearch.html)

### Third-Party Enhancements and Tools

PlanetScale Postgres does **not support third-party enhancements** to PostgreSQL's core capabilities at launch. This includes:

**Currently unsupported:**

* Custom background workers
* Third-party connection poolers (like [PgBouncer](https://www.pgbouncer.org/))
* External procedural languages beyond the standard ones
* Third-party monitoring tools that require database-level access
* Custom shared libraries or plugins

<Info>
  PlanetScale Postgres includes connection pooling by default.
</Info>

**Alternatives to consider:**

* Migrate custom functions to standard PostgreSQL syntax where possible
* Utilize Metrics, Insights, and 3rd party integrations for monitoring (LINKS HERE)

### Pre-Migration Checklist

Before starting your migration:

1. **Database Assessment**
   * Document your current PostgreSQL version
   * List all installed extensions and their usage
   * Identify any third-party tools or enhancements in use
   * Review custom functions and stored procedures

2. **Compatibility Testing**
   * Test your application against your target PostgreSQL version (18 or 17)
   * Validate that critical extensions are supported or have alternatives
   * Identify any custom code that may need modification

3. **Migration Planning**
   * Choose the appropriate migration method based on your requirements
   * Plan for testing in a staging environment
   * Prepare rollback procedures if needed
   * Schedule migration during low-traffic periods if possible

For the most up-to-date information on supported features and extensions, refer to the [PostgreSQL documentation](https://www.postgresql.org/docs/current/) and PlanetScale Postgres release notes.

# You got this!

Follow the migration guide that's right for you:

<Columns cols={2}>
  <Card title="Migrate using pgdump/restore" icon="recycle" horizontal href="/docs/postgres/imports/postgres-migrate-dumprestore" />

  <Card title="Migrate using WAL replication" icon="laptop" horizontal href="/docs/postgres/imports/postgres-migrate-walstream" />

  <Card title="Migrate using Amazon DMS" icon="aws" horizontal href="/docs/postgres/imports/postgres-migrate-dms" />
</Columns>

If you encounter issues while importing from a Postgres database, please [reach out to support](https://planetscale.com/contact?initial=support) for assistance.

## Need help?

Get help from [the PlanetScale Support team](https://support.planetscale.com/), or join our [GitHub discussion board](https://github.com/planetscale/discussion/discussions) to see how others are using PlanetScale.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://planetscale.com/llms.txt