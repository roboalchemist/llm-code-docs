# Source: https://docs.aws.amazon.com/quicksight/latest/developerguide/llms.txt

# Amazon Quick Sight Developer Guide

> The Amazon Quick Sight Developer Guide describes how to work with the Quick Sight API and contains a full list of Quick Sight API operations sorted by type.

- [Overview](https://docs.aws.amazon.com/quicksight/latest/developerguide/welcome.html)
- [Terminology and concepts](https://docs.aws.amazon.com/quicksight/latest/developerguide/terminology-and-concepts.html)
- [Document history](https://docs.aws.amazon.com/quicksight/latest/developerguide/doc-history.html)

## [Get started](https://docs.aws.amazon.com/quicksight/latest/developerguide/getting-started.html)

- [Prerequisites](https://docs.aws.amazon.com/quicksight/latest/developerguide/getting-started-prerequisites.html): Learn more abotu the required prerequistes for the Quick Sight APIs and SDKs.
- [Make API requests with the Quick Sight SDKs](https://docs.aws.amazon.com/quicksight/latest/developerguide/getting-started-making-api-requests.html): Use this section to download the Quick Sight SDKs and make an API request.
- [Use CLI skeleton files](https://docs.aws.amazon.com/quicksight/latest/developerguide/cli-skeletons.html): Use AWS CLI skeleton files to run CLI commands that require long and complicated strings.
- [Use the Quick Sight Dev Portal](https://docs.aws.amazon.com/quicksight/latest/developerguide/getting-started-dev-portal.html): Learn how to access and use the Quick Sight Dev portal.


## [Embed assets with Quick Sight](https://docs.aws.amazon.com/quicksight/latest/developerguide/embedded-analytics.html)

### [Get started](https://docs.aws.amazon.com/quicksight/latest/developerguide/embedded-analytics-getting-started.html)

Amazon Quick Sight is a scalable, embeddable, ML-powered BI Service built for the cloud.

- [Prerequisites](https://docs.aws.amazon.com/quicksight/latest/developerguide/embedded-analytics-getting-started-prereqs.html): Before you get started, familiarize yourself with the list of technologies Quick Sight uses to create an embedding experience.
- [Choose the right embedding solution](https://docs.aws.amazon.com/quicksight/latest/developerguide/embedded-analytics-choosing-right-solution.html): Learn more about the different types of embedding offered by Quick Sight.
- [Create your first embedding application](https://docs.aws.amazon.com/quicksight/latest/developerguide/embedded-analytics-first-app.html): Learn how to create your first embedding application with Quick Sight.

### [Customize embedded assets](https://docs.aws.amazon.com/quicksight/latest/developerguide/embedded-analytics-customize-assets.html)

Use Quick Sight embedded analytics to embed custom Quick Sight assets into your application that are tailored to meet your business needs.

- [Control the look and feel of embedded assets](https://docs.aws.amazon.com/quicksight/latest/developerguide/embedded-analytics-control-look-and-feel.html): Customize the look and feel of en embedded asset
- [Add interactivity to your embedded content](https://docs.aws.amazon.com/quicksight/latest/developerguide/embedded-analytics-add-interactivity.html): Add interactivity to embedded Quick Sight assets.
- [Personalization](https://docs.aws.amazon.com/quicksight/latest/developerguide/personalization-embedded-analytics.html): Personalize an embedded Quick Sight asset.
- [Embedding security](https://docs.aws.amazon.com/quicksight/latest/developerguide/embedded-analytics-security.html): Amazon Quick Sight provides a secure platform that allows you to distribute dashboards and insights to tens of thousands of users with multiple-region availability and built-in redundancy.


## [ARNs in Quick Sight](https://docs.aws.amazon.com/quicksight/latest/developerguide/arns.html)

- [ARN formats](https://docs.aws.amazon.com/quicksight/latest/developerguide/arn-formats.html): Learn about Amazon Resource Name (ARN) formats for Amazon Quick Sight.
- [Quick Sight resource ARNs](https://docs.aws.amazon.com/quicksight/latest/developerguide/resource-arns.html): Learn about Amazon Resource Names (ARNs) for Amazon Quick Sight resources.
- [Permissions](https://docs.aws.amazon.com/quicksight/latest/developerguide/resource-permissions.html): Learn about permissions for Quick Sight resources.
- [Errors](https://docs.aws.amazon.com/quicksight/latest/developerguide/resource-errors.html): Learn about the two types of Quick Sight error codes, client and server error codes.


## [Operations](https://docs.aws.amazon.com/quicksight/latest/developerguide/operations.html)

### [Account customization operations](https://docs.aws.amazon.com/quicksight/latest/developerguide/account-customization-operations.html)

Learn about different account customization operations in Amazon Quick Sight.

### [Account settings](https://docs.aws.amazon.com/quicksight/latest/developerguide/account-settings.html)

Learn about the different account settings operations in Amazon Quick Sight.

- [DescribeAccountSettings](https://docs.aws.amazon.com/quicksight/latest/developerguide/describe-account-settings.html): Use the DescribeAccountSettings API operation to describe the settings that were used when your Amazon Quick Sight subscription was first created in this AWS account.
- [UpdateAccountSettings](https://docs.aws.amazon.com/quicksight/latest/developerguide/update-account-settings.html): Use the UpdateAccountSettings API operation to update the Amazon Quick Sight settings in your AWS account.
- [CreateAccountCustomization](https://docs.aws.amazon.com/quicksight/latest/developerguide/create-account-customization.html): Use the CreateAccountCustomization API operation to create Amazon Quick Sight customizations in the current AWS Region.
- [DeleteAccountCustomization](https://docs.aws.amazon.com/quicksight/latest/developerguide/delete-account-customization.html): Use the DeleteAccountCustomization API operation to delete all Amazon Quick Sight customizations in this AWS Region for the specified AWS account and Quick Sight namespace.
- [DescribeAccountCustomization](https://docs.aws.amazon.com/quicksight/latest/developerguide/describe-account-customization.html): Use the DescribeAccountCustomization API operation to describe the customizations associated with the provided AWS account and Amazon Quick Sight namespace in an AWS Region.
- [UpdateAccountCustomization](https://docs.aws.amazon.com/quicksight/latest/developerguide/update-account-customization.html): Use the UpdateAccountCustomization API operation to update Amazon Quick Sight customizations in the current AWS Region.

### [Analysis operations](https://docs.aws.amazon.com/quicksight/latest/developerguide/analysis-operations.html)

Learn about different analysis operations in Amazon Quick Sight.

### [Analysis permissions operations](https://docs.aws.amazon.com/quicksight/latest/developerguide/analysis-permissions.html)

Learn about different analysis permissions operations in Amazon Quick Sight.

- [DescribeAnalysisPermissions](https://docs.aws.amazon.com/quicksight/latest/developerguide/describe-analysis-permissions.html): Use the DescribeAnalysisPermissions API operation to view the read and write permissions for an analysis.
- [UpdateAnalysisPermissions](https://docs.aws.amazon.com/quicksight/latest/developerguide/update-analysis-permissions.html): Use the UpdateAnalysisPermissions API operation to update the read and write permissions for an analysis.
- [CreateAnalysis](https://docs.aws.amazon.com/quicksight/latest/developerguide/create-analysis.html): Use the CreateAnalysis API operation to create an analysis in Amazon Quick Sight for a specified user.
- [DeleteAnalysis](https://docs.aws.amazon.com/quicksight/latest/developerguide/delete-analysis.html): Use the DeleteAnalysis API operation to delete an analysis from Amazon Quick Sight for a specified user.
- [DescribeAnalysis](https://docs.aws.amazon.com/quicksight/latest/developerguide/describe-analysis.html): Use the DescribeAnalysis API operation to view a summary of the metadata for an analysis for a specified user.
- [ListAnalyses](https://docs.aws.amazon.com/quicksight/latest/developerguide/list-analyses.html): Use the ListAnalyses API operation to list Amazon Quick Sight analyses that exist in the specified AWS account.
- [RestoreAnalysis](https://docs.aws.amazon.com/quicksight/latest/developerguide/restore-analysis.html): Use the RestoreAnalysis API operation to restore an analysis for a specified user.
- [SearchAnalyses](https://docs.aws.amazon.com/quicksight/latest/developerguide/search-analyses.html): Use the SearchAnalyses API operation to search for analyses that belong to the specified user.
- [UpdateAnalysis](https://docs.aws.amazon.com/quicksight/latest/developerguide/update-analysis.html): Use the UpdateAnalysis API operation to update an analysis in Amazon Quick Sight.

### [Asset bundle operations](https://docs.aws.amazon.com/quicksight/latest/developerguide/asset-bundle-ops.html)

Learn about different asset bundle operations in Amazon Quick Sight.

- [Permissions](https://docs.aws.amazon.com/quicksight/latest/developerguide/assetbundle-permissions.html): Permissions for the asset bundle APIs.
- [Asset bundle export operations](https://docs.aws.amazon.com/quicksight/latest/developerguide/assetbundle-export.html): Learn about different asset bundle export operations in Amazon Quick Sight.
- [Asset bundle import operations](https://docs.aws.amazon.com/quicksight/latest/developerguide/assetbundle-import.html): Learn about different asset bundle import operations in Amazon Quick Sight.

### [Dashboard operations](https://docs.aws.amazon.com/quicksight/latest/developerguide/dashboard-operations.html)

Learn about different dashboard operations in Amazon Quick Sight.

### [Dashboard permissions](https://docs.aws.amazon.com/quicksight/latest/developerguide/dashboard-permissions.html)

Learn about different dashboard permissions operations in Amazon Quick Sight.

- [DescribeDashboardPermissions](https://docs.aws.amazon.com/quicksight/latest/developerguide/describe-dashboard-permissions.html): Use the DescribeDashboardPermissions API operation to view the read and write permissions for a dashboard.
- [UpdateDashboardPermissions](https://docs.aws.amazon.com/quicksight/latest/developerguide/update-dashboard-permissions.html): Use the UpdateDashboardPermissions API operation to update read and write permissions for a dashboard.
- [CreateDashboard](https://docs.aws.amazon.com/quicksight/latest/developerguide/create-dashboard.html): Use the CreateDashboard API operation to create a dashboard.
- [DeleteDashboard](https://docs.aws.amazon.com/quicksight/latest/developerguide/delete-dashboard.html): Use the DeleteDashboard API operation to delete a dashboard.
- [DescribeDashboard](https://docs.aws.amazon.com/quicksight/latest/developerguide/describe-dashboard.html): Use the DescribeDashboard API operation to view the summary of a dashboard.
- [ListDashboards](https://docs.aws.amazon.com/quicksight/latest/developerguide/list-dashboards.html): Use the ListDashboards API operation to list dashboards in an AWS account.
- [ListDashboardVersions](https://docs.aws.amazon.com/quicksight/latest/developerguide/list-dashboard-versions.html): Use the ListDashboardVersions API operation to list all the versions of a dashboard in an AWS account.
- [SearchDashboards](https://docs.aws.amazon.com/quicksight/latest/developerguide/search-dashboards.html): Use the SearchDashboards API operation to search for dashboards in an AWS account.
- [UpdateDashboard](https://docs.aws.amazon.com/quicksight/latest/developerguide/update-dashboard.html): Use the UpdateDashboard API operation to update a dashboard in an AWS account.
- [UpdateDashboardPublishedVersion](https://docs.aws.amazon.com/quicksight/latest/developerguide/update-dashboard-published-version.html): Use the UpdateDashboardPublishedVersion API operation to update the published version of a dashboard.

### [Data source operations](https://docs.aws.amazon.com/quicksight/latest/developerguide/data-source-operations.html)

Learn about different data source operations for Amazon Quick Sight.

### [Data source permissions](https://docs.aws.amazon.com/quicksight/latest/developerguide/data-source-permissions.html)

Learn about different data source permissions operations in Amazon Quick Sight.

- [DescribeDataSourcePermissions](https://docs.aws.amazon.com/quicksight/latest/developerguide/describe-data-source-operation.html): Use the DescribeDataSourcePermissions API operation to describe the resource permissions for a data source.
- [UpdateDataSourcePermissions](https://docs.aws.amazon.com/quicksight/latest/developerguide/update-data-source-permissions.html): Use the UpdateDataSourcePermissions API operation to update the resource permissions for a data source.
- [CreateDataSource](https://docs.aws.amazon.com/quicksight/latest/developerguide/create-data-source.html): The CreateDataSource Operation.
- [DeleteDataSource](https://docs.aws.amazon.com/quicksight/latest/developerguide/delete-data-source.html): The DeleteDataSource Operation.
- [DescribeDataSource](https://docs.aws.amazon.com/quicksight/latest/developerguide/describe-data-source.html): The DescribeDataSource Operation.
- [ListDataSources](https://docs.aws.amazon.com/quicksight/latest/developerguide/list-data-sources.html): Use the ListDataSources API operation to list all data sources in the current AWS Region that belong to a particular AWS account.
- [UpdateDataSource](https://docs.aws.amazon.com/quicksight/latest/developerguide/update-data-source.html): Use the UpdateDataSource API operation to update a data source.

### [Dataset operations](https://docs.aws.amazon.com/quicksight/latest/developerguide/data-set-operations.html)

Learn about different dataset operations in Amazon Quick Sight.

### [Dataset permissions operations](https://docs.aws.amazon.com/quicksight/latest/developerguide/data-set-permissions.html)

Learn about the different dataset permissions operations in Amazon Quick Sight.

- [DescribeDataSetPermissions](https://docs.aws.amazon.com/quicksight/latest/developerguide/describe-data-set-permissions.html): Use the DescribeDataSetPermissions API operation to describe the permissions on a dataset.
- [UpdateDataSetPermissions](https://docs.aws.amazon.com/quicksight/latest/developerguide/update-data-set-permissions.html): Use the UpdateDataSetPermissions API operation to update the permissions on a dataset.
- [CreateDataSet](https://docs.aws.amazon.com/quicksight/latest/developerguide/create-data-set.html): The CreateDataSet Operation.
- [DeleteDataSet](https://docs.aws.amazon.com/quicksight/latest/developerguide/delete-data-set.html): Use the DeleteDataSet API operation to delete a dataset.
- [DescribeDataSet](https://docs.aws.amazon.com/quicksight/latest/developerguide/describe-data-set.html): Use the DescribeDataSet API operation to describe a dataset.
- [ListDataSets](https://docs.aws.amazon.com/quicksight/latest/developerguide/list-data-sets.html): Use the ListDataSets API operation to list all of the datasets that belong to a particular AWS account in an AWS Region.
- [UpdateDataSet](https://docs.aws.amazon.com/quicksight/latest/developerguide/update-data-set.html): Use the UpdateDataSet API operation to update a dataset.

### [Folder operations](https://docs.aws.amazon.com/quicksight/latest/developerguide/folder-operations.html)

Learn about the different folder operations in Amazon Quick Sight.

### [Folder membership operations](https://docs.aws.amazon.com/quicksight/latest/developerguide/folder-membership.html)

Learn about different folder membership operations in Amazon Quick Sight.

- [CreateFolderMembership](https://docs.aws.amazon.com/quicksight/latest/developerguide/create-folder-membership.html): Use the CreateFolderMembership to add an asset, such as a dashboard, analysis, or dataset, to a folder.
- [DeleteFolderMembership](https://docs.aws.amazon.com/quicksight/latest/developerguide/delete-folder-membership.html): Use the DeleteFolderMembership to delete an asset, such as a dashboard, analysis, or dataset, from a folder.
- [ListFolderMembers](https://docs.aws.amazon.com/quicksight/latest/developerguide/list-folder-members.html): Use the ListFolderMembers operation to list all assets (DASHBOARD, ANALYSIS, and DATASET) that are in a folder.

### [Folder permissions operations](https://docs.aws.amazon.com/quicksight/latest/developerguide/folder-permissions.html)

Learn about different folder permissions operations in Quick Sight.

- [DescribeFolderPermissions](https://docs.aws.amazon.com/quicksight/latest/developerguide/describe-folder-permissions.html): Use the DescribeFolderPermissions operation to describe the permissions of a folder.
- [DescribeFolderResolvedPermissions](https://docs.aws.amazon.com/quicksight/latest/developerguide/describe-folder-resolved-permissions.html): Use the DescribeFolderResolvedPermissions operation to describe the resolved permissions of a folder.
- [UpdateFolderPermissions](https://docs.aws.amazon.com/quicksight/latest/developerguide/update-folder-permissions.html): Use the UpdateFolderPermissions operation to update the permissions of a folder.
- [CreateFolder](https://docs.aws.amazon.com/quicksight/latest/developerguide/create-folder.html): The CreateFolder operation creates an empty shared folder.
- [DeleteFolder](https://docs.aws.amazon.com/quicksight/latest/developerguide/delete-folder.html): The DeleteFolder Operation.
- [DescribeFolder](https://docs.aws.amazon.com/quicksight/latest/developerguide/describe-folder.html): Use the DescribeFolder operation to describe a folder.
- [ListFolders](https://docs.aws.amazon.com/quicksight/latest/developerguide/list-folders.html): Use the ListFolders operation to list all folders in an Quick Sight account.
- [SearchFolders](https://docs.aws.amazon.com/quicksight/latest/developerguide/search-folders.html): Use the SearchFolders operation to search the subfolders of a folder.
- [UpdateFolder](https://docs.aws.amazon.com/quicksight/latest/developerguide/update-folder.html): Use the UpdateFolder operation to update the name of a folder.

### [Group operations](https://docs.aws.amazon.com/quicksight/latest/developerguide/group-operations.html)

Learn about different group API operations in Amazon Quick Sight.

### [Group membership operations](https://docs.aws.amazon.com/quicksight/latest/developerguide/group-membership.html)

With group membership API operations, you can view and update permissions for members in a group.

- [CreateGroupMembership](https://docs.aws.amazon.com/quicksight/latest/developerguide/create-group-membership.html): Use the CreateGroupMembership API operation to add an Amazon Quick Sight user to a Quick Sight group.
- [DeleteGroupMembership](https://docs.aws.amazon.com/quicksight/latest/developerguide/delete-group-membership.html): Use the DeleteGroupMembership API operation to remove a user from a group
- [DescribeGroupMembership](https://docs.aws.amazon.com/quicksight/latest/developerguide/describe-group-membership.html): Use the DescribeGroupMembership API operation to determine if a user is a member of the specified group.
- [ListGroupMemberships](https://docs.aws.amazon.com/quicksight/latest/developerguide/list-group-memberships.html): Use the ListGroupMemberships API operation to list member users in a group.
- [CreateGroup](https://docs.aws.amazon.com/quicksight/latest/developerguide/create-group.html): Use the CreateGroup API operation to create a user group in Amazon Quick Sight.
- [DeleteGroup](https://docs.aws.amazon.com/quicksight/latest/developerguide/delete-group.html): Use the DeleteGroup API operation to remove a user group from Amazon Quick Sight.
- [DescribeGroup](https://docs.aws.amazon.com/quicksight/latest/developerguide/describe-group.html): Use the DescribeGroup API operation to view an Amazon Quick Sight group's description and Amazon Resource Name (ARN).
- [ListGroups](https://docs.aws.amazon.com/quicksight/latest/developerguide/list-groups.html): Use the ListGroups API operation to list all user groups in Amazon Quick Sight.
- [SearchGroups](https://docs.aws.amazon.com/quicksight/latest/developerguide/search-groups.html): Use the SearchGroups operation to search groups in a namespace.
- [UpdateGroup](https://docs.aws.amazon.com/quicksight/latest/developerguide/update-group.html): Use the UpdateGroup API operation to change a group description in Amazon Quick Sight.

### [IAM policy assignment operations](https://docs.aws.amazon.com/quicksight/latest/developerguide/iam-policy-assignment-operations.html)

Learn about different IAM policy assignment operations in Amazon Quick Sight.

- [CreateIAMPolicyAssignment](https://docs.aws.amazon.com/quicksight/latest/developerguide/create-iam-policy-assignment.html): Use the CreateIAMPolicyAssignment API operation to create an assignment with one specified IAM policy, identified by its Amazon Resource Name (ARN).
- [DeleteIAMPolicyAssignment](https://docs.aws.amazon.com/quicksight/latest/developerguide/delete-iam-policy-assignment.html): Use the DeleteIAMPolicyAssignment API operation to delete an existing IAM policy assignment.
- [DescribeIAMPolicyAssignment](https://docs.aws.amazon.com/quicksight/latest/developerguide/describe-iam-policy-assignment.html): Use the DescribeIAMPolicyAssignment API operation to describe an existing IAM policy assignment.
- [ListIAMPolicyAssignments](https://docs.aws.amazon.com/quicksight/latest/developerguide/list-iam-policy-assignments.html): Use the ListIAMPolicyAssignments API operation to list IAM policy assignments in the current Amazon Quick Sight account.
- [ListIAMPolicyAssignmentsForUser](https://docs.aws.amazon.com/quicksight/latest/developerguide/list-iam-policy-assignments-for-user.html): Use the ListIAMPolicyAssignmentsForUser API operation to list all the IAM policy assignments.
- [UpdateIAMPolicyAssignment](https://docs.aws.amazon.com/quicksight/latest/developerguide/update-iam-policy-assignment.html): Use the UpdateIAMPolicyAssignment API operation to update an existing IAM policy assignment.

### [Ingestion operations](https://docs.aws.amazon.com/quicksight/latest/developerguide/ingestion-operations.html)

Learn about different ingestion operations in Amazon Quick Sight.

- [CancelIngestion](https://docs.aws.amazon.com/quicksight/latest/developerguide/cancel-ingestion.html): Use the CancelIngestion operation to cancel an ongoing ingestion of data into SPICE.
- [CreateIngestion](https://docs.aws.amazon.com/quicksight/latest/developerguide/create-ingestion.html): Use the CreateIngestion to create and start a new SPICE ingestion on a dataset.
- [DescribeIngestion](https://docs.aws.amazon.com/quicksight/latest/developerguide/describe-ingestion.html): Use the DescribeIngestion operation to describe a SPICE ingestion.
- [ListIngestions](https://docs.aws.amazon.com/quicksight/latest/developerguide/list-ingestions.html): Use the ListIngestions operation to list the history of SPICE ingestioned for a dataset.

### [IP and VPC endpoint restriction operations](https://docs.aws.amazon.com/quicksight/latest/developerguide/ip-restrictions-operations.html)

Learn about the different IP and VPC endpoint restriction operations in Amazon Quick Sight.

- [DescribeIpRestriction](https://docs.aws.amazon.com/quicksight/latest/developerguide/describe-ip-restriction.html): Use the DescribeIpRestriction operation to get a summary and status of IP rules.
- [UpdateIpRestriction](https://docs.aws.amazon.com/quicksight/latest/developerguide/update-ip-restriction.html): Use the UpdateIpRestriction operation to update the content and status of IP rules.
- [VPC endpoints (AWS PrivateLink)](https://docs.aws.amazon.com/quicksight/latest/developerguide/vpc-interface-endpoints.html): You can use an interface VPC endpoint to create a private connection between your VPC and Quick without requiring access over the internet or through a NAT device, a VPN connection, or an Direct Connect connection.
- [Key management operations](https://docs.aws.amazon.com/quicksight/latest/developerguide/cmk-operations.html): Learn about the creating and managing AWS KMS Customer Managed Keys (CMKs) with the Quick Sight APIs.

### [Namespace operations](https://docs.aws.amazon.com/quicksight/latest/developerguide/namespace-operations.html)

Learn about different namespace operations in Amazon Quick Sight.

- [CreateNamespace](https://docs.aws.amazon.com/quicksight/latest/developerguide/create-namespace.html): Use the CreateNamespace API operation to create a new namespace for you to use with Amazon Quick Sight.
- [DeleteNamespace](https://docs.aws.amazon.com/quicksight/latest/developerguide/delete-namespace.html): Use the DeleteNamespace API operation to delete a namespace and the users and groups that are associated with the namespace.
- [DescribeNamespace](https://docs.aws.amazon.com/quicksight/latest/developerguide/describe-namespace.html): Use the DescribeNamespace API operation to describe a specified namespace.
- [ListNamespaces](https://docs.aws.amazon.com/quicksight/latest/developerguide/list-namespaces.html): Use the ListNamespaces API operation to list namespaces for a specified AWS account

### [Tag operations](https://docs.aws.amazon.com/quicksight/latest/developerguide/tag-operations.html)

Learn about the different tag operations in Amazon Quick Sight.

- [ListTagsForResource](https://docs.aws.amazon.com/quicksight/latest/developerguide/list-tags-for-resource.html): Use the ListTagsForResource API operation to list tags assigned to a resource.
- [TagResource](https://docs.aws.amazon.com/quicksight/latest/developerguide/tag-resource.html): Use the TagResource API operation to assign one or more tags (key-value pairs) to the specified Amazon Quick Sight resource.
- [UntagResource](https://docs.aws.amazon.com/quicksight/latest/developerguide/untag-resource.html): Use the UntagResource API operation to remove a tag from a resource.

### [Template alias operations](https://docs.aws.amazon.com/quicksight/latest/developerguide/template-alias-operations.html)

Learn about template alias operations and examples for Amazon Quick Sight.

- [CreateTemplateAlias](https://docs.aws.amazon.com/quicksight/latest/developerguide/create-template-alias.html): Use the CreateTemplateAlias operation to create a template alias for a template.
- [DeleteTemplateAlias](https://docs.aws.amazon.com/quicksight/latest/developerguide/delete-template-alais.html): The DeleteTemplateAlias operation.
- [DescribeTemplateAlias](https://docs.aws.amazon.com/quicksight/latest/developerguide/describe-template-alias.html): Use the DescribeTemplateAlias operation to describe the template alias for a template.
- [ListTemplateAliases](https://docs.aws.amazon.com/quicksight/latest/developerguide/list-template-aliases.html): Use the ListTemplateAliases operation to list all the aliases of a template.
- [UpdateTemplateAlias](https://docs.aws.amazon.com/quicksight/latest/developerguide/update-template-alias.html): Use the UpdateTemplateAlias operation to update the template alias of a template.

### [Template operations](https://docs.aws.amazon.com/quicksight/latest/developerguide/template-operations.html)

Learn about different template operations in Amazon Quick Sight.

### [Template permissions](https://docs.aws.amazon.com/quicksight/latest/developerguide/template-permissions.html)

Learn about operations for template permissions in Amazon Quick Sight.

- [DescribeTemplatePermissions](https://docs.aws.amazon.com/quicksight/latest/developerguide/describe-template-permissions.html): Use the DescribeTemplatePermissions operation to describe read and write permissions for a template.
- [UpdateTemplatePermissions](https://docs.aws.amazon.com/quicksight/latest/developerguide/update-template-permissions.html): The UpdateTemplatePermissions operation.
- [CreateTemplate](https://docs.aws.amazon.com/quicksight/latest/developerguide/create-template.html): Use the CreateTemplate operation to create a template from an existing Quick Sight analysis or template.
- [DeleteTemplate](https://docs.aws.amazon.com/quicksight/latest/developerguide/delete-template.html): Use the DeleteTemplate operation to delete a template.
- [DescribeTemplate](https://docs.aws.amazon.com/quicksight/latest/developerguide/describe-template.html): Use the DescribeTemplate operation to describe a template's metadata.
- [ListTemplates](https://docs.aws.amazon.com/quicksight/latest/developerguide/list-templates.html): Use the ListTemplates operation to list all the templates in the current Quick Sight account.
- [ListTemplateVersions](https://docs.aws.amazon.com/quicksight/latest/developerguide/list-template-versions.html): Use the ListTemplateVersions operation to list all the versions of the templates in the current Quick Sight account.
- [UpdateTemplate](https://docs.aws.amazon.com/quicksight/latest/developerguide/update-template.html): Use the UpdateTemplate operation to update a template from an existing Quick Sight analysis or another template.

### [Theme operations](https://docs.aws.amazon.com/quicksight/latest/developerguide/theme-operations.html)

Learn about different theme operations in Amazon Quick Sight.

### [Theme permissions](https://docs.aws.amazon.com/quicksight/latest/developerguide/theme-permissions.html)

Learn about different theme permissions operations in Amazon Quick Sight.

- [DescribeThemePermissions](https://docs.aws.amazon.com/quicksight/latest/developerguide/describe-theme-permissions.html): Use the DescribeThemePermissions operation to describe the read and write permissions for a theme.
- [UpdateThemePermissions](https://docs.aws.amazon.com/quicksight/latest/developerguide/update-theme-permissions.html): Use the UpdateThemePermissions operation to update the resource permissions for a template.
- [CreateTheme](https://docs.aws.amazon.com/quicksight/latest/developerguide/create-theme.html): Use the CreateTheme operation to create a theme.
- [DeleteTheme](https://docs.aws.amazon.com/quicksight/latest/developerguide/delete-theme.html): Use the DeleteTheme operation to delete a theme.
- [DescribeTheme](https://docs.aws.amazon.com/quicksight/latest/developerguide/describe-theme.html): Use the DescribeTheme operation to describe a theme.
- [ListThemes](https://docs.aws.amazon.com/quicksight/latest/developerguide/list-themes.html): Use the ListThemes operation to list all the themes in the current AWS account.
- [ListThemeVersions](https://docs.aws.amazon.com/quicksight/latest/developerguide/list-theme-versions.html): Use the ListThemeVersions operation to list all the versions of the themes in the current AWS account.
- [UpdateTheme](https://docs.aws.amazon.com/quicksight/latest/developerguide/update-theme.html): Use the UpdateTheme operation to update a theme.

### [Theme alias operations](https://docs.aws.amazon.com/quicksight/latest/developerguide/theme-alias-operations.html)

Learn about different theme alias operations for Amazon Quick Sight.

- [CreateThemeAlias](https://docs.aws.amazon.com/quicksight/latest/developerguide/create-theme-alias.html): The CreateThemeAlias operation creates a theme alias for a theme.
- [DeleteThemeAlias](https://docs.aws.amazon.com/quicksight/latest/developerguide/delete-theme-alias.html): Use the DeleteThemeAlias operation to delete the version of the theme that the specified theme alias points to.
- [DescribeThemeAlias](https://docs.aws.amazon.com/quicksight/latest/developerguide/describe-theme-alias.html): Use the DescribeThemeAlias operation to describe the alias for a theme.
- [ListThemeAliases](https://docs.aws.amazon.com/quicksight/latest/developerguide/list-theme-aliases.html): Use the ListThemeAliases operation to list all the aliases of a theme.
- [UpdateThemeAlias](https://docs.aws.amazon.com/quicksight/latest/developerguide/update-theme-alias.html): Use the UpdateThemeAlias operation to update an alias of a theme.

### [User operations](https://docs.aws.amazon.com/quicksight/latest/developerguide/user-operations.html)

Learn about different user operations in Amazon Quick Sight and get examples for them.

- [DeleteUser](https://docs.aws.amazon.com/quicksight/latest/developerguide/delete-user.html): The DeleteUser operation.
- [DeleteUserByPrincipalTitle](https://docs.aws.amazon.com/quicksight/latest/developerguide/delete-user-by-principal-title.html): The DeleteUserByPrincipalTitle operation deletes a user identified by a principal ID.
- [DescribeUser](https://docs.aws.amazon.com/quicksight/latest/developerguide/describe-user.html): Use the DescribeUser operation to return information about a user, given the user name.
- [ListUserGroups](https://docs.aws.amazon.com/quicksight/latest/developerguide/list-user-groups.html): Use the ListUserGroups operation to list the Quick Sight groups that an Quick Sight user is a member of.
- [ListUsers](https://docs.aws.amazon.com/quicksight/latest/developerguide/list-users.html): The ListUsers operation.
- [RegisterUser](https://docs.aws.amazon.com/quicksight/latest/developerguide/register-user.html): Use the RegisterUser operation to create an Quick Sight user whose identity is associated with the IAM identity or role specified in the request.
- [UpdateUser](https://docs.aws.amazon.com/quicksight/latest/developerguide/update-user.html): Use the UpdateUser operation to update an Quick Sight user.
