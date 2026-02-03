# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.frauddetector_model_version.dataset.md

---
title: Fraud Detector Model Version
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Fraud Detector Model Version
---

# Fraud Detector Model Version

This table represents the Fraud Detector Model Version resource from Amazon Web Services.

```
aws.frauddetector_model_version
```

## Fields

| Title                  | ID   | Type       | Data Type                                                                                                                                                           | Description |
| ---------------------- | ---- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                   | core | string     |
| account_id             | core | string     |
| arn                    | core | string     | The model version ARN.                                                                                                                                              |
| created_time           | core | string     | The timestamp when the model was created.                                                                                                                           |
| external_events_detail | core | json       | The external events data details. This will be populated if the <code>trainingDataSource</code> for the model version is specified as <code>EXTERNAL_EVENTS</code>. |
| ingested_events_detail | core | json       | The ingested events data details. This will be populated if the <code>trainingDataSource</code> for the model version is specified as <code>INGESTED_EVENTS</code>. |
| last_updated_time      | core | string     | The timestamp when the model was last updated.                                                                                                                      |
| model_id               | core | string     | The model ID.                                                                                                                                                       |
| model_type             | core | string     | The model type.                                                                                                                                                     |
| model_version_number   | core | string     | The model version number.                                                                                                                                           |
| status                 | core | string     | The status of the model version.                                                                                                                                    |
| tags                   | core | hstore_csv |
| training_data_schema   | core | json       | The training data schema.                                                                                                                                           |
| training_data_source   | core | string     | The model version training data source.                                                                                                                             |
| training_result        | core | json       | The training results.                                                                                                                                               |
| training_result_v2     | core | json       | The training result details. The details include the relative importance of the variables.                                                                          |
