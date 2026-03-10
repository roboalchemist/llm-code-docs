# Source: https://docs.aws.amazon.com/eks/latest/APIReference/llms.txt

# Amazon EKS API Reference

## [Amazon Elastic Kubernetes Service](https://docs.aws.amazon.com/eks/latest/APIReference/Welcome_Amazon_Elastic_Kubernetes_Service.html)

Amazon Elastic Kubernetes Service (Amazon EKS) is a managed service that makes it easy for you to run Kubernetes on AWS without needing to setup or maintain your own Kubernetes control plane. Kubernetes is an open-source system for automating the deployment, scaling, and management of containerized applications.

Amazon EKS runs up-to-date versions of the open-source Kubernetes software, so you can use all the existing plugins and tooling from the Kubernetes community. Applications running on Amazon EKS are fully compatible with applications running on any standard Kubernetes environment, whether running in on-premises data centers or public clouds. This means that you can easily migrate any standard Kubernetes application to Amazon EKS without any code modification required.

### Actions

- [AssociateAccessPolicy](https://docs.aws.amazon.com/eks/latest/APIReference/API_AssociateAccessPolicy.html): Associates an access policy and its scope to an access entry.
- [AssociateEncryptionConfig](https://docs.aws.amazon.com/eks/latest/APIReference/API_AssociateEncryptionConfig.html): Associates an encryption configuration to an existing cluster.
- [AssociateIdentityProviderConfig](https://docs.aws.amazon.com/eks/latest/APIReference/API_AssociateIdentityProviderConfig.html): Associates an identity provider configuration to a cluster.
- [CreateAccessEntry](https://docs.aws.amazon.com/eks/latest/APIReference/API_CreateAccessEntry.html): Creates an access entry.
- [CreateAddon](https://docs.aws.amazon.com/eks/latest/APIReference/API_CreateAddon.html): Creates an Amazon EKS add-on.
- [CreateCapability](https://docs.aws.amazon.com/eks/latest/APIReference/API_CreateCapability.html): Creates a managed capability resource for an Amazon EKS cluster.
- [CreateCluster](https://docs.aws.amazon.com/eks/latest/APIReference/API_CreateCluster.html): Creates an Amazon EKS control plane.
- [CreateEksAnywhereSubscription](https://docs.aws.amazon.com/eks/latest/APIReference/API_CreateEksAnywhereSubscription.html): Creates an EKS Anywhere subscription.
- [CreateFargateProfile](https://docs.aws.amazon.com/eks/latest/APIReference/API_CreateFargateProfile.html): Creates an AWS Fargate profile for your Amazon EKS cluster.
- [CreateNodegroup](https://docs.aws.amazon.com/eks/latest/APIReference/API_CreateNodegroup.html): Creates a managed node group for an Amazon EKS cluster.
- [CreatePodIdentityAssociation](https://docs.aws.amazon.com/eks/latest/APIReference/API_CreatePodIdentityAssociation.html): Creates an EKS Pod Identity association between a service account in an Amazon EKS cluster and an IAM role with EKS Pod Identity.
- [DeleteAccessEntry](https://docs.aws.amazon.com/eks/latest/APIReference/API_DeleteAccessEntry.html): Deletes an access entry.
- [DeleteAddon](https://docs.aws.amazon.com/eks/latest/APIReference/API_DeleteAddon.html): Deletes an Amazon EKS add-on.
- [DeleteCapability](https://docs.aws.amazon.com/eks/latest/APIReference/API_DeleteCapability.html): Deletes a managed capability from your Amazon EKS cluster.
- [DeleteCluster](https://docs.aws.amazon.com/eks/latest/APIReference/API_DeleteCluster.html): Deletes an Amazon EKS cluster control plane.
- [DeleteEksAnywhereSubscription](https://docs.aws.amazon.com/eks/latest/APIReference/API_DeleteEksAnywhereSubscription.html): Deletes an expired or inactive subscription.
- [DeleteFargateProfile](https://docs.aws.amazon.com/eks/latest/APIReference/API_DeleteFargateProfile.html): Deletes an AWS Fargate profile.
- [DeleteNodegroup](https://docs.aws.amazon.com/eks/latest/APIReference/API_DeleteNodegroup.html): Deletes a managed node group.
- [DeletePodIdentityAssociation](https://docs.aws.amazon.com/eks/latest/APIReference/API_DeletePodIdentityAssociation.html): Deletes a EKS Pod Identity association.
- [DeregisterCluster](https://docs.aws.amazon.com/eks/latest/APIReference/API_DeregisterCluster.html): Deregisters a connected cluster to remove it from the Amazon EKS control plane.
- [DescribeAccessEntry](https://docs.aws.amazon.com/eks/latest/APIReference/API_DescribeAccessEntry.html): Describes an access entry.
- [DescribeAddon](https://docs.aws.amazon.com/eks/latest/APIReference/API_DescribeAddon.html): Describes an Amazon EKS add-on.
- [DescribeAddonConfiguration](https://docs.aws.amazon.com/eks/latest/APIReference/API_DescribeAddonConfiguration.html): Returns configuration options.
- [DescribeAddonVersions](https://docs.aws.amazon.com/eks/latest/APIReference/API_DescribeAddonVersions.html): Describes the versions for an add-on.
- [DescribeCapability](https://docs.aws.amazon.com/eks/latest/APIReference/API_DescribeCapability.html): Returns detailed information about a specific managed capability in your Amazon EKS cluster, including its current status, configuration, health information, and any issues that may be affecting its operation.
- [DescribeCluster](https://docs.aws.amazon.com/eks/latest/APIReference/API_DescribeCluster.html): Describes an Amazon EKS cluster.
- [DescribeClusterVersions](https://docs.aws.amazon.com/eks/latest/APIReference/API_DescribeClusterVersions.html): Lists available Kubernetes versions for Amazon EKS clusters.
- [DescribeEksAnywhereSubscription](https://docs.aws.amazon.com/eks/latest/APIReference/API_DescribeEksAnywhereSubscription.html): Returns descriptive information about a subscription.
- [DescribeFargateProfile](https://docs.aws.amazon.com/eks/latest/APIReference/API_DescribeFargateProfile.html): Describes an AWS Fargate profile.
- [DescribeIdentityProviderConfig](https://docs.aws.amazon.com/eks/latest/APIReference/API_DescribeIdentityProviderConfig.html): Describes an identity provider configuration.
- [DescribeInsight](https://docs.aws.amazon.com/eks/latest/APIReference/API_DescribeInsight.html): Returns details about an insight that you specify using its ID.
- [DescribeInsightsRefresh](https://docs.aws.amazon.com/eks/latest/APIReference/API_DescribeInsightsRefresh.html): Returns the status of the latest on-demand cluster insights refresh operation.
- [DescribeNodegroup](https://docs.aws.amazon.com/eks/latest/APIReference/API_DescribeNodegroup.html): Describes a managed node group.
- [DescribePodIdentityAssociation](https://docs.aws.amazon.com/eks/latest/APIReference/API_DescribePodIdentityAssociation.html): Returns descriptive information about an EKS Pod Identity association.
- [DescribeUpdate](https://docs.aws.amazon.com/eks/latest/APIReference/API_DescribeUpdate.html): Describes an update to an Amazon EKS resource.
- [DisassociateAccessPolicy](https://docs.aws.amazon.com/eks/latest/APIReference/API_DisassociateAccessPolicy.html): Disassociates an access policy from an access entry.
- [DisassociateIdentityProviderConfig](https://docs.aws.amazon.com/eks/latest/APIReference/API_DisassociateIdentityProviderConfig.html): Disassociates an identity provider configuration from a cluster.
- [ListAccessEntries](https://docs.aws.amazon.com/eks/latest/APIReference/API_ListAccessEntries.html): Lists the access entries for your cluster.
- [ListAccessPolicies](https://docs.aws.amazon.com/eks/latest/APIReference/API_ListAccessPolicies.html): Lists the available access policies.
- [ListAddons](https://docs.aws.amazon.com/eks/latest/APIReference/API_ListAddons.html): Lists the installed add-ons.
- [ListAssociatedAccessPolicies](https://docs.aws.amazon.com/eks/latest/APIReference/API_ListAssociatedAccessPolicies.html): Lists the access policies associated with an access entry.
- [ListCapabilities](https://docs.aws.amazon.com/eks/latest/APIReference/API_ListCapabilities.html): Lists all managed capabilities in your Amazon EKS cluster.
- [ListClusters](https://docs.aws.amazon.com/eks/latest/APIReference/API_ListClusters.html): Lists the Amazon EKS clusters in your AWS account in the specified AWS Region.
- [ListEksAnywhereSubscriptions](https://docs.aws.amazon.com/eks/latest/APIReference/API_ListEksAnywhereSubscriptions.html): Displays the full description of the subscription.
- [ListFargateProfiles](https://docs.aws.amazon.com/eks/latest/APIReference/API_ListFargateProfiles.html): Lists the AWS Fargate profiles associated with the specified cluster in your AWS account in the specified AWS Region.
- [ListIdentityProviderConfigs](https://docs.aws.amazon.com/eks/latest/APIReference/API_ListIdentityProviderConfigs.html): Lists the identity provider configurations for your cluster.
- [ListInsights](https://docs.aws.amazon.com/eks/latest/APIReference/API_ListInsights.html): Returns a list of all insights checked for against the specified cluster.
- [ListNodegroups](https://docs.aws.amazon.com/eks/latest/APIReference/API_ListNodegroups.html): Lists the managed node groups associated with the specified cluster in your AWS account in the specified AWS Region.
- [ListPodIdentityAssociations](https://docs.aws.amazon.com/eks/latest/APIReference/API_ListPodIdentityAssociations.html): List the EKS Pod Identity associations in a cluster.
- [ListTagsForResource](https://docs.aws.amazon.com/eks/latest/APIReference/API_ListTagsForResource.html): List the tags for an Amazon EKS resource.
- [ListUpdates](https://docs.aws.amazon.com/eks/latest/APIReference/API_ListUpdates.html): Lists the updates associated with an Amazon EKS resource in your AWS account, in the specified AWS Region.
- [RegisterCluster](https://docs.aws.amazon.com/eks/latest/APIReference/API_RegisterCluster.html): Connects a Kubernetes cluster to the Amazon EKS control plane.
- [StartInsightsRefresh](https://docs.aws.amazon.com/eks/latest/APIReference/API_StartInsightsRefresh.html): Initiates an on-demand refresh operation for cluster insights, getting the latest analysis outside of the standard refresh schedule.
- [TagResource](https://docs.aws.amazon.com/eks/latest/APIReference/API_TagResource.html): Associates the specified tags to an Amazon EKS resource with the specified resourceArn.
- [UntagResource](https://docs.aws.amazon.com/eks/latest/APIReference/API_UntagResource.html): Deletes specified tags from an Amazon EKS resource.
- [UpdateAccessEntry](https://docs.aws.amazon.com/eks/latest/APIReference/API_UpdateAccessEntry.html): Updates an access entry.
- [UpdateAddon](https://docs.aws.amazon.com/eks/latest/APIReference/API_UpdateAddon.html): Updates an Amazon EKS add-on.
- [UpdateCapability](https://docs.aws.amazon.com/eks/latest/APIReference/API_UpdateCapability.html): Updates the configuration of a managed capability in your Amazon EKS cluster.
- [UpdateClusterConfig](https://docs.aws.amazon.com/eks/latest/APIReference/API_UpdateClusterConfig.html): Updates an Amazon EKS cluster configuration.
- [UpdateClusterVersion](https://docs.aws.amazon.com/eks/latest/APIReference/API_UpdateClusterVersion.html): Updates an Amazon EKS cluster to the specified Kubernetes version.
- [UpdateEksAnywhereSubscription](https://docs.aws.amazon.com/eks/latest/APIReference/API_UpdateEksAnywhereSubscription.html): Update an EKS Anywhere Subscription.
- [UpdateNodegroupConfig](https://docs.aws.amazon.com/eks/latest/APIReference/API_UpdateNodegroupConfig.html): Updates an Amazon EKS managed node group configuration.
- [UpdateNodegroupVersion](https://docs.aws.amazon.com/eks/latest/APIReference/API_UpdateNodegroupVersion.html): Updates the Kubernetes version or AMI version of an Amazon EKS managed node group.
- [UpdatePodIdentityAssociation](https://docs.aws.amazon.com/eks/latest/APIReference/API_UpdatePodIdentityAssociation.html): Updates a EKS Pod Identity association.

### Data Types

- [AccessConfigResponse](https://docs.aws.amazon.com/eks/latest/APIReference/API_AccessConfigResponse.html): The access configuration for the cluster.
- [AccessEntry](https://docs.aws.amazon.com/eks/latest/APIReference/API_AccessEntry.html): An access entry allows an IAM principal (user or role) to access your cluster.
- [AccessPolicy](https://docs.aws.amazon.com/eks/latest/APIReference/API_AccessPolicy.html): An access policy includes permissions that allow Amazon EKS to authorize an IAM principal to work with Kubernetes objects on your cluster.
- [AccessScope](https://docs.aws.amazon.com/eks/latest/APIReference/API_AccessScope.html): The scope of an AccessPolicy that's associated to an AccessEntry.
- [Addon](https://docs.aws.amazon.com/eks/latest/APIReference/API_Addon.html): An Amazon EKS add-on.
- [AddonCompatibilityDetail](https://docs.aws.amazon.com/eks/latest/APIReference/API_AddonCompatibilityDetail.html): The summary information about the Amazon EKS add-on compatibility for the next Kubernetes version for an insight check in the UPGRADE_READINESS category.
- [AddonHealth](https://docs.aws.amazon.com/eks/latest/APIReference/API_AddonHealth.html): The health of the add-on.
- [AddonInfo](https://docs.aws.amazon.com/eks/latest/APIReference/API_AddonInfo.html): Information about an add-on.
- [AddonIssue](https://docs.aws.amazon.com/eks/latest/APIReference/API_AddonIssue.html): An issue related to an add-on.
- [AddonNamespaceConfigRequest](https://docs.aws.amazon.com/eks/latest/APIReference/API_AddonNamespaceConfigRequest.html): The namespace configuration request object for specifying a custom namespace when creating an addon.
- [AddonNamespaceConfigResponse](https://docs.aws.amazon.com/eks/latest/APIReference/API_AddonNamespaceConfigResponse.html): The namespace configuration response object containing information about the namespace where an addon is installed.
- [AddonPodIdentityAssociations](https://docs.aws.amazon.com/eks/latest/APIReference/API_AddonPodIdentityAssociations.html): A type of EKS Pod Identity association owned by an Amazon EKS add-on.
- [AddonPodIdentityConfiguration](https://docs.aws.amazon.com/eks/latest/APIReference/API_AddonPodIdentityConfiguration.html): Information about how to configure IAM for an add-on.
- [AddonVersionInfo](https://docs.aws.amazon.com/eks/latest/APIReference/API_AddonVersionInfo.html): Information about an add-on version.
- [ArgoCdAwsIdcConfigRequest](https://docs.aws.amazon.com/eks/latest/APIReference/API_ArgoCdAwsIdcConfigRequest.html): Configuration for integrating Argo CD with IAM Identity CenterIAM; Identity Center.
- [ArgoCdAwsIdcConfigResponse](https://docs.aws.amazon.com/eks/latest/APIReference/API_ArgoCdAwsIdcConfigResponse.html): The response object containing IAM Identity CenterIAM; Identity Center configuration details for an Argo CD capability.
- [ArgoCdConfigRequest](https://docs.aws.amazon.com/eks/latest/APIReference/API_ArgoCdConfigRequest.html): Configuration settings for an Argo CD capability.
- [ArgoCdConfigResponse](https://docs.aws.amazon.com/eks/latest/APIReference/API_ArgoCdConfigResponse.html): The response object containing Argo CD configuration details, including the server URL that you use to access the Argo CD web interface and API.
- [ArgoCdNetworkAccessConfigRequest](https://docs.aws.amazon.com/eks/latest/APIReference/API_ArgoCdNetworkAccessConfigRequest.html): Configuration for network access to the Argo CD capability's managed API server endpoint.
- [ArgoCdNetworkAccessConfigResponse](https://docs.aws.amazon.com/eks/latest/APIReference/API_ArgoCdNetworkAccessConfigResponse.html): The response object containing network access configuration for the Argo CD capability's managed API server endpoint.
- [ArgoCdRoleMapping](https://docs.aws.amazon.com/eks/latest/APIReference/API_ArgoCdRoleMapping.html): A mapping between an Argo CD role and IAM Identity CenterIAM; Identity Center identities.
- [AssociatedAccessPolicy](https://docs.aws.amazon.com/eks/latest/APIReference/API_AssociatedAccessPolicy.html): An access policy association.
- [AutoScalingGroup](https://docs.aws.amazon.com/eks/latest/APIReference/API_AutoScalingGroup.html): An Auto Scaling group that is associated with an Amazon EKS managed node group.
- [BlockStorage](https://docs.aws.amazon.com/eks/latest/APIReference/API_BlockStorage.html): Indicates the current configuration of the block storage capability on your EKS Auto Mode cluster.
- [Capability](https://docs.aws.amazon.com/eks/latest/APIReference/API_Capability.html): An object representing a managed capability in an Amazon EKS cluster.
- [CapabilityConfigurationRequest](https://docs.aws.amazon.com/eks/latest/APIReference/API_CapabilityConfigurationRequest.html): Configuration settings for a capability.
- [CapabilityConfigurationResponse](https://docs.aws.amazon.com/eks/latest/APIReference/API_CapabilityConfigurationResponse.html): The response object containing capability configuration details.
- [CapabilityHealth](https://docs.aws.amazon.com/eks/latest/APIReference/API_CapabilityHealth.html): Health information for a capability, including any issues that may be affecting its operation.
- [CapabilityIssue](https://docs.aws.amazon.com/eks/latest/APIReference/API_CapabilityIssue.html): An issue affecting a capability's health or operation.
- [CapabilitySummary](https://docs.aws.amazon.com/eks/latest/APIReference/API_CapabilitySummary.html): A summary of a capability, containing basic information without the full configuration details.
- [Certificate](https://docs.aws.amazon.com/eks/latest/APIReference/API_Certificate.html): An object representing the certificate-authority-data for your cluster.
- [ClientStat](https://docs.aws.amazon.com/eks/latest/APIReference/API_ClientStat.html): Details about clients using the deprecated resources.
- [Cluster](https://docs.aws.amazon.com/eks/latest/APIReference/API_Cluster.html): An object representing an Amazon EKS cluster.
- [ClusterHealth](https://docs.aws.amazon.com/eks/latest/APIReference/API_ClusterHealth.html): An object representing the health of your Amazon EKS cluster.
- [ClusterIssue](https://docs.aws.amazon.com/eks/latest/APIReference/API_ClusterIssue.html): An issue with your Amazon EKS cluster.
- [ClusterVersionInformation](https://docs.aws.amazon.com/eks/latest/APIReference/API_ClusterVersionInformation.html): Contains details about a specific EKS cluster version.
- [Compatibility](https://docs.aws.amazon.com/eks/latest/APIReference/API_Compatibility.html): Compatibility information.
- [ComputeConfigRequest](https://docs.aws.amazon.com/eks/latest/APIReference/API_ComputeConfigRequest.html): Request to update the configuration of the compute capability of your EKS Auto Mode cluster.
- [ComputeConfigResponse](https://docs.aws.amazon.com/eks/latest/APIReference/API_ComputeConfigResponse.html): Indicates the status of the request to update the compute capability of your EKS Auto Mode cluster.
- [ConnectorConfigRequest](https://docs.aws.amazon.com/eks/latest/APIReference/API_ConnectorConfigRequest.html): The configuration sent to a cluster for configuration.
- [ConnectorConfigResponse](https://docs.aws.amazon.com/eks/latest/APIReference/API_ConnectorConfigResponse.html): The full description of your connected cluster.
- [ControlPlanePlacementRequest](https://docs.aws.amazon.com/eks/latest/APIReference/API_ControlPlanePlacementRequest.html): The placement configuration for all the control plane instances of your local Amazon EKS cluster on an AWS Outpost.
- [ControlPlanePlacementResponse](https://docs.aws.amazon.com/eks/latest/APIReference/API_ControlPlanePlacementResponse.html): The placement configuration for all the control plane instances of your local Amazon EKS cluster on an AWS Outpost.
- [ControlPlaneScalingConfig](https://docs.aws.amazon.com/eks/latest/APIReference/API_ControlPlaneScalingConfig.html): The control plane scaling tier configuration.
- [CreateAccessConfigRequest](https://docs.aws.amazon.com/eks/latest/APIReference/API_CreateAccessConfigRequest.html): The access configuration information for the cluster.
- [DeprecationDetail](https://docs.aws.amazon.com/eks/latest/APIReference/API_DeprecationDetail.html): The summary information about deprecated resource usage for an insight check in the UPGRADE_READINESS category.
- [EksAnywhereSubscription](https://docs.aws.amazon.com/eks/latest/APIReference/API_EksAnywhereSubscription.html): An EKS Anywhere subscription authorizing the customer to support for licensed clusters and access to EKS Anywhere Curated Packages.
- [EksAnywhereSubscriptionTerm](https://docs.aws.amazon.com/eks/latest/APIReference/API_EksAnywhereSubscriptionTerm.html): An object representing the term duration and term unit type of your subscription.
- [ElasticLoadBalancing](https://docs.aws.amazon.com/eks/latest/APIReference/API_ElasticLoadBalancing.html): Indicates the current configuration of the load balancing capability on your EKS Auto Mode cluster.
- [EncryptionConfig](https://docs.aws.amazon.com/eks/latest/APIReference/API_EncryptionConfig.html): The encryption configuration for the cluster.
- [ErrorDetail](https://docs.aws.amazon.com/eks/latest/APIReference/API_ErrorDetail.html): An object representing an error when an asynchronous operation fails.
- [FargateProfile](https://docs.aws.amazon.com/eks/latest/APIReference/API_FargateProfile.html): An object representing an AWS Fargate profile.
- [FargateProfileHealth](https://docs.aws.amazon.com/eks/latest/APIReference/API_FargateProfileHealth.html): The health status of the Fargate profile.
- [FargateProfileIssue](https://docs.aws.amazon.com/eks/latest/APIReference/API_FargateProfileIssue.html): An issue that is associated with the Fargate profile.
- [FargateProfileSelector](https://docs.aws.amazon.com/eks/latest/APIReference/API_FargateProfileSelector.html): An object representing an AWS Fargate profile selector.
- [Identity](https://docs.aws.amazon.com/eks/latest/APIReference/API_Identity.html): An object representing an identity provider.
- [IdentityProviderConfig](https://docs.aws.amazon.com/eks/latest/APIReference/API_IdentityProviderConfig.html): An object representing an identity provider configuration.
- [IdentityProviderConfigResponse](https://docs.aws.amazon.com/eks/latest/APIReference/API_IdentityProviderConfigResponse.html): The full description of your identity configuration.
- [Insight](https://docs.aws.amazon.com/eks/latest/APIReference/API_Insight.html): A check that provides recommendations to remedy potential upgrade-impacting issues.
- [InsightCategorySpecificSummary](https://docs.aws.amazon.com/eks/latest/APIReference/API_InsightCategorySpecificSummary.html): Summary information that relates to the category of the insight.
- [InsightResourceDetail](https://docs.aws.amazon.com/eks/latest/APIReference/API_InsightResourceDetail.html): Returns information about the resource being evaluated.
- [InsightsFilter](https://docs.aws.amazon.com/eks/latest/APIReference/API_InsightsFilter.html): The criteria to use for the insights.
- [InsightStatus](https://docs.aws.amazon.com/eks/latest/APIReference/API_InsightStatus.html): The status of the insight.
- [InsightSummary](https://docs.aws.amazon.com/eks/latest/APIReference/API_InsightSummary.html): The summarized description of the insight.
- [Issue](https://docs.aws.amazon.com/eks/latest/APIReference/API_Issue.html): An object representing an issue with an Amazon EKS resource.
- [KubernetesNetworkConfigRequest](https://docs.aws.amazon.com/eks/latest/APIReference/API_KubernetesNetworkConfigRequest.html): The Kubernetes network configuration for the cluster.
- [KubernetesNetworkConfigResponse](https://docs.aws.amazon.com/eks/latest/APIReference/API_KubernetesNetworkConfigResponse.html): The Kubernetes network configuration for the cluster.
- [LaunchTemplateSpecification](https://docs.aws.amazon.com/eks/latest/APIReference/API_LaunchTemplateSpecification.html): An object representing a node group launch template specification.
- [License](https://docs.aws.amazon.com/eks/latest/APIReference/API_License.html): An EKS Anywhere license associated with a subscription.
- [Logging](https://docs.aws.amazon.com/eks/latest/APIReference/API_Logging.html): An object representing the logging configuration for resources in your cluster.
- [LogSetup](https://docs.aws.amazon.com/eks/latest/APIReference/API_LogSetup.html): An object representing the enabled or disabled Kubernetes control plane logs for your cluster.
- [MarketplaceInformation](https://docs.aws.amazon.com/eks/latest/APIReference/API_MarketplaceInformation.html): Information about an Amazon EKS add-on from the AWS Marketplace.
- [Nodegroup](https://docs.aws.amazon.com/eks/latest/APIReference/API_Nodegroup.html): An object representing an Amazon EKS managed node group.
- [NodegroupHealth](https://docs.aws.amazon.com/eks/latest/APIReference/API_NodegroupHealth.html): An object representing the health status of the node group.
- [NodegroupResources](https://docs.aws.amazon.com/eks/latest/APIReference/API_NodegroupResources.html): An object representing the resources associated with the node group, such as Auto Scaling groups and security groups for remote access.
- [NodegroupScalingConfig](https://docs.aws.amazon.com/eks/latest/APIReference/API_NodegroupScalingConfig.html): An object representing the scaling configuration details for the Auto Scaling group that is associated with your node group.
- [NodegroupUpdateConfig](https://docs.aws.amazon.com/eks/latest/APIReference/API_NodegroupUpdateConfig.html): The node group update configuration.
- [NodeRepairConfig](https://docs.aws.amazon.com/eks/latest/APIReference/API_NodeRepairConfig.html): The node auto repair configuration for the node group.
- [NodeRepairConfigOverrides](https://docs.aws.amazon.com/eks/latest/APIReference/API_NodeRepairConfigOverrides.html): Specify granular overrides for specific repair actions.
- [OIDC](https://docs.aws.amazon.com/eks/latest/APIReference/API_OIDC.html): An object representing the OpenID Connect (OIDC) identity provider information for the cluster.
- [OidcIdentityProviderConfig](https://docs.aws.amazon.com/eks/latest/APIReference/API_OidcIdentityProviderConfig.html): An object representing the configuration for an OpenID Connect (OIDC) identity provider.
- [OidcIdentityProviderConfigRequest](https://docs.aws.amazon.com/eks/latest/APIReference/API_OidcIdentityProviderConfigRequest.html): An object representing an OpenID Connect (OIDC) configuration.
- [OutpostConfigRequest](https://docs.aws.amazon.com/eks/latest/APIReference/API_OutpostConfigRequest.html): The configuration of your local Amazon EKS cluster on an AWS Outpost.
- [OutpostConfigResponse](https://docs.aws.amazon.com/eks/latest/APIReference/API_OutpostConfigResponse.html): An object representing the configuration of your local Amazon EKS cluster on an AWS Outpost.
- [PodIdentityAssociation](https://docs.aws.amazon.com/eks/latest/APIReference/API_PodIdentityAssociation.html): Amazon EKS Pod Identity associations provide the ability to manage credentials for your applications, similar to the way that Amazon EC2 instance profiles provide credentials to Amazon EC2 instances.
- [PodIdentityAssociationSummary](https://docs.aws.amazon.com/eks/latest/APIReference/API_PodIdentityAssociationSummary.html): The summarized description of the association.
- [Provider](https://docs.aws.amazon.com/eks/latest/APIReference/API_Provider.html): Identifies the AWS Key Management Service (AWS KMS) key used to encrypt the secrets.
- [RemoteAccessConfig](https://docs.aws.amazon.com/eks/latest/APIReference/API_RemoteAccessConfig.html): An object representing the remote access configuration for the managed node group.
- [RemoteNetworkConfigRequest](https://docs.aws.amazon.com/eks/latest/APIReference/API_RemoteNetworkConfigRequest.html): The configuration in the cluster for EKS Hybrid Nodes.
- [RemoteNetworkConfigResponse](https://docs.aws.amazon.com/eks/latest/APIReference/API_RemoteNetworkConfigResponse.html): The configuration in the cluster for EKS Hybrid Nodes.
- [RemoteNodeNetwork](https://docs.aws.amazon.com/eks/latest/APIReference/API_RemoteNodeNetwork.html): A network CIDR that can contain hybrid nodes.
- [RemotePodNetwork](https://docs.aws.amazon.com/eks/latest/APIReference/API_RemotePodNetwork.html): A network CIDR that can contain pods that run Kubernetes webhooks on hybrid nodes.
- [SsoIdentity](https://docs.aws.amazon.com/eks/latest/APIReference/API_SsoIdentity.html): An IAM Identity CenterIAM; Identity Center identity (user or group) that can be assigned permissions in a capability.
- [StorageConfigRequest](https://docs.aws.amazon.com/eks/latest/APIReference/API_StorageConfigRequest.html): Request to update the configuration of the storage capability of your EKS Auto Mode cluster.
- [StorageConfigResponse](https://docs.aws.amazon.com/eks/latest/APIReference/API_StorageConfigResponse.html): Indicates the status of the request to update the block storage capability of your EKS Auto Mode cluster.
- [Taint](https://docs.aws.amazon.com/eks/latest/APIReference/API_Taint.html): A property that allows a node to repel a Pod.
- [Update](https://docs.aws.amazon.com/eks/latest/APIReference/API_Update.html): An object representing an asynchronous update.
- [UpdateAccessConfigRequest](https://docs.aws.amazon.com/eks/latest/APIReference/API_UpdateAccessConfigRequest.html): The access configuration information for the cluster.
- [UpdateArgoCdConfig](https://docs.aws.amazon.com/eks/latest/APIReference/API_UpdateArgoCdConfig.html): Configuration updates for an Argo CD capability.
- [UpdateCapabilityConfiguration](https://docs.aws.amazon.com/eks/latest/APIReference/API_UpdateCapabilityConfiguration.html): Configuration updates for a capability.
- [UpdateLabelsPayload](https://docs.aws.amazon.com/eks/latest/APIReference/API_UpdateLabelsPayload.html): An object representing a Kubernetes label change for a managed node group.
- [UpdateParam](https://docs.aws.amazon.com/eks/latest/APIReference/API_UpdateParam.html): An object representing the details of an update request.
- [UpdateRoleMappings](https://docs.aws.amazon.com/eks/latest/APIReference/API_UpdateRoleMappings.html): Updates to RBAC role mappings for an Argo CD capability.
- [UpdateTaintsPayload](https://docs.aws.amazon.com/eks/latest/APIReference/API_UpdateTaintsPayload.html): An object representing the details of an update to a taints payload.
- [UpgradePolicyRequest](https://docs.aws.amazon.com/eks/latest/APIReference/API_UpgradePolicyRequest.html): The support policy to use for the cluster.
- [UpgradePolicyResponse](https://docs.aws.amazon.com/eks/latest/APIReference/API_UpgradePolicyResponse.html): This value indicates if extended support is enabled or disabled for the cluster.
- [VpcConfigRequest](https://docs.aws.amazon.com/eks/latest/APIReference/API_VpcConfigRequest.html): An object representing the VPC configuration to use for an Amazon EKS cluster.
- [VpcConfigResponse](https://docs.aws.amazon.com/eks/latest/APIReference/API_VpcConfigResponse.html): An object representing an Amazon EKS cluster VPC configuration response.
- [ZonalShiftConfigRequest](https://docs.aws.amazon.com/eks/latest/APIReference/API_ZonalShiftConfigRequest.html): The configuration for zonal shift for the cluster.
- [ZonalShiftConfigResponse](https://docs.aws.amazon.com/eks/latest/APIReference/API_ZonalShiftConfigResponse.html): The status of zonal shift configuration for the cluster

## [Amazon EKS Auth](https://docs.aws.amazon.com/eks/latest/APIReference/Welcome_Amazon_EKS_Auth.html)

The Amazon EKS Auth API and the `AssumeRoleForPodIdentity`action are only used by the EKS Pod Identity Agent.

### Actions

- [AssumeRoleForPodIdentity](https://docs.aws.amazon.com/eks/latest/APIReference/API_auth_AssumeRoleForPodIdentity.html): The Amazon EKS Auth API and the AssumeRoleForPodIdentity action are only used by the EKS Pod Identity Agent.

### Data Types

- [AssumedRoleUser](https://docs.aws.amazon.com/eks/latest/APIReference/API_auth_AssumedRoleUser.html): An object with the permanent IAM role identity and the temporary session name.
- [Credentials](https://docs.aws.amazon.com/eks/latest/APIReference/API_auth_Credentials.html): The AWS Signature Version 4 type of temporary credentials.
- [PodIdentityAssociation](https://docs.aws.amazon.com/eks/latest/APIReference/API_auth_PodIdentityAssociation.html): Amazon EKS Pod Identity associations provide the ability to manage credentials for your applications, similar to the way that Amazon EC2 instance profiles provide credentials to Amazon EC2 instances.
- [Subject](https://docs.aws.amazon.com/eks/latest/APIReference/API_auth_Subject.html): An object containing the name of the Kubernetes service account inside the cluster to associate the IAM credentials with.

## Common

- [Common Parameters](https://docs.aws.amazon.com/eks/latest/APIReference/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/eks/latest/APIReference/CommonErrors.html)