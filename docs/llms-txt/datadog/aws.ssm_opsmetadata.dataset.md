# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.ssm_opsmetadata.dataset.md

---
title: Systems Manager Ops Metadata
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Systems Manager Ops Metadata
---

# Systems Manager Ops Metadata

This table represents the Systems Manager Ops Metadata resource from Amazon Web Services.

```
aws.ssm_opsmetadata
```

## Fields

| Title              | ID   | Type       | Data Type                                                         | Description |
| ------------------ | ---- | ---------- | ----------------------------------------------------------------- | ----------- |
| _key               | core | string     |
| account_id         | core | string     |
| creation_date      | core | timestamp  | The date the OpsMetadata objects was created.                     |
| last_modified_date | core | timestamp  | The date the OpsMetadata object was last updated.                 |
| last_modified_user | core | string     | The user name who last updated the OpsMetadata object.            |
| ops_metadata_arn   | core | string     | The Amazon Resource Name (ARN) of the OpsMetadata Object or blob. |
| resource_id        | core | string     | The ID of the Application Manager application.                    |
| tags               | core | hstore_csv |
