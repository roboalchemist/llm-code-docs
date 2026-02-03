# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.inspector2_coverage.dataset.md

---
title: Inspector Coverage
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Inspector Coverage
---

# Inspector Coverage

This table represents the Inspector Coverage resource from Amazon Web Services.

```
aws.inspector2_coverage
```

## Fields

| Title             | ID   | Type       | Data Type                                                            | Description |
| ----------------- | ---- | ---------- | -------------------------------------------------------------------- | ----------- |
| _key              | core | string     |
| account_id        | core | string     |
| coverage_arn      | core | string     |
| last_scanned_at   | core | timestamp  | The date and time the resource was last checked for vulnerabilities. |
| resource_id       | core | string     | The ID of the covered resource.                                      |
| resource_metadata | core | json       | An object that contains details about the metadata.                  |
| resource_type     | core | string     | The type of the covered resource.                                    |
| scan_mode         | core | string     | The scan method that is applied to the instance.                     |
| scan_status       | core | json       | The status of the scan covering the resource.                        |
| scan_type         | core | string     | The Amazon Inspector scan type covering the resource.                |
| tags              | core | hstore_csv |
