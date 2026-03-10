# Source: https://docs.aws.amazon.com/rtb-fabric/latest/api/llms.txt

# AWS RTB Fabric API Reference

> AWS RTB Fabric provides secure, low-latency infrastructure for connecting real-time bidding (RTB) applications. Rather than hosting applications directly, RTB Fabric acts as the connecting fabric that enables your applications to communicate efficiently over private networks instead of the public internet. You maintain complete control over your applications, data, and bidding decisions, while RTB Fabric provides the underlying infrastructure for secure, reliable connectivity.

- [Welcome](https://docs.aws.amazon.com/rtb-fabric/latest/api/Welcome.html)
- [Common Parameters](https://docs.aws.amazon.com/rtb-fabric/latest/api/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/rtb-fabric/latest/api/CommonErrors.html)

## [Actions](https://docs.aws.amazon.com/rtb-fabric/latest/api/API_Operations.html)

- [AcceptLink](https://docs.aws.amazon.com/rtb-fabric/latest/api/API_AcceptLink.html): Accepts a link request between gateways.
- [CreateInboundExternalLink](https://docs.aws.amazon.com/rtb-fabric/latest/api/API_CreateInboundExternalLink.html): Creates an inbound external link.
- [CreateLink](https://docs.aws.amazon.com/rtb-fabric/latest/api/API_CreateLink.html): Creates a new link between gateways.
- [CreateOutboundExternalLink](https://docs.aws.amazon.com/rtb-fabric/latest/api/API_CreateOutboundExternalLink.html): Creates an outbound external link.
- [CreateRequesterGateway](https://docs.aws.amazon.com/rtb-fabric/latest/api/API_CreateRequesterGateway.html): Creates a requester gateway.
- [CreateResponderGateway](https://docs.aws.amazon.com/rtb-fabric/latest/api/API_CreateResponderGateway.html): Creates a responder gateway.
- [DeleteInboundExternalLink](https://docs.aws.amazon.com/rtb-fabric/latest/api/API_DeleteInboundExternalLink.html): Deletes an inbound external link.
- [DeleteLink](https://docs.aws.amazon.com/rtb-fabric/latest/api/API_DeleteLink.html): Deletes a link between gateways.
- [DeleteOutboundExternalLink](https://docs.aws.amazon.com/rtb-fabric/latest/api/API_DeleteOutboundExternalLink.html): Deletes an outbound external link.
- [DeleteRequesterGateway](https://docs.aws.amazon.com/rtb-fabric/latest/api/API_DeleteRequesterGateway.html): Deletes a requester gateway.
- [DeleteResponderGateway](https://docs.aws.amazon.com/rtb-fabric/latest/api/API_DeleteResponderGateway.html): Deletes a responder gateway.
- [GetInboundExternalLink](https://docs.aws.amazon.com/rtb-fabric/latest/api/API_GetInboundExternalLink.html): Retrieves information about an inbound external link.
- [GetLink](https://docs.aws.amazon.com/rtb-fabric/latest/api/API_GetLink.html): Retrieves information about a link between gateways.
- [GetOutboundExternalLink](https://docs.aws.amazon.com/rtb-fabric/latest/api/API_GetOutboundExternalLink.html): Retrieves information about an outbound external link.
- [GetRequesterGateway](https://docs.aws.amazon.com/rtb-fabric/latest/api/API_GetRequesterGateway.html): Retrieves information about a requester gateway.
- [GetResponderGateway](https://docs.aws.amazon.com/rtb-fabric/latest/api/API_GetResponderGateway.html): Retrieves information about a responder gateway.
- [ListLinks](https://docs.aws.amazon.com/rtb-fabric/latest/api/API_ListLinks.html): Lists links associated with gateways.
- [ListRequesterGateways](https://docs.aws.amazon.com/rtb-fabric/latest/api/API_ListRequesterGateways.html): Lists requester gateways.
- [ListResponderGateways](https://docs.aws.amazon.com/rtb-fabric/latest/api/API_ListResponderGateways.html): Lists reponder gateways.
- [ListTagsForResource](https://docs.aws.amazon.com/rtb-fabric/latest/api/API_ListTagsForResource.html): Lists tags for a resource.
- [RejectLink](https://docs.aws.amazon.com/rtb-fabric/latest/api/API_RejectLink.html): Rejects a link request between gateways.
- [TagResource](https://docs.aws.amazon.com/rtb-fabric/latest/api/API_TagResource.html): Assigns one or more tags (key-value pairs) to the specified resource.
- [UntagResource](https://docs.aws.amazon.com/rtb-fabric/latest/api/API_UntagResource.html): Removes a tag or tags from a resource.
- [UpdateLink](https://docs.aws.amazon.com/rtb-fabric/latest/api/API_UpdateLink.html): Updates the configuration of a link between gateways.
- [UpdateLinkModuleFlow](https://docs.aws.amazon.com/rtb-fabric/latest/api/API_UpdateLinkModuleFlow.html): Updates a link module flow.
- [UpdateRequesterGateway](https://docs.aws.amazon.com/rtb-fabric/latest/api/API_UpdateRequesterGateway.html): Updates a requester gateway.
- [UpdateResponderGateway](https://docs.aws.amazon.com/rtb-fabric/latest/api/API_UpdateResponderGateway.html): Updates a responder gateway.


## [Data Types](https://docs.aws.amazon.com/rtb-fabric/latest/api/API_Types.html)

- [Action](https://docs.aws.amazon.com/rtb-fabric/latest/api/API_Action.html): Describes a bid action.
- [AutoScalingGroupsConfiguration](https://docs.aws.amazon.com/rtb-fabric/latest/api/API_AutoScalingGroupsConfiguration.html): Describes the configuration of an auto scaling group.
- [EksEndpointsConfiguration](https://docs.aws.amazon.com/rtb-fabric/latest/api/API_EksEndpointsConfiguration.html): Describes the configuration of an Amazon Elastic Kubernetes Service endpoint.
- [Filter](https://docs.aws.amazon.com/rtb-fabric/latest/api/API_Filter.html): Describes the configuration of a filter.
- [FilterCriterion](https://docs.aws.amazon.com/rtb-fabric/latest/api/API_FilterCriterion.html): Describes the criteria for a filter.
- [HeaderTagAction](https://docs.aws.amazon.com/rtb-fabric/latest/api/API_HeaderTagAction.html): Describes the header tag for a bid action.
- [LinkApplicationLogConfiguration](https://docs.aws.amazon.com/rtb-fabric/latest/api/API_LinkApplicationLogConfiguration.html): Describes the configuration of a link application log.
- [LinkApplicationLogSampling](https://docs.aws.amazon.com/rtb-fabric/latest/api/API_LinkApplicationLogSampling.html): Describes a link application log sample.
- [LinkAttributes](https://docs.aws.amazon.com/rtb-fabric/latest/api/API_LinkAttributes.html): Describes the attributes of a link.
- [LinkLogSettings](https://docs.aws.amazon.com/rtb-fabric/latest/api/API_LinkLogSettings.html): Describes the settings for a link log.
- [ListLinksResponseStructure](https://docs.aws.amazon.com/rtb-fabric/latest/api/API_ListLinksResponseStructure.html): Describes a link.
- [ManagedEndpointConfiguration](https://docs.aws.amazon.com/rtb-fabric/latest/api/API_ManagedEndpointConfiguration.html): Describes the configuration of a managed endpoint.
- [ModuleConfiguration](https://docs.aws.amazon.com/rtb-fabric/latest/api/API_ModuleConfiguration.html): Describes the configuration of a module.
- [ModuleParameters](https://docs.aws.amazon.com/rtb-fabric/latest/api/API_ModuleParameters.html): Describes the parameters of a module.
- [NoBidAction](https://docs.aws.amazon.com/rtb-fabric/latest/api/API_NoBidAction.html): Describes a no bid action.
- [NoBidModuleParameters](https://docs.aws.amazon.com/rtb-fabric/latest/api/API_NoBidModuleParameters.html): Describes the parameters of a no bid module.
- [OpenRtbAttributeModuleParameters](https://docs.aws.amazon.com/rtb-fabric/latest/api/API_OpenRtbAttributeModuleParameters.html): Describes the parameters of an open RTB attribute module.
- [RateLimiterModuleParameters](https://docs.aws.amazon.com/rtb-fabric/latest/api/API_RateLimiterModuleParameters.html): Describes the parameters of a rate limit.
- [ResponderErrorMaskingForHttpCode](https://docs.aws.amazon.com/rtb-fabric/latest/api/API_ResponderErrorMaskingForHttpCode.html): Describes the masking for HTTP error codes.
- [TrustStoreConfiguration](https://docs.aws.amazon.com/rtb-fabric/latest/api/API_TrustStoreConfiguration.html): Describes the configuration of a trust store.
