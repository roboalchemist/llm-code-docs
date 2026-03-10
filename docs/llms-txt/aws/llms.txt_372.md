# Source: https://docs.aws.amazon.com/entityresolution/latest/apireference/llms.txt

# AWS Entity Resolution API Reference

> Welcome to the AWS Entity Resolution API Reference.

- [Welcome](https://docs.aws.amazon.com/entityresolution/latest/apireference/Welcome.html)
- [Common Parameters](https://docs.aws.amazon.com/entityresolution/latest/apireference/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/entityresolution/latest/apireference/CommonErrors.html)

## [Actions](https://docs.aws.amazon.com/entityresolution/latest/apireference/API_Operations.html)

- [AddPolicyStatement](https://docs.aws.amazon.com/entityresolution/latest/apireference/API_AddPolicyStatement.html): Adds a policy statement object.
- [BatchDeleteUniqueId](https://docs.aws.amazon.com/entityresolution/latest/apireference/API_BatchDeleteUniqueId.html): Deletes multiple unique IDs in a matching workflow.
- [CreateIdMappingWorkflow](https://docs.aws.amazon.com/entityresolution/latest/apireference/API_CreateIdMappingWorkflow.html): Creates an IdMappingWorkflow object which stores the configuration of the data processing job to be run.
- [CreateIdNamespace](https://docs.aws.amazon.com/entityresolution/latest/apireference/API_CreateIdNamespace.html): Creates an ID namespace object which will help customers provide metadata explaining their dataset and how to use it.
- [CreateMatchingWorkflow](https://docs.aws.amazon.com/entityresolution/latest/apireference/API_CreateMatchingWorkflow.html): Creates a matching workflow that defines the configuration for a data processing job.
- [CreateSchemaMapping](https://docs.aws.amazon.com/entityresolution/latest/apireference/API_CreateSchemaMapping.html): Creates a schema mapping, which defines the schema of the input customer records table.
- [DeleteIdMappingWorkflow](https://docs.aws.amazon.com/entityresolution/latest/apireference/API_DeleteIdMappingWorkflow.html): Deletes the IdMappingWorkflow with a given name.
- [DeleteIdNamespace](https://docs.aws.amazon.com/entityresolution/latest/apireference/API_DeleteIdNamespace.html): Deletes the IdNamespace with a given name.
- [DeleteMatchingWorkflow](https://docs.aws.amazon.com/entityresolution/latest/apireference/API_DeleteMatchingWorkflow.html): Deletes the MatchingWorkflow with a given name.
- [DeletePolicyStatement](https://docs.aws.amazon.com/entityresolution/latest/apireference/API_DeletePolicyStatement.html): Deletes the policy statement.
- [DeleteSchemaMapping](https://docs.aws.amazon.com/entityresolution/latest/apireference/API_DeleteSchemaMapping.html): Deletes the SchemaMapping with a given name.
- [GenerateMatchId](https://docs.aws.amazon.com/entityresolution/latest/apireference/API_GenerateMatchId.html): Generates or retrieves Match IDs for records using a rule-based matching workflow.
- [GetIdMappingJob](https://docs.aws.amazon.com/entityresolution/latest/apireference/API_GetIdMappingJob.html): Returns the status, metrics, and errors (if there are any) that are associated with a job.
- [GetIdMappingWorkflow](https://docs.aws.amazon.com/entityresolution/latest/apireference/API_GetIdMappingWorkflow.html): Returns the IdMappingWorkflow with a given name, if it exists.
- [GetIdNamespace](https://docs.aws.amazon.com/entityresolution/latest/apireference/API_GetIdNamespace.html): Returns the IdNamespace with a given name, if it exists.
- [GetMatchId](https://docs.aws.amazon.com/entityresolution/latest/apireference/API_GetMatchId.html): Returns the corresponding Match ID of a customer record if the record has been processed in a rule-based matching workflow.
- [GetMatchingJob](https://docs.aws.amazon.com/entityresolution/latest/apireference/API_GetMatchingJob.html): Returns the status, metrics, and errors (if there are any) that are associated with a job.
- [GetMatchingWorkflow](https://docs.aws.amazon.com/entityresolution/latest/apireference/API_GetMatchingWorkflow.html): Returns the MatchingWorkflow with a given name, if it exists.
- [GetPolicy](https://docs.aws.amazon.com/entityresolution/latest/apireference/API_GetPolicy.html): Returns the resource-based policy.
- [GetProviderService](https://docs.aws.amazon.com/entityresolution/latest/apireference/API_GetProviderService.html): Returns the ProviderService of a given name.
- [GetSchemaMapping](https://docs.aws.amazon.com/entityresolution/latest/apireference/API_GetSchemaMapping.html): Returns the SchemaMapping of a given name.
- [ListIdMappingJobs](https://docs.aws.amazon.com/entityresolution/latest/apireference/API_ListIdMappingJobs.html): Lists all ID mapping jobs for a given workflow.
- [ListIdMappingWorkflows](https://docs.aws.amazon.com/entityresolution/latest/apireference/API_ListIdMappingWorkflows.html): Returns a list of all the IdMappingWorkflows that have been created for an AWS account.
- [ListIdNamespaces](https://docs.aws.amazon.com/entityresolution/latest/apireference/API_ListIdNamespaces.html): Returns a list of all ID namespaces.
- [ListMatchingJobs](https://docs.aws.amazon.com/entityresolution/latest/apireference/API_ListMatchingJobs.html): Lists all jobs for a given workflow.
- [ListMatchingWorkflows](https://docs.aws.amazon.com/entityresolution/latest/apireference/API_ListMatchingWorkflows.html): Returns a list of all the MatchingWorkflows that have been created for an AWS account.
- [ListProviderServices](https://docs.aws.amazon.com/entityresolution/latest/apireference/API_ListProviderServices.html): Returns a list of all the ProviderServices that are available in this AWS Region.
- [ListSchemaMappings](https://docs.aws.amazon.com/entityresolution/latest/apireference/API_ListSchemaMappings.html): Returns a list of all the SchemaMappings that have been created for an AWS account.
- [ListTagsForResource](https://docs.aws.amazon.com/entityresolution/latest/apireference/API_ListTagsForResource.html): Displays the tags associated with an AWS Entity Resolution resource.
- [PutPolicy](https://docs.aws.amazon.com/entityresolution/latest/apireference/API_PutPolicy.html): Updates the resource-based policy.
- [StartIdMappingJob](https://docs.aws.amazon.com/entityresolution/latest/apireference/API_StartIdMappingJob.html): Starts the IdMappingJob of a workflow.
- [StartMatchingJob](https://docs.aws.amazon.com/entityresolution/latest/apireference/API_StartMatchingJob.html): Starts the MatchingJob of a workflow.
- [TagResource](https://docs.aws.amazon.com/entityresolution/latest/apireference/API_TagResource.html): Assigns one or more tags (key-value pairs) to the specified AWS Entity Resolution resource.
- [UntagResource](https://docs.aws.amazon.com/entityresolution/latest/apireference/API_UntagResource.html): Removes one or more tags from the specified AWS Entity Resolution resource.
- [UpdateIdMappingWorkflow](https://docs.aws.amazon.com/entityresolution/latest/apireference/API_UpdateIdMappingWorkflow.html): Updates an existing IdMappingWorkflow.
- [UpdateIdNamespace](https://docs.aws.amazon.com/entityresolution/latest/apireference/API_UpdateIdNamespace.html): Updates an existing ID namespace.
- [UpdateMatchingWorkflow](https://docs.aws.amazon.com/entityresolution/latest/apireference/API_UpdateMatchingWorkflow.html): Updates an existing matching workflow.
- [UpdateSchemaMapping](https://docs.aws.amazon.com/entityresolution/latest/apireference/API_UpdateSchemaMapping.html): Updates a schema mapping.


## [Data Types](https://docs.aws.amazon.com/entityresolution/latest/apireference/API_Types.html)

- [CustomerProfilesIntegrationConfig](https://docs.aws.amazon.com/entityresolution/latest/apireference/API_CustomerProfilesIntegrationConfig.html): Specifies the configuration for integrating with Customer Profiles.
- [DeletedUniqueId](https://docs.aws.amazon.com/entityresolution/latest/apireference/API_DeletedUniqueId.html): The deleted unique ID.
- [DeleteUniqueIdError](https://docs.aws.amazon.com/entityresolution/latest/apireference/API_DeleteUniqueIdError.html): The error information provided when the delete unique ID operation doesn't complete.
- [ErrorDetails](https://docs.aws.amazon.com/entityresolution/latest/apireference/API_ErrorDetails.html): An object containing an error message, if there was an error.
- [FailedRecord](https://docs.aws.amazon.com/entityresolution/latest/apireference/API_FailedRecord.html): The record that didn't generate a Match ID.
- [IdMappingIncrementalRunConfig](https://docs.aws.amazon.com/entityresolution/latest/apireference/API_IdMappingIncrementalRunConfig.html): Incremental run configuration for an ID mapping workflow.
- [IdMappingJobMetrics](https://docs.aws.amazon.com/entityresolution/latest/apireference/API_IdMappingJobMetrics.html): An object that contains metrics about an ID mapping job, including counts of input records, processed records, and mapped records between source and target identifiers.
- [IdMappingJobOutputSource](https://docs.aws.amazon.com/entityresolution/latest/apireference/API_IdMappingJobOutputSource.html): An object containing KMSArn, outputS3Path, and roleARN.
- [IdMappingRuleBasedProperties](https://docs.aws.amazon.com/entityresolution/latest/apireference/API_IdMappingRuleBasedProperties.html): An object that defines the list of matching rules to run in an ID mapping workflow.
- [IdMappingTechniques](https://docs.aws.amazon.com/entityresolution/latest/apireference/API_IdMappingTechniques.html): An object which defines the ID mapping technique and any additional configurations.
- [IdMappingWorkflowInputSource](https://docs.aws.amazon.com/entityresolution/latest/apireference/API_IdMappingWorkflowInputSource.html): An object containing inputSourceARN, schemaName, and type.
- [IdMappingWorkflowOutputSource](https://docs.aws.amazon.com/entityresolution/latest/apireference/API_IdMappingWorkflowOutputSource.html): The output source for the ID mapping workflow.
- [IdMappingWorkflowSummary](https://docs.aws.amazon.com/entityresolution/latest/apireference/API_IdMappingWorkflowSummary.html): A list of IdMappingWorkflowSummary objects, each of which contain the fields WorkflowName, WorkflowArn, CreatedAt, and UpdatedAt.
- [IdNamespaceIdMappingWorkflowMetadata](https://docs.aws.amazon.com/entityresolution/latest/apireference/API_IdNamespaceIdMappingWorkflowMetadata.html): The settings for the ID namespace for the ID mapping workflow job.
- [IdNamespaceIdMappingWorkflowProperties](https://docs.aws.amazon.com/entityresolution/latest/apireference/API_IdNamespaceIdMappingWorkflowProperties.html): An object containing idMappingType, providerProperties, and ruleBasedProperties.
- [IdNamespaceInputSource](https://docs.aws.amazon.com/entityresolution/latest/apireference/API_IdNamespaceInputSource.html): An object containing inputSourceARN and schemaName.
- [IdNamespaceSummary](https://docs.aws.amazon.com/entityresolution/latest/apireference/API_IdNamespaceSummary.html): A summary of ID namespaces.
- [IncrementalRunConfig](https://docs.aws.amazon.com/entityresolution/latest/apireference/API_IncrementalRunConfig.html): Optional.
- [InputSource](https://docs.aws.amazon.com/entityresolution/latest/apireference/API_InputSource.html): An object containing inputSourceARN, schemaName, and applyNormalization.
- [IntermediateSourceConfiguration](https://docs.aws.amazon.com/entityresolution/latest/apireference/API_IntermediateSourceConfiguration.html): The Amazon S3 location that temporarily stores your data while it processes.
- [JobMetrics](https://docs.aws.amazon.com/entityresolution/latest/apireference/API_JobMetrics.html): An object containing inputRecords, totalRecordsProcessed, matchIDs, and recordsNotProcessed.
- [JobOutputSource](https://docs.aws.amazon.com/entityresolution/latest/apireference/API_JobOutputSource.html): An object containing KMSArn, outputS3Path, and roleArn.
- [JobSummary](https://docs.aws.amazon.com/entityresolution/latest/apireference/API_JobSummary.html): An object containing the jobId, status, startTime, and endTime of a job.
- [MatchedRecord](https://docs.aws.amazon.com/entityresolution/latest/apireference/API_MatchedRecord.html): The matched record.
- [MatchGroup](https://docs.aws.amazon.com/entityresolution/latest/apireference/API_MatchGroup.html): The match group.
- [MatchingWorkflowSummary](https://docs.aws.amazon.com/entityresolution/latest/apireference/API_MatchingWorkflowSummary.html): A list of MatchingWorkflowSummary objects, each of which contain the fields workflowName, workflowArn, resolutionType, createdAt, updatedAt.
- [NamespaceProviderProperties](https://docs.aws.amazon.com/entityresolution/latest/apireference/API_NamespaceProviderProperties.html): An object containing providerConfiguration and providerServiceArn.
- [NamespaceRuleBasedProperties](https://docs.aws.amazon.com/entityresolution/latest/apireference/API_NamespaceRuleBasedProperties.html): The rule-based properties of an ID namespace.
- [OutputAttribute](https://docs.aws.amazon.com/entityresolution/latest/apireference/API_OutputAttribute.html): A list of OutputAttribute objects, each of which have the fields Name and Hashed.
- [OutputSource](https://docs.aws.amazon.com/entityresolution/latest/apireference/API_OutputSource.html): A list of OutputAttribute objects, each of which have the fields Name and Hashed.
- [ProviderComponentSchema](https://docs.aws.amazon.com/entityresolution/latest/apireference/API_ProviderComponentSchema.html): The input schema supported by provider service.
- [ProviderEndpointConfiguration](https://docs.aws.amazon.com/entityresolution/latest/apireference/API_ProviderEndpointConfiguration.html): The required configuration fields to use with the provider service.
- [ProviderIdNameSpaceConfiguration](https://docs.aws.amazon.com/entityresolution/latest/apireference/API_ProviderIdNameSpaceConfiguration.html): The provider configuration required for different ID namespace types.
- [ProviderIntermediateDataAccessConfiguration](https://docs.aws.amazon.com/entityresolution/latest/apireference/API_ProviderIntermediateDataAccessConfiguration.html): The required configuration fields to give intermediate access to a provider service.
- [ProviderMarketplaceConfiguration](https://docs.aws.amazon.com/entityresolution/latest/apireference/API_ProviderMarketplaceConfiguration.html): The identifiers of the provider service, from AWS Data Exchange.
- [ProviderProperties](https://docs.aws.amazon.com/entityresolution/latest/apireference/API_ProviderProperties.html): An object containing the providerServiceARN, intermediateSourceConfiguration, and providerConfiguration.
- [ProviderSchemaAttribute](https://docs.aws.amazon.com/entityresolution/latest/apireference/API_ProviderSchemaAttribute.html): The provider schema attribute.
- [ProviderServiceSummary](https://docs.aws.amazon.com/entityresolution/latest/apireference/API_ProviderServiceSummary.html): A list of ProviderService objects, each of which contain the fields providerName, providerServiceArn, providerServiceName, and providerServiceType.
- [Record](https://docs.aws.amazon.com/entityresolution/latest/apireference/API_Record.html): The record.
- [ResolutionTechniques](https://docs.aws.amazon.com/entityresolution/latest/apireference/API_ResolutionTechniques.html): An object which defines the resolutionType and the ruleBasedProperties.
- [Rule](https://docs.aws.amazon.com/entityresolution/latest/apireference/API_Rule.html): An object containing the ruleName and matchingKeys.
- [RuleBasedProperties](https://docs.aws.amazon.com/entityresolution/latest/apireference/API_RuleBasedProperties.html): An object which defines the list of matching rules to run in a matching workflow.
- [RuleCondition](https://docs.aws.amazon.com/entityresolution/latest/apireference/API_RuleCondition.html): An object that defines the ruleCondition and the ruleName to use in a matching workflow.
- [RuleConditionProperties](https://docs.aws.amazon.com/entityresolution/latest/apireference/API_RuleConditionProperties.html): The properties of a rule condition that provides the ability to use more complex syntax.
- [SchemaInputAttribute](https://docs.aws.amazon.com/entityresolution/latest/apireference/API_SchemaInputAttribute.html): A configuration object for defining input data fields in AWS Entity Resolution.
- [SchemaMappingSummary](https://docs.aws.amazon.com/entityresolution/latest/apireference/API_SchemaMappingSummary.html): An object containing schemaName, schemaArn, createdAt, updatedAt, and hasWorkflows.
