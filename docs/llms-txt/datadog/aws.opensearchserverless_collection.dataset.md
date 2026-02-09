# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.opensearchserverless_collection.dataset.md

---
title: OpenSearch Serverless Collection
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > OpenSearch Serverless Collection
---

# OpenSearch Serverless Collection

This table represents the OpenSearch Serverless Collection resource from Amazon Web Services.

```
aws.opensearchserverless_collection
```

## Fields

| Title                    | ID   | Type       | Data Type                          | Description |
| ------------------------ | ---- | ---------- | ---------------------------------- | ----------- |
| _key                     | core | string     |
| account_id               | core | string     |
| collection_details       | core | json       | Details about each collection.     |
| collection_error_details | core | json       | Error information for the request. |
| tags                     | core | hstore_csv |
