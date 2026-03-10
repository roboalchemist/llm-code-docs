# Source: https://docs.aws.amazon.com/eventbridge/latest/pipes-reference/llms.txt

# Amazon EventBridge Pipes APIReference

> Amazon EventBridge Pipes connects event sources to targets. Pipes reduces the need for specialized knowledge and integration code when developing event driven architectures. This helps ensures consistency across your companyâs applications. With Pipes, the target can be any available EventBridge target. To set up a pipe, you select the event source, add optional event filtering, define optional enrichment, and select the target for the event data.

- [Welcome](https://docs.aws.amazon.com/eventbridge/latest/pipes-reference/Welcome.html)
- [Common Parameters](https://docs.aws.amazon.com/eventbridge/latest/pipes-reference/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/eventbridge/latest/pipes-reference/CommonErrors.html)

## [Actions](https://docs.aws.amazon.com/eventbridge/latest/pipes-reference/API_Operations.html)

- [CreatePipe](https://docs.aws.amazon.com/eventbridge/latest/pipes-reference/API_CreatePipe.html): Create a pipe.
- [DeletePipe](https://docs.aws.amazon.com/eventbridge/latest/pipes-reference/API_DeletePipe.html): Delete an existing pipe.
- [DescribePipe](https://docs.aws.amazon.com/eventbridge/latest/pipes-reference/API_DescribePipe.html): Get the information about an existing pipe.
- [ListPipes](https://docs.aws.amazon.com/eventbridge/latest/pipes-reference/API_ListPipes.html): Get the pipes associated with this account.
- [ListTagsForResource](https://docs.aws.amazon.com/eventbridge/latest/pipes-reference/API_ListTagsForResource.html): Displays the tags associated with a pipe.
- [StartPipe](https://docs.aws.amazon.com/eventbridge/latest/pipes-reference/API_StartPipe.html): Start an existing pipe.
- [StopPipe](https://docs.aws.amazon.com/eventbridge/latest/pipes-reference/API_StopPipe.html): Stop an existing pipe.
- [TagResource](https://docs.aws.amazon.com/eventbridge/latest/pipes-reference/API_TagResource.html): Assigns one or more tags (key-value pairs) to the specified pipe.
- [UntagResource](https://docs.aws.amazon.com/eventbridge/latest/pipes-reference/API_UntagResource.html): Removes one or more tags from the specified pipes.
- [UpdatePipe](https://docs.aws.amazon.com/eventbridge/latest/pipes-reference/API_UpdatePipe.html): Update an existing pipe.


## [Data Types](https://docs.aws.amazon.com/eventbridge/latest/pipes-reference/API_Types.html)

- [AwsVpcConfiguration](https://docs.aws.amazon.com/eventbridge/latest/pipes-reference/API_AwsVpcConfiguration.html): This structure specifies the VPC subnets and security groups for the task, and whether a public IP address is to be used.
- [BatchArrayProperties](https://docs.aws.amazon.com/eventbridge/latest/pipes-reference/API_BatchArrayProperties.html): The array properties for the submitted job, such as the size of the array.
- [BatchContainerOverrides](https://docs.aws.amazon.com/eventbridge/latest/pipes-reference/API_BatchContainerOverrides.html): The overrides that are sent to a container.
- [BatchEnvironmentVariable](https://docs.aws.amazon.com/eventbridge/latest/pipes-reference/API_BatchEnvironmentVariable.html): The environment variables to send to the container.
- [BatchJobDependency](https://docs.aws.amazon.com/eventbridge/latest/pipes-reference/API_BatchJobDependency.html): An object that represents an AWS Batch job dependency.
- [BatchResourceRequirement](https://docs.aws.amazon.com/eventbridge/latest/pipes-reference/API_BatchResourceRequirement.html): The type and amount of a resource to assign to a container.
- [BatchRetryStrategy](https://docs.aws.amazon.com/eventbridge/latest/pipes-reference/API_BatchRetryStrategy.html): The retry strategy that's associated with a job.
- [CapacityProviderStrategyItem](https://docs.aws.amazon.com/eventbridge/latest/pipes-reference/API_CapacityProviderStrategyItem.html): The details of a capacity provider strategy.
- [CloudwatchLogsLogDestination](https://docs.aws.amazon.com/eventbridge/latest/pipes-reference/API_CloudwatchLogsLogDestination.html): The Amazon CloudWatch Logs logging configuration settings for the pipe.
- [CloudwatchLogsLogDestinationParameters](https://docs.aws.amazon.com/eventbridge/latest/pipes-reference/API_CloudwatchLogsLogDestinationParameters.html): The Amazon CloudWatch Logs logging configuration settings for the pipe.
- [DeadLetterConfig](https://docs.aws.amazon.com/eventbridge/latest/pipes-reference/API_DeadLetterConfig.html): A DeadLetterConfig object that contains information about a dead-letter queue configuration.
- [DimensionMapping](https://docs.aws.amazon.com/eventbridge/latest/pipes-reference/API_DimensionMapping.html): Maps source data to a dimension in the target Timestream for LiveAnalytics table.
- [EcsContainerOverride](https://docs.aws.amazon.com/eventbridge/latest/pipes-reference/API_EcsContainerOverride.html): The overrides that are sent to a container.
- [EcsEnvironmentFile](https://docs.aws.amazon.com/eventbridge/latest/pipes-reference/API_EcsEnvironmentFile.html): A list of files containing the environment variables to pass to a container.
- [EcsEnvironmentVariable](https://docs.aws.amazon.com/eventbridge/latest/pipes-reference/API_EcsEnvironmentVariable.html): The environment variables to send to the container.
- [EcsEphemeralStorage](https://docs.aws.amazon.com/eventbridge/latest/pipes-reference/API_EcsEphemeralStorage.html): The amount of ephemeral storage to allocate for the task.
- [EcsInferenceAcceleratorOverride](https://docs.aws.amazon.com/eventbridge/latest/pipes-reference/API_EcsInferenceAcceleratorOverride.html): Details on an Elastic Inference accelerator task override.
- [EcsResourceRequirement](https://docs.aws.amazon.com/eventbridge/latest/pipes-reference/API_EcsResourceRequirement.html): The type and amount of a resource to assign to a container.
- [EcsTaskOverride](https://docs.aws.amazon.com/eventbridge/latest/pipes-reference/API_EcsTaskOverride.html): The overrides that are associated with a task.
- [Filter](https://docs.aws.amazon.com/eventbridge/latest/pipes-reference/API_Filter.html): Filter events using an event pattern.
- [FilterCriteria](https://docs.aws.amazon.com/eventbridge/latest/pipes-reference/API_FilterCriteria.html): The collection of event patterns used to filter events.
- [FirehoseLogDestination](https://docs.aws.amazon.com/eventbridge/latest/pipes-reference/API_FirehoseLogDestination.html): The Amazon Data Firehose logging configuration settings for the pipe.
- [FirehoseLogDestinationParameters](https://docs.aws.amazon.com/eventbridge/latest/pipes-reference/API_FirehoseLogDestinationParameters.html): The Amazon Data Firehose logging configuration settings for the pipe.
- [MQBrokerAccessCredentials](https://docs.aws.amazon.com/eventbridge/latest/pipes-reference/API_MQBrokerAccessCredentials.html): The AWS Secrets Manager secret that stores your broker credentials.
- [MSKAccessCredentials](https://docs.aws.amazon.com/eventbridge/latest/pipes-reference/API_MSKAccessCredentials.html): The AWS Secrets Manager secret that stores your stream credentials.
- [MultiMeasureAttributeMapping](https://docs.aws.amazon.com/eventbridge/latest/pipes-reference/API_MultiMeasureAttributeMapping.html): A mapping of a source event data field to a measure in a Timestream for LiveAnalytics record.
- [MultiMeasureMapping](https://docs.aws.amazon.com/eventbridge/latest/pipes-reference/API_MultiMeasureMapping.html): Maps multiple measures from the source event to the same Timestream for LiveAnalytics record.
- [NetworkConfiguration](https://docs.aws.amazon.com/eventbridge/latest/pipes-reference/API_NetworkConfiguration.html): This structure specifies the network configuration for an Amazon ECS task.
- [Pipe](https://docs.aws.amazon.com/eventbridge/latest/pipes-reference/API_Pipe.html): An object that represents a pipe.
- [PipeEnrichmentHttpParameters](https://docs.aws.amazon.com/eventbridge/latest/pipes-reference/API_PipeEnrichmentHttpParameters.html): These are custom parameter to be used when the target is an API Gateway REST APIs or EventBridge ApiDestinations.
- [PipeEnrichmentParameters](https://docs.aws.amazon.com/eventbridge/latest/pipes-reference/API_PipeEnrichmentParameters.html): The parameters required to set up enrichment on your pipe.
- [PipeLogConfiguration](https://docs.aws.amazon.com/eventbridge/latest/pipes-reference/API_PipeLogConfiguration.html): The logging configuration settings for the pipe.
- [PipeLogConfigurationParameters](https://docs.aws.amazon.com/eventbridge/latest/pipes-reference/API_PipeLogConfigurationParameters.html): Specifies the logging configuration settings for the pipe.
- [PipeSourceActiveMQBrokerParameters](https://docs.aws.amazon.com/eventbridge/latest/pipes-reference/API_PipeSourceActiveMQBrokerParameters.html): The parameters for using an Active MQ broker as a source.
- [PipeSourceDynamoDBStreamParameters](https://docs.aws.amazon.com/eventbridge/latest/pipes-reference/API_PipeSourceDynamoDBStreamParameters.html): The parameters for using a DynamoDB stream as a source.
- [PipeSourceKinesisStreamParameters](https://docs.aws.amazon.com/eventbridge/latest/pipes-reference/API_PipeSourceKinesisStreamParameters.html): The parameters for using a Kinesis stream as a source.
- [PipeSourceManagedStreamingKafkaParameters](https://docs.aws.amazon.com/eventbridge/latest/pipes-reference/API_PipeSourceManagedStreamingKafkaParameters.html): The parameters for using an MSK stream as a source.
- [PipeSourceParameters](https://docs.aws.amazon.com/eventbridge/latest/pipes-reference/API_PipeSourceParameters.html): The parameters required to set up a source for your pipe.
- [PipeSourceRabbitMQBrokerParameters](https://docs.aws.amazon.com/eventbridge/latest/pipes-reference/API_PipeSourceRabbitMQBrokerParameters.html): The parameters for using a Rabbit MQ broker as a source.
- [PipeSourceSelfManagedKafkaParameters](https://docs.aws.amazon.com/eventbridge/latest/pipes-reference/API_PipeSourceSelfManagedKafkaParameters.html): The parameters for using a self-managed Apache Kafka stream as a source.
- [PipeSourceSqsQueueParameters](https://docs.aws.amazon.com/eventbridge/latest/pipes-reference/API_PipeSourceSqsQueueParameters.html): The parameters for using a Amazon SQS stream as a source.
- [PipeTargetBatchJobParameters](https://docs.aws.amazon.com/eventbridge/latest/pipes-reference/API_PipeTargetBatchJobParameters.html): The parameters for using an AWS Batch job as a target.
- [PipeTargetCloudWatchLogsParameters](https://docs.aws.amazon.com/eventbridge/latest/pipes-reference/API_PipeTargetCloudWatchLogsParameters.html): The parameters for using an CloudWatch Logs log stream as a target.
- [PipeTargetEcsTaskParameters](https://docs.aws.amazon.com/eventbridge/latest/pipes-reference/API_PipeTargetEcsTaskParameters.html): The parameters for using an Amazon ECS task as a target.
- [PipeTargetEventBridgeEventBusParameters](https://docs.aws.amazon.com/eventbridge/latest/pipes-reference/API_PipeTargetEventBridgeEventBusParameters.html): The parameters for using an EventBridge event bus as a target.
- [PipeTargetHttpParameters](https://docs.aws.amazon.com/eventbridge/latest/pipes-reference/API_PipeTargetHttpParameters.html): These are custom parameter to be used when the target is an API Gateway REST APIs or EventBridge ApiDestinations.
- [PipeTargetKinesisStreamParameters](https://docs.aws.amazon.com/eventbridge/latest/pipes-reference/API_PipeTargetKinesisStreamParameters.html): The parameters for using a Kinesis stream as a target.
- [PipeTargetLambdaFunctionParameters](https://docs.aws.amazon.com/eventbridge/latest/pipes-reference/API_PipeTargetLambdaFunctionParameters.html): The parameters for using a Lambda function as a target.
- [PipeTargetParameters](https://docs.aws.amazon.com/eventbridge/latest/pipes-reference/API_PipeTargetParameters.html): The parameters required to set up a target for your pipe.
- [PipeTargetRedshiftDataParameters](https://docs.aws.amazon.com/eventbridge/latest/pipes-reference/API_PipeTargetRedshiftDataParameters.html): These are custom parameters to be used when the target is a Amazon Redshift cluster to invoke the Amazon Redshift Data API BatchExecuteStatement.
- [PipeTargetSageMakerPipelineParameters](https://docs.aws.amazon.com/eventbridge/latest/pipes-reference/API_PipeTargetSageMakerPipelineParameters.html): The parameters for using a SageMaker AI pipeline as a target.
- [PipeTargetSqsQueueParameters](https://docs.aws.amazon.com/eventbridge/latest/pipes-reference/API_PipeTargetSqsQueueParameters.html): The parameters for using a Amazon SQS stream as a target.
- [PipeTargetStateMachineParameters](https://docs.aws.amazon.com/eventbridge/latest/pipes-reference/API_PipeTargetStateMachineParameters.html): The parameters for using a Step Functions state machine as a target.
- [PipeTargetTimestreamParameters](https://docs.aws.amazon.com/eventbridge/latest/pipes-reference/API_PipeTargetTimestreamParameters.html): The parameters for using a Timestream for LiveAnalytics table as a target.
- [PlacementConstraint](https://docs.aws.amazon.com/eventbridge/latest/pipes-reference/API_PlacementConstraint.html): An object representing a constraint on task placement.
- [PlacementStrategy](https://docs.aws.amazon.com/eventbridge/latest/pipes-reference/API_PlacementStrategy.html): The task placement strategy for a task or service.
- [S3LogDestination](https://docs.aws.amazon.com/eventbridge/latest/pipes-reference/API_S3LogDestination.html): The Amazon S3 logging configuration settings for the pipe.
- [S3LogDestinationParameters](https://docs.aws.amazon.com/eventbridge/latest/pipes-reference/API_S3LogDestinationParameters.html): The Amazon S3 logging configuration settings for the pipe.
- [SageMakerPipelineParameter](https://docs.aws.amazon.com/eventbridge/latest/pipes-reference/API_SageMakerPipelineParameter.html): Name/Value pair of a parameter to start execution of a SageMaker AI Model Building Pipeline.
- [SelfManagedKafkaAccessConfigurationCredentials](https://docs.aws.amazon.com/eventbridge/latest/pipes-reference/API_SelfManagedKafkaAccessConfigurationCredentials.html): The AWS Secrets Manager secret that stores your stream credentials.
- [SelfManagedKafkaAccessConfigurationVpc](https://docs.aws.amazon.com/eventbridge/latest/pipes-reference/API_SelfManagedKafkaAccessConfigurationVpc.html): This structure specifies the VPC subnets and security groups for the stream, and whether a public IP address is to be used.
- [SingleMeasureMapping](https://docs.aws.amazon.com/eventbridge/latest/pipes-reference/API_SingleMeasureMapping.html): Maps a single source data field to a single record in the specified Timestream for LiveAnalytics table.
- [Tag](https://docs.aws.amazon.com/eventbridge/latest/pipes-reference/API_Tag.html): A key-value pair associated with an AWS resource.
- [UpdatePipeSourceActiveMQBrokerParameters](https://docs.aws.amazon.com/eventbridge/latest/pipes-reference/API_UpdatePipeSourceActiveMQBrokerParameters.html): The parameters for using an Active MQ broker as a source.
- [UpdatePipeSourceDynamoDBStreamParameters](https://docs.aws.amazon.com/eventbridge/latest/pipes-reference/API_UpdatePipeSourceDynamoDBStreamParameters.html): The parameters for using a DynamoDB stream as a source.
- [UpdatePipeSourceKinesisStreamParameters](https://docs.aws.amazon.com/eventbridge/latest/pipes-reference/API_UpdatePipeSourceKinesisStreamParameters.html): The parameters for using a Kinesis stream as a source.
- [UpdatePipeSourceManagedStreamingKafkaParameters](https://docs.aws.amazon.com/eventbridge/latest/pipes-reference/API_UpdatePipeSourceManagedStreamingKafkaParameters.html): The parameters for using an MSK stream as a source.
- [UpdatePipeSourceParameters](https://docs.aws.amazon.com/eventbridge/latest/pipes-reference/API_UpdatePipeSourceParameters.html): The parameters required to set up a source for your pipe.
- [UpdatePipeSourceRabbitMQBrokerParameters](https://docs.aws.amazon.com/eventbridge/latest/pipes-reference/API_UpdatePipeSourceRabbitMQBrokerParameters.html): The parameters for using a Rabbit MQ broker as a source.
- [UpdatePipeSourceSelfManagedKafkaParameters](https://docs.aws.amazon.com/eventbridge/latest/pipes-reference/API_UpdatePipeSourceSelfManagedKafkaParameters.html): The parameters for using a self-managed Apache Kafka stream as a source.
- [UpdatePipeSourceSqsQueueParameters](https://docs.aws.amazon.com/eventbridge/latest/pipes-reference/API_UpdatePipeSourceSqsQueueParameters.html): The parameters for using a Amazon SQS stream as a source.
- [ValidationExceptionField](https://docs.aws.amazon.com/eventbridge/latest/pipes-reference/API_ValidationExceptionField.html): Indicates that an error has occurred while performing a validate operation.
