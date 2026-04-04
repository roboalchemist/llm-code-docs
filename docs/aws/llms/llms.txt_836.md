# Source: https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/llms.txt

# Amazon Verified Permissions API Reference Guide

> Learn about Amazon Verified Permissions and how you can use it to provide custom authorization services for your applications..

- [Welcome](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/Welcome.html)
- [Making API requests](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/making-api-requests.html)
- [Common Parameters](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/CommonErrors.html)
- [Document history](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/doc-history.html)
- [AWS Glossary](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/glossary.html)

## [Actions](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_Operations.html)

- [BatchGetPolicy](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_BatchGetPolicy.html): Retrieves information about a group (batch) of policies.
- [BatchIsAuthorized](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_BatchIsAuthorized.html): Makes a series of decisions about multiple authorization requests for one principal or resource.
- [BatchIsAuthorizedWithToken](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_BatchIsAuthorizedWithToken.html): Makes a series of decisions about multiple authorization requests for one token.
- [CreateIdentitySource](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_CreateIdentitySource.html): Adds an identity source to a policy storeâan Amazon Cognito user pool or OpenID Connect (OIDC) identity provider (IdP).
- [CreatePolicy](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_CreatePolicy.html): Creates a Cedar policy and saves it in the specified policy store.
- [CreatePolicyStore](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_CreatePolicyStore.html): Creates a policy store.
- [CreatePolicyTemplate](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_CreatePolicyTemplate.html): Creates a policy template.
- [DeleteIdentitySource](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_DeleteIdentitySource.html): Deletes an identity source that references an identity provider (IdP) such as Amazon Cognito.
- [DeletePolicy](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_DeletePolicy.html): Deletes the specified policy from the policy store.
- [DeletePolicyStore](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_DeletePolicyStore.html): Deletes the specified policy store.
- [DeletePolicyTemplate](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_DeletePolicyTemplate.html): Deletes the specified policy template from the policy store.
- [GetIdentitySource](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_GetIdentitySource.html): Retrieves the details about the specified identity source.
- [GetPolicy](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_GetPolicy.html): Retrieves information about the specified policy.
- [GetPolicyStore](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_GetPolicyStore.html): Retrieves details about a policy store.
- [GetPolicyTemplate](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_GetPolicyTemplate.html): Retrieve the details for the specified policy template in the specified policy store.
- [GetSchema](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_GetSchema.html): Retrieve the details for the specified schema in the specified policy store.
- [IsAuthorized](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_IsAuthorized.html): Makes an authorization decision about a service request described in the parameters.
- [IsAuthorizedWithToken](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_IsAuthorizedWithToken.html): Makes an authorization decision about a service request described in the parameters.
- [ListIdentitySources](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_ListIdentitySources.html): Returns a paginated list of all of the identity sources defined in the specified policy store.
- [ListPolicies](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_ListPolicies.html): Returns a paginated list of all policies stored in the specified policy store.
- [ListPolicyStores](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_ListPolicyStores.html): Returns a paginated list of all policy stores in the calling AWS account.
- [ListPolicyTemplates](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_ListPolicyTemplates.html): Returns a paginated list of all policy templates in the specified policy store.
- [ListTagsForResource](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_ListTagsForResource.html): Returns the tags associated with the specified Amazon Verified Permissions resource.
- [PutSchema](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_PutSchema.html): Creates or updates the policy schema in the specified policy store.
- [TagResource](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_TagResource.html): Assigns one or more tags (key-value pairs) to the specified Amazon Verified Permissions resource.
- [UntagResource](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_UntagResource.html): Removes one or more tags from the specified Amazon Verified Permissions resource.
- [UpdateIdentitySource](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_UpdateIdentitySource.html): Updates the specified identity source to use a new identity provider (IdP), or to change the mapping of identities from the IdP to a different principal entity type.
- [UpdatePolicy](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_UpdatePolicy.html): Modifies a Cedar static policy in the specified policy store.
- [UpdatePolicyStore](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_UpdatePolicyStore.html): Modifies the validation setting for a policy store.
- [UpdatePolicyTemplate](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_UpdatePolicyTemplate.html): Updates the specified policy template.


