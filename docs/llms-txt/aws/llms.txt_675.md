# Source: https://docs.aws.amazon.com/prometheus/latest/APIReference/llms.txt

# Amazon Managed Service for Prometheus API Reference

> Amazon Managed Service for Prometheus is a serverless, Prometheus-compatible monitoring service for container metrics that makes it easier to securely monitor container environments at scale. With Amazon Managed Service for Prometheus, you can use the same open-source Prometheus data model and query language that you use today to monitor the performance of your containerized workloads, and also enjoy improved scalability, availability, and security without having to manage the underlying infrastructure.

- [Welcome](https://docs.aws.amazon.com/prometheus/latest/APIReference/Welcome.html)
- [Common Parameters](https://docs.aws.amazon.com/prometheus/latest/APIReference/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/prometheus/latest/APIReference/CommonErrors.html)

## [Actions](https://docs.aws.amazon.com/prometheus/latest/APIReference/API_Operations.html)

- [CreateAlertManagerDefinition](https://docs.aws.amazon.com/prometheus/latest/APIReference/API_CreateAlertManagerDefinition.html): The CreateAlertManagerDefinition operation creates the alert manager definition in a workspace.
- [CreateAnomalyDetector](https://docs.aws.amazon.com/prometheus/latest/APIReference/API_CreateAnomalyDetector.html): Creates an anomaly detector within a workspace using the Random Cut Forest algorithm for time-series analysis.
- [CreateLoggingConfiguration](https://docs.aws.amazon.com/prometheus/latest/APIReference/API_CreateLoggingConfiguration.html): The CreateLoggingConfiguration operation creates rules and alerting logging configuration for the workspace.
- [CreateQueryLoggingConfiguration](https://docs.aws.amazon.com/prometheus/latest/APIReference/API_CreateQueryLoggingConfiguration.html): Creates a query logging configuration for the specified workspace.
- [CreateRuleGroupsNamespace](https://docs.aws.amazon.com/prometheus/latest/APIReference/API_CreateRuleGroupsNamespace.html): The CreateRuleGroupsNamespace operation creates a rule groups namespace within a workspace.
- [CreateScraper](https://docs.aws.amazon.com/prometheus/latest/APIReference/API_CreateScraper.html): The CreateScraper operation creates a scraper to collect metrics.
- [CreateWorkspace](https://docs.aws.amazon.com/prometheus/latest/APIReference/API_CreateWorkspace.html): Creates a Prometheus workspace.
- [DeleteAlertManagerDefinition](https://docs.aws.amazon.com/prometheus/latest/APIReference/API_DeleteAlertManagerDefinition.html): Deletes the alert manager definition from a workspace.
- [DeleteAnomalyDetector](https://docs.aws.amazon.com/prometheus/latest/APIReference/API_DeleteAnomalyDetector.html): Removes an anomaly detector from a workspace.
- [DeleteLoggingConfiguration](https://docs.aws.amazon.com/prometheus/latest/APIReference/API_DeleteLoggingConfiguration.html): Deletes the rules and alerting logging configuration for a workspace.
- [DeleteQueryLoggingConfiguration](https://docs.aws.amazon.com/prometheus/latest/APIReference/API_DeleteQueryLoggingConfiguration.html): Deletes the query logging configuration for the specified workspace.
- [DeleteResourcePolicy](https://docs.aws.amazon.com/prometheus/latest/APIReference/API_DeleteResourcePolicy.html): Deletes the resource-based policy attached to an Amazon Managed Service for Prometheus workspace.
- [DeleteRuleGroupsNamespace](https://docs.aws.amazon.com/prometheus/latest/APIReference/API_DeleteRuleGroupsNamespace.html): Deletes one rule groups namespace and its associated rule groups definition.
- [DeleteScraper](https://docs.aws.amazon.com/prometheus/latest/APIReference/API_DeleteScraper.html): The DeleteScraper operation deletes one scraper, and stops any metrics collection that the scraper performs.
- [DeleteScraperLoggingConfiguration](https://docs.aws.amazon.com/prometheus/latest/APIReference/API_DeleteScraperLoggingConfiguration.html): Deletes the logging configuration for a Amazon Managed Service for Prometheus scraper.
- [DeleteWorkspace](https://docs.aws.amazon.com/prometheus/latest/APIReference/API_DeleteWorkspace.html): Deletes an existing workspace.
- [DescribeAlertManagerDefinition](https://docs.aws.amazon.com/prometheus/latest/APIReference/API_DescribeAlertManagerDefinition.html): Retrieves the full information about the alert manager definition for a workspace.
- [DescribeAnomalyDetector](https://docs.aws.amazon.com/prometheus/latest/APIReference/API_DescribeAnomalyDetector.html): Retrieves detailed information about a specific anomaly detector, including its status and configuration.
- [DescribeLoggingConfiguration](https://docs.aws.amazon.com/prometheus/latest/APIReference/API_DescribeLoggingConfiguration.html): Returns complete information about the current rules and alerting logging configuration of the workspace.
- [DescribeQueryLoggingConfiguration](https://docs.aws.amazon.com/prometheus/latest/APIReference/API_DescribeQueryLoggingConfiguration.html): Retrieves the details of the query logging configuration for the specified workspace.
- [DescribeResourcePolicy](https://docs.aws.amazon.com/prometheus/latest/APIReference/API_DescribeResourcePolicy.html): Returns information about the resource-based policy attached to an Amazon Managed Service for Prometheus workspace.
- [DescribeRuleGroupsNamespace](https://docs.aws.amazon.com/prometheus/latest/APIReference/API_DescribeRuleGroupsNamespace.html): Returns complete information about one rule groups namespace.
- [DescribeScraper](https://docs.aws.amazon.com/prometheus/latest/APIReference/API_DescribeScraper.html): The DescribeScraper operation displays information about an existing scraper.
- [DescribeScraperLoggingConfiguration](https://docs.aws.amazon.com/prometheus/latest/APIReference/API_DescribeScraperLoggingConfiguration.html): Describes the logging configuration for a Amazon Managed Service for Prometheus scraper.
- [DescribeWorkspace](https://docs.aws.amazon.com/prometheus/latest/APIReference/API_DescribeWorkspace.html): Returns information about an existing workspace.
- [DescribeWorkspaceConfiguration](https://docs.aws.amazon.com/prometheus/latest/APIReference/API_DescribeWorkspaceConfiguration.html): Use this operation to return information about the configuration of a workspace.
- [GetDefaultScraperConfiguration](https://docs.aws.amazon.com/prometheus/latest/APIReference/API_GetDefaultScraperConfiguration.html): The GetDefaultScraperConfiguration operation returns the default scraper configuration used when Amazon EKS creates a scraper for you.
- [ListAnomalyDetectors](https://docs.aws.amazon.com/prometheus/latest/APIReference/API_ListAnomalyDetectors.html): Returns a paginated list of anomaly detectors for a workspace with optional filtering by alias.
- [ListRuleGroupsNamespaces](https://docs.aws.amazon.com/prometheus/latest/APIReference/API_ListRuleGroupsNamespaces.html): Returns a list of rule groups namespaces in a workspace.
- [ListScrapers](https://docs.aws.amazon.com/prometheus/latest/APIReference/API_ListScrapers.html): The ListScrapers operation lists all of the scrapers in your account.
- [ListTagsForResource](https://docs.aws.amazon.com/prometheus/latest/APIReference/API_ListTagsForResource.html): The ListTagsForResource operation returns the tags that are associated with an Amazon Managed Service for Prometheus resource.
- [ListWorkspaces](https://docs.aws.amazon.com/prometheus/latest/APIReference/API_ListWorkspaces.html): Lists all of the Amazon Managed Service for Prometheus workspaces in your account.
- [PutAlertManagerDefinition](https://docs.aws.amazon.com/prometheus/latest/APIReference/API_PutAlertManagerDefinition.html): Updates an existing alert manager definition in a workspace.
- [PutAnomalyDetector](https://docs.aws.amazon.com/prometheus/latest/APIReference/API_PutAnomalyDetector.html): When you call PutAnomalyDetector, the operation creates a new anomaly detector if one doesn't exist, or updates an existing one.
- [PutResourcePolicy](https://docs.aws.amazon.com/prometheus/latest/APIReference/API_PutResourcePolicy.html): Creates or updates a resource-based policy for an Amazon Managed Service for Prometheus workspace.
- [PutRuleGroupsNamespace](https://docs.aws.amazon.com/prometheus/latest/APIReference/API_PutRuleGroupsNamespace.html): Updates an existing rule groups namespace within a workspace.
- [TagResource](https://docs.aws.amazon.com/prometheus/latest/APIReference/API_TagResource.html): The TagResource operation associates tags with an Amazon Managed Service for Prometheus resource.
- [UntagResource](https://docs.aws.amazon.com/prometheus/latest/APIReference/API_UntagResource.html): Removes the specified tags from an Amazon Managed Service for Prometheus resource.
- [UpdateLoggingConfiguration](https://docs.aws.amazon.com/prometheus/latest/APIReference/API_UpdateLoggingConfiguration.html): Updates the log group ARN or the workspace ID of the current rules and alerting logging configuration.
- [UpdateQueryLoggingConfiguration](https://docs.aws.amazon.com/prometheus/latest/APIReference/API_UpdateQueryLoggingConfiguration.html): Updates the query logging configuration for the specified workspace.
- [UpdateScraper](https://docs.aws.amazon.com/prometheus/latest/APIReference/API_UpdateScraper.html): Updates an existing scraper.
- [UpdateScraperLoggingConfiguration](https://docs.aws.amazon.com/prometheus/latest/APIReference/API_UpdateScraperLoggingConfiguration.html): Updates the logging configuration for a Amazon Managed Service for Prometheus scraper.
- [UpdateWorkspaceAlias](https://docs.aws.amazon.com/prometheus/latest/APIReference/API_UpdateWorkspaceAlias.html): Updates the alias of an existing workspace.
- [UpdateWorkspaceConfiguration](https://docs.aws.amazon.com/prometheus/latest/APIReference/API_UpdateWorkspaceConfiguration.html): Use this operation to create or update the label sets, label set limits, and retention period of a workspace.


## [Data Types](https://docs.aws.amazon.com/prometheus/latest/APIReference/API_Types.html)

- [AlertManagerDefinitionDescription](https://docs.aws.amazon.com/prometheus/latest/APIReference/API_AlertManagerDefinitionDescription.html): The details of an alert manager definition.
- [AlertManagerDefinitionStatus](https://docs.aws.amazon.com/prometheus/latest/APIReference/API_AlertManagerDefinitionStatus.html): The status of the alert manager.
- [AmpConfiguration](https://docs.aws.amazon.com/prometheus/latest/APIReference/API_AmpConfiguration.html): The AmpConfiguration structure defines the Amazon Managed Service for Prometheus instance a scraper should send metrics to.
- [AnomalyDetectorConfiguration](https://docs.aws.amazon.com/prometheus/latest/APIReference/API_AnomalyDetectorConfiguration.html): The configuration for the anomaly detection algorithm.
- [AnomalyDetectorDescription](https://docs.aws.amazon.com/prometheus/latest/APIReference/API_AnomalyDetectorDescription.html): Detailed information about an anomaly detector.
- [AnomalyDetectorMissingDataAction](https://docs.aws.amazon.com/prometheus/latest/APIReference/API_AnomalyDetectorMissingDataAction.html): Specifies the action to take when data is missing during anomaly detection evaluation.
- [AnomalyDetectorStatus](https://docs.aws.amazon.com/prometheus/latest/APIReference/API_AnomalyDetectorStatus.html): The status information of an anomaly detector.
- [AnomalyDetectorSummary](https://docs.aws.amazon.com/prometheus/latest/APIReference/API_AnomalyDetectorSummary.html): Summary information about an anomaly detector for list operations.
- [CloudWatchLogDestination](https://docs.aws.amazon.com/prometheus/latest/APIReference/API_CloudWatchLogDestination.html): Configuration details for logging to CloudWatch Logs.
- [ComponentConfig](https://docs.aws.amazon.com/prometheus/latest/APIReference/API_ComponentConfig.html): Configuration settings for a scraper component.
- [Destination](https://docs.aws.amazon.com/prometheus/latest/APIReference/API_Destination.html): Where to send the metrics from a scraper.
- [EksConfiguration](https://docs.aws.amazon.com/prometheus/latest/APIReference/API_EksConfiguration.html): The EksConfiguration structure describes the connection to the Amazon EKS cluster from which a scraper collects metrics.
- [IgnoreNearExpected](https://docs.aws.amazon.com/prometheus/latest/APIReference/API_IgnoreNearExpected.html): Configuration for threshold settings that determine when values near expected values should be ignored during anomaly detection.
- [LimitsPerLabelSet](https://docs.aws.amazon.com/prometheus/latest/APIReference/API_LimitsPerLabelSet.html): This structure defines one label set used to enforce active time series limits for the workspace, and defines the limit for that label set.
- [LimitsPerLabelSetEntry](https://docs.aws.amazon.com/prometheus/latest/APIReference/API_LimitsPerLabelSetEntry.html): This structure contains the information about the limits that apply to time series that match one label set.
- [LoggingConfigurationMetadata](https://docs.aws.amazon.com/prometheus/latest/APIReference/API_LoggingConfigurationMetadata.html): Contains information about the current rules and alerting logging configuration for the workspace.
- [LoggingConfigurationStatus](https://docs.aws.amazon.com/prometheus/latest/APIReference/API_LoggingConfigurationStatus.html): The status of the logging configuration.
- [LoggingDestination](https://docs.aws.amazon.com/prometheus/latest/APIReference/API_LoggingDestination.html): Defines a destination and its associated filtering criteria for query logging.
- [LoggingFilter](https://docs.aws.amazon.com/prometheus/latest/APIReference/API_LoggingFilter.html): Filtering criteria that determine which queries are logged.
- [QueryLoggingConfigurationMetadata](https://docs.aws.amazon.com/prometheus/latest/APIReference/API_QueryLoggingConfigurationMetadata.html): The metadata for a query logging configuration.
- [QueryLoggingConfigurationStatus](https://docs.aws.amazon.com/prometheus/latest/APIReference/API_QueryLoggingConfigurationStatus.html): The status information for a query logging configuration.
- [RandomCutForestConfiguration](https://docs.aws.amazon.com/prometheus/latest/APIReference/API_RandomCutForestConfiguration.html): Configuration for the Random Cut Forest algorithm used for anomaly detection in time-series data.
- [RoleConfiguration](https://docs.aws.amazon.com/prometheus/latest/APIReference/API_RoleConfiguration.html): Use this structure to enable cross-account access, so that you can use a target account to access Prometheus metrics from source accounts.
- [RuleGroupsNamespaceDescription](https://docs.aws.amazon.com/prometheus/latest/APIReference/API_RuleGroupsNamespaceDescription.html): The details about one rule groups namespace.
- [RuleGroupsNamespaceStatus](https://docs.aws.amazon.com/prometheus/latest/APIReference/API_RuleGroupsNamespaceStatus.html): The status information about a rule groups namespace.
- [RuleGroupsNamespaceSummary](https://docs.aws.amazon.com/prometheus/latest/APIReference/API_RuleGroupsNamespaceSummary.html): The high-level information about a rule groups namespace.
- [ScrapeConfiguration](https://docs.aws.amazon.com/prometheus/latest/APIReference/API_ScrapeConfiguration.html): A scrape configuration for a scraper, base 64 encoded.
- [ScraperComponent](https://docs.aws.amazon.com/prometheus/latest/APIReference/API_ScraperComponent.html): A component of a Amazon Managed Service for Prometheus scraper that can be configured for logging.
- [ScraperDescription](https://docs.aws.amazon.com/prometheus/latest/APIReference/API_ScraperDescription.html): The ScraperDescription structure contains the full details about one scraper in your account.
- [ScraperLoggingConfigurationStatus](https://docs.aws.amazon.com/prometheus/latest/APIReference/API_ScraperLoggingConfigurationStatus.html): The status of a scraper logging configuration.
- [ScraperLoggingDestination](https://docs.aws.amazon.com/prometheus/latest/APIReference/API_ScraperLoggingDestination.html): The destination where scraper logs are sent.
- [ScraperStatus](https://docs.aws.amazon.com/prometheus/latest/APIReference/API_ScraperStatus.html): The ScraperStatus structure contains status information about the scraper.
- [ScraperSummary](https://docs.aws.amazon.com/prometheus/latest/APIReference/API_ScraperSummary.html): The ScraperSummary structure contains a summary of the details about one scraper in your account.
- [Source](https://docs.aws.amazon.com/prometheus/latest/APIReference/API_Source.html): The source of collected metrics for a scraper.
- [ValidationExceptionField](https://docs.aws.amazon.com/prometheus/latest/APIReference/API_ValidationExceptionField.html): Information about a field passed into a request that resulted in an exception.
- [VpcConfiguration](https://docs.aws.amazon.com/prometheus/latest/APIReference/API_VpcConfiguration.html): The Amazon VPC configuration that specifies the network settings for a Prometheus collector to securely connect to Amazon MSK clusters.
- [WorkspaceConfigurationDescription](https://docs.aws.amazon.com/prometheus/latest/APIReference/API_WorkspaceConfigurationDescription.html): This structure contains the description of the workspace configuration.
- [WorkspaceConfigurationStatus](https://docs.aws.amazon.com/prometheus/latest/APIReference/API_WorkspaceConfigurationStatus.html): This structure displays the current status of the workspace configuration, and might also contain a reason for that status.
- [WorkspaceDescription](https://docs.aws.amazon.com/prometheus/latest/APIReference/API_WorkspaceDescription.html): The full details about one Amazon Managed Service for Prometheus workspace in your account.
- [WorkspaceStatus](https://docs.aws.amazon.com/prometheus/latest/APIReference/API_WorkspaceStatus.html): The status of the workspace.
- [WorkspaceSummary](https://docs.aws.amazon.com/prometheus/latest/APIReference/API_WorkspaceSummary.html): The information about one Amazon Managed Service for Prometheus workspace in your account.


## [YAML types](https://docs.aws.amazon.com/prometheus/latest/APIReference/yaml-types.html)

- [AlertManagerDefinitionData](https://docs.aws.amazon.com/prometheus/latest/APIReference/yaml-AlertManagerDefinitionData.html): This structure contains the alert manager configuration as a blob (binary data).
- [RuleGroupsNamespaceData](https://docs.aws.amazon.com/prometheus/latest/APIReference/yaml-RuleGroupsNamespaceData.html): The RuleGroupsNamespaceData structure contains the rule groups file as a base64-encoded blob of the YAML file.
