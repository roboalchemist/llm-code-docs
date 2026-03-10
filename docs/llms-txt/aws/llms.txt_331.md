# Source: https://docs.aws.amazon.com/elasticloadbalancing/2012-06-01/APIReference/llms.txt

# Elastic Load Balancing API Reference

> A load balancer can distribute incoming traffic across your EC2 instances. This enables you to increase the availability of your application. The load balancer also monitors the health of its registered instances and ensures that it routes traffic only to healthy instances. You configure your load balancer to accept incoming traffic by specifying one or more listeners, which are configured with a protocol and port number for connections from clients to the load balancer and a protocol and port number for connections from the load balancer to the instances.

- [Welcome](https://docs.aws.amazon.com/elasticloadbalancing/2012-06-01/APIReference/Welcome.html)
- [Common Errors](https://docs.aws.amazon.com/elasticloadbalancing/2012-06-01/APIReference/CommonErrors.html)
- [Common Parameters](https://docs.aws.amazon.com/elasticloadbalancing/2012-06-01/APIReference/CommonParameters.html)
- [Query Requests](https://docs.aws.amazon.com/elasticloadbalancing/2012-06-01/APIReference/using-query-api.html)
- [SOAP API](https://docs.aws.amazon.com/elasticloadbalancing/2012-06-01/APIReference/using-soap-api.html)

## [Actions](https://docs.aws.amazon.com/elasticloadbalancing/2012-06-01/APIReference/API_Operations.html)

- [AddTags](https://docs.aws.amazon.com/elasticloadbalancing/2012-06-01/APIReference/API_AddTags.html): Adds the specified tags to the specified load balancer.
- [ApplySecurityGroupsToLoadBalancer](https://docs.aws.amazon.com/elasticloadbalancing/2012-06-01/APIReference/API_ApplySecurityGroupsToLoadBalancer.html): Associates one or more security groups with your load balancer in a virtual private cloud (VPC).
- [AttachLoadBalancerToSubnets](https://docs.aws.amazon.com/elasticloadbalancing/2012-06-01/APIReference/API_AttachLoadBalancerToSubnets.html): Adds one or more subnets to the set of configured subnets for the specified load balancer.
- [ConfigureHealthCheck](https://docs.aws.amazon.com/elasticloadbalancing/2012-06-01/APIReference/API_ConfigureHealthCheck.html): Specifies the health check settings to use when evaluating the health state of your EC2 instances.
- [CreateAppCookieStickinessPolicy](https://docs.aws.amazon.com/elasticloadbalancing/2012-06-01/APIReference/API_CreateAppCookieStickinessPolicy.html): Generates a stickiness policy with sticky session lifetimes that follow that of an application-generated cookie.
- [CreateLBCookieStickinessPolicy](https://docs.aws.amazon.com/elasticloadbalancing/2012-06-01/APIReference/API_CreateLBCookieStickinessPolicy.html): Generates a stickiness policy with sticky session lifetimes controlled by the lifetime of the browser (user-agent) or a specified expiration period.
- [CreateLoadBalancer](https://docs.aws.amazon.com/elasticloadbalancing/2012-06-01/APIReference/API_CreateLoadBalancer.html): Creates a Classic Load Balancer.
- [CreateLoadBalancerListeners](https://docs.aws.amazon.com/elasticloadbalancing/2012-06-01/APIReference/API_CreateLoadBalancerListeners.html): Creates one or more listeners for the specified load balancer.
- [CreateLoadBalancerPolicy](https://docs.aws.amazon.com/elasticloadbalancing/2012-06-01/APIReference/API_CreateLoadBalancerPolicy.html): Creates a policy with the specified attributes for the specified load balancer.
- [DeleteLoadBalancer](https://docs.aws.amazon.com/elasticloadbalancing/2012-06-01/APIReference/API_DeleteLoadBalancer.html): Deletes the specified load balancer.
- [DeleteLoadBalancerListeners](https://docs.aws.amazon.com/elasticloadbalancing/2012-06-01/APIReference/API_DeleteLoadBalancerListeners.html): Deletes the specified listeners from the specified load balancer.
- [DeleteLoadBalancerPolicy](https://docs.aws.amazon.com/elasticloadbalancing/2012-06-01/APIReference/API_DeleteLoadBalancerPolicy.html): Deletes the specified policy from the specified load balancer.
- [DeregisterInstancesFromLoadBalancer](https://docs.aws.amazon.com/elasticloadbalancing/2012-06-01/APIReference/API_DeregisterInstancesFromLoadBalancer.html): Deregisters the specified instances from the specified load balancer.
- [DescribeAccountLimits](https://docs.aws.amazon.com/elasticloadbalancing/2012-06-01/APIReference/API_DescribeAccountLimits.html): Describes the current Elastic Load Balancing resource limits for your AWS account.
- [DescribeInstanceHealth](https://docs.aws.amazon.com/elasticloadbalancing/2012-06-01/APIReference/API_DescribeInstanceHealth.html): Describes the state of the specified instances with respect to the specified load balancer.
- [DescribeLoadBalancerAttributes](https://docs.aws.amazon.com/elasticloadbalancing/2012-06-01/APIReference/API_DescribeLoadBalancerAttributes.html): Describes the attributes for the specified load balancer.
- [DescribeLoadBalancerPolicies](https://docs.aws.amazon.com/elasticloadbalancing/2012-06-01/APIReference/API_DescribeLoadBalancerPolicies.html): Describes the specified policies.
- [DescribeLoadBalancerPolicyTypes](https://docs.aws.amazon.com/elasticloadbalancing/2012-06-01/APIReference/API_DescribeLoadBalancerPolicyTypes.html): Describes the specified load balancer policy types or all load balancer policy types.
- [DescribeLoadBalancers](https://docs.aws.amazon.com/elasticloadbalancing/2012-06-01/APIReference/API_DescribeLoadBalancers.html): Describes the specified load balancers.
- [DescribeTags](https://docs.aws.amazon.com/elasticloadbalancing/2012-06-01/APIReference/API_DescribeTags.html): Describes the tags associated with the specified load balancers.
- [DetachLoadBalancerFromSubnets](https://docs.aws.amazon.com/elasticloadbalancing/2012-06-01/APIReference/API_DetachLoadBalancerFromSubnets.html): Removes the specified subnets from the set of configured subnets for the load balancer.
- [DisableAvailabilityZonesForLoadBalancer](https://docs.aws.amazon.com/elasticloadbalancing/2012-06-01/APIReference/API_DisableAvailabilityZonesForLoadBalancer.html): Removes the specified Availability Zones from the set of Availability Zones for the specified load balancer in EC2-Classic or a default VPC.
- [EnableAvailabilityZonesForLoadBalancer](https://docs.aws.amazon.com/elasticloadbalancing/2012-06-01/APIReference/API_EnableAvailabilityZonesForLoadBalancer.html): Adds the specified Availability Zones to the set of Availability Zones for the specified load balancer in EC2-Classic or a default VPC.
- [ModifyLoadBalancerAttributes](https://docs.aws.amazon.com/elasticloadbalancing/2012-06-01/APIReference/API_ModifyLoadBalancerAttributes.html): Modifies the attributes of the specified load balancer.
- [RegisterInstancesWithLoadBalancer](https://docs.aws.amazon.com/elasticloadbalancing/2012-06-01/APIReference/API_RegisterInstancesWithLoadBalancer.html): Adds the specified instances to the specified load balancer.
- [RemoveTags](https://docs.aws.amazon.com/elasticloadbalancing/2012-06-01/APIReference/API_RemoveTags.html): Removes one or more tags from the specified load balancer.
- [SetLoadBalancerListenerSSLCertificate](https://docs.aws.amazon.com/elasticloadbalancing/2012-06-01/APIReference/API_SetLoadBalancerListenerSSLCertificate.html): Sets the certificate that terminates the specified listener's SSL connections.
- [SetLoadBalancerPoliciesForBackendServer](https://docs.aws.amazon.com/elasticloadbalancing/2012-06-01/APIReference/API_SetLoadBalancerPoliciesForBackendServer.html): Replaces the set of policies associated with the specified port on which the EC2 instance is listening with a new set of policies.
- [SetLoadBalancerPoliciesOfListener](https://docs.aws.amazon.com/elasticloadbalancing/2012-06-01/APIReference/API_SetLoadBalancerPoliciesOfListener.html): Replaces the current set of policies for the specified load balancer port with the specified set of policies.


## [Data Types](https://docs.aws.amazon.com/elasticloadbalancing/2012-06-01/APIReference/API_Types.html)

- [AccessLog](https://docs.aws.amazon.com/elasticloadbalancing/2012-06-01/APIReference/API_AccessLog.html): Information about the AccessLog attribute.
- [AdditionalAttribute](https://docs.aws.amazon.com/elasticloadbalancing/2012-06-01/APIReference/API_AdditionalAttribute.html): Information about additional load balancer attributes.
- [AppCookieStickinessPolicy](https://docs.aws.amazon.com/elasticloadbalancing/2012-06-01/APIReference/API_AppCookieStickinessPolicy.html): Information about a policy for application-controlled session stickiness.
- [BackendServerDescription](https://docs.aws.amazon.com/elasticloadbalancing/2012-06-01/APIReference/API_BackendServerDescription.html): Information about the configuration of an EC2 instance.
- [ConnectionDraining](https://docs.aws.amazon.com/elasticloadbalancing/2012-06-01/APIReference/API_ConnectionDraining.html): Information about the ConnectionDraining attribute.
- [ConnectionSettings](https://docs.aws.amazon.com/elasticloadbalancing/2012-06-01/APIReference/API_ConnectionSettings.html): Information about the ConnectionSettings attribute.
- [CrossZoneLoadBalancing](https://docs.aws.amazon.com/elasticloadbalancing/2012-06-01/APIReference/API_CrossZoneLoadBalancing.html): Information about the CrossZoneLoadBalancing attribute.
- [HealthCheck](https://docs.aws.amazon.com/elasticloadbalancing/2012-06-01/APIReference/API_HealthCheck.html): Information about a health check.
- [Instance](https://docs.aws.amazon.com/elasticloadbalancing/2012-06-01/APIReference/API_Instance.html): The ID of an EC2 instance.
- [InstanceState](https://docs.aws.amazon.com/elasticloadbalancing/2012-06-01/APIReference/API_InstanceState.html): Information about the state of an EC2 instance.
- [LBCookieStickinessPolicy](https://docs.aws.amazon.com/elasticloadbalancing/2012-06-01/APIReference/API_LBCookieStickinessPolicy.html): Information about a policy for duration-based session stickiness.
- [Limit](https://docs.aws.amazon.com/elasticloadbalancing/2012-06-01/APIReference/API_Limit.html): Information about an Elastic Load Balancing resource limit for your AWS account.
- [Listener](https://docs.aws.amazon.com/elasticloadbalancing/2012-06-01/APIReference/API_Listener.html): Information about a listener.
- [ListenerDescription](https://docs.aws.amazon.com/elasticloadbalancing/2012-06-01/APIReference/API_ListenerDescription.html): The policies enabled for a listener.
- [LoadBalancerAttributes](https://docs.aws.amazon.com/elasticloadbalancing/2012-06-01/APIReference/API_LoadBalancerAttributes.html): The attributes for a load balancer.
- [LoadBalancerDescription](https://docs.aws.amazon.com/elasticloadbalancing/2012-06-01/APIReference/API_LoadBalancerDescription.html): Information about a load balancer.
- [Policies](https://docs.aws.amazon.com/elasticloadbalancing/2012-06-01/APIReference/API_Policies.html): The policies for a load balancer.
- [PolicyAttribute](https://docs.aws.amazon.com/elasticloadbalancing/2012-06-01/APIReference/API_PolicyAttribute.html): Information about a policy attribute.
- [PolicyAttributeDescription](https://docs.aws.amazon.com/elasticloadbalancing/2012-06-01/APIReference/API_PolicyAttributeDescription.html): Information about a policy attribute.
- [PolicyAttributeTypeDescription](https://docs.aws.amazon.com/elasticloadbalancing/2012-06-01/APIReference/API_PolicyAttributeTypeDescription.html): Information about a policy attribute type.
- [PolicyDescription](https://docs.aws.amazon.com/elasticloadbalancing/2012-06-01/APIReference/API_PolicyDescription.html): Information about a policy.
- [PolicyTypeDescription](https://docs.aws.amazon.com/elasticloadbalancing/2012-06-01/APIReference/API_PolicyTypeDescription.html): Information about a policy type.
- [SourceSecurityGroup](https://docs.aws.amazon.com/elasticloadbalancing/2012-06-01/APIReference/API_SourceSecurityGroup.html): Information about a source security group.
- [Tag](https://docs.aws.amazon.com/elasticloadbalancing/2012-06-01/APIReference/API_Tag.html): Information about a tag.
- [TagDescription](https://docs.aws.amazon.com/elasticloadbalancing/2012-06-01/APIReference/API_TagDescription.html): The tags associated with a load balancer.
- [TagKeyOnly](https://docs.aws.amazon.com/elasticloadbalancing/2012-06-01/APIReference/API_TagKeyOnly.html): The key of a tag.
