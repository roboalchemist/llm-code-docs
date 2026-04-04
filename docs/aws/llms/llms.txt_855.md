# Source: https://docs.aws.amazon.com/waf/latest/DDOSAPIReference/llms.txt

# AWS Shield Advanced AWS Shield Advanced API Reference

> This is the AWS Shield Advanced API Reference. This guide is for developers who need detailed information about the AWS Shield Advanced API actions, data types, and errors. For detailed information about AWS WAF and AWS Shield Advanced features and an overview of how to use the AWS WAF and AWS Shield Advanced APIs, see the AWS WAF and AWS Shield Developer Guide.

- [Welcome](https://docs.aws.amazon.com/waf/latest/DDOSAPIReference/Welcome.html)
- [Common Parameters](https://docs.aws.amazon.com/waf/latest/DDOSAPIReference/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/waf/latest/DDOSAPIReference/CommonErrors.html)

## [Actions](https://docs.aws.amazon.com/waf/latest/DDOSAPIReference/API_Operations.html)

- [AssociateDRTLogBucket](https://docs.aws.amazon.com/waf/latest/DDOSAPIReference/API_AssociateDRTLogBucket.html): Authorizes the Shield Response Team (SRT) to access the specified Amazon S3 bucket containing log data such as Application Load Balancer access logs, CloudFront logs, or logs from third party sources.
- [AssociateDRTRole](https://docs.aws.amazon.com/waf/latest/DDOSAPIReference/API_AssociateDRTRole.html): Authorizes the Shield Response Team (SRT) using the specified role, to access your AWS account to assist with DDoS attack mitigation during potential attacks.
- [AssociateHealthCheck](https://docs.aws.amazon.com/waf/latest/DDOSAPIReference/API_AssociateHealthCheck.html): Adds health-based detection to the Shield Advanced protection for a resource.
- [AssociateProactiveEngagementDetails](https://docs.aws.amazon.com/waf/latest/DDOSAPIReference/API_AssociateProactiveEngagementDetails.html): Initializes proactive engagement and sets the list of contacts for the Shield Response Team (SRT) to use.
- [CreateProtection](https://docs.aws.amazon.com/waf/latest/DDOSAPIReference/API_CreateProtection.html): Enables AWS Shield Advanced for a specific AWS resource.
- [CreateProtectionGroup](https://docs.aws.amazon.com/waf/latest/DDOSAPIReference/API_CreateProtectionGroup.html): Creates a grouping of protected resources so they can be handled as a collective.
- [CreateSubscription](https://docs.aws.amazon.com/waf/latest/DDOSAPIReference/API_CreateSubscription.html): Activates AWS Shield Advanced for an account.
- [DeleteProtection](https://docs.aws.amazon.com/waf/latest/DDOSAPIReference/API_DeleteProtection.html): Deletes an AWS Shield Advanced .
- [DeleteProtectionGroup](https://docs.aws.amazon.com/waf/latest/DDOSAPIReference/API_DeleteProtectionGroup.html): Removes the specified protection group.
- [DeleteSubscription](https://docs.aws.amazon.com/waf/latest/DDOSAPIReference/API_DeleteSubscription.html): This action has been deprecated.
- [DescribeAttack](https://docs.aws.amazon.com/waf/latest/DDOSAPIReference/API_DescribeAttack.html): Describes the details of a DDoS attack.
- [DescribeAttackStatistics](https://docs.aws.amazon.com/waf/latest/DDOSAPIReference/API_DescribeAttackStatistics.html): Provides information about the number and type of attacks AWS Shield has detected in the last year for all resources that belong to your account, regardless of whether you've defined Shield protections for them.
- [DescribeDRTAccess](https://docs.aws.amazon.com/waf/latest/DDOSAPIReference/API_DescribeDRTAccess.html): Returns the current role and list of Amazon S3 log buckets used by the Shield Response Team (SRT) to access your AWS account while assisting with attack mitigation.
- [DescribeEmergencyContactSettings](https://docs.aws.amazon.com/waf/latest/DDOSAPIReference/API_DescribeEmergencyContactSettings.html): A list of email addresses and phone numbers that the Shield Response Team (SRT) can use to contact you if you have proactive engagement enabled, for escalations to the SRT and to initiate proactive customer support.
- [DescribeProtection](https://docs.aws.amazon.com/waf/latest/DDOSAPIReference/API_DescribeProtection.html): Lists the details of a object.
- [DescribeProtectionGroup](https://docs.aws.amazon.com/waf/latest/DDOSAPIReference/API_DescribeProtectionGroup.html): Returns the specification for the specified protection group.
- [DescribeSubscription](https://docs.aws.amazon.com/waf/latest/DDOSAPIReference/API_DescribeSubscription.html): Provides details about the AWS Shield Advanced subscription for an account.
- [DisableApplicationLayerAutomaticResponse](https://docs.aws.amazon.com/waf/latest/DDOSAPIReference/API_DisableApplicationLayerAutomaticResponse.html): Disable the Shield Advanced automatic application layer DDoS mitigation feature for the protected resource.
- [DisableProactiveEngagement](https://docs.aws.amazon.com/waf/latest/DDOSAPIReference/API_DisableProactiveEngagement.html): Removes authorization from the Shield Response Team (SRT) to notify contacts about escalations to the SRT and to initiate proactive customer support.
- [DisassociateDRTLogBucket](https://docs.aws.amazon.com/waf/latest/DDOSAPIReference/API_DisassociateDRTLogBucket.html): Removes the Shield Response Team's (SRT) access to the specified Amazon S3 bucket containing the logs that you shared previously.
- [DisassociateDRTRole](https://docs.aws.amazon.com/waf/latest/DDOSAPIReference/API_DisassociateDRTRole.html): Removes the Shield Response Team's (SRT) access to your AWS account.
- [DisassociateHealthCheck](https://docs.aws.amazon.com/waf/latest/DDOSAPIReference/API_DisassociateHealthCheck.html): Removes health-based detection from the Shield Advanced protection for a resource.
- [EnableApplicationLayerAutomaticResponse](https://docs.aws.amazon.com/waf/latest/DDOSAPIReference/API_EnableApplicationLayerAutomaticResponse.html): Enable the Shield Advanced automatic application layer DDoS mitigation for the protected resource.
- [EnableProactiveEngagement](https://docs.aws.amazon.com/waf/latest/DDOSAPIReference/API_EnableProactiveEngagement.html): Authorizes the Shield Response Team (SRT) to use email and phone to notify contacts about escalations to the SRT and to initiate proactive customer support.
- [GetSubscriptionState](https://docs.aws.amazon.com/waf/latest/DDOSAPIReference/API_GetSubscriptionState.html): Returns the SubscriptionState, either Active or Inactive.
- [ListAttacks](https://docs.aws.amazon.com/waf/latest/DDOSAPIReference/API_ListAttacks.html): Returns all ongoing DDoS attacks or all DDoS attacks during a specified time period.
- [ListProtectionGroups](https://docs.aws.amazon.com/waf/latest/DDOSAPIReference/API_ListProtectionGroups.html): Retrieves objects for the account.
- [ListProtections](https://docs.aws.amazon.com/waf/latest/DDOSAPIReference/API_ListProtections.html): Retrieves objects for the account.
- [ListResourcesInProtectionGroup](https://docs.aws.amazon.com/waf/latest/DDOSAPIReference/API_ListResourcesInProtectionGroup.html): Retrieves the resources that are included in the protection group.
- [ListTagsForResource](https://docs.aws.amazon.com/waf/latest/DDOSAPIReference/API_ListTagsForResource.html): Gets information about AWS tags for a specified Amazon Resource Name (ARN) in AWS Shield.
- [TagResource](https://docs.aws.amazon.com/waf/latest/DDOSAPIReference/API_TagResource.html): Adds or updates tags for a resource in AWS Shield.
- [UntagResource](https://docs.aws.amazon.com/waf/latest/DDOSAPIReference/API_UntagResource.html): Removes tags from a resource in AWS Shield.
- [UpdateApplicationLayerAutomaticResponse](https://docs.aws.amazon.com/waf/latest/DDOSAPIReference/API_UpdateApplicationLayerAutomaticResponse.html): Updates an existing Shield Advanced automatic application layer DDoS mitigation configuration for the specified resource.
- [UpdateEmergencyContactSettings](https://docs.aws.amazon.com/waf/latest/DDOSAPIReference/API_UpdateEmergencyContactSettings.html): Updates the details of the list of email addresses and phone numbers that the Shield Response Team (SRT) can use to contact you if you have proactive engagement enabled, for escalations to the SRT and to initiate proactive customer support.
- [UpdateProtectionGroup](https://docs.aws.amazon.com/waf/latest/DDOSAPIReference/API_UpdateProtectionGroup.html): Updates an existing protection group.
- [UpdateSubscription](https://docs.aws.amazon.com/waf/latest/DDOSAPIReference/API_UpdateSubscription.html): Updates the details of an existing subscription.


## [Data Types](https://docs.aws.amazon.com/waf/latest/DDOSAPIReference/API_Types.html)

- [ApplicationLayerAutomaticResponseConfiguration](https://docs.aws.amazon.com/waf/latest/DDOSAPIReference/API_ApplicationLayerAutomaticResponseConfiguration.html): The automatic application layer DDoS mitigation settings for a .
- [AttackDetail](https://docs.aws.amazon.com/waf/latest/DDOSAPIReference/API_AttackDetail.html): The details of a DDoS attack.
- [AttackProperty](https://docs.aws.amazon.com/waf/latest/DDOSAPIReference/API_AttackProperty.html): Details of a AWS Shield event.
- [AttackStatisticsDataItem](https://docs.aws.amazon.com/waf/latest/DDOSAPIReference/API_AttackStatisticsDataItem.html): A single attack statistics data record.
- [AttackSummary](https://docs.aws.amazon.com/waf/latest/DDOSAPIReference/API_AttackSummary.html): Summarizes all DDoS attacks for a specified time period.
- [AttackVectorDescription](https://docs.aws.amazon.com/waf/latest/DDOSAPIReference/API_AttackVectorDescription.html): Describes the attack.
- [AttackVolume](https://docs.aws.amazon.com/waf/latest/DDOSAPIReference/API_AttackVolume.html): Information about the volume of attacks during the time period, included in an .
- [AttackVolumeStatistics](https://docs.aws.amazon.com/waf/latest/DDOSAPIReference/API_AttackVolumeStatistics.html): Statistics objects for the various data types in .
- [BlockAction](https://docs.aws.amazon.com/waf/latest/DDOSAPIReference/API_BlockAction.html): Specifies that Shield Advanced should configure its AWS WAF rules with the AWS WAF Block action.
- [Contributor](https://docs.aws.amazon.com/waf/latest/DDOSAPIReference/API_Contributor.html): A contributor to the attack and their contribution.
- [CountAction](https://docs.aws.amazon.com/waf/latest/DDOSAPIReference/API_CountAction.html): Specifies that Shield Advanced should configure its AWS WAF rules with the AWS WAF Count action.
- [EmergencyContact](https://docs.aws.amazon.com/waf/latest/DDOSAPIReference/API_EmergencyContact.html): Contact information that the SRT can use to contact you if you have proactive engagement enabled, for escalations to the SRT and to initiate proactive customer support.
- [InclusionProtectionFilters](https://docs.aws.amazon.com/waf/latest/DDOSAPIReference/API_InclusionProtectionFilters.html): Narrows the set of protections that the call retrieves.
- [InclusionProtectionGroupFilters](https://docs.aws.amazon.com/waf/latest/DDOSAPIReference/API_InclusionProtectionGroupFilters.html): Narrows the set of protection groups that the call retrieves.
- [Limit](https://docs.aws.amazon.com/waf/latest/DDOSAPIReference/API_Limit.html): Specifies how many protections of a given type you can create.
- [Mitigation](https://docs.aws.amazon.com/waf/latest/DDOSAPIReference/API_Mitigation.html): The mitigation applied to a DDoS attack.
- [Protection](https://docs.aws.amazon.com/waf/latest/DDOSAPIReference/API_Protection.html): An object that represents a resource that is under DDoS protection.
- [ProtectionGroup](https://docs.aws.amazon.com/waf/latest/DDOSAPIReference/API_ProtectionGroup.html): A grouping of protected resources that you and AWS Shield Advanced can monitor as a collective.
- [ProtectionGroupArbitraryPatternLimits](https://docs.aws.amazon.com/waf/latest/DDOSAPIReference/API_ProtectionGroupArbitraryPatternLimits.html): Limits settings on protection groups with arbitrary pattern type.
- [ProtectionGroupLimits](https://docs.aws.amazon.com/waf/latest/DDOSAPIReference/API_ProtectionGroupLimits.html): Limits settings on protection groups for your subscription.
- [ProtectionGroupPatternTypeLimits](https://docs.aws.amazon.com/waf/latest/DDOSAPIReference/API_ProtectionGroupPatternTypeLimits.html): Limits settings by pattern type in the protection groups for your subscription.
- [ProtectionLimits](https://docs.aws.amazon.com/waf/latest/DDOSAPIReference/API_ProtectionLimits.html): Limits settings on protections for your subscription.
- [ResponseAction](https://docs.aws.amazon.com/waf/latest/DDOSAPIReference/API_ResponseAction.html): Specifies the action setting that Shield Advanced should use in the AWS WAF rules that it creates on behalf of the protected resource in response to DDoS attacks.
- [SubResourceSummary](https://docs.aws.amazon.com/waf/latest/DDOSAPIReference/API_SubResourceSummary.html): The attack information for the specified SubResource.
- [Subscription](https://docs.aws.amazon.com/waf/latest/DDOSAPIReference/API_Subscription.html): Information about the AWS Shield Advanced subscription for an account.
- [SubscriptionLimits](https://docs.aws.amazon.com/waf/latest/DDOSAPIReference/API_SubscriptionLimits.html): Limits settings for your subscription.
- [SummarizedAttackVector](https://docs.aws.amazon.com/waf/latest/DDOSAPIReference/API_SummarizedAttackVector.html): A summary of information about the attack.
- [SummarizedCounter](https://docs.aws.amazon.com/waf/latest/DDOSAPIReference/API_SummarizedCounter.html): The counter that describes a DDoS attack.
- [Tag](https://docs.aws.amazon.com/waf/latest/DDOSAPIReference/API_Tag.html): A tag associated with an AWS resource.
- [TimeRange](https://docs.aws.amazon.com/waf/latest/DDOSAPIReference/API_TimeRange.html): The time range.
- [ValidationExceptionField](https://docs.aws.amazon.com/waf/latest/DDOSAPIReference/API_ValidationExceptionField.html): Provides information about a particular parameter passed inside a request that resulted in an exception.
