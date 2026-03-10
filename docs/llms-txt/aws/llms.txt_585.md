# Source: https://docs.aws.amazon.com/migrationhub-orchestrator/latest/APIReference/llms.txt

# Migration Hub Orchestrator Welcome

> This API reference provides descriptions, syntax, and other details about each of the actions and data types for AWS Migration Hub Orchestrator. The topic for each action shows the API request parameters and responses. Alternatively, you can use one of the AWS SDKs to access an API that is tailored to the programming language or platform that you're using.

- [Welcome](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/APIReference/Welcome.html)
- [Common Parameters](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/APIReference/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/APIReference/CommonErrors.html)

## [Actions](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/APIReference/API_Operations.html)

- [CreateTemplate](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/APIReference/API_CreateTemplate.html)
- [CreateWorkflow](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/APIReference/API_CreateWorkflow.html)
- [CreateWorkflowStep](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/APIReference/API_CreateWorkflowStep.html)
- [CreateWorkflowStepGroup](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/APIReference/API_CreateWorkflowStepGroup.html)
- [DeleteTemplate](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/APIReference/API_DeleteTemplate.html)
- [DeleteWorkflow](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/APIReference/API_DeleteWorkflow.html)
- [DeleteWorkflowStep](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/APIReference/API_DeleteWorkflowStep.html)
- [DeleteWorkflowStepGroup](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/APIReference/API_DeleteWorkflowStepGroup.html)
- [GetTemplate](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/APIReference/API_GetTemplate.html)
- [GetTemplateStep](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/APIReference/API_GetTemplateStep.html)
- [GetTemplateStepGroup](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/APIReference/API_GetTemplateStepGroup.html)
- [GetWorkflow](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/APIReference/API_GetWorkflow.html)
- [GetWorkflowStep](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/APIReference/API_GetWorkflowStep.html)
- [GetWorkflowStepGroup](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/APIReference/API_GetWorkflowStepGroup.html)
- [ListPlugins](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/APIReference/API_ListPlugins.html)
- [ListTagsForResource](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/APIReference/API_ListTagsForResource.html)
- [ListTemplates](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/APIReference/API_ListTemplates.html)
- [ListTemplateStepGroups](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/APIReference/API_ListTemplateStepGroups.html)
- [ListTemplateSteps](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/APIReference/API_ListTemplateSteps.html)
- [ListWorkflows](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/APIReference/API_ListWorkflows.html)
- [ListWorkflowStepGroups](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/APIReference/API_ListWorkflowStepGroups.html)
- [ListWorkflowSteps](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/APIReference/API_ListWorkflowSteps.html)
- [RetryWorkflowStep](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/APIReference/API_RetryWorkflowStep.html)
- [StartWorkflow](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/APIReference/API_StartWorkflow.html)
- [StopWorkflow](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/APIReference/API_StopWorkflow.html)
- [TagResource](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/APIReference/API_TagResource.html)
- [UntagResource](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/APIReference/API_UntagResource.html)
- [UpdateTemplate](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/APIReference/API_UpdateTemplate.html)
- [UpdateWorkflow](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/APIReference/API_UpdateWorkflow.html)
- [UpdateWorkflowStep](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/APIReference/API_UpdateWorkflowStep.html)
- [UpdateWorkflowStepGroup](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/APIReference/API_UpdateWorkflowStepGroup.html)


## [Data Types](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/APIReference/API_Types.html)

- [MigrationWorkflowSummary](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/APIReference/API_MigrationWorkflowSummary.html): The summary of a migration workflow.
- [PlatformCommand](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/APIReference/API_PlatformCommand.html): Command to be run on a particular operating system.
- [PlatformScriptKey](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/APIReference/API_PlatformScriptKey.html): The script location for a particular operating system.
- [PluginSummary](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/APIReference/API_PluginSummary.html): The summary of the Migration Hub Orchestrator plugin.
- [StepAutomationConfiguration](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/APIReference/API_StepAutomationConfiguration.html): The custom script to run tests on source or target environments.
- [StepInput](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/APIReference/API_StepInput.html): A map of key value pairs that is generated when you create a migration workflow.
- [StepOutput](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/APIReference/API_StepOutput.html): The output of the step.
- [TemplateInput](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/APIReference/API_TemplateInput.html): The input parameters of a template.
- [TemplateSource](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/APIReference/API_TemplateSource.html): The migration workflow template used as the source for the new template.
- [TemplateStepGroupSummary](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/APIReference/API_TemplateStepGroupSummary.html): The summary of the step group in the template.
- [TemplateStepSummary](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/APIReference/API_TemplateStepSummary.html): The summary of the step.
- [TemplateSummary](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/APIReference/API_TemplateSummary.html): The summary of the template.
- [Tool](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/APIReference/API_Tool.html): List of AWS services utilized in a migration workflow.
- [WorkflowStepAutomationConfiguration](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/APIReference/API_WorkflowStepAutomationConfiguration.html): The custom script to run tests on source or target environments.
- [WorkflowStepGroupSummary](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/APIReference/API_WorkflowStepGroupSummary.html): The summary of a step group in a workflow.
- [WorkflowStepOutput](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/APIReference/API_WorkflowStepOutput.html): The output of a step.
- [WorkflowStepOutputUnion](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/APIReference/API_WorkflowStepOutputUnion.html): A structure to hold multiple values of an output.
- [WorkflowStepSummary](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/APIReference/API_WorkflowStepSummary.html): The summary of the step in a migration workflow.
