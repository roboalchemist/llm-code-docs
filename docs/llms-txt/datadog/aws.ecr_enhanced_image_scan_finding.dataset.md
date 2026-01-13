# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.ecr_enhanced_image_scan_finding.dataset.md

---
title: ECR Enhanced Image Scan Finding
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > ECR Enhanced Image Scan Finding
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.ecr_enhanced_image_scan_finding.dataset/index.html
---

# ECR Enhanced Image Scan Finding

This table represents the ECR Enhanced Image Scan Finding resource from Amazon Web Services.

```
aws.ecr_enhanced_image_scan_finding
```

## Fields

| Title                         | ID   | Type      | Data Type                                                               | Description |
| ----------------------------- | ---- | --------- | ----------------------------------------------------------------------- | ----------- |
| _key                          | core | string    |
| account_id                    | core | string    |
| aws_account_id                | core | string    | The Amazon Web Services account ID associated with the image.           |
| description                   | core | string    | The description of the finding.                                         |
| finding_arn                   | core | string    | The Amazon Resource Number (ARN) of the finding.                        |
| first_observed_at             | core | timestamp | The date and time that the finding was first observed.                  |
| image_id                      | core | string    |
| last_observed_at              | core | timestamp | The date and time that the finding was last observed.                   |
| package_vulnerability_details | core | json      | An object that contains the details of a package vulnerability finding. |
| remediation                   | core | json      | An object that contains the details about how to remediate a finding.   |
| score                         | core | float64   | The Amazon Inspector score given to the finding.                        |
| score_details                 | core | json      | An object that contains details of the Amazon Inspector score.          |
| severity                      | core | string    | The severity of the finding.                                            |
| status                        | core | string    | The status of the finding.                                              |
| tags                          | core | hstore    |
| title                         | core | string    | The title of the finding.                                               |
| type                          | core | string    | The type of the finding.                                                |
| updated_at                    | core | timestamp | The date and time the finding was last updated at.                      |
