# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.osconfig_os_policy_assignment.dataset.md

---
title: OS policy assignment
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > OS policy assignment
---

# OS policy assignment

An OS policy assignment in Google Cloud is a configuration resource that defines and enforces operating system policies across virtual machine instances. It allows administrators to specify compliance rules, package installations, and configuration settings to ensure systems meet organizational standards. The assignments can target specific VM groups or projects and are automatically applied and monitored for compliance.

```
gcp.osconfig_os_policy_assignment
```

## Fields

| Title                | ID   | Type          | Data Type                                                                                                                                                                                                                                                                                                      | Description |
| -------------------- | ---- | ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                 | core | string        |
| ancestors            | core | array<string> |
| baseline             | core | bool          | Output only. Indicates that this revision has been successfully rolled out in this zone and new VMs will be assigned OS policies from this revision. For a given OS policy assignment, there is only one revision with a value of `true` for this field.                                                       |
| datadog_display_name | core | string        |
| deleted              | core | bool          | Output only. Indicates that this revision deletes the OS policy assignment.                                                                                                                                                                                                                                    |
| description          | core | string        | OS policy assignment description. Length of the description is limited to 1024 characters.                                                                                                                                                                                                                     |
| etag                 | core | string        | The etag for this OS policy assignment. If this is provided on update, it must match the server's etag.                                                                                                                                                                                                        |
| instance_filter      | core | json          | Required. Filter to select VMs.                                                                                                                                                                                                                                                                                |
| labels               | core | array<string> |
| name                 | core | string        | Resource name. Format: `projects/{project_number}/locations/{location}/osPolicyAssignments/{os_policy_assignment_id}` This field is ignored when you create an OS policy assignment.                                                                                                                           |
| organization_id      | core | string        |
| os_policies          | core | json          | Required. List of OS policies to be applied to the VMs.                                                                                                                                                                                                                                                        |
| parent               | core | string        |
| project_id           | core | string        |
| project_number       | core | string        |
| reconciling          | core | bool          | Output only. Indicates that reconciliation is in progress for the revision. This value is `true` when the `rollout_state` is one of: * IN_PROGRESS * CANCELLING                                                                                                                                                |
| region_id            | core | string        |
| resource_name        | core | string        |
| revision_create_time | core | timestamp     | Output only. The timestamp that the revision was created.                                                                                                                                                                                                                                                      |
| revision_id          | core | string        | Output only. The assignment revision ID A new revision is committed whenever a rollout is triggered for a OS policy assignment                                                                                                                                                                                 |
| rollout              | core | json          | Required. Rollout to deploy the OS policy assignment. A rollout is triggered in the following situations: 1) OSPolicyAssignment is created. 2) OSPolicyAssignment is updated and the update contains changes to one of the following fields: - instance_filter - os_policies 3) OSPolicyAssignment is deleted. |
| rollout_state        | core | string        | Output only. OS policy assignment rollout state                                                                                                                                                                                                                                                                |
| tags                 | core | hstore_csv    |
| uid                  | core | string        | Output only. Server generated unique id for the OS policy assignment resource.                                                                                                                                                                                                                                 |
| zone_id              | core | string        |
