# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.gkemulticloud_azure_client.dataset.md

---
title: AzureClient
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > AzureClient
---

# AzureClient

This table represents the AzureClient resource from Google Cloud Platform.

```
gcp.gkemulticloud_azure_client
```

## Fields

| Title                | ID   | Type          | Data Type                                                                                                                                                                                                                                                                                                                                                                                                                                         | Description |
| -------------------- | ---- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                 | core | string        |
| ancestors            | core | array<string> |
| annotations          | core | hstore        | Optional. Annotations on the resource. This field has the same restrictions as Kubernetes annotations. The total size of all keys and values combined is limited to 256k. Keys can have 2 segments: prefix (optional) and name (required), separated by a slash (/). Prefix must be a DNS subdomain. Name must be 63 characters or less, begin and end with alphanumerics, with dashes (-), underscores (_), dots (.), and alphanumerics between. |
| application_id       | core | string        | Required. The Azure Active Directory Application ID.                                                                                                                                                                                                                                                                                                                                                                                              |
| create_time          | core | timestamp     | Output only. The time at which this resource was created.                                                                                                                                                                                                                                                                                                                                                                                         |
| datadog_display_name | core | string        |
| labels               | core | array<string> |
| name                 | core | string        | The name of this resource. `AzureClient` resource names are formatted as `projects//locations//azureClients/`. See [Resource Names](https://cloud.google.com/apis/design/resource_names) for more details on Google Cloud resource names.                                                                                                                                                                                                         |
| organization_id      | core | string        |
| parent               | core | string        |
| pem_certificate      | core | string        | Output only. The PEM encoded x509 certificate.                                                                                                                                                                                                                                                                                                                                                                                                    |
| project_id           | core | string        |
| project_number       | core | string        |
| reconciling          | core | bool          | Output only. If set, there are currently pending changes to the client.                                                                                                                                                                                                                                                                                                                                                                           |
| region_id            | core | string        |
| resource_name        | core | string        |
| tags                 | core | hstore_csv    |
| tenant_id            | core | string        | Required. The Azure Active Directory Tenant ID.                                                                                                                                                                                                                                                                                                                                                                                                   |
| uid                  | core | string        | Output only. A globally unique identifier for the client.                                                                                                                                                                                                                                                                                                                                                                                         |
| update_time          | core | timestamp     | Output only. The time at which this client was last updated.                                                                                                                                                                                                                                                                                                                                                                                      |
| zone_id              | core | string        |
