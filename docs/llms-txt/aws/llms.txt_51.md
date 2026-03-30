# Source: https://docs.aws.amazon.com/MSKC/latest/mskc/llms.txt

# Amazon MSK Connect API Reference

- [Welcome](https://docs.aws.amazon.com/MSKC/latest/mskc/Welcome.html)
- [Common Parameters](https://docs.aws.amazon.com/MSKC/latest/mskc/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/MSKC/latest/mskc/CommonErrors.html)

## [Actions](https://docs.aws.amazon.com/MSKC/latest/mskc/API_Operations.html)

- [CreateConnector](https://docs.aws.amazon.com/MSKC/latest/mskc/API_CreateConnector.html): Creates a connector using the specified properties.
- [CreateCustomPlugin](https://docs.aws.amazon.com/MSKC/latest/mskc/API_CreateCustomPlugin.html): Creates a custom plugin using the specified properties.
- [CreateWorkerConfiguration](https://docs.aws.amazon.com/MSKC/latest/mskc/API_CreateWorkerConfiguration.html): Creates a worker configuration using the specified properties.
- [DeleteConnector](https://docs.aws.amazon.com/MSKC/latest/mskc/API_DeleteConnector.html): Deletes the specified connector.
- [DeleteCustomPlugin](https://docs.aws.amazon.com/MSKC/latest/mskc/API_DeleteCustomPlugin.html): Deletes a custom plugin.
- [DeleteWorkerConfiguration](https://docs.aws.amazon.com/MSKC/latest/mskc/API_DeleteWorkerConfiguration.html): Deletes the specified worker configuration.
- [DescribeConnector](https://docs.aws.amazon.com/MSKC/latest/mskc/API_DescribeConnector.html): Returns summary information about the connector.
- [DescribeConnectorOperation](https://docs.aws.amazon.com/MSKC/latest/mskc/API_DescribeConnectorOperation.html): Returns information about the specified connector's operations.
- [DescribeCustomPlugin](https://docs.aws.amazon.com/MSKC/latest/mskc/API_DescribeCustomPlugin.html): A summary description of the custom plugin.
- [DescribeWorkerConfiguration](https://docs.aws.amazon.com/MSKC/latest/mskc/API_DescribeWorkerConfiguration.html): Returns information about a worker configuration.
- [ListConnectorOperations](https://docs.aws.amazon.com/MSKC/latest/mskc/API_ListConnectorOperations.html): Lists information about a connector's operation(s).
- [ListConnectors](https://docs.aws.amazon.com/MSKC/latest/mskc/API_ListConnectors.html): Returns a list of all the connectors in this account and Region.
- [ListCustomPlugins](https://docs.aws.amazon.com/MSKC/latest/mskc/API_ListCustomPlugins.html): Returns a list of all of the custom plugins in this account and Region.
- [ListTagsForResource](https://docs.aws.amazon.com/MSKC/latest/mskc/API_ListTagsForResource.html): Lists all the tags attached to the specified resource.
- [ListWorkerConfigurations](https://docs.aws.amazon.com/MSKC/latest/mskc/API_ListWorkerConfigurations.html): Returns a list of all of the worker configurations in this account and Region.
- [TagResource](https://docs.aws.amazon.com/MSKC/latest/mskc/API_TagResource.html): Attaches tags to the specified resource.
- [UntagResource](https://docs.aws.amazon.com/MSKC/latest/mskc/API_UntagResource.html): Removes tags from the specified resource.
- [UpdateConnector](https://docs.aws.amazon.com/MSKC/latest/mskc/API_UpdateConnector.html): Updates the specified connector.


## [Data Types](https://docs.aws.amazon.com/MSKC/latest/mskc/API_Types.html)

- [ApacheKafkaCluster](https://docs.aws.amazon.com/MSKC/latest/mskc/API_ApacheKafkaCluster.html): The details of the Apache Kafka cluster to which the connector is connected.
- [ApacheKafkaClusterDescription](https://docs.aws.amazon.com/MSKC/latest/mskc/API_ApacheKafkaClusterDescription.html): The description of the Apache Kafka cluster to which the connector is connected.
- [AutoScaling](https://docs.aws.amazon.com/MSKC/latest/mskc/API_AutoScaling.html): Specifies how the connector scales.
- [AutoScalingDescription](https://docs.aws.amazon.com/MSKC/latest/mskc/API_AutoScalingDescription.html): Information about the auto scaling parameters for the connector.
- [AutoScalingUpdate](https://docs.aws.amazon.com/MSKC/latest/mskc/API_AutoScalingUpdate.html): The updates to the auto scaling parameters for the connector.
- [Capacity](https://docs.aws.amazon.com/MSKC/latest/mskc/API_Capacity.html): Information about the capacity of the connector, whether it is auto scaled or provisioned.
- [CapacityDescription](https://docs.aws.amazon.com/MSKC/latest/mskc/API_CapacityDescription.html): A description of the connector's capacity.
- [CapacityUpdate](https://docs.aws.amazon.com/MSKC/latest/mskc/API_CapacityUpdate.html): The target capacity for the connector.
- [CloudWatchLogsLogDelivery](https://docs.aws.amazon.com/MSKC/latest/mskc/API_CloudWatchLogsLogDelivery.html): The settings for delivering connector logs to Amazon CloudWatch Logs.
- [CloudWatchLogsLogDeliveryDescription](https://docs.aws.amazon.com/MSKC/latest/mskc/API_CloudWatchLogsLogDeliveryDescription.html): A description of the log delivery settings.
- [ConnectorOperationStep](https://docs.aws.amazon.com/MSKC/latest/mskc/API_ConnectorOperationStep.html): Details of a step that is involved in a connector's operation.
- [ConnectorOperationSummary](https://docs.aws.amazon.com/MSKC/latest/mskc/API_ConnectorOperationSummary.html): Summary of a connector operation.
- [ConnectorSummary](https://docs.aws.amazon.com/MSKC/latest/mskc/API_ConnectorSummary.html): Summary of a connector.
- [CustomPlugin](https://docs.aws.amazon.com/MSKC/latest/mskc/API_CustomPlugin.html): A plugin is an AWS resource that contains the code that defines a connector's logic.
- [CustomPluginDescription](https://docs.aws.amazon.com/MSKC/latest/mskc/API_CustomPluginDescription.html): Details about a custom plugin.
- [CustomPluginFileDescription](https://docs.aws.amazon.com/MSKC/latest/mskc/API_CustomPluginFileDescription.html): Details about a custom plugin file.
- [CustomPluginLocation](https://docs.aws.amazon.com/MSKC/latest/mskc/API_CustomPluginLocation.html): Information about the location of a custom plugin.
- [CustomPluginLocationDescription](https://docs.aws.amazon.com/MSKC/latest/mskc/API_CustomPluginLocationDescription.html): Information about the location of a custom plugin.
- [CustomPluginRevisionSummary](https://docs.aws.amazon.com/MSKC/latest/mskc/API_CustomPluginRevisionSummary.html): Details about the revision of a custom plugin.
- [CustomPluginSummary](https://docs.aws.amazon.com/MSKC/latest/mskc/API_CustomPluginSummary.html): A summary of the custom plugin.
- [FirehoseLogDelivery](https://docs.aws.amazon.com/MSKC/latest/mskc/API_FirehoseLogDelivery.html): The settings for delivering logs to Amazon Kinesis Data Firehose.
- [FirehoseLogDeliveryDescription](https://docs.aws.amazon.com/MSKC/latest/mskc/API_FirehoseLogDeliveryDescription.html): A description of the settings for delivering logs to Amazon Kinesis Data Firehose.
- [KafkaCluster](https://docs.aws.amazon.com/MSKC/latest/mskc/API_KafkaCluster.html): The details of the Apache Kafka cluster to which the connector is connected.
- [KafkaClusterClientAuthentication](https://docs.aws.amazon.com/MSKC/latest/mskc/API_KafkaClusterClientAuthentication.html): The client authentication information used in order to authenticate with the Apache Kafka cluster.
- [KafkaClusterClientAuthenticationDescription](https://docs.aws.amazon.com/MSKC/latest/mskc/API_KafkaClusterClientAuthenticationDescription.html): The client authentication information used in order to authenticate with the Apache Kafka cluster.
- [KafkaClusterDescription](https://docs.aws.amazon.com/MSKC/latest/mskc/API_KafkaClusterDescription.html): Details of how to connect to the Apache Kafka cluster.
- [KafkaClusterEncryptionInTransit](https://docs.aws.amazon.com/MSKC/latest/mskc/API_KafkaClusterEncryptionInTransit.html): Details of encryption in transit to the Apache Kafka cluster.
- [KafkaClusterEncryptionInTransitDescription](https://docs.aws.amazon.com/MSKC/latest/mskc/API_KafkaClusterEncryptionInTransitDescription.html): The description of the encryption in transit to the Apache Kafka cluster.
- [LogDelivery](https://docs.aws.amazon.com/MSKC/latest/mskc/API_LogDelivery.html): Details about log delivery.
- [LogDeliveryDescription](https://docs.aws.amazon.com/MSKC/latest/mskc/API_LogDeliveryDescription.html): The description of the log delivery settings.
- [Plugin](https://docs.aws.amazon.com/MSKC/latest/mskc/API_Plugin.html): A plugin is an AWS resource that contains the code that defines your connector logic.
- [PluginDescription](https://docs.aws.amazon.com/MSKC/latest/mskc/API_PluginDescription.html): The description of the plugin.
- [ProvisionedCapacity](https://docs.aws.amazon.com/MSKC/latest/mskc/API_ProvisionedCapacity.html): Details about a connector's provisioned capacity.
- [ProvisionedCapacityDescription](https://docs.aws.amazon.com/MSKC/latest/mskc/API_ProvisionedCapacityDescription.html): The description of a connector's provisioned capacity.
- [ProvisionedCapacityUpdate](https://docs.aws.amazon.com/MSKC/latest/mskc/API_ProvisionedCapacityUpdate.html): An update to a connector's fixed capacity.
- [S3Location](https://docs.aws.amazon.com/MSKC/latest/mskc/API_S3Location.html): The location of an object in Amazon S3.
- [S3LocationDescription](https://docs.aws.amazon.com/MSKC/latest/mskc/API_S3LocationDescription.html): The description of the location of an object in Amazon S3.
- [S3LogDelivery](https://docs.aws.amazon.com/MSKC/latest/mskc/API_S3LogDelivery.html): Details about delivering logs to Amazon S3.
- [S3LogDeliveryDescription](https://docs.aws.amazon.com/MSKC/latest/mskc/API_S3LogDeliveryDescription.html): The description of the details about delivering logs to Amazon S3.
- [ScaleInPolicy](https://docs.aws.amazon.com/MSKC/latest/mskc/API_ScaleInPolicy.html): The scale-in policy for the connector.
- [ScaleInPolicyDescription](https://docs.aws.amazon.com/MSKC/latest/mskc/API_ScaleInPolicyDescription.html): The description of the scale-in policy for the connector.
- [ScaleInPolicyUpdate](https://docs.aws.amazon.com/MSKC/latest/mskc/API_ScaleInPolicyUpdate.html): An update to the connector's scale-in policy.
- [ScaleOutPolicy](https://docs.aws.amazon.com/MSKC/latest/mskc/API_ScaleOutPolicy.html): The scale-out policy for the connector.
- [ScaleOutPolicyDescription](https://docs.aws.amazon.com/MSKC/latest/mskc/API_ScaleOutPolicyDescription.html): The description of the scale-out policy for the connector.
- [ScaleOutPolicyUpdate](https://docs.aws.amazon.com/MSKC/latest/mskc/API_ScaleOutPolicyUpdate.html): An update to the connector's scale-out policy.
- [StateDescription](https://docs.aws.amazon.com/MSKC/latest/mskc/API_StateDescription.html): Details about the state of a resource.
- [Vpc](https://docs.aws.amazon.com/MSKC/latest/mskc/API_Vpc.html): Information about the VPC in which the connector resides.
- [VpcDescription](https://docs.aws.amazon.com/MSKC/latest/mskc/API_VpcDescription.html): The description of the VPC in which the connector resides.
- [WorkerConfiguration](https://docs.aws.amazon.com/MSKC/latest/mskc/API_WorkerConfiguration.html): The configuration of the workers, which are the processes that run the connector logic.
- [WorkerConfigurationDescription](https://docs.aws.amazon.com/MSKC/latest/mskc/API_WorkerConfigurationDescription.html): The description of the worker configuration.
- [WorkerConfigurationRevisionDescription](https://docs.aws.amazon.com/MSKC/latest/mskc/API_WorkerConfigurationRevisionDescription.html): The description of the worker configuration revision.
- [WorkerConfigurationRevisionSummary](https://docs.aws.amazon.com/MSKC/latest/mskc/API_WorkerConfigurationRevisionSummary.html): The summary of a worker configuration revision.
- [WorkerConfigurationSummary](https://docs.aws.amazon.com/MSKC/latest/mskc/API_WorkerConfigurationSummary.html): The summary of a worker configuration.
- [WorkerLogDelivery](https://docs.aws.amazon.com/MSKC/latest/mskc/API_WorkerLogDelivery.html): Workers can send worker logs to different destination types.
- [WorkerLogDeliveryDescription](https://docs.aws.amazon.com/MSKC/latest/mskc/API_WorkerLogDeliveryDescription.html): Workers can send worker logs to different destination types.
- [WorkerSetting](https://docs.aws.amazon.com/MSKC/latest/mskc/API_WorkerSetting.html): Details about worker setting of a connector
