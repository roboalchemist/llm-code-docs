# Source: https://docs.aws.amazon.com/ram/latest/APIReference/llms.txt

# AWS RAM API Reference

> This is the AWS Resource Access Manager API Reference. This documentation provides descriptions and syntax for each of the actions and data types in AWS RAM. AWS RAM is a service that helps you securely share your AWS resources to other AWS accounts. If you use AWS Organizations to manage your accounts, then you can share your resources with your entire organization or to organizational units (OUs). For supported resource types, you can also share resources with individual AWS Identity and Access Management (IAM) roles and users.

- [Welcome](https://docs.aws.amazon.com/ram/latest/APIReference/Welcome.html)
- [Common Parameters](https://docs.aws.amazon.com/ram/latest/APIReference/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/ram/latest/APIReference/CommonErrors.html)

## [Actions](https://docs.aws.amazon.com/ram/latest/APIReference/API_Operations.html)

- [AcceptResourceShareInvitation](https://docs.aws.amazon.com/ram/latest/APIReference/API_AcceptResourceShareInvitation.html): Accepts an invitation to a resource share from another AWS account.
- [AssociateResourceShare](https://docs.aws.amazon.com/ram/latest/APIReference/API_AssociateResourceShare.html): Adds the specified list of principals, resources, and source constraints to a resource share.
- [AssociateResourceSharePermission](https://docs.aws.amazon.com/ram/latest/APIReference/API_AssociateResourceSharePermission.html): Adds or replaces the AWS RAM permission for a resource type included in a resource share.
- [CreatePermission](https://docs.aws.amazon.com/ram/latest/APIReference/API_CreatePermission.html): Creates a customer managed permission for a specified resource type that you can attach to resource shares.
- [CreatePermissionVersion](https://docs.aws.amazon.com/ram/latest/APIReference/API_CreatePermissionVersion.html): Creates a new version of the specified customer managed permission.
- [CreateResourceShare](https://docs.aws.amazon.com/ram/latest/APIReference/API_CreateResourceShare.html): Creates a resource share.
- [DeletePermission](https://docs.aws.amazon.com/ram/latest/APIReference/API_DeletePermission.html): Deletes the specified customer managed permission in the AWS Region in which you call this operation.
- [DeletePermissionVersion](https://docs.aws.amazon.com/ram/latest/APIReference/API_DeletePermissionVersion.html): Deletes one version of a customer managed permission.
- [DeleteResourceShare](https://docs.aws.amazon.com/ram/latest/APIReference/API_DeleteResourceShare.html): Deletes the specified resource share.
- [DisassociateResourceShare](https://docs.aws.amazon.com/ram/latest/APIReference/API_DisassociateResourceShare.html): Removes the specified principals, resources, or source constraints from participating in the specified resource share.
- [DisassociateResourceSharePermission](https://docs.aws.amazon.com/ram/latest/APIReference/API_DisassociateResourceSharePermission.html): Removes a managed permission from a resource share.
- [EnableSharingWithAwsOrganization](https://docs.aws.amazon.com/ram/latest/APIReference/API_EnableSharingWithAwsOrganization.html): Enables resource sharing within your organization in AWS Organizations.
- [GetPermission](https://docs.aws.amazon.com/ram/latest/APIReference/API_GetPermission.html): Retrieves the contents of a managed permission in JSON format.
- [GetResourcePolicies](https://docs.aws.amazon.com/ram/latest/APIReference/API_GetResourcePolicies.html): Retrieves the resource policies for the specified resources that you own and have shared.
- [GetResourceShareAssociations](https://docs.aws.amazon.com/ram/latest/APIReference/API_GetResourceShareAssociations.html): Retrieves the lists of resources and principals that associated for resource shares that you own.
- [GetResourceShareInvitations](https://docs.aws.amazon.com/ram/latest/APIReference/API_GetResourceShareInvitations.html): Retrieves details about invitations that you have received for resource shares.
- [GetResourceShares](https://docs.aws.amazon.com/ram/latest/APIReference/API_GetResourceShares.html): Retrieves details about the resource shares that you own or that are shared with you.
- [ListPendingInvitationResources](https://docs.aws.amazon.com/ram/latest/APIReference/API_ListPendingInvitationResources.html): Lists the resources in a resource share that is shared with you but for which the invitation is still PENDING.
- [ListPermissionAssociations](https://docs.aws.amazon.com/ram/latest/APIReference/API_ListPermissionAssociations.html): Lists information about the managed permission and its associations to any resource shares that use this managed permission.
- [ListPermissions](https://docs.aws.amazon.com/ram/latest/APIReference/API_ListPermissions.html): Retrieves a list of available AWS RAM permissions that you can use for the supported resource types.
- [ListPermissionVersions](https://docs.aws.amazon.com/ram/latest/APIReference/API_ListPermissionVersions.html): Lists the available versions of the specified AWS RAM permission.
- [ListPrincipals](https://docs.aws.amazon.com/ram/latest/APIReference/API_ListPrincipals.html): Lists the principals that you are sharing resources with or that are sharing resources with you.
- [ListReplacePermissionAssociationsWork](https://docs.aws.amazon.com/ram/latest/APIReference/API_ListReplacePermissionAssociationsWork.html): Retrieves the current status of the asynchronous tasks performed by AWS RAM when you perform the operation.
- [ListResources](https://docs.aws.amazon.com/ram/latest/APIReference/API_ListResources.html): Lists the resources that you added to a resource share or the resources that are shared with you.
- [ListResourceSharePermissions](https://docs.aws.amazon.com/ram/latest/APIReference/API_ListResourceSharePermissions.html): Lists the AWS RAM permissions that are associated with a resource share.
- [ListResourceTypes](https://docs.aws.amazon.com/ram/latest/APIReference/API_ListResourceTypes.html): Lists the resource types that can be shared by AWS RAM.
- [ListSourceAssociations](https://docs.aws.amazon.com/ram/latest/APIReference/API_ListSourceAssociations.html): Lists source associations for resource shares.
- [PromotePermissionCreatedFromPolicy](https://docs.aws.amazon.com/ram/latest/APIReference/API_PromotePermissionCreatedFromPolicy.html): When you attach a resource-based policy to a resource, AWS RAM automatically creates a resource share of featureSet=CREATED_FROM_POLICY with a managed permission that has the same IAM permissions as the original resource-based policy.
- [PromoteResourceShareCreatedFromPolicy](https://docs.aws.amazon.com/ram/latest/APIReference/API_PromoteResourceShareCreatedFromPolicy.html): When you attach a resource-based policy to a resource, AWS RAM automatically creates a resource share of featureSet=CREATED_FROM_POLICY with a managed permission that has the same IAM permissions as the original resource-based policy.
- [RejectResourceShareInvitation](https://docs.aws.amazon.com/ram/latest/APIReference/API_RejectResourceShareInvitation.html): Rejects an invitation to a resource share from another AWS account.
- [ReplacePermissionAssociations](https://docs.aws.amazon.com/ram/latest/APIReference/API_ReplacePermissionAssociations.html): Updates all resource shares that use a managed permission to a different managed permission.
- [SetDefaultPermissionVersion](https://docs.aws.amazon.com/ram/latest/APIReference/API_SetDefaultPermissionVersion.html): Designates the specified version number as the default version for the specified customer managed permission.
- [TagResource](https://docs.aws.amazon.com/ram/latest/APIReference/API_TagResource.html): Adds the specified tag keys and values to a resource share or managed permission.
- [UntagResource](https://docs.aws.amazon.com/ram/latest/APIReference/API_UntagResource.html): Removes the specified tag key and value pairs from the specified resource share or managed permission.
- [UpdateResourceShare](https://docs.aws.amazon.com/ram/latest/APIReference/API_UpdateResourceShare.html): Modifies some of the properties of the specified resource share.


## [Data Types](https://docs.aws.amazon.com/ram/latest/APIReference/API_Types.html)

- [AssociatedPermission](https://docs.aws.amazon.com/ram/latest/APIReference/API_AssociatedPermission.html): An object that describes a managed permission associated with a resource share.
- [AssociatedSource](https://docs.aws.amazon.com/ram/latest/APIReference/API_AssociatedSource.html): Information about a source association in a resource share.
- [Principal](https://docs.aws.amazon.com/ram/latest/APIReference/API_Principal.html): Describes a principal for use with AWS Resource Access Manager.
- [ReplacePermissionAssociationsWork](https://docs.aws.amazon.com/ram/latest/APIReference/API_ReplacePermissionAssociationsWork.html): A structure that represents the background work that AWS RAM performs when you invoke the operation.
- [Resource](https://docs.aws.amazon.com/ram/latest/APIReference/API_Resource.html): Describes a resource associated with a resource share in AWS RAM.
- [ResourceShare](https://docs.aws.amazon.com/ram/latest/APIReference/API_ResourceShare.html): Describes a resource share in AWS RAM.
- [ResourceShareAssociation](https://docs.aws.amazon.com/ram/latest/APIReference/API_ResourceShareAssociation.html): Describes an association between a resource share and either a principal or a resource.
- [ResourceShareConfiguration](https://docs.aws.amazon.com/ram/latest/APIReference/API_ResourceShareConfiguration.html): The configuration of the resource share
- [ResourceShareInvitation](https://docs.aws.amazon.com/ram/latest/APIReference/API_ResourceShareInvitation.html): Describes an invitation for an AWS account to join a resource share.
- [ResourceSharePermissionDetail](https://docs.aws.amazon.com/ram/latest/APIReference/API_ResourceSharePermissionDetail.html): Information about a AWS RAM managed permission.
- [ResourceSharePermissionSummary](https://docs.aws.amazon.com/ram/latest/APIReference/API_ResourceSharePermissionSummary.html): Information about an AWS RAM permission.
- [ServiceNameAndResourceType](https://docs.aws.amazon.com/ram/latest/APIReference/API_ServiceNameAndResourceType.html): Information about a shareable resource type and the AWS service to which resources of that type belong.
- [Tag](https://docs.aws.amazon.com/ram/latest/APIReference/API_Tag.html): A structure containing a tag.
- [TagFilter](https://docs.aws.amazon.com/ram/latest/APIReference/API_TagFilter.html): A tag key and optional list of possible values that you can use to filter results for tagged resources.
