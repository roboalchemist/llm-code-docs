# Source: https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/llms.txt

# Amazon OpenSearch Serverless API Reference

> Use the Amazon OpenSearch Serverless API to create, configure, and manage OpenSearch Serverless collections and security policies.

- [Welcome](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/Welcome.html)
- [Common Parameters](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/CommonErrors.html)

## [Actions](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_Operations.html)

- [BatchGetCollection](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_BatchGetCollection.html): Returns attributes for one or more collections, including the collection endpoint, the OpenSearch Dashboards endpoint, and FIPS-compliant endpoints.
- [BatchGetCollectionGroup](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_BatchGetCollectionGroup.html): Returns attributes for one or more collection groups, including capacity limits and the number of collections in each group.
- [BatchGetEffectiveLifecyclePolicy](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_BatchGetEffectiveLifecyclePolicy.html): Returns a list of successful and failed retrievals for the OpenSearch Serverless indexes.
- [BatchGetLifecyclePolicy](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_BatchGetLifecyclePolicy.html): Returns one or more configured OpenSearch Serverless lifecycle policies.
- [BatchGetVpcEndpoint](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_BatchGetVpcEndpoint.html): Returns attributes for one or more VPC endpoints associated with the current account.
- [CreateAccessPolicy](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_CreateAccessPolicy.html): Creates a data access policy for OpenSearch Serverless.
- [CreateCollection](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_CreateCollection.html): Creates a new OpenSearch Serverless collection.
- [CreateCollectionGroup](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_CreateCollectionGroup.html): Creates a collection group within OpenSearch Serverless.
- [CreateIndex](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_CreateIndex.html): Creates an index within an OpenSearch Serverless collection.
- [CreateLifecyclePolicy](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_CreateLifecyclePolicy.html): Creates a lifecyle policy to be applied to OpenSearch Serverless indexes.
- [CreateSecurityConfig](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_CreateSecurityConfig.html): Specifies a security configuration for OpenSearch Serverless.
- [CreateSecurityPolicy](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_CreateSecurityPolicy.html): Creates a security policy to be used by one or more OpenSearch Serverless collections.
- [CreateVpcEndpoint](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_CreateVpcEndpoint.html): Creates an OpenSearch Serverless-managed interface VPC endpoint.
- [DeleteAccessPolicy](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_DeleteAccessPolicy.html): Deletes an OpenSearch Serverless access policy.
- [DeleteCollection](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_DeleteCollection.html): Deletes an OpenSearch Serverless collection.
- [DeleteCollectionGroup](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_DeleteCollectionGroup.html): Deletes a collection group.
- [DeleteIndex](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_DeleteIndex.html): Deletes an index from an OpenSearch Serverless collection.
- [DeleteLifecyclePolicy](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_DeleteLifecyclePolicy.html): Deletes an OpenSearch Serverless lifecycle policy.
- [DeleteSecurityConfig](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_DeleteSecurityConfig.html): Deletes a security configuration for OpenSearch Serverless.
- [DeleteSecurityPolicy](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_DeleteSecurityPolicy.html): Deletes an OpenSearch Serverless security policy.
- [DeleteVpcEndpoint](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_DeleteVpcEndpoint.html): Deletes an OpenSearch Serverless-managed interface endpoint.
- [GetAccessPolicy](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_GetAccessPolicy.html): Returns an OpenSearch Serverless access policy.
- [GetAccountSettings](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_GetAccountSettings.html): Returns account-level settings related to OpenSearch Serverless.
- [GetIndex](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_GetIndex.html): Retrieves information about an index in an OpenSearch Serverless collection, including its schema definition.
- [GetPoliciesStats](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_GetPoliciesStats.html): Returns statistical information about your OpenSearch Serverless access policies, security configurations, and security policies.
- [GetSecurityConfig](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_GetSecurityConfig.html): Returns information about an OpenSearch Serverless security configuration.
- [GetSecurityPolicy](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_GetSecurityPolicy.html): Returns information about a configured OpenSearch Serverless security policy.
- [ListAccessPolicies](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_ListAccessPolicies.html): Returns information about a list of OpenSearch Serverless access policies.
- [ListCollectionGroups](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_ListCollectionGroups.html): Returns a list of collection groups.
- [ListCollections](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_ListCollections.html): Lists all OpenSearch Serverless collections.
- [ListLifecyclePolicies](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_ListLifecyclePolicies.html): Returns a list of OpenSearch Serverless lifecycle policies.
- [ListSecurityConfigs](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_ListSecurityConfigs.html): Returns information about configured OpenSearch Serverless security configurations.
- [ListSecurityPolicies](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_ListSecurityPolicies.html): Returns information about configured OpenSearch Serverless security policies.
- [ListTagsForResource](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_ListTagsForResource.html): Returns the tags for an OpenSearch Serverless resource.
- [ListVpcEndpoints](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_ListVpcEndpoints.html): Returns the OpenSearch Serverless-managed interface VPC endpoints associated with the current account.
- [TagResource](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_TagResource.html): Associates tags with an OpenSearch Serverless resource.
- [UntagResource](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_UntagResource.html): Removes a tag or set of tags from an OpenSearch Serverless resource.
- [UpdateAccessPolicy](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_UpdateAccessPolicy.html): Updates an OpenSearch Serverless access policy.
- [UpdateAccountSettings](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_UpdateAccountSettings.html): Update the OpenSearch Serverless settings for the current AWS account.
- [UpdateCollection](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_UpdateCollection.html): Updates an OpenSearch Serverless collection.
- [UpdateCollectionGroup](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_UpdateCollectionGroup.html): Updates the description and capacity limits of a collection group.
- [UpdateIndex](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_UpdateIndex.html): Updates an existing index in an OpenSearch Serverless collection.
- [UpdateLifecyclePolicy](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_UpdateLifecyclePolicy.html): Updates an OpenSearch Serverless access policy.
- [UpdateSecurityConfig](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_UpdateSecurityConfig.html): Updates a security configuration for OpenSearch Serverless.
- [UpdateSecurityPolicy](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_UpdateSecurityPolicy.html): Updates an OpenSearch Serverless security policy.
- [UpdateVpcEndpoint](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_UpdateVpcEndpoint.html): Updates an OpenSearch Serverless-managed interface endpoint.


