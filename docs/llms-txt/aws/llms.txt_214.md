# Source: https://docs.aws.amazon.com/codecatalyst/latest/APIReference/llms.txt

# Amazon CodeCatalyst Welcome

> Welcome to the Amazon CodeCatalyst API reference. This reference provides descriptions of operations and data types for Amazon CodeCatalyst. You can use the Amazon CodeCatalyst API to work with the following objects.

- [Welcome](https://docs.aws.amazon.com/codecatalyst/latest/APIReference/Welcome.html)

## [Actions](https://docs.aws.amazon.com/codecatalyst/latest/APIReference/API_Operations.html)

- [CreateAccessToken](https://docs.aws.amazon.com/codecatalyst/latest/APIReference/API_CreateAccessToken.html): Creates a personal access token (PAT) for the current user.
- [CreateDevEnvironment](https://docs.aws.amazon.com/codecatalyst/latest/APIReference/API_CreateDevEnvironment.html): Creates a Dev Environment in Amazon CodeCatalyst, a cloud-based development environment that you can use to quickly work on the code stored in the source repositories of your project.
- [CreateProject](https://docs.aws.amazon.com/codecatalyst/latest/APIReference/API_CreateProject.html): Creates a project in a specified space.
- [CreateSourceRepository](https://docs.aws.amazon.com/codecatalyst/latest/APIReference/API_CreateSourceRepository.html): Creates an empty Git-based source repository in a specified project.
- [CreateSourceRepositoryBranch](https://docs.aws.amazon.com/codecatalyst/latest/APIReference/API_CreateSourceRepositoryBranch.html): Creates a branch in a specified source repository in Amazon CodeCatalyst.
- [DeleteAccessToken](https://docs.aws.amazon.com/codecatalyst/latest/APIReference/API_DeleteAccessToken.html): Deletes a specified personal access token (PAT).
- [DeleteDevEnvironment](https://docs.aws.amazon.com/codecatalyst/latest/APIReference/API_DeleteDevEnvironment.html): Deletes a Dev Environment.
- [DeleteProject](https://docs.aws.amazon.com/codecatalyst/latest/APIReference/API_DeleteProject.html): Deletes a project in a space.
- [DeleteSourceRepository](https://docs.aws.amazon.com/codecatalyst/latest/APIReference/API_DeleteSourceRepository.html): Deletes a source repository in Amazon CodeCatalyst.
- [DeleteSpace](https://docs.aws.amazon.com/codecatalyst/latest/APIReference/API_DeleteSpace.html): Deletes a space.
- [GetDevEnvironment](https://docs.aws.amazon.com/codecatalyst/latest/APIReference/API_GetDevEnvironment.html): Returns information about a Dev Environment for a source repository in a project.
- [GetProject](https://docs.aws.amazon.com/codecatalyst/latest/APIReference/API_GetProject.html): Returns information about a project.
- [GetSourceRepository](https://docs.aws.amazon.com/codecatalyst/latest/APIReference/API_GetSourceRepository.html): Returns information about a source repository.
- [GetSourceRepositoryCloneUrls](https://docs.aws.amazon.com/codecatalyst/latest/APIReference/API_GetSourceRepositoryCloneUrls.html): Returns information about the URLs that can be used with a Git client to clone a source repository.
- [GetSpace](https://docs.aws.amazon.com/codecatalyst/latest/APIReference/API_GetSpace.html): Returns information about an space.
- [GetSubscription](https://docs.aws.amazon.com/codecatalyst/latest/APIReference/API_GetSubscription.html): Returns information about the AWS account used for billing purposes and the billing plan for the space.
- [GetUserDetails](https://docs.aws.amazon.com/codecatalyst/latest/APIReference/API_GetUserDetails.html): Returns information about a user.
- [GetWorkflow](https://docs.aws.amazon.com/codecatalyst/latest/APIReference/API_GetWorkflow.html): Returns information about a workflow.
- [GetWorkflowRun](https://docs.aws.amazon.com/codecatalyst/latest/APIReference/API_GetWorkflowRun.html): Returns information about a specified run of a workflow.
- [ListAccessTokens](https://docs.aws.amazon.com/codecatalyst/latest/APIReference/API_ListAccessTokens.html): Lists all personal access tokens (PATs) associated with the user who calls the API.
- [ListDevEnvironments](https://docs.aws.amazon.com/codecatalyst/latest/APIReference/API_ListDevEnvironments.html): Retrieves a list of Dev Environments in a project.
- [ListDevEnvironmentSessions](https://docs.aws.amazon.com/codecatalyst/latest/APIReference/API_ListDevEnvironmentSessions.html): Retrieves a list of active sessions for a Dev Environment in a project.
- [ListEventLogs](https://docs.aws.amazon.com/codecatalyst/latest/APIReference/API_ListEventLogs.html): Retrieves a list of events that occurred during a specific time in a space.
- [ListProjects](https://docs.aws.amazon.com/codecatalyst/latest/APIReference/API_ListProjects.html): Retrieves a list of projects.
- [ListSourceRepositories](https://docs.aws.amazon.com/codecatalyst/latest/APIReference/API_ListSourceRepositories.html): Retrieves a list of source repositories in a project.
- [ListSourceRepositoryBranches](https://docs.aws.amazon.com/codecatalyst/latest/APIReference/API_ListSourceRepositoryBranches.html): Retrieves a list of branches in a specified source repository.
- [ListSpaces](https://docs.aws.amazon.com/codecatalyst/latest/APIReference/API_ListSpaces.html): Retrieves a list of spaces.
- [ListWorkflowRuns](https://docs.aws.amazon.com/codecatalyst/latest/APIReference/API_ListWorkflowRuns.html): Retrieves a list of workflow runs of a specified workflow.
- [ListWorkflows](https://docs.aws.amazon.com/codecatalyst/latest/APIReference/API_ListWorkflows.html): Retrieves a list of workflows in a specified project.
- [StartDevEnvironment](https://docs.aws.amazon.com/codecatalyst/latest/APIReference/API_StartDevEnvironment.html): Starts a specified Dev Environment and puts it into an active state.
- [StartDevEnvironmentSession](https://docs.aws.amazon.com/codecatalyst/latest/APIReference/API_StartDevEnvironmentSession.html): Starts a session for a specified Dev Environment.
- [StartWorkflowRun](https://docs.aws.amazon.com/codecatalyst/latest/APIReference/API_StartWorkflowRun.html): Begins a run of a specified workflow.
- [StopDevEnvironment](https://docs.aws.amazon.com/codecatalyst/latest/APIReference/API_StopDevEnvironment.html): Pauses a specified Dev Environment and places it in a non-running state.
- [StopDevEnvironmentSession](https://docs.aws.amazon.com/codecatalyst/latest/APIReference/API_StopDevEnvironmentSession.html): Stops a session for a specified Dev Environment.
- [UpdateDevEnvironment](https://docs.aws.amazon.com/codecatalyst/latest/APIReference/API_UpdateDevEnvironment.html): Changes one or more values for a Dev Environment.
- [UpdateProject](https://docs.aws.amazon.com/codecatalyst/latest/APIReference/API_UpdateProject.html): Changes one or more values for a project.
- [UpdateSpace](https://docs.aws.amazon.com/codecatalyst/latest/APIReference/API_UpdateSpace.html): Changes one or more values for a space.
- [VerifySession](https://docs.aws.amazon.com/codecatalyst/latest/APIReference/API_VerifySession.html): Verifies whether the calling user has a valid Amazon CodeCatalyst login and session.


## [Data Types](https://docs.aws.amazon.com/codecatalyst/latest/APIReference/API_Types.html)

- [AccessTokenSummary](https://docs.aws.amazon.com/codecatalyst/latest/APIReference/API_AccessTokenSummary.html): Information about a specified personal access token (PAT).
- [DevEnvironmentAccessDetails](https://docs.aws.amazon.com/codecatalyst/latest/APIReference/API_DevEnvironmentAccessDetails.html): Information about connection details for a Dev Environment.
- [DevEnvironmentRepositorySummary](https://docs.aws.amazon.com/codecatalyst/latest/APIReference/API_DevEnvironmentRepositorySummary.html): Information about the source repsitory for a Dev Environment.
- [DevEnvironmentSessionConfiguration](https://docs.aws.amazon.com/codecatalyst/latest/APIReference/API_DevEnvironmentSessionConfiguration.html): Information about the configuration of a Dev Environment session.
- [DevEnvironmentSessionSummary](https://docs.aws.amazon.com/codecatalyst/latest/APIReference/API_DevEnvironmentSessionSummary.html): Information about active sessions for a Dev Environment.
- [DevEnvironmentSummary](https://docs.aws.amazon.com/codecatalyst/latest/APIReference/API_DevEnvironmentSummary.html): Information about a Dev Environment.
- [EmailAddress](https://docs.aws.amazon.com/codecatalyst/latest/APIReference/API_EmailAddress.html): Information about an email address.
- [EventLogEntry](https://docs.aws.amazon.com/codecatalyst/latest/APIReference/API_EventLogEntry.html): Information about an entry in an event log of Amazon CodeCatalyst activity.
- [EventPayload](https://docs.aws.amazon.com/codecatalyst/latest/APIReference/API_EventPayload.html): Information about the payload of an event recording Amazon CodeCatalyst activity.
- [ExecuteCommandSessionConfiguration](https://docs.aws.amazon.com/codecatalyst/latest/APIReference/API_ExecuteCommandSessionConfiguration.html): Information about the commands that will be run on a Dev Environment when an SSH session begins.
- [Filter](https://docs.aws.amazon.com/codecatalyst/latest/APIReference/API_Filter.html): Information about a filter used to limit results of a query.
- [Ide](https://docs.aws.amazon.com/codecatalyst/latest/APIReference/API_Ide.html): Information about an integrated development environment (IDE) used in a Dev Environment.
- [IdeConfiguration](https://docs.aws.amazon.com/codecatalyst/latest/APIReference/API_IdeConfiguration.html): Information about the configuration of an integrated development environment (IDE) for a Dev Environment.
- [ListSourceRepositoriesItem](https://docs.aws.amazon.com/codecatalyst/latest/APIReference/API_ListSourceRepositoriesItem.html): Information about a source repository returned in a list of source repositories.
- [ListSourceRepositoryBranchesItem](https://docs.aws.amazon.com/codecatalyst/latest/APIReference/API_ListSourceRepositoryBranchesItem.html): Information about a branch of a source repository returned in a list of branches.
- [PersistentStorage](https://docs.aws.amazon.com/codecatalyst/latest/APIReference/API_PersistentStorage.html): Information about the persistent storage for a Dev Environment.
- [PersistentStorageConfiguration](https://docs.aws.amazon.com/codecatalyst/latest/APIReference/API_PersistentStorageConfiguration.html): Information about the configuration of persistent storage for a Dev Environment.
- [ProjectInformation](https://docs.aws.amazon.com/codecatalyst/latest/APIReference/API_ProjectInformation.html): Information about a project in a space.
- [ProjectListFilter](https://docs.aws.amazon.com/codecatalyst/latest/APIReference/API_ProjectListFilter.html): nformation about the filter used to narrow the results returned in a list of projects.
- [ProjectSummary](https://docs.aws.amazon.com/codecatalyst/latest/APIReference/API_ProjectSummary.html): Information about a project.
- [RepositoryInput](https://docs.aws.amazon.com/codecatalyst/latest/APIReference/API_RepositoryInput.html): Information about a repository that will be cloned to a Dev Environment.
- [SpaceSummary](https://docs.aws.amazon.com/codecatalyst/latest/APIReference/API_SpaceSummary.html): Information about an space.
- [UserIdentity](https://docs.aws.amazon.com/codecatalyst/latest/APIReference/API_UserIdentity.html): Information about a user whose activity is recorded in an event for a space.
- [WorkflowDefinition](https://docs.aws.amazon.com/codecatalyst/latest/APIReference/API_WorkflowDefinition.html): Information about a workflow definition file.
- [WorkflowDefinitionSummary](https://docs.aws.amazon.com/codecatalyst/latest/APIReference/API_WorkflowDefinitionSummary.html): Information about a workflow definition.
- [WorkflowRunSortCriteria](https://docs.aws.amazon.com/codecatalyst/latest/APIReference/API_WorkflowRunSortCriteria.html): Information used to sort workflow runs in the returned list.
- [WorkflowRunStatusReason](https://docs.aws.amazon.com/codecatalyst/latest/APIReference/API_WorkflowRunStatusReason.html): Information about the status of a workflow run.
- [WorkflowRunSummary](https://docs.aws.amazon.com/codecatalyst/latest/APIReference/API_WorkflowRunSummary.html): Information about a workflow run.
- [WorkflowSortCriteria](https://docs.aws.amazon.com/codecatalyst/latest/APIReference/API_WorkflowSortCriteria.html): Information used to sort workflows in the returned list.
- [WorkflowSummary](https://docs.aws.amazon.com/codecatalyst/latest/APIReference/API_WorkflowSummary.html): Information about a workflow.
