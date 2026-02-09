# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.lookoutequipment_dataset.dataset.md

---
title: Lookout for Equipment Dataset
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Lookout for Equipment Dataset
---

# Lookout for Equipment Dataset

Lookout for Equipment Dataset in AWS is a resource that defines the data used to train and evaluate machine learning models for equipment monitoring. It stores metadata about the dataset, including its name, schema, status, and data sources. This dataset is essential for building predictive maintenance solutions, as it provides the historical sensor and operational data needed for anomaly detection and failure prediction.

```
aws.lookoutequipment_dataset
```

## Fields

| Title                         | ID   | Type       | Data Type                                                                                                                                                                                                                                                                                                | Description |
| ----------------------------- | ---- | ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                          | core | string     |
| account_id                    | core | string     |
| created_at                    | core | timestamp  | Specifies the time the dataset was created in Lookout for Equipment.                                                                                                                                                                                                                                     |
| data_end_time                 | core | timestamp  | Indicates the latest timestamp corresponding to data that was successfully ingested during the most recent ingestion of this particular dataset.                                                                                                                                                         |
| data_quality_summary          | core | json       | Gives statistics associated with the given dataset for the latest successful associated ingestion job id. These statistics primarily relate to quantifying incorrect data such as MissingCompleteSensorData, MissingSensorData, UnsupportedDateFormats, InsufficientSensorData, and DuplicateTimeStamps. |
| data_start_time               | core | timestamp  | Indicates the earliest timestamp corresponding to data that was successfully ingested during the most recent ingestion of this particular dataset.                                                                                                                                                       |
| dataset_arn                   | core | string     | The Amazon Resource Name (ARN) of the dataset being described.                                                                                                                                                                                                                                           |
| dataset_name                  | core | string     | The name of the dataset being described.                                                                                                                                                                                                                                                                 |
| ingested_files_summary        | core | json       | IngestedFilesSummary associated with the given dataset for the latest successful associated ingestion job id.                                                                                                                                                                                            |
| ingestion_input_configuration | core | json       | Specifies the S3 location configuration for the data input for the data ingestion job.                                                                                                                                                                                                                   |
| last_updated_at               | core | timestamp  | Specifies the time the dataset was last updated, if it was.                                                                                                                                                                                                                                              |
| role_arn                      | core | string     | The Amazon Resource Name (ARN) of the IAM role that you are using for this the data ingestion job.                                                                                                                                                                                                       |
| schema                        | core | string     | A JSON description of the data that is in each time series dataset, including names, column names, and data types.                                                                                                                                                                                       |
| server_side_kms_key_id        | core | string     | Provides the identifier of the KMS key used to encrypt dataset data by Amazon Lookout for Equipment.                                                                                                                                                                                                     |
| source_dataset_arn            | core | string     | The Amazon Resource Name (ARN) of the source dataset from which the current data being described was imported from.                                                                                                                                                                                      |
| status                        | core | string     | Indicates the status of the dataset.                                                                                                                                                                                                                                                                     |
| tags                          | core | hstore_csv |
