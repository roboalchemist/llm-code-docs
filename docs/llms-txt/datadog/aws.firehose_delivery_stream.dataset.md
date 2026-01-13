# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.firehose_delivery_stream.dataset.md

---
title: Kinesis Data Firehose Delivery Stream
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > DDSQL Reference > Data Directory > Kinesis Data Firehose Delivery
  Stream
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.firehose_delivery_stream.dataset/index.html
---

# Kinesis Data Firehose Delivery Stream

Kinesis Data Firehose Delivery Stream is a fully managed service in AWS that reliably loads real-time streaming data into destinations such as Amazon S3, Amazon Redshift, Amazon OpenSearch Service, or third-party services. It automatically scales to match data throughput, handles data transformation and compression, and requires no ongoing administration.

```
aws.firehose_delivery_stream
```

## Fields

| Title                                    | ID   | Type      | Data Type                                                                                                                                                                                                                                                                | Description |
| ---------------------------------------- | ---- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| _key                                     | core | string    |
| account_id                               | core | string    |
| create_timestamp                         | core | timestamp | The date and time that the Firehose stream was created.                                                                                                                                                                                                                  |
| delivery_stream_arn                      | core | string    | The Amazon Resource Name (ARN) of the Firehose stream. For more information, see Amazon Resource Names (ARNs) and Amazon Web Services Service Namespaces.                                                                                                                |
| delivery_stream_encryption_configuration | core | json      | Indicates the server-side encryption (SSE) status for the Firehose stream.                                                                                                                                                                                               |
| delivery_stream_name                     | core | string    | The name of the Firehose stream.                                                                                                                                                                                                                                         |
| delivery_stream_status                   | core | string    | The status of the Firehose stream. If the status of a Firehose stream is CREATING_FAILED, this status doesn't change, and you can't invoke CreateDeliveryStream again on it. However, you can invoke the DeleteDeliveryStream operation to delete it.                    |
| delivery_stream_type                     | core | string    | The Firehose stream type. This can be one of the following values: DirectPut: Provider applications access the Firehose stream directly. KinesisStreamAsSource: The Firehose stream uses a Kinesis data stream as a source.                                              |
| destinations                             | core | json      | The destinations.                                                                                                                                                                                                                                                        |
| failure_description                      | core | json      | Provides details in case one of the following operations fails due to an error related to KMS: CreateDeliveryStream, DeleteDeliveryStream, StartDeliveryStreamEncryption, StopDeliveryStreamEncryption.                                                                  |
| has_more_destinations                    | core | bool      | Indicates whether there are more destinations available to list.                                                                                                                                                                                                         |
| last_update_timestamp                    | core | timestamp | The date and time that the Firehose stream was last updated.                                                                                                                                                                                                             |
| tags                                     | core | hstore    |
| version_id                               | core | string    | Each time the destination is updated for a Firehose stream, the version ID is changed, and the current version ID is required when updating the destination. This is so that the service knows it is applying the changes to the correct version of the delivery stream. |
