# Source: https://docs.aws.amazon.com/application-discovery/latest/APIReference/llms.txt

# AWS Application Discovery Service API Reference

> AWS Application Discovery Service (Application Discovery Service) helps you plan application migration projects. It automatically identifies servers, virtual machines (VMs), and network dependencies in your on-premises data centers. For more information, see the AWS Application Discovery Service FAQ.

- [Welcome](https://docs.aws.amazon.com/application-discovery/latest/APIReference/Welcome.html)
- [Common Parameters](https://docs.aws.amazon.com/application-discovery/latest/APIReference/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/application-discovery/latest/APIReference/CommonErrors.html)

## [Actions](https://docs.aws.amazon.com/application-discovery/latest/APIReference/API_Operations.html)

- [AssociateConfigurationItemsToApplication](https://docs.aws.amazon.com/application-discovery/latest/APIReference/API_AssociateConfigurationItemsToApplication.html)
- [BatchDeleteAgents](https://docs.aws.amazon.com/application-discovery/latest/APIReference/API_BatchDeleteAgents.html)
- [BatchDeleteImportData](https://docs.aws.amazon.com/application-discovery/latest/APIReference/API_BatchDeleteImportData.html)
- [CreateApplication](https://docs.aws.amazon.com/application-discovery/latest/APIReference/API_CreateApplication.html)
- [CreateTags](https://docs.aws.amazon.com/application-discovery/latest/APIReference/API_CreateTags.html)
- [DeleteApplications](https://docs.aws.amazon.com/application-discovery/latest/APIReference/API_DeleteApplications.html)
- [DeleteTags](https://docs.aws.amazon.com/application-discovery/latest/APIReference/API_DeleteTags.html)
- [DescribeAgents](https://docs.aws.amazon.com/application-discovery/latest/APIReference/API_DescribeAgents.html)
- [DescribeBatchDeleteConfigurationTask](https://docs.aws.amazon.com/application-discovery/latest/APIReference/API_DescribeBatchDeleteConfigurationTask.html)
- [DescribeConfigurations](https://docs.aws.amazon.com/application-discovery/latest/APIReference/API_DescribeConfigurations.html)
- [DescribeContinuousExports](https://docs.aws.amazon.com/application-discovery/latest/APIReference/API_DescribeContinuousExports.html)
- [DescribeExportConfigurations](https://docs.aws.amazon.com/application-discovery/latest/APIReference/API_DescribeExportConfigurations.html)
- [DescribeExportTasks](https://docs.aws.amazon.com/application-discovery/latest/APIReference/API_DescribeExportTasks.html)
- [DescribeImportTasks](https://docs.aws.amazon.com/application-discovery/latest/APIReference/API_DescribeImportTasks.html)
- [DescribeTags](https://docs.aws.amazon.com/application-discovery/latest/APIReference/API_DescribeTags.html)
- [DisassociateConfigurationItemsFromApplication](https://docs.aws.amazon.com/application-discovery/latest/APIReference/API_DisassociateConfigurationItemsFromApplication.html)
- [ExportConfigurations](https://docs.aws.amazon.com/application-discovery/latest/APIReference/API_ExportConfigurations.html)
- [GetDiscoverySummary](https://docs.aws.amazon.com/application-discovery/latest/APIReference/API_GetDiscoverySummary.html)
- [ListConfigurations](https://docs.aws.amazon.com/application-discovery/latest/APIReference/API_ListConfigurations.html)
- [ListServerNeighbors](https://docs.aws.amazon.com/application-discovery/latest/APIReference/API_ListServerNeighbors.html)
- [StartBatchDeleteConfigurationTask](https://docs.aws.amazon.com/application-discovery/latest/APIReference/API_StartBatchDeleteConfigurationTask.html)
- [StartContinuousExport](https://docs.aws.amazon.com/application-discovery/latest/APIReference/API_StartContinuousExport.html)
- [StartDataCollectionByAgentIds](https://docs.aws.amazon.com/application-discovery/latest/APIReference/API_StartDataCollectionByAgentIds.html)
- [StartExportTask](https://docs.aws.amazon.com/application-discovery/latest/APIReference/API_StartExportTask.html)
- [StartImportTask](https://docs.aws.amazon.com/application-discovery/latest/APIReference/API_StartImportTask.html)
- [StopContinuousExport](https://docs.aws.amazon.com/application-discovery/latest/APIReference/API_StopContinuousExport.html)
- [StopDataCollectionByAgentIds](https://docs.aws.amazon.com/application-discovery/latest/APIReference/API_StopDataCollectionByAgentIds.html)
- [UpdateApplication](https://docs.aws.amazon.com/application-discovery/latest/APIReference/API_UpdateApplication.html)


## [Data Types](https://docs.aws.amazon.com/application-discovery/latest/APIReference/API_Types.html)

- [AgentConfigurationStatus](https://docs.aws.amazon.com/application-discovery/latest/APIReference/API_AgentConfigurationStatus.html): Information about agents that were instructed to start collecting data.
- [AgentInfo](https://docs.aws.amazon.com/application-discovery/latest/APIReference/API_AgentInfo.html): Information about agents associated with the userâs AWS account.
- [AgentNetworkInfo](https://docs.aws.amazon.com/application-discovery/latest/APIReference/API_AgentNetworkInfo.html): Network details about the host where the agent/collector resides.
- [BatchDeleteAgentError](https://docs.aws.amazon.com/application-discovery/latest/APIReference/API_BatchDeleteAgentError.html)
- [BatchDeleteConfigurationTask](https://docs.aws.amazon.com/application-discovery/latest/APIReference/API_BatchDeleteConfigurationTask.html)
- [BatchDeleteImportDataError](https://docs.aws.amazon.com/application-discovery/latest/APIReference/API_BatchDeleteImportDataError.html)
- [ConfigurationTag](https://docs.aws.amazon.com/application-discovery/latest/APIReference/API_ConfigurationTag.html): Tags for a configuration item.
- [ContinuousExportDescription](https://docs.aws.amazon.com/application-discovery/latest/APIReference/API_ContinuousExportDescription.html): A list of continuous export descriptions.
- [CustomerAgentInfo](https://docs.aws.amazon.com/application-discovery/latest/APIReference/API_CustomerAgentInfo.html): Inventory data for installed discovery agents.
- [CustomerAgentlessCollectorInfo](https://docs.aws.amazon.com/application-discovery/latest/APIReference/API_CustomerAgentlessCollectorInfo.html)
- [CustomerConnectorInfo](https://docs.aws.amazon.com/application-discovery/latest/APIReference/API_CustomerConnectorInfo.html): Inventory data for installed discovery connectors.
- [CustomerMeCollectorInfo](https://docs.aws.amazon.com/application-discovery/latest/APIReference/API_CustomerMeCollectorInfo.html)
- [DeleteAgent](https://docs.aws.amazon.com/application-discovery/latest/APIReference/API_DeleteAgent.html)
- [DeletionWarning](https://docs.aws.amazon.com/application-discovery/latest/APIReference/API_DeletionWarning.html)
- [Ec2RecommendationsExportPreferences](https://docs.aws.amazon.com/application-discovery/latest/APIReference/API_Ec2RecommendationsExportPreferences.html)
- [ExportFilter](https://docs.aws.amazon.com/application-discovery/latest/APIReference/API_ExportFilter.html): Used to select which agent's data is to be exported.
- [ExportInfo](https://docs.aws.amazon.com/application-discovery/latest/APIReference/API_ExportInfo.html): Information regarding the export status of discovered data.
- [ExportPreferences](https://docs.aws.amazon.com/application-discovery/latest/APIReference/API_ExportPreferences.html)
- [FailedConfiguration](https://docs.aws.amazon.com/application-discovery/latest/APIReference/API_FailedConfiguration.html)
- [Filter](https://docs.aws.amazon.com/application-discovery/latest/APIReference/API_Filter.html): A filter that can use conditional operators.
- [ImportTask](https://docs.aws.amazon.com/application-discovery/latest/APIReference/API_ImportTask.html)
- [ImportTaskFilter](https://docs.aws.amazon.com/application-discovery/latest/APIReference/API_ImportTaskFilter.html)
- [NeighborConnectionDetail](https://docs.aws.amazon.com/application-discovery/latest/APIReference/API_NeighborConnectionDetail.html): Details about neighboring servers.
- [OrderByElement](https://docs.aws.amazon.com/application-discovery/latest/APIReference/API_OrderByElement.html): A field and direction for ordered output.
- [ReservedInstanceOptions](https://docs.aws.amazon.com/application-discovery/latest/APIReference/API_ReservedInstanceOptions.html)
- [Tag](https://docs.aws.amazon.com/application-discovery/latest/APIReference/API_Tag.html): Metadata that help you categorize IT assets.
- [TagFilter](https://docs.aws.amazon.com/application-discovery/latest/APIReference/API_TagFilter.html): The tag filter.
- [UsageMetricBasis](https://docs.aws.amazon.com/application-discovery/latest/APIReference/API_UsageMetricBasis.html)