## [Data Types](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_Types.html)

- [ActionIdentifier](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_ActionIdentifier.html): Contains information about an action for a request for which an authorization decision is made.
- [AttributeValue](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_AttributeValue.html): The value of an attribute.
- [BatchGetPolicyErrorItem](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_BatchGetPolicyErrorItem.html): Contains the information about an error resulting from a BatchGetPolicy API call.
- [BatchGetPolicyInputItem](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_BatchGetPolicyInputItem.html): Information about a policy that you include in a BatchGetPolicy API request.
- [BatchGetPolicyOutputItem](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_BatchGetPolicyOutputItem.html): Contains information about a policy returned from a BatchGetPolicy API request.
- [BatchIsAuthorizedInputItem](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_BatchIsAuthorizedInputItem.html): An authorization request that you include in a BatchIsAuthorized API request.
- [BatchIsAuthorizedOutputItem](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_BatchIsAuthorizedOutputItem.html): The decision, based on policy evaluation, from an individual authorization request in a BatchIsAuthorized API request.
- [BatchIsAuthorizedWithTokenInputItem](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_BatchIsAuthorizedWithTokenInputItem.html): An authorization request that you include in a BatchIsAuthorizedWithToken API request.
- [BatchIsAuthorizedWithTokenOutputItem](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_BatchIsAuthorizedWithTokenOutputItem.html): The decision, based on policy evaluation, from an individual authorization request in a BatchIsAuthorizedWithToken API request.
- [CedarTagValue](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_CedarTagValue.html): The value of an entity's Cedar tag.
- [CognitoGroupConfiguration](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_CognitoGroupConfiguration.html): The type of entity that a policy store maps to groups from an Amazon Cognito user pool identity source.
- [CognitoGroupConfigurationDetail](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_CognitoGroupConfigurationDetail.html): The type of entity that a policy store maps to groups from an Amazon Cognito user pool identity source.
- [CognitoGroupConfigurationItem](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_CognitoGroupConfigurationItem.html): The type of entity that a policy store maps to groups from an Amazon Cognito user pool identity source.
- [CognitoUserPoolConfiguration](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_CognitoUserPoolConfiguration.html): The configuration for an identity source that represents a connection to an Amazon Cognito user pool used as an identity provider for Verified Permissions.
- [CognitoUserPoolConfigurationDetail](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_CognitoUserPoolConfigurationDetail.html): The configuration for an identity source that represents a connection to an Amazon Cognito user pool used as an identity provider for Verified Permissions.
- [CognitoUserPoolConfigurationItem](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_CognitoUserPoolConfigurationItem.html): The configuration for an identity source that represents a connection to an Amazon Cognito user pool used as an identity provider for Verified Permissions.
- [Configuration](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_Configuration.html): Contains configuration information used when creating a new identity source.
- [ConfigurationDetail](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_ConfigurationDetail.html): Contains configuration information about an identity source.
- [ConfigurationItem](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_ConfigurationItem.html): Contains configuration information about an identity source.
- [ContextDefinition](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_ContextDefinition.html): Contains additional details about the context of the request.
- [DeterminingPolicyItem](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_DeterminingPolicyItem.html): Contains information about one of the policies that determined an authorization decision.
- [EncryptionSettings](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_EncryptionSettings.html): A structure that contains the encryption configuration for the policy store and child resources.
- [EncryptionState](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_EncryptionState.html): A structure that contains the encryption configuration for the policy store and child resources.
- [EntitiesDefinition](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_EntitiesDefinition.html): Contains the list of entities to be considered during an authorization request.
- [EntityIdentifier](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_EntityIdentifier.html): Contains the identifier of an entity, including its ID and type.
- [EntityItem](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_EntityItem.html): Contains information about an entity that can be referenced in a Cedar policy.
- [EntityReference](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_EntityReference.html): Contains information about a principal or resource that can be referenced in a Cedar policy.
- [EvaluationErrorItem](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_EvaluationErrorItem.html): Contains a description of an evaluation error.
- [IdentitySourceDetails](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_IdentitySourceDetails.html): This data type has been deprecated.
- [IdentitySourceFilter](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_IdentitySourceFilter.html): A structure that defines characteristics of an identity source that you can use to filter.
- [IdentitySourceItem](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_IdentitySourceItem.html): A structure that defines an identity source.
- [IdentitySourceItemDetails](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_IdentitySourceItemDetails.html): This data type has been deprecated.
- [KmsEncryptionSettings](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_KmsEncryptionSettings.html): A structure that contains the KMS encryption configuration for the policy store.
- [KmsEncryptionState](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_KmsEncryptionState.html): A structure that contains the AWS KMS encryption configuration for the policy store.
- [OpenIdConnectAccessTokenConfiguration](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_OpenIdConnectAccessTokenConfiguration.html): The configuration of an OpenID Connect (OIDC) identity source for handling access token claims.
- [OpenIdConnectAccessTokenConfigurationDetail](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_OpenIdConnectAccessTokenConfigurationDetail.html): The configuration of an OpenID Connect (OIDC) identity source for handling access token claims.
- [OpenIdConnectAccessTokenConfigurationItem](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_OpenIdConnectAccessTokenConfigurationItem.html): The configuration of an OpenID Connect (OIDC) identity source for handling access token claims.
- [OpenIdConnectConfiguration](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_OpenIdConnectConfiguration.html): Contains configuration details of an OpenID Connect (OIDC) identity provider, or identity source, that Verified Permissions can use to generate entities from authenticated identities.
- [OpenIdConnectConfigurationDetail](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_OpenIdConnectConfigurationDetail.html): Contains configuration details of an OpenID Connect (OIDC) identity provider, or identity source, that Verified Permissions can use to generate entities from authenticated identities.
- [OpenIdConnectConfigurationItem](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_OpenIdConnectConfigurationItem.html): Contains configuration details of an OpenID Connect (OIDC) identity provider, or identity source, that Verified Permissions can use to generate entities from authenticated identities.
- [OpenIdConnectGroupConfiguration](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_OpenIdConnectGroupConfiguration.html): The claim in OIDC identity provider tokens that indicates a user's group membership, and the entity type that you want to map it to.
- [OpenIdConnectGroupConfigurationDetail](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_OpenIdConnectGroupConfigurationDetail.html): The claim in OIDC identity provider tokens that indicates a user's group membership, and the entity type that you want to map it to.
- [OpenIdConnectGroupConfigurationItem](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_OpenIdConnectGroupConfigurationItem.html): The claim in OIDC identity provider tokens that indicates a user's group membership, and the entity type that you want to map it to.
- [OpenIdConnectIdentityTokenConfiguration](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_OpenIdConnectIdentityTokenConfiguration.html): The configuration of an OpenID Connect (OIDC) identity source for handling identity (ID) token claims.
- [OpenIdConnectIdentityTokenConfigurationDetail](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_OpenIdConnectIdentityTokenConfigurationDetail.html): The configuration of an OpenID Connect (OIDC) identity source for handling identity (ID) token claims.
- [OpenIdConnectIdentityTokenConfigurationItem](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_OpenIdConnectIdentityTokenConfigurationItem.html): The configuration of an OpenID Connect (OIDC) identity source for handling identity (ID) token claims.
- [OpenIdConnectTokenSelection](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_OpenIdConnectTokenSelection.html): The token type that you want to process from your OIDC identity provider.
- [OpenIdConnectTokenSelectionDetail](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_OpenIdConnectTokenSelectionDetail.html): The token type that you want to process from your OIDC identity provider.
- [OpenIdConnectTokenSelectionItem](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_OpenIdConnectTokenSelectionItem.html): The token type that you want to process from your OIDC identity provider.
- [PolicyDefinition](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_PolicyDefinition.html): A structure that contains the details for a Cedar policy definition.
- [PolicyDefinitionDetail](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_PolicyDefinitionDetail.html): A structure that describes a policy definition.
- [PolicyDefinitionItem](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_PolicyDefinitionItem.html): A structure that describes a PolicyDefinintion.
- [PolicyFilter](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_PolicyFilter.html): Contains information about a filter to refine policies returned in a query.
- [PolicyItem](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_PolicyItem.html): Contains information about a policy.
- [PolicyStoreItem](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_PolicyStoreItem.html): Contains information about a policy store.
- [PolicyTemplateItem](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_PolicyTemplateItem.html): Contains details about a policy template
- [ResourceConflict](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_ResourceConflict.html): Contains information about a resource conflict.
- [SchemaDefinition](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_SchemaDefinition.html): Contains a list of principal types, resource types, and actions that can be specified in policies stored in the same policy store.
- [StaticPolicyDefinition](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_StaticPolicyDefinition.html): Contains information about a static policy.
- [StaticPolicyDefinitionDetail](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_StaticPolicyDefinitionDetail.html): A structure that contains details about a static policy.
- [StaticPolicyDefinitionItem](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_StaticPolicyDefinitionItem.html): A structure that contains details about a static policy.
- [TemplateLinkedPolicyDefinition](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_TemplateLinkedPolicyDefinition.html): Contains information about a policy created by instantiating a policy template.
- [TemplateLinkedPolicyDefinitionDetail](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_TemplateLinkedPolicyDefinitionDetail.html): Contains information about a policy that was created by instantiating a policy template.
- [TemplateLinkedPolicyDefinitionItem](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_TemplateLinkedPolicyDefinitionItem.html): Contains information about a policy created by instantiating a policy template.
- [UpdateCognitoGroupConfiguration](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_UpdateCognitoGroupConfiguration.html): The user group entities from an Amazon Cognito user pool identity source.
- [UpdateCognitoUserPoolConfiguration](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_UpdateCognitoUserPoolConfiguration.html): Contains configuration details of a Amazon Cognito user pool for use with an identity source.
- [UpdateConfiguration](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_UpdateConfiguration.html): Contains an update to replace the configuration in an existing identity source.
- [UpdateOpenIdConnectAccessTokenConfiguration](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_UpdateOpenIdConnectAccessTokenConfiguration.html): The configuration of an OpenID Connect (OIDC) identity source for handling access token claims.
- [UpdateOpenIdConnectConfiguration](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_UpdateOpenIdConnectConfiguration.html): Contains configuration details of an OpenID Connect (OIDC) identity provider, or identity source, that Verified Permissions can use to generate entities from authenticated identities.
- [UpdateOpenIdConnectGroupConfiguration](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_UpdateOpenIdConnectGroupConfiguration.html): The claim in OIDC identity provider tokens that indicates a user's group membership, and the entity type that you want to map it to.
- [UpdateOpenIdConnectIdentityTokenConfiguration](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_UpdateOpenIdConnectIdentityTokenConfiguration.html): The configuration of an OpenID Connect (OIDC) identity source for handling identity (ID) token claims.
- [UpdateOpenIdConnectTokenSelection](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_UpdateOpenIdConnectTokenSelection.html): The token type that you want to process from your OIDC identity provider.
- [UpdatePolicyDefinition](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_UpdatePolicyDefinition.html): Contains information about updates to be applied to a policy.
- [UpdateStaticPolicyDefinition](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_UpdateStaticPolicyDefinition.html): Contains information about an update to a static policy.
- [ValidationExceptionField](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_ValidationExceptionField.html): Details about a field that failed policy validation.
- [ValidationSettings](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_ValidationSettings.html): A structure that contains Cedar policy validation settings for the policy store.
