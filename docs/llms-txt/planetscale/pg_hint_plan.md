# Source: https://planetscale.com/docs/postgres/extensions/pg_hint_plan.md

# Extensions: pg_hint_plan

> The pg_hint_plan extension allows you to influence the query planner's decisions by providing hints. It can be used to optimize query performance by guiding the planner towards more efficient execution plans.

## Dashboard Configuration

The pg\_hint\_plan extension requires activation via the PlanetScale Dashboard before it can be used. It must be enabled through shared libraries and requires a database restart.

To enable pg\_hint\_plan:

<Steps>
  <Step>From the PlanetScale organization dashboard, select the desired database</Step>
  <Step>Navigate to the **Clusters** page from the menu on the left</Step>
  <Step>Choose the branch whose extensions you'd like to configure in the "**Branch**" dropdown</Step>
  <Step>Select the **Extensions** tab</Step>
  <Step>Enable pg\_hint\_plan and configure its parameters</Step>
  <Step>Click **Queue extension changes** to apply the configuration</Step>
  <Step>Once you're ready to apply the changes, click "**Apply changes**"</Step>
</Steps>

## Parameters

### pg\_hint\_plan.enable\_hint

* **Type**: Boolean
* **Default**: `true`
* **Description**: Enable/disable hint functionality.

### pg\_hint\_plan.enable\_hint\_table

* **Type**: Boolean
* **Default**: `false`
* **Description**: Enable hint table functionality.

### pg\_hint\_plan.parse\_messages

* **Type**: Select
* **Options**: error, warning, notice, info, log, debug
* **Default**: `info`
* **Description**: Control parsing message output.

### pg\_hint\_plan.debug\_print

* **Type**: Select
* **Options**: off, on, detailed, verbose
* **Default**: `off`
* **Description**: Enable debug output.

### pg\_hint\_plan.message\_level

* **Type**: Select
* **Options**: error, warning, notice, info, log, debug
* **Default**: `info`
* **Description**: Set message verbosity level.

## Usage

<Note>
  Unlike most PostgreSQL extensions, `pg_hint_plan` does not require `CREATE EXTENSION` to function. Once enabled
  through the dashboard, it's automatically loaded and available for use. You only need to run `CREATE EXTENSION` if you
  plan to use the hint table functionality (when `pg_hint_plan.enable_hint_table` is enabled).
</Note>

After enabling the extension through the dashboard, you can optionally install it in your database for hint table functionality:

```sql  theme={null}
-- Only required if using hint tables
CREATE EXTENSION IF NOT EXISTS pg_hint_plan;
```

Then you can use hints in your queries:

```sql  theme={null}
/*+
    SeqScan(t1)
    IndexScan(t2 t2_pkey)
*/
SELECT * FROM table1 t1 JOIN table2 t2 ON t1.id = t2.id;
```

## External Documentation

For more detailed information about pg\_hint\_plan usage and hint syntax, see the [official pg\_hint\_plan documentation](https://github.com/ossc-db/pg_hint_plan).


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://planetscale.com/llms.txt