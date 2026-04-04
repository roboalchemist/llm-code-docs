# Source: https://docs.aws.amazon.com/codebuild/latest/APIReference/llms.txt

# AWS CodeBuild API Reference

> AWS CodeBuild is a fully managed build service in the cloud.

- [Welcome](https://docs.aws.amazon.com/codebuild/latest/APIReference/Welcome.html)
- [Common Parameters](https://docs.aws.amazon.com/codebuild/latest/APIReference/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/codebuild/latest/APIReference/CommonErrors.html)

## [Actions](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_Operations.html)

- [BatchDeleteBuilds](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_BatchDeleteBuilds.html): Deletes one or more builds.
- [BatchGetBuildBatches](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_BatchGetBuildBatches.html): Retrieves information about one or more batch builds.
- [BatchGetBuilds](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_BatchGetBuilds.html): Gets information about one or more builds.
- [BatchGetCommandExecutions](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_BatchGetCommandExecutions.html): Gets information about the command executions.
- [BatchGetFleets](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_BatchGetFleets.html): Gets information about one or more compute fleets.
- [BatchGetProjects](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_BatchGetProjects.html): Gets information about one or more build projects.
- [BatchGetReportGroups](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_BatchGetReportGroups.html): Returns an array of report groups.
- [BatchGetReports](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_BatchGetReports.html): Returns an array of reports.
- [BatchGetSandboxes](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_BatchGetSandboxes.html): Gets information about the sandbox status.
- [CreateFleet](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_CreateFleet.html): Creates a compute fleet.
- [CreateProject](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_CreateProject.html): Creates a build project.
- [CreateReportGroup](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_CreateReportGroup.html): Creates a report group.
- [CreateWebhook](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_CreateWebhook.html): For an existing AWS CodeBuild build project that has its source code stored in a GitHub or Bitbucket repository, enables AWS CodeBuild to start rebuilding the source code every time a code change is pushed to the repository.
- [DeleteBuildBatch](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_DeleteBuildBatch.html): Deletes a batch build.
- [DeleteFleet](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_DeleteFleet.html): Deletes a compute fleet.
- [DeleteProject](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_DeleteProject.html): Deletes a build project.
- [DeleteReport](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_DeleteReport.html): Deletes a report.
- [DeleteReportGroup](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_DeleteReportGroup.html): Deletes a report group.
- [DeleteResourcePolicy](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_DeleteResourcePolicy.html): Deletes a resource policy that is identified by its resource ARN.
- [DeleteSourceCredentials](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_DeleteSourceCredentials.html): Deletes a set of GitHub, GitHub Enterprise, or Bitbucket source credentials.
- [DeleteWebhook](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_DeleteWebhook.html): For an existing AWS CodeBuild build project that has its source code stored in a GitHub or Bitbucket repository, stops AWS CodeBuild from rebuilding the source code every time a code change is pushed to the repository.
- [DescribeCodeCoverages](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_DescribeCodeCoverages.html): Retrieves one or more code coverage reports.
- [DescribeTestCases](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_DescribeTestCases.html): Returns a list of details about test cases for a report.
- [GetReportGroupTrend](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_GetReportGroupTrend.html): Analyzes and accumulates test report values for the specified test reports.
- [GetResourcePolicy](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_GetResourcePolicy.html): Gets a resource policy that is identified by its resource ARN.
- [ImportSourceCredentials](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_ImportSourceCredentials.html): Imports the source repository credentials for an AWS CodeBuild project that has its source code stored in a GitHub, GitHub Enterprise, GitLab, GitLab Self Managed, or Bitbucket repository.
- [InvalidateProjectCache](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_InvalidateProjectCache.html): Resets the cache for a project.
- [ListBuildBatches](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_ListBuildBatches.html): Retrieves the identifiers of your build batches in the current region.
- [ListBuildBatchesForProject](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_ListBuildBatchesForProject.html): Retrieves the identifiers of the build batches for a specific project.
- [ListBuilds](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_ListBuilds.html): Gets a list of build IDs, with each build ID representing a single build.
- [ListBuildsForProject](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_ListBuildsForProject.html): Gets a list of build identifiers for the specified build project, with each build identifier representing a single build.
- [ListCommandExecutionsForSandbox](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_ListCommandExecutionsForSandbox.html): Gets a list of command executions for a sandbox.
- [ListCuratedEnvironmentImages](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_ListCuratedEnvironmentImages.html): Gets information about Docker images that are managed by AWS CodeBuild.
- [ListFleets](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_ListFleets.html): Gets a list of compute fleet names with each compute fleet name representing a single compute fleet.
- [ListProjects](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_ListProjects.html): Gets a list of build project names, with each build project name representing a single build project.
- [ListReportGroups](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_ListReportGroups.html): Gets a list ARNs for the report groups in the current AWS account.
- [ListReports](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_ListReports.html): Returns a list of ARNs for the reports in the current AWS account.
- [ListReportsForReportGroup](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_ListReportsForReportGroup.html): Returns a list of ARNs for the reports that belong to a ReportGroup.
- [ListSandboxes](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_ListSandboxes.html): Gets a list of sandboxes.
- [ListSandboxesForProject](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_ListSandboxesForProject.html): Gets a list of sandboxes for a given project.
- [ListSharedProjects](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_ListSharedProjects.html): Gets a list of projects that are shared with other AWS accounts or users.
- [ListSharedReportGroups](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_ListSharedReportGroups.html): Gets a list of report groups that are shared with other AWS accounts or users.
- [ListSourceCredentials](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_ListSourceCredentials.html): Returns a list of SourceCredentialsInfo objects.
- [PutResourcePolicy](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_PutResourcePolicy.html): Stores a resource policy for the ARN of a Project or ReportGroup object.
- [RetryBuild](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_RetryBuild.html): Restarts a build.
- [RetryBuildBatch](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_RetryBuildBatch.html): Restarts a failed batch build.
- [StartBuild](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_StartBuild.html): Starts running a build with the settings defined in the project.
- [StartBuildBatch](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_StartBuildBatch.html): Starts a batch build for a project.
- [StartCommandExecution](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_StartCommandExecution.html): Starts a command execution.
- [StartSandbox](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_StartSandbox.html): Starts a sandbox.
- [StartSandboxConnection](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_StartSandboxConnection.html): Starts a sandbox connection.
- [StopBuild](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_StopBuild.html): Attempts to stop running a build.
- [StopBuildBatch](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_StopBuildBatch.html): Stops a running batch build.
- [StopSandbox](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_StopSandbox.html): Stops a sandbox.
- [UpdateFleet](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_UpdateFleet.html): Updates a compute fleet.
- [UpdateProject](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_UpdateProject.html): Changes the settings of a build project.
- [UpdateProjectVisibility](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_UpdateProjectVisibility.html): Changes the public visibility for a project.
- [UpdateReportGroup](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_UpdateReportGroup.html): Updates a report group.
- [UpdateWebhook](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_UpdateWebhook.html): Updates the webhook associated with an AWS CodeBuild build project.


## [Data Types](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_Types.html)

- [AutoRetryConfig](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_AutoRetryConfig.html): Information about the auto-retry configuration for the build.
- [BatchRestrictions](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_BatchRestrictions.html): Specifies restrictions for the batch build.
- [Build](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_Build.html): Information about a build.
- [BuildArtifacts](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_BuildArtifacts.html): Information about build output artifacts.
- [BuildBatch](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_BuildBatch.html): Contains information about a batch build.
- [BuildBatchFilter](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_BuildBatchFilter.html): Specifies filters when retrieving batch builds.
- [BuildBatchPhase](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_BuildBatchPhase.html): Contains information about a stage for a batch build.
- [BuildGroup](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_BuildGroup.html): Contains information about a batch build build group.
- [BuildNotDeleted](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_BuildNotDeleted.html): Information about a build that could not be successfully deleted.
- [BuildPhase](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_BuildPhase.html): Information about a stage for a build.
- [BuildStatusConfig](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_BuildStatusConfig.html): Contains information that defines how the AWS CodeBuild build project reports the build status to the source provider.
- [BuildSummary](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_BuildSummary.html): Contains summary information about a batch build group.
- [CloudWatchLogsConfig](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_CloudWatchLogsConfig.html): Information about CloudWatch Logs for a build project.
- [CodeCoverage](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_CodeCoverage.html): Contains code coverage report information.
- [CodeCoverageReportSummary](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_CodeCoverageReportSummary.html): Contains a summary of a code coverage report.
- [CommandExecution](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_CommandExecution.html): Contains command execution information.
- [ComputeConfiguration](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_ComputeConfiguration.html): Contains compute attributes.
- [DebugSession](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_DebugSession.html): Contains information about the debug session for a build.
- [DockerServer](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_DockerServer.html): Contains docker server information.
- [DockerServerStatus](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_DockerServerStatus.html): Contains information about the status of the docker server.
- [EnvironmentImage](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_EnvironmentImage.html): Information about a Docker image that is managed by AWS CodeBuild.
- [EnvironmentLanguage](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_EnvironmentLanguage.html): A set of Docker images that are related by programming language and are managed by AWS CodeBuild.
- [EnvironmentPlatform](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_EnvironmentPlatform.html): A set of Docker images that are related by platform and are managed by AWS CodeBuild.
- [EnvironmentVariable](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_EnvironmentVariable.html): Information about an environment variable for a build project or a build.
- [ExportedEnvironmentVariable](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_ExportedEnvironmentVariable.html): Contains information about an exported environment variable.
- [Fleet](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_Fleet.html): A set of dedicated instances for your build environment.
- [FleetProxyRule](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_FleetProxyRule.html): Information about the proxy rule for your reserved capacity instances.
- [FleetStatus](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_FleetStatus.html): The status of the compute fleet.
- [GitSubmodulesConfig](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_GitSubmodulesConfig.html): Information about the Git submodules configuration for an AWS CodeBuild build project.
- [LogsConfig](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_LogsConfig.html): Information about logs for a build project.
- [LogsLocation](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_LogsLocation.html): Information about build logs in CloudWatch Logs.
- [NetworkInterface](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_NetworkInterface.html): Describes a network interface.
- [PhaseContext](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_PhaseContext.html): Additional information about a build phase that has an error.
- [Project](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_Project.html): Information about a build project.
- [ProjectArtifacts](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_ProjectArtifacts.html): Information about the build output artifacts for the build project.
- [ProjectBadge](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_ProjectBadge.html): Information about the build badge for the build project.
- [ProjectBuildBatchConfig](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_ProjectBuildBatchConfig.html): Contains configuration information about a batch build project.
- [ProjectCache](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_ProjectCache.html): Information about the cache for the build project.
- [ProjectEnvironment](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_ProjectEnvironment.html): Information about the build environment of the build project.
- [ProjectFileSystemLocation](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_ProjectFileSystemLocation.html): Information about a file system created by Amazon Elastic File System (EFS).
- [ProjectFleet](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_ProjectFleet.html): Information about the compute fleet of the build project.
- [ProjectSource](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_ProjectSource.html): Information about the build input source code for the build project.
- [ProjectSourceVersion](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_ProjectSourceVersion.html): A source identifier and its corresponding version.
- [ProxyConfiguration](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_ProxyConfiguration.html): Information about the proxy configurations that apply network access control to your reserved capacity instances.
- [PullRequestBuildPolicy](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_PullRequestBuildPolicy.html): A PullRequestBuildPolicy object that defines comment-based approval requirements for triggering builds on pull requests.
- [RegistryCredential](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_RegistryCredential.html): Information about credentials that provide access to a private Docker registry.
- [Report](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_Report.html): Information about the results from running a series of test cases during the run of a build project.
- [ReportExportConfig](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_ReportExportConfig.html): Information about the location where the run of a report is exported.
- [ReportFilter](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_ReportFilter.html): A filter used to return reports with the status specified by the input status parameter.
- [ReportGroup](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_ReportGroup.html): A series of reports.
- [ReportGroupTrendStats](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_ReportGroupTrendStats.html): Contains trend statistics for a set of reports.
- [ReportWithRawData](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_ReportWithRawData.html): Contains the unmodified data for the report.
- [ResolvedArtifact](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_ResolvedArtifact.html): Represents a resolved build artifact.
- [S3LogsConfig](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_S3LogsConfig.html): Information about S3 logs for a build project.
- [S3ReportExportConfig](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_S3ReportExportConfig.html): Information about the S3 bucket where the raw data of a report are exported.
- [Sandbox](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_Sandbox.html): Contains sandbox information.
- [SandboxSession](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_SandboxSession.html): Contains information about the sandbox session.
- [SandboxSessionPhase](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_SandboxSessionPhase.html): Contains information about the sandbox phase.
- [ScalingConfigurationInput](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_ScalingConfigurationInput.html): The scaling configuration input of a compute fleet.
- [ScalingConfigurationOutput](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_ScalingConfigurationOutput.html): The scaling configuration output of a compute fleet.
- [ScopeConfiguration](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_ScopeConfiguration.html): Contains configuration information about the scope for a webhook.
- [SourceAuth](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_SourceAuth.html): Information about the authorization settings for AWS CodeBuild to access the source code to be built.
- [SourceCredentialsInfo](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_SourceCredentialsInfo.html): Information about the credentials for a GitHub, GitHub Enterprise, GitLab, GitLab Self Managed, or Bitbucket repository.
- [SSMSession](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_SSMSession.html): Contains information about the Session Manager session.
- [Tag](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_Tag.html): A tag, consisting of a key and a value.
- [TargetTrackingScalingConfiguration](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_TargetTrackingScalingConfiguration.html): Defines when a new instance is auto-scaled into the compute fleet.
- [TestCase](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_TestCase.html): Information about a test case created using a framework such as NUnit or Cucumber.
- [TestCaseFilter](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_TestCaseFilter.html): A filter used to return specific types of test cases.
- [TestReportSummary](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_TestReportSummary.html): Information about a test report.
- [VpcConfig](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_VpcConfig.html): Information about the VPC configuration that AWS CodeBuild accesses.
- [Webhook](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_Webhook.html): Information about a webhook that connects repository events to a build project in AWS CodeBuild.
- [WebhookFilter](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_WebhookFilter.html): A filter used to determine which webhooks trigger a build.


## [Public build API](https://docs.aws.amazon.com/codebuild/latest/APIReference/public-build.html)

### [Public build actions](https://docs.aws.amazon.com/codebuild/latest/APIReference/public-build-operations.html)

Lists the actions that are supported by the CodeBuild public build API

- [DescribeBuildBatchesForPublicProject](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_DescribeBuildBatchesForPublicProject.html)
- [DescribeBuildsForPublicProject](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_DescribeBuildsForPublicProject.html)
- [GetCloudWatchLogsForPublicBuild](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_GetCloudWatchLogsForPublicBuild.html)
- [GetPresignedUrlsForPublicBuild](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_GetPresignedUrlsForPublicBuild.html)
- [GetPublicBuild](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_GetPublicBuild.html)
- [GetPublicBuildBatch](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_GetPublicBuildBatch.html)
- [GetPublicProject](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_GetPublicProject.html)

### [Public build data types](https://docs.aws.amazon.com/codebuild/latest/APIReference/public-build-types.html)

Lists the data types that are supported by the CodeBuild public build API

- [BuildBatchForDescribeBuildBatchesPublic](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_BuildBatchForDescribeBuildBatchesPublic.html)
- [PublicBuild](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_PublicBuild.html)
- [PublicBuildArtifacts](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_PublicBuildArtifacts.html)
- [PublicBuildBatch](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_PublicBuildBatch.html)
- [PublicBuildGroup](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_PublicBuildGroup.html)
- [PublicBuildSummary](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_PublicBuildSummary.html)
- [PublicLogsStatus](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_PublicLogsStatus.html)
- [PublicProject](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_PublicProject.html)
- [PublicProjectArtifacts](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_PublicProjectArtifacts.html)
- [PublicProjectBuildBatchConfig](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_PublicProjectBuildBatchConfig.html)
- [PublicProjectEnvironment](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_PublicProjectEnvironment.html)
- [PublicProjectSource](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_PublicProjectSource.html)
- [PublicWebhook](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_PublicWebhook.html)
- [S3Downloadable](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_S3Downloadable.html)
