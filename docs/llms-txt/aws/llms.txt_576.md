# Source: https://docs.aws.amazon.com/mediatailor/latest/apireference/llms.txt

# AWS Elemental MediaTailor API Reference

> Use the AWS Elemental MediaTailor SDKs and CLI to configure scalable ad insertion and linear channels. With MediaTailor, you can assemble existing content into a linear stream and serve targeted ads to viewers while maintaining broadcast quality in over-the-top (OTT) video applications. For information about using the service, including detailed information about the settings covered in this guide, see the AWS Elemental MediaTailor User Guide.

- [Welcome](https://docs.aws.amazon.com/mediatailor/latest/apireference/Welcome.html)
- [Common Parameters](https://docs.aws.amazon.com/mediatailor/latest/apireference/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/mediatailor/latest/apireference/CommonErrors.html)

## [Actions](https://docs.aws.amazon.com/mediatailor/latest/apireference/API_Operations.html)

- [ConfigureLogsForChannel](https://docs.aws.amazon.com/mediatailor/latest/apireference/API_ConfigureLogsForChannel.html): Configures Amazon CloudWatch log settings for a channel.
- [ConfigureLogsForPlaybackConfiguration](https://docs.aws.amazon.com/mediatailor/latest/apireference/API_ConfigureLogsForPlaybackConfiguration.html): Defines where AWS Elemental MediaTailor sends logs for the playback configuration.
- [CreateChannel](https://docs.aws.amazon.com/mediatailor/latest/apireference/API_CreateChannel.html): Creates a channel.
- [CreateLiveSource](https://docs.aws.amazon.com/mediatailor/latest/apireference/API_CreateLiveSource.html): The live source configuration.
- [CreatePrefetchSchedule](https://docs.aws.amazon.com/mediatailor/latest/apireference/API_CreatePrefetchSchedule.html): Creates a prefetch schedule for a playback configuration.
- [CreateProgram](https://docs.aws.amazon.com/mediatailor/latest/apireference/API_CreateProgram.html): Creates a program within a channel.
- [CreateSourceLocation](https://docs.aws.amazon.com/mediatailor/latest/apireference/API_CreateSourceLocation.html): Creates a source location.
- [CreateVodSource](https://docs.aws.amazon.com/mediatailor/latest/apireference/API_CreateVodSource.html): The VOD source configuration parameters.
- [DeleteChannel](https://docs.aws.amazon.com/mediatailor/latest/apireference/API_DeleteChannel.html): Deletes a channel.
- [DeleteChannelPolicy](https://docs.aws.amazon.com/mediatailor/latest/apireference/API_DeleteChannelPolicy.html): The channel policy to delete.
- [DeleteLiveSource](https://docs.aws.amazon.com/mediatailor/latest/apireference/API_DeleteLiveSource.html): The live source to delete.
- [DeletePlaybackConfiguration](https://docs.aws.amazon.com/mediatailor/latest/apireference/API_DeletePlaybackConfiguration.html): Deletes a playback configuration.
- [DeletePrefetchSchedule](https://docs.aws.amazon.com/mediatailor/latest/apireference/API_DeletePrefetchSchedule.html): Deletes a prefetch schedule for a specific playback configuration.
- [DeleteProgram](https://docs.aws.amazon.com/mediatailor/latest/apireference/API_DeleteProgram.html): Deletes a program within a channel.
- [DeleteSourceLocation](https://docs.aws.amazon.com/mediatailor/latest/apireference/API_DeleteSourceLocation.html): Deletes a source location.
- [DeleteVodSource](https://docs.aws.amazon.com/mediatailor/latest/apireference/API_DeleteVodSource.html): The video on demand (VOD) source to delete.
- [DescribeChannel](https://docs.aws.amazon.com/mediatailor/latest/apireference/API_DescribeChannel.html): Describes a channel.
- [DescribeLiveSource](https://docs.aws.amazon.com/mediatailor/latest/apireference/API_DescribeLiveSource.html): The live source to describe.
- [DescribeProgram](https://docs.aws.amazon.com/mediatailor/latest/apireference/API_DescribeProgram.html): Describes a program within a channel.
- [DescribeSourceLocation](https://docs.aws.amazon.com/mediatailor/latest/apireference/API_DescribeSourceLocation.html): Describes a source location.
- [DescribeVodSource](https://docs.aws.amazon.com/mediatailor/latest/apireference/API_DescribeVodSource.html): Provides details about a specific video on demand (VOD) source in a specific source location.
- [GetChannelPolicy](https://docs.aws.amazon.com/mediatailor/latest/apireference/API_GetChannelPolicy.html): Returns the channel's IAM policy.
- [GetChannelSchedule](https://docs.aws.amazon.com/mediatailor/latest/apireference/API_GetChannelSchedule.html): Retrieves information about your channel's schedule.
- [GetPlaybackConfiguration](https://docs.aws.amazon.com/mediatailor/latest/apireference/API_GetPlaybackConfiguration.html): Retrieves a playback configuration.
- [GetPrefetchSchedule](https://docs.aws.amazon.com/mediatailor/latest/apireference/API_GetPrefetchSchedule.html): Retrieves a prefetch schedule for a playback configuration.
- [ListAlerts](https://docs.aws.amazon.com/mediatailor/latest/apireference/API_ListAlerts.html): Lists the alerts that are associated with a MediaTailor channel assembly resource.
- [ListChannels](https://docs.aws.amazon.com/mediatailor/latest/apireference/API_ListChannels.html): Retrieves information about the channels that are associated with the current AWS account.
- [ListLiveSources](https://docs.aws.amazon.com/mediatailor/latest/apireference/API_ListLiveSources.html): Lists the live sources contained in a source location.
- [ListPlaybackConfigurations](https://docs.aws.amazon.com/mediatailor/latest/apireference/API_ListPlaybackConfigurations.html): Retrieves existing playback configurations.
- [ListPrefetchSchedules](https://docs.aws.amazon.com/mediatailor/latest/apireference/API_ListPrefetchSchedules.html): Lists the prefetch schedules for a playback configuration.
- [ListSourceLocations](https://docs.aws.amazon.com/mediatailor/latest/apireference/API_ListSourceLocations.html): Lists the source locations for a channel.
- [ListTagsForResource](https://docs.aws.amazon.com/mediatailor/latest/apireference/API_ListTagsForResource.html): A list of tags that are associated with this resource.
- [ListVodSources](https://docs.aws.amazon.com/mediatailor/latest/apireference/API_ListVodSources.html): Lists the VOD sources contained in a source location.
- [PutChannelPolicy](https://docs.aws.amazon.com/mediatailor/latest/apireference/API_PutChannelPolicy.html): Creates an IAM policy for the channel.
- [PutPlaybackConfiguration](https://docs.aws.amazon.com/mediatailor/latest/apireference/API_PutPlaybackConfiguration.html): Creates a playback configuration.
- [StartChannel](https://docs.aws.amazon.com/mediatailor/latest/apireference/API_StartChannel.html): Starts a channel.
- [StopChannel](https://docs.aws.amazon.com/mediatailor/latest/apireference/API_StopChannel.html): Stops a channel.
- [TagResource](https://docs.aws.amazon.com/mediatailor/latest/apireference/API_TagResource.html): The resource to tag.
- [UntagResource](https://docs.aws.amazon.com/mediatailor/latest/apireference/API_UntagResource.html): The resource to untag.
- [UpdateChannel](https://docs.aws.amazon.com/mediatailor/latest/apireference/API_UpdateChannel.html): Updates a channel.
- [UpdateLiveSource](https://docs.aws.amazon.com/mediatailor/latest/apireference/API_UpdateLiveSource.html): Updates a live source's configuration.
- [UpdateProgram](https://docs.aws.amazon.com/mediatailor/latest/apireference/API_UpdateProgram.html): Updates a program within a channel.
- [UpdateSourceLocation](https://docs.aws.amazon.com/mediatailor/latest/apireference/API_UpdateSourceLocation.html): Updates a source location.
- [UpdateVodSource](https://docs.aws.amazon.com/mediatailor/latest/apireference/API_UpdateVodSource.html): Updates a VOD source's configuration.


## [Data Types](https://docs.aws.amazon.com/mediatailor/latest/apireference/API_Types.html)

- [AccessConfiguration](https://docs.aws.amazon.com/mediatailor/latest/apireference/API_AccessConfiguration.html): Access configuration parameters.
- [AdBreak](https://docs.aws.amazon.com/mediatailor/latest/apireference/API_AdBreak.html): Ad break configuration parameters.
- [AdBreakOpportunity](https://docs.aws.amazon.com/mediatailor/latest/apireference/API_AdBreakOpportunity.html): A location at which a zero-duration ad marker was detected in a VOD source manifest.
- [AdConditioningConfiguration](https://docs.aws.amazon.com/mediatailor/latest/apireference/API_AdConditioningConfiguration.html): The setting that indicates what conditioning MediaTailor will perform on ads that the ad decision server (ADS) returns.
- [AdMarkerPassthrough](https://docs.aws.amazon.com/mediatailor/latest/apireference/API_AdMarkerPassthrough.html): For HLS, when set to true, MediaTailor passes through EXT-X-CUE-IN, EXT-X-CUE-OUT, and EXT-X-SPLICEPOINT-SCTE35 ad markers from the origin manifest to the MediaTailor personalized manifest.
- [AdsInteractionLog](https://docs.aws.amazon.com/mediatailor/latest/apireference/API_AdsInteractionLog.html): Settings for customizing what events are included in logs for interactions with the ad decision server (ADS).
- [Alert](https://docs.aws.amazon.com/mediatailor/latest/apireference/API_Alert.html): Alert configuration parameters.
- [AlternateMedia](https://docs.aws.amazon.com/mediatailor/latest/apireference/API_AlternateMedia.html): A playlist of media (VOD and/or live) to be played instead of the default media on a particular program.
- [AudienceMedia](https://docs.aws.amazon.com/mediatailor/latest/apireference/API_AudienceMedia.html): An AudienceMedia object contains an Audience and a list of AlternateMedia.
- [AvailMatchingCriteria](https://docs.aws.amazon.com/mediatailor/latest/apireference/API_AvailMatchingCriteria.html): MediaTailor only places (consumes) prefetched ads if the ad break meets the criteria defined by the dynamic variables.
- [AvailSuppression](https://docs.aws.amazon.com/mediatailor/latest/apireference/API_AvailSuppression.html): The configuration for avail suppression, also known as ad suppression.
- [Bumper](https://docs.aws.amazon.com/mediatailor/latest/apireference/API_Bumper.html): The configuration for bumpers.
- [CdnConfiguration](https://docs.aws.amazon.com/mediatailor/latest/apireference/API_CdnConfiguration.html): The configuration for using a content delivery network (CDN), like Amazon CloudFront, for content and ad segment management.
- [Channel](https://docs.aws.amazon.com/mediatailor/latest/apireference/API_Channel.html): The configuration parameters for a channel.
- [ClipRange](https://docs.aws.amazon.com/mediatailor/latest/apireference/API_ClipRange.html): Clip range configuration for the VOD source associated with the program.
- [DashConfiguration](https://docs.aws.amazon.com/mediatailor/latest/apireference/API_DashConfiguration.html): The configuration for DASH content.
- [DashConfigurationForPut](https://docs.aws.amazon.com/mediatailor/latest/apireference/API_DashConfigurationForPut.html): The configuration for DASH PUT operations.
- [DashPlaylistSettings](https://docs.aws.amazon.com/mediatailor/latest/apireference/API_DashPlaylistSettings.html): Dash manifest configuration parameters.
- [DefaultSegmentDeliveryConfiguration](https://docs.aws.amazon.com/mediatailor/latest/apireference/API_DefaultSegmentDeliveryConfiguration.html): The optional configuration for a server that serves segments.
- [HlsConfiguration](https://docs.aws.amazon.com/mediatailor/latest/apireference/API_HlsConfiguration.html): The configuration for HLS content.
- [HlsPlaylistSettings](https://docs.aws.amazon.com/mediatailor/latest/apireference/API_HlsPlaylistSettings.html): HLS playlist configuration parameters.
- [HttpConfiguration](https://docs.aws.amazon.com/mediatailor/latest/apireference/API_HttpConfiguration.html): The HTTP configuration for the source location.
- [HttpPackageConfiguration](https://docs.aws.amazon.com/mediatailor/latest/apireference/API_HttpPackageConfiguration.html): The HTTP package configuration properties for the requested VOD source.
- [KeyValuePair](https://docs.aws.amazon.com/mediatailor/latest/apireference/API_KeyValuePair.html): For SCTE35_ENHANCED output, defines a key and corresponding value.
- [LivePreRollConfiguration](https://docs.aws.amazon.com/mediatailor/latest/apireference/API_LivePreRollConfiguration.html): The configuration for pre-roll ad insertion.
- [LiveSource](https://docs.aws.amazon.com/mediatailor/latest/apireference/API_LiveSource.html): Live source configuration parameters.
- [LogConfiguration](https://docs.aws.amazon.com/mediatailor/latest/apireference/API_LogConfiguration.html): Defines where AWS Elemental MediaTailor sends logs for the playback configuration.
- [LogConfigurationForChannel](https://docs.aws.amazon.com/mediatailor/latest/apireference/API_LogConfigurationForChannel.html): The log configuration for the channel.
- [ManifestProcessingRules](https://docs.aws.amazon.com/mediatailor/latest/apireference/API_ManifestProcessingRules.html): The configuration for manifest processing rules.
- [ManifestServiceInteractionLog](https://docs.aws.amazon.com/mediatailor/latest/apireference/API_ManifestServiceInteractionLog.html): Settings for customizing what events are included in logs for interactions with the origin server.
- [PlaybackConfiguration](https://docs.aws.amazon.com/mediatailor/latest/apireference/API_PlaybackConfiguration.html): A playback configuration.
- [PrefetchConsumption](https://docs.aws.amazon.com/mediatailor/latest/apireference/API_PrefetchConsumption.html): For single prefetch, describes how and when that MediaTailor places prefetched ads into upcoming ad breaks.
- [PrefetchRetrieval](https://docs.aws.amazon.com/mediatailor/latest/apireference/API_PrefetchRetrieval.html): A complex type that contains settings governing when MediaTailor prefetches ads, and which dynamic variables that MediaTailor includes in the request to the ad decision server.
- [PrefetchSchedule](https://docs.aws.amazon.com/mediatailor/latest/apireference/API_PrefetchSchedule.html): A prefetch schedule allows you to tell MediaTailor to fetch and prepare certain ads before an ad break happens.
- [RecurringConsumption](https://docs.aws.amazon.com/mediatailor/latest/apireference/API_RecurringConsumption.html): The settings that determine how and when MediaTailor places prefetched ads into upcoming ad breaks for recurring prefetch scedules.
- [RecurringPrefetchConfiguration](https://docs.aws.amazon.com/mediatailor/latest/apireference/API_RecurringPrefetchConfiguration.html): The configuration that defines how MediaTailor performs recurring prefetch.
- [RecurringRetrieval](https://docs.aws.amazon.com/mediatailor/latest/apireference/API_RecurringRetrieval.html): With recurring prefetch, MediaTailor automatically prefetches ads for every avail that occurs during the retrieval window.
- [RequestOutputItem](https://docs.aws.amazon.com/mediatailor/latest/apireference/API_RequestOutputItem.html): The output configuration for this channel.
- [ResponseOutputItem](https://docs.aws.amazon.com/mediatailor/latest/apireference/API_ResponseOutputItem.html): The output item response.
- [ScheduleAdBreak](https://docs.aws.amazon.com/mediatailor/latest/apireference/API_ScheduleAdBreak.html): The schedule's ad break properties.
- [ScheduleConfiguration](https://docs.aws.amazon.com/mediatailor/latest/apireference/API_ScheduleConfiguration.html): Schedule configuration parameters.
- [ScheduleEntry](https://docs.aws.amazon.com/mediatailor/latest/apireference/API_ScheduleEntry.html): The properties for a schedule.
- [SecretsManagerAccessTokenConfiguration](https://docs.aws.amazon.com/mediatailor/latest/apireference/API_SecretsManagerAccessTokenConfiguration.html): AWS Secrets Manager access token configuration parameters.
- [SegmentationDescriptor](https://docs.aws.amazon.com/mediatailor/latest/apireference/API_SegmentationDescriptor.html): The segmentation_descriptor message can contain advanced metadata fields, like content identifiers, to convey a wide range of information about the ad break.
- [SegmentDeliveryConfiguration](https://docs.aws.amazon.com/mediatailor/latest/apireference/API_SegmentDeliveryConfiguration.html): The segment delivery configuration settings.
- [SlateSource](https://docs.aws.amazon.com/mediatailor/latest/apireference/API_SlateSource.html): Slate VOD source configuration.
- [SourceLocation](https://docs.aws.amazon.com/mediatailor/latest/apireference/API_SourceLocation.html): A source location is a container for sources.
- [SpliceInsertMessage](https://docs.aws.amazon.com/mediatailor/latest/apireference/API_SpliceInsertMessage.html): Splice insert message configuration.
- [TimeShiftConfiguration](https://docs.aws.amazon.com/mediatailor/latest/apireference/API_TimeShiftConfiguration.html): The configuration for time-shifted viewing.
- [TimeSignalMessage](https://docs.aws.amazon.com/mediatailor/latest/apireference/API_TimeSignalMessage.html): The SCTE-35 time_signal message can be sent with one or more segmentation_descriptor messages.
- [TrafficShapingRetrievalWindow](https://docs.aws.amazon.com/mediatailor/latest/apireference/API_TrafficShapingRetrievalWindow.html): The configuration that tells AWS Elemental MediaTailor how to spread out requests to the ad decision server (ADS).
- [Transition](https://docs.aws.amazon.com/mediatailor/latest/apireference/API_Transition.html): Program transition configuration.
- [UpdateProgramScheduleConfiguration](https://docs.aws.amazon.com/mediatailor/latest/apireference/API_UpdateProgramScheduleConfiguration.html): Schedule configuration parameters.
- [UpdateProgramTransition](https://docs.aws.amazon.com/mediatailor/latest/apireference/API_UpdateProgramTransition.html): Program transition configuration.
- [VodSource](https://docs.aws.amazon.com/mediatailor/latest/apireference/API_VodSource.html): VOD source configuration parameters.
