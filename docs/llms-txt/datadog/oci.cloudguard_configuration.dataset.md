# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/oci/oci.cloudguard_configuration.dataset.md

---
title: Cloud Guard Configuration
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Cloud Guard Configuration
---

# Cloud Guard Configuration

This table represents the Cloud Guard Configuration resource from Oracle Cloud Infrastructure.

```
oci.cloudguard_configuration
```

## Fields

| Title                  | ID   | Type       | Data Type                                                                                                                                                                                                                                  | Description |
| ---------------------- | ---- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| _key                   | core | string     |
| cloud_account_id       | core | string     | The identifier of the related cloud account. The concept of an account might have different names in different cloud providers. AWS is calling it account, GCP calls it project and Azure uses the term subscription.                      |
| cloud_account_name     | core | string     | The name of the account this resource belongs to.                                                                                                                                                                                          |
| cloud_provider         | core | string     | The name of the cloud provider.                                                                                                                                                                                                            |
| cloud_tags             | core | hstore     |
| compartment_id         | core | string     | Compartment containing the resource. Used for Access control, logical grouping, and authorization boundaries.                                                                                                                              |
| created_at             | core | timestamp  | Time when the resource has been created.                                                                                                                                                                                                   |
| freeform_tags          | core | hstore     | The value to assign to the freeform_tags property of this Instance.                                                                                                                                                                        |
| name                   | core | string     | The name of this resource.                                                                                                                                                                                                                 |
| region_id              | core | string     | The region this resource resides within.                                                                                                                                                                                                   |
| reporting_region       | core | string     | The value to assign to the reporting_region property of this Configuration.                                                                                                                                                                |
| resource_type          | core | string     | The name of the resource type.                                                                                                                                                                                                             |
| self_manage_resources  | core | bool       | The value to assign to the self_manage_resources property of this Configuration.                                                                                                                                                           |
| service_configurations | core | json       | The value to assign to the service_configurations property of this Configuration.                                                                                                                                                          |
| status                 | core | string     | The value to assign to the status property of this Configuration. Allowed values for this property are: "ENABLED", "DISABLED", 'UNKNOWN_ENUM_VALUE'. Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'. |
| tags                   | core | hstore_csv |
| time_created           | core | timestamp  | The value to assign to the time_created property of this Instance.                                                                                                                                                                         |
| updated_at             | core | timestamp  | Time when the resource has been updated the last time.                                                                                                                                                                                     |
| zone_id                | core | string     | The zone this resource resides within.                                                                                                                                                                                                     |
