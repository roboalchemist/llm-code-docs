# Source: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/llms.txt

# Amazon DynamoDB API Reference

> Amazon DynamoDB is a fully managed NoSQL database service that provides fast and predictable performance with seamless scalability. DynamoDB lets you offload the administrative burdens of operating and scaling a distributed database, so that you don't have to worry about hardware provisioning, setup and configuration, replication, software patching, or cluster scaling.

- [Welcome](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/Welcome.html)
- [Common Errors](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/CommonErrors.html)

## [Actions](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_Operations.html)

### [Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_Operations_Amazon_DynamoDB.html)

The following actions are supported by Amazon DynamoDB:

- [BatchExecuteStatement](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_BatchExecuteStatement.html): This operation allows you to perform batch reads or writes on data stored in DynamoDB, using PartiQL.
- [BatchGetItem](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_BatchGetItem.html): The BatchGetItem operation returns the attributes of one or more items from one or more tables.
- [BatchWriteItem](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_BatchWriteItem.html): The BatchWriteItem operation puts or deletes multiple items in one or more tables.
- [CreateBackup](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_CreateBackup.html): Creates a backup for an existing table.
- [CreateGlobalTable](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_CreateGlobalTable.html): Creates a global table from an existing table.
- [CreateTable](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_CreateTable.html): The CreateTable operation adds a new table to your account.
- [DeleteBackup](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_DeleteBackup.html): Deletes an existing backup of a table.
- [DeleteItem](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_DeleteItem.html): Deletes a single item in a table by primary key.
- [DeleteResourcePolicy](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_DeleteResourcePolicy.html): Deletes the resource-based policy attached to the resource, which can be a table or stream.
- [DeleteTable](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_DeleteTable.html): The DeleteTable operation deletes a table and all of its items.
- [DescribeBackup](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_DescribeBackup.html): Describes an existing backup of a table.
- [DescribeContinuousBackups](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_DescribeContinuousBackups.html): Checks the status of continuous backups and point in time recovery on the specified table.
- [DescribeContributorInsights](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_DescribeContributorInsights.html): Returns information about contributor insights for a given table or global secondary index.
- [DescribeEndpoints](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_DescribeEndpoints.html): Returns the regional endpoint information.
- [DescribeExport](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_DescribeExport.html): Describes an existing table export.
- [DescribeGlobalTable](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_DescribeGlobalTable.html): Returns information about the specified global table.
- [DescribeGlobalTableSettings](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_DescribeGlobalTableSettings.html): Describes Region-specific settings for a global table.
- [DescribeImport](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_DescribeImport.html): Represents the properties of the import.
- [DescribeKinesisStreamingDestination](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_DescribeKinesisStreamingDestination.html): Returns information about the status of Kinesis streaming.
- [DescribeLimits](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_DescribeLimits.html): Returns the current provisioned-capacity quotas for your AWS account in a Region, both for the Region as a whole and for any one DynamoDB table that you create there.
- [DescribeTable](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_DescribeTable.html): Returns information about the table, including the current status of the table, when it was created, the primary key schema, and any indexes on the table.
- [DescribeTableReplicaAutoScaling](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_DescribeTableReplicaAutoScaling.html): Describes auto scaling settings across replicas of the global table at once.
- [DescribeTimeToLive](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_DescribeTimeToLive.html): Gives a description of the Time to Live (TTL) status on the specified table.
- [DisableKinesisStreamingDestination](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_DisableKinesisStreamingDestination.html): Stops replication from the DynamoDB table to the Kinesis data stream.
- [EnableKinesisStreamingDestination](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_EnableKinesisStreamingDestination.html): Starts table data replication to the specified Kinesis data stream at a timestamp chosen during the enable workflow.
- [ExecuteStatement](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ExecuteStatement.html): This operation allows you to perform reads and singleton writes on data stored in DynamoDB, using PartiQL.
- [ExecuteTransaction](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ExecuteTransaction.html): This operation allows you to perform transactional reads or writes on data stored in DynamoDB, using PartiQL.
- [ExportTableToPointInTime](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ExportTableToPointInTime.html): Exports table data to an S3 bucket.
- [GetItem](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_GetItem.html): The GetItem operation returns a set of attributes for the item with the given primary key.
- [GetResourcePolicy](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_GetResourcePolicy.html): Returns the resource-based policy document attached to the resource, which can be a table or stream, in JSON format.
- [ImportTable](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ImportTable.html): Imports table data from an S3 bucket.
- [ListBackups](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ListBackups.html): List DynamoDB backups that are associated with an AWS account and weren't made with AWS Backup.
- [ListContributorInsights](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ListContributorInsights.html): Returns a list of ContributorInsightsSummary for a table and all its global secondary indexes.
- [ListExports](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ListExports.html): Lists completed exports within the past 90 days, in reverse alphanumeric order of ExportArn.
- [ListGlobalTables](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ListGlobalTables.html): Lists all global tables that have a replica in the specified Region.
- [ListImports](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ListImports.html): Lists completed imports within the past 90 days.
- [ListTables](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ListTables.html): Returns an array of table names associated with the current account and endpoint.
- [ListTagsOfResource](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ListTagsOfResource.html): List all tags on an Amazon DynamoDB resource.
- [PutItem](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_PutItem.html): Creates a new item, or replaces an old item with a new item.
- [PutResourcePolicy](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_PutResourcePolicy.html): Attaches a resource-based policy document to the resource, which can be a table or stream.
- [Query](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_Query.html): You must provide the name of the partition key attribute and a single value for that attribute.
- [RestoreTableFromBackup](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_RestoreTableFromBackup.html): Creates a new table from an existing backup.
- [RestoreTableToPointInTime](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_RestoreTableToPointInTime.html): Restores the specified table to the specified point in time within EarliestRestorableDateTime and LatestRestorableDateTime.
- [Scan](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_Scan.html): The Scan operation returns one or more items and item attributes by accessing every item in a table or a secondary index.
- [TagResource](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_TagResource.html): Associate a set of tags with an Amazon DynamoDB resource.
- [TransactGetItems](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_TransactGetItems.html): TransactGetItems is a synchronous operation that atomically retrieves multiple items from one or more tables (but not from indexes) in a single account and Region.
- [TransactWriteItems](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_TransactWriteItems.html): TransactWriteItems is a synchronous write operation that groups up to 100 action requests.
- [UntagResource](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_UntagResource.html): Removes the association of tags from an Amazon DynamoDB resource.
- [UpdateContinuousBackups](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_UpdateContinuousBackups.html): UpdateContinuousBackups enables or disables point in time recovery for the specified table.
- [UpdateContributorInsights](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_UpdateContributorInsights.html): Updates the status for contributor insights for a specific table or index.
- [UpdateGlobalTable](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_UpdateGlobalTable.html): Adds or removes replicas in the specified global table.
- [UpdateGlobalTableSettings](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_UpdateGlobalTableSettings.html): Updates settings for a global table.
- [UpdateItem](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_UpdateItem.html): Edits an existing item's attributes, or adds a new item to the table if it does not already exist.
- [UpdateKinesisStreamingDestination](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_UpdateKinesisStreamingDestination.html): The command to update the Kinesis stream destination.
- [UpdateTable](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_UpdateTable.html): Modifies the provisioned throughput settings, global secondary indexes, or DynamoDB Streams settings for a given table.
- [UpdateTableReplicaAutoScaling](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_UpdateTableReplicaAutoScaling.html): Updates auto scaling settings on your global tables at once.
- [UpdateTimeToLive](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_UpdateTimeToLive.html): The UpdateTimeToLive method enables or disables Time to Live (TTL) for the specified table.

