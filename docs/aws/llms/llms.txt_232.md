# Source: https://docs.aws.amazon.com/cognitoidentity/latest/APIReference/llms.txt

# Amazon Cognito Federated Identities API Reference

> Amazon Cognito Federated Identities is a web service that delivers scoped temporary credentials to mobile devices and other untrusted environments. It uniquely identifies a device and supplies the user with a consistent identity over the lifetime of an application.

- [Welcome](https://docs.aws.amazon.com/cognitoidentity/latest/APIReference/Welcome.html)
- [Common Parameters](https://docs.aws.amazon.com/cognitoidentity/latest/APIReference/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/cognitoidentity/latest/APIReference/CommonErrors.html)

## [Actions](https://docs.aws.amazon.com/cognitoidentity/latest/APIReference/API_Operations.html)

- [CreateIdentityPool](https://docs.aws.amazon.com/cognitoidentity/latest/APIReference/API_CreateIdentityPool.html): Creates a new identity pool.
- [DeleteIdentities](https://docs.aws.amazon.com/cognitoidentity/latest/APIReference/API_DeleteIdentities.html): Deletes identities from an identity pool.
- [DeleteIdentityPool](https://docs.aws.amazon.com/cognitoidentity/latest/APIReference/API_DeleteIdentityPool.html): Deletes an identity pool.
- [DescribeIdentity](https://docs.aws.amazon.com/cognitoidentity/latest/APIReference/API_DescribeIdentity.html): Returns metadata related to the given identity, including when the identity was created and any associated linked logins.
- [DescribeIdentityPool](https://docs.aws.amazon.com/cognitoidentity/latest/APIReference/API_DescribeIdentityPool.html): Gets details about the requested identity pool, including pool name and ID, description, tags, and identity provviders.
- [GetCredentialsForIdentity](https://docs.aws.amazon.com/cognitoidentity/latest/APIReference/API_GetCredentialsForIdentity.html): Returns credentials for the provided identity ID.
- [GetId](https://docs.aws.amazon.com/cognitoidentity/latest/APIReference/API_GetId.html): Generates (or retrieves) IdentityID.
- [GetIdentityPoolRoles](https://docs.aws.amazon.com/cognitoidentity/latest/APIReference/API_GetIdentityPoolRoles.html): Gets the roles for an identity pool.
- [GetOpenIdToken](https://docs.aws.amazon.com/cognitoidentity/latest/APIReference/API_GetOpenIdToken.html): Gets an OpenID token, using a known Cognito ID.
- [GetOpenIdTokenForDeveloperIdentity](https://docs.aws.amazon.com/cognitoidentity/latest/APIReference/API_GetOpenIdTokenForDeveloperIdentity.html): Registers (or retrieves) a Cognito IdentityId and an OpenID Connect token for a user authenticated by your backend authentication process.
- [GetPrincipalTagAttributeMap](https://docs.aws.amazon.com/cognitoidentity/latest/APIReference/API_GetPrincipalTagAttributeMap.html): Use GetPrincipalTagAttributeMap to list all mappings between PrincipalTags and user attributes.
- [ListIdentities](https://docs.aws.amazon.com/cognitoidentity/latest/APIReference/API_ListIdentities.html): Lists the identities in an identity pool.
- [ListIdentityPools](https://docs.aws.amazon.com/cognitoidentity/latest/APIReference/API_ListIdentityPools.html): Lists all of the Cognito identity pools registered for your account.
- [ListTagsForResource](https://docs.aws.amazon.com/cognitoidentity/latest/APIReference/API_ListTagsForResource.html): Lists the tags that are assigned to an Amazon Cognito identity pool.
- [LookupDeveloperIdentity](https://docs.aws.amazon.com/cognitoidentity/latest/APIReference/API_LookupDeveloperIdentity.html): Retrieves the IdentityID associated with a DeveloperUserIdentifier or the list of DeveloperUserIdentifier values associated with an IdentityId for an existing identity.
- [MergeDeveloperIdentities](https://docs.aws.amazon.com/cognitoidentity/latest/APIReference/API_MergeDeveloperIdentities.html): Merges two users having different IdentityIds, existing in the same identity pool, and identified by the same developer provider.
- [SetIdentityPoolRoles](https://docs.aws.amazon.com/cognitoidentity/latest/APIReference/API_SetIdentityPoolRoles.html): Sets the roles for an identity pool.
- [SetPrincipalTagAttributeMap](https://docs.aws.amazon.com/cognitoidentity/latest/APIReference/API_SetPrincipalTagAttributeMap.html): You can use this operation to use default (username and clientID) attribute or custom attribute mappings.
- [TagResource](https://docs.aws.amazon.com/cognitoidentity/latest/APIReference/API_TagResource.html): Assigns a set of tags to the specified Amazon Cognito identity pool.
- [UnlinkDeveloperIdentity](https://docs.aws.amazon.com/cognitoidentity/latest/APIReference/API_UnlinkDeveloperIdentity.html): Unlinks a DeveloperUserIdentifier from an existing identity.
- [UnlinkIdentity](https://docs.aws.amazon.com/cognitoidentity/latest/APIReference/API_UnlinkIdentity.html): Unlinks a federated identity from an existing account.
- [UntagResource](https://docs.aws.amazon.com/cognitoidentity/latest/APIReference/API_UntagResource.html): Removes the specified tags from the specified Amazon Cognito identity pool.
- [UpdateIdentityPool](https://docs.aws.amazon.com/cognitoidentity/latest/APIReference/API_UpdateIdentityPool.html): Updates the configuration of an identity pool.


## [Data Types](https://docs.aws.amazon.com/cognitoidentity/latest/APIReference/API_Types.html)

- [CognitoIdentityProvider](https://docs.aws.amazon.com/cognitoidentity/latest/APIReference/API_CognitoIdentityProvider.html): A provider representing an Amazon Cognito user pool and its client ID.
- [Credentials](https://docs.aws.amazon.com/cognitoidentity/latest/APIReference/API_Credentials.html): Credentials for the provided identity ID.
- [IdentityDescription](https://docs.aws.amazon.com/cognitoidentity/latest/APIReference/API_IdentityDescription.html): A description of the identity.
- [IdentityPoolShortDescription](https://docs.aws.amazon.com/cognitoidentity/latest/APIReference/API_IdentityPoolShortDescription.html): A description of the identity pool.
- [MappingRule](https://docs.aws.amazon.com/cognitoidentity/latest/APIReference/API_MappingRule.html): A rule that maps a claim name, a claim value, and a match type to a role ARN.
- [RoleMapping](https://docs.aws.amazon.com/cognitoidentity/latest/APIReference/API_RoleMapping.html): A role mapping.
- [RulesConfigurationType](https://docs.aws.amazon.com/cognitoidentity/latest/APIReference/API_RulesConfigurationType.html): A container for rules.
- [UnprocessedIdentityId](https://docs.aws.amazon.com/cognitoidentity/latest/APIReference/API_UnprocessedIdentityId.html): An array of UnprocessedIdentityId objects, each of which contains an ErrorCode and IdentityId.
