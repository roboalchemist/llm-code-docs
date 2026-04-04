# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.identitytoolkit_default_supported_idp_config.dataset.md

---
title: Identity Platform Default Supported Idp Config
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > DDSQL Reference > Data Directory > Identity Platform Default Supported
  Idp Config
---

# Identity Platform Default Supported Idp Config

This resource represents the default configuration for supported identity providers in Google Cloud Identity Platform. It defines how external identity providers such as Google, Facebook, or others are integrated for authentication. The configuration includes default settings that control provider behavior, credentials, and connection parameters used by applications to enable secure user sign-in through third-party identity services.

```gdscript3
gcp.identitytoolkit_default_supported_idp_config
```

## Fields

| Title                | ID   | Type          | Data Type                                                                                                                            | Description |
| -------------------- | ---- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| _key                 | core | string        |
| ancestors            | core | array<string> |
| apple_sign_in_config | core | json          | Additional config for Apple-based projects.                                                                                          |
| client_id            | core | string        | OAuth client ID.                                                                                                                     |
| client_secret        | core | string        | OAuth client secret.                                                                                                                 |
| datadog_display_name | core | string        |
| enabled              | core | bool          | True if allows the user to sign in with the provider.                                                                                |
| labels               | core | array<string> |
| name                 | core | string        | The name of the DefaultSupportedIdpConfig resource, for example: "projects/my-awesome-project/defaultSupportedIdpConfigs/google.com" |
| organization_id      | core | string        |
| parent               | core | string        |
| project_id           | core | string        |
| project_number       | core | string        |
| region_id            | core | string        |
| resource_name        | core | string        |
| tags                 | core | hstore_csv    |
| zone_id              | core | string        |
