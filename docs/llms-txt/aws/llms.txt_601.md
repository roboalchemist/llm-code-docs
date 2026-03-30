# Source: https://docs.aws.amazon.com/mwaa-serverless/latest/APIReference/llms.txt

# Amazon Managed Workflows for Apache Airflow Serverless API Reference

> Amazon Managed Workflows for Apache Airflow Serverless provides a managed workflow orchestration platform for running Apache Airflow workflows in a serverless environment. You can use Amazon Managed Workflows for Apache Airflow Serverless to create, manage, and run data processing workflows without managing the underlying infrastructure, Airflow clusters, metadata databases, or scheduling overhead. The service provides secure multi-tenant run environments with automatic scaling, comprehensive logging, and integration with multiple AWS services for orchestrating complex analytics workloads.

- [Welcome](https://docs.aws.amazon.com/mwaa-serverless/latest/APIReference/Welcome.html)
- [Common Parameters](https://docs.aws.amazon.com/mwaa-serverless/latest/APIReference/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/mwaa-serverless/latest/APIReference/CommonErrors.html)

## [Actions](https://docs.aws.amazon.com/mwaa-serverless/latest/APIReference/API_Operations.html)

- [CreateWorkflow](https://docs.aws.amazon.com/mwaa-serverless/latest/APIReference/API_CreateWorkflow.html): Creates a new workflow in Amazon Managed Workflows for Apache Airflow Serverless.
- [DeleteWorkflow](https://docs.aws.amazon.com/mwaa-serverless/latest/APIReference/API_DeleteWorkflow.html): Deletes a workflow and all its versions.
- [GetTaskInstance](https://docs.aws.amazon.com/mwaa-serverless/latest/APIReference/API_GetTaskInstance.html): Retrieves detailed information about a specific task instance within a workflow run.
- [GetWorkflow](https://docs.aws.amazon.com/mwaa-serverless/latest/APIReference/API_GetWorkflow.html): Retrieves detailed information about a workflow, including its configuration, status, and metadata.
- [GetWorkflowRun](https://docs.aws.amazon.com/mwaa-serverless/latest/APIReference/API_GetWorkflowRun.html): Retrieves detailed information about a specific workflow run, including its status, execution details, and task instances.
- [ListTagsForResource](https://docs.aws.amazon.com/mwaa-serverless/latest/APIReference/API_ListTagsForResource.html): Lists all tags that are associated with a specified Amazon Managed Workflows for Apache Airflow Serverless resource.
- [ListTaskInstances](https://docs.aws.amazon.com/mwaa-serverless/latest/APIReference/API_ListTaskInstances.html): Lists all task instances for a specific workflow run, with optional pagination support.
- [ListWorkflowRuns](https://docs.aws.amazon.com/mwaa-serverless/latest/APIReference/API_ListWorkflowRuns.html): Lists all runs for a specified workflow, with optional pagination and filtering support.
- [ListWorkflows](https://docs.aws.amazon.com/mwaa-serverless/latest/APIReference/API_ListWorkflows.html): Lists all workflows in your account, with optional pagination support.
- [ListWorkflowVersions](https://docs.aws.amazon.com/mwaa-serverless/latest/APIReference/API_ListWorkflowVersions.html): Lists all versions of a specified workflow, with optional pagination support.
- [StartWorkflowRun](https://docs.aws.amazon.com/mwaa-serverless/latest/APIReference/API_StartWorkflowRun.html): Starts a new execution of a workflow.
- [StopWorkflowRun](https://docs.aws.amazon.com/mwaa-serverless/latest/APIReference/API_StopWorkflowRun.html): Stops a running workflow execution.
- [TagResource](https://docs.aws.amazon.com/mwaa-serverless/latest/APIReference/API_TagResource.html): Adds tags to an Amazon Managed Workflows for Apache Airflow Serverless resource.
- [UntagResource](https://docs.aws.amazon.com/mwaa-serverless/latest/APIReference/API_UntagResource.html): Removes tags from an Amazon Managed Workflows for Apache Airflow Serverless resource.
- [UpdateWorkflow](https://docs.aws.amazon.com/mwaa-serverless/latest/APIReference/API_UpdateWorkflow.html): Updates an existing workflow with new configuration settings.


## [Data Types](https://docs.aws.amazon.com/mwaa-serverless/latest/APIReference/API_Types.html)

- [DefinitionS3Location](https://docs.aws.amazon.com/mwaa-serverless/latest/APIReference/API_DefinitionS3Location.html): Specifies the Amazon S3 location of a workflow definition file.
- [EncryptionConfiguration](https://docs.aws.amazon.com/mwaa-serverless/latest/APIReference/API_EncryptionConfiguration.html): Configuration for encrypting workflow data at rest and in transit.
- [LoggingConfiguration](https://docs.aws.amazon.com/mwaa-serverless/latest/APIReference/API_LoggingConfiguration.html): Configuration for workflow logging that specifies where you should store your workflow execution logs.
- [NetworkConfiguration](https://docs.aws.amazon.com/mwaa-serverless/latest/APIReference/API_NetworkConfiguration.html): Network configuration for workflow execution.
- [RunDetailSummary](https://docs.aws.amazon.com/mwaa-serverless/latest/APIReference/API_RunDetailSummary.html): Summary information about a workflow run's execution details, including status and timing information.
- [ScheduleConfiguration](https://docs.aws.amazon.com/mwaa-serverless/latest/APIReference/API_ScheduleConfiguration.html): The configuration to use to schedule automated workflow execution using cron expressions.
- [TaskInstanceSummary](https://docs.aws.amazon.com/mwaa-serverless/latest/APIReference/API_TaskInstanceSummary.html): Summary information about a task instance within a workflow run, including its status and execution details.
- [ValidationExceptionField](https://docs.aws.amazon.com/mwaa-serverless/latest/APIReference/API_ValidationExceptionField.html): Contains information about a field that failed validation, including the field name and a descriptive error message.
- [WorkflowRunDetail](https://docs.aws.amazon.com/mwaa-serverless/latest/APIReference/API_WorkflowRunDetail.html): Detailed information about a workflow run execution, including timing, status, error information, and associated task instances.
- [WorkflowRunSummary](https://docs.aws.amazon.com/mwaa-serverless/latest/APIReference/API_WorkflowRunSummary.html): Summary information about a workflow run, including basic identification and status information.
- [WorkflowSummary](https://docs.aws.amazon.com/mwaa-serverless/latest/APIReference/API_WorkflowSummary.html): Summary information about a workflow, including basic identification and metadata.
- [WorkflowVersionSummary](https://docs.aws.amazon.com/mwaa-serverless/latest/APIReference/API_WorkflowVersionSummary.html): Summary information about a workflow version, including identification and configuration details.
