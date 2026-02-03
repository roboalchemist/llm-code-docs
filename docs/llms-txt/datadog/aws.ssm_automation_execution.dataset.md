# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.ssm_automation_execution.dataset.md

---
title: Systems Manager Automation Execution
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Systems Manager Automation Execution
---

# Systems Manager Automation Execution

Systems Manager Automation Execution in AWS represents the running instance of an automation workflow defined in Systems Manager. It provides details about the execution status, progress, and results of automation documents (runbooks) that automate operational tasks such as patching, configuration updates, or resource management.

```
aws.ssm_automation_execution
```

## Fields

| Title                          | ID   | Type          | Data Type                                                                                                                                                                                                                          | Description |
| ------------------------------ | ---- | ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                           | core | string        |
| account_id                     | core | string        |
| alarm_configuration            | core | json          | The details for the CloudWatch alarm applied to your automation.                                                                                                                                                                   |
| association_id                 | core | string        | The ID of a State Manager association used in the Automation operation.                                                                                                                                                            |
| automation_execution_id        | core | string        | The execution ID.                                                                                                                                                                                                                  |
| automation_execution_status    | core | string        | The execution status of the Automation.                                                                                                                                                                                            |
| automation_subtype             | core | string        | The subtype of the Automation operation. Currently, the only supported value is ChangeRequest.                                                                                                                                     |
| change_request_name            | core | string        | The name of the Change Manager change request.                                                                                                                                                                                     |
| current_action                 | core | string        | The action of the step that is currently running.                                                                                                                                                                                  |
| current_step_name              | core | string        | The name of the step that is currently running.                                                                                                                                                                                    |
| document_name                  | core | string        | The name of the Automation runbook used during the execution.                                                                                                                                                                      |
| document_version               | core | string        | The version of the document to use during execution.                                                                                                                                                                               |
| executed_by                    | core | string        | The Amazon Resource Name (ARN) of the user who ran the automation.                                                                                                                                                                 |
| execution_end_time             | core | timestamp     | The time the execution finished.                                                                                                                                                                                                   |
| execution_start_time           | core | timestamp     | The time the execution started.                                                                                                                                                                                                    |
| failure_message                | core | string        | A message describing why an execution has failed, if the status is set to Failed.                                                                                                                                                  |
| max_concurrency                | core | string        | The MaxConcurrency value specified by the user when the execution started.                                                                                                                                                         |
| max_errors                     | core | string        | The MaxErrors value specified by the user when the execution started.                                                                                                                                                              |
| mode                           | core | string        | The automation execution mode.                                                                                                                                                                                                     |
| ops_item_id                    | core | string        | The ID of an OpsItem that is created to represent a Change Manager change request.                                                                                                                                                 |
| outputs                        | core | string        | The list of execution outputs as defined in the Automation runbook.                                                                                                                                                                |
| parameters                     | core | string        | The key-value map of execution parameters, which were supplied when calling StartAutomationExecution.                                                                                                                              |
| parent_automation_execution_id | core | string        | The AutomationExecutionId of the parent automation.                                                                                                                                                                                |
| progress_counters              | core | json          | An aggregate of step execution statuses displayed in the Amazon Web Services Systems Manager console for a multi-Region and multi-account Automation execution.                                                                    |
| resolved_targets               | core | json          | A list of resolved targets in the rate control execution.                                                                                                                                                                          |
| runbooks                       | core | json          | Information about the Automation runbooks that are run as part of a runbook workflow. The Automation runbooks specified for the runbook workflow can't run until all required approvals for the change request have been received. |
| scheduled_time                 | core | timestamp     | The date and time the Automation operation is scheduled to start.                                                                                                                                                                  |
| step_executions                | core | json          | A list of details about the current state of all steps that comprise an execution. An Automation runbook contains a list of steps that are run in order.                                                                           |
| step_executions_truncated      | core | bool          | A boolean value that indicates if the response contains the full list of the Automation step executions. If true, use the DescribeAutomationStepExecutions API operation to get the full list of step executions.                  |
| tags                           | core | hstore_csv    |
| target                         | core | string        | The target of the execution.                                                                                                                                                                                                       |
| target_locations               | core | json          | The combination of Amazon Web Services Regions and/or Amazon Web Services accounts where you want to run the Automation.                                                                                                           |
| target_locations_url           | core | string        | A publicly accessible URL for a file that contains the TargetLocations body. Currently, only files in presigned Amazon S3 buckets are supported                                                                                    |
| target_maps                    | core | array<string> | The specified key-value mapping of document parameters to target resources.                                                                                                                                                        |
| target_parameter_name          | core | string        | The parameter name.                                                                                                                                                                                                                |
| targets                        | core | json          | The specified targets.                                                                                                                                                                                                             |
| triggered_alarms               | core | json          | The CloudWatch alarm that was invoked by the automation.                                                                                                                                                                           |
| variables                      | core | string        | Variables defined for the automation.                                                                                                                                                                                              |
