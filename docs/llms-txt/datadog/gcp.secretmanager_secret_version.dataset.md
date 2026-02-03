# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.secretmanager_secret_version.dataset.md

---
title: Secret Manager Secret Version
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Secret Manager Secret Version
---

# Secret Manager Secret Version

A Secret Manager Secret Version in Google Cloud securely stores a specific version of a secret, such as an API key or password. Each version is immutable once created, allowing safe rotation and rollback of secrets. Applications can access the latest or a specific version as needed, ensuring controlled and auditable secret management.

```
gcp.secretmanager_secret_version
```

## Fields

| Title                             | ID   | Type          | Data Type                                                                                                                                                                                                                                                                                                                                             | Description |
| --------------------------------- | ---- | ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                              | core | string        |
| ancestors                         | core | array<string> |
| client_specified_payload_checksum | core | bool          | Output only. True if payload checksum specified in SecretPayload object has been received by SecretManagerService on SecretManagerService.AddSecretVersion.                                                                                                                                                                                           |
| create_time                       | core | timestamp     | Output only. The time at which the SecretVersion was created.                                                                                                                                                                                                                                                                                         |
| customer_managed_encryption       | core | json          | Output only. The customer-managed encryption status of the SecretVersion. Only populated if customer-managed encryption is used and Secret is a regionalized secret.                                                                                                                                                                                  |
| datadog_display_name              | core | string        |
| destroy_time                      | core | timestamp     | Output only. The time this SecretVersion was destroyed. Only present if state is DESTROYED.                                                                                                                                                                                                                                                           |
| etag                              | core | string        | Output only. Etag of the currently stored SecretVersion.                                                                                                                                                                                                                                                                                              |
| labels                            | core | array<string> |
| name                              | core | string        | Output only. The resource name of the SecretVersion in the format `projects/*/secrets/*/versions/*`. SecretVersion IDs in a Secret start at 1 and are incremented for each subsequent version of the secret.                                                                                                                                          |
| organization_id                   | core | string        |
| parent                            | core | string        |
| project_id                        | core | string        |
| project_number                    | core | string        |
| region_id                         | core | string        |
| replication_status                | core | json          | The replication status of the SecretVersion.                                                                                                                                                                                                                                                                                                          |
| resource_name                     | core | string        |
| scheduled_destroy_time            | core | timestamp     | Optional. Output only. Scheduled destroy time for secret version. This is a part of the Delayed secret version destroy feature. For a Secret with a valid version destroy TTL, when a secert version is destroyed, version is moved to disabled state and it is scheduled for destruction Version is destroyed only after the scheduled_destroy_time. |
| state                             | core | string        | Output only. The current state of the SecretVersion.                                                                                                                                                                                                                                                                                                  |
| tags                              | core | hstore_csv    |
| zone_id                           | core | string        |
