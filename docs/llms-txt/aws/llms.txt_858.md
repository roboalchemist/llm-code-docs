# Source: https://docs.aws.amazon.com/wickr/latest/APIReference/llms.txt

# AWS Wickr API Reference

> Welcome to the AWS Wickr API Reference.

- [Welcome](https://docs.aws.amazon.com/wickr/latest/APIReference/Welcome.html)
- [Common Parameters](https://docs.aws.amazon.com/wickr/latest/APIReference/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/wickr/latest/APIReference/CommonErrors.html)

## [Actions](https://docs.aws.amazon.com/wickr/latest/APIReference/API_Operations.html)

- [BatchCreateUser](https://docs.aws.amazon.com/wickr/latest/APIReference/API_BatchCreateUser.html): Creates multiple users in a specified Wickr network.
- [BatchDeleteUser](https://docs.aws.amazon.com/wickr/latest/APIReference/API_BatchDeleteUser.html): Deletes multiple users from a specified Wickr network.
- [BatchLookupUserUname](https://docs.aws.amazon.com/wickr/latest/APIReference/API_BatchLookupUserUname.html): Looks up multiple user usernames from their unique username hashes (unames).
- [BatchReinviteUser](https://docs.aws.amazon.com/wickr/latest/APIReference/API_BatchReinviteUser.html): Resends invitation codes to multiple users who have pending invitations in a Wickr network.
- [BatchResetDevicesForUser](https://docs.aws.amazon.com/wickr/latest/APIReference/API_BatchResetDevicesForUser.html): Resets multiple devices for a specific user in a Wickr network.
- [BatchToggleUserSuspendStatus](https://docs.aws.amazon.com/wickr/latest/APIReference/API_BatchToggleUserSuspendStatus.html): Suspends or unsuspends multiple users in a Wickr network.
- [CreateBot](https://docs.aws.amazon.com/wickr/latest/APIReference/API_CreateBot.html): Creates a new bot in a specified Wickr network.
- [CreateDataRetentionBot](https://docs.aws.amazon.com/wickr/latest/APIReference/API_CreateDataRetentionBot.html): Creates a data retention bot in a Wickr network.
- [CreateDataRetentionBotChallenge](https://docs.aws.amazon.com/wickr/latest/APIReference/API_CreateDataRetentionBotChallenge.html): Creates a new challenge password for the data retention bot.
- [CreateNetwork](https://docs.aws.amazon.com/wickr/latest/APIReference/API_CreateNetwork.html): Creates a new Wickr network with specified access level and configuration.
- [CreateSecurityGroup](https://docs.aws.amazon.com/wickr/latest/APIReference/API_CreateSecurityGroup.html): Creates a new security group in a Wickr network.
- [DeleteBot](https://docs.aws.amazon.com/wickr/latest/APIReference/API_DeleteBot.html): Deletes a bot from a specified Wickr network.
- [DeleteDataRetentionBot](https://docs.aws.amazon.com/wickr/latest/APIReference/API_DeleteDataRetentionBot.html): Deletes the data retention bot from a Wickr network.
- [DeleteNetwork](https://docs.aws.amazon.com/wickr/latest/APIReference/API_DeleteNetwork.html): Deletes a Wickr network and all its associated resources, including users, bots, security groups, and settings.
- [DeleteSecurityGroup](https://docs.aws.amazon.com/wickr/latest/APIReference/API_DeleteSecurityGroup.html): Deletes a security group from a Wickr network.
- [GetBot](https://docs.aws.amazon.com/wickr/latest/APIReference/API_GetBot.html): Retrieves detailed information about a specific bot in a Wickr network, including its status, group membership, and authentication details.
- [GetBotsCount](https://docs.aws.amazon.com/wickr/latest/APIReference/API_GetBotsCount.html): Retrieves the count of bots in a Wickr network, categorized by their status (pending, active, and total).
- [GetDataRetentionBot](https://docs.aws.amazon.com/wickr/latest/APIReference/API_GetDataRetentionBot.html): Retrieves information about the data retention bot in a Wickr network, including its status and whether the data retention service is enabled.
- [GetGuestUserHistoryCount](https://docs.aws.amazon.com/wickr/latest/APIReference/API_GetGuestUserHistoryCount.html): Retrieves historical guest user count data for a Wickr network, showing the number of guest users per billing period over the past 90 days.
- [GetNetwork](https://docs.aws.amazon.com/wickr/latest/APIReference/API_GetNetwork.html): Retrieves detailed information about a specific Wickr network, including its configuration, access level, and status.
- [GetNetworkSettings](https://docs.aws.amazon.com/wickr/latest/APIReference/API_GetNetworkSettings.html): Retrieves all network-level settings for a Wickr network, including client metrics, data retention, and other configuration options.
- [GetOidcInfo](https://docs.aws.amazon.com/wickr/latest/APIReference/API_GetOidcInfo.html): Retrieves the OpenID Connect (OIDC) configuration for a Wickr network, including SSO settings and optional token information if access token parameters are provided.
- [GetOpentdfConfig](https://docs.aws.amazon.com/wickr/latest/APIReference/API_GetOpentdfConfig.html): Retrieves the OpenTDF integration configuration for a Wickr network.
- [GetSecurityGroup](https://docs.aws.amazon.com/wickr/latest/APIReference/API_GetSecurityGroup.html): Retrieves detailed information about a specific security group in a Wickr network, including its settings, member counts, and configuration.
- [GetUser](https://docs.aws.amazon.com/wickr/latest/APIReference/API_GetUser.html): Retrieves detailed information about a specific user in a Wickr network, including their profile, status, and activity history.
- [GetUsersCount](https://docs.aws.amazon.com/wickr/latest/APIReference/API_GetUsersCount.html): Retrieves the count of users in a Wickr network, categorized by their status (pending, active, rejected) and showing how many users can still be added.
- [ListBlockedGuestUsers](https://docs.aws.amazon.com/wickr/latest/APIReference/API_ListBlockedGuestUsers.html): Retrieves a paginated list of guest users who have been blocked from a Wickr network.
- [ListBots](https://docs.aws.amazon.com/wickr/latest/APIReference/API_ListBots.html): Retrieves a paginated list of bots in a specified Wickr network.
- [ListDevicesForUser](https://docs.aws.amazon.com/wickr/latest/APIReference/API_ListDevicesForUser.html): Retrieves a paginated list of devices associated with a specific user in a Wickr network.
- [ListGuestUsers](https://docs.aws.amazon.com/wickr/latest/APIReference/API_ListGuestUsers.html): Retrieves a paginated list of guest users who have communicated with your Wickr network.
- [ListNetworks](https://docs.aws.amazon.com/wickr/latest/APIReference/API_ListNetworks.html): Retrieves a paginated list of all Wickr networks associated with your AWS account.
- [ListSecurityGroups](https://docs.aws.amazon.com/wickr/latest/APIReference/API_ListSecurityGroups.html): Retrieves a paginated list of security groups in a specified Wickr network.
- [ListSecurityGroupUsers](https://docs.aws.amazon.com/wickr/latest/APIReference/API_ListSecurityGroupUsers.html): Retrieves a paginated list of users who belong to a specific security group in a Wickr network.
- [ListUsers](https://docs.aws.amazon.com/wickr/latest/APIReference/API_ListUsers.html): Retrieves a paginated list of users in a specified Wickr network.
- [RegisterOidcConfig](https://docs.aws.amazon.com/wickr/latest/APIReference/API_RegisterOidcConfig.html): Registers and saves an OpenID Connect (OIDC) configuration for a Wickr network, enabling Single Sign-On (SSO) authentication through an identity provider.
- [RegisterOidcConfigTest](https://docs.aws.amazon.com/wickr/latest/APIReference/API_RegisterOidcConfigTest.html): Tests an OpenID Connect (OIDC) configuration for a Wickr network by validating the connection to the identity provider and retrieving its supported capabilities.
- [RegisterOpentdfConfig](https://docs.aws.amazon.com/wickr/latest/APIReference/API_RegisterOpentdfConfig.html): Registers and saves OpenTDF configuration for a Wickr network, enabling attribute-based access control for Wickr through an OpenTDF provider.
- [UpdateBot](https://docs.aws.amazon.com/wickr/latest/APIReference/API_UpdateBot.html): Updates the properties of an existing bot in a Wickr network.
- [UpdateDataRetention](https://docs.aws.amazon.com/wickr/latest/APIReference/API_UpdateDataRetention.html): Updates the data retention bot settings, allowing you to enable or disable the data retention service, or acknowledge the public key message.
- [UpdateGuestUser](https://docs.aws.amazon.com/wickr/latest/APIReference/API_UpdateGuestUser.html): Updates the block status of a guest user in a Wickr network.
- [UpdateNetwork](https://docs.aws.amazon.com/wickr/latest/APIReference/API_UpdateNetwork.html): Updates the properties of an existing Wickr network, such as its name or encryption key configuration.
- [UpdateNetworkSettings](https://docs.aws.amazon.com/wickr/latest/APIReference/API_UpdateNetworkSettings.html): Updates network-level settings for a Wickr network.
- [UpdateSecurityGroup](https://docs.aws.amazon.com/wickr/latest/APIReference/API_UpdateSecurityGroup.html): Updates the properties of an existing security group in a Wickr network, such as its name or settings.
- [UpdateUser](https://docs.aws.amazon.com/wickr/latest/APIReference/API_UpdateUser.html): Updates the properties of an existing user in a Wickr network.


## [Data Types](https://docs.aws.amazon.com/wickr/latest/APIReference/API_Types.html)

- [BasicDeviceObject](https://docs.aws.amazon.com/wickr/latest/APIReference/API_BasicDeviceObject.html): Represents a device where a user has logged into Wickr, containing information about the device's type, status, and login history.
- [BatchCreateUserRequestItem](https://docs.aws.amazon.com/wickr/latest/APIReference/API_BatchCreateUserRequestItem.html): Contains the details for a single user to be created in a batch user creation request.
- [BatchDeviceErrorResponseItem](https://docs.aws.amazon.com/wickr/latest/APIReference/API_BatchDeviceErrorResponseItem.html): Contains error information for a device operation that failed in a batch device request.
- [BatchDeviceSuccessResponseItem](https://docs.aws.amazon.com/wickr/latest/APIReference/API_BatchDeviceSuccessResponseItem.html): Contains information about a device that was successfully processed in a batch device operation.
- [BatchUnameErrorResponseItem](https://docs.aws.amazon.com/wickr/latest/APIReference/API_BatchUnameErrorResponseItem.html): Contains error information for a username hash lookup that failed in a batch uname lookup request.
- [BatchUnameSuccessResponseItem](https://docs.aws.amazon.com/wickr/latest/APIReference/API_BatchUnameSuccessResponseItem.html): Contains information about a username hash that was successfully resolved in a batch uname lookup operation.
- [BatchUserErrorResponseItem](https://docs.aws.amazon.com/wickr/latest/APIReference/API_BatchUserErrorResponseItem.html): Contains error information for a user operation that failed in a batch user request.
- [BatchUserSuccessResponseItem](https://docs.aws.amazon.com/wickr/latest/APIReference/API_BatchUserSuccessResponseItem.html): Contains information about a user that was successfully processed in a batch user operation.
- [BlockedGuestUser](https://docs.aws.amazon.com/wickr/latest/APIReference/API_BlockedGuestUser.html): Represents a guest user who has been blocked from accessing a Wickr network.
- [Bot](https://docs.aws.amazon.com/wickr/latest/APIReference/API_Bot.html): Represents a bot account in a Wickr network with all its informational fields.
- [CallingSettings](https://docs.aws.amazon.com/wickr/latest/APIReference/API_CallingSettings.html): Defines the calling feature permissions and settings for users in a security group, controlling what types of calls users can initiate and participate in.
- [ErrorDetail](https://docs.aws.amazon.com/wickr/latest/APIReference/API_ErrorDetail.html): Contains detailed error information explaining why an operation failed, including which field caused the error and the reason for the failure.
- [GuestUser](https://docs.aws.amazon.com/wickr/latest/APIReference/API_GuestUser.html): Represents a guest user who has accessed the network from a federated Wickr network.
- [GuestUserHistoryCount](https://docs.aws.amazon.com/wickr/latest/APIReference/API_GuestUserHistoryCount.html): Contains the count of guest users for a specific billing period, used for tracking historical guest user activity.
- [Network](https://docs.aws.amazon.com/wickr/latest/APIReference/API_Network.html): Represents a Wickr network with all its configuration and status information.
- [NetworkSettings](https://docs.aws.amazon.com/wickr/latest/APIReference/API_NetworkSettings.html): Contains network-level configuration settings that apply to all users and security groups within a Wickr network.
- [OidcConfigInfo](https://docs.aws.amazon.com/wickr/latest/APIReference/API_OidcConfigInfo.html): Contains the OpenID Connect (OIDC) configuration information for Single Sign-On (SSO) authentication, including identity provider settings and client credentials.
- [OidcTokenInfo](https://docs.aws.amazon.com/wickr/latest/APIReference/API_OidcTokenInfo.html): Contains OAuth token information returned from the identity provider, including access tokens, ID tokens, and PKCE parameters used for secure authentication.
- [PasswordRequirements](https://docs.aws.amazon.com/wickr/latest/APIReference/API_PasswordRequirements.html): Defines password complexity requirements for users in a security group, including minimum length and character type requirements.
- [PermittedWickrEnterpriseNetwork](https://docs.aws.amazon.com/wickr/latest/APIReference/API_PermittedWickrEnterpriseNetwork.html): Identifies a Wickr enterprise network that is permitted for global federation, allowing users to communicate with members of the specified network.
- [ReadReceiptConfig](https://docs.aws.amazon.com/wickr/latest/APIReference/API_ReadReceiptConfig.html): Configuration for read receipts at the network level, controlling whether senders can see when their messages have been read.
- [SecurityGroup](https://docs.aws.amazon.com/wickr/latest/APIReference/API_SecurityGroup.html): Represents a security group in a Wickr network, containing membership statistics, configuration, and all permission settings that apply to its members.
- [SecurityGroupSettings](https://docs.aws.amazon.com/wickr/latest/APIReference/API_SecurityGroupSettings.html): Comprehensive configuration settings that define all user capabilities, restrictions, and features for members of a security group.
- [SecurityGroupSettingsRequest](https://docs.aws.amazon.com/wickr/latest/APIReference/API_SecurityGroupSettingsRequest.html): Contains the security group configuration settings that can be specified when creating or updating a security group.
- [Setting](https://docs.aws.amazon.com/wickr/latest/APIReference/API_Setting.html): Represents a single network-level configuration setting with its name, value, and data type.
- [ShredderSettings](https://docs.aws.amazon.com/wickr/latest/APIReference/API_ShredderSettings.html): Configuration for the message shredder feature, which securely deletes messages and files from devices to prevent data recovery.
- [UpdateUserDetails](https://docs.aws.amazon.com/wickr/latest/APIReference/API_UpdateUserDetails.html): Contains the modifiable details for updating an existing user, including name, password, security group membership, and invitation settings.
- [User](https://docs.aws.amazon.com/wickr/latest/APIReference/API_User.html): Represents a user account in a Wickr network with detailed profile information, status, security settings, and authentication details.
- [WickrAwsNetworks](https://docs.aws.amazon.com/wickr/latest/APIReference/API_WickrAwsNetworks.html): Identifies a AWS Wickr network by region and network ID, used for configuring permitted networks for global federation.


## [Service-specific Errors](https://docs.aws.amazon.com/wickr/latest/APIReference/API_Errors.html)

- [BadRequestError](https://docs.aws.amazon.com/wickr/latest/APIReference/API_BadRequestError.html): The request was invalid or malformed.
- [ForbiddenError](https://docs.aws.amazon.com/wickr/latest/APIReference/API_ForbiddenError.html): Access to the requested resource is forbidden.
- [InternalServerError](https://docs.aws.amazon.com/wickr/latest/APIReference/API_InternalServerError.html): An unexpected error occurred on the server while processing the request.
- [RateLimitError](https://docs.aws.amazon.com/wickr/latest/APIReference/API_RateLimitError.html): The request was throttled because too many requests were sent in a short period of time.
- [ResourceNotFoundError](https://docs.aws.amazon.com/wickr/latest/APIReference/API_ResourceNotFoundError.html): The requested resource could not be found.
- [UnauthorizedError](https://docs.aws.amazon.com/wickr/latest/APIReference/API_UnauthorizedError.html): The request was not authenticated or the authentication credentials were invalid.
- [ValidationError](https://docs.aws.amazon.com/wickr/latest/APIReference/API_ValidationError.html): One or more fields in the request failed validation.
