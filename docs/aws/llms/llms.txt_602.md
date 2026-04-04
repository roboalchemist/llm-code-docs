# Source: https://docs.aws.amazon.com/mwaa/latest/API/llms.txt

# Amazon Managed Workflows for Apache Airflow Amazon MWAA

> This section contains the Amazon Managed Workflows for Apache Airflow (MWAA) API reference documentation. For more information, see What is Amazon MWAA?.

- [Welcome](https://docs.aws.amazon.com/mwaa/latest/API/Welcome.html)
- [Common Parameters](https://docs.aws.amazon.com/mwaa/latest/API/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/mwaa/latest/API/CommonErrors.html)

## [Actions](https://docs.aws.amazon.com/mwaa/latest/API/API_Operations.html)

- [CreateCliToken](https://docs.aws.amazon.com/mwaa/latest/API/API_CreateCliToken.html): Creates a CLI token for the Airflow CLI.
- [CreateEnvironment](https://docs.aws.amazon.com/mwaa/latest/API/API_CreateEnvironment.html): Creates an Amazon Managed Workflows for Apache Airflow (Amazon MWAA) environment.
- [CreateWebLoginToken](https://docs.aws.amazon.com/mwaa/latest/API/API_CreateWebLoginToken.html): Creates a web login token for the Airflow Web UI.
- [DeleteEnvironment](https://docs.aws.amazon.com/mwaa/latest/API/API_DeleteEnvironment.html): Deletes an Amazon Managed Workflows for Apache Airflow (Amazon MWAA) environment.
- [GetEnvironment](https://docs.aws.amazon.com/mwaa/latest/API/API_GetEnvironment.html): Describes an Amazon Managed Workflows for Apache Airflow (MWAA) environment.
- [InvokeRestApi](https://docs.aws.amazon.com/mwaa/latest/API/API_InvokeRestApi.html): Invokes the Apache Airflow REST API on the webserver with the specified inputs.
- [ListEnvironments](https://docs.aws.amazon.com/mwaa/latest/API/API_ListEnvironments.html): Lists the Amazon Managed Workflows for Apache Airflow (MWAA) environments.
- [ListTagsForResource](https://docs.aws.amazon.com/mwaa/latest/API/API_ListTagsForResource.html): Lists the key-value tag pairs associated to the Amazon Managed Workflows for Apache Airflow (MWAA) environment.
- [PublishMetrics](https://docs.aws.amazon.com/mwaa/latest/API/API_PublishMetrics.html): This action has been deprecated.
- [TagResource](https://docs.aws.amazon.com/mwaa/latest/API/API_TagResource.html): Associates key-value tag pairs to your Amazon Managed Workflows for Apache Airflow (MWAA) environment.
- [UntagResource](https://docs.aws.amazon.com/mwaa/latest/API/API_UntagResource.html): Removes key-value tag pairs associated to your Amazon Managed Workflows for Apache Airflow (MWAA) environment.
- [UpdateEnvironment](https://docs.aws.amazon.com/mwaa/latest/API/API_UpdateEnvironment.html): Updates an Amazon Managed Workflows for Apache Airflow (MWAA) environment.


## [Data Types](https://docs.aws.amazon.com/mwaa/latest/API/API_Types.html)

- [Dimension](https://docs.aws.amazon.com/mwaa/latest/API/API_Dimension.html): This data type has been deprecated.
- [Environment](https://docs.aws.amazon.com/mwaa/latest/API/API_Environment.html): Describes an Amazon Managed Workflows for Apache Airflow (MWAA) environment.
- [LastUpdate](https://docs.aws.amazon.com/mwaa/latest/API/API_LastUpdate.html): Describes the status of the last update on the environment, and any errors that were encountered.
- [LoggingConfiguration](https://docs.aws.amazon.com/mwaa/latest/API/API_LoggingConfiguration.html): Describes the Apache Airflow log types that are published to CloudWatch Logs.
- [LoggingConfigurationInput](https://docs.aws.amazon.com/mwaa/latest/API/API_LoggingConfigurationInput.html): Defines the Apache Airflow log types to send to CloudWatch Logs.
- [MetricDatum](https://docs.aws.amazon.com/mwaa/latest/API/API_MetricDatum.html): This data type has been deprecated.
- [ModuleLoggingConfiguration](https://docs.aws.amazon.com/mwaa/latest/API/API_ModuleLoggingConfiguration.html): Describes the Apache Airflow log details for the log type (e.g.
- [ModuleLoggingConfigurationInput](https://docs.aws.amazon.com/mwaa/latest/API/API_ModuleLoggingConfigurationInput.html): Enables the Apache Airflow log type (e.g.
- [NetworkConfiguration](https://docs.aws.amazon.com/mwaa/latest/API/API_NetworkConfiguration.html): Describes the VPC networking components used to secure and enable network traffic between the AWS resources for your environment.
- [StatisticSet](https://docs.aws.amazon.com/mwaa/latest/API/API_StatisticSet.html): This data type has been deprecated.
- [UpdateError](https://docs.aws.amazon.com/mwaa/latest/API/API_UpdateError.html): Describes the error(s) encountered with the last update of the environment.
- [UpdateNetworkConfigurationInput](https://docs.aws.amazon.com/mwaa/latest/API/API_UpdateNetworkConfigurationInput.html): Defines the VPC networking components used to secure and enable network traffic between the AWS resources for your environment.
