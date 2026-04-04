# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.orgpolicy_policy.dataset.md

---
title: Organization Policy
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Organization Policy
---

# Organization Policy

Organization Policy in Google Cloud lets administrators define and enforce constraints across resources in an organization. It provides centralized control over configurations, ensuring compliance with security, governance, and operational standards. Policies can restrict or allow specific behaviors, such as resource locations, service usage, or configuration settings, helping maintain consistency and prevent misconfigurations across projects.

```
gcp.orgpolicy_policy
```

## Fields

| Title                | ID   | Type          | Data Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Description |
| -------------------- | ---- | ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                 | core | string        |
| alternate            | core | json          | Deprecated.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ancestors            | core | array<string> |
| datadog_display_name | core | string        |
| dry_run_spec         | core | json          | Dry-run policy. Audit-only policy, can be used to monitor how the policy would have impacted the existing and future resources if it's enforced.                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| etag                 | core | string        | Optional. An opaque tag indicating the current state of the policy, used for concurrency control. This 'etag' is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding.                                                                                                                                                                                                                                                                                                          |
| labels               | core | array<string> |
| name                 | core | string        | Immutable. The resource name of the policy. Must be one of the following forms, where `constraint_name` is the name of the constraint which this policy configures: * `projects/{project_number}/policies/{constraint_name}` * `folders/{folder_id}/policies/{constraint_name}` * `organizations/{organization_id}/policies/{constraint_name}` For example, `projects/123/policies/compute.disableSerialPortAccess`. Note: `projects/{project_id}/policies/{constraint_name}` is also an acceptable name for API requests, but responses will return the name using the equivalent project number. |
| organization_id      | core | string        |
| parent               | core | string        |
| project_id           | core | string        |
| project_number       | core | string        |
| region_id            | core | string        |
| resource_name        | core | string        |
| spec                 | core | json          | Basic information about the organization policy.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| tags                 | core | hstore_csv    |
| zone_id              | core | string        |
