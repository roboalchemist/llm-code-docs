# Source: https://planetscale.com/docs/vitess/imports/database-imports.md

# Database Imports

## Overview

PlanetScale provides an import tool in the dashboard that allows you to painlessly import an **existing internet-accessible MySQL or MariaDB database** into a PlanetScale database with *no downtime*.

<Note>
  You must be an [Organization Administrator](/docs/security/access-control#organization-administrator) to use this feature.
</Note>

Before you begin, it may be helpful to check out our [general MySQL compatibility guide](/docs/vitess/troubleshooting/mysql-compatibility).

## Import process overview

The import workflow gives you visibility into every step of your database migration. You'll see real-time progress, detailed logs, and replication metrics throughout. Here's what the process looks like:

1. **Create database** - Set up your PlanetScale database
2. **Connect to external database** - Add connection credentials and SSL/TLS settings
3. **Validate connection and schema** - We check connectivity, server configuration, and schema compatibility
4. **Select tables** - Pick which tables to import (all tables imported if foreign keys detected)
5. **Start workflow** - Kick off the import
6. **Monitor import** - Watch progress with real-time logs, per-table progress, and replication lag information
7. **Complete import** - Finalize and detach from your external database

<Note>
  **Note**

  It's recommended to avoid all schema changes / DDL (Data Definition Language) statements during an import on both your source database and the PlanetScale database. This includes `CREATE`, `DROP`, `ALTER`, `TRUNCATE`, etc.
</Note>

## Step 1: Create your PlanetScale database

<Steps>
  <Step>
    Head to your PlanetScale dashboard and click on "**New database**" > "**Import database**".

    <Frame>
      <img src="https://mintcdn.com/planetscale-cad1a68a/CkuVTAfsTSnAmv2e/docs/images/assets/docs/imports/import-workflows/import-database-dropdown.png?fit=max&auto=format&n=CkuVTAfsTSnAmv2e&q=85&s=dc2f02fdae66525265d68a569e5d4770" alt="Import database dropdown." data-og-width="1898" width="1898" data-og-height="666" height="666" data-path="docs/images/assets/docs/imports/import-workflows/import-database-dropdown.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/CkuVTAfsTSnAmv2e/docs/images/assets/docs/imports/import-workflows/import-database-dropdown.png?w=280&fit=max&auto=format&n=CkuVTAfsTSnAmv2e&q=85&s=0a45d2068d298febb277ec7c2bc407f9 280w, https://mintcdn.com/planetscale-cad1a68a/CkuVTAfsTSnAmv2e/docs/images/assets/docs/imports/import-workflows/import-database-dropdown.png?w=560&fit=max&auto=format&n=CkuVTAfsTSnAmv2e&q=85&s=3395254e30c5b0309543fcd51b124838 560w, https://mintcdn.com/planetscale-cad1a68a/CkuVTAfsTSnAmv2e/docs/images/assets/docs/imports/import-workflows/import-database-dropdown.png?w=840&fit=max&auto=format&n=CkuVTAfsTSnAmv2e&q=85&s=ad136fcd63be93eb8b840e431ce7ce7e 840w, https://mintcdn.com/planetscale-cad1a68a/CkuVTAfsTSnAmv2e/docs/images/assets/docs/imports/import-workflows/import-database-dropdown.png?w=1100&fit=max&auto=format&n=CkuVTAfsTSnAmv2e&q=85&s=184ddc9c79ad3576042ea6efef1e8918 1100w, https://mintcdn.com/planetscale-cad1a68a/CkuVTAfsTSnAmv2e/docs/images/assets/docs/imports/import-workflows/import-database-dropdown.png?w=1650&fit=max&auto=format&n=CkuVTAfsTSnAmv2e&q=85&s=c0fdbc9cebe1f9b222f7b37e6c6c389b 1650w, https://mintcdn.com/planetscale-cad1a68a/CkuVTAfsTSnAmv2e/docs/images/assets/docs/imports/import-workflows/import-database-dropdown.png?w=2500&fit=max&auto=format&n=CkuVTAfsTSnAmv2e&q=85&s=381259e00da6dc00ce074b48ae222cee 2500w" />
    </Frame>
  </Step>

  <Step>
    Give your imported database a name and [select a region](/docs/vitess/regions) from the dropdown.

    We recommend using the same name as the database you're importing from to avoid updating any database name references throughout your application code. If you'd prefer to use a different database name, make sure to update your app where applicable once you fully switch over to PlanetScale.
  </Step>

  <Step>
    Click "**Create database**" to proceed to the import workflow setup.
  </Step>
</Steps>

## Step 2: Connect to your external database

You'll be taken to the import workflow page where you can configure the connection to your external MySQL or MariaDB database.

### Connection settings

Fill in your connection info:

**Host name** - The address where your database is hosted.

**Port** - The port where your database is hosted. The default MySQL port is `3306`.

**Database name** - The exact database name you want to import.

**SSL verification mode** - Choose from these options:

* **Disabled** - No SSL encryption (not recommended for production)
* **Preferred** - Use SSL if available, otherwise connect without SSL
* **Required** - SSL is required, but certificate is not verified
* **Verify CA** - SSL is required and the certificate is verified against the CA
* **Verify Identity** - SSL is required and the certificate hostname is verified

If your database server has a valid SSL certificate, set this to `Required` or higher.
For more information about certificates from a Certificate Authority, check out our [Secure connections documentation](/docs/vitess/connecting/secure-connections#certificate-authorities).

**Username** - The username to connect with. This user needs proper permissions. See our [import tool user requirements guide](/docs/vitess/imports/import-tool-user-requirements) for the full list of required grants.

### Authentication method

Pick your authentication method:

**Authenticate with password:**
Provide the password for the username you entered.

**Authenticate with mTLS (mutual TLS):**

* **SSL client certificate** - Certificate to authenticate PlanetScale with your database server
* **SSL client key** - The private key for the client certificate

### Advanced settings (optional)

Click "**Show advanced settings**" for more options:

* **Import connections** - Maximum number of concurrent connections for the import (max 100)
* **Minimum TLS version** - Choose from TLS 1.0, 1.1, 1.2, or 1.3
* **SSL server name override** - Override the server name for SSL certificate verification
* **SSL CA certificate chain** - If your database server has a certificate with a non-trusted root CA, provide the full CA certificate chain here

<Note>
  **Note**

  You must have [binary logs](https://dev.mysql.com/doc/refman/8.0/en/binary-log.html) enabled on the database you're importing. See our [provider-specific migration guides](/docs/vitess/imports/database-imports#provider-specific-guides) for instructions on enabling binary logging.
</Note>

<Frame>
  <img src="https://mintcdn.com/planetscale-cad1a68a/4VhQ3O-86dqtVudH/docs/images/assets/docs/imports/import-workflows/external-database-connection-settings.png?fit=max&auto=format&n=4VhQ3O-86dqtVudH&q=85&s=c24607fa1f6dbd1ab7f6a049f26bdc20" alt="The connection form with SSL/TLS settings." data-og-width="2670" width="2670" data-og-height="3488" height="3488" data-path="docs/images/assets/docs/imports/import-workflows/external-database-connection-settings.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/4VhQ3O-86dqtVudH/docs/images/assets/docs/imports/import-workflows/external-database-connection-settings.png?w=280&fit=max&auto=format&n=4VhQ3O-86dqtVudH&q=85&s=da7681e3794b71233690bf73bf01222b 280w, https://mintcdn.com/planetscale-cad1a68a/4VhQ3O-86dqtVudH/docs/images/assets/docs/imports/import-workflows/external-database-connection-settings.png?w=560&fit=max&auto=format&n=4VhQ3O-86dqtVudH&q=85&s=23792d85ae1ba08829796fc940c5d81d 560w, https://mintcdn.com/planetscale-cad1a68a/4VhQ3O-86dqtVudH/docs/images/assets/docs/imports/import-workflows/external-database-connection-settings.png?w=840&fit=max&auto=format&n=4VhQ3O-86dqtVudH&q=85&s=2b17379a88e324eade2119555a11df52 840w, https://mintcdn.com/planetscale-cad1a68a/4VhQ3O-86dqtVudH/docs/images/assets/docs/imports/import-workflows/external-database-connection-settings.png?w=1100&fit=max&auto=format&n=4VhQ3O-86dqtVudH&q=85&s=9313a79fa523bf0f154303b4760acf47 1100w, https://mintcdn.com/planetscale-cad1a68a/4VhQ3O-86dqtVudH/docs/images/assets/docs/imports/import-workflows/external-database-connection-settings.png?w=1650&fit=max&auto=format&n=4VhQ3O-86dqtVudH&q=85&s=108f858da96f92161317b46f3c4ec6f9 1650w, https://mintcdn.com/planetscale-cad1a68a/4VhQ3O-86dqtVudH/docs/images/assets/docs/imports/import-workflows/external-database-connection-settings.png?w=2500&fit=max&auto=format&n=4VhQ3O-86dqtVudH&q=85&s=7bd663d1a05a2e94f5632e376498b214 2500w" />
</Frame>

## Step 3: Validate connection and schema

Once you've filled in your connection info, click "**Connect to database**". PlanetScale will run some checks on your external database.

### Connectivity check

We'll make sure we can connect to your database with the credentials and SSL/TLS settings you provided.

### Server configuration check

These server configuration values need to be set correctly for the import to work:

| Variable                       | Required Value | Documentation                                                                                                                  |
| :----------------------------- | :------------- | :----------------------------------------------------------------------------------------------------------------------------- |
| `gtid_mode`                    | `ON`           | [Documentation](https://dev.mysql.com/doc/refman/5.7/en/replication-options-gtids.html#sysvar_gtid_mode)                       |
| `binlog_format`                | `ROW`          | [Documentation](https://dev.mysql.com/doc/refman/5.7/en/replication-options-binary-log.html#sysvar_binlog_format)              |
| `binlog_row_image`             | `FULL`         | [Documentation](https://dev.mysql.com/doc/refman/8.0/en/replication-options-binary-log.html#sysvar_binlog_row_image)           |
| `expire_logs_days`\*           | `> 2`          | [Documentation](https://dev.mysql.com/doc/refman/8.0/en/replication-options-binary-log.html#sysvar_expire_logs_days)           |
| `binlog_expire_logs_seconds`\* | `> 172800`     | [Documentation](https://dev.mysql.com/doc/refman/8.0/en/replication-options-binary-log.html#sysvar_binlog_expire_logs_seconds) |

**\*** Either `expire_logs_days` or `binlog_expire_logs_seconds` needs to be set. If both are set, `binlog_expire_logs_seconds` takes precedence.

### Schema compatibility check

We'll look for any compatibility issues with your schema:

* **Missing unique key** - All tables must have a unique, not-null key. See our [Changing unique keys documentation](/docs/vitess/schema-changes/onlineddl-change-unique-keys) for more info.
* **Invalid charset** - We support `utf8`, `utf8mb4`, `utf8mb3`, `latin1`, and `ascii`. Tables with other charsets will be flagged.
* **Table names with special characters** - Tables with characters outside the standard ASCII set aren't supported.
* **Views** - Views are detected but won't be imported. You can create them manually after the import finishes.
* **Unsupported storage engines** - Only `InnoDB` is supported.
* **Foreign key constraints** - Detected and flagged for special handling (see below).

### Handling validation errors

If validation fails, you'll see error messages with links to troubleshooting docs. You have two options:

1. **Fix the issues** - Go back to your external database, fix the configuration or schema issues, and try connecting again. [Contact support](https://planetscale.com/contact?initial=support) if you encounter trouble addressing the incompatibilities.
2. **Skip and continue** - For certain failures, you can proceed anyway. Not recommended since this may cause the import to fail later.

<Warning>
  **Warning**

  If you choose to skip validation errors and proceed, all tables will be imported automatically (you won't be able to select specific tables). This may result in unexpected behavior or import failures.
</Warning>

## Step 4: Foreign key constraints

If your database uses foreign key constraints, we'll detect them during validation and automatically enable foreign key support.

### Important things to know

When importing with foreign keys:

* **All tables will be imported** - You can't select a subset of tables when foreign keys are present. This keeps referential integrity intact.
* **Use a replica if possible** - The foreign key import holds a long-running transaction on the source database, which can increase load. We recommend connecting to a replica instead of your primary.
* **Import retries** - If your import fails, it starts over from the beginning. Unlike regular imports, we can't resume from where we left off.

For more information about foreign key support and limitations, see our [foreign key constraints documentation](/docs/vitess/foreign-key-constraints).

## Step 5: Select tables to import

After validation passes, you'll see a workflow form with your source database on the left (with provider logo and table list) and PlanetScale on the right (with target keyspace and shard count). In Vitess a [keyspace](/docs/vitess/sharding/keyspaces) is the equivalent of a single, logical MySQL databases.

### Table selection

**If foreign keys were detected:**

* All tables are automatically selected
* You can't deselect individual tables
* You'll see: "All tables will be replicated due to foreign key constraints usage"

**If no foreign keys:**

* Select all tables or pick specific ones
* You can start with a subset of tables for testing if you want

### Workflow validation

Before creating the workflow, click "**Validate**" to run pre-migration checks:

* Safe migrations is enabled
* [VSchema](/docs/vitess/sharding/vschema) is valid
* Tables will be created automatically in the target keyspace (PlanetScale database)
* Enough storage is available

Once these checks pass, the "**Create workflow**" button will light up.

<Frame>
  <img src="https://mintcdn.com/planetscale-cad1a68a/4VhQ3O-86dqtVudH/docs/images/assets/docs/imports/import-workflows/validate-import-workflow.png?fit=max&auto=format&n=4VhQ3O-86dqtVudH&q=85&s=4d330febc731c349473ef66a2cfb741a" alt="The validation results showing checks passed and table list." data-og-width="2670" width="2670" data-og-height="2950" height="2950" data-path="docs/images/assets/docs/imports/import-workflows/validate-import-workflow.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/4VhQ3O-86dqtVudH/docs/images/assets/docs/imports/import-workflows/validate-import-workflow.png?w=280&fit=max&auto=format&n=4VhQ3O-86dqtVudH&q=85&s=7b7e4b93f023ff231dc5a5b7ab351346 280w, https://mintcdn.com/planetscale-cad1a68a/4VhQ3O-86dqtVudH/docs/images/assets/docs/imports/import-workflows/validate-import-workflow.png?w=560&fit=max&auto=format&n=4VhQ3O-86dqtVudH&q=85&s=eeb62fa716d33204058df9de906421d5 560w, https://mintcdn.com/planetscale-cad1a68a/4VhQ3O-86dqtVudH/docs/images/assets/docs/imports/import-workflows/validate-import-workflow.png?w=840&fit=max&auto=format&n=4VhQ3O-86dqtVudH&q=85&s=987b14e380151c0bfaebb6fb07df8477 840w, https://mintcdn.com/planetscale-cad1a68a/4VhQ3O-86dqtVudH/docs/images/assets/docs/imports/import-workflows/validate-import-workflow.png?w=1100&fit=max&auto=format&n=4VhQ3O-86dqtVudH&q=85&s=70a50330bcd3e014009dc990dc2556f3 1100w, https://mintcdn.com/planetscale-cad1a68a/4VhQ3O-86dqtVudH/docs/images/assets/docs/imports/import-workflows/validate-import-workflow.png?w=1650&fit=max&auto=format&n=4VhQ3O-86dqtVudH&q=85&s=55bf42b4230bdf68049ff5fafbe5ca08 1650w, https://mintcdn.com/planetscale-cad1a68a/4VhQ3O-86dqtVudH/docs/images/assets/docs/imports/import-workflows/validate-import-workflow.png?w=2500&fit=max&auto=format&n=4VhQ3O-86dqtVudH&q=85&s=3802f42b8658eb23a9292cc3a30285ab 2500w" />
</Frame>

### Advanced options

Click "**Advanced options**" to see additional settings that can optimize your import:

**Defer secondary index creation**

Checked by default. Creates secondary indexes (non-primary indexes) after copying data instead of during the initial copy.

* Why this helps: Maintaining many indexes while inserting data is slow. By deferring index creation until after all data is copied, your import can be significantly faster (often 2-3x faster for tables with multiple indexes).

* When it's disabled: Import will run slower. Automatically disabled for imports with foreign keys, since foreign key constraints require indexes to exist during the copy phase.

**DDL handling**

Controls what happens if schema changes (like `ALTER TABLE`, `ADD INDEX`, etc.) occur on your external database while the import is running.

* **STOP** (default, recommended) - The workflow stops immediately when schema changes are detected. You'll need to manually restart the workflow after reviewing the changes. This is the safest option because it lets you verify the schema changes won't cause issues before continuing.

* **IGNORE** - Schema changes are skipped and won't be applied to your PlanetScale database. Your import continues without interruption, but your schemas will diverge. Only use this if you're confident you don't need these changes or plan to apply them manually to your PlanetScale database later.

* **EXEC** - Schema changes are automatically applied to your PlanetScale database while the import continues running. If applying a schema change fails (for example, if it's not compatible with Vitess), the workflow stops and you'll need to restart it. Use this if you need schema changes to sync automatically but want safety checks.

* **EXEC\_IGNORE** - Attempts to apply schema changes but keeps running even if they fail.

<Warning>
  `EXEC_IGNORE` can lead to schema mismatches between your external database and PlanetScale database, potentially causing data inconsistencies or unexpected behavior. Only use this if you understand the risks and have a plan to handle failures.
</Warning>

<Note>
  **Important**

  Schema changes during an active import can cause problems. This setting is a safety mechanism for unexpected changes, not a way to intentionally modify schemas mid-import. If possible, avoid making schema changes until the import completes.
</Note>

**Global keyspace**

Not applicable for external database imports. This setting is only used when moving tables between keyspaces within PlanetScale.
When moving tables with `AUTO_INCREMENT` columns from an unsharded to a sharded keyspace, Vitess needs a place to store "sequence tables" that coordinate ID generation across shards. This setting specifies which unsharded keyspace should hold those sequence tables.
You can ignore this setting for external database imports.

## Step 6: Start the import workflow

After validation passes. click "**Create workflow**" to start the import process. You'll be redirected to the workflow monitoring page where you can track your import in real-time.

## Step 7: Monitor your import

The monitoring page shows you real-time progress of your import.

### Connection status

At the top, you'll see:

* A live connection indicator (green pulsing dot when connected)
* Your external database name and hostname
* Workflow info (name, who started it, when)

### Visual replication flow

The main view shows data flowing from your external database to PlanetScale:

**Source keyspace (left):**

* List of tables being imported
* Progress donuts for each table during the copy phase (0-100%)
* Row counts per table

**Replication arrow (center):**

* Animated arrow showing data flow direction
* Current phase ("Copying data" or "Replicating data")
* Replication lag graph with current lag in seconds

**Target keyspace (right):**

* Your PlanetScale shards (only one shard in most cases)
* Traffic serving status

<Frame>
  <img src="https://mintcdn.com/planetscale-cad1a68a/CkuVTAfsTSnAmv2e/docs/images/assets/docs/imports/import-workflows/copying-phase.png?fit=max&auto=format&n=CkuVTAfsTSnAmv2e&q=85&s=d6ca23c52a73a8ea5c8d83ddd2e2d3aa" alt="The visual replication flow with progress indicators." data-og-width="2670" width="2670" data-og-height="2948" height="2948" data-path="docs/images/assets/docs/imports/import-workflows/copying-phase.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/CkuVTAfsTSnAmv2e/docs/images/assets/docs/imports/import-workflows/copying-phase.png?w=280&fit=max&auto=format&n=CkuVTAfsTSnAmv2e&q=85&s=636d700ae4a68753187e4d0fe24f1913 280w, https://mintcdn.com/planetscale-cad1a68a/CkuVTAfsTSnAmv2e/docs/images/assets/docs/imports/import-workflows/copying-phase.png?w=560&fit=max&auto=format&n=CkuVTAfsTSnAmv2e&q=85&s=930a3bde595bcec0b8158698ba3ce835 560w, https://mintcdn.com/planetscale-cad1a68a/CkuVTAfsTSnAmv2e/docs/images/assets/docs/imports/import-workflows/copying-phase.png?w=840&fit=max&auto=format&n=CkuVTAfsTSnAmv2e&q=85&s=195d4ed670d3b6edd2b882c3ca0c4117 840w, https://mintcdn.com/planetscale-cad1a68a/CkuVTAfsTSnAmv2e/docs/images/assets/docs/imports/import-workflows/copying-phase.png?w=1100&fit=max&auto=format&n=CkuVTAfsTSnAmv2e&q=85&s=8eb2a46f4405344406a0746fbb4d397d 1100w, https://mintcdn.com/planetscale-cad1a68a/CkuVTAfsTSnAmv2e/docs/images/assets/docs/imports/import-workflows/copying-phase.png?w=1650&fit=max&auto=format&n=CkuVTAfsTSnAmv2e&q=85&s=6c9369b506093a81dd5da04c1b46eb69 1650w, https://mintcdn.com/planetscale-cad1a68a/CkuVTAfsTSnAmv2e/docs/images/assets/docs/imports/import-workflows/copying-phase.png?w=2500&fit=max&auto=format&n=CkuVTAfsTSnAmv2e&q=85&s=d3a48b52294441091ef509c617065a54 2500w" />
</Frame>

### Workflow phases

Your import will go through these states:

1. **Pending** - Workflow created, not started yet
2. **Copying** - Copying initial data (you'll see per-table progress here)
3. **Running** - Replicating changes to keep databases in sync
4. **Verifying data** - Optional data verification
5. **Verified data** - Verification complete
6. **Switching replicas** - Moving replica traffic to PlanetScale
7. **Switched replicas** - Replica traffic now on PlanetScale
8. **Switching primaries** - Moving primary traffic to PlanetScale
9. **Switched primaries** - Primary traffic now on PlanetScale
10. **Completed** - Import done
11. **Error** - Something went wrong, check error messages or logs

**You can now connect your application to PlanetScale**

Once the workflow enters the **Running** (replication) phase, bidirectional replication is active. This means you can safely connect your application to PlanetScale for testing while your external database remains the authoritative source. Any writes to either database will be replicated to the other, allowing you to validate your application's behavior against PlanetScale without risk.

This is the ideal time to test your application end-to-end before switching traffic.

### Adding a replica host name (optional)

If your external database has read replicas, you can route read traffic to them instead of your primary database. This helps reduce load on your primary during the import.

**How this works:**

If your application is configured to send read traffic to replicas, you can continue this pattern while testing PlanetScale. Adding a replica hostname allows PlanetScale to proxy traffic to your external replicas during the import. This is useful when you want to test PlanetScale with read traffic going to your replicas while writes continue to your primary.

<Note>
  **Important**

  PlanetScale doesn't automatically detect or route read-only transactions. You control which queries go to replicas through your application's database connection configuration. PlanetScale simply acts as a proxy, forwarding the traffic you send to replica connections through to your external replica databases.
</Note>

On the workflow monitoring page, under the connection status:

<Steps>
  <Step>
    Click "**Add a replica host name**" below your primary connection info
  </Step>

  <Step>
    Enter the hostname of your read replica (e.g., `replica.myserver.example.com`)
  </Step>

  <Step>
    Click "**Add**" to save
  </Step>
</Steps>

Once added, you'll see the replica connection listed below your primary. You can edit or delete it anytime during the import.

**Why use a replica:**

* Reduces load on your primary database during the copy phase
* Especially useful for large imports or high-traffic databases
* The replica must have the same data as your primary (replication lag should be minimal)

<Frame>
  <img src="https://mintlify.s3.us-west-1.amazonaws.com/planetscale-cad1a68a/docs/images/assets/docs/imports/import-workflows/add-replica-hostname.png" alt="Connection status add replica hostname." />
</Frame>

### Verify data (optional)

Once the initial copy completes and replication catches up, you can optionally verify that your data matches between the external database and PlanetScale.

Click "**Verify data**" on the workflow monitoring page to run a comparison. This checks that the copied data is identical between your external database and PlanetScale, giving you confidence before switching traffic.

### Switching traffic

Once you've verified your data, you can control how traffic is routed between your external database and PlanetScale:

1. **Switch replica traffic** - Serve read queries from PlanetScale while writes still go to your external database. This is an optional intermediate step that lets you test read traffic separately.
2. **Switch primary traffic** - Serve both reads and writes from PlanetScale. This switches all traffic at once, so you don't need to switch replica traffic first.
3. **Complete** - Finalize the migration

<Note>
  **Note**

  You can skip directly to switching primary traffic if you prefer. Switching primary traffic handles both reads and writes simultaneously, so switching replica traffic first is optional.
</Note>

<Warning>
  **Critical: Update connection strings before switching primary traffic**

  You must update your application's connection string to point to PlanetScale **before** switching primary traffic. If you switch primary traffic while your application is still connected to your external database, you will create a split-brain scenario where:

  * PlanetScale believes it is serving all traffic (reads and writes)
  * Your application continues writing to the external database
  * The two databases diverge, causing data inconsistency and potential data loss

  Always verify your application is connected to PlanetScale before proceeding with the primary traffic switch.
</Warning>

<Frame>
  <img src="https://mintcdn.com/planetscale-cad1a68a/CkuVTAfsTSnAmv2e/docs/images/assets/docs/imports/import-workflows/switch-traffic-dropdown.png?fit=max&auto=format&n=CkuVTAfsTSnAmv2e&q=85&s=4acd8f91a560c2534e6ba9045e321fa9" alt="Switch replica and primary traffice." data-og-width="1978" width="1978" data-og-height="902" height="902" data-path="docs/images/assets/docs/imports/import-workflows/switch-traffic-dropdown.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/CkuVTAfsTSnAmv2e/docs/images/assets/docs/imports/import-workflows/switch-traffic-dropdown.png?w=280&fit=max&auto=format&n=CkuVTAfsTSnAmv2e&q=85&s=0983f6e91c7d8f768df6c89e579843ba 280w, https://mintcdn.com/planetscale-cad1a68a/CkuVTAfsTSnAmv2e/docs/images/assets/docs/imports/import-workflows/switch-traffic-dropdown.png?w=560&fit=max&auto=format&n=CkuVTAfsTSnAmv2e&q=85&s=72dbead6c02d184f997e46b214afa7bb 560w, https://mintcdn.com/planetscale-cad1a68a/CkuVTAfsTSnAmv2e/docs/images/assets/docs/imports/import-workflows/switch-traffic-dropdown.png?w=840&fit=max&auto=format&n=CkuVTAfsTSnAmv2e&q=85&s=0de24d207ff3c64a861eeb5d0c5756f8 840w, https://mintcdn.com/planetscale-cad1a68a/CkuVTAfsTSnAmv2e/docs/images/assets/docs/imports/import-workflows/switch-traffic-dropdown.png?w=1100&fit=max&auto=format&n=CkuVTAfsTSnAmv2e&q=85&s=aab5a541cb9d973b7e83dea353661e0c 1100w, https://mintcdn.com/planetscale-cad1a68a/CkuVTAfsTSnAmv2e/docs/images/assets/docs/imports/import-workflows/switch-traffic-dropdown.png?w=1650&fit=max&auto=format&n=CkuVTAfsTSnAmv2e&q=85&s=c873dbbd90f99c3c22aa3c5312513f0a 1650w, https://mintcdn.com/planetscale-cad1a68a/CkuVTAfsTSnAmv2e/docs/images/assets/docs/imports/import-workflows/switch-traffic-dropdown.png?w=2500&fit=max&auto=format&n=CkuVTAfsTSnAmv2e&q=85&s=a739def00db91b1205f2de37e0574584 2500w" />
</Frame>

### Monitoring replication lag

The lag graph shows how far behind PlanetScale is from your external database. During the initial copy, lag will be high. Once the copy finishes and replication catches up, lag should drop.

<Frame>
  <img src="https://mintcdn.com/planetscale-cad1a68a/CkuVTAfsTSnAmv2e/docs/images/assets/docs/imports/import-workflows/replication-phase.png?fit=max&auto=format&n=CkuVTAfsTSnAmv2e&q=85&s=ad50823ab164d211c33fa655e6b1c47d" alt="The replication lag graph." data-og-width="1978" width="1978" data-og-height="854" height="854" data-path="docs/images/assets/docs/imports/import-workflows/replication-phase.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/CkuVTAfsTSnAmv2e/docs/images/assets/docs/imports/import-workflows/replication-phase.png?w=280&fit=max&auto=format&n=CkuVTAfsTSnAmv2e&q=85&s=fae2bbe6bf73345becfe87d4a998bc1b 280w, https://mintcdn.com/planetscale-cad1a68a/CkuVTAfsTSnAmv2e/docs/images/assets/docs/imports/import-workflows/replication-phase.png?w=560&fit=max&auto=format&n=CkuVTAfsTSnAmv2e&q=85&s=233ef6fe6ff09d0baa9678d778a63cc2 560w, https://mintcdn.com/planetscale-cad1a68a/CkuVTAfsTSnAmv2e/docs/images/assets/docs/imports/import-workflows/replication-phase.png?w=840&fit=max&auto=format&n=CkuVTAfsTSnAmv2e&q=85&s=81b3f11a2aed564114cca76bf5f90201 840w, https://mintcdn.com/planetscale-cad1a68a/CkuVTAfsTSnAmv2e/docs/images/assets/docs/imports/import-workflows/replication-phase.png?w=1100&fit=max&auto=format&n=CkuVTAfsTSnAmv2e&q=85&s=8ad33cdbf01dad527dbf50089fc3a25e 1100w, https://mintcdn.com/planetscale-cad1a68a/CkuVTAfsTSnAmv2e/docs/images/assets/docs/imports/import-workflows/replication-phase.png?w=1650&fit=max&auto=format&n=CkuVTAfsTSnAmv2e&q=85&s=55b27bf3642496b3997881b0687f8a78 1650w, https://mintcdn.com/planetscale-cad1a68a/CkuVTAfsTSnAmv2e/docs/images/assets/docs/imports/import-workflows/replication-phase.png?w=2500&fit=max&auto=format&n=CkuVTAfsTSnAmv2e&q=85&s=92725637599901b0d0eb66cd1b7923c7 2500w" />
</Frame>

## Step 8: Complete the import

Once you've switched all traffic to PlanetScale and verified everything is working:

<Steps>
  <Step>
    Monitor your application for any issues. Check:

    * Application logs for errors
    * Replication lag (should be near zero)
    * Error tracking tools
    * Application performance metrics
  </Step>

  <Step>
    When you're confident everything is working correctly, click "**Complete workflow**" on the workflow monitoring page.
  </Step>

  <Step>
    PlanetScale will detach your external database and the connection will be closed.
  </Step>
</Steps>

**What happens when you complete:**

* Replication from PlanetScale back to your external database stops
* The connection to your external database is closed
* All external database credentials are removed from PlanetScale
* The workflow is marked as complete

<Warning>
  **Important**

  Completing the workflow is not reversible. Make sure your application is running smoothly on PlanetScale before completing the import.
</Warning>

## Next steps

You just migrated your database to PlanetScale. Here are some things you can do next:

* [Create a development branch](/docs/vitess/schema-changes/branching) - Use branching in your development workflow.
* [Create a deploy request](/docs/vitess/schema-changes/branching#1-create-a-deploy-request) - Test schema changes in dev branches before pushing to production.

## Provider-specific migration guides

For detailed instructions on preparing your external database for import, see our provider-specific guides:

* [Amazon Aurora](/docs/vitess/imports/amazon-aurora-migration-guide)
* [AWS RDS for MySQL](/docs/vitess/imports/aws-rds-migration-guide)
* [Azure Database for MySQL](/docs/vitess/imports/azure-database-for-mysql-migration-guide)
* [DigitalOcean MySQL](/docs/vitess/imports/digitalocean-database-migration-guide)
* [Google Cloud SQL](/docs/vitess/imports/gcp-cloudsql-migration-guide)
* [MariaDB](/docs/vitess/imports/mariadb-migration-guide)

## Troubleshooting

For detailed troubleshooting guidance, see our [Import Troubleshooting guide](/docs/vitess/imports/import-troubleshooting).

## Need help?

Get help from [the PlanetScale Support team](https://support.planetscale.com/), or join our [GitHub discussion board](https://github.com/planetscale/discussion/discussions) to see how others are using PlanetScale.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://planetscale.com/llms.txt