# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.binaryauthorization_policy.dataset.md

---
title: Binary Authorization Policy
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Binary Authorization Policy
---

# Binary Authorization Policy

Binary Authorization Policy is a Google Cloud resource that defines rules for container image deployment security. It ensures that only trusted and verified container images are allowed to run on Google Kubernetes Engine or Cloud Run. The policy enforces signature verification and attestation checks before deployment, helping maintain compliance and prevent unauthorized code execution.

```
gcp.binaryauthorization_policy
```

## Fields

| Title                         | ID   | Type          | Data Type                                                                                                                                                                                                                                                                             | Description |
| ----------------------------- | ---- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                          | core | string        |
| admission_whitelist_patterns  | core | json          | Optional. Admission policy allowlisting. A matching admission request will always be permitted. This feature is typically used to exclude Google or third-party infrastructure images from Binary Authorization policies.                                                             |
| ancestors                     | core | array<string> |
| datadog_display_name          | core | string        |
| default_admission_rule        | core | json          | Required. Default admission rule for a cluster without a per-cluster, per- kubernetes-service-account, or per-istio-service-identity admission rule.                                                                                                                                  |
| description                   | core | string        | Optional. A descriptive comment.                                                                                                                                                                                                                                                      |
| etag                          | core | string        | Optional. A checksum, returned by the server, that can be sent on update requests to ensure the policy has an up-to-date value before attempting to update it. See https://google.aip.dev/154.                                                                                        |
| global_policy_evaluation_mode | core | string        | Optional. Controls the evaluation of a Google-maintained global admission policy for common system-level images. Images not covered by the global policy will be subject to the project admission policy. This setting has no effect when specified inside a global admission policy. |
| labels                        | core | array<string> |
| name                          | core | string        | Output only. The resource name, in the format `projects/*/policy`. There is at most one policy per project.                                                                                                                                                                           |
| organization_id               | core | string        |
| parent                        | core | string        |
| project_id                    | core | string        |
| project_number                | core | string        |
| region_id                     | core | string        |
| resource_name                 | core | string        |
| tags                          | core | hstore_csv    |
| update_time                   | core | timestamp     | Output only. Time when the policy was last updated.                                                                                                                                                                                                                                   |
| zone_id                       | core | string        |
