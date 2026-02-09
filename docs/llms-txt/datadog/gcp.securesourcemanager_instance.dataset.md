# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.securesourcemanager_instance.dataset.md

---
title: Secure Source Manager Instance
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Secure Source Manager Instance
---

# Secure Source Manager Instance

A Secure Source Manager Instance in Google Cloud is a fully managed, private Git repository service designed for secure source code management. It provides enterprise-grade security, access control, and integration with Google Cloud services. The instance allows teams to host, manage, and collaborate on code within a controlled environment, ensuring compliance and data protection.

```
gcp.securesourcemanager_instance
```

## Fields

| Title                                | ID   | Type          | Data Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Description |
| ------------------------------------ | ---- | ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                                 | core | string        |
| ancestors                            | core | array<string> |
| create_time                          | core | timestamp     | Output only. Create timestamp.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| datadog_display_name                 | core | string        |
| host_config                          | core | json          | Output only. A list of hostnames for this instance.                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| labels                               | core | array<string> | Optional. Labels as key value pairs. Keys and values can contain only lowercase letters, numeric characters, underscores, and dashes. For more information, see [Requirements for labels](https://cloud.google.com/resource-manager/docs/best-practices-labels#label_encoding).                                                                                                                                                                                                                                              |
| name                                 | core | string        | Optional. A unique identifier for an instance. The name should be of the format: `projects/{project_number}/locations/{location_id}/instances/{instance_id}` `project_number`: Maps to a unique int64 id assigned to each project. `location_id`: Refers to the region where the instance will be deployed. Since Secure Source Manager is a regional service, it must be one of the valid GCP regions. `instance_id`: User provided name for the instance, must be unique for a project_number and location_id combination. |
| organization_id                      | core | string        |
| parent                               | core | string        |
| private_config                       | core | json          | Optional. Private settings for private instance.                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| project_id                           | core | string        |
| project_number                       | core | string        |
| region_id                            | core | string        |
| resource_name                        | core | string        |
| state                                | core | string        | Output only. Current state of the instance.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| state_note                           | core | string        | Output only. An optional field providing information about the current instance state.                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| tags                                 | core | hstore_csv    |
| update_time                          | core | timestamp     | Output only. Update timestamp.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| workforce_identity_federation_config | core | json          | Optional. Configuration for Workforce Identity Federation to support third party identity provider. If unset, defaults to the Google OIDC IdP.                                                                                                                                                                                                                                                                                                                                                                               |
| zone_id                              | core | string        |
