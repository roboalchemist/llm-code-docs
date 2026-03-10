# Source: https://docs.aws.amazon.com/workmail/latest/APIReference/llms.txt

# Amazon WorkMail API Reference

## [Amazon WorkMail](https://docs.aws.amazon.com/workmail/latest/APIReference/Welcome_Amazon_WorkMail.html)

WorkMail is a secure, managed business email and calendaring service with support for existing desktop and mobile email clients. You can access your email, contacts, and calendars using Microsoft Outlook, your browser, or other native iOS and Android email applications. You can integrate WorkMail with your existing corporate directory and control both the keys that encrypt your data and the location in which your data is stored.

The WorkMail API is designed for the following scenarios:

- Listing and describing organizations

- Managing users

- Managing groups

- Managing resources

All WorkMail API operations are Amazon-authenticated and certificate-signed. They not only require the use of the AWS SDK, but also allow for the exclusive use of AWS Identity and Access Management users and roles to help facilitate access, trust, and permission policies. By creating a role and allowing an IAM user to access the WorkMail site, the IAM user gains full administrative visibility into the entire WorkMail organization (or as set in the IAM policy). This includes, but is not limited to, the ability to create, update, and delete users, groups, and resources. This allows developers to perform the scenarios listed above, as well as give users the ability to grant access on a selective basis using the IAM model.

### Actions

