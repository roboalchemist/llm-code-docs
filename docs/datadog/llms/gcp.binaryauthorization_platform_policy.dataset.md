# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.binaryauthorization_platform_policy.dataset.md

---
title: Binary Authorization Platform Policy
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Binary Authorization Platform Policy
---

# Binary Authorization Platform Policy

Binary Authorization Platform Policy in Google Cloud is a security control that enforces signature-based validation of container images before deployment. It ensures that only trusted and verified images, signed by authorized parties, can be executed on GKE or Cloud Run environments. This helps maintain compliance, prevent unauthorized code execution, and strengthen the overall software supply chain security.

```
gcp.binaryauthorization_platform_policy
```

## Fields

| Title                | ID   | Type          | Data Type                                                                                                                                | Description |
| -------------------- | ---- | ------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                 | core | string        |
| ancestors            | core | array<string> |
| datadog_display_name | core | string        |
| description          | core | string        | Optional. A description comment about the policy.                                                                                        |
| etag                 | core | string        | Optional. Used to prevent updating the policy when another request has updated it since it was retrieved.                                |
| gke_policy           | core | json          | Optional. GKE platform-specific policy.                                                                                                  |
| labels               | core | array<string> |
| name                 | core | string        | Output only. The relative resource name of the Binary Authorization platform policy, in the form of `projects/*/platforms/*/policies/*`. |
| organization_id      | core | string        |
| parent               | core | string        |
| project_id           | core | string        |
| project_number       | core | string        |
| region_id            | core | string        |
| resource_name        | core | string        |
| tags                 | core | hstore_csv    |
| update_time          | core | timestamp     | Output only. Time when the policy was last updated.                                                                                      |
| zone_id              | core | string        |
