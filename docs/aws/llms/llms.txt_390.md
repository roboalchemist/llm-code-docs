# Source: https://docs.aws.amazon.com/fis/latest/APIReference/llms.txt

# AWS Fault Injection Service API Reference

> AWS Fault Injection Service is a managed service that enables you to perform fault injection experiments on your AWS workloads. For more information, see the AWS Fault Injection Service User Guide.

- [Welcome](https://docs.aws.amazon.com/fis/latest/APIReference/Welcome.html)
- [Common Parameters](https://docs.aws.amazon.com/fis/latest/APIReference/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/fis/latest/APIReference/CommonErrors.html)

## [Actions](https://docs.aws.amazon.com/fis/latest/APIReference/API_Operations.html)

- [CreateExperimentTemplate](https://docs.aws.amazon.com/fis/latest/APIReference/API_CreateExperimentTemplate.html): Creates an experiment template.
- [CreateTargetAccountConfiguration](https://docs.aws.amazon.com/fis/latest/APIReference/API_CreateTargetAccountConfiguration.html): Creates a target account configuration for the experiment template.
- [DeleteExperimentTemplate](https://docs.aws.amazon.com/fis/latest/APIReference/API_DeleteExperimentTemplate.html): Deletes the specified experiment template.
- [DeleteTargetAccountConfiguration](https://docs.aws.amazon.com/fis/latest/APIReference/API_DeleteTargetAccountConfiguration.html): Deletes the specified target account configuration of the experiment template.
- [GetAction](https://docs.aws.amazon.com/fis/latest/APIReference/API_GetAction.html): Gets information about the specified AWS FIS action.
- [GetExperiment](https://docs.aws.amazon.com/fis/latest/APIReference/API_GetExperiment.html): Gets information about the specified experiment.
- [GetExperimentTargetAccountConfiguration](https://docs.aws.amazon.com/fis/latest/APIReference/API_GetExperimentTargetAccountConfiguration.html): Gets information about the specified target account configuration of the experiment.
- [GetExperimentTemplate](https://docs.aws.amazon.com/fis/latest/APIReference/API_GetExperimentTemplate.html): Gets information about the specified experiment template.
- [GetSafetyLever](https://docs.aws.amazon.com/fis/latest/APIReference/API_GetSafetyLever.html): Gets information about the specified safety lever.
- [GetTargetAccountConfiguration](https://docs.aws.amazon.com/fis/latest/APIReference/API_GetTargetAccountConfiguration.html): Gets information about the specified target account configuration of the experiment template.
- [GetTargetResourceType](https://docs.aws.amazon.com/fis/latest/APIReference/API_GetTargetResourceType.html): Gets information about the specified resource type.
- [ListActions](https://docs.aws.amazon.com/fis/latest/APIReference/API_ListActions.html): Lists the available AWS FIS actions.
- [ListExperimentResolvedTargets](https://docs.aws.amazon.com/fis/latest/APIReference/API_ListExperimentResolvedTargets.html): Lists the resolved targets information of the specified experiment.
- [ListExperiments](https://docs.aws.amazon.com/fis/latest/APIReference/API_ListExperiments.html): Lists your experiments.
- [ListExperimentTargetAccountConfigurations](https://docs.aws.amazon.com/fis/latest/APIReference/API_ListExperimentTargetAccountConfigurations.html): Lists the target account configurations of the specified experiment.
- [ListExperimentTemplates](https://docs.aws.amazon.com/fis/latest/APIReference/API_ListExperimentTemplates.html): Lists your experiment templates.
- [ListTagsForResource](https://docs.aws.amazon.com/fis/latest/APIReference/API_ListTagsForResource.html): Lists the tags for the specified resource.
- [ListTargetAccountConfigurations](https://docs.aws.amazon.com/fis/latest/APIReference/API_ListTargetAccountConfigurations.html): Lists the target account configurations of the specified experiment template.
- [ListTargetResourceTypes](https://docs.aws.amazon.com/fis/latest/APIReference/API_ListTargetResourceTypes.html): Lists the target resource types.
- [StartExperiment](https://docs.aws.amazon.com/fis/latest/APIReference/API_StartExperiment.html): Starts running an experiment from the specified experiment template.
- [StopExperiment](https://docs.aws.amazon.com/fis/latest/APIReference/API_StopExperiment.html): Stops the specified experiment.
- [TagResource](https://docs.aws.amazon.com/fis/latest/APIReference/API_TagResource.html): Applies the specified tags to the specified resource.
- [UntagResource](https://docs.aws.amazon.com/fis/latest/APIReference/API_UntagResource.html): Removes the specified tags from the specified resource.
- [UpdateExperimentTemplate](https://docs.aws.amazon.com/fis/latest/APIReference/API_UpdateExperimentTemplate.html): Updates the specified experiment template.
- [UpdateSafetyLeverState](https://docs.aws.amazon.com/fis/latest/APIReference/API_UpdateSafetyLeverState.html): Updates the specified safety lever state.
- [UpdateTargetAccountConfiguration](https://docs.aws.amazon.com/fis/latest/APIReference/API_UpdateTargetAccountConfiguration.html): Updates the target account configuration for the specified experiment template.


## [Data Types](https://docs.aws.amazon.com/fis/latest/APIReference/API_Types.html)

- [Action](https://docs.aws.amazon.com/fis/latest/APIReference/API_Action.html): Describes an action.
- [ActionParameter](https://docs.aws.amazon.com/fis/latest/APIReference/API_ActionParameter.html): Describes a parameter for an action.
- [ActionSummary](https://docs.aws.amazon.com/fis/latest/APIReference/API_ActionSummary.html): Provides a summary of an action.
- [ActionTarget](https://docs.aws.amazon.com/fis/latest/APIReference/API_ActionTarget.html): Describes a target for an action.
- [CreateExperimentTemplateActionInput](https://docs.aws.amazon.com/fis/latest/APIReference/API_CreateExperimentTemplateActionInput.html): Specifies an action for an experiment template.
- [CreateExperimentTemplateExperimentOptionsInput](https://docs.aws.amazon.com/fis/latest/APIReference/API_CreateExperimentTemplateExperimentOptionsInput.html): Specifies experiment options for an experiment template.
- [CreateExperimentTemplateLogConfigurationInput](https://docs.aws.amazon.com/fis/latest/APIReference/API_CreateExperimentTemplateLogConfigurationInput.html): Specifies the configuration for experiment logging.
- [CreateExperimentTemplateReportConfigurationInput](https://docs.aws.amazon.com/fis/latest/APIReference/API_CreateExperimentTemplateReportConfigurationInput.html): Specifies the configuration for experiment reports.
- [CreateExperimentTemplateStopConditionInput](https://docs.aws.amazon.com/fis/latest/APIReference/API_CreateExperimentTemplateStopConditionInput.html): Specifies a stop condition for an experiment template.
- [CreateExperimentTemplateTargetInput](https://docs.aws.amazon.com/fis/latest/APIReference/API_CreateExperimentTemplateTargetInput.html): Specifies a target for an experiment.
- [Experiment](https://docs.aws.amazon.com/fis/latest/APIReference/API_Experiment.html): Describes an experiment.
- [ExperimentAction](https://docs.aws.amazon.com/fis/latest/APIReference/API_ExperimentAction.html): Describes the action for an experiment.
- [ExperimentActionState](https://docs.aws.amazon.com/fis/latest/APIReference/API_ExperimentActionState.html): Describes the state of an action.
- [ExperimentCloudWatchLogsLogConfiguration](https://docs.aws.amazon.com/fis/latest/APIReference/API_ExperimentCloudWatchLogsLogConfiguration.html): Describes the configuration for experiment logging to Amazon CloudWatch Logs.
- [ExperimentError](https://docs.aws.amazon.com/fis/latest/APIReference/API_ExperimentError.html): Describes the error when an experiment has failed.
- [ExperimentLogConfiguration](https://docs.aws.amazon.com/fis/latest/APIReference/API_ExperimentLogConfiguration.html): Describes the configuration for experiment logging.
- [ExperimentOptions](https://docs.aws.amazon.com/fis/latest/APIReference/API_ExperimentOptions.html): Describes the options for an experiment.
- [ExperimentReport](https://docs.aws.amazon.com/fis/latest/APIReference/API_ExperimentReport.html): Describes the experiment report.
- [ExperimentReportConfiguration](https://docs.aws.amazon.com/fis/latest/APIReference/API_ExperimentReportConfiguration.html): Describes the report configuration for the experiment.
- [ExperimentReportConfigurationCloudWatchDashboard](https://docs.aws.amazon.com/fis/latest/APIReference/API_ExperimentReportConfigurationCloudWatchDashboard.html): Specifies the CloudWatch dashboard to include in the experiment report.
- [ExperimentReportConfigurationDataSources](https://docs.aws.amazon.com/fis/latest/APIReference/API_ExperimentReportConfigurationDataSources.html): Describes the data sources for the experiment report.
- [ExperimentReportConfigurationOutputs](https://docs.aws.amazon.com/fis/latest/APIReference/API_ExperimentReportConfigurationOutputs.html): Describes the output destinations of the experiment report.
- [ExperimentReportConfigurationOutputsS3Configuration](https://docs.aws.amazon.com/fis/latest/APIReference/API_ExperimentReportConfigurationOutputsS3Configuration.html): Specifies the S3 destination for the experiment report.
- [ExperimentReportError](https://docs.aws.amazon.com/fis/latest/APIReference/API_ExperimentReportError.html): Describes the error when experiment report generation has failed.
- [ExperimentReportS3Report](https://docs.aws.amazon.com/fis/latest/APIReference/API_ExperimentReportS3Report.html): Describes the S3 destination for the report.
- [ExperimentReportState](https://docs.aws.amazon.com/fis/latest/APIReference/API_ExperimentReportState.html): Describes the state of the experiment report generation.
- [ExperimentS3LogConfiguration](https://docs.aws.amazon.com/fis/latest/APIReference/API_ExperimentS3LogConfiguration.html): Describes the configuration for experiment logging to Amazon S3.
- [ExperimentState](https://docs.aws.amazon.com/fis/latest/APIReference/API_ExperimentState.html): Describes the state of an experiment.
- [ExperimentStopCondition](https://docs.aws.amazon.com/fis/latest/APIReference/API_ExperimentStopCondition.html): Describes the stop condition for an experiment.
- [ExperimentSummary](https://docs.aws.amazon.com/fis/latest/APIReference/API_ExperimentSummary.html): Provides a summary of an experiment.
- [ExperimentTarget](https://docs.aws.amazon.com/fis/latest/APIReference/API_ExperimentTarget.html): Describes a target for an experiment.
- [ExperimentTargetAccountConfiguration](https://docs.aws.amazon.com/fis/latest/APIReference/API_ExperimentTargetAccountConfiguration.html): Describes a target account configuration for an experiment.
- [ExperimentTargetAccountConfigurationSummary](https://docs.aws.amazon.com/fis/latest/APIReference/API_ExperimentTargetAccountConfigurationSummary.html): Provides a summary of a target account configuration.
- [ExperimentTargetFilter](https://docs.aws.amazon.com/fis/latest/APIReference/API_ExperimentTargetFilter.html): Describes a filter used for the target resources in an experiment.
- [ExperimentTemplate](https://docs.aws.amazon.com/fis/latest/APIReference/API_ExperimentTemplate.html): Describes an experiment template.
- [ExperimentTemplateAction](https://docs.aws.amazon.com/fis/latest/APIReference/API_ExperimentTemplateAction.html): Describes an action for an experiment template.
- [ExperimentTemplateCloudWatchLogsLogConfiguration](https://docs.aws.amazon.com/fis/latest/APIReference/API_ExperimentTemplateCloudWatchLogsLogConfiguration.html): Describes the configuration for experiment logging to Amazon CloudWatch Logs.
- [ExperimentTemplateCloudWatchLogsLogConfigurationInput](https://docs.aws.amazon.com/fis/latest/APIReference/API_ExperimentTemplateCloudWatchLogsLogConfigurationInput.html): Specifies the configuration for experiment logging to Amazon CloudWatch Logs.
- [ExperimentTemplateExperimentOptions](https://docs.aws.amazon.com/fis/latest/APIReference/API_ExperimentTemplateExperimentOptions.html): Describes the experiment options for an experiment template.
- [ExperimentTemplateLogConfiguration](https://docs.aws.amazon.com/fis/latest/APIReference/API_ExperimentTemplateLogConfiguration.html): Describes the configuration for experiment logging.
- [ExperimentTemplateReportConfiguration](https://docs.aws.amazon.com/fis/latest/APIReference/API_ExperimentTemplateReportConfiguration.html): Describes the experiment report configuration.
- [ExperimentTemplateReportConfigurationCloudWatchDashboard](https://docs.aws.amazon.com/fis/latest/APIReference/API_ExperimentTemplateReportConfigurationCloudWatchDashboard.html): The CloudWatch dashboards to include as data sources in the experiment report.
- [ExperimentTemplateReportConfigurationDataSources](https://docs.aws.amazon.com/fis/latest/APIReference/API_ExperimentTemplateReportConfigurationDataSources.html): Describes the data sources for the experiment report.
- [ExperimentTemplateReportConfigurationDataSourcesInput](https://docs.aws.amazon.com/fis/latest/APIReference/API_ExperimentTemplateReportConfigurationDataSourcesInput.html): Specifies the data sources for the experiment report.
- [ExperimentTemplateReportConfigurationOutputs](https://docs.aws.amazon.com/fis/latest/APIReference/API_ExperimentTemplateReportConfigurationOutputs.html): The output destinations of the experiment report.
- [ExperimentTemplateReportConfigurationOutputsInput](https://docs.aws.amazon.com/fis/latest/APIReference/API_ExperimentTemplateReportConfigurationOutputsInput.html): Specifies the outputs for the experiment templates.
- [ExperimentTemplateS3LogConfiguration](https://docs.aws.amazon.com/fis/latest/APIReference/API_ExperimentTemplateS3LogConfiguration.html): Describes the configuration for experiment logging to Amazon S3.
- [ExperimentTemplateS3LogConfigurationInput](https://docs.aws.amazon.com/fis/latest/APIReference/API_ExperimentTemplateS3LogConfigurationInput.html): Specifies the configuration for experiment logging to Amazon S3.
- [ExperimentTemplateStopCondition](https://docs.aws.amazon.com/fis/latest/APIReference/API_ExperimentTemplateStopCondition.html): Describes a stop condition for an experiment template.
- [ExperimentTemplateSummary](https://docs.aws.amazon.com/fis/latest/APIReference/API_ExperimentTemplateSummary.html): Provides a summary of an experiment template.
- [ExperimentTemplateTarget](https://docs.aws.amazon.com/fis/latest/APIReference/API_ExperimentTemplateTarget.html): Describes a target for an experiment template.
- [ExperimentTemplateTargetFilter](https://docs.aws.amazon.com/fis/latest/APIReference/API_ExperimentTemplateTargetFilter.html): Describes a filter used for the target resources in an experiment template.
- [ExperimentTemplateTargetInputFilter](https://docs.aws.amazon.com/fis/latest/APIReference/API_ExperimentTemplateTargetInputFilter.html): Specifies a filter used for the target resource input in an experiment template.
- [ReportConfigurationCloudWatchDashboardInput](https://docs.aws.amazon.com/fis/latest/APIReference/API_ReportConfigurationCloudWatchDashboardInput.html): Specifies the CloudWatch dashboard for the experiment report.
- [ReportConfigurationS3Output](https://docs.aws.amazon.com/fis/latest/APIReference/API_ReportConfigurationS3Output.html): Describes the S3 destination for the experiment report.
- [ReportConfigurationS3OutputInput](https://docs.aws.amazon.com/fis/latest/APIReference/API_ReportConfigurationS3OutputInput.html): Specifies the S3 destination for the experiment report.
- [ResolvedTarget](https://docs.aws.amazon.com/fis/latest/APIReference/API_ResolvedTarget.html): Describes a resolved target.
- [SafetyLever](https://docs.aws.amazon.com/fis/latest/APIReference/API_SafetyLever.html): Describes a safety lever.
- [SafetyLeverState](https://docs.aws.amazon.com/fis/latest/APIReference/API_SafetyLeverState.html): Describes the state of the safety lever.
- [StartExperimentExperimentOptionsInput](https://docs.aws.amazon.com/fis/latest/APIReference/API_StartExperimentExperimentOptionsInput.html): Specifies experiment options for running an experiment.
- [TargetAccountConfiguration](https://docs.aws.amazon.com/fis/latest/APIReference/API_TargetAccountConfiguration.html): Describes a target account configuration.
- [TargetAccountConfigurationSummary](https://docs.aws.amazon.com/fis/latest/APIReference/API_TargetAccountConfigurationSummary.html): Provides a summary of a target account configuration.
- [TargetResourceType](https://docs.aws.amazon.com/fis/latest/APIReference/API_TargetResourceType.html): Describes a resource type.
- [TargetResourceTypeParameter](https://docs.aws.amazon.com/fis/latest/APIReference/API_TargetResourceTypeParameter.html): Describes the parameters for a resource type.
- [TargetResourceTypeSummary](https://docs.aws.amazon.com/fis/latest/APIReference/API_TargetResourceTypeSummary.html): Describes a resource type.
- [UpdateExperimentTemplateActionInputItem](https://docs.aws.amazon.com/fis/latest/APIReference/API_UpdateExperimentTemplateActionInputItem.html): Specifies an action for an experiment template.
- [UpdateExperimentTemplateExperimentOptionsInput](https://docs.aws.amazon.com/fis/latest/APIReference/API_UpdateExperimentTemplateExperimentOptionsInput.html): Specifies an experiment option for an experiment template.
- [UpdateExperimentTemplateLogConfigurationInput](https://docs.aws.amazon.com/fis/latest/APIReference/API_UpdateExperimentTemplateLogConfigurationInput.html): Specifies the configuration for experiment logging.
- [UpdateExperimentTemplateReportConfigurationInput](https://docs.aws.amazon.com/fis/latest/APIReference/API_UpdateExperimentTemplateReportConfigurationInput.html): Specifies the input for the experiment report configuration.
- [UpdateExperimentTemplateStopConditionInput](https://docs.aws.amazon.com/fis/latest/APIReference/API_UpdateExperimentTemplateStopConditionInput.html): Specifies a stop condition for an experiment.
- [UpdateExperimentTemplateTargetInput](https://docs.aws.amazon.com/fis/latest/APIReference/API_UpdateExperimentTemplateTargetInput.html): Specifies a target for an experiment.
- [UpdateSafetyLeverStateInput](https://docs.aws.amazon.com/fis/latest/APIReference/API_UpdateSafetyLeverStateInput.html): Specifies a state for a safety lever.
