# Source: https://docs.aws.amazon.com/detective/latest/APIReference/llms.txt

# Amazon Detective API Reference

> Detective uses machine learning and purpose-built visualizations to help you to analyze and investigate security issues across your Amazon Web Services (AWS) workloads. Detective automatically extracts time-based events such as login attempts, API calls, and network traffic from AWS CloudTrail and Amazon Virtual Private Cloud (Amazon VPC) flow logs. It also extracts findings detected by Amazon GuardDuty.

- [Welcome](https://docs.aws.amazon.com/detective/latest/APIReference/Welcome.html)
- [Common Parameters](https://docs.aws.amazon.com/detective/latest/APIReference/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/detective/latest/APIReference/CommonErrors.html)

## [Actions](https://docs.aws.amazon.com/detective/latest/APIReference/API_Operations.html)

- [AcceptInvitation](https://docs.aws.amazon.com/detective/latest/APIReference/API_AcceptInvitation.html): Accepts an invitation for the member account to contribute data to a behavior graph.
- [BatchGetGraphMemberDatasources](https://docs.aws.amazon.com/detective/latest/APIReference/API_BatchGetGraphMemberDatasources.html): Gets data source package information for the behavior graph.
- [BatchGetMembershipDatasources](https://docs.aws.amazon.com/detective/latest/APIReference/API_BatchGetMembershipDatasources.html): Gets information on the data source package history for an account.
- [CreateGraph](https://docs.aws.amazon.com/detective/latest/APIReference/API_CreateGraph.html): Creates a new behavior graph for the calling account, and sets that account as the administrator account.
- [CreateMembers](https://docs.aws.amazon.com/detective/latest/APIReference/API_CreateMembers.html): CreateMembers is used to send invitations to accounts.
- [DeleteGraph](https://docs.aws.amazon.com/detective/latest/APIReference/API_DeleteGraph.html): Disables the specified behavior graph and queues it to be deleted.
- [DeleteMembers](https://docs.aws.amazon.com/detective/latest/APIReference/API_DeleteMembers.html): Removes the specified member accounts from the behavior graph.
- [DescribeOrganizationConfiguration](https://docs.aws.amazon.com/detective/latest/APIReference/API_DescribeOrganizationConfiguration.html): Returns information about the configuration for the organization behavior graph.
- [DisableOrganizationAdminAccount](https://docs.aws.amazon.com/detective/latest/APIReference/API_DisableOrganizationAdminAccount.html): Removes the Detective administrator account in the current Region.
- [DisassociateMembership](https://docs.aws.amazon.com/detective/latest/APIReference/API_DisassociateMembership.html): Removes the member account from the specified behavior graph.
- [EnableOrganizationAdminAccount](https://docs.aws.amazon.com/detective/latest/APIReference/API_EnableOrganizationAdminAccount.html): Designates the Detective administrator account for the organization in the current Region.
- [GetInvestigation](https://docs.aws.amazon.com/detective/latest/APIReference/API_GetInvestigation.html): Detective investigations lets you investigate IAM users and IAM roles using indicators of compromise.
- [GetMembers](https://docs.aws.amazon.com/detective/latest/APIReference/API_GetMembers.html): Returns the membership details for specified member accounts for a behavior graph.
- [ListDatasourcePackages](https://docs.aws.amazon.com/detective/latest/APIReference/API_ListDatasourcePackages.html): Lists data source packages in the behavior graph.
- [ListGraphs](https://docs.aws.amazon.com/detective/latest/APIReference/API_ListGraphs.html): Returns the list of behavior graphs that the calling account is an administrator account of.
- [ListIndicators](https://docs.aws.amazon.com/detective/latest/APIReference/API_ListIndicators.html): Gets the indicators from an investigation.
- [ListInvestigations](https://docs.aws.amazon.com/detective/latest/APIReference/API_ListInvestigations.html): Detective investigations lets you investigate IAM users and IAM roles using indicators of compromise.
- [ListInvitations](https://docs.aws.amazon.com/detective/latest/APIReference/API_ListInvitations.html): Retrieves the list of open and accepted behavior graph invitations for the member account.
- [ListMembers](https://docs.aws.amazon.com/detective/latest/APIReference/API_ListMembers.html): Retrieves the list of member accounts for a behavior graph.
- [ListOrganizationAdminAccounts](https://docs.aws.amazon.com/detective/latest/APIReference/API_ListOrganizationAdminAccounts.html): Returns information about the Detective administrator account for an organization.
- [ListTagsForResource](https://docs.aws.amazon.com/detective/latest/APIReference/API_ListTagsForResource.html): Returns the tag values that are assigned to a behavior graph.
- [RejectInvitation](https://docs.aws.amazon.com/detective/latest/APIReference/API_RejectInvitation.html): Rejects an invitation to contribute the account data to a behavior graph.
- [StartInvestigation](https://docs.aws.amazon.com/detective/latest/APIReference/API_StartInvestigation.html): Detective investigations lets you investigate IAM users and IAM roles using indicators of compromise.
- [StartMonitoringMember](https://docs.aws.amazon.com/detective/latest/APIReference/API_StartMonitoringMember.html): Sends a request to enable data ingest for a member account that has a status of ACCEPTED_BUT_DISABLED.
- [TagResource](https://docs.aws.amazon.com/detective/latest/APIReference/API_TagResource.html): Applies tag values to a behavior graph.
- [UntagResource](https://docs.aws.amazon.com/detective/latest/APIReference/API_UntagResource.html): Removes tags from a behavior graph.
- [UpdateDatasourcePackages](https://docs.aws.amazon.com/detective/latest/APIReference/API_UpdateDatasourcePackages.html): Starts a data source package for the Detective behavior graph.
- [UpdateInvestigationState](https://docs.aws.amazon.com/detective/latest/APIReference/API_UpdateInvestigationState.html): Updates the state of an investigation.
- [UpdateOrganizationConfiguration](https://docs.aws.amazon.com/detective/latest/APIReference/API_UpdateOrganizationConfiguration.html): Updates the configuration for the Organizations integration in the current Region.


## [Data Types](https://docs.aws.amazon.com/detective/latest/APIReference/API_Types.html)

- [Account](https://docs.aws.amazon.com/detective/latest/APIReference/API_Account.html): An AWS account that is the administrator account of or a member of a behavior graph.
- [Administrator](https://docs.aws.amazon.com/detective/latest/APIReference/API_Administrator.html): Information about the Detective administrator account for an organization.
- [DatasourcePackageIngestDetail](https://docs.aws.amazon.com/detective/latest/APIReference/API_DatasourcePackageIngestDetail.html): Details about the data source packages ingested by your behavior graph.
- [DatasourcePackageUsageInfo](https://docs.aws.amazon.com/detective/latest/APIReference/API_DatasourcePackageUsageInfo.html): Information on the usage of a data source package in the behavior graph.
- [DateFilter](https://docs.aws.amazon.com/detective/latest/APIReference/API_DateFilter.html): Contains details on the time range used to filter data.
- [FilterCriteria](https://docs.aws.amazon.com/detective/latest/APIReference/API_FilterCriteria.html): Details on the criteria used to define the filter for investigation results.
- [FlaggedIpAddressDetail](https://docs.aws.amazon.com/detective/latest/APIReference/API_FlaggedIpAddressDetail.html): Contains information on suspicious IP addresses identified as indicators of compromise.
- [Graph](https://docs.aws.amazon.com/detective/latest/APIReference/API_Graph.html): A behavior graph in Detective.
- [ImpossibleTravelDetail](https://docs.aws.amazon.com/detective/latest/APIReference/API_ImpossibleTravelDetail.html): Contains information on unusual and impossible travel in an account.
- [Indicator](https://docs.aws.amazon.com/detective/latest/APIReference/API_Indicator.html): Detective investigations triages indicators of compromises such as a finding and surfaces only the most critical and suspicious issues, so you can focus on high-level investigations.
- [IndicatorDetail](https://docs.aws.amazon.com/detective/latest/APIReference/API_IndicatorDetail.html): Details about the indicators of compromise which are used to determine if a resource is involved in a security incident.
- [InvestigationDetail](https://docs.aws.amazon.com/detective/latest/APIReference/API_InvestigationDetail.html): Details about the investigation related to a potential security event identified by Detective.
- [MemberDetail](https://docs.aws.amazon.com/detective/latest/APIReference/API_MemberDetail.html): Details about a member account in a behavior graph.
- [MembershipDatasources](https://docs.aws.amazon.com/detective/latest/APIReference/API_MembershipDatasources.html): Details on data source packages for members of the behavior graph.
- [NewAsoDetail](https://docs.aws.amazon.com/detective/latest/APIReference/API_NewAsoDetail.html): Details new Autonomous System Organizations (ASOs) used either at the resource or account level.
- [NewGeolocationDetail](https://docs.aws.amazon.com/detective/latest/APIReference/API_NewGeolocationDetail.html): Details new geolocations used either at the resource or account level.
- [NewUserAgentDetail](https://docs.aws.amazon.com/detective/latest/APIReference/API_NewUserAgentDetail.html): Details new user agents used either at the resource or account level.
- [RelatedFindingDetail](https://docs.aws.amazon.com/detective/latest/APIReference/API_RelatedFindingDetail.html): Details related activities associated with a potential security event.
- [RelatedFindingGroupDetail](https://docs.aws.amazon.com/detective/latest/APIReference/API_RelatedFindingGroupDetail.html): Details multiple activities as they related to a potential security event.
- [SortCriteria](https://docs.aws.amazon.com/detective/latest/APIReference/API_SortCriteria.html): Details about the criteria used for sorting investigations.
- [StringFilter](https://docs.aws.amazon.com/detective/latest/APIReference/API_StringFilter.html): A string for filtering Detective investigations.
- [TimestampForCollection](https://docs.aws.amazon.com/detective/latest/APIReference/API_TimestampForCollection.html): Details on when data collection began for a source package.
- [TTPsObservedDetail](https://docs.aws.amazon.com/detective/latest/APIReference/API_TTPsObservedDetail.html): Details tactics, techniques, and procedures (TTPs) used in a potential security event.
- [UnprocessedAccount](https://docs.aws.amazon.com/detective/latest/APIReference/API_UnprocessedAccount.html): A member account that was included in a request but for which the request could not be processed.
- [UnprocessedGraph](https://docs.aws.amazon.com/detective/latest/APIReference/API_UnprocessedGraph.html): Behavior graphs that could not be processed in the request.
