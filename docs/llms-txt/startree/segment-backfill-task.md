# Source: https://docs.startree.ai/corecapabilities/manage-data/segment-backfill-task.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Segment Backfill Task

## Overview

As data governance, compliance, and quality expectations continue to evolve, organizations require more precise tools to manage and maintain data in real-time analytics platforms. The Minion-Based Segment Backfill Task in StarTree Cloud addresses this need by enabling selective deletion and backfill of data in a way that is both powerful and easy to control, without resorting to complex, manual workarounds.

## Key Capabilities

### Selective Data Deletion

The Backfill Task supports multiple modes to select data for deletion:

* **Time range** (e.g., a specific day or hour)
* **Dimension filters** (e.g., currency = EUR, region = APAC)
* **Combination** of time range and dimension filters

It is recommended to configure one of these criteria for data deletion. If deletion is not required, use the File Ingestion Task instead.

### Selective Data Backfill

Users can re-ingest targeted subsets of data, such as corrected records or missing slices, without reprocessing entire partitions or tables.

### Atomic and Consistent Updates

Backfill operations are atomic by design. When segment replacement is involved, either all related segments are updated or none are, maintaining table integrity and avoiding partial updates or broken transitions.

## How Does it Work?

The Backfill Task is initiated via an ad-hoc execution API and operates on time-partitioned data with all-or-none consistency. It consists of four phases:

### 1. Segment Selector

Filters segments based on deletion or purge criteria. It identifies full deletions and partial purges, generating tasks with types: `Purge`, `Delete`, or `Ingest`.

### 2. Segment Purger

Removes specific records from segments using defined filters, without deleting entire segments.

### 3. Segment Deletor

Completely deletes segments that the Segment Selector marked for removal.

### 4. Data Ingestor

Uses the FileIngestionTask to bring in new data by creating segments that replace or append to existing ones.

## Limitations

