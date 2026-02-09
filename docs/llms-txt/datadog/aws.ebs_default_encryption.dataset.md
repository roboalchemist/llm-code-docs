# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.ebs_default_encryption.dataset.md

---
title: EBS Default Encryption
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > EBS Default Encryption
---

# EBS Default Encryption

This table represents the EBS Default Encryption resource from Amazon Web Services.

```
aws.ebs_default_encryption
```

## Fields

| Title                     | ID   | Type       | Data Type                                           | Description |
| ------------------------- | ---- | ---------- | --------------------------------------------------- | ----------- |
| _key                      | core | string     |
| account_id                | core | string     |
| ebs_encryption_by_default | core | bool       | Indicates whether encryption by default is enabled. |
| sse_type                  | core | string     | Reserved for future use.                            |
| tags                      | core | hstore_csv |
