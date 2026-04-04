# Source: https://docs.aws.amazon.com/outposts/latest/APIReference/llms.txt

# AWS Outposts API Reference

> AWS Outposts is a fully managed service that extends AWS infrastructure, APIs, and tools to customer premises. By providing local access to AWS managed infrastructure, AWS Outposts enables customers to build and run applications on premises using the same programming interfaces as in AWS Regions, while using local compute and storage resources for lower latency and local data processing needs.

- [Welcome](https://docs.aws.amazon.com/outposts/latest/APIReference/Welcome.html)
- [Common Parameters](https://docs.aws.amazon.com/outposts/latest/APIReference/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/outposts/latest/APIReference/CommonErrors.html)

## [Actions](https://docs.aws.amazon.com/outposts/latest/APIReference/API_Operations.html)

- [CancelCapacityTask](https://docs.aws.amazon.com/outposts/latest/APIReference/API_CancelCapacityTask.html): Cancels the capacity task.
- [CancelOrder](https://docs.aws.amazon.com/outposts/latest/APIReference/API_CancelOrder.html): Cancels the specified order for an Outpost.
- [CreateOrder](https://docs.aws.amazon.com/outposts/latest/APIReference/API_CreateOrder.html): Creates an order for an Outpost.
- [CreateOutpost](https://docs.aws.amazon.com/outposts/latest/APIReference/API_CreateOutpost.html): Creates an Outpost.
- [CreateSite](https://docs.aws.amazon.com/outposts/latest/APIReference/API_CreateSite.html): Creates a site for an Outpost.
- [DeleteOutpost](https://docs.aws.amazon.com/outposts/latest/APIReference/API_DeleteOutpost.html): Deletes the specified Outpost.
- [DeleteSite](https://docs.aws.amazon.com/outposts/latest/APIReference/API_DeleteSite.html): Deletes the specified site.
- [GetCapacityTask](https://docs.aws.amazon.com/outposts/latest/APIReference/API_GetCapacityTask.html): Gets details of the specified capacity task.
- [GetCatalogItem](https://docs.aws.amazon.com/outposts/latest/APIReference/API_GetCatalogItem.html): Gets information about the specified catalog item.
- [GetConnection](https://docs.aws.amazon.com/outposts/latest/APIReference/API_GetConnection.html)
- [GetOrder](https://docs.aws.amazon.com/outposts/latest/APIReference/API_GetOrder.html): Gets information about the specified order.
- [GetOutpost](https://docs.aws.amazon.com/outposts/latest/APIReference/API_GetOutpost.html): Gets information about the specified Outpost.
- [GetOutpostBillingInformation](https://docs.aws.amazon.com/outposts/latest/APIReference/API_GetOutpostBillingInformation.html): Gets current and historical billing information about the specified Outpost.
- [GetOutpostInstanceTypes](https://docs.aws.amazon.com/outposts/latest/APIReference/API_GetOutpostInstanceTypes.html): Gets the instance types for the specified Outpost.
- [GetOutpostSupportedInstanceTypes](https://docs.aws.amazon.com/outposts/latest/APIReference/API_GetOutpostSupportedInstanceTypes.html): Gets the instance types that an Outpost can support in InstanceTypeCapacity.
- [GetSite](https://docs.aws.amazon.com/outposts/latest/APIReference/API_GetSite.html): Gets information about the specified Outpost site.
- [GetSiteAddress](https://docs.aws.amazon.com/outposts/latest/APIReference/API_GetSiteAddress.html): Gets the site address of the specified site.
- [ListAssetInstances](https://docs.aws.amazon.com/outposts/latest/APIReference/API_ListAssetInstances.html): A list of Amazon EC2 instances, belonging to all accounts, running on the specified Outpost.
- [ListAssets](https://docs.aws.amazon.com/outposts/latest/APIReference/API_ListAssets.html): Lists the hardware assets for the specified Outpost.
- [ListBlockingInstancesForCapacityTask](https://docs.aws.amazon.com/outposts/latest/APIReference/API_ListBlockingInstancesForCapacityTask.html): A list of Amazon EC2 instances running on the Outpost and belonging to the account that initiated the capacity task.
- [ListCapacityTasks](https://docs.aws.amazon.com/outposts/latest/APIReference/API_ListCapacityTasks.html): Lists the capacity tasks for your AWS account.
- [ListCatalogItems](https://docs.aws.amazon.com/outposts/latest/APIReference/API_ListCatalogItems.html): Lists the items in the catalog.
- [ListOrders](https://docs.aws.amazon.com/outposts/latest/APIReference/API_ListOrders.html): Lists the Outpost orders for your AWS account.
- [ListOutposts](https://docs.aws.amazon.com/outposts/latest/APIReference/API_ListOutposts.html): Lists the Outposts for your AWS account.
- [ListSites](https://docs.aws.amazon.com/outposts/latest/APIReference/API_ListSites.html): Lists the Outpost sites for your AWS account.
- [ListTagsForResource](https://docs.aws.amazon.com/outposts/latest/APIReference/API_ListTagsForResource.html): Lists the tags for the specified resource.
- [StartCapacityTask](https://docs.aws.amazon.com/outposts/latest/APIReference/API_StartCapacityTask.html): Starts the specified capacity task.
- [StartConnection](https://docs.aws.amazon.com/outposts/latest/APIReference/API_StartConnection.html)
- [StartOutpostDecommission](https://docs.aws.amazon.com/outposts/latest/APIReference/API_StartOutpostDecommission.html): Starts the decommission process to return the Outposts racks or servers.
- [TagResource](https://docs.aws.amazon.com/outposts/latest/APIReference/API_TagResource.html): Adds tags to the specified resource.
- [UntagResource](https://docs.aws.amazon.com/outposts/latest/APIReference/API_UntagResource.html): Removes tags from the specified resource.
- [UpdateOutpost](https://docs.aws.amazon.com/outposts/latest/APIReference/API_UpdateOutpost.html): Updates an Outpost.
- [UpdateSite](https://docs.aws.amazon.com/outposts/latest/APIReference/API_UpdateSite.html): Updates the specified site.
- [UpdateSiteAddress](https://docs.aws.amazon.com/outposts/latest/APIReference/API_UpdateSiteAddress.html): Updates the address of the specified site.
- [UpdateSiteRackPhysicalProperties](https://docs.aws.amazon.com/outposts/latest/APIReference/API_UpdateSiteRackPhysicalProperties.html): Update the physical and logistical details for a rack at a site.


## [Data Types](https://docs.aws.amazon.com/outposts/latest/APIReference/API_Types.html)

- [Address](https://docs.aws.amazon.com/outposts/latest/APIReference/API_Address.html): Information about an address.
- [AssetInfo](https://docs.aws.amazon.com/outposts/latest/APIReference/API_AssetInfo.html): Information about hardware assets.
- [AssetInstance](https://docs.aws.amazon.com/outposts/latest/APIReference/API_AssetInstance.html): An Amazon EC2 instance.
- [AssetInstanceTypeCapacity](https://docs.aws.amazon.com/outposts/latest/APIReference/API_AssetInstanceTypeCapacity.html): The capacity for each instance type.
- [AssetLocation](https://docs.aws.amazon.com/outposts/latest/APIReference/API_AssetLocation.html): Information about the position of the asset in a rack.
- [BlockingInstance](https://docs.aws.amazon.com/outposts/latest/APIReference/API_BlockingInstance.html): A running Amazon EC2 instance that can be stopped to free up capacity needed to run the capacity task.
- [CapacityTaskFailure](https://docs.aws.amazon.com/outposts/latest/APIReference/API_CapacityTaskFailure.html): The capacity tasks that failed.
- [CapacityTaskSummary](https://docs.aws.amazon.com/outposts/latest/APIReference/API_CapacityTaskSummary.html): The summary of the capacity task.
- [CatalogItem](https://docs.aws.amazon.com/outposts/latest/APIReference/API_CatalogItem.html): Information about a catalog item.
- [ComputeAttributes](https://docs.aws.amazon.com/outposts/latest/APIReference/API_ComputeAttributes.html): Information about compute hardware assets.
- [ConnectionDetails](https://docs.aws.amazon.com/outposts/latest/APIReference/API_ConnectionDetails.html): Information about a connection.
- [EC2Capacity](https://docs.aws.amazon.com/outposts/latest/APIReference/API_EC2Capacity.html): Information about EC2 capacity.
- [InstancesToExclude](https://docs.aws.amazon.com/outposts/latest/APIReference/API_InstancesToExclude.html): User-specified instances that must not be stopped.
- [InstanceTypeCapacity](https://docs.aws.amazon.com/outposts/latest/APIReference/API_InstanceTypeCapacity.html): The instance type that you specify determines the combination of CPU, memory, storage, and networking capacity.
- [InstanceTypeItem](https://docs.aws.amazon.com/outposts/latest/APIReference/API_InstanceTypeItem.html): Information about an instance type.
- [LineItem](https://docs.aws.amazon.com/outposts/latest/APIReference/API_LineItem.html): Information about a line item.
- [LineItemAssetInformation](https://docs.aws.amazon.com/outposts/latest/APIReference/API_LineItemAssetInformation.html): Information about a line item asset.
- [LineItemRequest](https://docs.aws.amazon.com/outposts/latest/APIReference/API_LineItemRequest.html): Information about a line item request.
- [Order](https://docs.aws.amazon.com/outposts/latest/APIReference/API_Order.html): Information about an order.
- [OrderSummary](https://docs.aws.amazon.com/outposts/latest/APIReference/API_OrderSummary.html): A summary of line items in your order.
- [Outpost](https://docs.aws.amazon.com/outposts/latest/APIReference/API_Outpost.html): Information about an Outpost.
- [RackPhysicalProperties](https://docs.aws.amazon.com/outposts/latest/APIReference/API_RackPhysicalProperties.html): Information about the physical and logistical details for racks at sites.
- [ShipmentInformation](https://docs.aws.amazon.com/outposts/latest/APIReference/API_ShipmentInformation.html): Information about a line item shipment.
- [Site](https://docs.aws.amazon.com/outposts/latest/APIReference/API_Site.html): Information about a site.
- [Subscription](https://docs.aws.amazon.com/outposts/latest/APIReference/API_Subscription.html): Provides information about your AWS Outposts subscriptions.
