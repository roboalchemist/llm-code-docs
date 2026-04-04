# Source: https://docs.aws.amazon.com/ARG/latest/APIReference/llms.txt

# AWS Resource Groups Resource Groups API Reference

> AWS Resource Groups lets you organize AWS resources into groups, tag resources using virtually any criteria, and manage, monitor, and automate tasks on grouped resources.

- [Welcome](https://docs.aws.amazon.com/ARG/latest/APIReference/Welcome.html)
- [Making API requests](https://docs.aws.amazon.com/ARG/latest/APIReference/making-api-requests.html)
- [Common Parameters](https://docs.aws.amazon.com/ARG/latest/APIReference/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/ARG/latest/APIReference/CommonErrors.html)

## [Actions](https://docs.aws.amazon.com/ARG/latest/APIReference/API_Operations.html)

- [CancelTagSyncTask](https://docs.aws.amazon.com/ARG/latest/APIReference/API_CancelTagSyncTask.html): Cancels the specified tag-sync task.
- [CreateGroup](https://docs.aws.amazon.com/ARG/latest/APIReference/API_CreateGroup.html): Creates a resource group with the specified name and description.
- [DeleteGroup](https://docs.aws.amazon.com/ARG/latest/APIReference/API_DeleteGroup.html): Deletes the specified resource group.
- [GetAccountSettings](https://docs.aws.amazon.com/ARG/latest/APIReference/API_GetAccountSettings.html): Retrieves the current status of optional features in Resource Groups.
- [GetGroup](https://docs.aws.amazon.com/ARG/latest/APIReference/API_GetGroup.html): Returns information about a specified resource group.
- [GetGroupConfiguration](https://docs.aws.amazon.com/ARG/latest/APIReference/API_GetGroupConfiguration.html): Retrieves the service configuration associated with the specified resource group.
- [GetGroupQuery](https://docs.aws.amazon.com/ARG/latest/APIReference/API_GetGroupQuery.html): Retrieves the resource query associated with the specified resource group.
- [GetTags](https://docs.aws.amazon.com/ARG/latest/APIReference/API_GetTags.html): Returns a list of tags that are associated with a resource group, specified by an Amazon resource name (ARN).
- [GetTagSyncTask](https://docs.aws.amazon.com/ARG/latest/APIReference/API_GetTagSyncTask.html): Returns information about a specified tag-sync task.
- [GroupResources](https://docs.aws.amazon.com/ARG/latest/APIReference/API_GroupResources.html): Adds the specified resources to the specified group.
- [ListGroupingStatuses](https://docs.aws.amazon.com/ARG/latest/APIReference/API_ListGroupingStatuses.html): Returns the status of the last grouping or ungrouping action for each resource in the specified application group.
- [ListGroupResources](https://docs.aws.amazon.com/ARG/latest/APIReference/API_ListGroupResources.html): Returns a list of Amazon resource names (ARNs) of the resources that are members of a specified resource group.
- [ListGroups](https://docs.aws.amazon.com/ARG/latest/APIReference/API_ListGroups.html): Returns a list of existing Resource Groups in your account.
- [ListTagSyncTasks](https://docs.aws.amazon.com/ARG/latest/APIReference/API_ListTagSyncTasks.html): Returns a list of tag-sync tasks.
- [PutGroupConfiguration](https://docs.aws.amazon.com/ARG/latest/APIReference/API_PutGroupConfiguration.html): Attaches a service configuration to the specified group.
- [SearchResources](https://docs.aws.amazon.com/ARG/latest/APIReference/API_SearchResources.html): Returns a list of AWS resource identifiers that matches the specified query.
- [StartTagSyncTask](https://docs.aws.amazon.com/ARG/latest/APIReference/API_StartTagSyncTask.html): Creates a new tag-sync task to onboard and sync resources tagged with a specific tag key-value pair to an application.
- [Tag](https://docs.aws.amazon.com/ARG/latest/APIReference/API_Tag.html): Adds tags to a resource group with the specified Amazon resource name (ARN).
- [UngroupResources](https://docs.aws.amazon.com/ARG/latest/APIReference/API_UngroupResources.html): Removes the specified resources from the specified group.
- [Untag](https://docs.aws.amazon.com/ARG/latest/APIReference/API_Untag.html): Deletes tags from a specified resource group.
- [UpdateAccountSettings](https://docs.aws.amazon.com/ARG/latest/APIReference/API_UpdateAccountSettings.html): Turns on or turns off optional features in Resource Groups.
- [UpdateGroup](https://docs.aws.amazon.com/ARG/latest/APIReference/API_UpdateGroup.html): Updates the description for an existing group.
- [UpdateGroupQuery](https://docs.aws.amazon.com/ARG/latest/APIReference/API_UpdateGroupQuery.html): Updates the resource query of a group.


## [Data Types](https://docs.aws.amazon.com/ARG/latest/APIReference/API_Types.html)

- [AccountSettings](https://docs.aws.amazon.com/ARG/latest/APIReference/API_AccountSettings.html): The Resource Groups settings for this AWS account.
- [FailedResource](https://docs.aws.amazon.com/ARG/latest/APIReference/API_FailedResource.html): A resource that failed to be added to or removed from a group.
- [Group](https://docs.aws.amazon.com/ARG/latest/APIReference/API_Group.html): A resource group that contains AWS resources.
- [GroupConfiguration](https://docs.aws.amazon.com/ARG/latest/APIReference/API_GroupConfiguration.html): A service configuration associated with a resource group.
- [GroupConfigurationItem](https://docs.aws.amazon.com/ARG/latest/APIReference/API_GroupConfigurationItem.html): An item in a group configuration.
- [GroupConfigurationParameter](https://docs.aws.amazon.com/ARG/latest/APIReference/API_GroupConfigurationParameter.html): A parameter for a group configuration item.
- [GroupFilter](https://docs.aws.amazon.com/ARG/latest/APIReference/API_GroupFilter.html): A filter collection that you can use to restrict the results from a List operation to only those you want to include.
- [GroupIdentifier](https://docs.aws.amazon.com/ARG/latest/APIReference/API_GroupIdentifier.html): The unique identifiers for a resource group.
- [GroupingStatusesItem](https://docs.aws.amazon.com/ARG/latest/APIReference/API_GroupingStatusesItem.html): The information about a grouping or ungrouping resource action.
- [GroupQuery](https://docs.aws.amazon.com/ARG/latest/APIReference/API_GroupQuery.html): A mapping of a query attached to a resource group that determines the AWS resources that are members of the group.
- [ListGroupingStatusesFilter](https://docs.aws.amazon.com/ARG/latest/APIReference/API_ListGroupingStatusesFilter.html): A filter name and value pair that is used to obtain more specific results from the list of grouping statuses.
- [ListGroupResourcesItem](https://docs.aws.amazon.com/ARG/latest/APIReference/API_ListGroupResourcesItem.html): A structure returned by the operation that contains identity and group membership status information for one of the resources in the group.
- [ListTagSyncTasksFilter](https://docs.aws.amazon.com/ARG/latest/APIReference/API_ListTagSyncTasksFilter.html): Returns tag-sync tasks filtered by the Amazon resource name (ARN) or name of a specified application group.
- [PendingResource](https://docs.aws.amazon.com/ARG/latest/APIReference/API_PendingResource.html): A structure that identifies a resource that is currently pending addition to the group as a member.
- [QueryError](https://docs.aws.amazon.com/ARG/latest/APIReference/API_QueryError.html): A two-part error structure that can occur in ListGroupResources or SearchResources.
- [ResourceFilter](https://docs.aws.amazon.com/ARG/latest/APIReference/API_ResourceFilter.html): A filter name and value pair that is used to obtain more specific results from a list of resources.
- [ResourceIdentifier](https://docs.aws.amazon.com/ARG/latest/APIReference/API_ResourceIdentifier.html): A structure that contains the ARN of a resource and its resource type.
- [ResourceQuery](https://docs.aws.amazon.com/ARG/latest/APIReference/API_ResourceQuery.html): The query you can use to define a resource group or a search for resources.
- [ResourceStatus](https://docs.aws.amazon.com/ARG/latest/APIReference/API_ResourceStatus.html): A structure that identifies the current group membership status for a resource.
- [TagSyncTaskItem](https://docs.aws.amazon.com/ARG/latest/APIReference/API_TagSyncTaskItem.html): The Amazon resource name (ARN) of the tag-sync task.
