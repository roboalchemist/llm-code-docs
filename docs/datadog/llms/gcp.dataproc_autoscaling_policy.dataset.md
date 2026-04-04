# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.dataproc_autoscaling_policy.dataset.md

---
title: Dataproc Autoscaling Policy
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Dataproc Autoscaling Policy
---

# Dataproc Autoscaling Policy

A Dataproc Autoscaling Policy in Google Cloud automatically adjusts the number of worker nodes in a Dataproc cluster based on workload demands. It helps optimize resource usage and cost by scaling up during high demand and scaling down when idle. The policy defines rules for scaling behavior, such as thresholds and cooldown periods.

```
gcp.dataproc_autoscaling_policy
```

## Fields

| Title                   | ID   | Type          | Data Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Description |
| ----------------------- | ---- | ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                    | core | string        |
| ancestors               | core | array<string> |
| basic_algorithm         | core | json          |
| datadog_display_name    | core | string        |
| id                      | core | string        | Required. The policy id.The id must contain only letters (a-z, A-Z), numbers (0-9), underscores (_), and hyphens (-). Cannot begin or end with underscore or hyphen. Must consist of between 3 and 50 characters.                                                                                                                                                                                                                                                                            |
| labels                  | core | array<string> | Optional. The labels to associate with this autoscaling policy. Label keys must contain 1 to 63 characters, and must conform to RFC 1035 (https://www.ietf.org/rfc/rfc1035.txt). Label values may be empty, but, if present, must contain 1 to 63 characters, and must conform to RFC 1035 (https://www.ietf.org/rfc/rfc1035.txt). No more than 32 labels can be associated with an autoscaling policy.                                                                                      |
| name                    | core | string        | Output only. The "resource name" of the autoscaling policy, as described in https://cloud.google.com/apis/design/resource_names. For projects.regions.autoscalingPolicies, the resource name of the policy has the following format: projects/{project_id}/regions/{region}/autoscalingPolicies/{policy_id} For projects.locations.autoscalingPolicies, the resource name of the policy has the following format: projects/{project_id}/locations/{location}/autoscalingPolicies/{policy_id} |
| organization_id         | core | string        |
| parent                  | core | string        |
| project_id              | core | string        |
| project_number          | core | string        |
| region_id               | core | string        |
| resource_name           | core | string        |
| secondary_worker_config | core | json          | Optional. Describes how the autoscaler will operate for secondary workers.                                                                                                                                                                                                                                                                                                                                                                                                                   |
| tags                    | core | hstore_csv    |
| worker_config           | core | json          | Required. Describes how the autoscaler will operate for primary workers.                                                                                                                                                                                                                                                                                                                                                                                                                     |
| zone_id                 | core | string        |