### [DynamoDB Accelerator](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_Operations_Amazon_DynamoDB_Accelerator__DAX_.html)

The following actions are supported by DynamoDB Accelerator:

- [CreateCluster](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_dax_CreateCluster.html): Creates a DAX cluster.
- [CreateParameterGroup](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_dax_CreateParameterGroup.html): Creates a new parameter group.
- [CreateSubnetGroup](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_dax_CreateSubnetGroup.html): Creates a new subnet group.
- [DecreaseReplicationFactor](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_dax_DecreaseReplicationFactor.html): Removes one or more nodes from a DAX cluster.
- [DeleteCluster](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_dax_DeleteCluster.html): Deletes a previously provisioned DAX cluster.
- [DeleteParameterGroup](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_dax_DeleteParameterGroup.html): Deletes the specified parameter group.
- [DeleteSubnetGroup](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_dax_DeleteSubnetGroup.html): Deletes a subnet group.
- [DescribeClusters](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_dax_DescribeClusters.html): Returns information about all provisioned DAX clusters if no cluster identifier is specified, or about a specific DAX cluster if a cluster identifier is supplied.
- [DescribeDefaultParameters](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_dax_DescribeDefaultParameters.html): Returns the default system parameter information for the DAX caching software.
- [DescribeEvents](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_dax_DescribeEvents.html): Returns events related to DAX clusters and parameter groups.
- [DescribeParameterGroups](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_dax_DescribeParameterGroups.html): Returns a list of parameter group descriptions.
- [DescribeParameters](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_dax_DescribeParameters.html): Returns the detailed parameter list for a particular parameter group.
- [DescribeSubnetGroups](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_dax_DescribeSubnetGroups.html): Returns a list of subnet group descriptions.
- [IncreaseReplicationFactor](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_dax_IncreaseReplicationFactor.html): Adds one or more nodes to a DAX cluster.
- [ListTags](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_dax_ListTags.html): List all of the tags for a DAX cluster.
- [RebootNode](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_dax_RebootNode.html): Reboots a single node of a DAX cluster.
- [TagResource](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_dax_TagResource.html): Associates a set of tags with a DAX resource.
- [UntagResource](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_dax_UntagResource.html): Removes the association of tags from a DAX resource.
- [UpdateCluster](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_dax_UpdateCluster.html): Modifies the settings for a DAX cluster.
- [UpdateParameterGroup](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_dax_UpdateParameterGroup.html): Modifies the parameters of a parameter group.
- [UpdateSubnetGroup](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_dax_UpdateSubnetGroup.html): Modifies an existing subnet group.

