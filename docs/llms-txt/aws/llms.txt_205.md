# Source: https://docs.aws.amazon.com/cloudwatch/latest/observabilityadmin/llms.txt

# Amazon CloudWatch Observability Admin API Reference

> You can use Amazon CloudWatch Observability Admin to discover and understand the state of telemetry configuration in CloudWatch for your AWS Organization or account. This simplifies the process of auditing your telemetry collection configurations across multiple resource types within your AWS Organization or account. By providing a consolidated view, it allows you to easily review and manage telemetry settings, helping you ensure proper monitoring and data collection across your AWS environment. For more information, see Auditing CloudWatch telemetry conï¬gurations in the CloudWatch User Guide.

- [Welcome](https://docs.aws.amazon.com/cloudwatch/latest/observabilityadmin/Welcome.html)
- [Common Parameters](https://docs.aws.amazon.com/cloudwatch/latest/observabilityadmin/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/cloudwatch/latest/observabilityadmin/CommonErrors.html)

## [Actions](https://docs.aws.amazon.com/cloudwatch/latest/observabilityadmin/API_Operations.html)

- [CreateCentralizationRuleForOrganization](https://docs.aws.amazon.com/cloudwatch/latest/observabilityadmin/API_CreateCentralizationRuleForOrganization.html): Creates a centralization rule that applies across an AWS Organization.
- [CreateS3TableIntegration](https://docs.aws.amazon.com/cloudwatch/latest/observabilityadmin/API_CreateS3TableIntegration.html): Creates an integration between CloudWatch and S3 Tables for analytics.
- [CreateTelemetryPipeline](https://docs.aws.amazon.com/cloudwatch/latest/observabilityadmin/API_CreateTelemetryPipeline.html): Creates a telemetry pipeline for processing and transforming telemetry data.
- [CreateTelemetryRule](https://docs.aws.amazon.com/cloudwatch/latest/observabilityadmin/API_CreateTelemetryRule.html): Creates a telemetry rule that defines how telemetry should be configured for AWS resources in your account.
- [CreateTelemetryRuleForOrganization](https://docs.aws.amazon.com/cloudwatch/latest/observabilityadmin/API_CreateTelemetryRuleForOrganization.html): Creates a telemetry rule that applies across an AWS Organization.
- [DeleteCentralizationRuleForOrganization](https://docs.aws.amazon.com/cloudwatch/latest/observabilityadmin/API_DeleteCentralizationRuleForOrganization.html): Deletes an organization-wide centralization rule.
- [DeleteS3TableIntegration](https://docs.aws.amazon.com/cloudwatch/latest/observabilityadmin/API_DeleteS3TableIntegration.html): Deletes an S3 Table integration and its associated data.
- [DeleteTelemetryPipeline](https://docs.aws.amazon.com/cloudwatch/latest/observabilityadmin/API_DeleteTelemetryPipeline.html): Deletes a telemetry pipeline and its associated resources.
- [DeleteTelemetryRule](https://docs.aws.amazon.com/cloudwatch/latest/observabilityadmin/API_DeleteTelemetryRule.html): Deletes a telemetry rule from your account.
- [DeleteTelemetryRuleForOrganization](https://docs.aws.amazon.com/cloudwatch/latest/observabilityadmin/API_DeleteTelemetryRuleForOrganization.html): Deletes an organization-wide telemetry rule.
- [GetCentralizationRuleForOrganization](https://docs.aws.amazon.com/cloudwatch/latest/observabilityadmin/API_GetCentralizationRuleForOrganization.html): Retrieves the details of a specific organization centralization rule.
- [GetS3TableIntegration](https://docs.aws.amazon.com/cloudwatch/latest/observabilityadmin/API_GetS3TableIntegration.html): Retrieves information about a specific S3 Table integration, including its configuration, status, and metadata.
- [GetTelemetryEnrichmentStatus](https://docs.aws.amazon.com/cloudwatch/latest/observabilityadmin/API_GetTelemetryEnrichmentStatus.html): Returns the current status of the resource tags for telemetry feature, which enhances telemetry data with additional resource metadata from AWS Resource Explorer.
- [GetTelemetryEvaluationStatus](https://docs.aws.amazon.com/cloudwatch/latest/observabilityadmin/API_GetTelemetryEvaluationStatus.html): Returns the current onboarding status of the telemetry config feature, including the status of the feature and reason the feature failed to start or stop.
- [GetTelemetryEvaluationStatusForOrganization](https://docs.aws.amazon.com/cloudwatch/latest/observabilityadmin/API_GetTelemetryEvaluationStatusForOrganization.html): This returns the onboarding status of the telemetry configuration feature for the organization.
- [GetTelemetryPipeline](https://docs.aws.amazon.com/cloudwatch/latest/observabilityadmin/API_GetTelemetryPipeline.html): Retrieves information about a specific telemetry pipeline, including its configuration, status, and metadata.
- [GetTelemetryRule](https://docs.aws.amazon.com/cloudwatch/latest/observabilityadmin/API_GetTelemetryRule.html): Retrieves the details of a specific telemetry rule in your account.
- [GetTelemetryRuleForOrganization](https://docs.aws.amazon.com/cloudwatch/latest/observabilityadmin/API_GetTelemetryRuleForOrganization.html): Retrieves the details of a specific organization telemetry rule.
- [ListCentralizationRulesForOrganization](https://docs.aws.amazon.com/cloudwatch/latest/observabilityadmin/API_ListCentralizationRulesForOrganization.html): Lists all centralization rules in your organization.
- [ListResourceTelemetry](https://docs.aws.amazon.com/cloudwatch/latest/observabilityadmin/API_ListResourceTelemetry.html): Returns a list of telemetry configurations for AWS resources supported by telemetry config.
- [ListResourceTelemetryForOrganization](https://docs.aws.amazon.com/cloudwatch/latest/observabilityadmin/API_ListResourceTelemetryForOrganization.html): Returns a list of telemetry configurations for AWS resources supported by telemetry config in the organization.
- [ListS3TableIntegrations](https://docs.aws.amazon.com/cloudwatch/latest/observabilityadmin/API_ListS3TableIntegrations.html): Lists all S3 Table integrations in your account.
- [ListTagsForResource](https://docs.aws.amazon.com/cloudwatch/latest/observabilityadmin/API_ListTagsForResource.html): Lists all tags attached to the specified resource.
- [ListTelemetryPipelines](https://docs.aws.amazon.com/cloudwatch/latest/observabilityadmin/API_ListTelemetryPipelines.html): Returns a list of telemetry pipelines in your account.
- [ListTelemetryRules](https://docs.aws.amazon.com/cloudwatch/latest/observabilityadmin/API_ListTelemetryRules.html): Lists all telemetry rules in your account.
- [ListTelemetryRulesForOrganization](https://docs.aws.amazon.com/cloudwatch/latest/observabilityadmin/API_ListTelemetryRulesForOrganization.html): Lists all telemetry rules in your organization.
- [StartTelemetryEnrichment](https://docs.aws.amazon.com/cloudwatch/latest/observabilityadmin/API_StartTelemetryEnrichment.html): Enables the resource tags for telemetry feature for your account, which enhances telemetry data with additional resource metadata from AWS Resource Explorer to provide richer context for monitoring and observability.
- [StartTelemetryEvaluation](https://docs.aws.amazon.com/cloudwatch/latest/observabilityadmin/API_StartTelemetryEvaluation.html): This action begins onboarding the caller AWS account to the telemetry config feature.
- [StartTelemetryEvaluationForOrganization](https://docs.aws.amazon.com/cloudwatch/latest/observabilityadmin/API_StartTelemetryEvaluationForOrganization.html): This actions begins onboarding the organization and all member accounts to the telemetry config feature.
- [StopTelemetryEnrichment](https://docs.aws.amazon.com/cloudwatch/latest/observabilityadmin/API_StopTelemetryEnrichment.html): Disables the resource tags for telemetry feature for your account, stopping the enhancement of telemetry data with additional resource metadata.
- [StopTelemetryEvaluation](https://docs.aws.amazon.com/cloudwatch/latest/observabilityadmin/API_StopTelemetryEvaluation.html): This action begins offboarding the caller AWS account from the telemetry config feature.
- [StopTelemetryEvaluationForOrganization](https://docs.aws.amazon.com/cloudwatch/latest/observabilityadmin/API_StopTelemetryEvaluationForOrganization.html): This action offboards the Organization of the caller AWS account from the telemetry config feature.
- [TagResource](https://docs.aws.amazon.com/cloudwatch/latest/observabilityadmin/API_TagResource.html): Adds or updates tags for a resource.
- [TestTelemetryPipeline](https://docs.aws.amazon.com/cloudwatch/latest/observabilityadmin/API_TestTelemetryPipeline.html): Tests a pipeline configuration with sample records to validate data processing before deployment.
- [UntagResource](https://docs.aws.amazon.com/cloudwatch/latest/observabilityadmin/API_UntagResource.html): Removes tags from a resource.
- [UpdateCentralizationRuleForOrganization](https://docs.aws.amazon.com/cloudwatch/latest/observabilityadmin/API_UpdateCentralizationRuleForOrganization.html): Updates an existing centralization rule that applies across an AWS Organization.
- [UpdateTelemetryPipeline](https://docs.aws.amazon.com/cloudwatch/latest/observabilityadmin/API_UpdateTelemetryPipeline.html): Updates the configuration of an existing telemetry pipeline.
- [UpdateTelemetryRule](https://docs.aws.amazon.com/cloudwatch/latest/observabilityadmin/API_UpdateTelemetryRule.html): Updates an existing telemetry rule in your account.
- [UpdateTelemetryRuleForOrganization](https://docs.aws.amazon.com/cloudwatch/latest/observabilityadmin/API_UpdateTelemetryRuleForOrganization.html): Updates an existing telemetry rule that applies across an AWS Organization.
- [ValidateTelemetryPipelineConfiguration](https://docs.aws.amazon.com/cloudwatch/latest/observabilityadmin/API_ValidateTelemetryPipelineConfiguration.html): Validates a pipeline configuration without creating the pipeline.


## [Data Types](https://docs.aws.amazon.com/cloudwatch/latest/observabilityadmin/API_Types.html)

- [ActionCondition](https://docs.aws.amazon.com/cloudwatch/latest/observabilityadmin/API_ActionCondition.html): Condition that matches based on the specific WAF action taken on the request.
- [AdvancedEventSelector](https://docs.aws.amazon.com/cloudwatch/latest/observabilityadmin/API_AdvancedEventSelector.html): Advanced event selectors let you create fine-grained selectors for management, data, and network activity events.
- [AdvancedFieldSelector](https://docs.aws.amazon.com/cloudwatch/latest/observabilityadmin/API_AdvancedFieldSelector.html): Defines criteria for selecting resources based on field values.
- [CentralizationRule](https://docs.aws.amazon.com/cloudwatch/latest/observabilityadmin/API_CentralizationRule.html): Defines how telemetry data should be centralized across an AWS Organization, including source and destination configurations.
- [CentralizationRuleDestination](https://docs.aws.amazon.com/cloudwatch/latest/observabilityadmin/API_CentralizationRuleDestination.html): Configuration specifying the primary destination for centralized telemetry data.
- [CentralizationRuleSource](https://docs.aws.amazon.com/cloudwatch/latest/observabilityadmin/API_CentralizationRuleSource.html): Configuration specifying the source of telemetry data to be centralized.
- [CentralizationRuleSummary](https://docs.aws.amazon.com/cloudwatch/latest/observabilityadmin/API_CentralizationRuleSummary.html): A summary of a centralization rule's key properties and status.
- [CloudtrailParameters](https://docs.aws.amazon.com/cloudwatch/latest/observabilityadmin/API_CloudtrailParameters.html): Parameters specific to AWS CloudTrail telemetry configuration.
- [Condition](https://docs.aws.amazon.com/cloudwatch/latest/observabilityadmin/API_Condition.html): A single condition that can match based on WAF rule action or label name.
- [ConfigurationSummary](https://docs.aws.amazon.com/cloudwatch/latest/observabilityadmin/API_ConfigurationSummary.html): Provides a summary of pipeline configuration components including sources, processors, and destinations.
- [DataSource](https://docs.aws.amazon.com/cloudwatch/latest/observabilityadmin/API_DataSource.html): Information about a data source associated with the telemetry pipeline.
- [DestinationLogsConfiguration](https://docs.aws.amazon.com/cloudwatch/latest/observabilityadmin/API_DestinationLogsConfiguration.html): Configuration for centralization destination log groups, including encryption and backup settings.
- [ELBLoadBalancerLoggingParameters](https://docs.aws.amazon.com/cloudwatch/latest/observabilityadmin/API_ELBLoadBalancerLoggingParameters.html): Configuration parameters for ELB load balancer logging, including output format and field delimiter settings.
- [Encryption](https://docs.aws.amazon.com/cloudwatch/latest/observabilityadmin/API_Encryption.html): Defines the encryption configuration for S3 Table integrations, including the encryption algorithm and KMS key settings.
- [FieldToMatch](https://docs.aws.amazon.com/cloudwatch/latest/observabilityadmin/API_FieldToMatch.html): Specifies a field in the request to redact from WAF logs, such as headers, query parameters, or body content.
- [Filter](https://docs.aws.amazon.com/cloudwatch/latest/observabilityadmin/API_Filter.html): A single filter condition that specifies behavior, requirement, and matching conditions for WAF log records.
- [IntegrationSummary](https://docs.aws.amazon.com/cloudwatch/latest/observabilityadmin/API_IntegrationSummary.html): Contains summary information about an S3 Table integration for listing operations.
- [LabelNameCondition](https://docs.aws.amazon.com/cloudwatch/latest/observabilityadmin/API_LabelNameCondition.html): Condition that matches based on WAF rule labels, with label names limited to 1024 characters.
- [LogDeliveryParameters](https://docs.aws.amazon.com/cloudwatch/latest/observabilityadmin/API_LogDeliveryParameters.html): Configuration parameters for Amazon Bedrock AgentCore logging, including logType settings.
- [LoggingFilter](https://docs.aws.amazon.com/cloudwatch/latest/observabilityadmin/API_LoggingFilter.html): Configuration that determines which WAF log records to keep or drop based on specified conditions.
- [LogGroupNameConfiguration](https://docs.aws.amazon.com/cloudwatch/latest/observabilityadmin/API_LogGroupNameConfiguration.html): Configuration that specifies a naming pattern for destination log groups created during centralization.
- [LogsBackupConfiguration](https://docs.aws.amazon.com/cloudwatch/latest/observabilityadmin/API_LogsBackupConfiguration.html): Configuration for backing up centralized log data to a secondary region.
- [LogsEncryptionConfiguration](https://docs.aws.amazon.com/cloudwatch/latest/observabilityadmin/API_LogsEncryptionConfiguration.html): Configuration for encrypting centralized log groups.
- [PipelineOutput](https://docs.aws.amazon.com/cloudwatch/latest/observabilityadmin/API_PipelineOutput.html): Contains the output from pipeline test operations, including processed records and any errors encountered.
- [PipelineOutputError](https://docs.aws.amazon.com/cloudwatch/latest/observabilityadmin/API_PipelineOutputError.html): Contains detailed error information from pipeline test operations, providing structured error responses for better debugging and troubleshooting capabilities.
- [Record](https://docs.aws.amazon.com/cloudwatch/latest/observabilityadmin/API_Record.html): Represents a test record structure used for pipeline testing operations to validate data processing.
- [SingleHeader](https://docs.aws.amazon.com/cloudwatch/latest/observabilityadmin/API_SingleHeader.html): Structure containing a name field limited to 64 characters for header or query parameter identification.
- [Source](https://docs.aws.amazon.com/cloudwatch/latest/observabilityadmin/API_Source.html): A list of source plugin types used in the pipeline configuration (such as cloudwatch_logs or s3).
- [SourceLogsConfiguration](https://docs.aws.amazon.com/cloudwatch/latest/observabilityadmin/API_SourceLogsConfiguration.html): Configuration for selecting and handling source log groups for centralization.
- [TelemetryConfiguration](https://docs.aws.amazon.com/cloudwatch/latest/observabilityadmin/API_TelemetryConfiguration.html): A model representing the state of a resource within an account according to telemetry config.
- [TelemetryDestinationConfiguration](https://docs.aws.amazon.com/cloudwatch/latest/observabilityadmin/API_TelemetryDestinationConfiguration.html): Configuration specifying where and how telemetry data should be delivered for AWS resources.
- [TelemetryPipeline](https://docs.aws.amazon.com/cloudwatch/latest/observabilityadmin/API_TelemetryPipeline.html): Represents a complete telemetry pipeline resource with configuration, status, and metadata for data processing and transformation.
- [TelemetryPipelineConfiguration](https://docs.aws.amazon.com/cloudwatch/latest/observabilityadmin/API_TelemetryPipelineConfiguration.html): Defines the configuration for a pipeline, including how data flows from sources through processors to destinations.
- [TelemetryPipelineStatusReason](https://docs.aws.amazon.com/cloudwatch/latest/observabilityadmin/API_TelemetryPipelineStatusReason.html): Provides detailed information about the status of a telemetry pipeline, including reasons for specific states.
- [TelemetryPipelineSummary](https://docs.aws.amazon.com/cloudwatch/latest/observabilityadmin/API_TelemetryPipelineSummary.html): Contains summary information about a telemetry pipeline for listing operations.
- [TelemetryRule](https://docs.aws.amazon.com/cloudwatch/latest/observabilityadmin/API_TelemetryRule.html): Defines how telemetry should be configured for specific AWS resources.
- [TelemetryRuleSummary](https://docs.aws.amazon.com/cloudwatch/latest/observabilityadmin/API_TelemetryRuleSummary.html): A summary of a telemetry rule's key properties.
- [ValidationError](https://docs.aws.amazon.com/cloudwatch/latest/observabilityadmin/API_ValidationError.html): Represents a detailed validation error with message, reason, and field mapping for comprehensive error reporting.
- [VPCFlowLogParameters](https://docs.aws.amazon.com/cloudwatch/latest/observabilityadmin/API_VPCFlowLogParameters.html): Configuration parameters specific to VPC Flow Logs.
- [WAFLoggingParameters](https://docs.aws.amazon.com/cloudwatch/latest/observabilityadmin/API_WAFLoggingParameters.html): Configuration parameters for WAF logging, including redacted fields and logging filters.
