# Source: https://docs.mage.ai/guides/streaming/destinations/duckdb.md

# Source: https://docs.mage.ai/data-integrations/destinations/duckdb.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.mage.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# DuckDB

> How to configure DuckDB as a destination in Mage to write pipeline data to local DuckDB files for fast, embedded analytics.

export const ProOnly = ({button = 'Get started for free', description = 'Try our fully managed solution to access this advanced feature.', source = 'documentation', title = 'Only in Mage Pro.'}) => <a href={`https://cloud.mage.ai/sign-up?source=${source}`} className="block my-4 px-5 py-4 overflow-hidden rounded-xl flex gap-3 border border-emerald-500/20 bg-emerald-50/50 dark:border-emerald-500/30 dark:bg-emerald-500/10" target="_blank">
    <div style={{
  display: 'flex',
  alignItems: 'center',
  width: '100%'
}}>
      <div className="text-sm prose min-w-0 text-emerald-900 dark:text-emerald-200" style={{
  flex: 1
}}>
        {title}
        <p className="normal">{description}</p>
      </div>

      <div> </div>

      <div>
        <ProButton label={button} href={`https://cloud.mage.ai/sign-up?source=${source}`} />
      </div>
    </div>
  </a>;

export const ProButton = ({href, label = 'Get started with Mage Pro for free', source = 'documentation'}) => <div style={{
  height: 32,
  position: 'relative'
}}>
    <a target="_blank" className="group px-4 py-1.5 relative inline-flex items-center text-sm font-medium rounded-full" href={href ?? `https://cloud.mage.ai/sign-up?source=${source}`}>
      <span className="absolute inset-0 bg-primary-dark dark:bg-primary-light/10 border-primary-light/30 rounded-full dark:border group-hover:opacity-[0.9] dark:group-hover:border-primary-light/60">
      </span>

      <div className="mr-0.5 space-x-2.5 flex items-center">
        <span class="z-10 text-white dark:text-primary-light">
          {label}
        </span>

        <svg width="3" height="24" viewBox="0 -9 3 24" class="h-5 rotate-0 overflow-visible text-white/90 dark:text-primary-light">
          <path d="M0 0L3 3L0 6" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"></path>
        </svg>
      </div>
    </a>
  </div>;

<ProOnly source="data-integration" />

![DuckDB Logo](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*Qcgc4cmJk5lFGBwi.png)

***

## Overview

Use **DuckDB** as a destination in Mage to write structured data to local DuckDB database files. DuckDB is an embedded analytical database that runs in-process, making it ideal for fast local analytics, data staging, or lightweight data processing workflows.

This destination is perfect for scenarios where you need to quickly analyze data locally before pushing to a larger data warehouse, or for building lightweight analytics pipelines.

***

## Required Configuration

You must enter the following configuration when writing to a DuckDB destination:

| Key         | Description                                                             | Example Value                               | Required |
| ----------- | ----------------------------------------------------------------------- | ------------------------------------------- | -------- |
| `file_path` | Absolute file path to the `.duckdb` file where data will be saved.      | `/home/src/default_repo/mage_output.duckdb` | ✅        |
| `if_exists` | What to do if the table already exists: `replace`, `append`, or `fail`. | `replace`                                   | ✅        |

***

## Configuration Options

### `if_exists` Values

| Value     | Description                                                                                    |
| --------- | ---------------------------------------------------------------------------------------------- |
| `replace` | Overwrites the existing table with new data. The table will be recreated on each pipeline run. |
| `append`  | Adds new data to the existing table. Existing rows remain unchanged.                           |
| `fail`    | Raises an error if the table already exists. Useful for preventing accidental overwrites.      |

***

## Notes

* **Embedded Database**: DuckDB is an embedded database. The file is local to the machine or container where Mage is running.
* **Pandas Integration**: Supports writing pandas DataFrames directly to tables in a `.duckdb` file.
* **File Path**: Use absolute paths to ensure the file is created in the correct location.
* **Performance**: DuckDB is optimized for analytical queries and can handle large datasets efficiently.
* **Use Cases**: Ideal for fast, local analytics or staging data before pushing to a warehouse.

***

## Sample Configuration

```yaml  theme={"system"}
file_path: /home/src/default_repo/mage_output.duckdb
if_exists: replace
```

***

## Related Resources

* [DuckDB Documentation](https://duckdb.org/docs/)
* [DuckDB Python API](https://duckdb.org/docs/api/python/overview)
* [DuckDB GitHub Repository](https://github.com/duckdb/duckdb)


Built with [Mintlify](https://mintlify.com).