### [Amazon DynamoDB Streams](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_Operations_Amazon_DynamoDB_Streams.html)

The following actions are supported by Amazon DynamoDB Streams:

- [DescribeStream](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_streams_DescribeStream.html): Returns information about a stream, including the current status of the stream, its Amazon Resource Name (ARN), the composition of its shards, and its corresponding DynamoDB table.
- [GetRecords](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_streams_GetRecords.html): Retrieves the stream records from a given shard.
- [GetShardIterator](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_streams_GetShardIterator.html): Returns a shard iterator.
- [ListStreams](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_streams_ListStreams.html): Returns an array of stream ARNs associated with the current account and endpoint.


## [Data Types](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_Types.html)

### [Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_Types_Amazon_DynamoDB.html)

The following data types are supported by Amazon DynamoDB:

- [ArchivalSummary](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ArchivalSummary.html): Contains details of a table archival operation.
- [AttributeDefinition](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_AttributeDefinition.html): Represents an attribute for describing the schema for the table and indexes.
- [AttributeValue](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_AttributeValue.html): Represents the data for an attribute.
- [AttributeValueUpdate](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_AttributeValueUpdate.html): For the UpdateItem operation, represents the attributes to be modified, the action to perform on each, and the new value for each.
- [AutoScalingPolicyDescription](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_AutoScalingPolicyDescription.html): Represents the properties of the scaling policy.
- [AutoScalingPolicyUpdate](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_AutoScalingPolicyUpdate.html): Represents the auto scaling policy to be modified.
- [AutoScalingSettingsDescription](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_AutoScalingSettingsDescription.html): Represents the auto scaling settings for a global table or global secondary index.
- [AutoScalingSettingsUpdate](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_AutoScalingSettingsUpdate.html): Represents the auto scaling settings to be modified for a global table or global secondary index.
- [AutoScalingTargetTrackingScalingPolicyConfigurationDescription](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_AutoScalingTargetTrackingScalingPolicyConfigurationDescription.html): Represents the properties of a target tracking scaling policy.
- [AutoScalingTargetTrackingScalingPolicyConfigurationUpdate](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_AutoScalingTargetTrackingScalingPolicyConfigurationUpdate.html): Represents the settings of a target tracking scaling policy that will be modified.
- [BackupDescription](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_BackupDescription.html): Contains the description of the backup created for the table.
- [BackupDetails](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_BackupDetails.html): Contains the details of the backup created for the table.
- [BackupSummary](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_BackupSummary.html): Contains details for the backup.
- [BatchStatementError](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_BatchStatementError.html): An error associated with a statement in a PartiQL batch that was run.
- [BatchStatementRequest](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_BatchStatementRequest.html): A PartiQL batch statement request.
- [BatchStatementResponse](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_BatchStatementResponse.html): A PartiQL batch statement response..
- [BillingModeSummary](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_BillingModeSummary.html): Contains the details for the read/write capacity mode.
- [CancellationReason](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_CancellationReason.html): An ordered list of errors for each item in the request which caused the transaction to get cancelled.
- [Capacity](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_Capacity.html): Represents the amount of provisioned throughput capacity consumed on a table or an index.
- [Condition](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_Condition.html): Represents the selection criteria for a Query or Scan operation:
- [ConditionCheck](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ConditionCheck.html): Represents a request to perform a check that an item exists or to check the condition of specific attributes of the item.
- [ConsumedCapacity](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ConsumedCapacity.html): The capacity units consumed by an operation.
- [ContinuousBackupsDescription](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ContinuousBackupsDescription.html): Represents the continuous backups and point in time recovery settings on the table.
- [ContributorInsightsSummary](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ContributorInsightsSummary.html): Represents a Contributor Insights summary entry.
- [CreateGlobalSecondaryIndexAction](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_CreateGlobalSecondaryIndexAction.html): Represents a new global secondary index to be added to an existing table.
- [CreateGlobalTableWitnessGroupMemberAction](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_CreateGlobalTableWitnessGroupMemberAction.html): Specifies the action to add a new witness Region to a MRSC global table.
- [CreateReplicaAction](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_CreateReplicaAction.html): Represents a replica to be added.
- [CreateReplicationGroupMemberAction](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_CreateReplicationGroupMemberAction.html): Represents a replica to be created.
- [CsvOptions](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_CsvOptions.html): Processing options for the CSV file being imported.
- [Delete](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_Delete.html): Represents a request to perform a DeleteItem operation.
- [DeleteGlobalSecondaryIndexAction](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_DeleteGlobalSecondaryIndexAction.html): Represents a global secondary index to be deleted from an existing table.
- [DeleteGlobalTableWitnessGroupMemberAction](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_DeleteGlobalTableWitnessGroupMemberAction.html): Specifies the action to remove a witness Region from a MRSC global table.
- [DeleteReplicaAction](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_DeleteReplicaAction.html): Represents a replica to be removed.
- [DeleteReplicationGroupMemberAction](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_DeleteReplicationGroupMemberAction.html): Represents a replica to be deleted.
- [DeleteRequest](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_DeleteRequest.html): Represents a request to perform a DeleteItem operation on an item.
- [EnableKinesisStreamingConfiguration](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_EnableKinesisStreamingConfiguration.html): Enables setting the configuration for Kinesis Streaming.
- [Endpoint](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_Endpoint.html): An endpoint information details.
- [ExpectedAttributeValue](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ExpectedAttributeValue.html): Represents a condition to be compared with an attribute value.
- [ExportDescription](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ExportDescription.html): Represents the properties of the exported table.
- [ExportSummary](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ExportSummary.html): Summary information about an export task.
- [FailureException](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_FailureException.html): Represents a failure a contributor insights operation.
- [Get](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_Get.html): Specifies an item and related attribute values to retrieve in a TransactGetItem object.
- [GlobalSecondaryIndex](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_GlobalSecondaryIndex.html): Represents the properties of a global secondary index.
- [GlobalSecondaryIndexAutoScalingUpdate](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_GlobalSecondaryIndexAutoScalingUpdate.html): Represents the auto scaling settings of a global secondary index for a global table that will be modified.
- [GlobalSecondaryIndexDescription](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_GlobalSecondaryIndexDescription.html): Represents the properties of a global secondary index.
- [GlobalSecondaryIndexInfo](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_GlobalSecondaryIndexInfo.html): Represents the properties of a global secondary index for the table when the backup was created.
- [GlobalSecondaryIndexUpdate](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_GlobalSecondaryIndexUpdate.html): Represents one of the following:
- [GlobalSecondaryIndexWarmThroughputDescription](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_GlobalSecondaryIndexWarmThroughputDescription.html): The description of the warm throughput value on a global secondary index.
- [GlobalTable](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_GlobalTable.html): Represents the properties of a global table.
- [GlobalTableDescription](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_GlobalTableDescription.html): Contains details about the global table.
- [GlobalTableGlobalSecondaryIndexSettingsUpdate](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_GlobalTableGlobalSecondaryIndexSettingsUpdate.html): Represents the settings of a global secondary index for a global table that will be modified.
- [GlobalTableWitnessDescription](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_GlobalTableWitnessDescription.html): Represents the properties of a witness Region in a MRSC global table.
- [GlobalTableWitnessGroupUpdate](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_GlobalTableWitnessGroupUpdate.html): Represents one of the following:
- [ImportSummary](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ImportSummary.html): Summary information about the source file for the import.
- [ImportTableDescription](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ImportTableDescription.html): Represents the properties of the table being imported into.
- [IncrementalExportSpecification](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_IncrementalExportSpecification.html): Optional object containing the parameters specific to an incremental export.
- [InputFormatOptions](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_InputFormatOptions.html): The format options for the data that was imported into the target table.
- [ItemCollectionMetrics](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ItemCollectionMetrics.html): Information about item collections, if any, that were affected by the operation.
- [ItemResponse](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ItemResponse.html): Details for the requested item.
- [KeysAndAttributes](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_KeysAndAttributes.html): Represents a set of primary keys and, for each key, the attributes to retrieve from the table.
- [KeySchemaElement](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_KeySchemaElement.html): Represents a single element of a key schema.
- [KinesisDataStreamDestination](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_KinesisDataStreamDestination.html): Describes a Kinesis data stream destination.
- [LocalSecondaryIndex](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_LocalSecondaryIndex.html): Represents the properties of a local secondary index.
- [LocalSecondaryIndexDescription](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_LocalSecondaryIndexDescription.html): Represents the properties of a local secondary index.
- [LocalSecondaryIndexInfo](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_LocalSecondaryIndexInfo.html): Represents the properties of a local secondary index for the table when the backup was created.
- [OnDemandThroughput](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_OnDemandThroughput.html): Sets the maximum number of read and write units for the specified on-demand table.
- [OnDemandThroughputOverride](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_OnDemandThroughputOverride.html): Overrides the on-demand throughput settings for this replica table.
- [ParameterizedStatement](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ParameterizedStatement.html): Represents a PartiQL statement that uses parameters.
- [PointInTimeRecoveryDescription](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_PointInTimeRecoveryDescription.html): The description of the point in time settings applied to the table.
- [PointInTimeRecoverySpecification](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_PointInTimeRecoverySpecification.html): Represents the settings used to enable point in time recovery.
- [Projection](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_Projection.html): Represents attributes that are copied (projected) from the table into an index.
- [ProvisionedThroughput](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ProvisionedThroughput.html): Represents the provisioned throughput settings for the specified global secondary index.
- [ProvisionedThroughputDescription](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ProvisionedThroughputDescription.html): Represents the provisioned throughput settings for the table, consisting of read and write capacity units, along with data about increases and decreases.
- [ProvisionedThroughputOverride](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ProvisionedThroughputOverride.html): Replica-specific provisioned throughput settings.
- [Put](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_Put.html): Represents a request to perform a PutItem operation.
- [PutRequest](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_PutRequest.html): Represents a request to perform a PutItem operation on an item.
- [Replica](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_Replica.html): Represents the properties of a replica.
- [ReplicaAutoScalingDescription](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ReplicaAutoScalingDescription.html): Represents the auto scaling settings of the replica.
- [ReplicaAutoScalingUpdate](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ReplicaAutoScalingUpdate.html): Represents the auto scaling settings of a replica that will be modified.
- [ReplicaDescription](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ReplicaDescription.html): Contains the details of the replica.
- [ReplicaGlobalSecondaryIndex](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ReplicaGlobalSecondaryIndex.html): Represents the properties of a replica global secondary index.
- [ReplicaGlobalSecondaryIndexAutoScalingDescription](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ReplicaGlobalSecondaryIndexAutoScalingDescription.html): Represents the auto scaling configuration for a replica global secondary index.
- [ReplicaGlobalSecondaryIndexAutoScalingUpdate](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ReplicaGlobalSecondaryIndexAutoScalingUpdate.html): Represents the auto scaling settings of a global secondary index for a replica that will be modified.
- [ReplicaGlobalSecondaryIndexDescription](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ReplicaGlobalSecondaryIndexDescription.html): Represents the properties of a replica global secondary index.
- [ReplicaGlobalSecondaryIndexSettingsDescription](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ReplicaGlobalSecondaryIndexSettingsDescription.html): Represents the properties of a global secondary index.
- [ReplicaGlobalSecondaryIndexSettingsUpdate](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ReplicaGlobalSecondaryIndexSettingsUpdate.html): Represents the settings of a global secondary index for a global table that will be modified.
- [ReplicaSettingsDescription](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ReplicaSettingsDescription.html): Represents the properties of a replica.
- [ReplicaSettingsUpdate](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ReplicaSettingsUpdate.html): Represents the settings for a global table in a Region that will be modified.
- [ReplicationGroupUpdate](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ReplicationGroupUpdate.html): Represents one of the following:
- [ReplicaUpdate](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ReplicaUpdate.html): Represents one of the following:
- [RestoreSummary](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_RestoreSummary.html): Contains details for the restore.
- [S3BucketSource](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_S3BucketSource.html): The S3 bucket that is being imported from.
- [SourceTableDetails](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_SourceTableDetails.html): Contains the details of the table when the backup was created.
- [SourceTableFeatureDetails](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_SourceTableFeatureDetails.html): Contains the details of the features enabled on the table when the backup was created.
- [SSEDescription](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_SSEDescription.html): The description of the server-side encryption status on the specified table.
- [SSESpecification](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_SSESpecification.html): Represents the settings used to enable server-side encryption.
- [StreamSpecification](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_StreamSpecification.html): Represents the DynamoDB Streams configuration for a table in DynamoDB.
- [TableAutoScalingDescription](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_TableAutoScalingDescription.html): Represents the auto scaling configuration for a global table.
- [TableClassSummary](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_TableClassSummary.html): Contains details of the table class.
- [TableCreationParameters](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_TableCreationParameters.html): The parameters for the table created as part of the import operation.
- [TableDescription](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_TableDescription.html): Represents the properties of a table.
- [TableWarmThroughputDescription](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_TableWarmThroughputDescription.html): Represents the warm throughput value (in read units per second and write units per second) of the table.
- [Tag](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_Tag.html): Describes a tag.
- [ThrottlingReason](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ThrottlingReason.html): Represents the specific reason why a DynamoDB request was throttled and the ARN of the impacted resource.
- [TimeToLiveDescription](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_TimeToLiveDescription.html): The description of the Time to Live (TTL) status on the specified table.
- [TimeToLiveSpecification](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_TimeToLiveSpecification.html): Represents the settings used to enable or disable Time to Live (TTL) for the specified table.
- [TransactGetItem](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_TransactGetItem.html): Specifies an item to be retrieved as part of the transaction.
- [TransactWriteItem](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_TransactWriteItem.html): A list of requests that can perform update, put, delete, or check operations on multiple items in one or more tables atomically.
- [Update](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_Update.html): Represents a request to perform an UpdateItem operation.
- [UpdateGlobalSecondaryIndexAction](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_UpdateGlobalSecondaryIndexAction.html): Represents the new provisioned throughput settings to be applied to a global secondary index.
- [UpdateKinesisStreamingConfiguration](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_UpdateKinesisStreamingConfiguration.html): Enables updating the configuration for Kinesis Streaming.
- [UpdateReplicationGroupMemberAction](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_UpdateReplicationGroupMemberAction.html): Represents a replica to be modified.
- [WarmThroughput](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_WarmThroughput.html): Provides visibility into the number of read and write operations your table or secondary index can instantaneously support.
- [WriteRequest](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_WriteRequest.html): Represents an operation to perform - either DeleteItem or PutItem.

