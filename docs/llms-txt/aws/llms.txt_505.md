# Source: https://docs.aws.amazon.com/kinesis/latest/APIReference/llms.txt

# Amazon Kinesis Data Streams Service API Reference

> Amazon Kinesis Data Streams is a managed service that scales elastically for real-time processing of streaming big data.

- [Welcome](https://docs.aws.amazon.com/kinesis/latest/APIReference/Welcome.html)
- [Common Errors](https://docs.aws.amazon.com/kinesis/latest/APIReference/CommonErrors.html)

## [Actions](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_Operations.html)

- [AddTagsToStream](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_AddTagsToStream.html): Adds or updates tags for the specified Kinesis data stream.
- [CreateStream](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_CreateStream.html): Creates a Kinesis data stream.
- [DecreaseStreamRetentionPeriod](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_DecreaseStreamRetentionPeriod.html): Decreases the Kinesis data stream's retention period, which is the length of time data records are accessible after they are added to the stream.
- [DeleteResourcePolicy](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_DeleteResourcePolicy.html): Delete a policy for the specified data stream or consumer.
- [DeleteStream](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_DeleteStream.html): Deletes a Kinesis data stream and all its shards and data.
- [DeregisterStreamConsumer](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_DeregisterStreamConsumer.html): To deregister a consumer, provide its ARN.
- [DescribeAccountSettings](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_DescribeAccountSettings.html): Describes the account-level settings for Amazon Kinesis Data Streams.
- [DescribeLimits](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_DescribeLimits.html): Describes the shard limits and usage for the account.
- [DescribeStream](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_DescribeStream.html): Describes the specified Kinesis data stream.
- [DescribeStreamConsumer](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_DescribeStreamConsumer.html): To get the description of a registered consumer, provide the ARN of the consumer.
- [DescribeStreamSummary](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_DescribeStreamSummary.html): Provides a summarized description of the specified Kinesis data stream without the shard list.
- [DisableEnhancedMonitoring](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_DisableEnhancedMonitoring.html): Disables enhanced monitoring.
- [EnableEnhancedMonitoring](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_EnableEnhancedMonitoring.html): Enables enhanced Kinesis data stream monitoring for shard-level metrics.
- [GetRecords](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_GetRecords.html): Gets data records from a Kinesis data stream's shard.
- [GetResourcePolicy](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_GetResourcePolicy.html): Returns a policy attached to the specified data stream or consumer.
- [GetShardIterator](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_GetShardIterator.html): Gets an Amazon Kinesis shard iterator.
- [IncreaseStreamRetentionPeriod](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_IncreaseStreamRetentionPeriod.html): Increases the Kinesis data stream's retention period, which is the length of time data records are accessible after they are added to the stream.
- [ListShards](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_ListShards.html): Lists the shards in a stream and provides information about each shard.
- [ListStreamConsumers](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_ListStreamConsumers.html): Lists the consumers registered to receive data from a stream using enhanced fan-out, and provides information about each consumer.
- [ListStreams](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_ListStreams.html): Lists your Kinesis data streams.
- [ListTagsForResource](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_ListTagsForResource.html): List all tags added to the specified Kinesis resource.
- [ListTagsForStream](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_ListTagsForStream.html): Lists the tags for the specified Kinesis data stream.
- [MergeShards](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_MergeShards.html): Merges two adjacent shards in a Kinesis data stream and combines them into a single shard to reduce the stream's capacity to ingest and transport data.
- [PutRecord](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_PutRecord.html): Writes a single data record into an Amazon Kinesis data stream.
- [PutRecords](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_PutRecords.html): Writes multiple data records into a Kinesis data stream in a single call (also referred to as a PutRecords request).
- [PutResourcePolicy](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_PutResourcePolicy.html): Attaches a resource-based policy to a data stream or registered consumer.
- [RegisterStreamConsumer](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_RegisterStreamConsumer.html): Registers a consumer with a Kinesis data stream.
- [RemoveTagsFromStream](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_RemoveTagsFromStream.html): Removes tags from the specified Kinesis data stream.
- [SplitShard](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_SplitShard.html): Splits a shard into two new shards in the Kinesis data stream, to increase the stream's capacity to ingest and transport data.
- [StartStreamEncryption](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_StartStreamEncryption.html): Enables or updates server-side encryption using an AWS KMS key for a specified stream.
- [StopStreamEncryption](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_StopStreamEncryption.html): Disables server-side encryption for a specified stream.
- [SubscribeToShard](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_SubscribeToShard.html): This operation establishes an HTTP/2 connection between the consumer you specify in the ConsumerARN parameter and the shard you specify in the ShardId parameter.
- [TagResource](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_TagResource.html): Adds or updates tags for the specified Kinesis resource.
- [UntagResource](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_UntagResource.html): Removes tags from the specified Kinesis resource.
- [UpdateAccountSettings](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_UpdateAccountSettings.html): Updates the account-level settings for Amazon Kinesis Data Streams.
- [UpdateMaxRecordSize](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_UpdateMaxRecordSize.html): This allows you to update the MaxRecordSize of a single record that you can write to, and read from a stream.
- [UpdateShardCount](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_UpdateShardCount.html): Updates the shard count of the specified stream to the specified number of shards.
- [UpdateStreamMode](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_UpdateStreamMode.html): Updates the capacity mode of the data stream.
- [UpdateStreamWarmThroughput](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_UpdateStreamWarmThroughput.html): Updates the warm throughput configuration for the specified Amazon Kinesis Data Streams on-demand data stream.


## [Data Types](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_Types.html)

- [ChildShard](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_ChildShard.html): Output parameter of the GetRecords API.
- [Consumer](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_Consumer.html): An object that represents the details of the consumer you registered.
- [ConsumerDescription](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_ConsumerDescription.html): An object that represents the details of a registered consumer.
- [EnhancedMetrics](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_EnhancedMetrics.html): Represents enhanced metrics types.
- [HashKeyRange](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_HashKeyRange.html): The range of possible hash key values for the shard, which is a set of ordered contiguous positive integers.
- [MinimumThroughputBillingCommitmentInput](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_MinimumThroughputBillingCommitmentInput.html): Represents the request parameters for configuring minimum throughput billing commitment.
- [MinimumThroughputBillingCommitmentOutput](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_MinimumThroughputBillingCommitmentOutput.html): Represents the current status of minimum throughput billing commitment for an account.
- [PutRecordsRequestEntry](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_PutRecordsRequestEntry.html): Represents the output for PutRecords.
- [PutRecordsResultEntry](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_PutRecordsResultEntry.html): Represents the result of an individual record from a PutRecords request.
- [Record](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_Record.html): The unit of data of the Kinesis data stream, which is composed of a sequence number, a partition key, and a data blob.
- [SequenceNumberRange](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_SequenceNumberRange.html): The range of possible sequence numbers for the shard.
- [Shard](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_Shard.html): A uniquely identified group of data records in a Kinesis data stream.
- [ShardFilter](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_ShardFilter.html): The request parameter used to filter out the response of the ListShards API.
- [StartingPosition](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_StartingPosition.html): The starting position in the data stream from which to start streaming.
- [StreamDescription](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_StreamDescription.html): Represents the output for .
- [StreamDescriptionSummary](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_StreamDescriptionSummary.html): Represents the output for
- [StreamModeDetails](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_StreamModeDetails.html): Specifies the capacity mode to which you want to set your data stream.
- [StreamSummary](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_StreamSummary.html): The summary of a stream.
- [SubscribeToShardEvent](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_SubscribeToShardEvent.html): After you call , Kinesis Data Streams sends events of this type over an HTTP/2 connection to your consumer.
- [SubscribeToShardEventStream](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_SubscribeToShardEventStream.html): This is a tagged union for all of the types of events an enhanced fan-out consumer can receive over HTTP/2 after a call to .
- [Tag](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_Tag.html): Metadata assigned to the stream or consumer, consisting of a key-value pair.
- [WarmThroughputObject](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_WarmThroughputObject.html): Represents the warm throughput configuration on the stream.
