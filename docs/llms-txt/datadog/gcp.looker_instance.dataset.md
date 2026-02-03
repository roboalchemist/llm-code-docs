# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.looker_instance.dataset.md

---
title: Looker Instance
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Looker Instance
---

# Looker Instance

A Looker Instance in Google Cloud is a managed business intelligence and data analytics platform that allows users to explore, analyze, and visualize data from various sources. It provides a centralized environment for creating dashboards, reports, and data models, enabling teams to make data-driven decisions. The service integrates with BigQuery and other databases, offering secure access control, scalability, and collaboration features.

```
gcp.looker_instance
```

## Fields

| Title                        | ID   | Type          | Data Type                                                                                                                                                                                                                     | Description |
| ---------------------------- | ---- | ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                         | core | string        |
| admin_settings               | core | json          | Looker Instance Admin settings.                                                                                                                                                                                               |
| ancestors                    | core | array<string> |
| class_type                   | core | string        | Optional. Storage class of the instance.                                                                                                                                                                                      |
| consumer_network             | core | string        | Network name in the consumer project. Format: `projects/{project}/global/networks/{network}`. Note that the consumer network may be in a different GCP project than the consumer project that is hosting the Looker Instance. |
| create_time                  | core | timestamp     | Output only. The time when the Looker instance provisioning was first requested.                                                                                                                                              |
| custom_domain                | core | json          | Custom domain configuration for the instance.                                                                                                                                                                                 |
| datadog_display_name         | core | string        |
| deny_maintenance_period      | core | json          | Maintenance denial period for this instance.                                                                                                                                                                                  |
| egress_public_ip             | core | string        | Output only. Public Egress IP (IPv4).                                                                                                                                                                                         |
| encryption_config            | core | json          | Encryption configuration (CMEK). Only set if CMEK has been enabled on the instance.                                                                                                                                           |
| fips_enabled                 | core | bool          | Optional. Whether FIPS is enabled on the Looker instance.                                                                                                                                                                     |
| gemini_enabled               | core | bool          | Optional. Whether Gemini feature is enabled on the Looker instance or not.                                                                                                                                                    |
| ingress_private_ip           | core | string        | Output only. Private Ingress IP (IPv4).                                                                                                                                                                                       |
| ingress_public_ip            | core | string        | Output only. Public Ingress IP (IPv4).                                                                                                                                                                                        |
| labels                       | core | array<string> |
| last_deny_maintenance_period | core | json          | Output only. Last computed maintenance denial period for this instance.                                                                                                                                                       |
| linked_lsp_project_number    | core | int64         | Optional. Linked Google Cloud Project Number for Looker Studio Pro.                                                                                                                                                           |
| looker_uri                   | core | string        | Output only. Looker instance URI which can be used to access the Looker Instance UI.                                                                                                                                          |
| looker_version               | core | string        | Output only. The Looker version that the instance is using.                                                                                                                                                                   |
| maintenance_schedule         | core | json          | Maintenance schedule for this instance.                                                                                                                                                                                       |
| maintenance_window           | core | json          | Maintenance window for this instance.                                                                                                                                                                                         |
| name                         | core | string        | Output only. Format: `projects/{project}/locations/{location}/instances/{instance}`.                                                                                                                                          |
| oauth_config                 | core | json          | Looker instance OAuth login settings.                                                                                                                                                                                         |
| organization_id              | core | string        |
| parent                       | core | string        |
| platform_edition             | core | string        | Platform edition.                                                                                                                                                                                                             |
| private_ip_enabled           | core | bool          | Whether private IP is enabled on the Looker instance.                                                                                                                                                                         |
| project_id                   | core | string        |
| project_number               | core | string        |
| psc_config                   | core | json          | Optional. PSC configuration. Used when `psc_enabled` is true.                                                                                                                                                                 |
| psc_enabled                  | core | bool          | Optional. Whether to use Private Service Connect (PSC) for private IP connectivity. If true, neither `public_ip_enabled` nor `private_ip_enabled` can be true.                                                                |
| public_ip_enabled            | core | bool          | Whether public IP is enabled on the Looker instance.                                                                                                                                                                          |
| region_id                    | core | string        |
| reserved_range               | core | string        | Name of a reserved IP address range within the Instance.consumer_network, to be used for private services access connection. May or may not be specified in a create request.                                                 |
| resource_name                | core | string        |
| satisfies_pzi                | core | bool          | Output only. Reserved for future use.                                                                                                                                                                                         |
| satisfies_pzs                | core | bool          | Output only. Reserved for future use.                                                                                                                                                                                         |
| state                        | core | string        | Output only. The state of the instance.                                                                                                                                                                                       |
| tags                         | core | hstore_csv    |
| update_time                  | core | timestamp     | Output only. The time when the Looker instance was last updated.                                                                                                                                                              |
| user_metadata                | core | json          | Optional. User metadata.                                                                                                                                                                                                      |
| zone_id                      | core | string        |
