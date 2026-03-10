# Source: https://docs.aws.amazon.com/amazonq/latest/api-reference/llms.txt

# Amazon Q Business API Reference

## [QBusiness](https://docs.aws.amazon.com/amazonq/latest/api-reference/Welcome_QBusiness.html)

This is the Amazon Q BusinessAPI Reference. Amazon Q Business is a fully managed, generative-AI powered enterprise chat assistant that you can deploy within your organization. Amazon Q Business enhances employee productivity by supporting key tasks such as question-answering, knowledge discovery, writing email messages, summarizing text, drafting document outlines, and brainstorming ideas. Users ask questions of Amazon Q Business and get answers that are presented in a conversational manner. For an introduction to the service, see the [Amazon Q Business User Guide](https://docs.aws.amazon.com/amazonq/latest/business-use-dg/what-is.html).

For an overview of the Amazon Q Business APIs, see [Overview of Amazon Q Business API operations](https://docs.aws.amazon.com/amazonq/latest/business-use-dg/api-ref.html#api-overview).

For information about the IAM access control permissions you need to use this API, see [IAM roles for Amazon Q Business](https://docs.aws.amazon.com/amazonq/latest/business-use-dg/iam-roles.html)in the Amazon Q Business User Guide.

The following resources provide additional information about using the Amazon Q Business API:

- [Setting up for Amazon Q Business](https://docs.aws.amazon.com/amazonq/latest/business-use-dg/setting-up.html)
- [Amazon Q Business CLI Reference](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/qbusiness/index.html)
- [AWS General Reference](https://docs.aws.amazon.com/general/latest/gr/amazonq.html)

### Actions

- [AssociatePermission](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_AssociatePermission.html): Adds or updates a permission policy for a Amazon Q Business application, allowing cross-account access for an ISV.
- [BatchDeleteDocument](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_BatchDeleteDocument.html): Asynchronously deletes one or more documents added using the BatchPutDocument API from an Amazon Q Business index.
- [BatchPutDocument](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_BatchPutDocument.html): Adds one or more documents to an Amazon Q Business index.
- [CancelSubscription](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_CancelSubscription.html): Unsubscribes a user or a group from their pricing tier in an Amazon Q Business application.
- [Chat](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_Chat.html): Starts or continues a streaming Amazon Q Business conversation.
- [ChatSync](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_ChatSync.html): Starts or continues a non-streaming Amazon Q Business conversation.
- [CheckDocumentAccess](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_CheckDocumentAccess.html): Verifies if a user has access permissions for a specified document and returns the actual ACL attached to the document.
- [CreateAnonymousWebExperienceUrl](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_CreateAnonymousWebExperienceUrl.html): Creates a unique URL for anonymous Amazon Q Business web experience.
- [CreateApplication](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_CreateApplication.html): Creates an Amazon Q Business application.
- [CreateChatResponseConfiguration](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_CreateChatResponseConfiguration.html): Creates a new chat response configuration for an Amazon Q Business application.
- [CreateDataAccessor](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_CreateDataAccessor.html): Creates a new data accessor for an ISV to access data from a Amazon Q Business application.
- [CreateDataSource](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_CreateDataSource.html): Creates a data source connector for an Amazon Q Business application.
- [CreateIndex](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_CreateIndex.html): Creates an Amazon Q Business index.
- [CreatePlugin](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_CreatePlugin.html): Creates an Amazon Q Business plugin.
- [CreateRetriever](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_CreateRetriever.html): Adds a retriever to your Amazon Q Business application.
- [CreateSubscription](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_CreateSubscription.html): Subscribes an IAM Identity Center user or a group to a pricing tier for an Amazon Q Business application.
- [CreateUser](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_CreateUser.html): Creates a universally unique identifier (UUID) mapped to a list of local user ids within an application.
- [CreateWebExperience](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_CreateWebExperience.html): Creates an Amazon Q Business web experience.
- [DeleteApplication](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DeleteApplication.html): Deletes an Amazon Q Business application.
- [DeleteAttachment](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DeleteAttachment.html): Deletes an attachment associated with a specific Amazon Q Business conversation.
- [DeleteChatControlsConfiguration](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DeleteChatControlsConfiguration.html): Deletes chat controls configured for an existing Amazon Q Business application.
- [DeleteChatResponseConfiguration](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DeleteChatResponseConfiguration.html): Deletes a specified chat response configuration from an Amazon Q Business application.
- [DeleteConversation](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DeleteConversation.html): Deletes an Amazon Q Business web experience conversation.
- [DeleteDataAccessor](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DeleteDataAccessor.html): Deletes a specified data accessor.
- [DeleteDataSource](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DeleteDataSource.html): Deletes an Amazon Q Business data source connector.
- [DeleteGroup](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DeleteGroup.html): Deletes a group so that all users and sub groups that belong to the group can no longer access documents only available to that group.
- [DeleteIndex](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DeleteIndex.html): Deletes an Amazon Q Business index.
- [DeletePlugin](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DeletePlugin.html): Deletes an Amazon Q Business plugin.
- [DeleteRetriever](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DeleteRetriever.html): Deletes the retriever used by an Amazon Q Business application.
- [DeleteUser](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DeleteUser.html): Deletes a user by email id.
- [DeleteWebExperience](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DeleteWebExperience.html): Deletes an Amazon Q Business web experience.
- [DisassociatePermission](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DisassociatePermission.html): Removes a permission policy from a Amazon Q Business application, revoking the cross-account access that was previously granted to an ISV.
- [GetApplication](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_GetApplication.html): Gets information about an existing Amazon Q Business application.
- [GetChatControlsConfiguration](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_GetChatControlsConfiguration.html): Gets information about chat controls configured for an existing Amazon Q Business application.
- [GetChatResponseConfiguration](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_GetChatResponseConfiguration.html): Retrieves detailed information about a specific chat response configuration from an Amazon Q Business application.
- [GetDataAccessor](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_GetDataAccessor.html): Retrieves information about a specified data accessor.
- [GetDataSource](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_GetDataSource.html): Gets information about an existing Amazon Q Business data source connector.
- [GetDocumentContent](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_GetDocumentContent.html): Retrieves the content of a document that was ingested into Amazon Q Business.
- [GetGroup](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_GetGroup.html): Describes a group by group name.
- [GetIndex](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_GetIndex.html): Gets information about an existing Amazon Q Business index.
- [GetMedia](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_GetMedia.html): Returns the image bytes corresponding to a media object.
- [GetPlugin](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_GetPlugin.html): Gets information about an existing Amazon Q Business plugin.
- [GetPolicy](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_GetPolicy.html): Retrieves the current permission policy for a Amazon Q Business application.
- [GetRetriever](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_GetRetriever.html): Gets information about an existing retriever used by an Amazon Q Business application.
- [GetUser](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_GetUser.html): Describes the universally unique identifier (UUID) associated with a local user in a data source.
- [GetWebExperience](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_GetWebExperience.html): Gets information about an existing Amazon Q Business web experience.
- [ListApplications](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_ListApplications.html): Lists Amazon Q Business applications.
- [ListAttachments](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_ListAttachments.html): Gets a list of attachments associated with an Amazon Q Business web experience or a list of attachements associated with a specific Amazon Q Business conversation.
- [ListChatResponseConfigurations](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_ListChatResponseConfigurations.html): Retrieves a list of all chat response configurations available in a specified Amazon Q Business application.
- [ListConversations](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_ListConversations.html): Lists one or more Amazon Q Business conversations.
- [ListDataAccessors](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_ListDataAccessors.html): Lists the data accessors for a Amazon Q Business application.
- [ListDataSources](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_ListDataSources.html): Lists the Amazon Q Business data source connectors that you have created.
- [ListDataSourceSyncJobs](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_ListDataSourceSyncJobs.html): Get information about an Amazon Q Business data source connector synchronization.
- [ListDocuments](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_ListDocuments.html): A list of documents attached to an index.
- [ListGroups](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_ListGroups.html): Provides a list of groups that are mapped to users.
- [ListIndices](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_ListIndices.html): Lists the Amazon Q Business indices you have created.
- [ListMessages](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_ListMessages.html): Gets a list of messages associated with an Amazon Q Business web experience.
- [ListPluginActions](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_ListPluginActions.html): Lists configured Amazon Q Business actions for a specific plugin in an Amazon Q Business application.
- [ListPlugins](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_ListPlugins.html): Lists configured Amazon Q Business plugins.
- [ListPluginTypeActions](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_ListPluginTypeActions.html): Lists configured Amazon Q Business actions for any plugin typeâboth built-in and custom.
- [ListPluginTypeMetadata](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_ListPluginTypeMetadata.html): Lists metadata for all Amazon Q Business plugin types.
- [ListRetrievers](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_ListRetrievers.html): Lists the retriever used by an Amazon Q Business application.
- [ListSubscriptions](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_ListSubscriptions.html): Lists all subscriptions created in an Amazon Q Business application.
- [ListTagsForResource](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_ListTagsForResource.html): Gets a list of tags associated with a specified resource.
- [ListWebExperiences](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_ListWebExperiences.html): Lists one or more Amazon Q Business Web Experiences.
- [PutFeedback](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_PutFeedback.html): Enables your end user to provide feedback on their Amazon Q Business generated chat responses.
- [PutGroup](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_PutGroup.html): Create, or updates, a mapping of usersâwho have access to a documentâto groups.
- [SearchRelevantContent](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_SearchRelevantContent.html): Searches for relevant content in a Amazon Q Business application based on a query.
- [StartDataSourceSyncJob](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_StartDataSourceSyncJob.html): Starts a data source connector synchronization job.
- [StopDataSourceSyncJob](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_StopDataSourceSyncJob.html): Stops an Amazon Q Business data source connector synchronization job already in progress.
- [TagResource](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_TagResource.html): Adds the specified tag to the specified Amazon Q Business application or data source resource.
- [UntagResource](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_UntagResource.html): Removes a tag from an Amazon Q Business application or a data source.
- [UpdateApplication](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_UpdateApplication.html): Updates an existing Amazon Q Business application.
- [UpdateChatControlsConfiguration](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_UpdateChatControlsConfiguration.html): Updates a set of chat controls configured for an existing Amazon Q Business application.
- [UpdateChatResponseConfiguration](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_UpdateChatResponseConfiguration.html): Updates an existing chat response configuration in an Amazon Q Business application.
- [UpdateDataAccessor](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_UpdateDataAccessor.html): Updates an existing data accessor.
- [UpdateDataSource](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_UpdateDataSource.html): Updates an existing Amazon Q Business data source connector.
- [UpdateIndex](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_UpdateIndex.html): Updates an Amazon Q Business index.
- [UpdatePlugin](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_UpdatePlugin.html): Updates an Amazon Q Business plugin.
- [UpdateRetriever](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_UpdateRetriever.html): Updates the retriever used for your Amazon Q Business application.
- [UpdateSubscription](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_UpdateSubscription.html): Updates the pricing tier for an Amazon Q Business subscription.
- [UpdateUser](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_UpdateUser.html): Updates a information associated with a user id.
- [UpdateWebExperience](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_UpdateWebExperience.html): Updates an Amazon Q Business web experience.

### Data Types

- [AccessConfiguration](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_AccessConfiguration.html): Used to configure access permissions for a document.
- [AccessControl](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_AccessControl.html): A list of principals.
- [ActionConfiguration](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_ActionConfiguration.html): Specifies an allowed action and its associated filter configuration.
- [ActionExecution](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_ActionExecution.html): Performs an Amazon Q Business plugin action during a non-streaming chat conversation.
- [ActionExecutionEvent](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_ActionExecutionEvent.html): A request from an end user signalling an intent to perform an Amazon Q Business plugin action during a streaming chat.
- [ActionExecutionPayloadField](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_ActionExecutionPayloadField.html): A user input field in an plugin action execution payload.
- [ActionFilterConfiguration](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_ActionFilterConfiguration.html): Specifies filters to apply to an allowed action.
- [ActionReview](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_ActionReview.html): An output event that Amazon Q Business returns to an user who wants to perform a plugin action during a non-streaming chat conversation.
- [ActionReviewEvent](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_ActionReviewEvent.html): An output event that Amazon Q Business returns to an user who wants to perform a plugin action during a streaming chat conversation.
- [ActionReviewPayloadField](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_ActionReviewPayloadField.html): A user input field in an plugin action review payload.
- [ActionReviewPayloadFieldAllowedValue](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_ActionReviewPayloadFieldAllowedValue.html): Information about the field values that an end user can use to provide to Amazon Q Business for Amazon Q Business to perform the requested plugin action.
- [ActionSummary](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_ActionSummary.html): Summary information for an Amazon Q Business plugin action.
- [APISchema](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_APISchema.html): Contains details about the OpenAPI schema for a custom plugin.
- [Application](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_Application.html): Summary information for an Amazon Q Business application.
- [AppliedAttachmentsConfiguration](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_AppliedAttachmentsConfiguration.html): Configuration information about the file upload during chat feature for your application.
- [AppliedCreatorModeConfiguration](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_AppliedCreatorModeConfiguration.html): The creator mode specific admin controls configured for an Amazon Q Business application.
- [AppliedOrchestrationConfiguration](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_AppliedOrchestrationConfiguration.html): The chat orchestration specific admin controls configured for an Amazon Q Business application.
- [AssociatedGroup](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_AssociatedGroup.html): Represents a group associated with a given user in the access control system.
- [AssociatedUser](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_AssociatedUser.html): Represents an associated user in the access control system.
- [Attachment](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_Attachment.html): An attachment in an Amazon Q Business conversation.
- [AttachmentInput](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_AttachmentInput.html): This is either a file directly uploaded into a web experience chat or a reference to an existing attachment that is part of a web experience chat.
- [AttachmentInputEvent](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_AttachmentInputEvent.html): A file input event activated by a end user request to upload files into their web experience chat.
- [AttachmentOutput](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_AttachmentOutput.html): The details of a file uploaded during chat.
- [AttachmentsConfiguration](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_AttachmentsConfiguration.html): Configuration information for the file upload during chat feature.
- [AttributeFilter](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_AttributeFilter.html): Enables filtering of responses based on document attributes or metadata fields.
- [AudioExtractionConfiguration](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_AudioExtractionConfiguration.html): Configuration settings for audio content extraction and processing.
- [AudioSourceDetails](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_AudioSourceDetails.html): Details about an audio source, including its identifier, format, and time information.
- [AuthChallengeRequest](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_AuthChallengeRequest.html): A request made by Amazon Q Business to a third paty authentication server to authenticate a custom plugin user.
- [AuthChallengeRequestEvent](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_AuthChallengeRequestEvent.html): An authentication verification event activated by an end user request to use a custom plugin.
- [AuthChallengeResponse](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_AuthChallengeResponse.html): Contains details of the authentication information received from a third party authentication server in response to an authentication challenge.
- [AuthChallengeResponseEvent](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_AuthChallengeResponseEvent.html): An authentication verification event response by a third party authentication server to Amazon Q Business.
- [AutoSubscriptionConfiguration](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_AutoSubscriptionConfiguration.html): Subscription configuration information for an Amazon Q Business application using IAM identity federation for user management.
- [BasicAuthConfiguration](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_BasicAuthConfiguration.html): Information about the basic authentication credentials used to configure a plugin.
- [BlockedPhrasesConfiguration](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_BlockedPhrasesConfiguration.html): Provides information about the phrases blocked from chat by your chat control configuration.
- [BlockedPhrasesConfigurationUpdate](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_BlockedPhrasesConfigurationUpdate.html): Updates a blocked phrases configuration in your Amazon Q Business application.
- [BrowserExtensionConfiguration](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_BrowserExtensionConfiguration.html): The container for browser extension configuration for an Amazon Q Business web experience.
- [ChatInputStream](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_ChatInputStream.html): The streaming input for the Chat API.
- [ChatModeConfiguration](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_ChatModeConfiguration.html): Configuration information for Amazon Q Business conversation modes.
- [ChatOutputStream](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_ChatOutputStream.html): The streaming output for the Chat API.
- [ChatResponseConfiguration](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_ChatResponseConfiguration.html): Configuration details that define how Amazon Q Business generates and formats responses to user queries in chat interactions.
- [ChatResponseConfigurationDetail](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_ChatResponseConfigurationDetail.html): Detailed information about a chat response configuration, including comprehensive settings and parameters that define how Amazon Q Business generates and formats responses.
- [ConfigurationEvent](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_ConfigurationEvent.html): A configuration event activated by an end user request to select a specific chat mode.
- [ContentBlockerRule](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_ContentBlockerRule.html): A rule for configuring how Amazon Q Business responds when it encounters a a blocked topic.
- [ContentRetrievalRule](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_ContentRetrievalRule.html): Rules for retrieving content from data sources connected to a Amazon Q Business application for a specific topic control configuration.
- [ContentSource](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_ContentSource.html): Specifies the source of content to search in.
- [Conversation](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_Conversation.html): A conversation in an Amazon Q Business application.
- [ConversationSource](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_ConversationSource.html): The source reference for an existing attachment in an existing conversation.
- [CopyFromSource](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_CopyFromSource.html): The source reference for an existing attachment.
- [CreatorModeConfiguration](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_CreatorModeConfiguration.html): Configuration information required to invoke chat in CREATOR_MODE.
- [CustomizationConfiguration](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_CustomizationConfiguration.html): Contains the configuration information to customize the logo, font, and color of an Amazon Q Business web experience with individual files for each property or a CSS file for them all.
- [CustomPluginConfiguration](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_CustomPluginConfiguration.html): Configuration information required to create a custom plugin.
- [DataAccessor](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DataAccessor.html): Provides summary information about a data accessor.
- [DataAccessorAuthenticationConfiguration](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DataAccessorAuthenticationConfiguration.html): A union type that contains the specific authentication configuration based on the authentication type selected.
- [DataAccessorAuthenticationDetail](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DataAccessorAuthenticationDetail.html): Contains the authentication configuration details for a data accessor.
- [DataAccessorIdcTrustedTokenIssuerConfiguration](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DataAccessorIdcTrustedTokenIssuerConfiguration.html): Configuration details for IAM Identity Center Trusted Token Issuer (TTI) authentication.
- [DataSource](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DataSource.html): A data source in an Amazon Q Business application.
- [DataSourceSyncJob](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DataSourceSyncJob.html): Provides information about an Amazon Q Business data source connector synchronization job.
- [DataSourceSyncJobMetrics](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DataSourceSyncJobMetrics.html): Maps a batch delete document request to a specific Amazon Q Business data source connector sync job.
- [DataSourceVpcConfiguration](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DataSourceVpcConfiguration.html): Provides configuration information needed to connect to an Amazon VPC (Virtual Private Cloud).
- [DateAttributeBoostingConfiguration](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DateAttributeBoostingConfiguration.html): Provides information on boosting DATE type document attributes.
- [DeleteDocument](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DeleteDocument.html): A document deleted from an Amazon Q Business data source connector.
- [Document](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_Document.html): A document in an Amazon Q Business application.
- [DocumentAcl](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DocumentAcl.html): Represents the Access Control List (ACL) for a document, containing both allowlist and denylist conditions.
- [DocumentAclCondition](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DocumentAclCondition.html): Represents a condition in the document's ACL, specifying access rules for users and groups.
- [DocumentAclGroup](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DocumentAclGroup.html): Represents a group in the document's ACL, used to define access permissions for multiple users collectively.
- [DocumentAclMembership](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DocumentAclMembership.html): Represents membership rules in the document's ACL, defining how users or groups are associated with access permissions.
- [DocumentAclUser](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DocumentAclUser.html): Represents a user in the document's ACL, used to define access permissions for individual users.
- [DocumentAttribute](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DocumentAttribute.html): A document attribute or metadata field.
- [DocumentAttributeBoostingConfiguration](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DocumentAttributeBoostingConfiguration.html): Provides information on boosting supported Amazon Q Business document attribute types.
- [DocumentAttributeCondition](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DocumentAttributeCondition.html): The condition used for the target document attribute or metadata field when ingesting documents into Amazon Q Business.
- [DocumentAttributeConfiguration](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DocumentAttributeConfiguration.html): Configuration information for document attributes.
- [DocumentAttributeTarget](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DocumentAttributeTarget.html): The target document attribute or metadata field you want to alter when ingesting documents into Amazon Q Business.
- [DocumentAttributeValue](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DocumentAttributeValue.html): The value of a document attribute.
- [DocumentContent](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DocumentContent.html): The contents of a document.
- [DocumentDetails](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DocumentDetails.html): The details of a document within an Amazon Q Business index.
- [DocumentEnrichmentConfiguration](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DocumentEnrichmentConfiguration.html): Provides the configuration information for altering document metadata and content during the document ingestion process.
- [EligibleDataSource](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_EligibleDataSource.html): The identifier of the data source Amazon Q Business will generate responses from.
- [EncryptionConfiguration](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_EncryptionConfiguration.html): Provides the identifier of the AWS KMS key used to encrypt data indexed by Amazon Q Business.
- [EndOfInputEvent](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_EndOfInputEvent.html): The end of the streaming input for the Chat API.
- [ErrorDetail](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_ErrorDetail.html): Provides information about a Amazon Q Business request error.
- [FailedAttachmentEvent](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_FailedAttachmentEvent.html): A failed file upload during web experience chat.
- [FailedDocument](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_FailedDocument.html): A list of documents that could not be removed from an Amazon Q Business index.
- [GroupMembers](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_GroupMembers.html): A list of users or sub groups that belong to a group.
- [GroupStatusDetail](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_GroupStatusDetail.html): Provides the details of a group's status.
- [GroupSummary](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_GroupSummary.html): Summary information for groups.
- [HallucinationReductionConfiguration](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_HallucinationReductionConfiguration.html): Configuration information required to setup hallucination reduction.
- [HookConfiguration](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_HookConfiguration.html): Provides the configuration information for invoking a Lambda function in AWS Lambda to alter document metadata and content when ingesting documents into Amazon Q Business.
- [IdcAuthConfiguration](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_IdcAuthConfiguration.html): Information about the AWS IAM Identity Center Application used to configure authentication for a plugin.
- [IdentityProviderConfiguration](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_IdentityProviderConfiguration.html): Provides information about the identity provider (IdP) used to authenticate end users of an Amazon Q Business web experience.
- [ImageExtractionConfiguration](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_ImageExtractionConfiguration.html): The configuration for extracting semantic meaning from images in documents.
- [ImageSourceDetails](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_ImageSourceDetails.html): Details about an image source, including its identifier and format.
- [Index](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_Index.html): Summary information for your Amazon Q Business index.
- [IndexCapacityConfiguration](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_IndexCapacityConfiguration.html): Provides information about index capacity configuration.
- [IndexStatistics](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_IndexStatistics.html): Provides information about the number of documents in an index.
- [InlineDocumentEnrichmentConfiguration](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_InlineDocumentEnrichmentConfiguration.html): Provides the configuration information for applying basic logic to alter document metadata and content when ingesting documents into Amazon Q Business.
- [InstructionCollection](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_InstructionCollection.html): A set of instructions that define how Amazon Q Business should generate and format responses to user queries.
- [KendraIndexConfiguration](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_KendraIndexConfiguration.html): Stores an Amazon Kendra index as a retriever.
- [MediaExtractionConfiguration](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_MediaExtractionConfiguration.html): The configuration for extracting information from media in documents.
- [MemberGroup](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_MemberGroup.html): The sub groups that belong to a group.
- [MemberUser](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_MemberUser.html): The users that belong to a group.
- [Message](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_Message.html): A message in an Amazon Q Business web experience.
- [MessageUsefulnessFeedback](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_MessageUsefulnessFeedback.html): End user feedback on an AI-generated web experience chat message usefulness.
- [MetadataEvent](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_MetadataEvent.html): A metadata event for a AI-generated text output message in a Amazon Q Business conversation, containing associated metadata generated.
- [NativeIndexConfiguration](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_NativeIndexConfiguration.html): Configuration information for an Amazon Q Business index.
- [NoAuthConfiguration](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_NoAuthConfiguration.html): Information about invoking a custom plugin without any authentication or authorization requirement.
- [NumberAttributeBoostingConfiguration](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_NumberAttributeBoostingConfiguration.html): Provides information on boosting NUMBER type document attributes.
- [OAuth2ClientCredentialConfiguration](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_OAuth2ClientCredentialConfiguration.html): Information about the OAuth 2.0 authentication credential/token used to configure a plugin.
- [OpenIDConnectProviderConfiguration](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_OpenIDConnectProviderConfiguration.html): Information about the OIDC-compliant identity provider (IdP) used to authenticate end users of an Amazon Q Business web experience.
- [OrchestrationConfiguration](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_OrchestrationConfiguration.html): Configuration information required to enable chat orchestration for your Amazon Q Business application.
- [PermissionCondition](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_PermissionCondition.html): Defines a condition that restricts when a permission is effective.
- [PersonalizationConfiguration](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_PersonalizationConfiguration.html): Configuration information about chat response personalization.
- [Plugin](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_Plugin.html): Information about an Amazon Q Business plugin and its configuration.
- [PluginAuthConfiguration](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_PluginAuthConfiguration.html): Authentication configuration information for an Amazon Q Business plugin.
- [PluginConfiguration](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_PluginConfiguration.html): Configuration information required to invoke chat in PLUGIN_MODE.
- [PluginTypeMetadataSummary](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_PluginTypeMetadataSummary.html): Summary metadata information for a Amazon Q Business plugin.
- [Principal](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_Principal.html): Provides user and group information used for filtering documents to use for generating Amazon Q Business conversation responses.
- [PrincipalGroup](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_PrincipalGroup.html): Provides information about a group associated with the principal.
- [PrincipalUser](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_PrincipalUser.html): Provides information about a user associated with a principal.
- [QAppsConfiguration](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_QAppsConfiguration.html): Configuration information about Amazon Q Apps.
- [QuickSightConfiguration](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_QuickSightConfiguration.html): The Amazon Quick configuration for an Amazon Q Business application that uses Quick as the identity provider.
- [RelevantContent](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_RelevantContent.html): Represents a piece of content that is relevant to a search query.
- [ResponseConfiguration](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_ResponseConfiguration.html): Configuration settings to define how Amazon Q Business generates and formats responses to user queries.
- [Retriever](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_Retriever.html): Summary information for the retriever used for your Amazon Q Business application.
- [RetrieverConfiguration](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_RetrieverConfiguration.html): Provides information on how the retriever used for your Amazon Q Business application is configured.
- [RetrieverContentSource](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_RetrieverContentSource.html): Specifies a retriever as the content source for a search.
- [Rule](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_Rule.html): Guardrail rules for an Amazon Q Business application.
- [RuleConfiguration](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_RuleConfiguration.html): Provides configuration information about a rule.
- [S3](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_S3.html): Information required for Amazon Q Business to find a specific file in an Amazon S3 bucket.
- [SamlConfiguration](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_SamlConfiguration.html): Provides the SAML 2.0 compliant identity provider (IdP) configuration information Amazon Q Business needs to deploy a Amazon Q Business web experience.
- [SamlProviderConfiguration](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_SamlProviderConfiguration.html): Information about the SAML 2.0-compliant identity provider (IdP) used to authenticate end users of an Amazon Q Business web experience.
- [ScoreAttributes](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_ScoreAttributes.html): Provides information about the relevance score of content.
- [SnippetExcerpt](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_SnippetExcerpt.html): Contains the relevant text excerpt from a source that was used to generate a citation text segment in an Amazon Q Business chat response.
- [SourceAttribution](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_SourceAttribution.html): The documents used to generate an Amazon Q Business web experience response.
- [SourceDetails](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_SourceDetails.html): Container for details about different types of media sources (image, audio, or video).
- [StringAttributeBoostingConfiguration](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_StringAttributeBoostingConfiguration.html): Provides information on boosting STRING type document attributes.
- [StringListAttributeBoostingConfiguration](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_StringListAttributeBoostingConfiguration.html): Provides information on boosting STRING_LIST type document attributes.
- [Subscription](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_Subscription.html): Information about an Amazon Q Business subscription.
- [SubscriptionDetails](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_SubscriptionDetails.html): The details of an Amazon Q Business subscription.
- [SubscriptionPrincipal](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_SubscriptionPrincipal.html): A user or group in the IAM Identity Center instance connected to the Amazon Q Business application.
- [Tag](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_Tag.html): A list of key/value pairs that identify an index, FAQ, or data source.
- [TextDocumentStatistics](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_TextDocumentStatistics.html): Provides information about text documents in an index.
- [TextInputEvent](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_TextInputEvent.html): An input event for a end user message in an Amazon Q Business web experience.
- [TextOutputEvent](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_TextOutputEvent.html): An output event for an AI-generated response in an Amazon Q Business web experience.
- [TextSegment](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_TextSegment.html): Provides information about a text extract in a chat response that can be attributed to a source document.
- [TopicConfiguration](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_TopicConfiguration.html): The topic specific controls configured for an Amazon Q Business application.
- [UserAlias](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_UserAlias.html): Aliases attached to a user id within an Amazon Q Business application.
- [UsersAndGroups](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_UsersAndGroups.html): Provides information about users and group names associated with a topic control rule.
- [ValidationExceptionField](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_ValidationExceptionField.html): The input failed to meet the constraints specified by Amazon Q Business in a specified field.
- [VideoExtractionConfiguration](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_VideoExtractionConfiguration.html): Configuration settings for video content extraction and processing.
- [VideoSourceDetails](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_VideoSourceDetails.html): Details about a video source, including its identifier, format, and time information.
- [WebExperience](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_WebExperience.html): Provides information for an Amazon Q Business web experience.
- [WebExperienceAuthConfiguration](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_WebExperienceAuthConfiguration.html): Provides the authorization configuration information needed to deploy a Amazon Q Business web experience to end users.

## [QApps](https://docs.aws.amazon.com/amazonq/latest/api-reference/Welcome_QApps.html)

The Amazon Q Apps feature capability within Amazon Q Business allows web experience users to create lightweight, purpose-built AI apps to fulfill specific tasks from within their web experience. For example, users can create a Q App that exclusively generates marketing-related content to improve your marketing team's productivity or a Q App for writing customer emails and creating promotional content using a certain style of voice, tone, and branding. For more information on the capabilities, see [Amazon Q Apps capabilities](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/deploy-experience-iam-role.html#q-apps-actions)in the Amazon Q Business User Guide.

For an overview of the Amazon Q App APIs, see [Overview of Amazon Q Apps API operations](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_Operations_QApps.html).

For information about the IAM access control permissions you need to use the Amazon Q Apps API, see [IAM role for the Amazon Q Business web experience including Amazon Q Apps](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/deploy-experience-iam-role.html)in the Amazon Q Business User Guide.

### Actions

- [AssociateLibraryItemReview](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_qapps_AssociateLibraryItemReview.html): Associates a rating or review for a library item with the user submitting the request.
- [AssociateQAppWithUser](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_qapps_AssociateQAppWithUser.html): This operation creates a link between the user's identity calling the operation and a specific Q App.
- [BatchCreateCategory](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_qapps_BatchCreateCategory.html): Creates Categories for the Amazon Q Business application environment instance.
- [BatchDeleteCategory](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_qapps_BatchDeleteCategory.html): Deletes Categories for the Amazon Q Business application environment instance.
- [BatchUpdateCategory](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_qapps_BatchUpdateCategory.html): Updates Categories for the Amazon Q Business application environment instance.
- [CreateLibraryItem](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_qapps_CreateLibraryItem.html): Creates a new library item for an Amazon Q App, allowing it to be discovered and used by other allowed users.
- [CreatePresignedUrl](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_qapps_CreatePresignedUrl.html): Creates a presigned URL for an S3 POST operation to upload a file.
- [CreateQApp](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_qapps_CreateQApp.html): Creates a new Amazon Q App based on the provided definition.
- [DeleteLibraryItem](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_qapps_DeleteLibraryItem.html): Deletes a library item for an Amazon Q App, removing it from the library so it can no longer be discovered or used by other users.
- [DeleteQApp](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_qapps_DeleteQApp.html): Deletes an Amazon Q App owned by the user.
- [DescribeQAppPermissions](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_qapps_DescribeQAppPermissions.html): Describes read permissions for a Amazon Q App in Amazon Q Business application environment instance.
- [DisassociateLibraryItemReview](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_qapps_DisassociateLibraryItemReview.html): Removes a rating or review previously submitted by the user for a library item.
- [DisassociateQAppFromUser](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_qapps_DisassociateQAppFromUser.html): Disassociates a Q App from a user removing the user's access to run the Q App.
- [ExportQAppSessionData](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_qapps_ExportQAppSessionData.html): Exports the collected data of a Q App data collection session.
- [GetLibraryItem](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_qapps_GetLibraryItem.html): Retrieves details about a library item for an Amazon Q App, including its metadata, categories, ratings, and usage statistics.
- [GetQApp](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_qapps_GetQApp.html): Retrieves the full details of an Q App, including its definition specifying the cards and flow.
- [GetQAppSession](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_qapps_GetQAppSession.html): Retrieves the current state and results for an active session of an Amazon Q App.
- [GetQAppSessionMetadata](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_qapps_GetQAppSessionMetadata.html): Retrieves the current configuration of a Q App session.
- [ImportDocument](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_qapps_ImportDocument.html): Uploads a file that can then be used either as a default in a FileUploadCard from Q App definition or as a file that is used inside a single Q App run.
- [ListCategories](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_qapps_ListCategories.html): Lists the categories of a Amazon Q Business application environment instance.
- [ListLibraryItems](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_qapps_ListLibraryItems.html): Lists the library items for Amazon Q Apps that are published and available for users in your AWS account.
- [ListQApps](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_qapps_ListQApps.html): Lists the Amazon Q Apps owned by or associated with the user either because they created it or because they used it from the library in the past.
- [ListQAppSessionData](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_qapps_ListQAppSessionData.html): Lists the collected data of a Q App data collection session.
- [ListTagsForResource](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_qapps_ListTagsForResource.html): Lists the tags associated with an Amazon Q Apps resource.
- [PredictQApp](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_qapps_PredictQApp.html): Generates an Amazon Q App definition based on either a conversation or a problem statement provided as input.The resulting app definition can be used to call CreateQApp.
- [StartQAppSession](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_qapps_StartQAppSession.html): Starts a new session for an Amazon Q App, allowing inputs to be provided and the app to be run.
- [StopQAppSession](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_qapps_StopQAppSession.html): Stops an active session for an Amazon Q App.This deletes all data related to the session and makes it invalid for future uses.
- [TagResource](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_qapps_TagResource.html): Associates tags with an Amazon Q Apps resource.
- [UntagResource](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_qapps_UntagResource.html): Disassociates tags from an Amazon Q Apps resource.
- [UpdateLibraryItem](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_qapps_UpdateLibraryItem.html): Updates the library item for an Amazon Q App.
- [UpdateLibraryItemMetadata](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_qapps_UpdateLibraryItemMetadata.html): Updates the verification status of a library item for an Amazon Q App.
- [UpdateQApp](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_qapps_UpdateQApp.html): Updates an existing Amazon Q App, allowing modifications to its title, description, and definition.
- [UpdateQAppPermissions](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_qapps_UpdateQAppPermissions.html): Updates read permissions for a Amazon Q App in Amazon Q Business application environment instance.
- [UpdateQAppSession](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_qapps_UpdateQAppSession.html): Updates the session for a given Q App sessionId.
- [UpdateQAppSessionMetadata](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_qapps_UpdateQAppSessionMetadata.html): Updates the configuration metadata of a session for a given Q App sessionId.

### Data Types

- [AppDefinition](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_qapps_AppDefinition.html): The definition of the Q App, specifying the cards and flow.
- [AppDefinitionInput](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_qapps_AppDefinitionInput.html): The input for defining an Q App.
- [AttributeFilter](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_qapps_AttributeFilter.html): The filter criteria used on responses based on document attributes or metadata fields.
- [BatchCreateCategoryInputCategory](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_qapps_BatchCreateCategoryInputCategory.html): The category object to be created.
- [Card](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_qapps_Card.html): A card representing a component or step in an Amazon Q App's flow.
- [CardInput](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_qapps_CardInput.html): The properties defining an input card in an Amazon Q App.
- [CardStatus](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_qapps_CardStatus.html): The current status and value of a card in an active Amazon Q App session.
- [CardValue](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_qapps_CardValue.html): The value or result associated with a card in a Amazon Q App session.
- [Category](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_qapps_Category.html): A category used to classify and filter library items for Amazon Q Apps.
- [CategoryInput](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_qapps_CategoryInput.html): A label that web experience users associate with a library item.
- [ConversationMessage](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_qapps_ConversationMessage.html): A message in a conversation, used as input for generating an Amazon Q App definition.
- [DocumentAttribute](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_qapps_DocumentAttribute.html): A document attribute or metadata field.
- [DocumentAttributeValue](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_qapps_DocumentAttributeValue.html): The value of a document attribute.
- [FileUploadCard](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_qapps_FileUploadCard.html): A card in an Amazon Q App that allows the user to upload a file.
- [FileUploadCardInput](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_qapps_FileUploadCardInput.html): Represents a file upload card.
- [FormInputCard](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_qapps_FormInputCard.html): A card in an Amazon Q App that allows the user to submit a response.
- [FormInputCardInput](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_qapps_FormInputCardInput.html): Represents a form input card for an Amazon Q App.
- [FormInputCardMetadata](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_qapps_FormInputCardMetadata.html): The metadata of the form input card.
- [LibraryItemMember](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_qapps_LibraryItemMember.html): A library item is a snapshot of an Amazon Q App that can be published so the users in their Amazon Q Apps library can discover it, clone it, and run it.
- [PermissionInput](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_qapps_PermissionInput.html): The permission to grant or revoke for a Amazon Q App.
- [PermissionOutput](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_qapps_PermissionOutput.html): The permission granted to the Amazon Q App.
- [PredictAppDefinition](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_qapps_PredictAppDefinition.html): The definition of an Amazon Q App generated based on input such as a conversation or problem statement.
- [PredictQAppInputOptions](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_qapps_PredictQAppInputOptions.html): The input options for generating an Q App definition.
- [PrincipalOutput](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_qapps_PrincipalOutput.html): The principal for which the permission applies.
- [QAppSessionData](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_qapps_QAppSessionData.html): The response collected for a Amazon Q App session.
- [QPluginCard](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_qapps_QPluginCard.html): A card in an Q App that integrates with a third-party plugin or service.
- [QPluginCardInput](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_qapps_QPluginCardInput.html): The input shape for defining a plugin card in an Amazon Q App.
- [QQueryCard](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_qapps_QQueryCard.html): A card in a Amazon Q App that generates a response based on the Amazon Q Business service.
- [QQueryCardInput](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_qapps_QQueryCardInput.html): The input shape for defining a query card in an Amazon Q App.
- [SessionSharingConfiguration](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_qapps_SessionSharingConfiguration.html): The sharing configuration of an Amazon Q App data collection session.
- [Submission](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_qapps_Submission.html): A record created when a user submits a form card.
- [SubmissionMutation](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_qapps_SubmissionMutation.html): Represents an action performed on a submission.
- [TextInputCard](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_qapps_TextInputCard.html): A card in an Amazon Q App that allows the user to input text.
- [TextInputCardInput](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_qapps_TextInputCardInput.html): The input shape for defining a text input card in an Amazon Q App.
- [User](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_qapps_User.html): A user of an Amazon Q App.
- [UserAppItem](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_qapps_UserAppItem.html): An Amazon Q App associated with a user, either owned by the user or favorited.

## Common

- [Common Parameters](https://docs.aws.amazon.com/amazonq/latest/api-reference/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/amazonq/latest/api-reference/CommonErrors.html)