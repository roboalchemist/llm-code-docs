# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.dataplex_data_scan.dataset.md

---
title: Dataplex DataScan
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Dataplex DataScan
---

# Dataplex DataScan

Dataplex DataScan in Google Cloud is a managed service that allows you to run data quality and profiling scans on your datasets. It helps you assess the structure, validity, and consistency of your data across different storage systems. By automating checks and generating insights, DataScan supports governance, compliance, and data reliability efforts within Dataplex-managed environments.

```
gcp.dataplex_data_scan
```

## Fields

| Title                     | ID   | Type          | Data Type                                                                                                                                                                                                                                                 | Description |
| ------------------------- | ---- | ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                      | core | string        |
| ancestors                 | core | array<string> |
| create_time               | core | timestamp     | Output only. The time when the scan was created.                                                                                                                                                                                                          |
| data                      | core | json          | Required. The data source for DataScan.                                                                                                                                                                                                                   |
| data_discovery_result     | core | json          | Output only. The result of a data discovery scan.                                                                                                                                                                                                         |
| data_discovery_spec       | core | json          | Settings for a data discovery scan.                                                                                                                                                                                                                       |
| data_documentation_result | core | json          | Output only. The result of a data documentation scan.                                                                                                                                                                                                     |
| data_documentation_spec   | core | json          | Settings for a data documentation scan.                                                                                                                                                                                                                   |
| data_profile_result       | core | json          | Output only. The result of a data profile scan.                                                                                                                                                                                                           |
| data_profile_spec         | core | json          | Settings for a data profile scan.                                                                                                                                                                                                                         |
| data_quality_result       | core | json          | Output only. The result of a data quality scan.                                                                                                                                                                                                           |
| data_quality_spec         | core | json          | Settings for a data quality scan.                                                                                                                                                                                                                         |
| datadog_display_name      | core | string        |
| description               | core | string        | Optional. Description of the scan. Must be between 1-1024 characters.                                                                                                                                                                                     |
| execution_spec            | core | json          | Optional. DataScan execution settings.If not specified, the fields in it will use their default values.                                                                                                                                                   |
| execution_status          | core | json          | Output only. Status of the data scan execution.                                                                                                                                                                                                           |
| gcp_display_name          | core | string        | Optional. User friendly display name. Must be between 1-256 characters.                                                                                                                                                                                   |
| labels                    | core | array<string> | Optional. User-defined labels for the scan.                                                                                                                                                                                                               |
| name                      | core | string        | Output only. Identifier. The relative resource name of the scan, of the form: projects/{project}/locations/{location_id}/dataScans/{datascan_id}, where project refers to a project_id or project_number and location_id refers to a Google Cloud region. |
| organization_id           | core | string        |
| parent                    | core | string        |
| project_id                | core | string        |
| project_number            | core | string        |
| region_id                 | core | string        |
| resource_name             | core | string        |
| state                     | core | string        | Output only. Current state of the DataScan.                                                                                                                                                                                                               |
| tags                      | core | hstore_csv    |
| type                      | core | string        | Output only. The type of DataScan.                                                                                                                                                                                                                        |
| uid                       | core | string        | Output only. System generated globally unique ID for the scan. This ID will be different if the scan is deleted and re-created with the same name.                                                                                                        |
| update_time               | core | timestamp     | Output only. The time when the scan was last updated.                                                                                                                                                                                                     |
| zone_id                   | core | string        |
