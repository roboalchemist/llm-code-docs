# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.glue_registry.dataset.md

---
title: Glue Registry
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Glue Registry
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.glue_registry.dataset/index.html
---

# Glue Registry

AWS Glue Registry is a centralized repository for managing and storing schema definitions used in data streams and event-driven applications. It helps ensure data consistency by allowing producers and consumers to share and validate schemas. This reduces data compatibility issues, improves governance, and simplifies integration across services like Amazon Kinesis, Kafka, and AWS Glue.

```
aws.glue_registry
```

## Fields

| Title         | ID   | Type   | Data Type                                       | Description |
| ------------- | ---- | ------ | ----------------------------------------------- | ----------- |
| _key          | core | string |
| account_id    | core | string |
| created_time  | core | string | The data the registry was created.              |
| description   | core | string | A description of the registry.                  |
| registry_arn  | core | string | The Amazon Resource Name (ARN) of the registry. |
| registry_name | core | string | The name of the registry.                       |
| status        | core | string | The status of the registry.                     |
| tags          | core | hstore |
| updated_time  | core | string | The date the registry was updated.              |
