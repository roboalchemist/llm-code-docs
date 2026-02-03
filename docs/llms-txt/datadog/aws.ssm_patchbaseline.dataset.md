# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.ssm_patchbaseline.dataset.md

---
title: Systems Manager Patch Baseline
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Systems Manager Patch Baseline
---

# Systems Manager Patch Baseline

This table represents the Systems Manager Patch Baseline resource from Amazon Web Services.

```
aws.ssm_patchbaseline
```

## Fields

| Title                                        | ID   | Type          | Data Type                                                                                                                                                                                                                                                                                           | Description |
| -------------------------------------------- | ---- | ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                                         | core | string        |
| account_id                                   | core | string        |
| approval_rules                               | core | json          | A set of rules used to include patches in the baseline.                                                                                                                                                                                                                                             |
| approved_patches                             | core | array<string> | A list of explicitly approved patches for the baseline.                                                                                                                                                                                                                                             |
| approved_patches_compliance_level            | core | string        | Returns the specified compliance severity level for approved patches in the patch baseline.                                                                                                                                                                                                         |
| approved_patches_enable_non_security         | core | bool          | Indicates whether the list of approved patches includes non-security updates that should be applied to the managed nodes. The default value is <code>false</code>. Applies to Linux managed nodes only.                                                                                             |
| available_security_updates_compliance_status | core | string        | Indicates the compliance status of managed nodes for which security-related patches are available but were not approved. This preference is specified when the <code>CreatePatchBaseline</code> or <code>UpdatePatchBaseline</code> commands are run. Applies to Windows Server managed nodes only. |
| baseline_id                                  | core | string        | The ID of the retrieved patch baseline.                                                                                                                                                                                                                                                             |
| created_date                                 | core | timestamp     | The date the patch baseline was created.                                                                                                                                                                                                                                                            |
| description                                  | core | string        | A description of the patch baseline.                                                                                                                                                                                                                                                                |
| global_filters                               | core | json          | A set of global filters used to exclude patches from the baseline.                                                                                                                                                                                                                                  |
| modified_date                                | core | timestamp     | The date the patch baseline was last modified.                                                                                                                                                                                                                                                      |
| name                                         | core | string        | The name of the patch baseline.                                                                                                                                                                                                                                                                     |
| operating_system                             | core | string        | Returns the operating system specified for the patch baseline.                                                                                                                                                                                                                                      |
| patch_groups                                 | core | array<string> | Patch groups included in the patch baseline.                                                                                                                                                                                                                                                        |
| rejected_patches                             | core | array<string> | A list of explicitly rejected patches for the baseline.                                                                                                                                                                                                                                             |
| rejected_patches_action                      | core | string        | The action specified to take on patches included in the <code>RejectedPatches</code> list. A patch can be allowed only if it is a dependency of another package, or blocked entirely along with packages that include it as a dependency.                                                           |
| sources                                      | core | json          | Information about the patches to use to update the managed nodes, including target operating systems and source repositories. Applies to Linux managed nodes only.                                                                                                                                  |
| tags                                         | core | hstore_csv    |
