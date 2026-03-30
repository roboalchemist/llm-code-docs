# Source: https://docs.aws.amazon.com/resource-explorer/latest/apireference/llms.txt

# AWS Resource Explorer API Reference Guide

> Learn about AWS Resource Explorer and how you can use it to search for and interact with the AWS resources; in your accounts.

- [Welcome](https://docs.aws.amazon.com/resource-explorer/latest/apireference/Welcome.html)
- [Common Errors](https://docs.aws.amazon.com/resource-explorer/latest/apireference/CommonErrors.html)
- [Making API requests](https://docs.aws.amazon.com/resource-explorer/latest/apireference/making-api-requests.html)
- [Common Parameters](https://docs.aws.amazon.com/resource-explorer/latest/apireference/CommonParameters.html)
- [Document history](https://docs.aws.amazon.com/resource-explorer/latest/apireference/doc-history.html)
- [AWS Glossary](https://docs.aws.amazon.com/resource-explorer/latest/apireference/glossary.html)

## [Actions](https://docs.aws.amazon.com/resource-explorer/latest/apireference/API_Operations.html)

- [AssociateDefaultView](https://docs.aws.amazon.com/resource-explorer/latest/apireference/API_AssociateDefaultView.html): Sets the specified view as the default for the AWS Region in which you call this operation.
- [BatchGetView](https://docs.aws.amazon.com/resource-explorer/latest/apireference/API_BatchGetView.html): Retrieves details about a list of views.
- [CreateIndex](https://docs.aws.amazon.com/resource-explorer/latest/apireference/API_CreateIndex.html): Turns on AWS Resource Explorer in the AWS Region in which you called this operation by creating an index.
- [CreateResourceExplorerSetup](https://docs.aws.amazon.com/resource-explorer/latest/apireference/API_CreateResourceExplorerSetup.html): Creates a Resource Explorer setup configuration across multiple AWS Regions.
- [CreateView](https://docs.aws.amazon.com/resource-explorer/latest/apireference/API_CreateView.html): Creates a view that users can query by using the operation.
- [DeleteIndex](https://docs.aws.amazon.com/resource-explorer/latest/apireference/API_DeleteIndex.html): Deletes the specified index and turns off AWS Resource Explorer in the specified AWS Region.
- [DeleteResourceExplorerSetup](https://docs.aws.amazon.com/resource-explorer/latest/apireference/API_DeleteResourceExplorerSetup.html): Deletes a Resource Explorer setup configuration.
- [DeleteView](https://docs.aws.amazon.com/resource-explorer/latest/apireference/API_DeleteView.html): Deletes the specified view.
- [DisassociateDefaultView](https://docs.aws.amazon.com/resource-explorer/latest/apireference/API_DisassociateDefaultView.html): After you call this operation, the affected AWS Region no longer has a default view.
- [GetAccountLevelServiceConfiguration](https://docs.aws.amazon.com/resource-explorer/latest/apireference/API_GetAccountLevelServiceConfiguration.html): Retrieves the status of your account's AWS service access, and validates the service linked role required to access the multi-account search feature.
- [GetDefaultView](https://docs.aws.amazon.com/resource-explorer/latest/apireference/API_GetDefaultView.html): Retrieves the Amazon Resource Name (ARN) of the view that is the default for the AWS Region in which you call this operation.
- [GetIndex](https://docs.aws.amazon.com/resource-explorer/latest/apireference/API_GetIndex.html): Retrieves details about the AWS Resource Explorer index in the AWS Region in which you invoked the operation.
- [GetManagedView](https://docs.aws.amazon.com/resource-explorer/latest/apireference/API_GetManagedView.html): Retrieves details of the specified AWS-managed view.
- [GetResourceExplorerSetup](https://docs.aws.amazon.com/resource-explorer/latest/apireference/API_GetResourceExplorerSetup.html): Retrieves the status and details of a Resource Explorer setup operation.
- [GetServiceIndex](https://docs.aws.amazon.com/resource-explorer/latest/apireference/API_GetServiceIndex.html): Retrieves information about the Resource Explorer index in the current AWS Region.
- [GetServiceView](https://docs.aws.amazon.com/resource-explorer/latest/apireference/API_GetServiceView.html): Retrieves details about a specific Resource Explorer service view.
- [GetView](https://docs.aws.amazon.com/resource-explorer/latest/apireference/API_GetView.html): Retrieves details of the specified view.
- [ListIndexes](https://docs.aws.amazon.com/resource-explorer/latest/apireference/API_ListIndexes.html): Retrieves a list of all of the indexes in AWS Regions that are currently collecting resource information for AWS Resource Explorer.
- [ListIndexesForMembers](https://docs.aws.amazon.com/resource-explorer/latest/apireference/API_ListIndexesForMembers.html): Retrieves a list of a member's indexes in all AWS Regions that are currently collecting resource information for AWS Resource Explorer.
- [ListManagedViews](https://docs.aws.amazon.com/resource-explorer/latest/apireference/API_ListManagedViews.html): Lists the Amazon resource names (ARNs) of the AWS-managed views available in the AWS Region in which you call this operation.
- [ListResources](https://docs.aws.amazon.com/resource-explorer/latest/apireference/API_ListResources.html): Returns a list of resources and their details that match the specified criteria.
- [ListServiceIndexes](https://docs.aws.amazon.com/resource-explorer/latest/apireference/API_ListServiceIndexes.html): Lists all Resource Explorer indexes across the specified AWS Regions.
- [ListServiceViews](https://docs.aws.amazon.com/resource-explorer/latest/apireference/API_ListServiceViews.html): Lists all Resource Explorer service views available in the current AWS account.
- [ListStreamingAccessForServices](https://docs.aws.amazon.com/resource-explorer/latest/apireference/API_ListStreamingAccessForServices.html): Returns a list of AWS services that have been granted streaming access to your Resource Explorer data.
- [ListSupportedResourceTypes](https://docs.aws.amazon.com/resource-explorer/latest/apireference/API_ListSupportedResourceTypes.html): Retrieves a list of all resource types currently supported by AWS Resource Explorer.
- [ListTagsForResource](https://docs.aws.amazon.com/resource-explorer/latest/apireference/API_ListTagsForResource.html): Lists the tags that are attached to the specified resource.
- [ListViews](https://docs.aws.amazon.com/resource-explorer/latest/apireference/API_ListViews.html): Lists the Amazon resource names (ARNs) of the views available in the AWS Region in which you call this operation.
- [Search](https://docs.aws.amazon.com/resource-explorer/latest/apireference/API_Search.html): Searches for resources and displays details about all resources that match the specified criteria.
- [TagResource](https://docs.aws.amazon.com/resource-explorer/latest/apireference/API_TagResource.html): Adds one or more tag key and value pairs to an AWS Resource Explorer view or index.
- [UntagResource](https://docs.aws.amazon.com/resource-explorer/latest/apireference/API_UntagResource.html): Removes one or more tag key and value pairs from an AWS Resource Explorer view or index.
- [UpdateIndexType](https://docs.aws.amazon.com/resource-explorer/latest/apireference/API_UpdateIndexType.html): Changes the type of the index from one of the following types to the other.
- [UpdateView](https://docs.aws.amazon.com/resource-explorer/latest/apireference/API_UpdateView.html): Modifies some of the details of a view.


## [Data Types](https://docs.aws.amazon.com/resource-explorer/latest/apireference/API_Types.html)

- [BatchGetViewError](https://docs.aws.amazon.com/resource-explorer/latest/apireference/API_BatchGetViewError.html): A collection of error messages for any views that AWS Resource Explorer couldn't retrieve details.
- [ErrorDetails](https://docs.aws.amazon.com/resource-explorer/latest/apireference/API_ErrorDetails.html): Contains information about an error that occurred during a Resource Explorer setup operation.
- [IncludedProperty](https://docs.aws.amazon.com/resource-explorer/latest/apireference/API_IncludedProperty.html): Information about an additional property that describes a resource, that you can optionally include in the view.
- [Index](https://docs.aws.amazon.com/resource-explorer/latest/apireference/API_Index.html): An index is the data store used by AWS Resource Explorer to hold information about your AWS resources that the service discovers.
- [IndexStatus](https://docs.aws.amazon.com/resource-explorer/latest/apireference/API_IndexStatus.html): Contains information about the status of a Resource Explorer index operation in a specific Region.
- [ManagedView](https://docs.aws.amazon.com/resource-explorer/latest/apireference/API_ManagedView.html): An AWS-managed view is how other AWS services can access resource information indexed by Resource Explorer for your AWS account or organization with your consent.
- [MemberIndex](https://docs.aws.amazon.com/resource-explorer/latest/apireference/API_MemberIndex.html): An index is the data store used by AWS Resource Explorer to hold information about your AWS resources that the service discovers.
- [OrgConfiguration](https://docs.aws.amazon.com/resource-explorer/latest/apireference/API_OrgConfiguration.html): This is a structure that contains the status of AWS service access, and whether you have a valid service-linked role to enable multi-account search for your organization.
- [RegionStatus](https://docs.aws.amazon.com/resource-explorer/latest/apireference/API_RegionStatus.html): Contains information about the status of Resource Explorer configuration in a specific AWS Region.
- [Resource](https://docs.aws.amazon.com/resource-explorer/latest/apireference/API_Resource.html): A resource in AWS that AWS Resource Explorer has discovered, and for which it has stored information in the index of the AWS Region that contains the resource.
- [ResourceCount](https://docs.aws.amazon.com/resource-explorer/latest/apireference/API_ResourceCount.html): Information about the number of results that match the query.
- [ResourceProperty](https://docs.aws.amazon.com/resource-explorer/latest/apireference/API_ResourceProperty.html): A structure that describes a property of a resource.
- [SearchFilter](https://docs.aws.amazon.com/resource-explorer/latest/apireference/API_SearchFilter.html): A search filter defines which resources can be part of a search query result set.
- [ServiceView](https://docs.aws.amazon.com/resource-explorer/latest/apireference/API_ServiceView.html): Contains the configuration and properties of a Resource Explorer service view.
- [StreamingAccessDetails](https://docs.aws.amazon.com/resource-explorer/latest/apireference/API_StreamingAccessDetails.html): Contains information about an AWS service that has been granted streaming access to your Resource Explorer data.
- [SupportedResourceType](https://docs.aws.amazon.com/resource-explorer/latest/apireference/API_SupportedResourceType.html): A structure that describes a resource type supported by AWS Resource Explorer.
- [ValidationExceptionField](https://docs.aws.amazon.com/resource-explorer/latest/apireference/API_ValidationExceptionField.html): A structure that describes a request field with a validation error.
- [View](https://docs.aws.amazon.com/resource-explorer/latest/apireference/API_View.html): A view is a structure that defines a set of filters that provide a view into the information in the AWS Resource Explorer index.
- [ViewStatus](https://docs.aws.amazon.com/resource-explorer/latest/apireference/API_ViewStatus.html): Contains information about the status of a Resource Explorer view operation in a specific Region.
