# Source: https://docs.aws.amazon.com/license-manager-user-subscriptions/latest/APIReference/llms.txt

# License Manager User Subscriptions API Reference

> With AWS License Manager, you can create user-based subscriptions to utilize licensed software with a per user subscription fee on Amazon EC2 instances.

- [Welcome](https://docs.aws.amazon.com/license-manager-user-subscriptions/latest/APIReference/Welcome.html)
- [Common Parameters](https://docs.aws.amazon.com/license-manager-user-subscriptions/latest/APIReference/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/license-manager-user-subscriptions/latest/APIReference/CommonErrors.html)

## [Actions](https://docs.aws.amazon.com/license-manager-user-subscriptions/latest/APIReference/API_Operations.html)

- [AssociateUser](https://docs.aws.amazon.com/license-manager-user-subscriptions/latest/APIReference/API_AssociateUser.html): Associates the user to an EC2 instance to utilize user-based subscriptions.
- [CreateLicenseServerEndpoint](https://docs.aws.amazon.com/license-manager-user-subscriptions/latest/APIReference/API_CreateLicenseServerEndpoint.html): Creates a network endpoint for the Remote Desktop Services (RDS) license server.
- [DeleteLicenseServerEndpoint](https://docs.aws.amazon.com/license-manager-user-subscriptions/latest/APIReference/API_DeleteLicenseServerEndpoint.html): Deletes a LicenseServerEndpoint resource.
- [DeregisterIdentityProvider](https://docs.aws.amazon.com/license-manager-user-subscriptions/latest/APIReference/API_DeregisterIdentityProvider.html): Deregisters the Active Directory identity provider from License Manager user-based subscriptions.
- [DisassociateUser](https://docs.aws.amazon.com/license-manager-user-subscriptions/latest/APIReference/API_DisassociateUser.html): Disassociates the user from an EC2 instance providing user-based subscriptions.
- [ListIdentityProviders](https://docs.aws.amazon.com/license-manager-user-subscriptions/latest/APIReference/API_ListIdentityProviders.html): Lists the Active Directory identity providers for user-based subscriptions.
- [ListInstances](https://docs.aws.amazon.com/license-manager-user-subscriptions/latest/APIReference/API_ListInstances.html): Lists the EC2 instances providing user-based subscriptions.
- [ListLicenseServerEndpoints](https://docs.aws.amazon.com/license-manager-user-subscriptions/latest/APIReference/API_ListLicenseServerEndpoints.html): List the Remote Desktop Services (RDS) License Server endpoints
- [ListProductSubscriptions](https://docs.aws.amazon.com/license-manager-user-subscriptions/latest/APIReference/API_ListProductSubscriptions.html): Lists the user-based subscription products available from an identity provider.
- [ListTagsForResource](https://docs.aws.amazon.com/license-manager-user-subscriptions/latest/APIReference/API_ListTagsForResource.html): Returns the list of tags for the specified resource.
- [ListUserAssociations](https://docs.aws.amazon.com/license-manager-user-subscriptions/latest/APIReference/API_ListUserAssociations.html): Lists user associations for an identity provider.
- [RegisterIdentityProvider](https://docs.aws.amazon.com/license-manager-user-subscriptions/latest/APIReference/API_RegisterIdentityProvider.html): Registers an identity provider for user-based subscriptions.
- [StartProductSubscription](https://docs.aws.amazon.com/license-manager-user-subscriptions/latest/APIReference/API_StartProductSubscription.html): Starts a product subscription for a user with the specified identity provider.
- [StopProductSubscription](https://docs.aws.amazon.com/license-manager-user-subscriptions/latest/APIReference/API_StopProductSubscription.html): Stops a product subscription for a user with the specified identity provider.
- [TagResource](https://docs.aws.amazon.com/license-manager-user-subscriptions/latest/APIReference/API_TagResource.html): Adds tags to a resource.
- [UntagResource](https://docs.aws.amazon.com/license-manager-user-subscriptions/latest/APIReference/API_UntagResource.html): Removes tags from a resource.
- [UpdateIdentityProviderSettings](https://docs.aws.amazon.com/license-manager-user-subscriptions/latest/APIReference/API_UpdateIdentityProviderSettings.html): Updates additional product configuration settings for the registered identity provider.


## [Data Types](https://docs.aws.amazon.com/license-manager-user-subscriptions/latest/APIReference/API_Types.html)

- [ActiveDirectoryIdentityProvider](https://docs.aws.amazon.com/license-manager-user-subscriptions/latest/APIReference/API_ActiveDirectoryIdentityProvider.html): Details about an Active Directory identity provider.
- [ActiveDirectorySettings](https://docs.aws.amazon.com/license-manager-user-subscriptions/latest/APIReference/API_ActiveDirectorySettings.html): Contains network access and credential details that are needed for user administration in the Active Directory.
- [CredentialsProvider](https://docs.aws.amazon.com/license-manager-user-subscriptions/latest/APIReference/API_CredentialsProvider.html): Contains information about the credential provider for user administration.
- [DomainNetworkSettings](https://docs.aws.amazon.com/license-manager-user-subscriptions/latest/APIReference/API_DomainNetworkSettings.html): Contains network settings for the Active Directory domain.
- [Filter](https://docs.aws.amazon.com/license-manager-user-subscriptions/latest/APIReference/API_Filter.html): A filter name and value pair that is used to return more specific results from a describe or list operation.
- [IdentityProvider](https://docs.aws.amazon.com/license-manager-user-subscriptions/latest/APIReference/API_IdentityProvider.html): Refers to an identity provider.
- [IdentityProviderSummary](https://docs.aws.amazon.com/license-manager-user-subscriptions/latest/APIReference/API_IdentityProviderSummary.html): Describes an identity provider.
- [InstanceSummary](https://docs.aws.amazon.com/license-manager-user-subscriptions/latest/APIReference/API_InstanceSummary.html): Describes an EC2 instance providing user-based subscriptions.
- [InstanceUserSummary](https://docs.aws.amazon.com/license-manager-user-subscriptions/latest/APIReference/API_InstanceUserSummary.html): Describes users of an EC2 instance providing user-based subscriptions.
- [LicenseServer](https://docs.aws.amazon.com/license-manager-user-subscriptions/latest/APIReference/API_LicenseServer.html): Information about a Remote Desktop Services (RDS) license server.
- [LicenseServerEndpoint](https://docs.aws.amazon.com/license-manager-user-subscriptions/latest/APIReference/API_LicenseServerEndpoint.html): Contains details about a network endpoint for a Remote Desktop Services (RDS) license server.
- [LicenseServerSettings](https://docs.aws.amazon.com/license-manager-user-subscriptions/latest/APIReference/API_LicenseServerSettings.html): The settings to configure your license server.
- [ProductUserSummary](https://docs.aws.amazon.com/license-manager-user-subscriptions/latest/APIReference/API_ProductUserSummary.html): A summary of the user-based subscription products for a specific user.
- [RdsSalSettings](https://docs.aws.amazon.com/license-manager-user-subscriptions/latest/APIReference/API_RdsSalSettings.html): Server settings that are specific to a Remote Desktop Services (RDS) license server.
- [SecretsManagerCredentialsProvider](https://docs.aws.amazon.com/license-manager-user-subscriptions/latest/APIReference/API_SecretsManagerCredentialsProvider.html): Contains a credentials secret that's stored in AWS Secrets Manager.
- [ServerEndpoint](https://docs.aws.amazon.com/license-manager-user-subscriptions/latest/APIReference/API_ServerEndpoint.html): A network endpoint through which you can access one or more servers.
- [ServerSettings](https://docs.aws.amazon.com/license-manager-user-subscriptions/latest/APIReference/API_ServerSettings.html): Contains settings for a specific server.
- [Settings](https://docs.aws.amazon.com/license-manager-user-subscriptions/latest/APIReference/API_Settings.html): The registered identity providerâs product related configuration settings such as the subnets to provision VPC endpoints, and the security group ID that is associated with the VPC endpoints.
- [UpdateSettings](https://docs.aws.amazon.com/license-manager-user-subscriptions/latest/APIReference/API_UpdateSettings.html): Updates the registered identity providerâs product related configuration settings such as the subnets to provision VPC endpoints.