### [DynamoDB Accelerator](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_Types_Amazon_DynamoDB_Accelerator__DAX_.html)

The following data types are supported by DynamoDB Accelerator:

- [Cluster](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_dax_Cluster.html): Contains all of the attributes of a specific DAX cluster.
- [Endpoint](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_dax_Endpoint.html): Represents the information required for client programs to connect to the endpoint for a DAX cluster.
- [Event](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_dax_Event.html): Represents a single occurrence of something interesting within the system.
- [Node](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_dax_Node.html): Represents an individual node within a DAX cluster.
- [NodeTypeSpecificValue](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_dax_NodeTypeSpecificValue.html): Represents a parameter value that is applicable to a particular node type.
- [NotificationConfiguration](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_dax_NotificationConfiguration.html): Describes a notification topic and its status.
- [Parameter](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_dax_Parameter.html): Describes an individual setting that controls some aspect of DAX behavior.
- [ParameterGroup](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_dax_ParameterGroup.html): A named set of parameters that are applied to all of the nodes in a DAX cluster.
- [ParameterGroupStatus](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_dax_ParameterGroupStatus.html): The status of a parameter group.
- [ParameterNameValue](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_dax_ParameterNameValue.html): An individual DAX parameter.
- [SecurityGroupMembership](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_dax_SecurityGroupMembership.html): An individual VPC security group and its status.
- [SSEDescription](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_dax_SSEDescription.html): The description of the server-side encryption status on the specified DAX cluster.
- [SSESpecification](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_dax_SSESpecification.html): Represents the settings used to enable server-side encryption.
- [Subnet](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_dax_Subnet.html): Represents the subnet associated with a DAX cluster.
- [SubnetGroup](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_dax_SubnetGroup.html): Represents the output of one of the following actions:
- [Tag](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_dax_Tag.html): A description of a tag.

### [Amazon DynamoDB Streams](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_Types_Amazon_DynamoDB_Streams.html)

The following data types are supported by Amazon DynamoDB Streams:

- [AttributeValue](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_streams_AttributeValue.html): Represents the data for an attribute.
- [Identity](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_streams_Identity.html): Contains details about the type of identity that made the request.
- [KeySchemaElement](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_streams_KeySchemaElement.html): Represents a single element of a key schema.
- [Record](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_streams_Record.html): A description of a unique event within a stream.
- [SequenceNumberRange](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_streams_SequenceNumberRange.html): The beginning and ending sequence numbers for the stream records contained within a shard.
- [Shard](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_streams_Shard.html): A uniquely identified group of stream records within a stream.
- [ShardFilter](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_streams_ShardFilter.html): This optional field contains the filter definition for the DescribeStream API.
- [Stream](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_streams_Stream.html): Represents all of the data describing a particular stream.
- [StreamDescription](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_streams_StreamDescription.html): Represents all of the data describing a particular stream.
- [StreamRecord](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_streams_StreamRecord.html): A description of a single data modification that was performed on an item in a DynamoDB table.