## [Data Types](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_Types.html)

- [AccessPolicyDetail](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_AccessPolicyDetail.html): Details about an OpenSearch Serverless access policy.
- [AccessPolicyStats](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_AccessPolicyStats.html): Statistics for an OpenSearch Serverless access policy.
- [AccessPolicySummary](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_AccessPolicySummary.html): A summary of the data access policy.
- [AccountSettingsDetail](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_AccountSettingsDetail.html): OpenSearch Serverless-related information for the current account.
- [CapacityLimits](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_CapacityLimits.html): The maximum capacity limits for all OpenSearch Serverless collections, in OpenSearch Compute Units (OCUs).
- [CollectionDetail](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_CollectionDetail.html): Details about each OpenSearch Serverless collection, including the collection endpoint, the OpenSearch Dashboards endpoint, and FIPS-compliant endpoints for federal government workloads.
- [CollectionErrorDetail](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_CollectionErrorDetail.html): Error information for an OpenSearch Serverless request.
- [CollectionFilters](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_CollectionFilters.html): A list of filter keys that you can use for LIST, UPDATE, and DELETE requests to OpenSearch Serverless collections.
- [CollectionGroupCapacityLimits](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_CollectionGroupCapacityLimits.html): Capacity limits for a collection group.
- [CollectionGroupDetail](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_CollectionGroupDetail.html): Details about a collection group.
- [CollectionGroupErrorDetail](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_CollectionGroupErrorDetail.html): Error details for a collection group operation.
- [CollectionGroupSummary](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_CollectionGroupSummary.html): Summary information about a collection group.
- [CollectionSummary](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_CollectionSummary.html): Details about each OpenSearch Serverless collection.
- [CreateCollectionDetail](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_CreateCollectionDetail.html): Details about the created OpenSearch Serverless collection.
- [CreateCollectionGroupDetail](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_CreateCollectionGroupDetail.html): Details about the created collection group.
- [CreateIamIdentityCenterConfigOptions](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_CreateIamIdentityCenterConfigOptions.html): Describes IAM Identity Center options for creating an OpenSearch Serverless security configuration in the form of a key-value map.
- [CreateVpcEndpointDetail](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_CreateVpcEndpointDetail.html): Creation details for an OpenSearch Serverless-managed interface endpoint.
- [DeleteCollectionDetail](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_DeleteCollectionDetail.html): Details about a deleted OpenSearch Serverless collection.
- [DeleteVpcEndpointDetail](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_DeleteVpcEndpointDetail.html): Deletion details for an OpenSearch Serverless-managed interface endpoint.
- [EffectiveLifecyclePolicyDetail](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_EffectiveLifecyclePolicyDetail.html): Error information for an OpenSearch Serverless request.
- [EffectiveLifecyclePolicyErrorDetail](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_EffectiveLifecyclePolicyErrorDetail.html): Error information for an OpenSearch Serverless request.
- [EncryptionConfig](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_EncryptionConfig.html): Encryption settings for a collection.
- [FipsEndpoints](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_FipsEndpoints.html): FIPS-compliant endpoint URLs for an OpenSearch Serverless collection.
- [IamFederationConfigOptions](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_IamFederationConfigOptions.html): Describes IAM federation options for an OpenSearch Serverless security configuration in the form of a key-value map.
- [IamIdentityCenterConfigOptions](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_IamIdentityCenterConfigOptions.html): Describes IAM Identity Center options for an OpenSearch Serverless security configuration in the form of a key-value map.
- [LifecyclePolicyDetail](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_LifecyclePolicyDetail.html): Details about an OpenSearch Serverless lifecycle policy.
- [LifecyclePolicyErrorDetail](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_LifecyclePolicyErrorDetail.html): Error information for an OpenSearch Serverless request.
- [LifecyclePolicyIdentifier](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_LifecyclePolicyIdentifier.html): The unique identifiers of policy types and policy names.
- [LifecyclePolicyResourceIdentifier](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_LifecyclePolicyResourceIdentifier.html): The unique identifiers of policy types and resource names.
- [LifecyclePolicyStats](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_LifecyclePolicyStats.html): Statistics for an OpenSearch Serverless lifecycle policy.
- [LifecyclePolicySummary](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_LifecyclePolicySummary.html): A summary of the lifecycle policy.
- [SamlConfigOptions](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_SamlConfigOptions.html): Describes SAML options for an OpenSearch Serverless security configuration in the form of a key-value map.
- [SecurityConfigDetail](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_SecurityConfigDetail.html): Details about a security configuration for OpenSearch Serverless.
- [SecurityConfigStats](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_SecurityConfigStats.html): Statistics for an OpenSearch Serverless security configuration.
- [SecurityConfigSummary](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_SecurityConfigSummary.html): A summary of a security configuration for OpenSearch Serverless.
- [SecurityPolicyDetail](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_SecurityPolicyDetail.html): Details about an OpenSearch Serverless security policy.
- [SecurityPolicyStats](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_SecurityPolicyStats.html): Statistics for an OpenSearch Serverless security policy.
- [SecurityPolicySummary](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_SecurityPolicySummary.html): A summary of a security policy for OpenSearch Serverless.
- [Tag](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_Tag.html): A map of key-value pairs associated to an OpenSearch Serverless resource.
- [UpdateCollectionDetail](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_UpdateCollectionDetail.html): Details about an updated OpenSearch Serverless collection.
- [UpdateCollectionGroupDetail](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_UpdateCollectionGroupDetail.html): Details about the updated collection group.
- [UpdateIamIdentityCenterConfigOptions](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_UpdateIamIdentityCenterConfigOptions.html): Describes IAM Identity Center options for updating an OpenSearch Serverless security configuration in the form of a key-value map.
- [UpdateVpcEndpointDetail](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_UpdateVpcEndpointDetail.html): Update details for an OpenSearch Serverless-managed interface endpoint.
- [VectorOptions](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_VectorOptions.html): Configuration options for vector search capabilities in an OpenSearch Serverless collection.
- [VpcEndpointDetail](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_VpcEndpointDetail.html): Details about an OpenSearch Serverless-managed interface endpoint.
- [VpcEndpointErrorDetail](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_VpcEndpointErrorDetail.html): Error information for a failed BatchGetVpcEndpoint request.
- [VpcEndpointFilters](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_VpcEndpointFilters.html): Filter the results of a ListVpcEndpoints request.
- [VpcEndpointSummary](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_VpcEndpointSummary.html): The VPC endpoint object.
