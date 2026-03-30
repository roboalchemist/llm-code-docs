# Source: https://docs.aws.amazon.com/step-functions/latest/apireference/llms.txt

# AWS Step Functions API Reference

> With AWS Step Functions, you can create workflows, also called state machines, to build distributed applications, automate processes, orchestrate microservices, and create data and machine learning pipelines.

- [Welcome](https://docs.aws.amazon.com/step-functions/latest/apireference/Welcome.html)
- [Common Parameters](https://docs.aws.amazon.com/step-functions/latest/apireference/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/step-functions/latest/apireference/CommonErrors.html)

## [Actions](https://docs.aws.amazon.com/step-functions/latest/apireference/API_Operations.html)

- [CreateActivity](https://docs.aws.amazon.com/step-functions/latest/apireference/API_CreateActivity.html): Creates an activity.
- [CreateStateMachine](https://docs.aws.amazon.com/step-functions/latest/apireference/API_CreateStateMachine.html): Creates a state machine.
- [CreateStateMachineAlias](https://docs.aws.amazon.com/step-functions/latest/apireference/API_CreateStateMachineAlias.html): Creates an alias for a state machine that points to one or two versions of the same state machine.
- [DeleteActivity](https://docs.aws.amazon.com/step-functions/latest/apireference/API_DeleteActivity.html): Deletes an activity.
- [DeleteStateMachine](https://docs.aws.amazon.com/step-functions/latest/apireference/API_DeleteStateMachine.html): Deletes a state machine.
- [DeleteStateMachineAlias](https://docs.aws.amazon.com/step-functions/latest/apireference/API_DeleteStateMachineAlias.html): Deletes a state machine alias.
- [DeleteStateMachineVersion](https://docs.aws.amazon.com/step-functions/latest/apireference/API_DeleteStateMachineVersion.html): Deletes a state machine version.
- [DescribeActivity](https://docs.aws.amazon.com/step-functions/latest/apireference/API_DescribeActivity.html): Describes an activity.
- [DescribeExecution](https://docs.aws.amazon.com/step-functions/latest/apireference/API_DescribeExecution.html): Provides information about a state machine execution, such as the state machine associated with the execution, the execution input and output, and relevant execution metadata.
- [DescribeMapRun](https://docs.aws.amazon.com/step-functions/latest/apireference/API_DescribeMapRun.html): Provides information about a Map Run's configuration, progress, and results.
- [DescribeStateMachine](https://docs.aws.amazon.com/step-functions/latest/apireference/API_DescribeStateMachine.html): Provides information about a state machine's definition, its IAM role Amazon Resource Name (ARN), and configuration.
- [DescribeStateMachineAlias](https://docs.aws.amazon.com/step-functions/latest/apireference/API_DescribeStateMachineAlias.html): Returns details about a state machine alias.
- [DescribeStateMachineForExecution](https://docs.aws.amazon.com/step-functions/latest/apireference/API_DescribeStateMachineForExecution.html): Provides information about a state machine's definition, its execution role ARN, and configuration.
- [GetActivityTask](https://docs.aws.amazon.com/step-functions/latest/apireference/API_GetActivityTask.html): Used by workers to retrieve a task (with the specified activity ARN) which has been scheduled for execution by a running state machine.
- [GetExecutionHistory](https://docs.aws.amazon.com/step-functions/latest/apireference/API_GetExecutionHistory.html): Returns the history of the specified execution as a list of events.
- [ListActivities](https://docs.aws.amazon.com/step-functions/latest/apireference/API_ListActivities.html): Lists the existing activities.
- [ListExecutions](https://docs.aws.amazon.com/step-functions/latest/apireference/API_ListExecutions.html): Lists all executions of a state machine or a Map Run.
- [ListMapRuns](https://docs.aws.amazon.com/step-functions/latest/apireference/API_ListMapRuns.html): Lists all Map Runs that were started by a given state machine execution.
- [ListStateMachineAliases](https://docs.aws.amazon.com/step-functions/latest/apireference/API_ListStateMachineAliases.html): Lists aliases for a specified state machine ARN.
- [ListStateMachines](https://docs.aws.amazon.com/step-functions/latest/apireference/API_ListStateMachines.html): Lists the existing state machines.
- [ListStateMachineVersions](https://docs.aws.amazon.com/step-functions/latest/apireference/API_ListStateMachineVersions.html): Lists versions for the specified state machine Amazon Resource Name (ARN).
- [ListTagsForResource](https://docs.aws.amazon.com/step-functions/latest/apireference/API_ListTagsForResource.html): List tags for a given resource.
- [PublishStateMachineVersion](https://docs.aws.amazon.com/step-functions/latest/apireference/API_PublishStateMachineVersion.html): Creates a version from the current revision of a state machine.
- [RedriveExecution](https://docs.aws.amazon.com/step-functions/latest/apireference/API_RedriveExecution.html): Restarts unsuccessful executions of Standard workflows that didn't complete successfully in the last 14 days.
- [SendTaskFailure](https://docs.aws.amazon.com/step-functions/latest/apireference/API_SendTaskFailure.html): Used by activity workers, Task states using the callback pattern, and optionally Task states using the job run pattern to report that the task identified by the taskToken failed.
- [SendTaskHeartbeat](https://docs.aws.amazon.com/step-functions/latest/apireference/API_SendTaskHeartbeat.html): Used by activity workers and Task states using the callback pattern, and optionally Task states using the job run pattern to report to Step Functions that the task represented by the specified taskToken is still making progress.
- [SendTaskSuccess](https://docs.aws.amazon.com/step-functions/latest/apireference/API_SendTaskSuccess.html): Used by activity workers, Task states using the callback pattern, and optionally Task states using the job run pattern to report that the task identified by the taskToken completed successfully.
- [StartExecution](https://docs.aws.amazon.com/step-functions/latest/apireference/API_StartExecution.html): Starts a state machine execution.
- [StartSyncExecution](https://docs.aws.amazon.com/step-functions/latest/apireference/API_StartSyncExecution.html): Starts a Synchronous Express state machine execution.
- [StopExecution](https://docs.aws.amazon.com/step-functions/latest/apireference/API_StopExecution.html): Stops an execution.
- [TagResource](https://docs.aws.amazon.com/step-functions/latest/apireference/API_TagResource.html): Add a tag to a Step Functions resource.
- [TestState](https://docs.aws.amazon.com/step-functions/latest/apireference/API_TestState.html): Accepts the definition of a single state and executes it.
- [UntagResource](https://docs.aws.amazon.com/step-functions/latest/apireference/API_UntagResource.html): Remove a tag from a Step Functions resource
- [UpdateMapRun](https://docs.aws.amazon.com/step-functions/latest/apireference/API_UpdateMapRun.html): Updates an in-progress Map Run's configuration to include changes to the settings that control maximum concurrency and Map Run failure.
- [UpdateStateMachine](https://docs.aws.amazon.com/step-functions/latest/apireference/API_UpdateStateMachine.html): Updates an existing state machine by modifying its definition, roleArn, loggingConfiguration, or EncryptionConfiguration.
- [UpdateStateMachineAlias](https://docs.aws.amazon.com/step-functions/latest/apireference/API_UpdateStateMachineAlias.html): Updates the configuration of an existing state machine alias by modifying its description or routingConfiguration.
- [ValidateStateMachineDefinition](https://docs.aws.amazon.com/step-functions/latest/apireference/API_ValidateStateMachineDefinition.html): Validates the syntax of a state machine definition specified in Amazon States Language (ASL), a JSON-based, structured language.


## [Data Types](https://docs.aws.amazon.com/step-functions/latest/apireference/API_Types.html)

- [ActivityFailedEventDetails](https://docs.aws.amazon.com/step-functions/latest/apireference/API_ActivityFailedEventDetails.html): Contains details about an activity that failed during an execution.
- [ActivityListItem](https://docs.aws.amazon.com/step-functions/latest/apireference/API_ActivityListItem.html): Contains details about an activity.
- [ActivityScheduledEventDetails](https://docs.aws.amazon.com/step-functions/latest/apireference/API_ActivityScheduledEventDetails.html): Contains details about an activity scheduled during an execution.
- [ActivityScheduleFailedEventDetails](https://docs.aws.amazon.com/step-functions/latest/apireference/API_ActivityScheduleFailedEventDetails.html): Contains details about an activity schedule failure that occurred during an execution.
- [ActivityStartedEventDetails](https://docs.aws.amazon.com/step-functions/latest/apireference/API_ActivityStartedEventDetails.html): Contains details about the start of an activity during an execution.
- [ActivitySucceededEventDetails](https://docs.aws.amazon.com/step-functions/latest/apireference/API_ActivitySucceededEventDetails.html): Contains details about an activity that successfully terminated during an execution.
- [ActivityTimedOutEventDetails](https://docs.aws.amazon.com/step-functions/latest/apireference/API_ActivityTimedOutEventDetails.html): Contains details about an activity timeout that occurred during an execution.
- [AssignedVariablesDetails](https://docs.aws.amazon.com/step-functions/latest/apireference/API_AssignedVariablesDetails.html): Provides details about assigned variables in an execution history event.
- [BillingDetails](https://docs.aws.amazon.com/step-functions/latest/apireference/API_BillingDetails.html): An object that describes workflow billing details.
- [CloudWatchEventsExecutionDataDetails](https://docs.aws.amazon.com/step-functions/latest/apireference/API_CloudWatchEventsExecutionDataDetails.html): Provides details about execution input or output.
- [CloudWatchLogsLogGroup](https://docs.aws.amazon.com/step-functions/latest/apireference/API_CloudWatchLogsLogGroup.html)
- [EncryptionConfiguration](https://docs.aws.amazon.com/step-functions/latest/apireference/API_EncryptionConfiguration.html): Settings to configure server-side encryption.
- [EvaluationFailedEventDetails](https://docs.aws.amazon.com/step-functions/latest/apireference/API_EvaluationFailedEventDetails.html): Contains details about an evaluation failure that occurred while processing a state, for example, when a JSONata expression throws an error.
- [ExecutionAbortedEventDetails](https://docs.aws.amazon.com/step-functions/latest/apireference/API_ExecutionAbortedEventDetails.html): Contains details about an abort of an execution.
- [ExecutionFailedEventDetails](https://docs.aws.amazon.com/step-functions/latest/apireference/API_ExecutionFailedEventDetails.html): Contains details about an execution failure event.
- [ExecutionListItem](https://docs.aws.amazon.com/step-functions/latest/apireference/API_ExecutionListItem.html): Contains details about an execution.
- [ExecutionRedrivenEventDetails](https://docs.aws.amazon.com/step-functions/latest/apireference/API_ExecutionRedrivenEventDetails.html): Contains details about a redriven execution.
- [ExecutionStartedEventDetails](https://docs.aws.amazon.com/step-functions/latest/apireference/API_ExecutionStartedEventDetails.html): Contains details about the start of the execution.
- [ExecutionSucceededEventDetails](https://docs.aws.amazon.com/step-functions/latest/apireference/API_ExecutionSucceededEventDetails.html): Contains details about the successful termination of the execution.
- [ExecutionTimedOutEventDetails](https://docs.aws.amazon.com/step-functions/latest/apireference/API_ExecutionTimedOutEventDetails.html): Contains details about the execution timeout that occurred during the execution.
- [HistoryEvent](https://docs.aws.amazon.com/step-functions/latest/apireference/API_HistoryEvent.html): Contains details about the events of an execution.
- [HistoryEventExecutionDataDetails](https://docs.aws.amazon.com/step-functions/latest/apireference/API_HistoryEventExecutionDataDetails.html): Provides details about input or output in an execution history event.
- [InspectionData](https://docs.aws.amazon.com/step-functions/latest/apireference/API_InspectionData.html): Contains additional details about the state's execution, including its input and output data processing flow, and HTTP request and response information.
- [InspectionDataRequest](https://docs.aws.amazon.com/step-functions/latest/apireference/API_InspectionDataRequest.html): Contains additional details about the state's execution, including its input and output data processing flow, and HTTP request information.
- [InspectionDataResponse](https://docs.aws.amazon.com/step-functions/latest/apireference/API_InspectionDataResponse.html): Contains additional details about the state's execution, including its input and output data processing flow, and HTTP response information.
- [InspectionErrorDetails](https://docs.aws.amazon.com/step-functions/latest/apireference/API_InspectionErrorDetails.html): An object containing data about a handled exception in the tested state.
- [LambdaFunctionFailedEventDetails](https://docs.aws.amazon.com/step-functions/latest/apireference/API_LambdaFunctionFailedEventDetails.html): Contains details about a Lambda function that failed during an execution.
- [LambdaFunctionScheduledEventDetails](https://docs.aws.amazon.com/step-functions/latest/apireference/API_LambdaFunctionScheduledEventDetails.html): Contains details about a Lambda function scheduled during an execution.
- [LambdaFunctionScheduleFailedEventDetails](https://docs.aws.amazon.com/step-functions/latest/apireference/API_LambdaFunctionScheduleFailedEventDetails.html): Contains details about a failed Lambda function schedule event that occurred during an execution.
- [LambdaFunctionStartFailedEventDetails](https://docs.aws.amazon.com/step-functions/latest/apireference/API_LambdaFunctionStartFailedEventDetails.html): Contains details about a lambda function that failed to start during an execution.
- [LambdaFunctionSucceededEventDetails](https://docs.aws.amazon.com/step-functions/latest/apireference/API_LambdaFunctionSucceededEventDetails.html): Contains details about a Lambda function that successfully terminated during an execution.
- [LambdaFunctionTimedOutEventDetails](https://docs.aws.amazon.com/step-functions/latest/apireference/API_LambdaFunctionTimedOutEventDetails.html): Contains details about a Lambda function timeout that occurred during an execution.
- [LogDestination](https://docs.aws.amazon.com/step-functions/latest/apireference/API_LogDestination.html)
- [LoggingConfiguration](https://docs.aws.amazon.com/step-functions/latest/apireference/API_LoggingConfiguration.html): The LoggingConfiguration data type is used to set CloudWatch Logs options.
- [MapIterationEventDetails](https://docs.aws.amazon.com/step-functions/latest/apireference/API_MapIterationEventDetails.html): Contains details about an iteration of a Map state.
- [MapRunExecutionCounts](https://docs.aws.amazon.com/step-functions/latest/apireference/API_MapRunExecutionCounts.html): Contains details about all of the child workflow executions started by a Map Run.
- [MapRunFailedEventDetails](https://docs.aws.amazon.com/step-functions/latest/apireference/API_MapRunFailedEventDetails.html): Contains details about a Map Run failure event that occurred during a state machine execution.
- [MapRunItemCounts](https://docs.aws.amazon.com/step-functions/latest/apireference/API_MapRunItemCounts.html): Contains details about items that were processed in all of the child workflow executions that were started by a Map Run.
- [MapRunListItem](https://docs.aws.amazon.com/step-functions/latest/apireference/API_MapRunListItem.html): Contains details about a specific Map Run.
- [MapRunRedrivenEventDetails](https://docs.aws.amazon.com/step-functions/latest/apireference/API_MapRunRedrivenEventDetails.html): Contains details about a Map Run that was redriven.
- [MapRunStartedEventDetails](https://docs.aws.amazon.com/step-functions/latest/apireference/API_MapRunStartedEventDetails.html): Contains details about a Map Run that was started during a state machine execution.
- [MapStateStartedEventDetails](https://docs.aws.amazon.com/step-functions/latest/apireference/API_MapStateStartedEventDetails.html): Details about a Map state that was started.
- [MockErrorOutput](https://docs.aws.amazon.com/step-functions/latest/apireference/API_MockErrorOutput.html): A JSON object that contains a mocked error.
- [MockInput](https://docs.aws.amazon.com/step-functions/latest/apireference/API_MockInput.html): A JSON object that contains a mocked result or errorOutput.
- [RoutingConfigurationListItem](https://docs.aws.amazon.com/step-functions/latest/apireference/API_RoutingConfigurationListItem.html): Contains details about the routing configuration of a state machine alias.
- [StateEnteredEventDetails](https://docs.aws.amazon.com/step-functions/latest/apireference/API_StateEnteredEventDetails.html): Contains details about a state entered during an execution.
- [StateExitedEventDetails](https://docs.aws.amazon.com/step-functions/latest/apireference/API_StateExitedEventDetails.html): Contains details about an exit from a state during an execution.
- [StateMachineAliasListItem](https://docs.aws.amazon.com/step-functions/latest/apireference/API_StateMachineAliasListItem.html): Contains details about a specific state machine alias.
- [StateMachineListItem](https://docs.aws.amazon.com/step-functions/latest/apireference/API_StateMachineListItem.html): Contains details about the state machine.
- [StateMachineVersionListItem](https://docs.aws.amazon.com/step-functions/latest/apireference/API_StateMachineVersionListItem.html): Contains details about a specific state machine version.
- [Tag](https://docs.aws.amazon.com/step-functions/latest/apireference/API_Tag.html): Tags are key-value pairs that can be associated with Step Functions state machines and activities.
- [TaskCredentials](https://docs.aws.amazon.com/step-functions/latest/apireference/API_TaskCredentials.html): Contains details about the credentials that Step Functions uses for a task.
- [TaskFailedEventDetails](https://docs.aws.amazon.com/step-functions/latest/apireference/API_TaskFailedEventDetails.html): Contains details about a task failure event.
- [TaskScheduledEventDetails](https://docs.aws.amazon.com/step-functions/latest/apireference/API_TaskScheduledEventDetails.html): Contains details about a task scheduled during an execution.
- [TaskStartedEventDetails](https://docs.aws.amazon.com/step-functions/latest/apireference/API_TaskStartedEventDetails.html): Contains details about the start of a task during an execution.
- [TaskStartFailedEventDetails](https://docs.aws.amazon.com/step-functions/latest/apireference/API_TaskStartFailedEventDetails.html): Contains details about a task that failed to start during an execution.
- [TaskSubmitFailedEventDetails](https://docs.aws.amazon.com/step-functions/latest/apireference/API_TaskSubmitFailedEventDetails.html): Contains details about a task that failed to submit during an execution.
- [TaskSubmittedEventDetails](https://docs.aws.amazon.com/step-functions/latest/apireference/API_TaskSubmittedEventDetails.html): Contains details about a task submitted to a resource .
- [TaskSucceededEventDetails](https://docs.aws.amazon.com/step-functions/latest/apireference/API_TaskSucceededEventDetails.html): Contains details about the successful completion of a task state.
- [TaskTimedOutEventDetails](https://docs.aws.amazon.com/step-functions/latest/apireference/API_TaskTimedOutEventDetails.html): Contains details about a resource timeout that occurred during an execution.
- [TestStateConfiguration](https://docs.aws.amazon.com/step-functions/latest/apireference/API_TestStateConfiguration.html): Contains configurations for the tested state.
- [TracingConfiguration](https://docs.aws.amazon.com/step-functions/latest/apireference/API_TracingConfiguration.html): Selects whether or not the state machine's AWS X-Ray tracing is enabled.
- [ValidateStateMachineDefinitionDiagnostic](https://docs.aws.amazon.com/step-functions/latest/apireference/API_ValidateStateMachineDefinitionDiagnostic.html): Describes potential issues found during state machine validation.
