# Source: https://planetscale.com/docs/postgres/extensions/pg_squeeze.md

# Extensions: pg_squeeze

> pg_squeeze automatically cleans up unused space in tables (table bloat). pg_squeeze helps maintain optimal table performance by removing dead space that accumulates over time from UPDATE and DELETE operations.

## Dashboard Configuration

This extension requires activation via the PlanetScale Dashboard before it can be used. It must be enabled through shared libraries and requires a database restart.

To enable pg\_squeeze:

<Steps>
  <Step>From the PlanetScale organization dashboard, select the desired database</Step>
  <Step>Navigate to the **Clusters** page from the menu on the left</Step>
  <Step>Choose the branch whose extensions you'd like to configure in the "**Branch**" dropdown</Step>
  <Step>Select the **Extensions** tab</Step>
  <Step>Enable pg\_squeeze and configure its parameters</Step>
  <Step>Click **Queue extension changes** to apply the configuration</Step>
  <Step>Once you're ready to apply the changes, click "**Apply changes**"</Step>
</Steps>

## Parameters

### squeeze.max\_xlock\_time

* **Type**: Integer (milliseconds)
* **Default**: `0`
* **Minimum**: `0`
* **Description**: The maximum time the processed table may be locked exclusively.

### squeeze.worker\_autostart

* **Type**: String
* **Default**: `postgres`
* **Description**: Space-separated list of databases to start background workers for automatically.

### squeeze.workers\_per\_database

* **Type**: Integer
* **Default**: `1`
* **Minimum**: `1`
* **Description**: Maximum number of worker processes launched per database. Must be less than or equal to cluster-level max\_worker\_processes.

## Usage

After enabling the extension through the dashboard, you can install it in your database:

```sql  theme={null}
CREATE EXTENSION IF NOT EXISTS pg_squeeze;
```

Then you can schedule tables for squeezing:

```sql  theme={null}
-- Schedule a table to be squeezed
SELECT squeeze.squeeze_table('public', 'your_table_name');
```

## External Documentation

For more detailed information about pg\_squeeze usage and configuration, see the [official pg\_squeeze documentation](https://github.com/cybertec-postgresql/pg_squeeze/).


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://planetscale.com/llms.txt