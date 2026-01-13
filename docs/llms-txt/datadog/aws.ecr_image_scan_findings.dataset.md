# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.ecr_image_scan_findings.dataset.md

---
title: ECR Image Scan Findings
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > ECR Image Scan Findings
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.ecr_image_scan_findings.dataset/index.html
---

# ECR Image Scan Findings

This table represents the ECR Image Scan Findings resource from Amazon Web Services.

```
aws.ecr_image_scan_findings
```

## Fields

| Title                           | ID   | Type      | Data Type                                              | Description |
| ------------------------------- | ---- | --------- | ------------------------------------------------------ | ----------- |
| _key                            | core | string    |
| account_id                      | core | string    |
| critical                        | core | int64     |
| high                            | core | int64     |
| image_id                        | core | string    |
| image_scan_completed_at         | core | timestamp | The time of the last completed image scan.             |
| informational                   | core | int64     |
| low                             | core | int64     |
| medium                          | core | int64     |
| tags                            | core | hstore    |
| undefined                       | core | int64     |
| vulnerability_source_updated_at | core | timestamp | The time when the vulnerability data was last scanned. |
