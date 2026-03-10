# Source: https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/llms.txt

# Amazon Bedrock AgentCore Data Plane API Reference

> Welcome to the Amazon Bedrock AgentCore Data Plane API reference. Data Plane actions process and handle data or workloads within AWS services.

- [Welcome](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/Welcome.html)
- [Common Parameters](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/CommonErrors.html)

## [Actions](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_Operations.html)

- [BatchCreateMemoryRecords](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_BatchCreateMemoryRecords.html): Creates multiple memory records in a single batch operation for the specified memory with custom content.
- [BatchDeleteMemoryRecords](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_BatchDeleteMemoryRecords.html): Deletes multiple memory records in a single batch operation from the specified memory.
- [BatchUpdateMemoryRecords](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_BatchUpdateMemoryRecords.html): Updates multiple memory records with custom content in a single batch operation within the specified memory.
- [CompleteResourceTokenAuth](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_CompleteResourceTokenAuth.html): Confirms the user authentication session for obtaining OAuth2.0 tokens for a resource.
- [CreateEvent](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_CreateEvent.html): Creates an event in an AgentCore Memory resource.
- [DeleteEvent](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_DeleteEvent.html): Deletes an event from an AgentCore Memory resource.
- [DeleteMemoryRecord](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_DeleteMemoryRecord.html): Deletes a memory record from an AgentCore Memory resource.
- [Evaluate](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_Evaluate.html): Performs on-demand evaluation of agent traces using a specified evaluator.
- [GetAgentCard](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_GetAgentCard.html): Retrieves the A2A agent card associated with an AgentCore Runtime agent.
- [GetBrowserSession](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_GetBrowserSession.html): Retrieves detailed information about a specific browser session in Amazon Bedrock AgentCore.
- [GetCodeInterpreterSession](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_GetCodeInterpreterSession.html): Retrieves detailed information about a specific code interpreter session in Amazon Bedrock AgentCore.
- [GetEvent](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_GetEvent.html): Retrieves information about a specific event in an AgentCore Memory resource.
- [GetMemoryRecord](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_GetMemoryRecord.html): Retrieves a specific memory record from an AgentCore Memory resource.
- [GetResourceApiKey](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_GetResourceApiKey.html): Retrieves the API key associated with an API key credential provider.
- [GetResourceOauth2Token](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_GetResourceOauth2Token.html): Returns the OAuth 2.0 token of the provided resource.
- [GetWorkloadAccessToken](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_GetWorkloadAccessToken.html): Obtains a workload access token for agentic workloads not acting on behalf of a user.
- [GetWorkloadAccessTokenForJWT](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_GetWorkloadAccessTokenForJWT.html): Obtains a workload access token for agentic workloads acting on behalf of a user, using a JWT token.
- [GetWorkloadAccessTokenForUserId](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_GetWorkloadAccessTokenForUserId.html): Obtains a workload access token for agentic workloads acting on behalf of a user, using the user's ID.
- [InvokeAgentRuntime](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_InvokeAgentRuntime.html): Sends a request to an agent or tool hosted in an Amazon Bedrock AgentCore Runtime and receives responses in real-time.
- [InvokeCodeInterpreter](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_InvokeCodeInterpreter.html): Executes code within an active code interpreter session in Amazon Bedrock AgentCore.
- [ListActors](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_ListActors.html): Lists all actors in an AgentCore Memory resource.
- [ListBrowserSessions](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_ListBrowserSessions.html): Retrieves a list of browser sessions in Amazon Bedrock AgentCore that match the specified criteria.
- [ListCodeInterpreterSessions](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_ListCodeInterpreterSessions.html): Retrieves a list of code interpreter sessions in Amazon Bedrock AgentCore that match the specified criteria.
- [ListEvents](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_ListEvents.html): Lists events in an AgentCore Memory resource based on specified criteria.
- [ListMemoryExtractionJobs](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_ListMemoryExtractionJobs.html): Lists all long-term memory extraction jobs that are eligible to be started with optional filtering.
- [ListMemoryRecords](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_ListMemoryRecords.html): Lists memory records in an AgentCore Memory resource based on specified criteria.
- [ListSessions](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_ListSessions.html): Lists sessions in an AgentCore Memory resource based on specified criteria.
- [RetrieveMemoryRecords](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_RetrieveMemoryRecords.html): Searches for and retrieves memory records from an AgentCore Memory resource based on specified search criteria.
- [SaveBrowserSessionProfile](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_SaveBrowserSessionProfile.html): Saves the current state of a browser session as a reusable profile in Amazon Bedrock AgentCore.
- [StartBrowserSession](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_StartBrowserSession.html): Creates and initializes a browser session in Amazon Bedrock AgentCore.
- [StartCodeInterpreterSession](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_StartCodeInterpreterSession.html): Creates and initializes a code interpreter session in Amazon Bedrock AgentCore.
- [StartMemoryExtractionJob](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_StartMemoryExtractionJob.html): Starts a memory extraction job that processes events that failed extraction previously in an AgentCore Memory resource and produces structured memory records.
- [StopBrowserSession](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_StopBrowserSession.html): Terminates an active browser session in Amazon Bedrock AgentCore.
- [StopCodeInterpreterSession](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_StopCodeInterpreterSession.html): Terminates an active code interpreter session in Amazon Bedrock AgentCore.
- [StopRuntimeSession](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_StopRuntimeSession.html): Stops a session that is running in an running AgentCore Runtime agent.
- [UpdateBrowserStream](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_UpdateBrowserStream.html): Updates a browser stream.


