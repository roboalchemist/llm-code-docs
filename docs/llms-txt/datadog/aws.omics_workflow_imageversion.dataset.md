# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.omics_workflow_imageversion.dataset.md

---
title: Omics Workflow Imageversion
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Omics Workflow Imageversion
---

# Omics Workflow Imageversion

This table represents the omics_workflow_imageversion resource from Amazon Web Services.

```
aws.omics_workflow_imageversion
```

## Fields

| Title                    | ID   | Type       | Data Type | Description |
| ------------------------ | ---- | ---------- | --------- | ----------- |
| _key                     | core | string     |
| accelerators             | core | string     |
| account_id               | core | string     |
| arn                      | core | string     |
| creation_time            | core | timestamp  |
| definition               | core | string     |
| description              | core | string     |
| digest                   | core | string     |
| engine                   | core | string     |
| main                     | core | string     |
| metadata                 | core | hstore     |
| parameter_template       | core | string     |
| status                   | core | string     |
| status_message           | core | string     |
| storage_capacity         | core | int64      |
| storage_type             | core | string     |
| tags                     | core | hstore_csv |
| type                     | core | string     |
| uuid                     | core | string     |
| version_name             | core | string     |
| workflow_bucket_owner_id | core | string     |
| workflow_id              | core | string     |
