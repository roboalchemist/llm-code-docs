# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.osis_pipeline_blueprint.dataset.md

---
title: OpenSearch Ingestion Pipeline Blueprint
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > DDSQL Reference > Data Directory > OpenSearch Ingestion Pipeline
  Blueprint
---

# OpenSearch Ingestion Pipeline Blueprint

An OpenSearch Ingestion Pipeline Blueprint in AWS provides a predefined configuration template that helps you set up data ingestion pipelines for Amazon OpenSearch Service. It defines the structure and components needed to collect, process, and deliver data into OpenSearch, making it easier to build pipelines without starting from scratch.

```
aws.osis_pipeline_blueprint
```

## Fields

| Title      | ID   | Type       | Data Type                               | Description |
| ---------- | ---- | ---------- | --------------------------------------- | ----------- |
| _key       | core | string     |
| account_id | core | string     |
| blueprint  | core | json       | The requested blueprint in YAML format. |
| format     | core | string     | The format of the blueprint.            |
| tags       | core | hstore_csv |
