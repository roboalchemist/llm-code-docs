# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.panorama_package.dataset.md

---
title: Panorama Package
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Panorama Package
---

# Panorama Package

An AWS Panorama Package is a containerized application that runs on AWS Panorama devices. It includes computer vision models and business logic that can be deployed to analyze video streams locally without sending data to the cloud. Packages are versioned, managed, and deployed through AWS Panorama, enabling edge-based machine learning for real-time insights.

```
aws.panorama_package
```

## Fields

| Title                       | ID   | Type          | Data Type                                               | Description |
| --------------------------- | ---- | ------------- | ------------------------------------------------------- | ----------- |
| _key                        | core | string        |
| account_id                  | core | string        |
| arn                         | core | string        | The package's ARN.                                      |
| created_time                | core | timestamp     | When the package was created.                           |
| package_id                  | core | string        | The package's ID.                                       |
| package_name                | core | string        | The package's name.                                     |
| read_access_principal_arns  | core | array<string> | ARNs of accounts that have read access to the package.  |
| storage_location            | core | json          | The package's storage location.                         |
| tags                        | core | hstore_csv    |
| write_access_principal_arns | core | array<string> | ARNs of accounts that have write access to the package. |
