# Source: https://docs.aws.amazon.com/connect-outbound/latest/APIReference/llms.txt

# Amazon Connect Outbound Campaigns API Reference

> With the outbound campaigns feature of Amazon Connect, you can create high-volume outbound campaigns. For example, you can use this feature for appointment reminders, telemarketing, subscription renewals, or debt collection. For more information, see Set up outbound communications in the Amazon Connect Administrator Guide.

- [Welcome](https://docs.aws.amazon.com/connect-outbound/latest/APIReference/Welcome.html)
- [Best practices for using PutDialRequestBatch](https://docs.aws.amazon.com/connect-outbound/latest/APIReference/api-outbound-campaign-calls.html)
- [Common Parameters](https://docs.aws.amazon.com/connect-outbound/latest/APIReference/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/connect-outbound/latest/APIReference/CommonErrors.html)

## [Actions](https://docs.aws.amazon.com/connect-outbound/latest/APIReference/API_Operations.html)

- [CreateCampaign](https://docs.aws.amazon.com/connect-outbound/latest/APIReference/API_CreateCampaign.html): Creates an outbound campaign.
- [DeleteCampaign](https://docs.aws.amazon.com/connect-outbound/latest/APIReference/API_DeleteCampaign.html): Deletes an outbound campaign.
- [DeleteConnectInstanceConfig](https://docs.aws.amazon.com/connect-outbound/latest/APIReference/API_DeleteConnectInstanceConfig.html): Deletes configuration information for an Amazon Connect instance.
- [DeleteInstanceOnboardingJob](https://docs.aws.amazon.com/connect-outbound/latest/APIReference/API_DeleteInstanceOnboardingJob.html): Deletes the workflow to onboard to outbound campaigns.
- [DescribeCampaign](https://docs.aws.amazon.com/connect-outbound/latest/APIReference/API_DescribeCampaign.html): Describes an outbound campaign.
- [GetCampaignState](https://docs.aws.amazon.com/connect-outbound/latest/APIReference/API_GetCampaignState.html): Returns the state of an outbound campaign.
- [GetCampaignStateBatch](https://docs.aws.amazon.com/connect-outbound/latest/APIReference/API_GetCampaignStateBatch.html): Returns the state of listed of outbound campaigns.
- [GetConnectInstanceConfig](https://docs.aws.amazon.com/connect-outbound/latest/APIReference/API_GetConnectInstanceConfig.html): Get configuration information about an Amazon Connect instance.
- [GetInstanceOnboardingJobStatus](https://docs.aws.amazon.com/connect-outbound/latest/APIReference/API_GetInstanceOnboardingJobStatus.html): Gets the status of the workflow to onboard to outbound campaigns.
- [ListCampaigns](https://docs.aws.amazon.com/connect-outbound/latest/APIReference/API_ListCampaigns.html): Lists outbound campaigns.
- [ListTagsForResource](https://docs.aws.amazon.com/connect-outbound/latest/APIReference/API_ListTagsForResource.html): Lists tags for a resource.
- [PauseCampaign](https://docs.aws.amazon.com/connect-outbound/latest/APIReference/API_PauseCampaign.html): Pauses an outbound campaign.
- [PutDialRequestBatch](https://docs.aws.amazon.com/connect-outbound/latest/APIReference/API_PutDialRequestBatch.html): Takes in a list of DialRequests to be dialed as part of an outbound campaign.
- [ResumeCampaign](https://docs.aws.amazon.com/connect-outbound/latest/APIReference/API_ResumeCampaign.html): Resumes an outbound campaign.
- [StartCampaign](https://docs.aws.amazon.com/connect-outbound/latest/APIReference/API_StartCampaign.html): Starts an outbound campaign.
- [StartInstanceOnboardingJob](https://docs.aws.amazon.com/connect-outbound/latest/APIReference/API_StartInstanceOnboardingJob.html): Starts the workflow to onboard an Amazon Connect instance to outbound campaigns.
- [StopCampaign](https://docs.aws.amazon.com/connect-outbound/latest/APIReference/API_StopCampaign.html): Stops an Amazon Connect campaign.
- [TagResource](https://docs.aws.amazon.com/connect-outbound/latest/APIReference/API_TagResource.html): Adds the specified tags to a resource.
- [UntagResource](https://docs.aws.amazon.com/connect-outbound/latest/APIReference/API_UntagResource.html): Removes the specified tags from the specified resource.
- [UpdateCampaignDialerConfig](https://docs.aws.amazon.com/connect-outbound/latest/APIReference/API_UpdateCampaignDialerConfig.html): Updates DialerConfig for an outbound campaign.
- [UpdateCampaignName](https://docs.aws.amazon.com/connect-outbound/latest/APIReference/API_UpdateCampaignName.html): Updates the name of an outbound campaign.
- [UpdateCampaignOutboundCallConfig](https://docs.aws.amazon.com/connect-outbound/latest/APIReference/API_UpdateCampaignOutboundCallConfig.html): Updates OutboundCallConfig for an outbound campaign.


## [Data Types](https://docs.aws.amazon.com/connect-outbound/latest/APIReference/API_Types.html)

- [AgentlessDialerConfig](https://docs.aws.amazon.com/connect-outbound/latest/APIReference/API_AgentlessDialerConfig.html): Contains agentless dialer configuration for an outbound campaign.
- [AnswerMachineDetectionConfig](https://docs.aws.amazon.com/connect-outbound/latest/APIReference/API_AnswerMachineDetectionConfig.html): Contains information about answering machine detection.
- [Campaign](https://docs.aws.amazon.com/connect-outbound/latest/APIReference/API_Campaign.html): Contains information about an outbound campaign.
- [CampaignFilters](https://docs.aws.amazon.com/connect-outbound/latest/APIReference/API_CampaignFilters.html): Contains the filters to apply when retrieving campaigns.
- [CampaignSummary](https://docs.aws.amazon.com/connect-outbound/latest/APIReference/API_CampaignSummary.html): Contains summary information about an outbound campaign.
- [DialerConfig](https://docs.aws.amazon.com/connect-outbound/latest/APIReference/API_DialerConfig.html): Contains dialer configuration for an outbound campaign.
- [DialRequest](https://docs.aws.amazon.com/connect-outbound/latest/APIReference/API_DialRequest.html): Contains information about a dial request.
- [EncryptionConfig](https://docs.aws.amazon.com/connect-outbound/latest/APIReference/API_EncryptionConfig.html): Contains encryption configuration for an Amazon Connect instance.
- [FailedCampaignStateResponse](https://docs.aws.amazon.com/connect-outbound/latest/APIReference/API_FailedCampaignStateResponse.html): Contains information about a failed campaign.
- [FailedRequest](https://docs.aws.amazon.com/connect-outbound/latest/APIReference/API_FailedRequest.html): Failure details for a DialRequest.
- [InstanceConfig](https://docs.aws.amazon.com/connect-outbound/latest/APIReference/API_InstanceConfig.html): Contains configuration information about the Amazon Connect instance.
- [InstanceIdFilter](https://docs.aws.amazon.com/connect-outbound/latest/APIReference/API_InstanceIdFilter.html): Contains the filter to apply when retrieving outbound campaigns.
- [InstanceOnboardingJobStatus](https://docs.aws.amazon.com/connect-outbound/latest/APIReference/API_InstanceOnboardingJobStatus.html): Contains information about the status of the workflow to onboard to outbound campaigns.
- [OutboundCallConfig](https://docs.aws.amazon.com/connect-outbound/latest/APIReference/API_OutboundCallConfig.html): Contains outbound call configuration for an outbound campaign.
- [PredictiveDialerConfig](https://docs.aws.amazon.com/connect-outbound/latest/APIReference/API_PredictiveDialerConfig.html): Contains predictive dialer configuration for an outbound campaign.
- [ProgressiveDialerConfig](https://docs.aws.amazon.com/connect-outbound/latest/APIReference/API_ProgressiveDialerConfig.html): Contains progressive dialer configuration for an outbound campaign.
- [SuccessfulCampaignStateResponse](https://docs.aws.amazon.com/connect-outbound/latest/APIReference/API_SuccessfulCampaignStateResponse.html): The state response when the campaign is successful.
- [SuccessfulRequest](https://docs.aws.amazon.com/connect-outbound/latest/APIReference/API_SuccessfulRequest.html): Success details for a DialRequest.
