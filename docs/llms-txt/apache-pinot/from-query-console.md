# Source: https://docs.pinot.apache.org/release-0.11.0/basics/data-import/from-query-console.md

# Source: https://docs.pinot.apache.org/release-0.12.0/basics/data-import/from-query-console.md

# Source: https://docs.pinot.apache.org/release-0.12.1/basics/data-import/from-query-console.md

# Source: https://docs.pinot.apache.org/release-1.0.0/basics/data-import/from-query-console.md

# Source: https://docs.pinot.apache.org/release-1.1.0/basics/data-import/from-query-console.md

# Source: https://docs.pinot.apache.org/release-1.2.0/basics/data-import/from-query-console.md

# Source: https://docs.pinot.apache.org/release-1.3.0/basics/data-import/from-query-console.md

# Source: https://docs.pinot.apache.org/release-1.4.0/manage-data/data-import/from-query-console.md

# Source: https://docs.pinot.apache.org/manage-data/data-import/from-query-console.md

# SQL Insert Into From Files

{% hint style="info" %}
This feature is supported after the 0.11.0 release. Reference PR: <https://github.com/apache/pinot/pull/8557>
{% endhint %}

### Prerequisite

* Ensure you have available Pinot Minion instances deployed within the cluster.
* Pinot version is 0.11.0 or above

### How it works

1. Parse the query with the table name and directory URI along with a list of options for the ingestion job.
2. Call controller minion task execution API endpoint to schedule the task on minion
3. Response has the schema of table name and task job id.

### Usage Syntax

> INSERT INTO \[database.]table FROM FILE dataDirURI OPTION ( k=v ) \[, OPTION (k=v)]\*

### Example

```
SET taskName = 'myTask-s3';
SET input.fs.className = 'org.apache.pinot.plugin.filesystem.S3PinotFS';
SET input.fs.prop.accessKey = 'my-key';
SET input.fs.prop.secretKey = 'my-secret';
SET input.fs.prop.region = 'us-west-2';
INSERT INTO "baseballStats"
FROM FILE 's3://my-bucket/public_data_set/baseballStats/rawdata/'
```

## Insert Rows into Pinot

We are actively developing this feature...

The details will be revealed soon.
