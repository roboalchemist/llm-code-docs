# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.codeguru_security_scanname.dataset.md

---
title: CodeGuru Security Scanname
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > CodeGuru Security Scanname
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.codeguru_security_scanname.dataset/index.html
---

# CodeGuru Security Scanname

This table represents the CodeGuru Security Scanname resource from Amazon Web Services.

```
aws.codeguru_security_scanname
```

## Fields

| Title               | ID   | Type      | Data Type                                                                                                                                                                                                                                                                    | Description |
| ------------------- | ---- | --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                | core | string    |
| account_id          | core | string    |
| analysis_type       | core | string    | The type of analysis CodeGuru Security performed in the scan, either <code>Security</code> or <code>All</code>. The <code>Security</code> type only generates findings related to security. The <code>All</code> type generates both security findings and quality findings. |
| created_at          | core | timestamp | The time the scan was created.                                                                                                                                                                                                                                               |
| error_message       | core | string    | Details about the error that causes a scan to fail to be retrieved.                                                                                                                                                                                                          |
| number_of_revisions | core | int64     | The number of times a scan has been re-run on a revised resource.                                                                                                                                                                                                            |
| run_id              | core | string    | UUID that identifies the individual scan run.                                                                                                                                                                                                                                |
| scan_name           | core | string    | The name of the scan.                                                                                                                                                                                                                                                        |
| scan_name_arn       | core | string    | The ARN for the scan name.                                                                                                                                                                                                                                                   |
| scan_state          | core | string    | The current state of the scan. Returns either <code>InProgress</code>, <code>Successful</code>, or <code>Failed</code>.                                                                                                                                                      |
| tags                | core | hstore    |
| updated_at          | core | timestamp | The time when the scan was last updated. Only available for <code>STANDARD</code> scan types.                                                                                                                                                                                |
