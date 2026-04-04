# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.clouddeploy_automation_run.dataset.md

---
title: Cloud Deploy AutomationRun
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Cloud Deploy AutomationRun
---

# Cloud Deploy AutomationRun

Cloud Deploy AutomationRun in Google Cloud represents an automated execution instance within a Cloud Deploy pipeline. It manages and tracks the lifecycle of automated deployment tasks, such as triggering rollouts, running pre- or post-deployment actions, and integrating with other CI/CD tools. It helps ensure consistent, repeatable, and auditable deployment processes across environments.

```
gcp.clouddeploy_automation_run
```

## Fields

| Title                           | ID   | Type          | Data Type                                                                                                                                                                                                                                             | Description |
| ------------------------------- | ---- | ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                            | core | string        |
| advance_rollout_operation       | core | json          | Output only. Advances a rollout to the next phase.                                                                                                                                                                                                    |
| ancestors                       | core | array<string> |
| automation_id                   | core | string        | Output only. The ID of the automation that initiated the operation.                                                                                                                                                                                   |
| automation_snapshot             | core | json          | Output only. Snapshot of the Automation taken at AutomationRun creation time.                                                                                                                                                                         |
| create_time                     | core | timestamp     | Output only. Time at which the `AutomationRun` was created.                                                                                                                                                                                           |
| datadog_display_name            | core | string        |
| etag                            | core | string        | Output only. The weak etag of the `AutomationRun` resource. This checksum is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding. |
| expire_time                     | core | timestamp     | Output only. Time the `AutomationRun` expires. An `AutomationRun` expires after 14 days from its creation date.                                                                                                                                       |
| labels                          | core | array<string> |
| name                            | core | string        | Output only. Name of the `AutomationRun`. Format is `projects/{project}/locations/{location}/deliveryPipelines/{delivery_pipeline}/automationRuns/{automation_run}`.                                                                                  |
| organization_id                 | core | string        |
| parent                          | core | string        |
| policy_violation                | core | json          | Output only. Contains information about what policies prevented the `AutomationRun` from proceeding.                                                                                                                                                  |
| project_id                      | core | string        |
| project_number                  | core | string        |
| promote_release_operation       | core | json          | Output only. Promotes a release to a specified 'Target'.                                                                                                                                                                                              |
| region_id                       | core | string        |
| repair_rollout_operation        | core | json          | Output only. Repairs a failed 'Rollout'.                                                                                                                                                                                                              |
| resource_name                   | core | string        |
| rule_id                         | core | string        | Output only. The ID of the automation rule that initiated the operation.                                                                                                                                                                              |
| service_account                 | core | string        | Output only. Email address of the user-managed IAM service account that performs the operations against Cloud Deploy resources.                                                                                                                       |
| state                           | core | string        | Output only. Current state of the `AutomationRun`.                                                                                                                                                                                                    |
| state_description               | core | string        | Output only. Explains the current state of the `AutomationRun`. Present only when an explanation is needed.                                                                                                                                           |
| tags                            | core | hstore_csv    |
| target_id                       | core | string        | Output only. The ID of the source target that initiates the `AutomationRun`. The value of this field is the last segment of a target name.                                                                                                            |
| timed_promote_release_operation | core | json          | Output only. Promotes a release to a specified 'Target' as defined in a Timed Promote Release rule.                                                                                                                                                   |
| update_time                     | core | timestamp     | Output only. Time at which the automationRun was updated.                                                                                                                                                                                             |
| wait_until_time                 | core | timestamp     | Output only. Earliest time the `AutomationRun` will attempt to resume. Wait-time is configured by `wait` in automation rule.                                                                                                                          |
| zone_id                         | core | string        |
