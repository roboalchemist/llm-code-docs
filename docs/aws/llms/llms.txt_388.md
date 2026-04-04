# Source: https://docs.aws.amazon.com/firehose/latest/APIReference/llms.txt

# Amazon Data Firehose API Reference

> Amazon Data Firehose is a fully managed service that delivers real-time streaming data to destinations such as Amazon Simple Storage Service (Amazon S3), Amazon OpenSearch Service, Amazon Redshift, Splunk, and various other supported destinations.

- [Welcome](https://docs.aws.amazon.com/firehose/latest/APIReference/Welcome.html)
- [Common Errors](https://docs.aws.amazon.com/firehose/latest/APIReference/CommonErrors.html)

## [Actions](https://docs.aws.amazon.com/firehose/latest/APIReference/API_Operations.html)

- [CreateDeliveryStream](https://docs.aws.amazon.com/firehose/latest/APIReference/API_CreateDeliveryStream.html): Creates a Firehose stream.
- [DeleteDeliveryStream](https://docs.aws.amazon.com/firehose/latest/APIReference/API_DeleteDeliveryStream.html): Deletes a Firehose stream and its data.
- [DescribeDeliveryStream](https://docs.aws.amazon.com/firehose/latest/APIReference/API_DescribeDeliveryStream.html): Describes the specified Firehose stream and its status.
- [ListDeliveryStreams](https://docs.aws.amazon.com/firehose/latest/APIReference/API_ListDeliveryStreams.html): Lists your Firehose streams in alphabetical order of their names.
- [ListTagsForDeliveryStream](https://docs.aws.amazon.com/firehose/latest/APIReference/API_ListTagsForDeliveryStream.html): Lists the tags for the specified Firehose stream.
- [PutRecord](https://docs.aws.amazon.com/firehose/latest/APIReference/API_PutRecord.html): Writes a single data record into an Firehose stream.
- [PutRecordBatch](https://docs.aws.amazon.com/firehose/latest/APIReference/API_PutRecordBatch.html): Writes multiple data records into a Firehose stream in a single call, which can achieve higher throughput per producer than when writing single records.
- [StartDeliveryStreamEncryption](https://docs.aws.amazon.com/firehose/latest/APIReference/API_StartDeliveryStreamEncryption.html): Enables server-side encryption (SSE) for the Firehose stream.
- [StopDeliveryStreamEncryption](https://docs.aws.amazon.com/firehose/latest/APIReference/API_StopDeliveryStreamEncryption.html): Disables server-side encryption (SSE) for the Firehose stream.
- [TagDeliveryStream](https://docs.aws.amazon.com/firehose/latest/APIReference/API_TagDeliveryStream.html): Adds or updates tags for the specified Firehose stream.
- [UntagDeliveryStream](https://docs.aws.amazon.com/firehose/latest/APIReference/API_UntagDeliveryStream.html): Removes tags from the specified Firehose stream.
- [UpdateDestination](https://docs.aws.amazon.com/firehose/latest/APIReference/API_UpdateDestination.html): Updates the specified destination of the specified Firehose stream.


## [Data Types](https://docs.aws.amazon.com/firehose/latest/APIReference/API_Types.html)

- [AmazonOpenSearchServerlessBufferingHints](https://docs.aws.amazon.com/firehose/latest/APIReference/API_AmazonOpenSearchServerlessBufferingHints.html): Describes the buffering to perform before delivering data to the Serverless offering for Amazon OpenSearch Service destination.
- [AmazonOpenSearchServerlessDestinationConfiguration](https://docs.aws.amazon.com/firehose/latest/APIReference/API_AmazonOpenSearchServerlessDestinationConfiguration.html): Describes the configuration of a destination in the Serverless offering for Amazon OpenSearch Service.
- [AmazonOpenSearchServerlessDestinationDescription](https://docs.aws.amazon.com/firehose/latest/APIReference/API_AmazonOpenSearchServerlessDestinationDescription.html): The destination description in the Serverless offering for Amazon OpenSearch Service.
- [AmazonOpenSearchServerlessDestinationUpdate](https://docs.aws.amazon.com/firehose/latest/APIReference/API_AmazonOpenSearchServerlessDestinationUpdate.html): Describes an update for a destination in the Serverless offering for Amazon OpenSearch Service.
- [AmazonOpenSearchServerlessRetryOptions](https://docs.aws.amazon.com/firehose/latest/APIReference/API_AmazonOpenSearchServerlessRetryOptions.html): Configures retry behavior in case Firehose is unable to deliver documents to the Serverless offering for Amazon OpenSearch Service.
- [AmazonopensearchserviceBufferingHints](https://docs.aws.amazon.com/firehose/latest/APIReference/API_AmazonopensearchserviceBufferingHints.html): Describes the buffering to perform before delivering data to the Amazon OpenSearch Service destination.
- [AmazonopensearchserviceDestinationConfiguration](https://docs.aws.amazon.com/firehose/latest/APIReference/API_AmazonopensearchserviceDestinationConfiguration.html): Describes the configuration of a destination in Amazon OpenSearch Service
- [AmazonopensearchserviceDestinationDescription](https://docs.aws.amazon.com/firehose/latest/APIReference/API_AmazonopensearchserviceDestinationDescription.html): The destination description in Amazon OpenSearch Service.
- [AmazonopensearchserviceDestinationUpdate](https://docs.aws.amazon.com/firehose/latest/APIReference/API_AmazonopensearchserviceDestinationUpdate.html): Describes an update for a destination in Amazon OpenSearch Service.
- [AmazonopensearchserviceRetryOptions](https://docs.aws.amazon.com/firehose/latest/APIReference/API_AmazonopensearchserviceRetryOptions.html): Configures retry behavior in case Firehose is unable to deliver documents to Amazon OpenSearch Service.
- [AuthenticationConfiguration](https://docs.aws.amazon.com/firehose/latest/APIReference/API_AuthenticationConfiguration.html): The authentication configuration of the Amazon MSK cluster.
- [BufferingHints](https://docs.aws.amazon.com/firehose/latest/APIReference/API_BufferingHints.html): Describes hints for the buffering to perform before delivering data to the destination.
- [CatalogConfiguration](https://docs.aws.amazon.com/firehose/latest/APIReference/API_CatalogConfiguration.html): Describes the containers where the destination Apache Iceberg Tables are persisted.
- [CloudWatchLoggingOptions](https://docs.aws.amazon.com/firehose/latest/APIReference/API_CloudWatchLoggingOptions.html): Describes the Amazon CloudWatch logging options for your Firehose stream.
- [CopyCommand](https://docs.aws.amazon.com/firehose/latest/APIReference/API_CopyCommand.html): Describes a COPY command for Amazon Redshift.
- [DatabaseColumnList](https://docs.aws.amazon.com/firehose/latest/APIReference/API_DatabaseColumnList.html): The structure used to configure the list of column patterns in source database endpoint for Firehose to read from.
- [DatabaseList](https://docs.aws.amazon.com/firehose/latest/APIReference/API_DatabaseList.html): The structure used to configure the list of database patterns in source database endpoint for Firehose to read from.
- [DatabaseSnapshotInfo](https://docs.aws.amazon.com/firehose/latest/APIReference/API_DatabaseSnapshotInfo.html): The structure that describes the snapshot information of a table in source database endpoint that Firehose reads.
- [DatabaseSourceAuthenticationConfiguration](https://docs.aws.amazon.com/firehose/latest/APIReference/API_DatabaseSourceAuthenticationConfiguration.html): The structure to configure the authentication methods for Firehose to connect to source database endpoint.
- [DatabaseSourceConfiguration](https://docs.aws.amazon.com/firehose/latest/APIReference/API_DatabaseSourceConfiguration.html): The top level object for configuring streams with database as a source.
- [DatabaseSourceDescription](https://docs.aws.amazon.com/firehose/latest/APIReference/API_DatabaseSourceDescription.html): The top level object for database source description.
- [DatabaseSourceVPCConfiguration](https://docs.aws.amazon.com/firehose/latest/APIReference/API_DatabaseSourceVPCConfiguration.html): The structure for details of the VPC Endpoint Service which Firehose uses to create a PrivateLink to the database.
- [DatabaseTableList](https://docs.aws.amazon.com/firehose/latest/APIReference/API_DatabaseTableList.html): The structure used to configure the list of table patterns in source database endpoint for Firehose to read from.
- [DataFormatConversionConfiguration](https://docs.aws.amazon.com/firehose/latest/APIReference/API_DataFormatConversionConfiguration.html): Specifies that you want Firehose to convert data from the JSON format to the Parquet or ORC format before writing it to Amazon S3.
- [DeliveryStreamDescription](https://docs.aws.amazon.com/firehose/latest/APIReference/API_DeliveryStreamDescription.html): Contains information about a Firehose stream.
- [DeliveryStreamEncryptionConfiguration](https://docs.aws.amazon.com/firehose/latest/APIReference/API_DeliveryStreamEncryptionConfiguration.html): Contains information about the server-side encryption (SSE) status for the delivery stream, the type customer master key (CMK) in use, if any, and the ARN of the CMK.
- [DeliveryStreamEncryptionConfigurationInput](https://docs.aws.amazon.com/firehose/latest/APIReference/API_DeliveryStreamEncryptionConfigurationInput.html): Specifies the type and Amazon Resource Name (ARN) of the CMK to use for Server-Side Encryption (SSE).
- [Deserializer](https://docs.aws.amazon.com/firehose/latest/APIReference/API_Deserializer.html): The deserializer you want Firehose to use for converting the input data from JSON.
- [DestinationDescription](https://docs.aws.amazon.com/firehose/latest/APIReference/API_DestinationDescription.html): Describes the destination for a Firehose stream.
- [DestinationTableConfiguration](https://docs.aws.amazon.com/firehose/latest/APIReference/API_DestinationTableConfiguration.html): Describes the configuration of a destination in Apache Iceberg Tables.
- [DirectPutSourceConfiguration](https://docs.aws.amazon.com/firehose/latest/APIReference/API_DirectPutSourceConfiguration.html): The structure that configures parameters such as ThroughputHintInMBs for a stream configured with Direct PUT as a source.
- [DirectPutSourceDescription](https://docs.aws.amazon.com/firehose/latest/APIReference/API_DirectPutSourceDescription.html): The structure that configures parameters such as ThroughputHintInMBs for a stream configured with Direct PUT as a source.
- [DocumentIdOptions](https://docs.aws.amazon.com/firehose/latest/APIReference/API_DocumentIdOptions.html): Indicates the method for setting up document ID.
- [DynamicPartitioningConfiguration](https://docs.aws.amazon.com/firehose/latest/APIReference/API_DynamicPartitioningConfiguration.html): The configuration of the dynamic partitioning mechanism that creates smaller data sets from the streaming data by partitioning it based on partition keys.
- [ElasticsearchBufferingHints](https://docs.aws.amazon.com/firehose/latest/APIReference/API_ElasticsearchBufferingHints.html): Describes the buffering to perform before delivering data to the Amazon OpenSearch Service destination.
- [ElasticsearchDestinationConfiguration](https://docs.aws.amazon.com/firehose/latest/APIReference/API_ElasticsearchDestinationConfiguration.html): Describes the configuration of a destination in Amazon OpenSearch Service.
- [ElasticsearchDestinationDescription](https://docs.aws.amazon.com/firehose/latest/APIReference/API_ElasticsearchDestinationDescription.html): The destination description in Amazon OpenSearch Service.
- [ElasticsearchDestinationUpdate](https://docs.aws.amazon.com/firehose/latest/APIReference/API_ElasticsearchDestinationUpdate.html): Describes an update for a destination in Amazon OpenSearch Service.
- [ElasticsearchRetryOptions](https://docs.aws.amazon.com/firehose/latest/APIReference/API_ElasticsearchRetryOptions.html): Configures retry behavior in case Firehose is unable to deliver documents to Amazon OpenSearch Service.
- [EncryptionConfiguration](https://docs.aws.amazon.com/firehose/latest/APIReference/API_EncryptionConfiguration.html): Describes the encryption for a destination in Amazon S3.
- [ExtendedS3DestinationConfiguration](https://docs.aws.amazon.com/firehose/latest/APIReference/API_ExtendedS3DestinationConfiguration.html): Describes the configuration of a destination in Amazon S3.
- [ExtendedS3DestinationDescription](https://docs.aws.amazon.com/firehose/latest/APIReference/API_ExtendedS3DestinationDescription.html): Describes a destination in Amazon S3.
- [ExtendedS3DestinationUpdate](https://docs.aws.amazon.com/firehose/latest/APIReference/API_ExtendedS3DestinationUpdate.html): Describes an update for a destination in Amazon S3.
- [FailureDescription](https://docs.aws.amazon.com/firehose/latest/APIReference/API_FailureDescription.html): Provides details in case one of the following operations fails due to an error related to KMS: , , , .
- [HiveJsonSerDe](https://docs.aws.amazon.com/firehose/latest/APIReference/API_HiveJsonSerDe.html): The native Hive / HCatalog JsonSerDe.
- [HttpEndpointBufferingHints](https://docs.aws.amazon.com/firehose/latest/APIReference/API_HttpEndpointBufferingHints.html): Describes the buffering options that can be applied before data is delivered to the HTTP endpoint destination.
- [HttpEndpointCommonAttribute](https://docs.aws.amazon.com/firehose/latest/APIReference/API_HttpEndpointCommonAttribute.html): Describes the metadata that's delivered to the specified HTTP endpoint destination.
- [HttpEndpointConfiguration](https://docs.aws.amazon.com/firehose/latest/APIReference/API_HttpEndpointConfiguration.html): Describes the configuration of the HTTP endpoint to which Kinesis Firehose delivers data.
- [HttpEndpointDescription](https://docs.aws.amazon.com/firehose/latest/APIReference/API_HttpEndpointDescription.html): Describes the HTTP endpoint selected as the destination.
- [HttpEndpointDestinationConfiguration](https://docs.aws.amazon.com/firehose/latest/APIReference/API_HttpEndpointDestinationConfiguration.html): Describes the configuration of the HTTP endpoint destination.
- [HttpEndpointDestinationDescription](https://docs.aws.amazon.com/firehose/latest/APIReference/API_HttpEndpointDestinationDescription.html): Describes the HTTP endpoint destination.
- [HttpEndpointDestinationUpdate](https://docs.aws.amazon.com/firehose/latest/APIReference/API_HttpEndpointDestinationUpdate.html): Updates the specified HTTP endpoint destination.
- [HttpEndpointRequestConfiguration](https://docs.aws.amazon.com/firehose/latest/APIReference/API_HttpEndpointRequestConfiguration.html): The configuration of the HTTP endpoint request.
- [HttpEndpointRetryOptions](https://docs.aws.amazon.com/firehose/latest/APIReference/API_HttpEndpointRetryOptions.html): Describes the retry behavior in case Firehose is unable to deliver data to the specified HTTP endpoint destination, or if it doesn't receive a valid acknowledgment of receipt from the specified HTTP endpoint destination.
- [IcebergDestinationConfiguration](https://docs.aws.amazon.com/firehose/latest/APIReference/API_IcebergDestinationConfiguration.html): Specifies the destination configure settings for Apache Iceberg Table.
- [IcebergDestinationDescription](https://docs.aws.amazon.com/firehose/latest/APIReference/API_IcebergDestinationDescription.html): Describes a destination in Apache Iceberg Tables.
- [IcebergDestinationUpdate](https://docs.aws.amazon.com/firehose/latest/APIReference/API_IcebergDestinationUpdate.html): Describes an update for a destination in Apache Iceberg Tables.
- [InputFormatConfiguration](https://docs.aws.amazon.com/firehose/latest/APIReference/API_InputFormatConfiguration.html): Specifies the deserializer you want to use to convert the format of the input data.
- [KinesisStreamSourceConfiguration](https://docs.aws.amazon.com/firehose/latest/APIReference/API_KinesisStreamSourceConfiguration.html): The stream and role Amazon Resource Names (ARNs) for a Kinesis data stream used as the source for a Firehose stream.
- [KinesisStreamSourceDescription](https://docs.aws.amazon.com/firehose/latest/APIReference/API_KinesisStreamSourceDescription.html): Details about a Kinesis data stream used as the source for a Firehose stream.
- [KMSEncryptionConfig](https://docs.aws.amazon.com/firehose/latest/APIReference/API_KMSEncryptionConfig.html): Describes an encryption key for a destination in Amazon S3.
- [MSKSourceConfiguration](https://docs.aws.amazon.com/firehose/latest/APIReference/API_MSKSourceConfiguration.html): The configuration for the Amazon MSK cluster to be used as the source for a delivery stream.
- [MSKSourceDescription](https://docs.aws.amazon.com/firehose/latest/APIReference/API_MSKSourceDescription.html): Details about the Amazon MSK cluster used as the source for a Firehose stream.
- [OpenXJsonSerDe](https://docs.aws.amazon.com/firehose/latest/APIReference/API_OpenXJsonSerDe.html): The OpenX SerDe.
- [OrcSerDe](https://docs.aws.amazon.com/firehose/latest/APIReference/API_OrcSerDe.html): A serializer to use for converting data to the ORC format before storing it in Amazon S3.
- [OutputFormatConfiguration](https://docs.aws.amazon.com/firehose/latest/APIReference/API_OutputFormatConfiguration.html): Specifies the serializer that you want Firehose to use to convert the format of your data before it writes it to Amazon S3.
- [ParquetSerDe](https://docs.aws.amazon.com/firehose/latest/APIReference/API_ParquetSerDe.html): A serializer to use for converting data to the Parquet format before storing it in Amazon S3.
- [PartitionField](https://docs.aws.amazon.com/firehose/latest/APIReference/API_PartitionField.html): Represents a single field in a PartitionSpec.
- [PartitionSpec](https://docs.aws.amazon.com/firehose/latest/APIReference/API_PartitionSpec.html): Represents how to produce partition data for a table.
- [ProcessingConfiguration](https://docs.aws.amazon.com/firehose/latest/APIReference/API_ProcessingConfiguration.html): Describes a data processing configuration.
- [Processor](https://docs.aws.amazon.com/firehose/latest/APIReference/API_Processor.html): Describes a data processor.
- [ProcessorParameter](https://docs.aws.amazon.com/firehose/latest/APIReference/API_ProcessorParameter.html): Describes the processor parameter.
- [PutRecordBatchResponseEntry](https://docs.aws.amazon.com/firehose/latest/APIReference/API_PutRecordBatchResponseEntry.html): Contains the result for an individual record from a request.
- [Record](https://docs.aws.amazon.com/firehose/latest/APIReference/API_Record.html): The unit of data in a Firehose stream.
- [RedshiftDestinationConfiguration](https://docs.aws.amazon.com/firehose/latest/APIReference/API_RedshiftDestinationConfiguration.html): Describes the configuration of a destination in Amazon Redshift.
- [RedshiftDestinationDescription](https://docs.aws.amazon.com/firehose/latest/APIReference/API_RedshiftDestinationDescription.html): Describes a destination in Amazon Redshift.
- [RedshiftDestinationUpdate](https://docs.aws.amazon.com/firehose/latest/APIReference/API_RedshiftDestinationUpdate.html): Describes an update for a destination in Amazon Redshift.
- [RedshiftRetryOptions](https://docs.aws.amazon.com/firehose/latest/APIReference/API_RedshiftRetryOptions.html): Configures retry behavior in case Firehose is unable to deliver documents to Amazon Redshift.
- [RetryOptions](https://docs.aws.amazon.com/firehose/latest/APIReference/API_RetryOptions.html): The retry behavior in case Firehose is unable to deliver data to a destination.
- [S3DestinationConfiguration](https://docs.aws.amazon.com/firehose/latest/APIReference/API_S3DestinationConfiguration.html): Describes the configuration of a destination in Amazon S3.
- [S3DestinationDescription](https://docs.aws.amazon.com/firehose/latest/APIReference/API_S3DestinationDescription.html): Describes a destination in Amazon S3.
- [S3DestinationUpdate](https://docs.aws.amazon.com/firehose/latest/APIReference/API_S3DestinationUpdate.html): Describes an update for a destination in Amazon S3.
- [SchemaConfiguration](https://docs.aws.amazon.com/firehose/latest/APIReference/API_SchemaConfiguration.html): Specifies the schema to which you want Firehose to configure your data before it writes it to Amazon S3.
- [SchemaEvolutionConfiguration](https://docs.aws.amazon.com/firehose/latest/APIReference/API_SchemaEvolutionConfiguration.html): The configuration to enable schema evolution.
- [SecretsManagerConfiguration](https://docs.aws.amazon.com/firehose/latest/APIReference/API_SecretsManagerConfiguration.html): The structure that defines how Firehose accesses the secret.
- [Serializer](https://docs.aws.amazon.com/firehose/latest/APIReference/API_Serializer.html): The serializer that you want Firehose to use to convert data to the target format before writing it to Amazon S3.
- [SnowflakeBufferingHints](https://docs.aws.amazon.com/firehose/latest/APIReference/API_SnowflakeBufferingHints.html): Describes the buffering to perform before delivering data to the Snowflake destination.
- [SnowflakeDestinationConfiguration](https://docs.aws.amazon.com/firehose/latest/APIReference/API_SnowflakeDestinationConfiguration.html): Configure Snowflake destination
- [SnowflakeDestinationDescription](https://docs.aws.amazon.com/firehose/latest/APIReference/API_SnowflakeDestinationDescription.html): Optional Snowflake destination description
- [SnowflakeDestinationUpdate](https://docs.aws.amazon.com/firehose/latest/APIReference/API_SnowflakeDestinationUpdate.html): Update to configuration settings
- [SnowflakeRetryOptions](https://docs.aws.amazon.com/firehose/latest/APIReference/API_SnowflakeRetryOptions.html): Specify how long Firehose retries sending data to the New Relic HTTP endpoint.
- [SnowflakeRoleConfiguration](https://docs.aws.amazon.com/firehose/latest/APIReference/API_SnowflakeRoleConfiguration.html): Optionally configure a Snowflake role.
- [SnowflakeVpcConfiguration](https://docs.aws.amazon.com/firehose/latest/APIReference/API_SnowflakeVpcConfiguration.html): Configure a Snowflake VPC
- [SourceDescription](https://docs.aws.amazon.com/firehose/latest/APIReference/API_SourceDescription.html): Details about a Kinesis data stream used as the source for a Firehose stream.
- [SplunkBufferingHints](https://docs.aws.amazon.com/firehose/latest/APIReference/API_SplunkBufferingHints.html): The buffering options.
- [SplunkDestinationConfiguration](https://docs.aws.amazon.com/firehose/latest/APIReference/API_SplunkDestinationConfiguration.html): Describes the configuration of a destination in Splunk.
- [SplunkDestinationDescription](https://docs.aws.amazon.com/firehose/latest/APIReference/API_SplunkDestinationDescription.html): Describes a destination in Splunk.
- [SplunkDestinationUpdate](https://docs.aws.amazon.com/firehose/latest/APIReference/API_SplunkDestinationUpdate.html): Describes an update for a destination in Splunk.
- [SplunkRetryOptions](https://docs.aws.amazon.com/firehose/latest/APIReference/API_SplunkRetryOptions.html): Configures retry behavior in case Firehose is unable to deliver documents to Splunk, or if it doesn't receive an acknowledgment from Splunk.
- [TableCreationConfiguration](https://docs.aws.amazon.com/firehose/latest/APIReference/API_TableCreationConfiguration.html): The configuration to enable automatic table creation.
- [Tag](https://docs.aws.amazon.com/firehose/latest/APIReference/API_Tag.html): Metadata that you can assign to a Firehose stream, consisting of a key-value pair.
- [VpcConfiguration](https://docs.aws.amazon.com/firehose/latest/APIReference/API_VpcConfiguration.html): The details of the VPC of the Amazon OpenSearch or Amazon OpenSearch Serverless destination.
- [VpcConfigurationDescription](https://docs.aws.amazon.com/firehose/latest/APIReference/API_VpcConfigurationDescription.html): The details of the VPC of the Amazon OpenSearch Service destination.
