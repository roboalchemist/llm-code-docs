# Source: https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/llms.txt

# Migration Hub Strategy Recommendations API Reference

> This API reference provides descriptions, syntax, and other details about each of the actions and data types for Migration Hub Strategy Recommendations (Strategy Recommendations). The topic for each action shows the API request parameters and the response. Alternatively, you can use one of the AWS SDKs to access an API that is tailored to the programming language or platform that you're using. For more information, see AWS SDKs.

- [Welcome](https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/Welcome.html)
- [Common Parameters](https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/CommonErrors.html)

## [Actions](https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_Operations.html)

- [GetApplicationComponentDetails](https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_GetApplicationComponentDetails.html)
- [GetApplicationComponentStrategies](https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_GetApplicationComponentStrategies.html)
- [GetAssessment](https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_GetAssessment.html)
- [GetImportFileTask](https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_GetImportFileTask.html)
- [GetLatestAssessmentId](https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_GetLatestAssessmentId.html)
- [GetPortfolioPreferences](https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_GetPortfolioPreferences.html)
- [GetPortfolioSummary](https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_GetPortfolioSummary.html)
- [GetRecommendationReportDetails](https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_GetRecommendationReportDetails.html)
- [GetServerDetails](https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_GetServerDetails.html)
- [GetServerStrategies](https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_GetServerStrategies.html)
- [ListAnalyzableServers](https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_ListAnalyzableServers.html)
- [ListApplicationComponents](https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_ListApplicationComponents.html)
- [ListCollectors](https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_ListCollectors.html)
- [ListImportFileTask](https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_ListImportFileTask.html)
- [ListServers](https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_ListServers.html)
- [PutPortfolioPreferences](https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_PutPortfolioPreferences.html)
- [StartAssessment](https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_StartAssessment.html)
- [StartImportFileTask](https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_StartImportFileTask.html)
- [StartRecommendationReportGeneration](https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_StartRecommendationReportGeneration.html)
- [StopAssessment](https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_StopAssessment.html)
- [UpdateApplicationComponentConfig](https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_UpdateApplicationComponentConfig.html)
- [UpdateServerConfig](https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_UpdateServerConfig.html)


## [Data Types](https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_Types.html)

- [AnalysisStatusUnion](https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_AnalysisStatusUnion.html): A combination of existing analysis statuses.
- [AnalyzableServerSummary](https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_AnalyzableServerSummary.html): A summary of information about an analyzable server.
- [AnalyzerNameUnion](https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_AnalyzerNameUnion.html): The combination of the existing analyzers.
- [AntipatternReportResult](https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_AntipatternReportResult.html): The anti-pattern report result.
- [AntipatternSeveritySummary](https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_AntipatternSeveritySummary.html): Contains the summary of anti-patterns and their severity.
- [ApplicationComponentDetail](https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_ApplicationComponentDetail.html): Contains detailed information about an application component.
- [ApplicationComponentStatusSummary](https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_ApplicationComponentStatusSummary.html): Summary of the analysis status of the application component.
- [ApplicationComponentStrategy](https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_ApplicationComponentStrategy.html): Contains information about a strategy recommendation for an application component.
- [ApplicationComponentSummary](https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_ApplicationComponentSummary.html): Contains the summary of application components.
- [ApplicationPreferences](https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_ApplicationPreferences.html): Application preferences that you specify.
- [AppUnitError](https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_AppUnitError.html): Error in the analysis of the application unit.
- [AssessmentSummary](https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_AssessmentSummary.html): Contains the summary of the assessment results.
- [AssessmentTarget](https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_AssessmentTarget.html): Defines the criteria of assessment.
- [AssociatedApplication](https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_AssociatedApplication.html): Object containing details about applications as defined in Application Discovery Service.
- [AwsManagedResources](https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_AwsManagedResources.html): Object containing the choice of application destination that you specify.
- [BusinessGoals](https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_BusinessGoals.html): Business goals that you specify.
- [Collector](https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_Collector.html): Process data collector that runs in the environment that you specify.
- [ConfigurationSummary](https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_ConfigurationSummary.html): Summary of the collector configuration.
- [DatabaseConfigDetail](https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_DatabaseConfigDetail.html): Configuration information used for assessing databases.
- [DatabaseMigrationPreference](https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_DatabaseMigrationPreference.html): Preferences for migrating a database to AWS.
- [DatabasePreferences](https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_DatabasePreferences.html): Preferences on managing your databases on AWS.
- [DataCollectionDetails](https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_DataCollectionDetails.html): Detailed information about an assessment.
- [Group](https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_Group.html): The object containing information about distinct imports or groups for Strategy Recommendations.
- [Heterogeneous](https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_Heterogeneous.html): The object containing details about heterogeneous database preferences.
- [Homogeneous](https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_Homogeneous.html): The object containing details about homogeneous database preferences.
- [ImportFileTaskInformation](https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_ImportFileTaskInformation.html): Information about the import file tasks you request.
- [IPAddressBasedRemoteInfo](https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_IPAddressBasedRemoteInfo.html): IP address based configurations.
- [ManagementPreference](https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_ManagementPreference.html): Preferences for migrating an application to AWS.
- [NetworkInfo](https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_NetworkInfo.html): Information about the server's network for which the assessment was run.
- [NoDatabaseMigrationPreference](https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_NoDatabaseMigrationPreference.html): The object containing details about database migration preferences, when you have no particular preference.
- [NoManagementPreference](https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_NoManagementPreference.html): Object containing the choice of application destination that you specify.
- [OSInfo](https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_OSInfo.html): Information about the operating system.
- [PipelineInfo](https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_PipelineInfo.html): Detailed information of the pipeline.
- [PrioritizeBusinessGoals](https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_PrioritizeBusinessGoals.html): Rank of business goals based on priority.
- [RecommendationReportDetails](https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_RecommendationReportDetails.html): Contains detailed information about a recommendation report.
- [RecommendationSet](https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_RecommendationSet.html): Contains a recommendation set.
- [RemoteSourceCodeAnalysisServerInfo](https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_RemoteSourceCodeAnalysisServerInfo.html): Information about the server configured for source code analysis.
- [Result](https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_Result.html): The error in server analysis.
- [S3Object](https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_S3Object.html): Contains the S3 bucket name and the Amazon S3 key name.
- [SelfManageResources](https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_SelfManageResources.html): Self-managed resources.
- [ServerDetail](https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_ServerDetail.html): Detailed information about a server.
- [ServerError](https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_ServerError.html): The error in server analysis.
- [ServerStatusSummary](https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_ServerStatusSummary.html): The status summary of the server analysis.
- [ServerStrategy](https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_ServerStrategy.html): Contains information about a strategy recommendation for a server.
- [ServerSummary](https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_ServerSummary.html): Object containing details about the servers imported by Application Discovery Service
- [SourceCode](https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_SourceCode.html): Object containing source code information that is linked to an application component.
- [SourceCodeRepository](https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_SourceCodeRepository.html): Object containing source code information that is linked to an application component.
- [StrategyOption](https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_StrategyOption.html): Information about all the available strategy options for migrating and modernizing an application component.
- [StrategySummary](https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_StrategySummary.html): Object containing the summary of the strategy recommendations.
- [SystemInfo](https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_SystemInfo.html): Information about the server that hosts application components.
- [TransformationTool](https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_TransformationTool.html): Information of the transformation tool that can be used to migrate and modernize the application.
- [VcenterBasedRemoteInfo](https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_VcenterBasedRemoteInfo.html): Details about the server in vCenter.
- [VersionControlInfo](https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_VersionControlInfo.html): Details about the version control configuration.
