# Source: https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/llms.txt

# Elastic Load Balancing API Reference

> A load balancer distributes incoming traffic across targets, such as your EC2 instances. This enables you to increase the availability of your application. The load balancer also monitors the health of its registered targets and ensures that it routes traffic only to healthy targets. You configure your load balancer to accept incoming traffic by specifying one or more listeners, which are configured with a protocol and port number for connections from clients to the load balancer. You configure a target group with a protocol and port number for connections from the load balancer to the targets, and with health check settings to be used when checking the health status of the targets.

- [Welcome](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/Welcome.html)
- [Common Parameters](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/CommonErrors.html)

## [Actions](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_Operations.html)

- [AddListenerCertificates](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_AddListenerCertificates.html): Adds the specified SSL server certificate to the certificate list for the specified HTTPS or TLS listener.
- [AddTags](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_AddTags.html): Adds the specified tags to the specified Elastic Load Balancing resource.
- [AddTrustStoreRevocations](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_AddTrustStoreRevocations.html): Adds the specified revocation file to the specified trust store.
- [CreateListener](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_CreateListener.html): Creates a listener for the specified Application Load Balancer, Network Load Balancer, or Gateway Load Balancer.
- [CreateLoadBalancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_CreateLoadBalancer.html): Creates an Application Load Balancer, Network Load Balancer, or Gateway Load Balancer.
- [CreateRule](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_CreateRule.html): Creates a rule for the specified listener.
- [CreateTargetGroup](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_CreateTargetGroup.html): Creates a target group.
- [CreateTrustStore](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_CreateTrustStore.html): Creates a trust store.
- [DeleteListener](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_DeleteListener.html): Deletes the specified listener.
- [DeleteLoadBalancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_DeleteLoadBalancer.html): Deletes the specified Application Load Balancer, Network Load Balancer, or Gateway Load Balancer.
- [DeleteRule](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_DeleteRule.html): Deletes the specified rule.
- [DeleteSharedTrustStoreAssociation](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_DeleteSharedTrustStoreAssociation.html): Deletes a shared trust store association.
- [DeleteTargetGroup](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_DeleteTargetGroup.html): Deletes the specified target group.
- [DeleteTrustStore](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_DeleteTrustStore.html): Deletes a trust store.
- [DeregisterTargets](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_DeregisterTargets.html): Deregisters the specified targets from the specified target group.
- [DescribeAccountLimits](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_DescribeAccountLimits.html): Describes the current Elastic Load Balancing resource limits for your AWS account.
- [DescribeCapacityReservation](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_DescribeCapacityReservation.html): Describes the capacity reservation status for the specified load balancer.
- [DescribeListenerAttributes](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_DescribeListenerAttributes.html): Describes the attributes for the specified listener.
- [DescribeListenerCertificates](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_DescribeListenerCertificates.html): Describes the default certificate and the certificate list for the specified HTTPS or TLS listener.
- [DescribeListeners](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_DescribeListeners.html): Describes the specified listeners or the listeners for the specified Application Load Balancer, Network Load Balancer, or Gateway Load Balancer.
- [DescribeLoadBalancerAttributes](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_DescribeLoadBalancerAttributes.html): Describes the attributes for the specified Application Load Balancer, Network Load Balancer, or Gateway Load Balancer.
- [DescribeLoadBalancers](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_DescribeLoadBalancers.html): Describes the specified load balancers or all of your load balancers.
- [DescribeRules](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_DescribeRules.html): Describes the specified rules or the rules for the specified listener.
- [DescribeSSLPolicies](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_DescribeSSLPolicies.html): Describes the specified policies or all policies used for SSL negotiation.
- [DescribeTags](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_DescribeTags.html): Describes the tags for the specified Elastic Load Balancing resources.
- [DescribeTargetGroupAttributes](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_DescribeTargetGroupAttributes.html): Describes the attributes for the specified target group.
- [DescribeTargetGroups](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_DescribeTargetGroups.html): Describes the specified target groups or all of your target groups.
- [DescribeTargetHealth](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_DescribeTargetHealth.html): Describes the health of the specified targets or all of your targets.
- [DescribeTrustStoreAssociations](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_DescribeTrustStoreAssociations.html): Describes all resources associated with the specified trust store.
- [DescribeTrustStoreRevocations](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_DescribeTrustStoreRevocations.html): Describes the revocation files in use by the specified trust store or revocation files.
- [DescribeTrustStores](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_DescribeTrustStores.html): Describes all trust stores for the specified account.
- [GetResourcePolicy](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_GetResourcePolicy.html): Retrieves the resource policy for a specified resource.
- [GetTrustStoreCaCertificatesBundle](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_GetTrustStoreCaCertificatesBundle.html): Retrieves the ca certificate bundle.
- [GetTrustStoreRevocationContent](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_GetTrustStoreRevocationContent.html): Retrieves the specified revocation file.
- [ModifyCapacityReservation](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_ModifyCapacityReservation.html): Modifies the capacity reservation of the specified load balancer.
- [ModifyIpPools](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_ModifyIpPools.html): [Application Load Balancers] Modify the IP pool associated to a load balancer.
- [ModifyListener](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_ModifyListener.html): Replaces the specified properties of the specified listener.
- [ModifyListenerAttributes](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_ModifyListenerAttributes.html): Modifies the specified attributes of the specified listener.
- [ModifyLoadBalancerAttributes](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_ModifyLoadBalancerAttributes.html): Modifies the specified attributes of the specified Application Load Balancer, Network Load Balancer, or Gateway Load Balancer.
- [ModifyRule](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_ModifyRule.html): Replaces the specified properties of the specified rule.
- [ModifyTargetGroup](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_ModifyTargetGroup.html): Modifies the health checks used when evaluating the health state of the targets in the specified target group.
- [ModifyTargetGroupAttributes](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_ModifyTargetGroupAttributes.html): Modifies the specified attributes of the specified target group.
- [ModifyTrustStore](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_ModifyTrustStore.html): Update the ca certificate bundle for the specified trust store.
- [RegisterTargets](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_RegisterTargets.html): Registers the specified targets with the specified target group.
- [RemoveListenerCertificates](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_RemoveListenerCertificates.html): Removes the specified certificate from the certificate list for the specified HTTPS or TLS listener.
- [RemoveTags](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_RemoveTags.html): Removes the specified tags from the specified Elastic Load Balancing resources.
- [RemoveTrustStoreRevocations](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_RemoveTrustStoreRevocations.html): Removes the specified revocation file from the specified trust store.
- [SetIpAddressType](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_SetIpAddressType.html): Sets the type of IP addresses used by the subnets of the specified load balancer.
- [SetRulePriorities](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_SetRulePriorities.html): Sets the priorities of the specified rules.
- [SetSecurityGroups](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_SetSecurityGroups.html): Associates the specified security groups with the specified Application Load Balancer or Network Load Balancer.
- [SetSubnets](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_SetSubnets.html): Enables the Availability Zones for the specified public subnets for the specified Application Load Balancer, Network Load Balancer or Gateway Load Balancer.


