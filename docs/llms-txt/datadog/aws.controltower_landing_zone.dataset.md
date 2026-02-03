# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.controltower_landing_zone.dataset.md

---
title: Control Tower Landing Zone
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Control Tower Landing Zone
---

# Control Tower Landing Zone

AWS Control Tower Landing Zone is a pre-configured, secure, multi-account environment that follows AWS best practices. It automates the setup of foundational services such as identity, logging, and security guardrails, enabling organizations to quickly establish a governed cloud environment.

```
aws.controltower_landing_zone
```

## Fields

| Title                    | ID   | Type       | Data Type                                                                                | Description |
| ------------------------ | ---- | ---------- | ---------------------------------------------------------------------------------------- | ----------- |
| _key                     | core | string     |
| account_id               | core | string     |
| arn                      | core | string     | The ARN of the landing zone.                                                             |
| drift_status             | core | json       | The drift status of the landing zone.                                                    |
| latest_available_version | core | string     | The latest available version of the landing zone.                                        |
| manifest                 | core | json       | The landing zone manifest JSON text file that specifies the landing zone configurations. |
| status                   | core | string     | The landing zone deployment status. One of ACTIVE, PROCESSING, FAILED.                   |
| tags                     | core | hstore_csv |
| version                  | core | string     | The landing zone's current deployed version.                                             |
