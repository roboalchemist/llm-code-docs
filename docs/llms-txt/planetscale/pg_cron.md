# Source: https://planetscale.com/docs/postgres/extensions/pg_cron.md

# Extensions: pg_cron

> pg_cron is a simple cron-based job scheduler for PostgreSQL. It allows you to run SQL commands on a schedule, similar to how cron jobs work in Unix-like systems.

## Dashboard Configuration

This extension requires activation via the PlanetScale Dashboard before it can be used. It must be enabled through shared libraries and requires a database restart.

To enable pg\_cron:

<Steps>
  <Step>From the PlanetScale organization dashboard, select the desired database</Step>
  <Step>Navigate to the **Clusters** page from the menu on the left</Step>
  <Step>Choose the branch whose extensions you'd like to configure in the "**Branch**" dropdown</Step>
  <Step>Select the **Extensions** tab</Step>
  <Step>Enable pg\_cron and configure its parameters</Step>
  <Step>Click **Queue extension changes** to apply the configuration</Step>
  <Step>Once you're ready to apply the changes, click "**Apply changes**"</Step>
</Steps>

## Parameters

### cron.database\_name

* **Type**: String
* **Default**: `postgres`
* **Description**: Name of the database where pg\_cron is installed (via CREATE EXTENSION).

### cron.launch\_active\_jobs

* **Type**: Boolean
* **Default**: `true`
* **Description**: Switch to enable/disable running cron jobs - applies to all jobs.

### cron.log\_min\_messages

* **Type**: Select
* **Options**: error, warning, notice, info, log, debug
* **Default**: `warning`
* **Description**: Lowest severity messages to log from the launcher background worker.

### cron.log\_run

* **Type**: Boolean
* **Default**: `true`
* **Description**: Log all cron runs in the cron.job\_run\_details table.

### cron.log\_statement

* **Type**: Boolean
* **Default**: `true`
* **Description**: Log all cron statements before running them.

### cron.max\_running\_jobs

* **Type**: Integer
* **Default**: `1`
* **Minimum**: `1`
* **Description**: Maximum number of jobs that can run at once. Must be less than or equal to cluster-level max\_worker\_processes.

## Usage

After enabling the extension through the dashboard, you can install it in your database:

```sql  theme={null}
CREATE EXTENSION IF NOT EXISTS pg_cron;
```

Then you can schedule jobs using the `cron.schedule` function:

```sql  theme={null}
-- Schedule a job to run every minute
SELECT cron.schedule('job-name', '* * * * *', 'SELECT 1;');
```

## External Documentation

For more detailed information about pg\_cron usage and functionality, see the [official pg\_cron documentation](https://github.com/citusdata/pg_cron).


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://planetscale.com/llms.txt