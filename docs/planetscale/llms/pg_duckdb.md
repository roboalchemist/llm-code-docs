# Source: https://planetscale.com/docs/postgres/extensions/pg_duckdb.md

# Extensions: pg_duckdb

> pg_duckdb is a Postgres extension that embeds DuckDB, a high-performance analytical database, directly into Postgres.

<Warning>
  We don't recommend running `pg_duckdb` directly on your PlanetScale Postgres database as it can consume significant resources during analytical queries. If you want to use DuckDB for analytics, we recommend using [MotherDuck](https://motherduck.com/) to host your analytical workloads separately.
</Warning>

## Dashboard Configuration

This extension requires activation via the PlanetScale dashboard before it can be used. It must be enabled through shared libraries and requires a database restart.

To enable pg\_duckdb:

<Steps>
  <Step>From the PlanetScale organization dashboard, select the desired database</Step>
  <Step>Navigate to the **Clusters** page from the menu on the left</Step>
  <Step>Choose the branch whose extensions you'd like to configure in the "**Branch**" dropdown</Step>
  <Step>Select the **Extensions** tab</Step>
  <Step>Enable `pg_duckdb` and configure its parameters</Step>
  <Step>Click **Queue extension changes** to apply the configuration</Step>
  <Step>Once you're ready to apply the changes, click "**Apply changes**"</Step>
</Steps>

## Parameters

### duckdb.postgres\_role

* **Type**: String
* **Default**: `pscale_superuser`
* **Description**: Specifies the Postgres role that is allowed to use DuckDB execution and manage secrets.

### duckdb.memory\_limit

* **Type**: Integer
* **Default**: 0
* **Description**: Maximum memory DuckDB can use per connection in megabytes. Setting to 0 activates DuckDB's default (80% of available RAM).

## Usage

After enabling the extension through the dashboard, you can install it in your database:

```sql  theme={null}
CREATE EXTENSION IF NOT EXISTS pg_duckdb;
```

Once installed, you can use DuckDB's analytical capabilities directly from PostgreSQL. For example:

```sql  theme={null}
-- Query PostgreSQL tables using DuckDB's analytical engine
SELECT * FROM duckdb.read_parquet('s3://bucket/data.parquet');
```

## External Documentation

For more detailed information about `pg_duckdb` usage and functionality, see the [official `pg_duckdb` documentation](https://github.com/duckdb/pg_duckdb).


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://planetscale.com/llms.txt