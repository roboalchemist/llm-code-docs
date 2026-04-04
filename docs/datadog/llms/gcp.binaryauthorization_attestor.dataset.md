# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.binaryauthorization_attestor.dataset.md

---
title: Binary Authorization Attestor
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Binary Authorization Attestor
---

# Binary Authorization Attestor

A Binary Authorization Attestor in Google Cloud is a security resource that defines and manages trusted authorities for container image verification. It ensures that only images signed by approved attestors can be deployed to Google Kubernetes Engine or Cloud Run. This helps enforce policy compliance and prevents unauthorized or unverified software from running in production environments.

```
gcp.binaryauthorization_attestor
```

## Fields

| Title                   | ID   | Type          | Data Type                                                                                                                                                                                        | Description |
| ----------------------- | ---- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| _key                    | core | string        |
| ancestors               | core | array<string> |
| datadog_display_name    | core | string        |
| description             | core | string        | Optional. A descriptive comment. This field may be updated. The field may be displayed in chooser dialogs.                                                                                       |
| etag                    | core | string        | Optional. A checksum, returned by the server, that can be sent on update requests to ensure the attestor has an up-to-date value before attempting to update it. See https://google.aip.dev/154. |
| labels                  | core | array<string> |
| name                    | core | string        | Required. The resource name, in the format: `projects/*/attestors/*`. This field may not be updated.                                                                                             |
| organization_id         | core | string        |
| parent                  | core | string        |
| project_id              | core | string        |
| project_number          | core | string        |
| region_id               | core | string        |
| resource_name           | core | string        |
| tags                    | core | hstore_csv    |
| update_time             | core | timestamp     | Output only. Time when the attestor was last updated.                                                                                                                                            |
| user_owned_grafeas_note | core | json          | This specifies how an attestation will be read, and how it will be used during policy enforcement.                                                                                               |
| zone_id                 | core | string        |