## [Data Types](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_Types.html)

- [ActorSummary](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_ActorSummary.html): Contains summary information about an actor in an AgentCore Memory resource.
- [AutomationStream](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_AutomationStream.html): The configuration for a stream that enables programmatic control of a browser session in Amazon Bedrock AgentCore.
- [AutomationStreamUpdate](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_AutomationStreamUpdate.html): Contains information about an update to an automation stream.
- [Branch](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_Branch.html): Contains information about a branch in an AgentCore Memory resource.
- [BranchFilter](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_BranchFilter.html): Contains filter criteria for branches when listing events.
- [BrowserExtension](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_BrowserExtension.html): Browser extension configuration.
- [BrowserProfileConfiguration](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_BrowserProfileConfiguration.html): The configuration for a browser profile in Amazon Bedrock AgentCore.
- [BrowserSessionStream](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_BrowserSessionStream.html): The collection of streams associated with a browser session in Amazon Bedrock AgentCore.
- [BrowserSessionSummary](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_BrowserSessionSummary.html): A condensed representation of a browser session in Amazon Bedrock AgentCore.
- [CodeInterpreterResult](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_CodeInterpreterResult.html): The output produced by executing code in a code interpreter session in Amazon Bedrock AgentCore.
- [CodeInterpreterSessionSummary](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_CodeInterpreterSessionSummary.html): A condensed representation of a code interpreter session in Amazon Bedrock AgentCore.
- [CodeInterpreterStreamOutput](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_CodeInterpreterStreamOutput.html): Contains output from a code interpreter stream.
- [Content](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_Content.html): Contains the content of a memory item.
- [ContentBlock](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_ContentBlock.html): A block of content in a response.
- [Context](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_Context.html): The contextual information associated with an evaluation, including span context details that identify the specific traces and sessions being evaluated within the agent's execution flow.
- [Conversational](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_Conversational.html): Contains conversational content for an event payload.
- [EvaluationInput](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_EvaluationInput.html): The input data structure containing agent session spans in OpenTelemetry format.
- [EvaluationResultContent](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_EvaluationResultContent.html): The comprehensive result of an evaluation containing the score, explanation, evaluator metadata, and execution details.
- [EvaluationTarget](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_EvaluationTarget.html): The specification of which trace or span IDs to evaluate within the provided input data.
- [Event](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_Event.html): Contains information about an event in an AgentCore Memory resource.
- [EventMetadataFilterExpression](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_EventMetadataFilterExpression.html): Filter expression for retrieving events based on metadata associated with an event.
- [ExtractionJob](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_ExtractionJob.html): Represents the metadata of a memory extraction job such as the message identifiers that compose this job.
- [ExtractionJobFilterInput](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_ExtractionJobFilterInput.html): Filters for querying memory extraction jobs based on various criteria.
- [ExtractionJobMessages](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_ExtractionJobMessages.html): The list of messages that compose this extraction job.
- [ExtractionJobMetadata](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_ExtractionJobMetadata.html): Metadata information associated with this extraction job.
- [FilterInput](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_FilterInput.html): Contains filter criteria for listing events.
- [InputContentBlock](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_InputContentBlock.html): A block of input content.
- [LeftExpression](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_LeftExpression.html): Left expression of the event metadata filter.
- [LiveViewStream](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_LiveViewStream.html): The configuration for a stream that provides a visual representation of a browser session in Amazon Bedrock AgentCore.
- [MemoryContent](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_MemoryContent.html): Contains the content of a memory record.
- [MemoryMetadataFilterExpression](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_MemoryMetadataFilterExpression.html): Filters to apply to metadata associated with a memory.
- [MemoryRecord](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_MemoryRecord.html): Contains information about a memory record in an AgentCore Memory resource.
- [MemoryRecordCreateInput](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_MemoryRecordCreateInput.html): Input structure to create a new memory record.
- [MemoryRecordDeleteInput](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_MemoryRecordDeleteInput.html): Input structure to delete an existing memory record.
- [MemoryRecordOutput](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_MemoryRecordOutput.html): Output information returned after processing a memory record operation.
- [MemoryRecordSummary](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_MemoryRecordSummary.html): Contains summary information about a memory record.
- [MemoryRecordUpdateInput](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_MemoryRecordUpdateInput.html): Input structure to update an existing memory record.
- [MessageMetadata](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_MessageMetadata.html): Metadata information associated with this message.
- [MetadataValue](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_MetadataValue.html): Value associated with the eventMetadata key.
- [PayloadType](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_PayloadType.html): Contains the payload content for an event.
- [ResourceContent](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_ResourceContent.html): Contains information about resource content.
- [ResourceLocation](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_ResourceLocation.html): The location of the browser extension.
- [RightExpression](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_RightExpression.html): Right expression of the eventMetadatafilter.
- [S3Location](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_S3Location.html): The Amazon S3 location configuration of a resource.
- [SearchCriteria](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_SearchCriteria.html): Contains search criteria for retrieving memory records.
- [SessionSummary](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_SessionSummary.html): Contains summary information about a session in an AgentCore Memory resource.
- [SpanContext](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_SpanContext.html): The contextual information that uniquely identifies a span within the distributed tracing system.
- [StreamUpdate](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_StreamUpdate.html): Contains information about an update to a stream.
- [TokenUsage](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_TokenUsage.html): The token consumption statistics for language model operations during evaluation.
- [ToolArguments](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_ToolArguments.html): The collection of arguments that specify the operation to perform and its parameters when invoking a tool in Amazon Bedrock AgentCore.
- [ToolResultStructuredContent](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_ToolResultStructuredContent.html): Contains structured content from a tool result.
- [UserIdentifier](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_UserIdentifier.html): The OAuth2.0 token or user ID that was used to generate the workload access token used for initiating the user authorization flow to retrieve OAuth2.0 tokens.
- [ValidationExceptionField](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_ValidationExceptionField.html): Stores information about a field passed inside a request that resulted in an exception.
- [ViewPort](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_ViewPort.html): The configuration that defines the dimensions of a browser viewport in a browser session.