## [Data Types](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_Types.html)

- [Action](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_Action.html): Information about an action.
- [AdministrativeOverride](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_AdministrativeOverride.html): Information about the override status applied to a target.
- [AnomalyDetection](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_AnomalyDetection.html): Information about anomaly detection and mitigation.
- [AuthenticateCognitoActionConfig](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_AuthenticateCognitoActionConfig.html): Request parameters to use when integrating with Amazon Cognito to authenticate users.
- [AuthenticateOidcActionConfig](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_AuthenticateOidcActionConfig.html): Request parameters when using an identity provider (IdP) that is compliant with OpenID Connect (OIDC) to authenticate users.
- [AvailabilityZone](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_AvailabilityZone.html): Information about an Availability Zone.
- [CapacityReservationStatus](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_CapacityReservationStatus.html): The status of a capacity reservation.
- [Certificate](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_Certificate.html): Information about an SSL server certificate.
- [Cipher](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_Cipher.html): Information about a cipher used in a policy.
- [DescribeTrustStoreRevocation](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_DescribeTrustStoreRevocation.html): Information about the revocations used by a trust store.
- [FixedResponseActionConfig](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_FixedResponseActionConfig.html): Information about an action that returns a custom HTTP response.
- [ForwardActionConfig](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_ForwardActionConfig.html): Information about a forward action.
- [HostHeaderConditionConfig](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_HostHeaderConditionConfig.html): Information about a host header condition.
- [HostHeaderRewriteConfig](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_HostHeaderRewriteConfig.html): Information about a host header rewrite transform.
- [HttpHeaderConditionConfig](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_HttpHeaderConditionConfig.html): Information about an HTTP header condition.
- [HttpRequestMethodConditionConfig](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_HttpRequestMethodConditionConfig.html): Information about an HTTP method condition.
- [IpamPools](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_IpamPools.html): An IPAM pool is a collection of IP address CIDRs.
- [JwtValidationActionAdditionalClaim](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_JwtValidationActionAdditionalClaim.html): Information about an additional claim to validate.
- [JwtValidationActionConfig](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_JwtValidationActionConfig.html): Information about a JSON Web Token (JWT) validation action.
- [Limit](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_Limit.html): Information about an Elastic Load Balancing resource limit for your AWS account.
- [Listener](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_Listener.html): Information about a listener.
- [ListenerAttribute](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_ListenerAttribute.html): Information about a listener attribute.
- [LoadBalancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_LoadBalancer.html): Information about a load balancer.
- [LoadBalancerAddress](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_LoadBalancerAddress.html): Information about a static IP address for a load balancer.
- [LoadBalancerAttribute](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_LoadBalancerAttribute.html): Information about a load balancer attribute.
- [LoadBalancerState](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_LoadBalancerState.html): Information about the state of the load balancer.
- [Matcher](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_Matcher.html): The codes to use when checking for a successful response from a target.
- [MinimumLoadBalancerCapacity](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_MinimumLoadBalancerCapacity.html): The minimum capacity for a load balancer.
- [MutualAuthenticationAttributes](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_MutualAuthenticationAttributes.html): Information about the mutual authentication attributes of a listener.
- [PathPatternConditionConfig](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_PathPatternConditionConfig.html): Information about a path pattern condition.
- [QueryStringConditionConfig](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_QueryStringConditionConfig.html): Information about a query string condition.
- [QueryStringKeyValuePair](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_QueryStringKeyValuePair.html): Information about a key/value pair.
- [RedirectActionConfig](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_RedirectActionConfig.html): Information about a redirect action.
- [RevocationContent](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_RevocationContent.html): Information about a revocation file.
- [RewriteConfig](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_RewriteConfig.html): Information about a rewrite transform.
- [Rule](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_Rule.html): Information about a rule.
- [RuleCondition](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_RuleCondition.html): Information about a condition for a rule.
- [RulePriorityPair](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_RulePriorityPair.html): Information about the priorities for the rules for a listener.
- [RuleTransform](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_RuleTransform.html): Information about a transform to apply to requests that match a rule.
- [SourceIpConditionConfig](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_SourceIpConditionConfig.html): Information about a source IP condition.
- [SslPolicy](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_SslPolicy.html): Information about a policy used for SSL negotiation.
- [SubnetMapping](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_SubnetMapping.html): Information about a subnet mapping.
- [Tag](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_Tag.html): Information about a tag.
- [TagDescription](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_TagDescription.html): The tags associated with a resource.
- [TargetDescription](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_TargetDescription.html): Information about a target.
- [TargetGroup](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_TargetGroup.html): Information about a target group.
- [TargetGroupAttribute](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_TargetGroupAttribute.html): Information about a target group attribute.
- [TargetGroupStickinessConfig](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_TargetGroupStickinessConfig.html): Information about the target group stickiness for a rule.
- [TargetGroupTuple](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_TargetGroupTuple.html): Information about how traffic will be distributed between multiple target groups in a forward rule.
- [TargetHealth](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_TargetHealth.html): Information about the current health of a target.
- [TargetHealthDescription](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_TargetHealthDescription.html): Information about the health of a target.
- [TrustStore](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_TrustStore.html): Information about a trust store.
- [TrustStoreAssociation](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_TrustStoreAssociation.html): Information about the resources a trust store is associated with.
- [TrustStoreRevocation](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_TrustStoreRevocation.html): Information about a revocation file in use by a trust store.
- [UrlRewriteConfig](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_UrlRewriteConfig.html): Information about a URL rewrite transform.
- [ZonalCapacityReservationState](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_ZonalCapacityReservationState.html): The capacity reservation status for each Availability Zone.
