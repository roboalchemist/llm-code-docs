# Source: https://docs.aws.amazon.com/inspector/v2/APIReference/llms.txt

# Inspector Inspector V2 API Reference

> Amazon Inspector is a vulnerability discovery service that automates continuous scanning for security vulnerabilities within your Amazon EC2, Amazon ECR, and AWS Lambda environments.

- [Welcome](https://docs.aws.amazon.com/inspector/v2/APIReference/Welcome.html)
- [Common Parameters](https://docs.aws.amazon.com/inspector/v2/APIReference/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/inspector/v2/APIReference/CommonErrors.html)

## [Actions](https://docs.aws.amazon.com/inspector/v2/APIReference/API_Operations.html)

### [Inspector2](https://docs.aws.amazon.com/inspector/v2/APIReference/API_Operations_Inspector2.html)

The following actions are supported by Inspector2:

- [AssociateMember](https://docs.aws.amazon.com/inspector/v2/APIReference/API_AssociateMember.html): Associates an AWS account with an Amazon Inspector delegated administrator.
- [BatchAssociateCodeSecurityScanConfiguration](https://docs.aws.amazon.com/inspector/v2/APIReference/API_BatchAssociateCodeSecurityScanConfiguration.html): Associates multiple code repositories with an Amazon Inspector code security scan configuration.
- [BatchDisassociateCodeSecurityScanConfiguration](https://docs.aws.amazon.com/inspector/v2/APIReference/API_BatchDisassociateCodeSecurityScanConfiguration.html): Disassociates multiple code repositories from an Amazon Inspector code security scan configuration.
- [BatchGetAccountStatus](https://docs.aws.amazon.com/inspector/v2/APIReference/API_BatchGetAccountStatus.html): Retrieves the Amazon Inspector status of multiple AWS accounts within your environment.
- [BatchGetCodeSnippet](https://docs.aws.amazon.com/inspector/v2/APIReference/API_BatchGetCodeSnippet.html): Retrieves code snippets from findings that Amazon Inspector detected code vulnerabilities in.
- [BatchGetFindingDetails](https://docs.aws.amazon.com/inspector/v2/APIReference/API_BatchGetFindingDetails.html): Gets vulnerability details for findings.
- [BatchGetFreeTrialInfo](https://docs.aws.amazon.com/inspector/v2/APIReference/API_BatchGetFreeTrialInfo.html): Gets free trial status for multiple AWS accounts.
- [BatchGetMemberEc2DeepInspectionStatus](https://docs.aws.amazon.com/inspector/v2/APIReference/API_BatchGetMemberEc2DeepInspectionStatus.html): Retrieves Amazon Inspector deep inspection activation status of multiple member accounts within your organization.
- [BatchUpdateMemberEc2DeepInspectionStatus](https://docs.aws.amazon.com/inspector/v2/APIReference/API_BatchUpdateMemberEc2DeepInspectionStatus.html): Activates or deactivates Amazon Inspector deep inspection for the provided member accounts in your organization.
- [CancelFindingsReport](https://docs.aws.amazon.com/inspector/v2/APIReference/API_CancelFindingsReport.html): Cancels the given findings report.
- [CancelSbomExport](https://docs.aws.amazon.com/inspector/v2/APIReference/API_CancelSbomExport.html): Cancels a software bill of materials (SBOM) report.
- [CreateCisScanConfiguration](https://docs.aws.amazon.com/inspector/v2/APIReference/API_CreateCisScanConfiguration.html): Creates a CIS scan configuration.
- [CreateCodeSecurityIntegration](https://docs.aws.amazon.com/inspector/v2/APIReference/API_CreateCodeSecurityIntegration.html): Creates a code security integration with a source code repository provider.
- [CreateCodeSecurityScanConfiguration](https://docs.aws.amazon.com/inspector/v2/APIReference/API_CreateCodeSecurityScanConfiguration.html): Creates a scan configuration for code security scanning.
- [CreateFilter](https://docs.aws.amazon.com/inspector/v2/APIReference/API_CreateFilter.html): Creates a filter resource using specified filter criteria.
- [CreateFindingsReport](https://docs.aws.amazon.com/inspector/v2/APIReference/API_CreateFindingsReport.html): Creates a finding report.
- [CreateSbomExport](https://docs.aws.amazon.com/inspector/v2/APIReference/API_CreateSbomExport.html): Creates a software bill of materials (SBOM) report.
- [DeleteCisScanConfiguration](https://docs.aws.amazon.com/inspector/v2/APIReference/API_DeleteCisScanConfiguration.html): Deletes a CIS scan configuration.
- [DeleteCodeSecurityIntegration](https://docs.aws.amazon.com/inspector/v2/APIReference/API_DeleteCodeSecurityIntegration.html): Deletes a code security integration.
- [DeleteCodeSecurityScanConfiguration](https://docs.aws.amazon.com/inspector/v2/APIReference/API_DeleteCodeSecurityScanConfiguration.html): Deletes a code security scan configuration.
- [DeleteFilter](https://docs.aws.amazon.com/inspector/v2/APIReference/API_DeleteFilter.html): Deletes a filter resource.
- [DescribeOrganizationConfiguration](https://docs.aws.amazon.com/inspector/v2/APIReference/API_DescribeOrganizationConfiguration.html): Describe Amazon Inspector configuration settings for an AWS organization.
- [Disable](https://docs.aws.amazon.com/inspector/v2/APIReference/API_Disable.html): Disables Amazon Inspector scans for one or more AWS accounts.
- [DisableDelegatedAdminAccount](https://docs.aws.amazon.com/inspector/v2/APIReference/API_DisableDelegatedAdminAccount.html): Disables the Amazon Inspector delegated administrator for your organization.
- [DisassociateMember](https://docs.aws.amazon.com/inspector/v2/APIReference/API_DisassociateMember.html): Disassociates a member account from an Amazon Inspector delegated administrator.
- [Enable](https://docs.aws.amazon.com/inspector/v2/APIReference/API_Enable.html): Enables Amazon Inspector scans for one or more AWS accounts.
- [EnableDelegatedAdminAccount](https://docs.aws.amazon.com/inspector/v2/APIReference/API_EnableDelegatedAdminAccount.html): Enables the Amazon Inspector delegated administrator for your AWS Organizations organization.
- [GetCisScanReport](https://docs.aws.amazon.com/inspector/v2/APIReference/API_GetCisScanReport.html): Retrieves a CIS scan report.
- [GetCisScanResultDetails](https://docs.aws.amazon.com/inspector/v2/APIReference/API_GetCisScanResultDetails.html): Retrieves CIS scan result details.
- [GetClustersForImage](https://docs.aws.amazon.com/inspector/v2/APIReference/API_GetClustersForImage.html): Returns a list of clusters and metadata associated with an image.
- [GetCodeSecurityIntegration](https://docs.aws.amazon.com/inspector/v2/APIReference/API_GetCodeSecurityIntegration.html): Retrieves information about a code security integration.
- [GetCodeSecurityScan](https://docs.aws.amazon.com/inspector/v2/APIReference/API_GetCodeSecurityScan.html): Retrieves information about a specific code security scan.
- [GetCodeSecurityScanConfiguration](https://docs.aws.amazon.com/inspector/v2/APIReference/API_GetCodeSecurityScanConfiguration.html): Retrieves information about a code security scan configuration.
- [GetConfiguration](https://docs.aws.amazon.com/inspector/v2/APIReference/API_GetConfiguration.html): Retrieves setting configurations for Inspector scans.
- [GetDelegatedAdminAccount](https://docs.aws.amazon.com/inspector/v2/APIReference/API_GetDelegatedAdminAccount.html): Retrieves information about the Amazon Inspector delegated administrator for your organization.
- [GetEc2DeepInspectionConfiguration](https://docs.aws.amazon.com/inspector/v2/APIReference/API_GetEc2DeepInspectionConfiguration.html): Retrieves the activation status of Amazon Inspector deep inspection and custom paths associated with your account.
- [GetEncryptionKey](https://docs.aws.amazon.com/inspector/v2/APIReference/API_GetEncryptionKey.html): Gets an encryption key.
- [GetFindingsReportStatus](https://docs.aws.amazon.com/inspector/v2/APIReference/API_GetFindingsReportStatus.html): Gets the status of a findings report.
- [GetMember](https://docs.aws.amazon.com/inspector/v2/APIReference/API_GetMember.html): Gets member information for your organization.
- [GetSbomExport](https://docs.aws.amazon.com/inspector/v2/APIReference/API_GetSbomExport.html): Gets details of a software bill of materials (SBOM) report.
- [ListAccountPermissions](https://docs.aws.amazon.com/inspector/v2/APIReference/API_ListAccountPermissions.html): Lists the permissions an account has to configure Amazon Inspector.
- [ListCisScanConfigurations](https://docs.aws.amazon.com/inspector/v2/APIReference/API_ListCisScanConfigurations.html): Lists CIS scan configurations.
- [ListCisScanResultsAggregatedByChecks](https://docs.aws.amazon.com/inspector/v2/APIReference/API_ListCisScanResultsAggregatedByChecks.html): Lists scan results aggregated by checks.
- [ListCisScanResultsAggregatedByTargetResource](https://docs.aws.amazon.com/inspector/v2/APIReference/API_ListCisScanResultsAggregatedByTargetResource.html): Lists scan results aggregated by a target resource.
- [ListCisScans](https://docs.aws.amazon.com/inspector/v2/APIReference/API_ListCisScans.html): Returns a CIS scan list.
- [ListCodeSecurityIntegrations](https://docs.aws.amazon.com/inspector/v2/APIReference/API_ListCodeSecurityIntegrations.html): Lists all code security integrations in your account.
- [ListCodeSecurityScanConfigurationAssociations](https://docs.aws.amazon.com/inspector/v2/APIReference/API_ListCodeSecurityScanConfigurationAssociations.html): Lists the associations between code repositories and Amazon Inspector code security scan configurations.
- [ListCodeSecurityScanConfigurations](https://docs.aws.amazon.com/inspector/v2/APIReference/API_ListCodeSecurityScanConfigurations.html): Lists all code security scan configurations in your account.
- [ListCoverage](https://docs.aws.amazon.com/inspector/v2/APIReference/API_ListCoverage.html): Lists coverage details for your environment.
- [ListCoverageStatistics](https://docs.aws.amazon.com/inspector/v2/APIReference/API_ListCoverageStatistics.html): Lists Amazon Inspector coverage statistics for your environment.
- [ListDelegatedAdminAccounts](https://docs.aws.amazon.com/inspector/v2/APIReference/API_ListDelegatedAdminAccounts.html): Lists information about the Amazon Inspector delegated administrator of your organization.
- [ListFilters](https://docs.aws.amazon.com/inspector/v2/APIReference/API_ListFilters.html): Lists the filters associated with your account.
- [ListFindingAggregations](https://docs.aws.amazon.com/inspector/v2/APIReference/API_ListFindingAggregations.html): Lists aggregated finding data for your environment based on specific criteria.
- [ListFindings](https://docs.aws.amazon.com/inspector/v2/APIReference/API_ListFindings.html): Lists findings for your environment.
- [ListMembers](https://docs.aws.amazon.com/inspector/v2/APIReference/API_ListMembers.html): List members associated with the Amazon Inspector delegated administrator for your organization.
- [ListTagsForResource](https://docs.aws.amazon.com/inspector/v2/APIReference/API_ListTagsForResource.html): Lists all tags attached to a given resource.
- [ListUsageTotals](https://docs.aws.amazon.com/inspector/v2/APIReference/API_ListUsageTotals.html): Lists the Amazon Inspector usage totals over the last 30 days.
- [ResetEncryptionKey](https://docs.aws.amazon.com/inspector/v2/APIReference/API_ResetEncryptionKey.html): Resets an encryption key.
- [SearchVulnerabilities](https://docs.aws.amazon.com/inspector/v2/APIReference/API_SearchVulnerabilities.html): Lists Amazon Inspector coverage details for a specific vulnerability.
- [SendCisSessionHealth](https://docs.aws.amazon.com/inspector/v2/APIReference/API_SendCisSessionHealth.html): Sends a CIS session health.
- [SendCisSessionTelemetry](https://docs.aws.amazon.com/inspector/v2/APIReference/API_SendCisSessionTelemetry.html): Sends a CIS session telemetry.
- [StartCisSession](https://docs.aws.amazon.com/inspector/v2/APIReference/API_StartCisSession.html): Starts a CIS session.
- [StartCodeSecurityScan](https://docs.aws.amazon.com/inspector/v2/APIReference/API_StartCodeSecurityScan.html): Initiates a code security scan on a specified repository.
- [StopCisSession](https://docs.aws.amazon.com/inspector/v2/APIReference/API_StopCisSession.html): Stops a CIS session.
- [TagResource](https://docs.aws.amazon.com/inspector/v2/APIReference/API_TagResource.html): Adds tags to a resource.
- [UntagResource](https://docs.aws.amazon.com/inspector/v2/APIReference/API_UntagResource.html): Removes tags from a resource.
- [UpdateCisScanConfiguration](https://docs.aws.amazon.com/inspector/v2/APIReference/API_UpdateCisScanConfiguration.html): Updates a CIS scan configuration.
- [UpdateCodeSecurityIntegration](https://docs.aws.amazon.com/inspector/v2/APIReference/API_UpdateCodeSecurityIntegration.html): Updates an existing code security integration.
- [UpdateCodeSecurityScanConfiguration](https://docs.aws.amazon.com/inspector/v2/APIReference/API_UpdateCodeSecurityScanConfiguration.html): Updates an existing code security scan configuration.
- [UpdateConfiguration](https://docs.aws.amazon.com/inspector/v2/APIReference/API_UpdateConfiguration.html): Updates setting configurations for your Amazon Inspector account.
- [UpdateEc2DeepInspectionConfiguration](https://docs.aws.amazon.com/inspector/v2/APIReference/API_UpdateEc2DeepInspectionConfiguration.html): Activates, deactivates Amazon Inspector deep inspection, or updates custom paths for your account.
- [UpdateEncryptionKey](https://docs.aws.amazon.com/inspector/v2/APIReference/API_UpdateEncryptionKey.html): Updates an encryption key.
- [UpdateFilter](https://docs.aws.amazon.com/inspector/v2/APIReference/API_UpdateFilter.html): Specifies the action that is to be applied to the findings that match the filter.
- [UpdateOrganizationConfiguration](https://docs.aws.amazon.com/inspector/v2/APIReference/API_UpdateOrganizationConfiguration.html): Updates the configurations for your Amazon Inspector organization.
- [UpdateOrgEc2DeepInspectionConfiguration](https://docs.aws.amazon.com/inspector/v2/APIReference/API_UpdateOrgEc2DeepInspectionConfiguration.html): Updates the Amazon Inspector deep inspection custom paths for your organization.

### [Inspector Scan](https://docs.aws.amazon.com/inspector/v2/APIReference/API_Operations_Inspector_Scan.html)

The following actions are supported by Inspector Scan:

- [ScanSbom](https://docs.aws.amazon.com/inspector/v2/APIReference/API_scan_ScanSbom.html): Scans a provided CycloneDX 1.5 SBOM and reports on any discovered vulnerabilities.


## [Data Types](https://docs.aws.amazon.com/inspector/v2/APIReference/API_Types.html)

### [Inspector2](https://docs.aws.amazon.com/inspector/v2/APIReference/API_Types_Inspector2.html)

The following data types are supported by Inspector2:

- [Account](https://docs.aws.amazon.com/inspector/v2/APIReference/API_Account.html): An AWS account within your environment that Amazon Inspector has been enabled for.
- [AccountAggregation](https://docs.aws.amazon.com/inspector/v2/APIReference/API_AccountAggregation.html): An object that contains details about an aggregation response based on AWS accounts.
- [AccountAggregationResponse](https://docs.aws.amazon.com/inspector/v2/APIReference/API_AccountAggregationResponse.html): An aggregation of findings by AWS account ID.
- [AccountState](https://docs.aws.amazon.com/inspector/v2/APIReference/API_AccountState.html): An object with details the status of an AWS account within your Amazon Inspector environment.
- [AggregationRequest](https://docs.aws.amazon.com/inspector/v2/APIReference/API_AggregationRequest.html): Contains details about an aggregation request.
- [AggregationResponse](https://docs.aws.amazon.com/inspector/v2/APIReference/API_AggregationResponse.html): A structure that contains details about the results of an aggregation type.
- [AmiAggregation](https://docs.aws.amazon.com/inspector/v2/APIReference/API_AmiAggregation.html): The details that define an aggregation based on Amazon machine images (AMIs).
- [AmiAggregationResponse](https://docs.aws.amazon.com/inspector/v2/APIReference/API_AmiAggregationResponse.html): A response that contains the results of a finding aggregation by AMI.
- [AssociateConfigurationRequest](https://docs.aws.amazon.com/inspector/v2/APIReference/API_AssociateConfigurationRequest.html): Contains details about a request to associate a code repository with a scan configuration.
- [AtigData](https://docs.aws.amazon.com/inspector/v2/APIReference/API_AtigData.html): The Amazon Web Services Threat Intel Group (ATIG) details for a specific vulnerability.
- [AutoEnable](https://docs.aws.amazon.com/inspector/v2/APIReference/API_AutoEnable.html): Represents which scan types are automatically enabled for new members of your Amazon Inspector organization.
- [AwsEc2InstanceDetails](https://docs.aws.amazon.com/inspector/v2/APIReference/API_AwsEc2InstanceDetails.html): Details of the Amazon EC2 instance involved in a finding.
- [AwsEcrContainerAggregation](https://docs.aws.amazon.com/inspector/v2/APIReference/API_AwsEcrContainerAggregation.html): An aggregation of information about Amazon ECR containers.
- [AwsEcrContainerAggregationResponse](https://docs.aws.amazon.com/inspector/v2/APIReference/API_AwsEcrContainerAggregationResponse.html): An aggregation of information about Amazon ECR containers.
- [AwsEcrContainerImageDetails](https://docs.aws.amazon.com/inspector/v2/APIReference/API_AwsEcrContainerImageDetails.html): The image details of the Amazon ECR container image.
- [AwsEcsMetadataDetails](https://docs.aws.amazon.com/inspector/v2/APIReference/API_AwsEcsMetadataDetails.html): Metadata about tasks where an image was in use.
- [AwsEksMetadataDetails](https://docs.aws.amazon.com/inspector/v2/APIReference/API_AwsEksMetadataDetails.html): The metadata for an Amazon EKS pod where an Amazon ECR image is in use.
- [AwsEksWorkloadInfo](https://docs.aws.amazon.com/inspector/v2/APIReference/API_AwsEksWorkloadInfo.html): Information about the workload.
- [AwsLambdaFunctionDetails](https://docs.aws.amazon.com/inspector/v2/APIReference/API_AwsLambdaFunctionDetails.html): A summary of information about the AWS Lambda function.
- [CisaData](https://docs.aws.amazon.com/inspector/v2/APIReference/API_CisaData.html): The Cybersecurity and Infrastructure Security Agency (CISA) details for a specific vulnerability.
- [CisCheckAggregation](https://docs.aws.amazon.com/inspector/v2/APIReference/API_CisCheckAggregation.html): A CIS check.
- [CisDateFilter](https://docs.aws.amazon.com/inspector/v2/APIReference/API_CisDateFilter.html): The CIS date filter.
- [CisFindingStatusFilter](https://docs.aws.amazon.com/inspector/v2/APIReference/API_CisFindingStatusFilter.html): The CIS finding status filter.
- [CisNumberFilter](https://docs.aws.amazon.com/inspector/v2/APIReference/API_CisNumberFilter.html): The CIS number filter.
- [CisResultStatusFilter](https://docs.aws.amazon.com/inspector/v2/APIReference/API_CisResultStatusFilter.html): The CIS result status filter.
- [CisScan](https://docs.aws.amazon.com/inspector/v2/APIReference/API_CisScan.html): The CIS scan.
- [CisScanConfiguration](https://docs.aws.amazon.com/inspector/v2/APIReference/API_CisScanConfiguration.html): The CIS scan configuration.
- [CisScanResultDetails](https://docs.aws.amazon.com/inspector/v2/APIReference/API_CisScanResultDetails.html): The CIS scan result details.
- [CisScanResultDetailsFilterCriteria](https://docs.aws.amazon.com/inspector/v2/APIReference/API_CisScanResultDetailsFilterCriteria.html): The CIS scan result details filter criteria.
- [CisScanResultsAggregatedByChecksFilterCriteria](https://docs.aws.amazon.com/inspector/v2/APIReference/API_CisScanResultsAggregatedByChecksFilterCriteria.html): The scan results aggregated by checks filter criteria.
- [CisScanResultsAggregatedByTargetResourceFilterCriteria](https://docs.aws.amazon.com/inspector/v2/APIReference/API_CisScanResultsAggregatedByTargetResourceFilterCriteria.html): The scan results aggregated by target resource filter criteria.
- [CisScanStatusFilter](https://docs.aws.amazon.com/inspector/v2/APIReference/API_CisScanStatusFilter.html): The CIS scan status filter.
- [CisSecurityLevelFilter](https://docs.aws.amazon.com/inspector/v2/APIReference/API_CisSecurityLevelFilter.html): The CIS security level filter.
- [CisSessionMessage](https://docs.aws.amazon.com/inspector/v2/APIReference/API_CisSessionMessage.html): The CIS session message.
- [CisStringFilter](https://docs.aws.amazon.com/inspector/v2/APIReference/API_CisStringFilter.html): The CIS string filter.
- [CisTargetResourceAggregation](https://docs.aws.amazon.com/inspector/v2/APIReference/API_CisTargetResourceAggregation.html): The CIS target resource aggregation.
- [CisTargets](https://docs.aws.amazon.com/inspector/v2/APIReference/API_CisTargets.html): The CIS targets.
- [CisTargetStatusFilter](https://docs.aws.amazon.com/inspector/v2/APIReference/API_CisTargetStatusFilter.html): The CIS target status filter.
- [CisTargetStatusReasonFilter](https://docs.aws.amazon.com/inspector/v2/APIReference/API_CisTargetStatusReasonFilter.html): The CIS target status reason filter.
- [ClusterDetails](https://docs.aws.amazon.com/inspector/v2/APIReference/API_ClusterDetails.html): Details about the task or pod in the cluster.
- [ClusterForImageFilterCriteria](https://docs.aws.amazon.com/inspector/v2/APIReference/API_ClusterForImageFilterCriteria.html): The filter criteria to be used.
- [ClusterInformation](https://docs.aws.amazon.com/inspector/v2/APIReference/API_ClusterInformation.html): Information about the cluster.
- [ClusterMetadata](https://docs.aws.amazon.com/inspector/v2/APIReference/API_ClusterMetadata.html): The metadata for a cluster.
- [CodeFilePath](https://docs.aws.amazon.com/inspector/v2/APIReference/API_CodeFilePath.html): Contains information on where a code vulnerability is located in your Lambda function.
- [CodeLine](https://docs.aws.amazon.com/inspector/v2/APIReference/API_CodeLine.html): Contains information on the lines of code associated with a code snippet.
- [CodeRepositoryAggregation](https://docs.aws.amazon.com/inspector/v2/APIReference/API_CodeRepositoryAggregation.html): The details that define an aggregation based on code repositories.
- [CodeRepositoryAggregationResponse](https://docs.aws.amazon.com/inspector/v2/APIReference/API_CodeRepositoryAggregationResponse.html): A response that contains the results of a finding aggregation by code repository.
- [CodeRepositoryDetails](https://docs.aws.amazon.com/inspector/v2/APIReference/API_CodeRepositoryDetails.html): Contains details about a code repository associated with a finding.
- [CodeRepositoryMetadata](https://docs.aws.amazon.com/inspector/v2/APIReference/API_CodeRepositoryMetadata.html): Contains metadata information about a code repository that is being scanned by Amazon Inspector.
- [CodeRepositoryOnDemandScan](https://docs.aws.amazon.com/inspector/v2/APIReference/API_CodeRepositoryOnDemandScan.html): Contains information about on-demand scans performed on a code repository.
- [CodeSecurityIntegrationSummary](https://docs.aws.amazon.com/inspector/v2/APIReference/API_CodeSecurityIntegrationSummary.html): A summary of information about a code security integration.
- [CodeSecurityResource](https://docs.aws.amazon.com/inspector/v2/APIReference/API_CodeSecurityResource.html): Identifies a specific resource in a code repository that will be scanned.
- [CodeSecurityScanConfiguration](https://docs.aws.amazon.com/inspector/v2/APIReference/API_CodeSecurityScanConfiguration.html): Contains the configuration settings for code security scans.
- [CodeSecurityScanConfigurationAssociationSummary](https://docs.aws.amazon.com/inspector/v2/APIReference/API_CodeSecurityScanConfigurationAssociationSummary.html): A summary of an association between a code repository and a scan configuration.
- [CodeSecurityScanConfigurationSummary](https://docs.aws.amazon.com/inspector/v2/APIReference/API_CodeSecurityScanConfigurationSummary.html): A summary of information about a code security scan configuration.
- [CodeSnippetError](https://docs.aws.amazon.com/inspector/v2/APIReference/API_CodeSnippetError.html): Contains information about any errors encountered while trying to retrieve a code snippet.
- [CodeSnippetResult](https://docs.aws.amazon.com/inspector/v2/APIReference/API_CodeSnippetResult.html): Contains information on a code snippet retrieved by Amazon Inspector from a code vulnerability finding.
- [CodeVulnerabilityDetails](https://docs.aws.amazon.com/inspector/v2/APIReference/API_CodeVulnerabilityDetails.html): Contains information on the code vulnerability identified in your Lambda function.
- [ComputePlatform](https://docs.aws.amazon.com/inspector/v2/APIReference/API_ComputePlatform.html): A compute platform.
- [ContinuousIntegrationScanConfiguration](https://docs.aws.amazon.com/inspector/v2/APIReference/API_ContinuousIntegrationScanConfiguration.html): Configuration settings for continuous integration scans that run automatically when code changes are made.
- [Counts](https://docs.aws.amazon.com/inspector/v2/APIReference/API_Counts.html): a structure that contains information on the count of resources within a group.
- [CoverageDateFilter](https://docs.aws.amazon.com/inspector/v2/APIReference/API_CoverageDateFilter.html): Contains details of a coverage date filter.
- [CoverageFilterCriteria](https://docs.aws.amazon.com/inspector/v2/APIReference/API_CoverageFilterCriteria.html): A structure that identifies filter criteria for GetCoverageStatistics.
- [CoverageMapFilter](https://docs.aws.amazon.com/inspector/v2/APIReference/API_CoverageMapFilter.html): Contains details of a coverage map filter.
- [CoverageNumberFilter](https://docs.aws.amazon.com/inspector/v2/APIReference/API_CoverageNumberFilter.html): The coverage number to be used in the filter.
- [CoverageStringFilter](https://docs.aws.amazon.com/inspector/v2/APIReference/API_CoverageStringFilter.html): Contains details of a coverage string filter.
- [CoveredResource](https://docs.aws.amazon.com/inspector/v2/APIReference/API_CoveredResource.html): An object that contains details about a resource covered by Amazon Inspector.
- [CreateCisTargets](https://docs.aws.amazon.com/inspector/v2/APIReference/API_CreateCisTargets.html): Creates CIS targets.
- [CreateGitLabSelfManagedIntegrationDetail](https://docs.aws.amazon.com/inspector/v2/APIReference/API_CreateGitLabSelfManagedIntegrationDetail.html): Contains details required to create an integration with a self-managed GitLab instance.
- [CreateIntegrationDetail](https://docs.aws.amazon.com/inspector/v2/APIReference/API_CreateIntegrationDetail.html): Contains details required to create a code security integration with a specific repository provider.
- [Cvss2](https://docs.aws.amazon.com/inspector/v2/APIReference/API_Cvss2.html): The Common Vulnerability Scoring System (CVSS) version 2 details for the vulnerability.
- [Cvss3](https://docs.aws.amazon.com/inspector/v2/APIReference/API_Cvss3.html): The Common Vulnerability Scoring System (CVSS) version 3 details for the vulnerability.
- [Cvss4](https://docs.aws.amazon.com/inspector/v2/APIReference/API_Cvss4.html): The Common Vulnerability Scoring System (CVSS) version 4 details for the vulnerability.
- [CvssScore](https://docs.aws.amazon.com/inspector/v2/APIReference/API_CvssScore.html): The CVSS score for a finding.
- [CvssScoreAdjustment](https://docs.aws.amazon.com/inspector/v2/APIReference/API_CvssScoreAdjustment.html): Details on adjustments Amazon Inspector made to the CVSS score for a finding.
- [CvssScoreDetails](https://docs.aws.amazon.com/inspector/v2/APIReference/API_CvssScoreDetails.html): Information about the CVSS score.
- [DailySchedule](https://docs.aws.amazon.com/inspector/v2/APIReference/API_DailySchedule.html): A daily schedule.
- [DateFilter](https://docs.aws.amazon.com/inspector/v2/APIReference/API_DateFilter.html): Contains details on the time range used to filter findings.
- [DelegatedAdmin](https://docs.aws.amazon.com/inspector/v2/APIReference/API_DelegatedAdmin.html): Details of the Amazon Inspector delegated administrator for your organization.
- [DelegatedAdminAccount](https://docs.aws.amazon.com/inspector/v2/APIReference/API_DelegatedAdminAccount.html): Details of the Amazon Inspector delegated administrator for your organization.
- [Destination](https://docs.aws.amazon.com/inspector/v2/APIReference/API_Destination.html): Contains details of the Amazon S3 bucket and AWS KMS key used to export findings.
- [DisassociateConfigurationRequest](https://docs.aws.amazon.com/inspector/v2/APIReference/API_DisassociateConfigurationRequest.html): Contains details about a request to disassociate a code repository from a scan configuration.
- [Ec2Configuration](https://docs.aws.amazon.com/inspector/v2/APIReference/API_Ec2Configuration.html): Enables agent-based scanning, which scans instances that are not managed by SSM.
- [Ec2ConfigurationState](https://docs.aws.amazon.com/inspector/v2/APIReference/API_Ec2ConfigurationState.html): Details about the state of the EC2 scan configuration for your environment.
- [Ec2InstanceAggregation](https://docs.aws.amazon.com/inspector/v2/APIReference/API_Ec2InstanceAggregation.html): The details that define an aggregation based on Amazon EC2 instances.
- [Ec2InstanceAggregationResponse](https://docs.aws.amazon.com/inspector/v2/APIReference/API_Ec2InstanceAggregationResponse.html): A response that contains the results of a finding aggregation by Amazon EC2 instance.
- [Ec2Metadata](https://docs.aws.amazon.com/inspector/v2/APIReference/API_Ec2Metadata.html): Meta data details of an Amazon EC2 instance.
- [Ec2ScanModeState](https://docs.aws.amazon.com/inspector/v2/APIReference/API_Ec2ScanModeState.html): The state of your Amazon EC2 scan mode configuration.
- [EcrConfiguration](https://docs.aws.amazon.com/inspector/v2/APIReference/API_EcrConfiguration.html): Details about the ECR automated re-scan duration setting for your environment.
- [EcrConfigurationState](https://docs.aws.amazon.com/inspector/v2/APIReference/API_EcrConfigurationState.html): Details about the state of the ECR scans for your environment.
- [EcrContainerImageMetadata](https://docs.aws.amazon.com/inspector/v2/APIReference/API_EcrContainerImageMetadata.html): Information on the Amazon ECR image metadata associated with a finding.
- [EcrRepositoryMetadata](https://docs.aws.amazon.com/inspector/v2/APIReference/API_EcrRepositoryMetadata.html): Information on the Amazon ECR repository metadata associated with a finding.
- [EcrRescanDurationState](https://docs.aws.amazon.com/inspector/v2/APIReference/API_EcrRescanDurationState.html): Details about the state of your ECR re-scan duration settings.
- [Epss](https://docs.aws.amazon.com/inspector/v2/APIReference/API_Epss.html): Details about the Exploit Prediction Scoring System (EPSS) score.
- [EpssDetails](https://docs.aws.amazon.com/inspector/v2/APIReference/API_EpssDetails.html): Details about the Exploit Prediction Scoring System (EPSS) score for a finding.
- [Evidence](https://docs.aws.amazon.com/inspector/v2/APIReference/API_Evidence.html): Details of the evidence for a vulnerability identified in a finding.
- [ExploitabilityDetails](https://docs.aws.amazon.com/inspector/v2/APIReference/API_ExploitabilityDetails.html): The details of an exploit available for a finding discovered in your environment.
- [ExploitObserved](https://docs.aws.amazon.com/inspector/v2/APIReference/API_ExploitObserved.html): Contains information on when this exploit was observed.
- [FailedAccount](https://docs.aws.amazon.com/inspector/v2/APIReference/API_FailedAccount.html): An object with details on why an account failed to enable Amazon Inspector.
- [FailedAssociationResult](https://docs.aws.amazon.com/inspector/v2/APIReference/API_FailedAssociationResult.html): Details about a failed attempt to associate or disassociate a code repository with a scan configuration.
- [FailedMemberAccountEc2DeepInspectionStatusState](https://docs.aws.amazon.com/inspector/v2/APIReference/API_FailedMemberAccountEc2DeepInspectionStatusState.html): An object that contains details about a member account in your organization that failed to activate Amazon Inspector deep inspection.
- [Filter](https://docs.aws.amazon.com/inspector/v2/APIReference/API_Filter.html): Details about a filter.
- [FilterCriteria](https://docs.aws.amazon.com/inspector/v2/APIReference/API_FilterCriteria.html): Details on the criteria used to define the filter.
- [Finding](https://docs.aws.amazon.com/inspector/v2/APIReference/API_Finding.html): Details about an Amazon Inspector finding.
- [FindingDetail](https://docs.aws.amazon.com/inspector/v2/APIReference/API_FindingDetail.html): Details of the vulnerability identified in a finding.
- [FindingDetailsError](https://docs.aws.amazon.com/inspector/v2/APIReference/API_FindingDetailsError.html): Details about an error encountered when trying to return vulnerability data for a finding.
- [FindingTypeAggregation](https://docs.aws.amazon.com/inspector/v2/APIReference/API_FindingTypeAggregation.html): The details that define an aggregation based on finding type.
- [FindingTypeAggregationResponse](https://docs.aws.amazon.com/inspector/v2/APIReference/API_FindingTypeAggregationResponse.html): A response that contains the results of a finding type aggregation.
- [FreeTrialAccountInfo](https://docs.aws.amazon.com/inspector/v2/APIReference/API_FreeTrialAccountInfo.html): Information about the Amazon Inspector free trial for an account.
- [FreeTrialInfo](https://docs.aws.amazon.com/inspector/v2/APIReference/API_FreeTrialInfo.html): An object that contains information about the Amazon Inspector free trial for an account.
- [FreeTrialInfoError](https://docs.aws.amazon.com/inspector/v2/APIReference/API_FreeTrialInfoError.html): Information about an error received while accessing free trail data for an account.
- [ImageLayerAggregation](https://docs.aws.amazon.com/inspector/v2/APIReference/API_ImageLayerAggregation.html): The details that define an aggregation based on container image layers.
- [ImageLayerAggregationResponse](https://docs.aws.amazon.com/inspector/v2/APIReference/API_ImageLayerAggregationResponse.html): A response that contains the results of a finding aggregation by image layer.
- [InspectorScoreDetails](https://docs.aws.amazon.com/inspector/v2/APIReference/API_InspectorScoreDetails.html): Information about the Amazon Inspector score given to a finding.
- [LambdaFunctionAggregation](https://docs.aws.amazon.com/inspector/v2/APIReference/API_LambdaFunctionAggregation.html): The details that define a findings aggregation based on AWS Lambda functions.
- [LambdaFunctionAggregationResponse](https://docs.aws.amazon.com/inspector/v2/APIReference/API_LambdaFunctionAggregationResponse.html): A response that contains the results of an AWS Lambda function finding aggregation.
- [LambdaFunctionMetadata](https://docs.aws.amazon.com/inspector/v2/APIReference/API_LambdaFunctionMetadata.html): The AWS Lambda function metadata.
- [LambdaLayerAggregation](https://docs.aws.amazon.com/inspector/v2/APIReference/API_LambdaLayerAggregation.html): The details that define a findings aggregation based on an AWS Lambda function's layers.
- [LambdaLayerAggregationResponse](https://docs.aws.amazon.com/inspector/v2/APIReference/API_LambdaLayerAggregationResponse.html): A response that contains the results of an AWS Lambda function layer finding aggregation.
- [LambdaVpcConfig](https://docs.aws.amazon.com/inspector/v2/APIReference/API_LambdaVpcConfig.html): The VPC security groups and subnets that are attached to an AWS Lambda function.
- [ListCisScanConfigurationsFilterCriteria](https://docs.aws.amazon.com/inspector/v2/APIReference/API_ListCisScanConfigurationsFilterCriteria.html): A list of CIS scan configurations filter criteria.
- [ListCisScansFilterCriteria](https://docs.aws.amazon.com/inspector/v2/APIReference/API_ListCisScansFilterCriteria.html): A list of CIS scans filter criteria.
- [MapFilter](https://docs.aws.amazon.com/inspector/v2/APIReference/API_MapFilter.html): An object that describes details of a map filter.
- [Member](https://docs.aws.amazon.com/inspector/v2/APIReference/API_Member.html): Details on a member account in your organization.
- [MemberAccountEc2DeepInspectionStatus](https://docs.aws.amazon.com/inspector/v2/APIReference/API_MemberAccountEc2DeepInspectionStatus.html): An object that contains details about the status of Amazon Inspector deep inspection for a member account in your organization.
- [MemberAccountEc2DeepInspectionStatusState](https://docs.aws.amazon.com/inspector/v2/APIReference/API_MemberAccountEc2DeepInspectionStatusState.html): An object that contains details about the state of Amazon Inspector deep inspection for a member account.
- [MonthlySchedule](https://docs.aws.amazon.com/inspector/v2/APIReference/API_MonthlySchedule.html): A monthly schedule.
- [NetworkPath](https://docs.aws.amazon.com/inspector/v2/APIReference/API_NetworkPath.html): Information on the network path associated with a finding.
- [NetworkReachabilityDetails](https://docs.aws.amazon.com/inspector/v2/APIReference/API_NetworkReachabilityDetails.html): Contains the details of a network reachability finding.
- [NumberFilter](https://docs.aws.amazon.com/inspector/v2/APIReference/API_NumberFilter.html): An object that describes the details of a number filter.
- [OneTimeSchedule](https://docs.aws.amazon.com/inspector/v2/APIReference/API_OneTimeSchedule.html): A one time schedule.
- [PackageAggregation](https://docs.aws.amazon.com/inspector/v2/APIReference/API_PackageAggregation.html): The details that define an aggregation based on operating system package type.
- [PackageAggregationResponse](https://docs.aws.amazon.com/inspector/v2/APIReference/API_PackageAggregationResponse.html): A response that contains the results of a finding aggregation by image layer.
- [PackageFilter](https://docs.aws.amazon.com/inspector/v2/APIReference/API_PackageFilter.html): Contains information on the details of a package filter.
- [PackageVulnerabilityDetails](https://docs.aws.amazon.com/inspector/v2/APIReference/API_PackageVulnerabilityDetails.html): Information about a package vulnerability finding.
- [PeriodicScanConfiguration](https://docs.aws.amazon.com/inspector/v2/APIReference/API_PeriodicScanConfiguration.html): Configuration settings for periodic scans that run on a scheduled basis.
- [Permission](https://docs.aws.amazon.com/inspector/v2/APIReference/API_Permission.html): Contains information on the permissions an account has within Amazon Inspector.
- [PortRange](https://docs.aws.amazon.com/inspector/v2/APIReference/API_PortRange.html): Details about the port range associated with a finding.
- [PortRangeFilter](https://docs.aws.amazon.com/inspector/v2/APIReference/API_PortRangeFilter.html): An object that describes the details of a port range filter.
- [ProjectCodeSecurityScanConfiguration](https://docs.aws.amazon.com/inspector/v2/APIReference/API_ProjectCodeSecurityScanConfiguration.html): Contains the scan configuration settings applied to a specific project in a code repository.
- [ProjectContinuousIntegrationScanConfiguration](https://docs.aws.amazon.com/inspector/v2/APIReference/API_ProjectContinuousIntegrationScanConfiguration.html): Contains the continuous integration scan configuration settings applied to a specific project.
- [ProjectPeriodicScanConfiguration](https://docs.aws.amazon.com/inspector/v2/APIReference/API_ProjectPeriodicScanConfiguration.html): Contains the periodic scan configuration settings applied to a specific project.
- [Recommendation](https://docs.aws.amazon.com/inspector/v2/APIReference/API_Recommendation.html): Details about the recommended course of action to remediate the finding.
- [Remediation](https://docs.aws.amazon.com/inspector/v2/APIReference/API_Remediation.html): Information on how to remediate a finding.
- [RepositoryAggregation](https://docs.aws.amazon.com/inspector/v2/APIReference/API_RepositoryAggregation.html): The details that define an aggregation based on repository.
- [RepositoryAggregationResponse](https://docs.aws.amazon.com/inspector/v2/APIReference/API_RepositoryAggregationResponse.html): A response that contains details on the results of a finding aggregation by repository.
- [Resource](https://docs.aws.amazon.com/inspector/v2/APIReference/API_Resource.html): Details about the resource involved in a finding.
- [ResourceDetails](https://docs.aws.amazon.com/inspector/v2/APIReference/API_ResourceDetails.html): Contains details about the resource involved in the finding.
- [ResourceFilterCriteria](https://docs.aws.amazon.com/inspector/v2/APIReference/API_ResourceFilterCriteria.html): The resource filter criteria for a Software bill of materials (SBOM) report.
- [ResourceMapFilter](https://docs.aws.amazon.com/inspector/v2/APIReference/API_ResourceMapFilter.html): A resource map filter for a software bill of material report.
- [ResourceScanMetadata](https://docs.aws.amazon.com/inspector/v2/APIReference/API_ResourceScanMetadata.html): An object that contains details about the metadata for an Amazon ECR resource.
- [ResourceState](https://docs.aws.amazon.com/inspector/v2/APIReference/API_ResourceState.html): Details the state of Amazon Inspector for each resource type Amazon Inspector scans.
- [ResourceStatus](https://docs.aws.amazon.com/inspector/v2/APIReference/API_ResourceStatus.html): Details the status of Amazon Inspector for each resource type Amazon Inspector scans.
- [ResourceStringFilter](https://docs.aws.amazon.com/inspector/v2/APIReference/API_ResourceStringFilter.html): A resource string filter for a software bill of materials report.
- [ScanStatus](https://docs.aws.amazon.com/inspector/v2/APIReference/API_ScanStatus.html): The status of the scan.
- [Schedule](https://docs.aws.amazon.com/inspector/v2/APIReference/API_Schedule.html): A schedule.
- [ScopeSettings](https://docs.aws.amazon.com/inspector/v2/APIReference/API_ScopeSettings.html): Defines the scope of repositories to be included in code security scans.
- [SearchVulnerabilitiesFilterCriteria](https://docs.aws.amazon.com/inspector/v2/APIReference/API_SearchVulnerabilitiesFilterCriteria.html): Details on the criteria used to define the filter for a vulnerability search.
- [SeverityCounts](https://docs.aws.amazon.com/inspector/v2/APIReference/API_SeverityCounts.html): An object that contains the counts of aggregated finding per severity.
- [SortCriteria](https://docs.aws.amazon.com/inspector/v2/APIReference/API_SortCriteria.html): Details about the criteria used to sort finding results.
- [StartCisSessionMessage](https://docs.aws.amazon.com/inspector/v2/APIReference/API_StartCisSessionMessage.html): The start CIS session message.
- [State](https://docs.aws.amazon.com/inspector/v2/APIReference/API_State.html): An object that described the state of Amazon Inspector scans for an account.
- [StatusCounts](https://docs.aws.amazon.com/inspector/v2/APIReference/API_StatusCounts.html): The status counts.
- [Step](https://docs.aws.amazon.com/inspector/v2/APIReference/API_Step.html): Details about the step associated with a finding.
- [StopCisMessageProgress](https://docs.aws.amazon.com/inspector/v2/APIReference/API_StopCisMessageProgress.html): The stop CIS message progress.
- [StopCisSessionMessage](https://docs.aws.amazon.com/inspector/v2/APIReference/API_StopCisSessionMessage.html): The stop CIS session message.
- [StringFilter](https://docs.aws.amazon.com/inspector/v2/APIReference/API_StringFilter.html): An object that describes the details of a string filter.
- [SuccessfulAssociationResult](https://docs.aws.amazon.com/inspector/v2/APIReference/API_SuccessfulAssociationResult.html): Details about a successful association or disassociation between a code repository and a scan configuration.
- [SuggestedFix](https://docs.aws.amazon.com/inspector/v2/APIReference/API_SuggestedFix.html): A suggested fix for a vulnerability in your Lambda function code.
- [TagFilter](https://docs.aws.amazon.com/inspector/v2/APIReference/API_TagFilter.html): The tag filter.
- [Time](https://docs.aws.amazon.com/inspector/v2/APIReference/API_Time.html): The time.
- [TitleAggregation](https://docs.aws.amazon.com/inspector/v2/APIReference/API_TitleAggregation.html): The details that define an aggregation based on finding title.
- [TitleAggregationResponse](https://docs.aws.amazon.com/inspector/v2/APIReference/API_TitleAggregationResponse.html): A response that contains details on the results of a finding aggregation by title.
- [UpdateCisTargets](https://docs.aws.amazon.com/inspector/v2/APIReference/API_UpdateCisTargets.html): Updates CIS targets.
- [UpdateGitHubIntegrationDetail](https://docs.aws.amazon.com/inspector/v2/APIReference/API_UpdateGitHubIntegrationDetail.html): Contains details required to update an integration with GitHub.
- [UpdateGitLabSelfManagedIntegrationDetail](https://docs.aws.amazon.com/inspector/v2/APIReference/API_UpdateGitLabSelfManagedIntegrationDetail.html): Contains details required to update an integration with a self-managed GitLab instance.
- [UpdateIntegrationDetails](https://docs.aws.amazon.com/inspector/v2/APIReference/API_UpdateIntegrationDetails.html): Contains details required to update a code security integration with a specific repository provider.
- [Usage](https://docs.aws.amazon.com/inspector/v2/APIReference/API_Usage.html): Contains usage information about the cost of Amazon Inspector operation.
- [UsageTotal](https://docs.aws.amazon.com/inspector/v2/APIReference/API_UsageTotal.html): The total of usage for an account ID.
- [ValidationExceptionField](https://docs.aws.amazon.com/inspector/v2/APIReference/API_ValidationExceptionField.html): An object that describes a validation exception.
- [Vulnerability](https://docs.aws.amazon.com/inspector/v2/APIReference/API_Vulnerability.html): Contains details about a specific vulnerability Amazon Inspector can detect.
- [VulnerablePackage](https://docs.aws.amazon.com/inspector/v2/APIReference/API_VulnerablePackage.html): Information on the vulnerable package identified by a finding.
- [WeeklySchedule](https://docs.aws.amazon.com/inspector/v2/APIReference/API_WeeklySchedule.html): A weekly schedule.

### [Inspector Scan](https://docs.aws.amazon.com/inspector/v2/APIReference/API_Types_Inspector_Scan.html)

The following data types are supported by Inspector Scan:

- [ValidationExceptionField](https://docs.aws.amazon.com/inspector/v2/APIReference/API_scan_ValidationExceptionField.html): The request has failed validation due to missing required fields or having invalid inputs.
