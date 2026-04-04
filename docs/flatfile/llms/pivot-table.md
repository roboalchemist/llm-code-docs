# Source: https://flatfile.com/docs/plugins/pivot-table.md

> ## Documentation Index
> Fetch the complete documentation index at: https://flatfile.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Pivot Table Exporter

> A Flatfile plugin that performs data analysis and summarization by generating pivot tables from workbook data and uploading them as Markdown documents.

The Pivot Table Exporter plugin for Flatfile is designed to perform data analysis and summarization directly within the Flatfile environment. It listens for a specific job trigger ('workbook:generatePivotTable'), fetches all records from the first sheet in a workbook, and then generates a pivot table based on user-defined configuration. The resulting pivot table is formatted into a Markdown document and uploaded back to the Flatfile space. This is useful for users who need to quickly aggregate, group, and analyze data during an import process without leaving the Flatfile UI. For example, it can be used to summarize sales data by region and category, or count records based on different attributes.

## Installation

Install the plugin using npm:

```bash  theme={null}
npm install @flatfile/plugin-export-pivot-table
```

## Configuration & Parameters

The plugin accepts a configuration object with the following parameters:

### Required Parameters

<ParamField path="pivotColumn" type="string" required>
  The name of the column in your sheet to use as the main pivot (rows in the output table).
</ParamField>

<ParamField path="aggregateColumn" type="string" required>
  The name of the column containing the numerical data to be aggregated.
</ParamField>

<ParamField path="aggregationMethod" type="'sum' | 'average' | 'count' | 'min' | 'max'" required>
  The mathematical operation to perform on the `aggregateColumn`.
</ParamField>

### Optional Parameters

<ParamField path="groupByColumn" type="string">
  An optional column to group the data by. If provided, this will create distinct columns in the output table for each unique value in the `groupByColumn`.
</ParamField>

<ParamField path="debug" type="boolean" default="false">
  If set to true, the plugin will log any caught errors to the console, which is useful for server-side debugging.
</ParamField>

### Default Behavior

By default, the plugin requires `pivotColumn`, `aggregateColumn`, and `aggregationMethod` to be defined. If `groupByColumn` is not provided, the plugin will aggregate data across all records for each unique `pivotColumn` value and present the result in a single "Total" column. The `debug` mode is disabled by default, meaning errors are only reported back to the Flatfile job status without being logged to the console.

## Usage Examples

### Basic Usage

This example shows the simplest way to use the plugin with the required configuration.

<CodeGroup>
  ```javascript JavaScript theme={null}
  import { FlatfileListener } from '@flatfile/listener';
  import { pivotTablePlugin } from '@flatfile/plugin-export-pivot-table';

  export default function(listener) {
    listener.use(
      pivotTablePlugin({
        pivotColumn: 'country',
        aggregateColumn: 'order_value',
        aggregationMethod: 'sum',
      })
    );
  }
  ```

  ```typescript TypeScript theme={null}
  import { FlatfileListener } from '@flatfile/listener';
  import { pivotTablePlugin } from '@flatfile/plugin-export-pivot-table';

  export default function(listener: FlatfileListener) {
    listener.use(
      pivotTablePlugin({
        pivotColumn: 'country',
        aggregateColumn: 'order_value',
        aggregationMethod: 'sum',
      })
    );
  }
  ```
</CodeGroup>

### Configuration with Optional Parameters

This example demonstrates a more complete configuration, including the optional `groupByColumn` and `debug` options.

<CodeGroup>
  ```javascript JavaScript theme={null}
  import { FlatfileListener } from '@flatfile/listener';
  import { pivotTablePlugin } from '@flatfile/plugin-export-pivot-table';

  export default function(listener) {
    listener.use(
      pivotTablePlugin({
        pivotColumn: 'Region',
        aggregateColumn: 'Sales',
        aggregationMethod: 'average',
        groupByColumn: 'Category',
        debug: true,
      })
    );
  }
  ```

  ```typescript TypeScript theme={null}
  import { FlatfileListener } from '@flatfile/listener';
  import { pivotTablePlugin } from '@flatfile/plugin-export-pivot-table';

  export default function(listener: FlatfileListener) {
    listener.use(
      pivotTablePlugin({
        pivotColumn: 'Region',
        aggregateColumn: 'Sales',
        aggregationMethod: 'average',
        groupByColumn: 'Category',
        debug: true,
      })
    );
  }
  ```
</CodeGroup>

### Error Handling with Debug Mode

The plugin has built-in error handling. To see more detailed logs on your server, enable the `debug` flag.

<CodeGroup>
  ```javascript JavaScript theme={null}
  import { FlatfileListener } from '@flatfile/listener';
  import { pivotTablePlugin } from '@flatfile/plugin-export-pivot-table';

  const listener = new FlatfileListener();

  // Enable debug mode to log errors to the server console
  listener.use(
    pivotTablePlugin({
      pivotColumn: 'non_existent_column', // This will cause an error
      aggregateColumn: 'Sales',
      aggregationMethod: 'sum',
      debug: true,
    })
  );

  export default listener;
  ```

  ```typescript TypeScript theme={null}
  import { FlatfileListener } from '@flatfile/listener';
  import { pivotTablePlugin } from '@flatfile/plugin-export-pivot-table';

  const listener = new FlatfileListener();

  // Enable debug mode to log errors to the server console
  listener.use(
    pivotTablePlugin({
      pivotColumn: 'non_existent_column', // This will cause an error
      aggregateColumn: 'Sales',
      aggregationMethod: 'sum',
      debug: true,
    })
  );

  export default listener;
  ```
</CodeGroup>

## Troubleshooting

If you encounter issues with the pivot table plugin, follow these troubleshooting steps:

1. **Check the job outcome message**: If a job fails, check the "outcome" message on the job in the Flatfile UI for initial error information.

2. **Enable debug mode**: If the error message is not clear, re-run the job with the `debug: true` configuration option enabled and check your server-side logs for a more detailed error stack trace.

3. **Verify column names**: Common errors include providing incorrect column names in the configuration that do not match the columns in the sheet.

4. **Check data types**: Ensure that the `aggregateColumn` contains numeric data. Non-numeric values will be treated as 0.

## Notes

### Requirements and Limitations

* The plugin must be deployed in a server-side listener environment
* It triggers on a specific job: `job: 'workbook:generatePivotTable'`. This job must be initiated from the Flatfile UI or via an API call
* The plugin processes data from the first sheet it finds in the workbook (`sheets.data[0]`). It does not currently support selecting a specific sheet by name or ID
* The values in the `aggregateColumn` are expected to be numbers. Non-numeric values will be treated as 0

### Error Handling

The plugin uses a `try...catch` block to manage errors during its execution:

* On start, it acknowledges the job with `api.jobs.ack`
* On success, it completes the job with `api.jobs.complete` and a success message
* On failure, it fails the job with `api.jobs.fail` and an error message
* If the `debug: true` option is set, the caught error object is also logged to the console
