# Source: https://docs.airbyte.com/integrations/destinations/clickhouse-migrations.md

![](https://connectors.airbyte.com/files/metadata/airbyte/destination-clickhouse/latest/icon.svg)

# ClickHouse Migration Guide

Copy Page

* Availability

  Core Standard Plus Pro Enterprise Flex Self-Managed Enterprise PyAirbyte

* Support Level

  [Airbyte](/integrations/connector-support-levels.md)

* Connector Version

  [2.1.23](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/destination-clickhouse)

  <!-- -->

  [ ](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/destination-clickhouse)(last updated a month ago)

* Sync Success Rate

* Usage Rate

* Definition ID

  `ce0d828e-1dc4-496c-b122-2da42e637e48`

## SSH support[​](#ssh-support "Direct link to SSH support")

warning

SSH tunneling support for the ClickHouse connector is currently in **Beta**.

## Upgrading to 2.0.0[​](#upgrading-to-200 "Direct link to Upgrading to 2.0.0")

Version 2.0.0 represents a fundamental architectural change from version 1.0.0.

**Version 1.0.0 behavior:**

* Wrote all data as JSON to raw tables in the `airbyte_internal` database
* Used table names like `airbyte_internal.{database}_raw__stream_{table}`

**Version 2.0.0 behavior:**

* Writes data to typed columns matching your source schema
* Creates tables in the configured database with clean table names: `{database}.{table}`
* No longer uses the `airbyte_internal` database or `_raw__stream_` prefixes

While this is a breaking change, existing connections continue to function after upgrading. However, data is written to a completely different location in a different format. **You must update any downstream pipelines** (SQL queries, BI dashboards, data transformations) to reference the new table locations and schema structure.

### Migrating Existing Data to the New Format[​](#migrating-existing-data-to-the-new-format "Direct link to Migrating Existing Data to the New Format")

Airbyte cannot automatically migrate data from the v1 raw table format to the v2 typed table format. To get your data into the new format, you must perform a full refresh sync from your source.

**Migration steps:**

1. Upgrade your ClickHouse destination connector to version 2.0.0 or later
2. Trigger a full refresh sync to populate the new typed tables
3. Verify the new tables contain the expected data
4. Update your downstream pipelines to reference the new table locations
5. Optional: Remove the old v1 raw tables (see below)

#### Optional: Removing the Old v1 Raw Tables[​](#optional-removing-the-old-v1-raw-tables "Direct link to Optional: Removing the Old v1 Raw Tables")

The v2 connector does not automatically remove tables created by the v1 connector. After successfully migrating to v2 and verifying your data, you can optionally remove the old raw tables created by v1 to free up storage space.

For most users, old tables are located in the `airbyte_internal` database with names matching the pattern `airbyte_internal.{database}_raw__stream_{table}`. However, the exact location may vary based on your v1 configuration.

caution

The v2 ClickHouse destination uses the `airbyte_internal` database for temporary scratch space (for example, streams running in `dedup` mode, truncate refreshes, and overwrite syncs). Dropping the entire `airbyte_internal` database can interrupt active syncs and cause data loss. Only drop the specific v1 raw tables you no longer need.

To remove old v1 tables:

```
-- List tables in the airbyte_internal database
SHOW TABLES FROM airbyte_internal;

-- Drop individual v1 raw tables
DROP TABLE airbyte_internal.{database}_raw__stream_{table};
```

### Gotchas[​](#gotchas "Direct link to Gotchas")

Users commonly encounter the following issues when migrating to version 2. Use these steps to understand and resolve them.

#### Namespaces and Databases[​](#namespaces-and-databases "Direct link to Namespaces and Databases")

In version 2.0.0, namespaces are treated as ClickHouse databases. If you configure a custom namespace for your connection, the connector uses that namespace as the database name instead of the database specified in the destination settings.

**Version 1.0.0 behavior:**

* Namespaces were added as prefixes to table names
* Example: namespace `my_namespace` created tables like `default.my_namespace_table_name`

**Version 2.0.0 behavior:**

* Namespaces map directly to ClickHouse databases
* Example: namespace `my_namespace` creates tables like `my_namespace.table_name`

If you have existing connections that use custom namespaces, review your configuration and update downstream pipelines accordingly.

#### Hostname Configuration[​](#hostname-configuration "Direct link to Hostname Configuration")

The hostname field in version 2.0.0 must **not** include the protocol prefix (`http://` or `https://`).

**Incorrect:** `https://my-clickhouse-server.com` **Correct:** `my-clickhouse-server.com`

Version 1.0.0 incidentally tolerated protocols in the hostname field, but version 2.0.0 requires clean hostnames. If your configuration includes a protocol in the hostname, remove it before upgrading or the connection check will fail.
