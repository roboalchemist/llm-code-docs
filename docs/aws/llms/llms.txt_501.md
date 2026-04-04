# Source: https://docs.aws.amazon.com/keyspaces/latest/APIReference/llms.txt

# Amazon Keyspaces (for Apache Cassandra) API Reference

> Amazon Keyspaces (for Apache Cassandra) is a scalable, highly available, and managed Apache Cassandra-compatible database service. Amazon Keyspaces makes it easy to migrate, run, and scale Cassandra workloads in the AWS Cloud. With just a few clicks on the AWS Management Console or a few lines of code, you can create keyspaces and tables in Amazon Keyspaces, without deploying any infrastructure or installing software.

- [Welcome](https://docs.aws.amazon.com/keyspaces/latest/APIReference/Welcome.html)
- [Common Parameters](https://docs.aws.amazon.com/keyspaces/latest/APIReference/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/keyspaces/latest/APIReference/CommonErrors.html)

## [Actions](https://docs.aws.amazon.com/keyspaces/latest/APIReference/API_Operations.html)

- [CreateKeyspace](https://docs.aws.amazon.com/keyspaces/latest/APIReference/API_CreateKeyspace.html): The CreateKeyspace operation adds a new keyspace to your account.
- [CreateTable](https://docs.aws.amazon.com/keyspaces/latest/APIReference/API_CreateTable.html): The CreateTable operation adds a new table to the specified keyspace.
- [CreateType](https://docs.aws.amazon.com/keyspaces/latest/APIReference/API_CreateType.html): The CreateType operation creates a new user-defined type in the specified keyspace.
- [DeleteKeyspace](https://docs.aws.amazon.com/keyspaces/latest/APIReference/API_DeleteKeyspace.html): The DeleteKeyspace operation deletes a keyspace and all of its tables.
- [DeleteTable](https://docs.aws.amazon.com/keyspaces/latest/APIReference/API_DeleteTable.html): The DeleteTable operation deletes a table and all of its data.
- [DeleteType](https://docs.aws.amazon.com/keyspaces/latest/APIReference/API_DeleteType.html): The DeleteType operation deletes a user-defined type (UDT).
- [GetKeyspace](https://docs.aws.amazon.com/keyspaces/latest/APIReference/API_GetKeyspace.html): Returns the name of the specified keyspace, the Amazon Resource Name (ARN), the replication strategy, the AWS Regions of a multi-Region keyspace, and the status of newly added Regions after an UpdateKeyspace operation.
- [GetTable](https://docs.aws.amazon.com/keyspaces/latest/APIReference/API_GetTable.html): Returns information about the table, including the table's name and current status, the keyspace name, configuration settings, and metadata.
- [GetTableAutoScalingSettings](https://docs.aws.amazon.com/keyspaces/latest/APIReference/API_GetTableAutoScalingSettings.html): Returns auto scaling related settings of the specified table in JSON format.
- [GetType](https://docs.aws.amazon.com/keyspaces/latest/APIReference/API_GetType.html): The GetType operation returns information about the type, for example the field definitions, the timestamp when the type was last modified, the level of nesting, the status, and details about if the type is used in other types and tables.
- [ListKeyspaces](https://docs.aws.amazon.com/keyspaces/latest/APIReference/API_ListKeyspaces.html): The ListKeyspaces operation returns a list of keyspaces.
- [ListTables](https://docs.aws.amazon.com/keyspaces/latest/APIReference/API_ListTables.html): The ListTables operation returns a list of tables for a specified keyspace.
- [ListTagsForResource](https://docs.aws.amazon.com/keyspaces/latest/APIReference/API_ListTagsForResource.html): Returns a list of all tags associated with the specified Amazon Keyspaces resource.
- [ListTypes](https://docs.aws.amazon.com/keyspaces/latest/APIReference/API_ListTypes.html): The ListTypes operation returns a list of types for a specified keyspace.
- [RestoreTable](https://docs.aws.amazon.com/keyspaces/latest/APIReference/API_RestoreTable.html): Restores the table to the specified point in time within the earliest_restorable_timestamp and the current time.
- [TagResource](https://docs.aws.amazon.com/keyspaces/latest/APIReference/API_TagResource.html): Associates a set of tags with a Amazon Keyspaces resource.
- [UntagResource](https://docs.aws.amazon.com/keyspaces/latest/APIReference/API_UntagResource.html): Removes the association of tags from a Amazon Keyspaces resource.
- [UpdateKeyspace](https://docs.aws.amazon.com/keyspaces/latest/APIReference/API_UpdateKeyspace.html): Adds a new AWS Region to the keyspace.
- [UpdateTable](https://docs.aws.amazon.com/keyspaces/latest/APIReference/API_UpdateTable.html): Adds new columns to the table or updates one of the table's settings, for example capacity mode, auto scaling, encryption, point-in-time recovery, or ttl settings.


## [Data Types](https://docs.aws.amazon.com/keyspaces/latest/APIReference/API_Types.html)

- [AutoScalingPolicy](https://docs.aws.amazon.com/keyspaces/latest/APIReference/API_AutoScalingPolicy.html): Amazon Keyspaces supports the target tracking auto scaling policy.
- [AutoScalingSettings](https://docs.aws.amazon.com/keyspaces/latest/APIReference/API_AutoScalingSettings.html): The optional auto scaling settings for a table with provisioned throughput capacity.
- [AutoScalingSpecification](https://docs.aws.amazon.com/keyspaces/latest/APIReference/API_AutoScalingSpecification.html): The optional auto scaling capacity settings for a table in provisioned capacity mode.
- [CapacitySpecification](https://docs.aws.amazon.com/keyspaces/latest/APIReference/API_CapacitySpecification.html): Amazon Keyspaces has two read/write capacity modes for processing reads and writes on your tables:
- [CapacitySpecificationSummary](https://docs.aws.amazon.com/keyspaces/latest/APIReference/API_CapacitySpecificationSummary.html): The read/write throughput capacity mode for a table.
- [CdcSpecification](https://docs.aws.amazon.com/keyspaces/latest/APIReference/API_CdcSpecification.html): The settings for the CDC stream of a table.
- [CdcSpecificationSummary](https://docs.aws.amazon.com/keyspaces/latest/APIReference/API_CdcSpecificationSummary.html): The settings of the CDC stream of the table.
- [ClientSideTimestamps](https://docs.aws.amazon.com/keyspaces/latest/APIReference/API_ClientSideTimestamps.html): The client-side timestamp setting of the table.
- [ClusteringKey](https://docs.aws.amazon.com/keyspaces/latest/APIReference/API_ClusteringKey.html): The optional clustering column portion of your primary key determines how the data is clustered and sorted within each partition.
- [ColumnDefinition](https://docs.aws.amazon.com/keyspaces/latest/APIReference/API_ColumnDefinition.html): The names and data types of regular columns.
- [Comment](https://docs.aws.amazon.com/keyspaces/latest/APIReference/API_Comment.html): An optional comment that describes the table.
- [EncryptionSpecification](https://docs.aws.amazon.com/keyspaces/latest/APIReference/API_EncryptionSpecification.html): Amazon Keyspaces encrypts and decrypts the table data at rest transparently and integrates with AWS Key Management Service for storing and managing the encryption key.
- [FieldDefinition](https://docs.aws.amazon.com/keyspaces/latest/APIReference/API_FieldDefinition.html): A field definition consists out of a name and a type.
- [KeyspaceSummary](https://docs.aws.amazon.com/keyspaces/latest/APIReference/API_KeyspaceSummary.html): Represents the properties of a keyspace.
- [PartitionKey](https://docs.aws.amazon.com/keyspaces/latest/APIReference/API_PartitionKey.html): The partition key portion of the primary key is required and determines how Amazon Keyspaces stores the data.
- [PointInTimeRecovery](https://docs.aws.amazon.com/keyspaces/latest/APIReference/API_PointInTimeRecovery.html): Point-in-time recovery (PITR) helps protect your Amazon Keyspaces tables from accidental write or delete operations by providing you continuous backups of your table data.
- [PointInTimeRecoverySummary](https://docs.aws.amazon.com/keyspaces/latest/APIReference/API_PointInTimeRecoverySummary.html): The point-in-time recovery status of the specified table.
- [ReplicaAutoScalingSpecification](https://docs.aws.amazon.com/keyspaces/latest/APIReference/API_ReplicaAutoScalingSpecification.html): The auto scaling settings of a multi-Region table in the specified AWS Region.
- [ReplicaSpecification](https://docs.aws.amazon.com/keyspaces/latest/APIReference/API_ReplicaSpecification.html): The AWS Region specific settings of a multi-Region table.
- [ReplicaSpecificationSummary](https://docs.aws.amazon.com/keyspaces/latest/APIReference/API_ReplicaSpecificationSummary.html): The Region-specific settings of a multi-Region table in the specified AWS Region.
- [ReplicationGroupStatus](https://docs.aws.amazon.com/keyspaces/latest/APIReference/API_ReplicationGroupStatus.html): This shows the summary status of the keyspace after a new AWS Region was added.
- [ReplicationSpecification](https://docs.aws.amazon.com/keyspaces/latest/APIReference/API_ReplicationSpecification.html): The replication specification of the keyspace includes:
- [SchemaDefinition](https://docs.aws.amazon.com/keyspaces/latest/APIReference/API_SchemaDefinition.html): Describes the schema of the table.
- [StaticColumn](https://docs.aws.amazon.com/keyspaces/latest/APIReference/API_StaticColumn.html): The static columns of the table.
- [TableSummary](https://docs.aws.amazon.com/keyspaces/latest/APIReference/API_TableSummary.html): Returns the name of the specified table, the keyspace it is stored in, and the unique identifier in the format of an Amazon Resource Name (ARN).
- [Tag](https://docs.aws.amazon.com/keyspaces/latest/APIReference/API_Tag.html): Describes a tag.
- [TargetTrackingScalingPolicyConfiguration](https://docs.aws.amazon.com/keyspaces/latest/APIReference/API_TargetTrackingScalingPolicyConfiguration.html): The auto scaling policy that scales a table based on the ratio of consumed to provisioned capacity.
- [TimeToLive](https://docs.aws.amazon.com/keyspaces/latest/APIReference/API_TimeToLive.html): Enable custom Time to Live (TTL) settings for rows and columns without setting a TTL default for the specified table.
- [WarmThroughputSpecification](https://docs.aws.amazon.com/keyspaces/latest/APIReference/API_WarmThroughputSpecification.html): Specifies the warm throughput settings for a table.
- [WarmThroughputSpecificationSummary](https://docs.aws.amazon.com/keyspaces/latest/APIReference/API_WarmThroughputSpecificationSummary.html): Contains the current warm throughput settings for a table, including the configured capacity units and the current status of the warm throughput configuration.


## [Service-specific Errors](https://docs.aws.amazon.com/keyspaces/latest/APIReference/API_Errors.html)

- [AccessDeniedException](https://docs.aws.amazon.com/keyspaces/latest/APIReference/API_AccessDeniedException.html): You don't have sufficient access permissions to perform this action.
- [ConflictException](https://docs.aws.amazon.com/keyspaces/latest/APIReference/API_ConflictException.html): Amazon Keyspaces couldn't complete the requested action.
- [InternalServerException](https://docs.aws.amazon.com/keyspaces/latest/APIReference/API_InternalServerException.html): Amazon Keyspaces was unable to fully process this request because of an internal server error.
- [ResourceNotFoundException](https://docs.aws.amazon.com/keyspaces/latest/APIReference/API_ResourceNotFoundException.html): The operation tried to access a keyspace, table, or type that doesn't exist.
- [ServiceQuotaExceededException](https://docs.aws.amazon.com/keyspaces/latest/APIReference/API_ServiceQuotaExceededException.html): The operation exceeded the service quota for this resource.
- [ValidationException](https://docs.aws.amazon.com/keyspaces/latest/APIReference/API_ValidationException.html): The operation failed due to an invalid or malformed request.