| Constraint                              | Description                                                                                                                                                                                                                                |
| --------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| No Native Scheduling Support            | Triggered on demand via API; users must manage automation.                                                                                                                                                                                 |
| No Preview or Dry Run Mode              | No simulation capability; filters should be validated thoroughly.                                                                                                                                                                          |
| No Support for Upsert-Enabled Tables    | Not supported currently.                                                                                                                                                                                                                   |
| Task Interference                       | Disable other tasks (FileIngestion, SegmentRefresh, AlterTableTask) during backfill execution.                                                                                                                                             |
| No Support for Sync Mode enabled Tables | The Backfill Task should not be executed on the Pinot tables that were originally ingested using [sync-mode in File Ingestion Task](https://docs.startree.ai/corecapabilities/ingestdata/adv-concepts/batch/file-ingestion-task#sync-mode) |
| No Support for Delta Ingested Tables    | The Backfill Task should not be executed on Pinot tables that were originally ingested from a Delta table.                                                                                                                                 |

## Configuration Parameters

If Backfill also needs to ingest new data, it is important to configure the Segment Backfill Task using the [File Ingestion Task configuration parameters](https://docs.startree.ai/corecapabilities/ingestdata/adv-concepts/batch/file-ingestion-task). A reference table of key Backfill-related configuration parameters is provided below.

| Parameter                      | Description                                                                                                        | Accepted Values / Format                  | Example                         |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ----------------------------------------- | ------------------------------- |
| `backfill.start.time.ms`       | Start timestamp for purge/replace                                                                                  | Epoch ms                                  | `1727748000000`                 |
| `backfill.end.time.ms`         | End timestamp                                                                                                      | Epoch ms                                  | `1727755200000`                 |
| `backfill.field.names`         | Multi-dimensional filters                                                                                          | Comma-separated                           | `industry,country`              |
| `backfill.field.values`        | Values for field names                                                                                             | Comma-separated                           | `ENERGY,Germany`                |
| `backfill.comparison.operator` | Field comparison logic                                                                                             | `==`(default), `!=`, `<`, `<=`, `>`, `>=` | `"!="`                          |
| `backfill.input.dir`           | Data source path for ingestion. Make sure backfill input directory is different to the actual ingestion directory. | File path                                 | `/data/clean/stocks/2024-10-01` |
| `backfill.logical.operator`    | Combines multiple filters                                                                                          | `&&`(default), `\|\|`                     | `\|\|`                          |
| `backfill.input.format`        | Input file format                                                                                                  | `CSV`, `JSON`, etc.                       | `CSV`                           |

## Sample Task Configuration

```json  theme={null}
{
  "task": {
    "taskTypeConfigsMap": {
      "SegmentBackfillTask": {
        "backfill.start.time.ms": 1735689601000,
        "backfill.end.time.ms": 1735775999000,
        "backfill.input.dir": "/path/to/data",
        "backfill.input.format": "json",
        "input.fs.className": "org.apache.pinot.plugin.filesystem.S3PinotFS",
        "input.fs.prop.accessKey": "MY_ACCESS_KEY",
        "input.fs.prop.secretKey": "MY_SECRET_KEY",
        "input.fs.prop.region": "us-west-2"
      }
    }
  }
}
```

## Key Use Case Scenarios

### 1. Delete a Subset of Table

Remove data/segments for a specific time range.

```json  theme={null}
{
  "backfill.start.time.ms": "<start_timestamp_ms>",
  "backfill.end.time.ms": "<end_timestamp_ms>"
}
```

### 2. Replace a Subset of the Table

Delete existing data and replace with clean data for a specific time range.

```json  theme={null}
{
  "backfill.start.time.ms": "<start_timestamp_ms>",
  "backfill.end.time.ms": "<end_timestamp_ms>",
  "backfill.input.dir": "/path/to/clean/data",
  "backfill.input.format": "CSV"
}
```

### 3. Mixed Operation: Delete Some, Replace Others, and Add New Segments

A table has inconsistent data - some segments are invalid and should be removed, some are outdated and need replacing, and new records need to be appended.
Perform a combination of:

* Deleting some segments outright,
* Replacing a set of segments,
* Ingesting entirely new segments.

```json  theme={null}
{
  "backfill.segment.list": "segment_old1, segment_old2",
  "backfill.start.time.ms": "<start_timestamp_ms>",
  "backfill.end.time.ms": "<end_timestamp_ms>",
  "backfill.input.dir": "/path/to/new/data",
  "backfill.input.format": "CSV"
}
```

### 4. Replace Data Matching Multiple Values

**Example: currency is EUR or USD**

```json  theme={null}
{
  "backfill.field.names": "currency, currency",
  "backfill.field.values": "EUR,USD",
  "backfill.logical.operator": "||",
  "backfill.input.dir": "/path/to/data",
  "backfill.input.format": "CSV"
}
```

**Example: industry is ENERGY or country is Germany**

```json  theme={null}
{
  "backfill.field.names": "industry,country",
  "backfill.field.values": "ENERGY,Germany",
  "backfill.logical.operator": "||",
  "backfill.input.dir": "/path/to/data",
  "backfill.input.format": "CSV"
}
```

**Example: currency is not EUR**

```json  theme={null}
{
  "backfill.field.names": "currency",
  "backfill.field.values": "EUR",
  "backfill.comparison.operator": "!=",
  "backfill.input.dir": "/path/to/data",
  "backfill.input.format": "CSV"
}
```

### 5. Replace with Time and Multi-dimension Filter

```json  theme={null}
{
  "backfill.start.time.ms": "<start_timestamp_ms>",
  "backfill.end.time.ms": "<end_timestamp_ms>",
  "backfill.field.names": "currency, currency",
  "backfill.field.values": "EUR,USD",
  "backfill.logical.operator": "||",
  "backfill.input.dir": "/path/to/data",
  "backfill.input.format": "CSV"
}
```

### 6. Add New Data or Segments Only

**Use the File Ingestion Task when no deletion is needed.**

## FAQs & Recommendations

<AccordionGroup>
  <Accordion title="Is custom dimension partitioning required?">
    No, segment purger performs record-level scans.
  </Accordion>

  <Accordion title="Can I use Backfill Task on Upsert tables?">
    No, it’s not supported at the moment.
  </Accordion>

  <Accordion title="Can Backfill Task be used for deletion only?">
    Yes, Backfill Task can be used for deletion only. A time based or dimension based filter can also be applied for selective deletion.
  </Accordion>

  <Accordion title="Should I use Backfill to only ingest new data?">
    No, use the File Ingestion Task for that.
  </Accordion>

  <Accordion title="Can it run with other tasks?">
    No, disable concurrent tasks.
  </Accordion>

  <Accordion title="What if new data is small and segments become uneven?">
    Cluster Health Check dashboard can give insights into Segment sizes and skewness if there is any. Use Alter Table Task after Backfill to optimize the Segment size.
  </Accordion>
</AccordionGroup>

Built with [Mintlify](https://mintlify.com).