- [AssociateDelegateToResource](https://docs.aws.amazon.com/workmail/latest/APIReference/API_AssociateDelegateToResource.html): Adds a member (user or group) to the resource's set of delegates.
- [AssociateMemberToGroup](https://docs.aws.amazon.com/workmail/latest/APIReference/API_AssociateMemberToGroup.html): Adds a member (user or group) to the group's set.
- [AssumeImpersonationRole](https://docs.aws.amazon.com/workmail/latest/APIReference/API_AssumeImpersonationRole.html): Assumes an impersonation role for the given WorkMail organization.
- [CancelMailboxExportJob](https://docs.aws.amazon.com/workmail/latest/APIReference/API_CancelMailboxExportJob.html): Cancels a mailbox export job.
- [CreateAlias](https://docs.aws.amazon.com/workmail/latest/APIReference/API_CreateAlias.html): Adds an alias to the set of a given member (user or group) of WorkMail.
- [CreateAvailabilityConfiguration](https://docs.aws.amazon.com/workmail/latest/APIReference/API_CreateAvailabilityConfiguration.html): Creates an AvailabilityConfiguration for the given WorkMail organization and domain.
- [CreateGroup](https://docs.aws.amazon.com/workmail/latest/APIReference/API_CreateGroup.html): Creates a group that can be used in WorkMail by calling the operation.
- [CreateIdentityCenterApplication](https://docs.aws.amazon.com/workmail/latest/APIReference/API_CreateIdentityCenterApplication.html): Creates the WorkMail application in IAM Identity Center that can be used later in the WorkMail - IdC integration.
- [CreateImpersonationRole](https://docs.aws.amazon.com/workmail/latest/APIReference/API_CreateImpersonationRole.html): Creates an impersonation role for the given WorkMail organization.
- [CreateMobileDeviceAccessRule](https://docs.aws.amazon.com/workmail/latest/APIReference/API_CreateMobileDeviceAccessRule.html): Creates a new mobile device access rule for the specified WorkMail organization.
- [CreateOrganization](https://docs.aws.amazon.com/workmail/latest/APIReference/API_CreateOrganization.html): Creates a new WorkMail organization.
- [CreateResource](https://docs.aws.amazon.com/workmail/latest/APIReference/API_CreateResource.html): Creates a new WorkMail resource.
- [CreateUser](https://docs.aws.amazon.com/workmail/latest/APIReference/API_CreateUser.html): Creates a user who can be used in WorkMail by calling the operation.
- [DeleteAccessControlRule](https://docs.aws.amazon.com/workmail/latest/APIReference/API_DeleteAccessControlRule.html): Deletes an access control rule for the specified WorkMail organization.
- [DeleteAlias](https://docs.aws.amazon.com/workmail/latest/APIReference/API_DeleteAlias.html): Remove one or more specified aliases from a set of aliases for a given user.
- [DeleteAvailabilityConfiguration](https://docs.aws.amazon.com/workmail/latest/APIReference/API_DeleteAvailabilityConfiguration.html): Deletes the AvailabilityConfiguration for the given WorkMail organization and domain.
- [DeleteEmailMonitoringConfiguration](https://docs.aws.amazon.com/workmail/latest/APIReference/API_DeleteEmailMonitoringConfiguration.html): Deletes the email monitoring configuration for a specified organization.
- [DeleteGroup](https://docs.aws.amazon.com/workmail/latest/APIReference/API_DeleteGroup.html): Deletes a group from WorkMail.
- [DeleteIdentityCenterApplication](https://docs.aws.amazon.com/workmail/latest/APIReference/API_DeleteIdentityCenterApplication.html): Deletes the IAM Identity Center application from WorkMail.
- [DeleteIdentityProviderConfiguration](https://docs.aws.amazon.com/workmail/latest/APIReference/API_DeleteIdentityProviderConfiguration.html): Disables the integration between IdC and WorkMail.
- [DeleteImpersonationRole](https://docs.aws.amazon.com/workmail/latest/APIReference/API_DeleteImpersonationRole.html): Deletes an impersonation role for the given WorkMail organization.
- [DeleteMailboxPermissions](https://docs.aws.amazon.com/workmail/latest/APIReference/API_DeleteMailboxPermissions.html): Deletes permissions granted to a member (user or group).
- [DeleteMobileDeviceAccessOverride](https://docs.aws.amazon.com/workmail/latest/APIReference/API_DeleteMobileDeviceAccessOverride.html): Deletes the mobile device access override for the given WorkMail organization, user, and device.
- [DeleteMobileDeviceAccessRule](https://docs.aws.amazon.com/workmail/latest/APIReference/API_DeleteMobileDeviceAccessRule.html): Deletes a mobile device access rule for the specified WorkMail organization.
- [DeleteOrganization](https://docs.aws.amazon.com/workmail/latest/APIReference/API_DeleteOrganization.html): Deletes an WorkMail organization and all underlying AWS resources managed by WorkMail as part of the organization.
- [DeletePersonalAccessToken](https://docs.aws.amazon.com/workmail/latest/APIReference/API_DeletePersonalAccessToken.html): Deletes the Personal Access Token from the provided WorkMail Organization.
- [DeleteResource](https://docs.aws.amazon.com/workmail/latest/APIReference/API_DeleteResource.html): Deletes the specified resource.
- [DeleteRetentionPolicy](https://docs.aws.amazon.com/workmail/latest/APIReference/API_DeleteRetentionPolicy.html): Deletes the specified retention policy from the specified organization.
- [DeleteUser](https://docs.aws.amazon.com/workmail/latest/APIReference/API_DeleteUser.html): Deletes a user from WorkMail and all subsequent systems.
- [DeregisterFromWorkMail](https://docs.aws.amazon.com/workmail/latest/APIReference/API_DeregisterFromWorkMail.html): Mark a user, group, or resource as no longer used in WorkMail.
- [DeregisterMailDomain](https://docs.aws.amazon.com/workmail/latest/APIReference/API_DeregisterMailDomain.html): Removes a domain from WorkMail, stops email routing to WorkMail, and removes the authorization allowing WorkMail use.
- [DescribeEmailMonitoringConfiguration](https://docs.aws.amazon.com/workmail/latest/APIReference/API_DescribeEmailMonitoringConfiguration.html): Describes the current email monitoring configuration for a specified organization.
- [DescribeEntity](https://docs.aws.amazon.com/workmail/latest/APIReference/API_DescribeEntity.html): Returns basic details about an entity in WorkMail.
- [DescribeGroup](https://docs.aws.amazon.com/workmail/latest/APIReference/API_DescribeGroup.html): Returns the data available for the group.
- [DescribeIdentityProviderConfiguration](https://docs.aws.amazon.com/workmail/latest/APIReference/API_DescribeIdentityProviderConfiguration.html): Returns detailed information on the current IdC setup for the WorkMail organization.
- [DescribeInboundDmarcSettings](https://docs.aws.amazon.com/workmail/latest/APIReference/API_DescribeInboundDmarcSettings.html): Lists the settings in a DMARC policy for a specified organization.
- [DescribeMailboxExportJob](https://docs.aws.amazon.com/workmail/latest/APIReference/API_DescribeMailboxExportJob.html): Describes the current status of a mailbox export job.
- [DescribeOrganization](https://docs.aws.amazon.com/workmail/latest/APIReference/API_DescribeOrganization.html): Provides more information regarding a given organization based on its identifier.
- [DescribeResource](https://docs.aws.amazon.com/workmail/latest/APIReference/API_DescribeResource.html): Returns the data available for the resource.
- [DescribeUser](https://docs.aws.amazon.com/workmail/latest/APIReference/API_DescribeUser.html): Provides information regarding the user.
- [DisassociateDelegateFromResource](https://docs.aws.amazon.com/workmail/latest/APIReference/API_DisassociateDelegateFromResource.html): Removes a member from the resource's set of delegates.
- [DisassociateMemberFromGroup](https://docs.aws.amazon.com/workmail/latest/APIReference/API_DisassociateMemberFromGroup.html): Removes a member from a group.
- [GetAccessControlEffect](https://docs.aws.amazon.com/workmail/latest/APIReference/API_GetAccessControlEffect.html): Gets the effects of an organization's access control rules as they apply to a specified IPv4 address, access protocol action, and user ID or impersonation role ID.
- [GetDefaultRetentionPolicy](https://docs.aws.amazon.com/workmail/latest/APIReference/API_GetDefaultRetentionPolicy.html): Gets the default retention policy details for the specified organization.
- [GetImpersonationRole](https://docs.aws.amazon.com/workmail/latest/APIReference/API_GetImpersonationRole.html): Gets the impersonation role details for the given WorkMail organization.
- [GetImpersonationRoleEffect](https://docs.aws.amazon.com/workmail/latest/APIReference/API_GetImpersonationRoleEffect.html): Tests whether the given impersonation role can impersonate a target user.
- [GetMailboxDetails](https://docs.aws.amazon.com/workmail/latest/APIReference/API_GetMailboxDetails.html): Requests a user's mailbox details for a specified organization and user.
- [GetMailDomain](https://docs.aws.amazon.com/workmail/latest/APIReference/API_GetMailDomain.html): Gets details for a mail domain, including domain records required to configure your domain with recommended security.
- [GetMobileDeviceAccessEffect](https://docs.aws.amazon.com/workmail/latest/APIReference/API_GetMobileDeviceAccessEffect.html): Simulates the effect of the mobile device access rules for the given attributes of a sample access event.
- [GetMobileDeviceAccessOverride](https://docs.aws.amazon.com/workmail/latest/APIReference/API_GetMobileDeviceAccessOverride.html): Gets the mobile device access override for the given WorkMail organization, user, and device.
- [GetPersonalAccessTokenMetadata](https://docs.aws.amazon.com/workmail/latest/APIReference/API_GetPersonalAccessTokenMetadata.html): Requests details of a specific Personal Access Token within the WorkMail organization.
- [ListAccessControlRules](https://docs.aws.amazon.com/workmail/latest/APIReference/API_ListAccessControlRules.html): Lists the access control rules for the specified organization.
- [ListAliases](https://docs.aws.amazon.com/workmail/latest/APIReference/API_ListAliases.html): Creates a paginated call to list the aliases associated with a given entity.
- [ListAvailabilityConfigurations](https://docs.aws.amazon.com/workmail/latest/APIReference/API_ListAvailabilityConfigurations.html): List all the AvailabilityConfiguration's for the given WorkMail organization.
- [ListGroupMembers](https://docs.aws.amazon.com/workmail/latest/APIReference/API_ListGroupMembers.html): Returns an overview of the members of a group.
- [ListGroups](https://docs.aws.amazon.com/workmail/latest/APIReference/API_ListGroups.html): Returns summaries of the organization's groups.
- [ListGroupsForEntity](https://docs.aws.amazon.com/workmail/latest/APIReference/API_ListGroupsForEntity.html): Returns all the groups to which an entity belongs.
- [ListImpersonationRoles](https://docs.aws.amazon.com/workmail/latest/APIReference/API_ListImpersonationRoles.html): Lists all the impersonation roles for the given WorkMail organization.
- [ListMailboxExportJobs](https://docs.aws.amazon.com/workmail/latest/APIReference/API_ListMailboxExportJobs.html): Lists the mailbox export jobs started for the specified organization within the last seven days.
- [ListMailboxPermissions](https://docs.aws.amazon.com/workmail/latest/APIReference/API_ListMailboxPermissions.html): Lists the mailbox permissions associated with a user, group, or resource mailbox.
- [ListMailDomains](https://docs.aws.amazon.com/workmail/latest/APIReference/API_ListMailDomains.html): Lists the mail domains in a given WorkMail organization.
- [ListMobileDeviceAccessOverrides](https://docs.aws.amazon.com/workmail/latest/APIReference/API_ListMobileDeviceAccessOverrides.html): Lists all the mobile device access overrides for any given combination of WorkMail organization, user, or device.
- [ListMobileDeviceAccessRules](https://docs.aws.amazon.com/workmail/latest/APIReference/API_ListMobileDeviceAccessRules.html): Lists the mobile device access rules for the specified WorkMail organization.
- [ListOrganizations](https://docs.aws.amazon.com/workmail/latest/APIReference/API_ListOrganizations.html): Returns summaries of the customer's organizations.
- [ListPersonalAccessTokens](https://docs.aws.amazon.com/workmail/latest/APIReference/API_ListPersonalAccessTokens.html): Returns a summary of your Personal Access Tokens.
- [ListResourceDelegates](https://docs.aws.amazon.com/workmail/latest/APIReference/API_ListResourceDelegates.html): Lists the delegates associated with a resource.
- [ListResources](https://docs.aws.amazon.com/workmail/latest/APIReference/API_ListResources.html): Returns summaries of the organization's resources.
- [ListTagsForResource](https://docs.aws.amazon.com/workmail/latest/APIReference/API_ListTagsForResource.html): Lists the tags applied to an WorkMail organization resource.
- [ListUsers](https://docs.aws.amazon.com/workmail/latest/APIReference/API_ListUsers.html): Returns summaries of the organization's users.
- [PutAccessControlRule](https://docs.aws.amazon.com/workmail/latest/APIReference/API_PutAccessControlRule.html): Adds a new access control rule for the specified organization.
- [PutEmailMonitoringConfiguration](https://docs.aws.amazon.com/workmail/latest/APIReference/API_PutEmailMonitoringConfiguration.html): Creates or updates the email monitoring configuration for a specified organization.
- [PutIdentityProviderConfiguration](https://docs.aws.amazon.com/workmail/latest/APIReference/API_PutIdentityProviderConfiguration.html): Enables integration between IAM Identity Center (IdC) and WorkMail to proxy authentication requests for mailbox users.
- [PutInboundDmarcSettings](https://docs.aws.amazon.com/workmail/latest/APIReference/API_PutInboundDmarcSettings.html): Enables or disables a DMARC policy for a given organization.
- [PutMailboxPermissions](https://docs.aws.amazon.com/workmail/latest/APIReference/API_PutMailboxPermissions.html): Sets permissions for a user, group, or resource.
- [PutMobileDeviceAccessOverride](https://docs.aws.amazon.com/workmail/latest/APIReference/API_PutMobileDeviceAccessOverride.html): Creates or updates a mobile device access override for the given WorkMail organization, user, and device.
- [PutRetentionPolicy](https://docs.aws.amazon.com/workmail/latest/APIReference/API_PutRetentionPolicy.html): Puts a retention policy to the specified organization.
- [RegisterMailDomain](https://docs.aws.amazon.com/workmail/latest/APIReference/API_RegisterMailDomain.html): Registers a new domain in WorkMail and SES, and configures it for use by WorkMail.
- [RegisterToWorkMail](https://docs.aws.amazon.com/workmail/latest/APIReference/API_RegisterToWorkMail.html): Registers an existing and disabled user, group, or resource for WorkMail use by associating a mailbox and calendaring capabilities.
- [ResetPassword](https://docs.aws.amazon.com/workmail/latest/APIReference/API_ResetPassword.html): Allows the administrator to reset the password for a user.
- [StartMailboxExportJob](https://docs.aws.amazon.com/workmail/latest/APIReference/API_StartMailboxExportJob.html): Starts a mailbox export job to export MIME-format email messages and calendar items from the specified mailbox to the specified Amazon Simple Storage Service (Amazon S3) bucket.
- [TagResource](https://docs.aws.amazon.com/workmail/latest/APIReference/API_TagResource.html): Applies the specified tags to the specified WorkMailorganization resource.
- [TestAvailabilityConfiguration](https://docs.aws.amazon.com/workmail/latest/APIReference/API_TestAvailabilityConfiguration.html): Performs a test on an availability provider to ensure that access is allowed.
- [UntagResource](https://docs.aws.amazon.com/workmail/latest/APIReference/API_UntagResource.html): Untags the specified tags from the specified WorkMail organization resource.
- [UpdateAvailabilityConfiguration](https://docs.aws.amazon.com/workmail/latest/APIReference/API_UpdateAvailabilityConfiguration.html): Updates an existing AvailabilityConfiguration for the given WorkMail organization and domain.
- [UpdateDefaultMailDomain](https://docs.aws.amazon.com/workmail/latest/APIReference/API_UpdateDefaultMailDomain.html): Updates the default mail domain for an organization.
- [UpdateGroup](https://docs.aws.amazon.com/workmail/latest/APIReference/API_UpdateGroup.html): Updates attributes in a group.
- [UpdateImpersonationRole](https://docs.aws.amazon.com/workmail/latest/APIReference/API_UpdateImpersonationRole.html): Updates an impersonation role for the given WorkMail organization.
- [UpdateMailboxQuota](https://docs.aws.amazon.com/workmail/latest/APIReference/API_UpdateMailboxQuota.html): Updates a user's current mailbox quota for a specified organization and user.
- [UpdateMobileDeviceAccessRule](https://docs.aws.amazon.com/workmail/latest/APIReference/API_UpdateMobileDeviceAccessRule.html): Updates a mobile device access rule for the specified WorkMail organization.
- [UpdatePrimaryEmailAddress](https://docs.aws.amazon.com/workmail/latest/APIReference/API_UpdatePrimaryEmailAddress.html): Updates the primary email for a user, group, or resource.
- [UpdateResource](https://docs.aws.amazon.com/workmail/latest/APIReference/API_UpdateResource.html): Updates data for the resource.
- [UpdateUser](https://docs.aws.amazon.com/workmail/latest/APIReference/API_UpdateUser.html): Updates data for the user.

### Data Types

- [AccessControlRule](https://docs.aws.amazon.com/workmail/latest/APIReference/API_AccessControlRule.html): A rule that controls access to an WorkMail organization.
- [AvailabilityConfiguration](https://docs.aws.amazon.com/workmail/latest/APIReference/API_AvailabilityConfiguration.html): List all the AvailabilityConfiguration's for the given WorkMail organization.
- [BookingOptions](https://docs.aws.amazon.com/workmail/latest/APIReference/API_BookingOptions.html): At least one delegate must be associated to the resource to disable automatic replies from the resource.
- [Delegate](https://docs.aws.amazon.com/workmail/latest/APIReference/API_Delegate.html): The name of the attribute, which is one of the values defined in the UserAttribute enumeration.
- [DnsRecord](https://docs.aws.amazon.com/workmail/latest/APIReference/API_DnsRecord.html): A DNS record uploaded to your DNS provider.
- [Domain](https://docs.aws.amazon.com/workmail/latest/APIReference/API_Domain.html): The domain to associate with an WorkMail organization.
- [EwsAvailabilityProvider](https://docs.aws.amazon.com/workmail/latest/APIReference/API_EwsAvailabilityProvider.html): Describes an EWS based availability provider.
- [FolderConfiguration](https://docs.aws.amazon.com/workmail/latest/APIReference/API_FolderConfiguration.html): The configuration applied to an organization's folders by its retention policy.
- [Group](https://docs.aws.amazon.com/workmail/latest/APIReference/API_Group.html): The representation of an WorkMail group.
- [GroupIdentifier](https://docs.aws.amazon.com/workmail/latest/APIReference/API_GroupIdentifier.html): The identifier that contains the Group ID and name of a group.
- [IdentityCenterConfiguration](https://docs.aws.amazon.com/workmail/latest/APIReference/API_IdentityCenterConfiguration.html): The IAM Identity Center configuration.
- [ImpersonationMatchedRule](https://docs.aws.amazon.com/workmail/latest/APIReference/API_ImpersonationMatchedRule.html): The impersonation rule that matched the input.
- [ImpersonationRole](https://docs.aws.amazon.com/workmail/latest/APIReference/API_ImpersonationRole.html): An impersonation role for the given WorkMail organization.
- [ImpersonationRule](https://docs.aws.amazon.com/workmail/latest/APIReference/API_ImpersonationRule.html): The rules for the given impersonation role.
- [LambdaAvailabilityProvider](https://docs.aws.amazon.com/workmail/latest/APIReference/API_LambdaAvailabilityProvider.html): Describes a Lambda based availability provider.
- [ListGroupsFilters](https://docs.aws.amazon.com/workmail/latest/APIReference/API_ListGroupsFilters.html): Filtering options for ListGroups operation.
- [ListGroupsForEntityFilters](https://docs.aws.amazon.com/workmail/latest/APIReference/API_ListGroupsForEntityFilters.html): Filtering options for ListGroupsForEntity operation.
- [ListResourcesFilters](https://docs.aws.amazon.com/workmail/latest/APIReference/API_ListResourcesFilters.html): Filtering options for ListResources operation.
- [ListUsersFilters](https://docs.aws.amazon.com/workmail/latest/APIReference/API_ListUsersFilters.html): Filtering options for ListUsers operation.
- [MailboxExportJob](https://docs.aws.amazon.com/workmail/latest/APIReference/API_MailboxExportJob.html): The details of a mailbox export job, including the user or resource ID associated with the mailbox and the S3 bucket that the mailbox contents are exported to.
- [MailDomainSummary](https://docs.aws.amazon.com/workmail/latest/APIReference/API_MailDomainSummary.html): The data for a given domain.
- [Member](https://docs.aws.amazon.com/workmail/latest/APIReference/API_Member.html): The representation of a user or group.
- [MobileDeviceAccessMatchedRule](https://docs.aws.amazon.com/workmail/latest/APIReference/API_MobileDeviceAccessMatchedRule.html): The rule that a simulated user matches.
- [MobileDeviceAccessOverride](https://docs.aws.amazon.com/workmail/latest/APIReference/API_MobileDeviceAccessOverride.html): The override object.
- [MobileDeviceAccessRule](https://docs.aws.amazon.com/workmail/latest/APIReference/API_MobileDeviceAccessRule.html): A rule that controls access to mobile devices for an WorkMail group.
- [OrganizationSummary](https://docs.aws.amazon.com/workmail/latest/APIReference/API_OrganizationSummary.html): The representation of an organization.
- [Permission](https://docs.aws.amazon.com/workmail/latest/APIReference/API_Permission.html): Permission granted to a user, group, or resource to access a certain aspect of another user, group, or resource mailbox.
- [PersonalAccessTokenConfiguration](https://docs.aws.amazon.com/workmail/latest/APIReference/API_PersonalAccessTokenConfiguration.html): Displays the Personal Access Token status.
- [PersonalAccessTokenSummary](https://docs.aws.amazon.com/workmail/latest/APIReference/API_PersonalAccessTokenSummary.html): The summary of the Personal Access Token.
- [RedactedEwsAvailabilityProvider](https://docs.aws.amazon.com/workmail/latest/APIReference/API_RedactedEwsAvailabilityProvider.html): Describes an EWS based availability provider when returned from the service.
- [Resource](https://docs.aws.amazon.com/workmail/latest/APIReference/API_Resource.html): The representation of a resource.
- [Tag](https://docs.aws.amazon.com/workmail/latest/APIReference/API_Tag.html): Describes a tag applied to a resource.
- [User](https://docs.aws.amazon.com/workmail/latest/APIReference/API_User.html): The representation of an WorkMail user.

## [Amazon WorkMail Message Flow](https://docs.aws.amazon.com/workmail/latest/APIReference/Welcome_Amazon_WorkMail_Message_Flow.html)

The WorkMail Message Flow API provides access to email messages as they are being sent and received by a WorkMail organization.

### Actions

- [GetRawMessageContent](https://docs.aws.amazon.com/workmail/latest/APIReference/API_messageflow_GetRawMessageContent.html): Retrieves the raw content of an in-transit email message, in MIME format.
- [PutRawMessageContent](https://docs.aws.amazon.com/workmail/latest/APIReference/API_messageflow_PutRawMessageContent.html): Updates the raw content of an in-transit email message, in MIME format.

### Data Types

- [RawMessageContent](https://docs.aws.amazon.com/workmail/latest/APIReference/API_messageflow_RawMessageContent.html): Provides the MIME content of the updated email message as an S3 object.
- [S3Reference](https://docs.aws.amazon.com/workmail/latest/APIReference/API_messageflow_S3Reference.html): Amazon S3 object representing the updated message content, in MIME format.

## Common

- [Common Parameters](https://docs.aws.amazon.com/workmail/latest/APIReference/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/workmail/latest/APIReference/CommonErrors.html)