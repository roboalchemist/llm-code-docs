# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.osconfig_os_policy_assignment_report.dataset.md

---
title: OS Policy Assignment Report
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > OS Policy Assignment Report
---

# OS Policy Assignment Report

An OS Policy Assignment Report in Google Cloud provides detailed compliance information for virtual machine instances based on assigned OS policies. It shows whether each instance meets the configuration and compliance requirements defined in the policy, including package installations, file settings, and system configurations. This helps administrators monitor and maintain consistent OS configurations across their fleet.

```
gcp.osconfig_os_policy_assignment_report
```

## Fields

| Title                 | ID   | Type          | Data Type                                                                                                                                                                                                                                                                                                                                                                  | Description |
| --------------------- | ---- | ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                  | core | string        |
| ancestors             | core | array<string> |
| datadog_display_name  | core | string        |
| instance              | core | string        | The Compute Engine VM instance name.                                                                                                                                                                                                                                                                                                                                       |
| labels                | core | array<string> |
| last_run_id           | core | string        | Unique identifier of the last attempted run to apply the OS policies associated with this assignment on the VM. This ID is logged by the OS Config agent while applying the OS policies associated with this assignment on the VM. NOTE: If the service is unable to successfully connect to the agent for this run, then this id will not be available in the agent logs. |
| name                  | core | string        | The `OSPolicyAssignmentReport` API resource name. Format: `projects/{project_number}/locations/{location}/instances/{instance_id}/osPolicyAssignments/{os_policy_assignment_id}/report`                                                                                                                                                                                    |
| organization_id       | core | string        |
| os_policy_assignment  | core | string        | Reference to the `OSPolicyAssignment` API resource that the `OSPolicy` belongs to. Format: `projects/{project_number}/locations/{location}/osPolicyAssignments/{os_policy_assignment_id@revision_id}`                                                                                                                                                                      |
| os_policy_compliances | core | json          | Compliance data for each `OSPolicy` that is applied to the VM.                                                                                                                                                                                                                                                                                                             |
| parent                | core | string        |
| project_id            | core | string        |
| project_number        | core | string        |
| region_id             | core | string        |
| resource_name         | core | string        |
| tags                  | core | hstore_csv    |
| update_time           | core | timestamp     | Timestamp for when the report was last generated.                                                                                                                                                                                                                                                                                                                          |
| zone_id               | core | string        |
