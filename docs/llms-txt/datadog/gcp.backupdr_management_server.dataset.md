# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.backupdr_management_server.dataset.md

---
title: Backup and DR Management Server
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Backup and DR Management Server
---

# Backup and DR Management Server

Backup and DR Management Server in Google Cloud is a managed service that provides centralized backup, disaster recovery, and data protection for workloads running in GCP and on-premises environments. It automates backup scheduling, retention, and recovery operations, ensuring business continuity and compliance.

```
gcp.backupdr_management_server
```

## Fields

| Title                                     | ID   | Type          | Data Type                                                                                                                                                                                                                                                                                             | Description |
| ----------------------------------------- | ---- | ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                                      | core | string        |
| ancestors                                 | core | array<string> |
| ba_proxy_uri                              | core | array<string> | Output only. The hostname or ip address of the exposed AGM endpoints, used by BAs to connect to BA proxy.                                                                                                                                                                                             |
| create_time                               | core | timestamp     | Output only. The time when the instance was created.                                                                                                                                                                                                                                                  |
| datadog_display_name                      | core | string        |
| description                               | core | string        | Optional. The description of the ManagementServer instance (2048 characters or less).                                                                                                                                                                                                                 |
| etag                                      | core | string        | Optional. Server specified ETag for the ManagementServer resource to prevent simultaneous updates from overwiting each other.                                                                                                                                                                         |
| labels                                    | core | array<string> | Optional. Resource labels to represent user provided metadata. Labels currently defined: 1. migrate_from_go= If set to true, the MS is created in migration ready mode.                                                                                                                               |
| management_uri                            | core | json          | Output only. The hostname or ip address of the exposed AGM endpoints, used by clients to connect to AGM/RD graphical user interface and APIs.                                                                                                                                                         |
| name                                      | core | string        | Output only. Identifier. The resource name.                                                                                                                                                                                                                                                           |
| networks                                  | core | json          | Optional. VPC networks to which the ManagementServer instance is connected. For this version, only a single network is supported. This field is optional if MS is created without PSA                                                                                                                 |
| oauth2_client_id                          | core | string        | Output only. The OAuth 2.0 client id is required to make API calls to the BackupDR instance API of this ManagementServer. This is the value that should be provided in the 'aud' field of the OIDC ID Token (see openid specification https://openid.net/specs/openid-connect-core-1_0.html#IDToken). |
| organization_id                           | core | string        |
| parent                                    | core | string        |
| project_id                                | core | string        |
| project_number                            | core | string        |
| region_id                                 | core | string        |
| resource_name                             | core | string        |
| satisfies_pzi                             | core | bool          | Output only. Reserved for future use.                                                                                                                                                                                                                                                                 |
| satisfies_pzs                             | core | bool          | Output only. Reserved for future use.                                                                                                                                                                                                                                                                 |
| state                                     | core | string        | Output only. The ManagementServer state.                                                                                                                                                                                                                                                              |
| tags                                      | core | hstore_csv    |
| type                                      | core | string        | Optional. The type of the ManagementServer resource.                                                                                                                                                                                                                                                  |
| update_time                               | core | timestamp     | Output only. The time when the instance was updated.                                                                                                                                                                                                                                                  |
| workforce_identity_based_management_uri   | core | json          | Output only. The hostnames of the exposed AGM endpoints for both types of user i.e. 1p and 3p, used to connect AGM/RM UI.                                                                                                                                                                             |
| workforce_identity_based_oauth2_client_id | core | json          | Output only. The OAuth client IDs for both types of user i.e. 1p and 3p.                                                                                                                                                                                                                              |
| zone_id                                   | core | string        |
