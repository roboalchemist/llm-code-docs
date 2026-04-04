# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.integrations_auth_config.dataset.md

---
title: Integration Auth Config
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Integration Auth Config
---

# Integration Auth Config

Integration Auth Config in Google Cloud is a configuration resource that defines authentication settings for integrations and connectors. It manages credentials, tokens, and identity mappings required for secure communication between Google Cloud services and external systems. This resource helps standardize and centralize authentication across integration workflows.

```
gcp.integrations_auth_config
```

## Fields

| Title                        | ID   | Type          | Data Type                                                                                                                                                                   | Description |
| ---------------------------- | ---- | ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                         | core | string        |
| ancestors                    | core | array<string> |
| certificate_id               | core | string        | Certificate id for client certificate                                                                                                                                       |
| create_time                  | core | timestamp     | Output only. The timestamp when the auth config is created.                                                                                                                 |
| creator_email                | core | string        | The creator's email address. Generated based on the End User Credentials/LOAS role of the user making the call.                                                             |
| credential_type              | core | string        | Required. Credential type of the encrypted credential.                                                                                                                      |
| datadog_display_name         | core | string        |
| decrypted_credential         | core | json          | Raw auth credentials.                                                                                                                                                       |
| description                  | core | string        | Optional. A description of the auth config.                                                                                                                                 |
| expiry_notification_duration | core | array<string> | Optional. User can define the time to receive notification after which the auth config becomes invalid. Support up to 30 days. Support granularity in hours.                |
| gcp_display_name             | core | string        | Required. The name of the auth config.                                                                                                                                      |
| labels                       | core | array<string> |
| last_modifier_email          | core | string        | The last modifier's email address. Generated based on the End User Credentials/LOAS role of the user making the call.                                                       |
| name                         | core | string        | Resource name of the auth config. For more information, see Manage authentication profiles. projects/{project}/locations/{location}/authConfigs/{authConfig}.               |
| organization_id              | core | string        |
| override_valid_time          | core | timestamp     | Optional. User provided expiry time to override. For the example of Salesforce, username/password credentials can be valid for 6 months depending on the instance settings. |
| parent                       | core | string        |
| project_id                   | core | string        |
| project_number               | core | string        |
| reason                       | core | string        | Output only. The reason / details of the current status.                                                                                                                    |
| region_id                    | core | string        |
| resource_name                | core | string        |
| state                        | core | string        | Output only. The status of the auth config.                                                                                                                                 |
| tags                         | core | hstore_csv    |
| update_time                  | core | timestamp     | Output only. The timestamp when the auth config is modified.                                                                                                                |
| valid_time                   | core | timestamp     | Optional. The time until the auth config is valid. Empty or max value is considered the auth config won't expire.                                                           |
| visibility                   | core | string        | Optional. The visibility of the auth config.                                                                                                                                |
| zone_id                      | core | string        |
