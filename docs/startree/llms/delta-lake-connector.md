# Source: https://docs.startree.ai/corecapabilities/ingestdata/adv-concepts/batch/delta-lake-connector.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Delta Lake Ingestion

The Delta Lake connector allows ingestion from a Delta Lake data platform hosted in S3 and GCS into Pinot. The ingestion is done as a periodic pull based system that is executed by the Pinot Minion framework. You specify the period that you want the ingestion task to follow and on each trigger Minion will check if there has been a change to the Delta Lake since the last execution and, if there has, it will ingest the new data.

StarTree's Delta Lake connector supports both the older Standalone Delta Lake API(v3.3.2) and the new Delta Kernel API(v4.0.0). With the Delta Kernel API, the StarTree Delta Lake connector also supports the use of [Deletion Vectors](https://docs.delta.io/latest/delta-deletion-vectors.html).

## Prerequisites

* Delta Lake ingestion can only be enabled for offline Pinot tables
* This connector supports Delta tables hosted on Amazon S3 and Google Cloud Storage(GCS).
* This connector supports only sync mode, meaning each file in Delta Lake maps to a single segment in Pinot. Therefore, it is recommended to size the files appropriately to avoid creating an excessive number of segments. Find the [official documentation](https://docs.databricks.com/en/delta/tune-file-size.html#set-a-target-file-size) on how to tune the size of files in your Delta table.

## Limitations

* Support for ADLS is not yet available.
* Delta tasks do not utilize checkpoints. Consequently, no table entry is created at the ZK path PROPERTYSTORE→MINION\_TASK\_METADATA. This limitation applies to both Delta Standalone mode and Delta Kernel mode. Tasks will fail if not completed within one day, as Delta does not track progress. Subsequent triggers will generate new tasks to resume processing.

## Pinot Table Configuration

The offline table task configs can be manually set with the following connection and ingestion parameters.

## Connection Parameters

All the following properties are required to establish connection with Delta Tables.

| Property Name                               | Required | Description                                                                                                                                                                                                                         |
| ------------------------------------------- | -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| delta.ingestion.table.fs                    | Yes      | Must be set to "S3" or "GCS"                                                                                                                                                                                                        |
| delta.ingestion.table.uri                   | Yes      | It is the source location of the Delta Lake table. <br /> For Amazon S3, the URI should start with: `s3a://<bucket-name>/path/to/delta-table`. <br /> For GCS, the URI should start with: `gs://<bucket-name>/path/to/delta-table`. |
| delta.ingestion.useDeltaKernel              | No       | When set to `"true"` this will make the Delta Lake connector use the Delta Kernel API.  When not provided this will default to `false`. It should be set to `true`, when delta table is hosted on GCS                               |
| delta.ingestion.table.kernel.maxFilesPerRun | No       | Set this to limit files processed per ingestion run. The default value is -1, which means unlimited or all files.                                                                                                                   |
| delta.ingestion.max.parallel.ops            | No       | Control parallel operations, the default value is 1                                                                                                                                                                                 |
| delta.ingestion.preserveNullValues          | No       | Preserve null values in complex data types(arrays, maps, structs). The default value is false. The supported values are true, and false.                                                                                            |
| tableMaxNumTasks                            | No       | This is used to determine how to partition ingestion jobs across Minion workers                                                                                                                                                     |
| schedule                                    | Yes      | This sets the schedule for execution and uses the [Quartz schedule format](https://www.quartz-scheduler.org/documentation/quartz-2.3.0/tutorials/tutorial-lesson-06.html) for setting the schedule                                  |
| segmentIngestionType                        | Yes      | It should be set to REFRESH. As the complete segment is replaced every time during ingestion for a particular file. This configuration is part of `ingestionConfig.batchIngestionConfig`                                            |
| batch.segment.upload                        | No       | Enable batch segment uploads. This is kept enabled by default. The supported values are true, and false. When enabled it requires push.mode to be set as METADATA, which is set as default.                                         |

## Authentication Parameters

### Delta Tables hosted on S3 via Basic Authentication

Use the following JSON configuration when Delta is set up on S3 with Basic Authentication

```json  theme={null}
"ingestionConfig": {
    "batchIngestionConfig": {
      "segmentIngestionType": "REFRESH"
    }
  }

"task": {
      "taskTypeConfigsMap": {
        "DeltaTableIngestionTask": {
          "delta.ingestion.table.fs": "S3",
          "delta.ingestion.useDeltaKernel": "true",
          "delta.ingestion.table.uri": "s3a://bucket-name/path/to/delta-table",
          "delta.ingestion.table.s3.accessKey": "myAccessKey",
          "delta.ingestion.table.s3.secretKey": "mySecretKey",
          "delta.ingestion.table.s3.region": "us-west-2",
          "schedule": "0 20 * ? * * *",
          "tableMaxNumTasks": "1000"
        }
      }
    }
```

#### Property Descriptions

| Property Name                      | Required | Description                                                                                                                       |
| ---------------------------------- | -------- | --------------------------------------------------------------------------------------------------------------------------------- |
| delta.ingestion.table.s3.region    | Yes      | The AWS region that houses the Delta Lake.                                                                                        |
| delta.ingestion.table.s3.accessKey | No       | If you are using Access Key based authorization then this is for the AWS access key. You will also need the AWS Secret Key below. |
| delta.ingestion.table.s3.secretKey | No       | The AWS Secret Key.                                                                                                               |

### Delta Tables hosted on S3 via IAM based Authentication

```json  theme={null}
"ingestionConfig": {
    "batchIngestionConfig": {
      "segmentIngestionType": "REFRESH"
    }
  }

"task": {
      "taskTypeConfigsMap": {
        "DeltaTableIngestionTask": {
          {
                  "tableMaxNumTasks": "1000",
                  "schedule": "0 20 * ? * * *",
                  "delta.ingestion.useDeltaKernel": "true",
                  "delta.ingestion.table.fs": "S3",
                  "delta.ingestion.table.uri": "s3a://my-bucket/my-data-directory/",
                  "delta.ingestion.table.s3.role.arn": "arn:aws:iam::123456789012:role/PinotS3AccessRole",
                  "delta.ingestion.table.s3.region": "s3_region",
                  "fs.s3a.assumed.role.arn": "arn:aws:iam::123456789012:role/PinotS3AccessRole",
                  "fs.s3a.assumed.role.sts.endpoint": "https://sts.region.amazonaws.com",
                  "fs.s3a.assumed.role.sts.endpoint.region": "s3_region",
                  "fs.s3a.aws.credentials.provider": "ai.startree.connectors.auth.AssumedRoleCredentialsProvider",
                  "fs.s3a.assumed.role.credentials.provider": "com.amazonaws.auth.InstanceProfileCredentialsProvider"
          }
        }
      }
    }
```

#### Property Descriptions

If you are using IAM to managed access to your S3 bucket then, use the following parameters:

| Property Name                            | Required | Description                                                                                                                                                                                                       |
| ---------------------------------------- | -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| delta.ingestion.table.s3.region          | Yes      | The AWS region that houses the Delta Lake.                                                                                                                                                                        |
| delta.ingestion.table.s3.role.arn        | Yes      | `"arn:aws:iam::REPLACE_WITH_AWS_ACCOUNT_ID_WHERE_DATA_RESIDES:role/DataManagerDeltaLakeS3IAMRole"`                                                                                                                |
| fs.s3a.aws.credentials.provider          | Yes      | Must be `"org.apache.hadoop.fs.s3a.auth.AssumedRoleCredentialProvider"` on StarTree Pinot versions 1.2.0\* and `"ai.startree.connectors.auth.AssumedRoleCredentialsProvider"` on StarTree Pinot versions 1.3.0\*. |
| fs.s3a.assumed.role.sts.endpoint         | Yes      | The STS endpoint for your account (e.g., `https://sts.us-west-2.amazonaws.com`)                                                                                                                                   |
| fs.s3a.assumed.role.sts.endpoint.region  | Yes      | The Region for your account (e.g, `us-west-2`)                                                                                                                                                                    |
| fs.s3a.assumed.role.arn                  | Yes      | The ARN For the Role that will be assumed to get access (`"arn:aws:iam::REPLACE_WITH_AWS_ACCOUNT_ID_WHERE_DATA_RESIDES:role/DataManagerDeltaLakeS3IAMRole"`)                                                      |
| fs.s3a.assumed.role.credentials.provider | Yes      | Must be `com.amazonaws.auth.InstanceProfileCredentialsProvider`. Used to gain a set of temporary security credentials to access an ARN that is in an account outside of the StarTree cluster.                     |

### Delta Tables hosted on GCS

Use the following JSON configuration when Delta is set up on GCS

```json  theme={null}
"ingestionConfig": {
    "batchIngestionConfig": {
      "segmentIngestionType": "REFRESH"
    }
  }

"task": {
      "taskTypeConfigsMap": {
        "DeltaTableIngestionTask": {
          "delta.ingestion.table.fs": "GCS",
          "delta.ingestion.useDeltaKernel": "true",
          "delta.ingestion.table.uri": "gs://bucket-name/path/to/delta-table",
          "delta.ingestion.table.gcs.projectId": "project_id_123",
          "delta.ingestion.table.gcs.keyContentBase64": "hraUc5dzBCQVFFRkFBU0NCS2d3Z2dTa=",
          "schedule": "0 20 * ? * * *",
          "tableMaxNumTasks": "1000"
        }
      }
    }
```

#### Property Descriptions

| Property Name                              | Required | Description                                                                                                                                                                                                                                                                                                                                                                     |
| ------------------------------------------ | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| delta.ingestion.table.gcs.projectId        | Yes      | It is the GCP project ID associated with the bucket that stores Delta Lake data.                                                                                                                                                                                                                                                                                                |
| delta.ingestion.table.gcs.keyContentBase64 | No       | It is used to specify the Google Cloud Service Account key in Base64-encoded format for authentication when accessing Delta Lake data stored in GCS. `delta.ingestion.table.gcs.keyFile` can be alternatively used instead of this parameter. See [Google documentation](https://cloud.google.com/iam/docs/keys-create-delete#creating) on how to create a service account key. |
| delta.ingestion.table.gcs.keyFile          | No       | It specifies the path to the Google Cloud Service Account key file used for authentication when accessing Delta Lake data stored in a GCS bucket. It should be available locally in all minions. `delta.ingestion.table.gcs.keyContentBase64` can be alternatively used instead of this parameter.                                                                              |

## Frequently Asked Questions

<AccordionGroup>
  <Accordion title="What happens if the same row is updated multiple times in my Delta table (e.g., order status updates)?">
    StarTree uses Delta Kernel Library to get the updated list of files and uses the Minion framework to manage data segments. Every time a row is added, updated, or deleted in Delta, the underlying files change, which updates the table version. Pinot detects these changes and updates its corresponding table segments accordingly — ensuring the latest state is always reflected.

    If there are 1M rows in a table and only one row is updated. This will result into update in one segment only since file and segment has 1:1 mapping. In other words,

    * If all 1M rows are stored in a single file and hence one single segment, the entire segment will be replaced even if just one row changes.
    * If the 1M rows are split across 10 files, only the relevant segment (1 out of 10) mapped to the particular file containing the updated row will be replaced.

    This ensures Pinot always reflects the latest state while maintaining efficient resource usage, depending on how the segments are structured.
  </Accordion>

  <Accordion title="Can I configure Pinot to refresh every minute like my Delta table?">
    Yes, you can. Pinot supports high-frequency scheduling, including a 1-minute refresh. This will create one ingestion task per minute. However, if you’re targeting sub-minute or near real-time updates, a streaming ingestion approach may be more efficient.
  </Accordion>

  <Accordion title="Does StarTree support Unity Catalog (UC) for column-level access control?">
    Not at the moment. Unity Catalog support is currently not available in the Delta Kernel libraries, so Pinot doesn’t support it either. As a workaround, you can filter out restricted columns while creating the Pinot table.
  </Accordion>

  <Accordion title="Does Pinot always poll the S3 bucket to list files for ingestion?">
    No. Pinot uses an internal watermark system via Zookeeper to avoid scanning all files every time. It only checks for new files added after the watermark. DeltaIngestionTask (Delta ingestion) relies on Delta’s transaction logs. Starting from version 1.3.0, it no longer uses a watermark — it simply applies the differences between versions.
  </Accordion>

  <Accordion title="Does StarTree support Delta Column Mapping?">
    Yes, We now support column mapping with both NAME and ID mode.
  </Accordion>
</AccordionGroup>

Built with [Mintlify](https://mintlify.com).
