# Source: https://docs.aws.amazon.com/nova-act/latest/APIReference/llms.txt

# Amazon Nova Act Amazon Nova Act API Reference

> The Nova Act service provides a REST API for managing AI-powered workflow automation. It enables users to create workflow definitions, execute workflow runs, manage sessions, and orchestrate acts (individual AI tasks) with tool integrations.

- [Welcome](https://docs.aws.amazon.com/nova-act/latest/APIReference/Welcome.html)
- [Common Parameters](https://docs.aws.amazon.com/nova-act/latest/APIReference/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/nova-act/latest/APIReference/CommonErrors.html)

## [Actions](https://docs.aws.amazon.com/nova-act/latest/APIReference/API_Operations.html)

- [CreateAct](https://docs.aws.amazon.com/nova-act/latest/APIReference/API_CreateAct.html): Creates a new AI task (act) within a session that can interact with tools and perform specific actions.
- [CreateSession](https://docs.aws.amazon.com/nova-act/latest/APIReference/API_CreateSession.html): Creates a new session context within a workflow run to manage conversation state and acts.
- [CreateWorkflowDefinition](https://docs.aws.amazon.com/nova-act/latest/APIReference/API_CreateWorkflowDefinition.html): Creates a new workflow definition template that can be used to execute multiple workflow runs.
- [CreateWorkflowRun](https://docs.aws.amazon.com/nova-act/latest/APIReference/API_CreateWorkflowRun.html): Creates a new execution instance of a workflow definition with specified parameters.
- [DeleteWorkflowDefinition](https://docs.aws.amazon.com/nova-act/latest/APIReference/API_DeleteWorkflowDefinition.html): Deletes a workflow definition and all associated resources.
- [DeleteWorkflowRun](https://docs.aws.amazon.com/nova-act/latest/APIReference/API_DeleteWorkflowRun.html): Terminates and cleans up a workflow run, stopping all associated acts and sessions.
- [GetWorkflowDefinition](https://docs.aws.amazon.com/nova-act/latest/APIReference/API_GetWorkflowDefinition.html): Retrieves the details and configuration of a specific workflow definition.
- [GetWorkflowRun](https://docs.aws.amazon.com/nova-act/latest/APIReference/API_GetWorkflowRun.html): Retrieves the current state, configuration, and execution details of a workflow run.
- [InvokeActStep](https://docs.aws.amazon.com/nova-act/latest/APIReference/API_InvokeActStep.html): Executes the next step of an act, processing tool call results and returning new tool calls if needed.
- [ListActs](https://docs.aws.amazon.com/nova-act/latest/APIReference/API_ListActs.html): Lists all acts within a specific session with their current status and execution details.
- [ListModels](https://docs.aws.amazon.com/nova-act/latest/APIReference/API_ListModels.html): Lists all available AI models that can be used for workflow execution, including their status and compatibility information.
- [ListSessions](https://docs.aws.amazon.com/nova-act/latest/APIReference/API_ListSessions.html): Lists all sessions within a specific workflow run.
- [ListWorkflowDefinitions](https://docs.aws.amazon.com/nova-act/latest/APIReference/API_ListWorkflowDefinitions.html): Lists all workflow definitions in your account with optional filtering and pagination.
- [ListWorkflowRuns](https://docs.aws.amazon.com/nova-act/latest/APIReference/API_ListWorkflowRuns.html): Lists all workflow runs for a specific workflow definition with optional filtering and pagination.
- [UpdateAct](https://docs.aws.amazon.com/nova-act/latest/APIReference/API_UpdateAct.html): Updates an existing act's configuration, status, or error information.
- [UpdateWorkflowRun](https://docs.aws.amazon.com/nova-act/latest/APIReference/API_UpdateWorkflowRun.html): Updates the configuration or state of an active workflow run.


## [Data Types](https://docs.aws.amazon.com/nova-act/latest/APIReference/API_Types.html)

- [ActError](https://docs.aws.amazon.com/nova-act/latest/APIReference/API_ActError.html): Error information when an act fails to execute successfully.
- [ActSummary](https://docs.aws.amazon.com/nova-act/latest/APIReference/API_ActSummary.html): Summary information about an act, including its status and execution timing.
- [Call](https://docs.aws.amazon.com/nova-act/latest/APIReference/API_Call.html): A request for the client to execute a specific tool with given parameters.
- [CallResult](https://docs.aws.amazon.com/nova-act/latest/APIReference/API_CallResult.html): The result returned from executing a tool call.
- [CallResultContent](https://docs.aws.amazon.com/nova-act/latest/APIReference/API_CallResultContent.html): Content returned from a tool call execution.
- [ClientInfo](https://docs.aws.amazon.com/nova-act/latest/APIReference/API_ClientInfo.html): Information about the client making API requests, used for compatibility checking.
- [CompatibilityInformation](https://docs.aws.amazon.com/nova-act/latest/APIReference/API_CompatibilityInformation.html): Information about client compatibility and supported model versions.
- [ModelAlias](https://docs.aws.amazon.com/nova-act/latest/APIReference/API_ModelAlias.html): An alias that provides a stable reference to a model version.
- [ModelLifecycle](https://docs.aws.amazon.com/nova-act/latest/APIReference/API_ModelLifecycle.html): Lifecycle information for an AI model.
- [ModelSummary](https://docs.aws.amazon.com/nova-act/latest/APIReference/API_ModelSummary.html): Summary information about an available AI model.
- [SessionSummary](https://docs.aws.amazon.com/nova-act/latest/APIReference/API_SessionSummary.html): Summary information about a session within a workflow run.
- [ToolInputSchema](https://docs.aws.amazon.com/nova-act/latest/APIReference/API_ToolInputSchema.html): The schema definition for tool input parameters.
- [ToolSpec](https://docs.aws.amazon.com/nova-act/latest/APIReference/API_ToolSpec.html): Specification for a tool that acts can invoke, including its name, description, and input schema.
- [TraceLocation](https://docs.aws.amazon.com/nova-act/latest/APIReference/API_TraceLocation.html): Information about where trace data is stored for debugging and monitoring.
- [ValidationExceptionField](https://docs.aws.amazon.com/nova-act/latest/APIReference/API_ValidationExceptionField.html): Information about a field that failed validation.
- [WorkflowDefinitionSummary](https://docs.aws.amazon.com/nova-act/latest/APIReference/API_WorkflowDefinitionSummary.html): Summary information about a workflow definition, used in list operations.
- [WorkflowExportConfig](https://docs.aws.amazon.com/nova-act/latest/APIReference/API_WorkflowExportConfig.html): Configuration settings for exporting workflow execution data and logs to Amazon Simple Storage Service (Amazon S3).
- [WorkflowRunSummary](https://docs.aws.amazon.com/nova-act/latest/APIReference/API_WorkflowRunSummary.html): Summary information about a workflow run, including execution status and timing.


## [Service-specific Errors](https://docs.aws.amazon.com/nova-act/latest/APIReference/API_Errors.html)

- [AccessDeniedException](https://docs.aws.amazon.com/nova-act/latest/APIReference/API_AccessDeniedException.html): You don't have sufficient permissions to perform this action.
- [ConflictException](https://docs.aws.amazon.com/nova-act/latest/APIReference/API_ConflictException.html): The request could not be completed due to a conflict with the current state of the resource.
- [InternalServerException](https://docs.aws.amazon.com/nova-act/latest/APIReference/API_InternalServerException.html): An internal server error occurred.
- [ResourceNotFoundException](https://docs.aws.amazon.com/nova-act/latest/APIReference/API_ResourceNotFoundException.html): The requested resource was not found.
- [ServiceQuotaExceededException](https://docs.aws.amazon.com/nova-act/latest/APIReference/API_ServiceQuotaExceededException.html): The request would exceed a service quota limit.
- [ThrottlingException](https://docs.aws.amazon.com/nova-act/latest/APIReference/API_ThrottlingException.html): The request was throttled due to too many requests.
- [ValidationException](https://docs.aws.amazon.com/nova-act/latest/APIReference/API_ValidationException.html): The input parameters for the request are invalid.
