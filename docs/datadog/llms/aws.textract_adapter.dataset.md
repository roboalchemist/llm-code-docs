# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.textract_adapter.dataset.md

---
title: Textract Adapter
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Textract Adapter
---

# Textract Adapter

Textract Adapter in AWS is part of the Amazon Textract service, which extracts text, forms, and tables from documents. The GetAdapterResponse shape represents the structured output returned when retrieving details about a Textract adapter, which is a configuration that customizes how Textract processes and interprets documents. It provides metadata and response information that helps integrate Textract's document analysis into applications more effectively.

```
aws.textract_adapter
```

## Fields

| Title         | ID   | Type          | Data Type                                                                     | Description |
| ------------- | ---- | ------------- | ----------------------------------------------------------------------------- | ----------- |
| _key          | core | string        |
| account_id    | core | string        |
| adapter_id    | core | string        | A string identifying the adapter that information has been retrieved for.     |
| adapter_name  | core | string        | The name of the requested adapter.                                            |
| auto_update   | core | string        | Binary value indicating if the adapter is being automatically updated or not. |
| creation_time | core | timestamp     | The date and time the requested adapter was created at.                       |
| description   | core | string        | The description for the requested adapter.                                    |
| feature_types | core | array<string> | List of the targeted feature types for the requested adapter.                 |
| tags          | core | hstore_csv    |
