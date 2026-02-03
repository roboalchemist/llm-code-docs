# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.oracledatabase_cloud_exadata_infrastructure.dataset.md

---
title: Oracle Cloud Exadata Infrastructure
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Oracle Cloud Exadata Infrastructure
---

# Oracle Cloud Exadata Infrastructure

This table represents the Oracle Cloud Exadata Infrastructure resource from Google Cloud Platform.

```
gcp.oracledatabase_cloud_exadata_infrastructure
```

## Fields

| Title                | ID   | Type          | Data Type                                                                                                                                                                     | Description |
| -------------------- | ---- | ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                 | core | string        |
| ancestors            | core | array<string> |
| create_time          | core | timestamp     | Output only. The date and time that the Exadata Infrastructure was created.                                                                                                   |
| datadog_display_name | core | string        |
| entitlement_id       | core | string        | Output only. Entitlement ID of the private offer against which this infrastructure resource is provisioned.                                                                   |
| gcp_display_name     | core | string        | Optional. User friendly name for this resource.                                                                                                                               |
| gcp_oracle_zone      | core | string        | Optional. The GCP Oracle zone where Oracle Exadata Infrastructure is hosted. Example: us-east4-b-r2. If not specified, the system will pick a zone based on availability.     |
| labels               | core | array<string> | Optional. Labels or tags associated with the resource.                                                                                                                        |
| name                 | core | string        | Identifier. The name of the Exadata Infrastructure resource with the format: projects/{project}/locations/{region}/cloudExadataInfrastructures/{cloud_exadata_infrastructure} |
| organization_id      | core | string        |
| parent               | core | string        |
| project_id           | core | string        |
| project_number       | core | string        |
| properties           | core | json          | Optional. Various properties of the infra.                                                                                                                                    |
| region_id            | core | string        |
| resource_name        | core | string        |
| tags                 | core | hstore_csv    |
| zone_id              | core | string        |
