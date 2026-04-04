# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.ecr_image_scan_finding.dataset.md

---
title: ECR Image Scan Finding
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > ECR Image Scan Finding
---

# ECR Image Scan Finding

This table represents the ECR Image Scan Finding resource from Amazon Web Services.

```
aws.ecr_image_scan_finding
```

## Fields

| Title       | ID   | Type       | Data Type                                                                   | Description |
| ----------- | ---- | ---------- | --------------------------------------------------------------------------- | ----------- |
| _key        | core | string     |
| account_id  | core | string     |
| attributes  | core | json       | A collection of attributes of the host from which the finding is generated. |
| description | core | string     | The description of the finding.                                             |
| image_id    | core | string     |
| name        | core | string     | The name associated with the finding, usually a CVE number.                 |
| severity    | core | string     | The finding severity.                                                       |
| tags        | core | hstore_csv |
| uri         | core | string     | A link containing additional details about the security vulnerability.      |
