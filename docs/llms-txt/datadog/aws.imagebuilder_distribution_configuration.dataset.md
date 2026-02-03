# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.imagebuilder_distribution_configuration.dataset.md

---
title: EC2 Image Builder Distribution Configuration
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > DDSQL Reference > Data Directory > EC2 Image Builder Distribution
  Configuration
---

# EC2 Image Builder Distribution Configuration

EC2 Image Builder Distribution Configuration in AWS defines how machine images are distributed after they are created. It specifies target regions, accounts, and settings for sharing or copying images, ensuring consistent deployment across environments. This helps automate image lifecycle management and simplifies multi-region or multi-account distribution.

```
aws.imagebuilder_distribution_configuration
```

## Fields

| Title                      | ID   | Type       | Data Type                                             | Description |
| -------------------------- | ---- | ---------- | ----------------------------------------------------- | ----------- |
| _key                       | core | string     |
| account_id                 | core | string     |
| distribution_configuration | core | json       | The distribution configuration object.                |
| request_id                 | core | string     | The request ID that uniquely identifies this request. |
| tags                       | core | hstore_csv |
