# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.bedrock_provisioned_model_throughput.dataset.md

---
title: Bedrock Provisioned Model Throughput
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Bedrock Provisioned Model Throughput
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.bedrock_provisioned_model_throughput.dataset/index.html
---

# Bedrock Provisioned Model Throughput

This table represents the Bedrock Provisioned Model Throughput resource from Amazon Web Services.

```
aws.bedrock_provisioned_model_throughput
```

## Fields

| Title                      | ID   | Type      | Data Type                                                                                                                                                                                                      | Description |
| -------------------------- | ---- | --------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                       | core | string    |
| account_id                 | core | string    |
| commitment_duration        | core | string    | The duration for which the Provisioned Throughput was committed.                                                                                                                                               |
| commitment_expiration_time | core | timestamp | The timestamp for when the commitment term of the Provisioned Throughput expires.                                                                                                                              |
| creation_time              | core | timestamp | The time that the Provisioned Throughput was created.                                                                                                                                                          |
| desired_model_arn          | core | string    | The Amazon Resource Name (ARN) of the model requested to be associated to this Provisioned Throughput. This value differs from the <code>modelArn</code> if updating hasn't completed.                         |
| desired_model_units        | core | int64     | The number of model units that was requested to be allocated to the Provisioned Throughput.                                                                                                                    |
| foundation_model_arn       | core | string    | The Amazon Resource Name (ARN) of the base model for which the Provisioned Throughput was created, or of the base model that the custom model for which the Provisioned Throughput was created was customized. |
| last_modified_time         | core | timestamp | The time that the Provisioned Throughput was last modified.                                                                                                                                                    |
| model_arn                  | core | string    | The Amazon Resource Name (ARN) of the model associated with the Provisioned Throughput.                                                                                                                        |
| model_units                | core | int64     | The number of model units allocated to the Provisioned Throughput.                                                                                                                                             |
| provisioned_model_arn      | core | string    | The Amazon Resource Name (ARN) of the Provisioned Throughput.                                                                                                                                                  |
| provisioned_model_name     | core | string    | The name of the Provisioned Throughput.                                                                                                                                                                        |
| status                     | core | string    | The status of the Provisioned Throughput.                                                                                                                                                                      |
| tags                       | core | hstore    |
