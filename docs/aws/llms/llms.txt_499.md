# Source: https://docs.aws.amazon.com/kendra/latest/APIReference/llms.txt

# Amazon Kendra API Reference 

> Details about operations and parameters in the Amazon Kendra API Reference

## [Amazon Kendra API Reference](https://docs.aws.amazon.com/kendra/latest/APIReference/welcome.html)

### [Actions](https://docs.aws.amazon.com/kendra/latest/APIReference/API_Operations.html)

The following actions are supported by Amazon Kendra:

### [Amazon Kendra](https://docs.aws.amazon.com/kendra/latest/APIReference/API_Operations_Amazon_Kendra.html)

The following actions are supported by Amazon Kendra:

- [AssociateEntitiesToExperience](https://docs.aws.amazon.com/kendra/latest/APIReference/API_AssociateEntitiesToExperience.html): Grants users or groups in your IAM Identity Center identity source access to your Amazon Kendra experience.
- [AssociatePersonasToEntities](https://docs.aws.amazon.com/kendra/latest/APIReference/API_AssociatePersonasToEntities.html): Defines the specific permissions of users or groups in your IAM Identity Center identity source with access to your Amazon Kendra experience.
- [BatchDeleteDocument](https://docs.aws.amazon.com/kendra/latest/APIReference/API_BatchDeleteDocument.html): Removes one or more documents from an index.
- [BatchDeleteFeaturedResultsSet](https://docs.aws.amazon.com/kendra/latest/APIReference/API_BatchDeleteFeaturedResultsSet.html): Removes one or more sets of featured results.
- [BatchGetDocumentStatus](https://docs.aws.amazon.com/kendra/latest/APIReference/API_BatchGetDocumentStatus.html): Returns the indexing status for one or more documents submitted with the BatchPutDocument API.
- [BatchPutDocument](https://docs.aws.amazon.com/kendra/latest/APIReference/API_BatchPutDocument.html): Adds one or more documents to an index.
- [ClearQuerySuggestions](https://docs.aws.amazon.com/kendra/latest/APIReference/API_ClearQuerySuggestions.html): Clears existing query suggestions from an index.
- [CreateAccessControlConfiguration](https://docs.aws.amazon.com/kendra/latest/APIReference/API_CreateAccessControlConfiguration.html): Creates an access configuration for your documents.
- [CreateDataSource](https://docs.aws.amazon.com/kendra/latest/APIReference/API_CreateDataSource.html): Creates a data source connector that you want to use with an Amazon Kendra index.
- [CreateExperience](https://docs.aws.amazon.com/kendra/latest/APIReference/API_CreateExperience.html): Creates an Amazon Kendra experience such as a search application.
- [CreateFaq](https://docs.aws.amazon.com/kendra/latest/APIReference/API_CreateFaq.html): Creates a set of frequently ask questions (FAQs) using a specified FAQ file stored in an Amazon S3 bucket.
- [CreateFeaturedResultsSet](https://docs.aws.amazon.com/kendra/latest/APIReference/API_CreateFeaturedResultsSet.html): Creates a set of featured results to display at the top of the search results page.
- [CreateIndex](https://docs.aws.amazon.com/kendra/latest/APIReference/API_CreateIndex.html): Creates an Amazon Kendra index.
- [CreateQuerySuggestionsBlockList](https://docs.aws.amazon.com/kendra/latest/APIReference/API_CreateQuerySuggestionsBlockList.html): Creates a block list to exlcude certain queries from suggestions.
- [CreateThesaurus](https://docs.aws.amazon.com/kendra/latest/APIReference/API_CreateThesaurus.html): Creates a thesaurus for an index.
- [DeleteAccessControlConfiguration](https://docs.aws.amazon.com/kendra/latest/APIReference/API_DeleteAccessControlConfiguration.html): Deletes an access control configuration that you created for your documents in an index.
- [DeleteDataSource](https://docs.aws.amazon.com/kendra/latest/APIReference/API_DeleteDataSource.html): Deletes an Amazon Kendra data source connector.
- [DeleteExperience](https://docs.aws.amazon.com/kendra/latest/APIReference/API_DeleteExperience.html): Deletes your Amazon Kendra experience such as a search application.
- [DeleteFaq](https://docs.aws.amazon.com/kendra/latest/APIReference/API_DeleteFaq.html): Removes a FAQ from an index.
- [DeleteIndex](https://docs.aws.amazon.com/kendra/latest/APIReference/API_DeleteIndex.html): Deletes an Amazon Kendra index.
- [DeletePrincipalMapping](https://docs.aws.amazon.com/kendra/latest/APIReference/API_DeletePrincipalMapping.html): Deletes a group so that all users that belong to the group can no longer access documents only available to that group.
- [DeleteQuerySuggestionsBlockList](https://docs.aws.amazon.com/kendra/latest/APIReference/API_DeleteQuerySuggestionsBlockList.html): Deletes a block list used for query suggestions for an index.
- [DeleteThesaurus](https://docs.aws.amazon.com/kendra/latest/APIReference/API_DeleteThesaurus.html): Deletes an Amazon Kendra thesaurus.
- [DescribeAccessControlConfiguration](https://docs.aws.amazon.com/kendra/latest/APIReference/API_DescribeAccessControlConfiguration.html): Gets information about an access control configuration that you created for your documents in an index.
- [DescribeDataSource](https://docs.aws.amazon.com/kendra/latest/APIReference/API_DescribeDataSource.html): Gets information about an Amazon Kendra data source connector.
- [DescribeExperience](https://docs.aws.amazon.com/kendra/latest/APIReference/API_DescribeExperience.html): Gets information about your Amazon Kendra experience such as a search application.
- [DescribeFaq](https://docs.aws.amazon.com/kendra/latest/APIReference/API_DescribeFaq.html): Gets information about a FAQ.
- [DescribeFeaturedResultsSet](https://docs.aws.amazon.com/kendra/latest/APIReference/API_DescribeFeaturedResultsSet.html): Gets information about a set of featured results.
- [DescribeIndex](https://docs.aws.amazon.com/kendra/latest/APIReference/API_DescribeIndex.html): Gets information about an Amazon Kendra index.
- [DescribePrincipalMapping](https://docs.aws.amazon.com/kendra/latest/APIReference/API_DescribePrincipalMapping.html): Describes the processing of PUT and DELETE actions for mapping users to their groups.
- [DescribeQuerySuggestionsBlockList](https://docs.aws.amazon.com/kendra/latest/APIReference/API_DescribeQuerySuggestionsBlockList.html): Gets information about a block list used for query suggestions for an index.
- [DescribeQuerySuggestionsConfig](https://docs.aws.amazon.com/kendra/latest/APIReference/API_DescribeQuerySuggestionsConfig.html): Gets information on the settings of query suggestions for an index.
- [DescribeThesaurus](https://docs.aws.amazon.com/kendra/latest/APIReference/API_DescribeThesaurus.html): Gets information about an Amazon Kendra thesaurus.
- [DisassociateEntitiesFromExperience](https://docs.aws.amazon.com/kendra/latest/APIReference/API_DisassociateEntitiesFromExperience.html): Prevents users or groups in your IAM Identity Center identity source from accessing your Amazon Kendra experience.
- [DisassociatePersonasFromEntities](https://docs.aws.amazon.com/kendra/latest/APIReference/API_DisassociatePersonasFromEntities.html): Removes the specific permissions of users or groups in your IAM Identity Center identity source with access to your Amazon Kendra experience.
- [GetQuerySuggestions](https://docs.aws.amazon.com/kendra/latest/APIReference/API_GetQuerySuggestions.html): Fetches the queries that are suggested to your users.
- [GetSnapshots](https://docs.aws.amazon.com/kendra/latest/APIReference/API_GetSnapshots.html): Retrieves search metrics data.
- [ListAccessControlConfigurations](https://docs.aws.amazon.com/kendra/latest/APIReference/API_ListAccessControlConfigurations.html): Lists one or more access control configurations for an index.
- [ListDataSources](https://docs.aws.amazon.com/kendra/latest/APIReference/API_ListDataSources.html): Lists the data source connectors that you have created.
- [ListDataSourceSyncJobs](https://docs.aws.amazon.com/kendra/latest/APIReference/API_ListDataSourceSyncJobs.html): Gets statistics about synchronizing a data source connector.
- [ListEntityPersonas](https://docs.aws.amazon.com/kendra/latest/APIReference/API_ListEntityPersonas.html): Lists specific permissions of users and groups with access to your Amazon Kendra experience.
- [ListExperienceEntities](https://docs.aws.amazon.com/kendra/latest/APIReference/API_ListExperienceEntities.html): Lists users or groups in your IAM Identity Center identity source that are granted access to your Amazon Kendra experience.
- [ListExperiences](https://docs.aws.amazon.com/kendra/latest/APIReference/API_ListExperiences.html): Lists one or more Amazon Kendra experiences.
- [ListFaqs](https://docs.aws.amazon.com/kendra/latest/APIReference/API_ListFaqs.html): Gets a list of FAQs associated with an index.
- [ListFeaturedResultsSets](https://docs.aws.amazon.com/kendra/latest/APIReference/API_ListFeaturedResultsSets.html): Lists all your sets of featured results for a given index.
- [ListGroupsOlderThanOrderingId](https://docs.aws.amazon.com/kendra/latest/APIReference/API_ListGroupsOlderThanOrderingId.html): Provides a list of groups that are mapped to users before a given ordering or timestamp identifier.
- [ListIndices](https://docs.aws.amazon.com/kendra/latest/APIReference/API_ListIndices.html): Lists the Amazon Kendra indexes that you created.
- [ListQuerySuggestionsBlockLists](https://docs.aws.amazon.com/kendra/latest/APIReference/API_ListQuerySuggestionsBlockLists.html): Lists the block lists used for query suggestions for an index.
- [ListTagsForResource](https://docs.aws.amazon.com/kendra/latest/APIReference/API_ListTagsForResource.html): Gets a list of tags associated with a resource.
- [ListThesauri](https://docs.aws.amazon.com/kendra/latest/APIReference/API_ListThesauri.html): Lists the thesauri for an index.
- [PutPrincipalMapping](https://docs.aws.amazon.com/kendra/latest/APIReference/API_PutPrincipalMapping.html): Maps users to their groups so that you only need to provide the user ID when you issue the query.
- [Query](https://docs.aws.amazon.com/kendra/latest/APIReference/API_Query.html): Searches an index given an input query.
- [Retrieve](https://docs.aws.amazon.com/kendra/latest/APIReference/API_Retrieve.html): Retrieves relevant passages or text excerpts given an input query.
- [StartDataSourceSyncJob](https://docs.aws.amazon.com/kendra/latest/APIReference/API_StartDataSourceSyncJob.html): Starts a synchronization job for a data source connector.
- [StopDataSourceSyncJob](https://docs.aws.amazon.com/kendra/latest/APIReference/API_StopDataSourceSyncJob.html): Stops a synchronization job that is currently running.
- [SubmitFeedback](https://docs.aws.amazon.com/kendra/latest/APIReference/API_SubmitFeedback.html): Enables you to provide feedback to Amazon Kendra to improve the performance of your index.
- [TagResource](https://docs.aws.amazon.com/kendra/latest/APIReference/API_TagResource.html): Adds the specified tag to the specified index, FAQ, data source, or other resource.
- [UntagResource](https://docs.aws.amazon.com/kendra/latest/APIReference/API_UntagResource.html): Removes a tag from an index, FAQ, data source, or other resource.
- [UpdateAccessControlConfiguration](https://docs.aws.amazon.com/kendra/latest/APIReference/API_UpdateAccessControlConfiguration.html): Updates an access control configuration for your documents in an index.
- [UpdateDataSource](https://docs.aws.amazon.com/kendra/latest/APIReference/API_UpdateDataSource.html): Updates an Amazon Kendra data source connector.
- [UpdateExperience](https://docs.aws.amazon.com/kendra/latest/APIReference/API_UpdateExperience.html): Updates your Amazon Kendra experience such as a search application.
- [UpdateFeaturedResultsSet](https://docs.aws.amazon.com/kendra/latest/APIReference/API_UpdateFeaturedResultsSet.html): Updates a set of featured results.
- [UpdateIndex](https://docs.aws.amazon.com/kendra/latest/APIReference/API_UpdateIndex.html): Updates an Amazon Kendra index.
- [UpdateQuerySuggestionsBlockList](https://docs.aws.amazon.com/kendra/latest/APIReference/API_UpdateQuerySuggestionsBlockList.html): Updates a block list used for query suggestions for an index.
- [UpdateQuerySuggestionsConfig](https://docs.aws.amazon.com/kendra/latest/APIReference/API_UpdateQuerySuggestionsConfig.html): Updates the settings of query suggestions for an index.
- [UpdateThesaurus](https://docs.aws.amazon.com/kendra/latest/APIReference/API_UpdateThesaurus.html): Updates a thesaurus for an index.

### [Amazon Kendra Intelligent Ranking](https://docs.aws.amazon.com/kendra/latest/APIReference/API_Operations_Amazon_Kendra_Intelligent_Ranking.html)

The following actions are supported by Amazon Kendra Intelligent Ranking:

- [CreateRescoreExecutionPlan](https://docs.aws.amazon.com/kendra/latest/APIReference/API_Ranking_CreateRescoreExecutionPlan.html): Creates a rescore execution plan.
- [DeleteRescoreExecutionPlan](https://docs.aws.amazon.com/kendra/latest/APIReference/API_Ranking_DeleteRescoreExecutionPlan.html): Deletes a rescore execution plan.
- [DescribeRescoreExecutionPlan](https://docs.aws.amazon.com/kendra/latest/APIReference/API_Ranking_DescribeRescoreExecutionPlan.html): Gets information about a rescore execution plan.
- [ListRescoreExecutionPlans](https://docs.aws.amazon.com/kendra/latest/APIReference/API_Ranking_ListRescoreExecutionPlans.html): Lists your rescore execution plans.
- [ListTagsForResource](https://docs.aws.amazon.com/kendra/latest/APIReference/API_Ranking_ListTagsForResource.html): Gets a list of tags associated with a specified resource.
- [Rescore](https://docs.aws.amazon.com/kendra/latest/APIReference/API_Ranking_Rescore.html): Rescores or re-ranks search results from a search service such as OpenSearch (self managed).
- [TagResource](https://docs.aws.amazon.com/kendra/latest/APIReference/API_Ranking_TagResource.html): Adds a specified tag to a specified rescore execution plan.
- [UntagResource](https://docs.aws.amazon.com/kendra/latest/APIReference/API_Ranking_UntagResource.html): Removes a tag from a rescore execution plan.
- [UpdateRescoreExecutionPlan](https://docs.aws.amazon.com/kendra/latest/APIReference/API_Ranking_UpdateRescoreExecutionPlan.html): Updates a rescore execution plan.

### [Data Types](https://docs.aws.amazon.com/kendra/latest/APIReference/API_Types.html)

The following data types are supported by Amazon Kendra:

### [Amazon Kendra](https://docs.aws.amazon.com/kendra/latest/APIReference/API_Types_Amazon_Kendra.html)

The following data types are supported by Amazon Kendra:

- [AccessControlConfigurationSummary](https://docs.aws.amazon.com/kendra/latest/APIReference/API_AccessControlConfigurationSummary.html): Summary information on an access control configuration that you created for your documents in an index.
- [AccessControlListConfiguration](https://docs.aws.amazon.com/kendra/latest/APIReference/API_AccessControlListConfiguration.html): Access Control List files for the documents in a data source.
- [AclConfiguration](https://docs.aws.amazon.com/kendra/latest/APIReference/API_AclConfiguration.html): Provides information about the column that should be used for filtering the query response by groups.
- [AdditionalResultAttribute](https://docs.aws.amazon.com/kendra/latest/APIReference/API_AdditionalResultAttribute.html): An attribute returned from an index query.
- [AdditionalResultAttributeValue](https://docs.aws.amazon.com/kendra/latest/APIReference/API_AdditionalResultAttributeValue.html): An attribute returned with a document from a search.
- [AlfrescoConfiguration](https://docs.aws.amazon.com/kendra/latest/APIReference/API_AlfrescoConfiguration.html): Provides the configuration information to connect to Alfresco as your data source.
- [AttributeFilter](https://docs.aws.amazon.com/kendra/latest/APIReference/API_AttributeFilter.html): Filters the search results based on document attributes or fields.
- [AttributeSuggestionsDescribeConfig](https://docs.aws.amazon.com/kendra/latest/APIReference/API_AttributeSuggestionsDescribeConfig.html): Gets information on the configuration of document fields/attributes that you want to base query suggestions on.
- [AttributeSuggestionsGetConfig](https://docs.aws.amazon.com/kendra/latest/APIReference/API_AttributeSuggestionsGetConfig.html): Provides the configuration information for the document fields/attributes that you want to base query suggestions on.
- [AttributeSuggestionsUpdateConfig](https://docs.aws.amazon.com/kendra/latest/APIReference/API_AttributeSuggestionsUpdateConfig.html): Updates the configuration information for the document fields/attributes that you want to base query suggestions on.
- [AuthenticationConfiguration](https://docs.aws.amazon.com/kendra/latest/APIReference/API_AuthenticationConfiguration.html): Provides the configuration information to connect to websites that require user authentication.
- [BasicAuthenticationConfiguration](https://docs.aws.amazon.com/kendra/latest/APIReference/API_BasicAuthenticationConfiguration.html): Provides the configuration information to connect to websites that require basic user authentication.
- [BatchDeleteDocumentResponseFailedDocument](https://docs.aws.amazon.com/kendra/latest/APIReference/API_BatchDeleteDocumentResponseFailedDocument.html): Provides information about documents that could not be removed from an index by the BatchDeleteDocument API.
- [BatchDeleteFeaturedResultsSetError](https://docs.aws.amazon.com/kendra/latest/APIReference/API_BatchDeleteFeaturedResultsSetError.html): Provides information about a set of featured results that couldn't be removed from an index by the BatchDeleteFeaturedResultsSet API.
- [BatchGetDocumentStatusResponseError](https://docs.aws.amazon.com/kendra/latest/APIReference/API_BatchGetDocumentStatusResponseError.html): Provides a response when the status of a document could not be retrieved.
- [BatchPutDocumentResponseFailedDocument](https://docs.aws.amazon.com/kendra/latest/APIReference/API_BatchPutDocumentResponseFailedDocument.html): Provides information about a document that could not be indexed.
- [BoxConfiguration](https://docs.aws.amazon.com/kendra/latest/APIReference/API_BoxConfiguration.html): Provides the configuration information to connect to Box as your data source.
- [CapacityUnitsConfiguration](https://docs.aws.amazon.com/kendra/latest/APIReference/API_CapacityUnitsConfiguration.html): Specifies additional capacity units configured for your Enterprise Edition index.
- [ClickFeedback](https://docs.aws.amazon.com/kendra/latest/APIReference/API_ClickFeedback.html): Gathers information about when a particular result was clicked by a user.
- [CollapseConfiguration](https://docs.aws.amazon.com/kendra/latest/APIReference/API_CollapseConfiguration.html): Specifies how to group results by document attribute value, and how to display them collapsed/expanded under a designated primary document for each group.
- [CollapsedResultDetail](https://docs.aws.amazon.com/kendra/latest/APIReference/API_CollapsedResultDetail.html): Provides details about a collapsed group of search results.
- [ColumnConfiguration](https://docs.aws.amazon.com/kendra/latest/APIReference/API_ColumnConfiguration.html): Provides information about how Amazon Kendra should use the columns of a database in an index.
- [ConflictingItem](https://docs.aws.amazon.com/kendra/latest/APIReference/API_ConflictingItem.html): Information about a conflicting query used across different sets of featured results.
- [ConfluenceAttachmentConfiguration](https://docs.aws.amazon.com/kendra/latest/APIReference/API_ConfluenceAttachmentConfiguration.html): Configuration of attachment settings for the Confluence data source.
- [ConfluenceAttachmentToIndexFieldMapping](https://docs.aws.amazon.com/kendra/latest/APIReference/API_ConfluenceAttachmentToIndexFieldMapping.html): Maps attributes or field names of Confluence attachments to Amazon Kendra index field names.
- [ConfluenceBlogConfiguration](https://docs.aws.amazon.com/kendra/latest/APIReference/API_ConfluenceBlogConfiguration.html): Configuration of blog settings for the Confluence data source.
- [ConfluenceBlogToIndexFieldMapping](https://docs.aws.amazon.com/kendra/latest/APIReference/API_ConfluenceBlogToIndexFieldMapping.html): Maps attributes or field names of Confluence blog to Amazon Kendra index field names.
- [ConfluenceConfiguration](https://docs.aws.amazon.com/kendra/latest/APIReference/API_ConfluenceConfiguration.html): Provides the configuration information to connect to Confluence as your data source.
- [ConfluencePageConfiguration](https://docs.aws.amazon.com/kendra/latest/APIReference/API_ConfluencePageConfiguration.html): Configuration of the page settings for the Confluence data source.
- [ConfluencePageToIndexFieldMapping](https://docs.aws.amazon.com/kendra/latest/APIReference/API_ConfluencePageToIndexFieldMapping.html): Maps attributes or field names of Confluence pages to Amazon Kendra index field names.
- [ConfluenceSpaceConfiguration](https://docs.aws.amazon.com/kendra/latest/APIReference/API_ConfluenceSpaceConfiguration.html): Configuration information for indexing Confluence spaces.
- [ConfluenceSpaceToIndexFieldMapping](https://docs.aws.amazon.com/kendra/latest/APIReference/API_ConfluenceSpaceToIndexFieldMapping.html): Maps attributes or field names of Confluence spaces to Amazon Kendra index field names.
- [ConnectionConfiguration](https://docs.aws.amazon.com/kendra/latest/APIReference/API_ConnectionConfiguration.html): Provides the configuration information that's required to connect to a database.
- [ContentSourceConfiguration](https://docs.aws.amazon.com/kendra/latest/APIReference/API_ContentSourceConfiguration.html): Provides the configuration information for your content sources, such as data sources, FAQs, and content indexed directly via BatchPutDocument.
- [Correction](https://docs.aws.amazon.com/kendra/latest/APIReference/API_Correction.html): A corrected misspelled word in a query.
- [CustomDocumentEnrichmentConfiguration](https://docs.aws.amazon.com/kendra/latest/APIReference/API_CustomDocumentEnrichmentConfiguration.html): Provides the configuration information for altering document metadata and content during the document ingestion process.
- [DatabaseConfiguration](https://docs.aws.amazon.com/kendra/latest/APIReference/API_DatabaseConfiguration.html): Provides the configuration information to an Amazon Kendra supported database.
- [DataSourceConfiguration](https://docs.aws.amazon.com/kendra/latest/APIReference/API_DataSourceConfiguration.html): Provides the configuration information for an Amazon Kendra data source.
- [DataSourceGroup](https://docs.aws.amazon.com/kendra/latest/APIReference/API_DataSourceGroup.html): Data source information for user context filtering.
- [DataSourceSummary](https://docs.aws.amazon.com/kendra/latest/APIReference/API_DataSourceSummary.html): Summary information for a Amazon Kendra data source.
- [DataSourceSyncJob](https://docs.aws.amazon.com/kendra/latest/APIReference/API_DataSourceSyncJob.html): Provides information about a data source synchronization job.
- [DataSourceSyncJobMetrics](https://docs.aws.amazon.com/kendra/latest/APIReference/API_DataSourceSyncJobMetrics.html): Maps a batch delete document request to a specific data source sync job.
- [DataSourceSyncJobMetricTarget](https://docs.aws.amazon.com/kendra/latest/APIReference/API_DataSourceSyncJobMetricTarget.html): Maps a particular data source sync job to a particular data source.
- [DataSourceToIndexFieldMapping](https://docs.aws.amazon.com/kendra/latest/APIReference/API_DataSourceToIndexFieldMapping.html): Maps attributes or field names of the documents synced from the data source to Amazon Kendra index field names.
- [DataSourceVpcConfiguration](https://docs.aws.amazon.com/kendra/latest/APIReference/API_DataSourceVpcConfiguration.html): Provides the configuration information to connect to an Amazon VPC.
- [Document](https://docs.aws.amazon.com/kendra/latest/APIReference/API_Document.html): A document in an index.
- [DocumentAttribute](https://docs.aws.amazon.com/kendra/latest/APIReference/API_DocumentAttribute.html): A document attribute or metadata field.
- [DocumentAttributeCondition](https://docs.aws.amazon.com/kendra/latest/APIReference/API_DocumentAttributeCondition.html): The condition used for the target document attribute or metadata field when ingesting documents into Amazon Kendra.
- [DocumentAttributeTarget](https://docs.aws.amazon.com/kendra/latest/APIReference/API_DocumentAttributeTarget.html): The target document attribute or metadata field you want to alter when ingesting documents into Amazon Kendra.
- [DocumentAttributeValue](https://docs.aws.amazon.com/kendra/latest/APIReference/API_DocumentAttributeValue.html): The value of a document attribute.
- [DocumentAttributeValueCountPair](https://docs.aws.amazon.com/kendra/latest/APIReference/API_DocumentAttributeValueCountPair.html): Provides the count of documents that match a particular document attribute or field when doing a faceted search.
- [DocumentInfo](https://docs.aws.amazon.com/kendra/latest/APIReference/API_DocumentInfo.html): Identifies a document for which to retrieve status information
- [DocumentMetadataConfiguration](https://docs.aws.amazon.com/kendra/latest/APIReference/API_DocumentMetadataConfiguration.html): Specifies the properties, such as relevance tuning and searchability, of an index field.
- [DocumentRelevanceConfiguration](https://docs.aws.amazon.com/kendra/latest/APIReference/API_DocumentRelevanceConfiguration.html): Overrides the document relevance properties of a custom index field.
- [DocumentsMetadataConfiguration](https://docs.aws.amazon.com/kendra/latest/APIReference/API_DocumentsMetadataConfiguration.html): Document metadata files that contain information such as the document access control information, source URI, document author, and custom attributes.
- [EntityConfiguration](https://docs.aws.amazon.com/kendra/latest/APIReference/API_EntityConfiguration.html): Provides the configuration information for users or groups in your IAM Identity Center identity source to grant access your Amazon Kendra experience.
- [EntityDisplayData](https://docs.aws.amazon.com/kendra/latest/APIReference/API_EntityDisplayData.html): Information about the user entity.
- [EntityPersonaConfiguration](https://docs.aws.amazon.com/kendra/latest/APIReference/API_EntityPersonaConfiguration.html): Provides the configuration information for users or groups in your IAM Identity Center identity source for access to your Amazon Kendra experience.
- [ExpandConfiguration](https://docs.aws.amazon.com/kendra/latest/APIReference/API_ExpandConfiguration.html): Specifies the configuration information needed to customize how collapsed search result groups expand.
- [ExpandedResultItem](https://docs.aws.amazon.com/kendra/latest/APIReference/API_ExpandedResultItem.html): A single expanded result in a collapsed group of search results.
- [ExperienceConfiguration](https://docs.aws.amazon.com/kendra/latest/APIReference/API_ExperienceConfiguration.html): Provides the configuration information for your Amazon Kendra experience.
- [ExperienceEndpoint](https://docs.aws.amazon.com/kendra/latest/APIReference/API_ExperienceEndpoint.html): Provides the configuration information for the endpoint for your Amazon Kendra experience.
- [ExperienceEntitiesSummary](https://docs.aws.amazon.com/kendra/latest/APIReference/API_ExperienceEntitiesSummary.html): Summary information for users or groups in your IAM Identity Center identity source with granted access to your Amazon Kendra experience.
- [ExperiencesSummary](https://docs.aws.amazon.com/kendra/latest/APIReference/API_ExperiencesSummary.html): Summary information for your Amazon Kendra experience.
- [Facet](https://docs.aws.amazon.com/kendra/latest/APIReference/API_Facet.html): Information about a document attribute or field.
- [FacetResult](https://docs.aws.amazon.com/kendra/latest/APIReference/API_FacetResult.html): The facet values for the documents in the response.
- [FailedEntity](https://docs.aws.amazon.com/kendra/latest/APIReference/API_FailedEntity.html): Information on the users or groups in your IAM Identity Center identity source that failed to properly configure with your Amazon Kendra experience.
- [FaqStatistics](https://docs.aws.amazon.com/kendra/latest/APIReference/API_FaqStatistics.html): Provides statistical information about the FAQ questions and answers for an index.
- [FaqSummary](https://docs.aws.amazon.com/kendra/latest/APIReference/API_FaqSummary.html): Summary information for frequently asked questions and answers included in an index.
- [FeaturedDocument](https://docs.aws.amazon.com/kendra/latest/APIReference/API_FeaturedDocument.html): A featured document.
- [FeaturedDocumentMissing](https://docs.aws.amazon.com/kendra/latest/APIReference/API_FeaturedDocumentMissing.html): A document ID doesn't exist but you have specified as a featured document.
- [FeaturedDocumentWithMetadata](https://docs.aws.amazon.com/kendra/latest/APIReference/API_FeaturedDocumentWithMetadata.html): A featured document with its metadata information.
- [FeaturedResultsItem](https://docs.aws.amazon.com/kendra/latest/APIReference/API_FeaturedResultsItem.html): A single featured result item.
- [FeaturedResultsSet](https://docs.aws.amazon.com/kendra/latest/APIReference/API_FeaturedResultsSet.html): A set of featured results that are displayed at the top of your search results.
- [FeaturedResultsSetSummary](https://docs.aws.amazon.com/kendra/latest/APIReference/API_FeaturedResultsSetSummary.html): Summary information for a set of featured results.
- [FsxConfiguration](https://docs.aws.amazon.com/kendra/latest/APIReference/API_FsxConfiguration.html): Provides the configuration information to connect to Amazon FSx as your data source.
- [GitHubConfiguration](https://docs.aws.amazon.com/kendra/latest/APIReference/API_GitHubConfiguration.html): Provides the configuration information to connect to GitHub as your data source.
- [GitHubDocumentCrawlProperties](https://docs.aws.amazon.com/kendra/latest/APIReference/API_GitHubDocumentCrawlProperties.html): Provides the configuration information to include certain types of GitHub content.
- [GoogleDriveConfiguration](https://docs.aws.amazon.com/kendra/latest/APIReference/API_GoogleDriveConfiguration.html): Provides the configuration information to connect to Google Drive as your data source.
- [GroupMembers](https://docs.aws.amazon.com/kendra/latest/APIReference/API_GroupMembers.html): A list of users that belong to a group.
- [GroupOrderingIdSummary](https://docs.aws.amazon.com/kendra/latest/APIReference/API_GroupOrderingIdSummary.html): Summary information on the processing of PUT and DELETE actions for mapping users to their groups.
- [GroupSummary](https://docs.aws.amazon.com/kendra/latest/APIReference/API_GroupSummary.html): Summary information for groups.
- [HierarchicalPrincipal](https://docs.aws.amazon.com/kendra/latest/APIReference/API_HierarchicalPrincipal.html): Information to define the hierarchy for which documents users should have access to.
- [Highlight](https://docs.aws.amazon.com/kendra/latest/APIReference/API_Highlight.html): Provides information that you can use to highlight a search result so that your users can quickly identify terms in the response.
- [HookConfiguration](https://docs.aws.amazon.com/kendra/latest/APIReference/API_HookConfiguration.html): Provides the configuration information for invoking a Lambda function in AWS Lambda to alter document metadata and content when ingesting documents into Amazon Kendra.
- [IndexConfigurationSummary](https://docs.aws.amazon.com/kendra/latest/APIReference/API_IndexConfigurationSummary.html): Summary information on the configuration of an index.
- [IndexStatistics](https://docs.aws.amazon.com/kendra/latest/APIReference/API_IndexStatistics.html): Provides information about the number of documents and the number of questions and answers in an index.
- [InlineCustomDocumentEnrichmentConfiguration](https://docs.aws.amazon.com/kendra/latest/APIReference/API_InlineCustomDocumentEnrichmentConfiguration.html): Provides the configuration information for applying basic logic to alter document metadata and content when ingesting documents into Amazon Kendra.
- [JiraConfiguration](https://docs.aws.amazon.com/kendra/latest/APIReference/API_JiraConfiguration.html): Provides the configuration information to connect to Jira as your data source.
- [JsonTokenTypeConfiguration](https://docs.aws.amazon.com/kendra/latest/APIReference/API_JsonTokenTypeConfiguration.html): Provides the configuration information for the JSON token type.
- [JwtTokenTypeConfiguration](https://docs.aws.amazon.com/kendra/latest/APIReference/API_JwtTokenTypeConfiguration.html): Provides the configuration information for the JWT token type.
- [MemberGroup](https://docs.aws.amazon.com/kendra/latest/APIReference/API_MemberGroup.html): The sub groups that belong to a group.
- [MemberUser](https://docs.aws.amazon.com/kendra/latest/APIReference/API_MemberUser.html): The users that belong to a group.
- [OneDriveConfiguration](https://docs.aws.amazon.com/kendra/latest/APIReference/API_OneDriveConfiguration.html): Provides the configuration information to connect to OneDrive as your data source.
- [OneDriveUsers](https://docs.aws.amazon.com/kendra/latest/APIReference/API_OneDriveUsers.html): User accounts whose documents should be indexed.
- [OnPremiseConfiguration](https://docs.aws.amazon.com/kendra/latest/APIReference/API_OnPremiseConfiguration.html): Provides the configuration information to connect to GitHub Enterprise Server (on premises).
- [PersonasSummary](https://docs.aws.amazon.com/kendra/latest/APIReference/API_PersonasSummary.html): Summary information for users or groups in your IAM Identity Center identity source.
- [Principal](https://docs.aws.amazon.com/kendra/latest/APIReference/API_Principal.html): Provides user and group information for user context filtering.
- [ProxyConfiguration](https://docs.aws.amazon.com/kendra/latest/APIReference/API_ProxyConfiguration.html): Provides the configuration information for a web proxy to connect to website hosts.
- [QueryResultItem](https://docs.aws.amazon.com/kendra/latest/APIReference/API_QueryResultItem.html): A single query result.
- [QuerySuggestionsBlockListSummary](https://docs.aws.amazon.com/kendra/latest/APIReference/API_QuerySuggestionsBlockListSummary.html): Summary information on a query suggestions block list.
- [QuipConfiguration](https://docs.aws.amazon.com/kendra/latest/APIReference/API_QuipConfiguration.html): Provides the configuration information to connect to Quip as your data source.
- [Relevance](https://docs.aws.amazon.com/kendra/latest/APIReference/API_Relevance.html): Provides information for tuning the relevance of a field in a search.
- [RelevanceFeedback](https://docs.aws.amazon.com/kendra/latest/APIReference/API_RelevanceFeedback.html): Provides feedback on how relevant a document is to a search.
- [RetrieveResultItem](https://docs.aws.amazon.com/kendra/latest/APIReference/API_RetrieveResultItem.html): A single retrieved relevant passage result.
- [S3DataSourceConfiguration](https://docs.aws.amazon.com/kendra/latest/APIReference/API_S3DataSourceConfiguration.html): Provides the configuration information to connect to an Amazon S3 bucket.
- [S3Path](https://docs.aws.amazon.com/kendra/latest/APIReference/API_S3Path.html): Information required to find a specific file in an Amazon S3 bucket.
- [SaaSConfiguration](https://docs.aws.amazon.com/kendra/latest/APIReference/API_SaaSConfiguration.html): Provides the configuration information to connect to GitHub Enterprise Cloud (SaaS).
- [SalesforceChatterFeedConfiguration](https://docs.aws.amazon.com/kendra/latest/APIReference/API_SalesforceChatterFeedConfiguration.html): The configuration information for syncing a Salesforce chatter feed.
- [SalesforceConfiguration](https://docs.aws.amazon.com/kendra/latest/APIReference/API_SalesforceConfiguration.html): Provides the configuration information to connect to Salesforce as your data source.
- [SalesforceCustomKnowledgeArticleTypeConfiguration](https://docs.aws.amazon.com/kendra/latest/APIReference/API_SalesforceCustomKnowledgeArticleTypeConfiguration.html): Provides the configuration information for indexing Salesforce custom articles.
- [SalesforceKnowledgeArticleConfiguration](https://docs.aws.amazon.com/kendra/latest/APIReference/API_SalesforceKnowledgeArticleConfiguration.html): Provides the configuration information for the knowledge article types that Amazon Kendra indexes.
- [SalesforceStandardKnowledgeArticleTypeConfiguration](https://docs.aws.amazon.com/kendra/latest/APIReference/API_SalesforceStandardKnowledgeArticleTypeConfiguration.html): Provides the configuration information for standard Salesforce knowledge articles.
- [SalesforceStandardObjectAttachmentConfiguration](https://docs.aws.amazon.com/kendra/latest/APIReference/API_SalesforceStandardObjectAttachmentConfiguration.html): Provides the configuration information for processing attachments to Salesforce standard objects.
- [SalesforceStandardObjectConfiguration](https://docs.aws.amazon.com/kendra/latest/APIReference/API_SalesforceStandardObjectConfiguration.html): Provides the configuration information for indexing a single standard object.
- [ScoreAttributes](https://docs.aws.amazon.com/kendra/latest/APIReference/API_ScoreAttributes.html): Provides a relative ranking that indicates how confident Amazon Kendra is that the response is relevant to the query.
- [Search](https://docs.aws.amazon.com/kendra/latest/APIReference/API_Search.html): Provides information about how a custom index field is used during a search.
- [SeedUrlConfiguration](https://docs.aws.amazon.com/kendra/latest/APIReference/API_SeedUrlConfiguration.html): Provides the configuration information for the seed or starting point URLs to crawl.
- [ServerSideEncryptionConfiguration](https://docs.aws.amazon.com/kendra/latest/APIReference/API_ServerSideEncryptionConfiguration.html): Provides the identifier of the AWS KMS key used to encrypt data indexed by Amazon Kendra.
- [ServiceNowConfiguration](https://docs.aws.amazon.com/kendra/latest/APIReference/API_ServiceNowConfiguration.html): Provides the configuration information to connect to ServiceNow as your data source.
- [ServiceNowKnowledgeArticleConfiguration](https://docs.aws.amazon.com/kendra/latest/APIReference/API_ServiceNowKnowledgeArticleConfiguration.html): Provides the configuration information for crawling knowledge articles in the ServiceNow site.
- [ServiceNowServiceCatalogConfiguration](https://docs.aws.amazon.com/kendra/latest/APIReference/API_ServiceNowServiceCatalogConfiguration.html): Provides the configuration information for crawling service catalog items in the ServiceNow site
- [SharePointConfiguration](https://docs.aws.amazon.com/kendra/latest/APIReference/API_SharePointConfiguration.html): Provides the configuration information to connect to Microsoft SharePoint as your data source.
- [SiteMapsConfiguration](https://docs.aws.amazon.com/kendra/latest/APIReference/API_SiteMapsConfiguration.html): Provides the configuration information for the sitemap URLs to crawl.
- [SlackConfiguration](https://docs.aws.amazon.com/kendra/latest/APIReference/API_SlackConfiguration.html): Provides the configuration information to connect to Slack as your data source.
- [SortingConfiguration](https://docs.aws.amazon.com/kendra/latest/APIReference/API_SortingConfiguration.html): Specifies the document attribute to use to sort the response to a Amazon Kendra query.
- [SourceDocument](https://docs.aws.amazon.com/kendra/latest/APIReference/API_SourceDocument.html): The document ID and its fields/attributes that are used for a query suggestion, if document fields set to use for query suggestions.
- [SpellCorrectedQuery](https://docs.aws.amazon.com/kendra/latest/APIReference/API_SpellCorrectedQuery.html): A query with suggested spell corrections.
- [SpellCorrectionConfiguration](https://docs.aws.amazon.com/kendra/latest/APIReference/API_SpellCorrectionConfiguration.html): Provides the configuration information for suggested query spell corrections.
- [SqlConfiguration](https://docs.aws.amazon.com/kendra/latest/APIReference/API_SqlConfiguration.html): Provides the configuration information to use a SQL database.
- [Status](https://docs.aws.amazon.com/kendra/latest/APIReference/API_Status.html): Provides information about the status of documents submitted for indexing.
- [SuggestableConfig](https://docs.aws.amazon.com/kendra/latest/APIReference/API_SuggestableConfig.html): Provides the configuration information for a document field/attribute that you want to base query suggestions on.
- [Suggestion](https://docs.aws.amazon.com/kendra/latest/APIReference/API_Suggestion.html): A single query suggestion.
- [SuggestionHighlight](https://docs.aws.amazon.com/kendra/latest/APIReference/API_SuggestionHighlight.html): The text highlights for a single query suggestion.
- [SuggestionTextWithHighlights](https://docs.aws.amazon.com/kendra/latest/APIReference/API_SuggestionTextWithHighlights.html): Provides text and information about where to highlight the query suggestion text.
- [SuggestionValue](https://docs.aws.amazon.com/kendra/latest/APIReference/API_SuggestionValue.html): The SuggestionTextWithHighlights structure information.
- [TableCell](https://docs.aws.amazon.com/kendra/latest/APIReference/API_TableCell.html): Provides information about a table cell in a table excerpt.
- [TableExcerpt](https://docs.aws.amazon.com/kendra/latest/APIReference/API_TableExcerpt.html): An excerpt from a table within a document.
- [TableRow](https://docs.aws.amazon.com/kendra/latest/APIReference/API_TableRow.html): Information about a row in a table excerpt.
- [Tag](https://docs.aws.amazon.com/kendra/latest/APIReference/API_Tag.html): A key-value pair that identifies or categorizes an index, FAQ, data source, or other resource.
- [TemplateConfiguration](https://docs.aws.amazon.com/kendra/latest/APIReference/API_TemplateConfiguration.html): Provides a template for the configuration information to connect to your data source.
- [TextDocumentStatistics](https://docs.aws.amazon.com/kendra/latest/APIReference/API_TextDocumentStatistics.html): Provides information about text documents indexed in an index.
- [TextWithHighlights](https://docs.aws.amazon.com/kendra/latest/APIReference/API_TextWithHighlights.html): Provides text and information about where to highlight the text.
- [ThesaurusSummary](https://docs.aws.amazon.com/kendra/latest/APIReference/API_ThesaurusSummary.html): An array of summary information for a thesaurus or multiple thesauri.
- [TimeRange](https://docs.aws.amazon.com/kendra/latest/APIReference/API_TimeRange.html): Provides a range of time.
- [Urls](https://docs.aws.amazon.com/kendra/latest/APIReference/API_Urls.html): Provides the configuration information of the URLs to crawl.
- [UserContext](https://docs.aws.amazon.com/kendra/latest/APIReference/API_UserContext.html): Provides information about the user context for an Amazon Kendra index.
- [UserGroupResolutionConfiguration](https://docs.aws.amazon.com/kendra/latest/APIReference/API_UserGroupResolutionConfiguration.html): Provides the configuration information to get users and groups from an AWS IAM Identity Center identity source.
- [UserIdentityConfiguration](https://docs.aws.amazon.com/kendra/latest/APIReference/API_UserIdentityConfiguration.html): Provides the configuration information for the identifiers of your users.
- [UserTokenConfiguration](https://docs.aws.amazon.com/kendra/latest/APIReference/API_UserTokenConfiguration.html): Provides the configuration information for a token.
- [Warning](https://docs.aws.amazon.com/kendra/latest/APIReference/API_Warning.html): The warning code and message that explains a problem with a query.
- [WebCrawlerConfiguration](https://docs.aws.amazon.com/kendra/latest/APIReference/API_WebCrawlerConfiguration.html): Provides the configuration information required for Amazon Kendra Web Crawler.
- [WorkDocsConfiguration](https://docs.aws.amazon.com/kendra/latest/APIReference/API_WorkDocsConfiguration.html): Provides the configuration information to connect to WorkDocs as your data source.

### [Amazon Kendra Intelligent Ranking](https://docs.aws.amazon.com/kendra/latest/APIReference/API_Types_Amazon_Kendra_Intelligent_Ranking.html)

The following data types are supported by Amazon Kendra Intelligent Ranking:

- [CapacityUnitsConfiguration](https://docs.aws.amazon.com/kendra/latest/APIReference/API_Ranking_CapacityUnitsConfiguration.html): Sets additional capacity units configured for your rescore execution plan.
- [Document](https://docs.aws.amazon.com/kendra/latest/APIReference/API_Ranking_Document.html): Information about a document from a search service such as OpenSearch (self managed).
- [RescoreExecutionPlanSummary](https://docs.aws.amazon.com/kendra/latest/APIReference/API_Ranking_RescoreExecutionPlanSummary.html): Summary information for a rescore execution plan.
- [RescoreResultItem](https://docs.aws.amazon.com/kendra/latest/APIReference/API_Ranking_RescoreResultItem.html): A result item for a document with a new relevancy score.
- [Tag](https://docs.aws.amazon.com/kendra/latest/APIReference/API_Ranking_Tag.html): A key-value pair that identifies or categorizes a rescore execution plan.
- [Common Parameters](https://docs.aws.amazon.com/kendra/latest/APIReference/CommonParameters.html): The following list contains the parameters that all actions use for signing Signature Version 4 requests with a query string.
- [Common Errors](https://docs.aws.amazon.com/kendra/latest/APIReference/CommonErrors.html): This section lists the errors common to the API actions of all AWS services.
