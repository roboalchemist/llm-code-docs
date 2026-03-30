# Source: https://docs.aws.amazon.com/mediapackage/latest/APIReference/llms.txt

# AWS Elemental MediaPackage V2 Live API Live API Reference

> This is the AWS Elemental MediaPackage v2 Live REST API Reference. It describes all the MediaPackage API operations for live content in detail, and provides sample requests, responses, and errors for the supported web services protocols.

- [Welcome](https://docs.aws.amazon.com/mediapackage/latest/APIReference/Welcome.html)
- [Common Parameters](https://docs.aws.amazon.com/mediapackage/latest/APIReference/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/mediapackage/latest/APIReference/CommonErrors.html)

## [Actions](https://docs.aws.amazon.com/mediapackage/latest/APIReference/API_Operations.html)

- [CancelHarvestJob](https://docs.aws.amazon.com/mediapackage/latest/APIReference/API_CancelHarvestJob.html): Cancels an in-progress harvest job.
- [CreateChannel](https://docs.aws.amazon.com/mediapackage/latest/APIReference/API_CreateChannel.html): Create a channel to start receiving content streams.
- [CreateChannelGroup](https://docs.aws.amazon.com/mediapackage/latest/APIReference/API_CreateChannelGroup.html): Create a channel group to group your channels and origin endpoints.
- [CreateHarvestJob](https://docs.aws.amazon.com/mediapackage/latest/APIReference/API_CreateHarvestJob.html): Creates a new harvest job to export content from a MediaPackage v2 channel to an S3 bucket.
- [CreateOriginEndpoint](https://docs.aws.amazon.com/mediapackage/latest/APIReference/API_CreateOriginEndpoint.html): The endpoint is attached to a channel, and represents the output of the live content.
- [DeleteChannel](https://docs.aws.amazon.com/mediapackage/latest/APIReference/API_DeleteChannel.html): Delete a channel to stop AWS Elemental MediaPackage from receiving further content.
- [DeleteChannelGroup](https://docs.aws.amazon.com/mediapackage/latest/APIReference/API_DeleteChannelGroup.html): Delete a channel group.
- [DeleteChannelPolicy](https://docs.aws.amazon.com/mediapackage/latest/APIReference/API_DeleteChannelPolicy.html): Delete a channel policy.
- [DeleteOriginEndpoint](https://docs.aws.amazon.com/mediapackage/latest/APIReference/API_DeleteOriginEndpoint.html): Origin endpoints can serve content until they're deleted.
- [DeleteOriginEndpointPolicy](https://docs.aws.amazon.com/mediapackage/latest/APIReference/API_DeleteOriginEndpointPolicy.html): Delete an origin endpoint policy.
- [GetChannel](https://docs.aws.amazon.com/mediapackage/latest/APIReference/API_GetChannel.html): Retrieves the specified channel that's configured in AWS Elemental MediaPackage.
- [GetChannelGroup](https://docs.aws.amazon.com/mediapackage/latest/APIReference/API_GetChannelGroup.html): Retrieves the specified channel group that's configured in AWS Elemental MediaPackage.
- [GetChannelPolicy](https://docs.aws.amazon.com/mediapackage/latest/APIReference/API_GetChannelPolicy.html): Retrieves the specified channel policy that's configured in AWS Elemental MediaPackage.
- [GetHarvestJob](https://docs.aws.amazon.com/mediapackage/latest/APIReference/API_GetHarvestJob.html): Retrieves the details of a specific harvest job.
- [GetOriginEndpoint](https://docs.aws.amazon.com/mediapackage/latest/APIReference/API_GetOriginEndpoint.html): Retrieves the specified origin endpoint that's configured in AWS Elemental MediaPackage to obtain its playback URL and to view the packaging settings that it's currently using.
- [GetOriginEndpointPolicy](https://docs.aws.amazon.com/mediapackage/latest/APIReference/API_GetOriginEndpointPolicy.html): Retrieves the specified origin endpoint policy that's configured in AWS Elemental MediaPackage.
- [ListChannelGroups](https://docs.aws.amazon.com/mediapackage/latest/APIReference/API_ListChannelGroups.html): Retrieves all channel groups that are configured in AWS Elemental MediaPackage.
- [ListChannels](https://docs.aws.amazon.com/mediapackage/latest/APIReference/API_ListChannels.html): Retrieves all channels in a specific channel group that are configured in AWS Elemental MediaPackage.
- [ListHarvestJobs](https://docs.aws.amazon.com/mediapackage/latest/APIReference/API_ListHarvestJobs.html): Retrieves a list of harvest jobs that match the specified criteria.
- [ListOriginEndpoints](https://docs.aws.amazon.com/mediapackage/latest/APIReference/API_ListOriginEndpoints.html): Retrieves all origin endpoints in a specific channel that are configured in AWS Elemental MediaPackage.
- [ListTagsForResource](https://docs.aws.amazon.com/mediapackage/latest/APIReference/API_ListTagsForResource.html): Lists the tags assigned to a resource.
- [PutChannelPolicy](https://docs.aws.amazon.com/mediapackage/latest/APIReference/API_PutChannelPolicy.html): Attaches an IAM policy to the specified channel.
- [PutOriginEndpointPolicy](https://docs.aws.amazon.com/mediapackage/latest/APIReference/API_PutOriginEndpointPolicy.html): Attaches an IAM policy to the specified origin endpoint.
- [ResetChannelState](https://docs.aws.amazon.com/mediapackage/latest/APIReference/API_ResetChannelState.html): Resetting the channel can help to clear errors from misconfigurations in the encoder.
- [ResetOriginEndpointState](https://docs.aws.amazon.com/mediapackage/latest/APIReference/API_ResetOriginEndpointState.html): Resetting the origin endpoint can help to resolve unexpected behavior and other content packaging issues.
- [TagResource](https://docs.aws.amazon.com/mediapackage/latest/APIReference/API_TagResource.html): Assigns one of more tags (key-value pairs) to the specified MediaPackage resource.
- [UntagResource](https://docs.aws.amazon.com/mediapackage/latest/APIReference/API_UntagResource.html): Removes one or more tags from the specified resource.
- [UpdateChannel](https://docs.aws.amazon.com/mediapackage/latest/APIReference/API_UpdateChannel.html): Update the specified channel.
- [UpdateChannelGroup](https://docs.aws.amazon.com/mediapackage/latest/APIReference/API_UpdateChannelGroup.html): Update the specified channel group.
- [UpdateOriginEndpoint](https://docs.aws.amazon.com/mediapackage/latest/APIReference/API_UpdateOriginEndpoint.html): Update the specified origin endpoint.


## [Data Types](https://docs.aws.amazon.com/mediapackage/latest/APIReference/API_Types.html)

- [CdnAuthConfiguration](https://docs.aws.amazon.com/mediapackage/latest/APIReference/API_CdnAuthConfiguration.html): The settings to enable CDN authorization headers in MediaPackage.
- [ChannelGroupListConfiguration](https://docs.aws.amazon.com/mediapackage/latest/APIReference/API_ChannelGroupListConfiguration.html): The configuration of the channel group.
- [ChannelListConfiguration](https://docs.aws.amazon.com/mediapackage/latest/APIReference/API_ChannelListConfiguration.html): The configuration of the channel.
- [CreateDashManifestConfiguration](https://docs.aws.amazon.com/mediapackage/latest/APIReference/API_CreateDashManifestConfiguration.html): Create a DASH manifest configuration.
- [CreateHlsManifestConfiguration](https://docs.aws.amazon.com/mediapackage/latest/APIReference/API_CreateHlsManifestConfiguration.html): Create an HTTP live streaming (HLS) manifest configuration.
- [CreateLowLatencyHlsManifestConfiguration](https://docs.aws.amazon.com/mediapackage/latest/APIReference/API_CreateLowLatencyHlsManifestConfiguration.html): Create a low-latency HTTP live streaming (HLS) manifest configuration.
- [CreateMssManifestConfiguration](https://docs.aws.amazon.com/mediapackage/latest/APIReference/API_CreateMssManifestConfiguration.html): Configuration parameters for creating a Microsoft Smooth Streaming (MSS) manifest.
- [DashBaseUrl](https://docs.aws.amazon.com/mediapackage/latest/APIReference/API_DashBaseUrl.html): The base URLs to use for retrieving segments.
- [DashDvbFontDownload](https://docs.aws.amazon.com/mediapackage/latest/APIReference/API_DashDvbFontDownload.html): For use with DVB-DASH profiles only.
- [DashDvbMetricsReporting](https://docs.aws.amazon.com/mediapackage/latest/APIReference/API_DashDvbMetricsReporting.html): For use with DVB-DASH profiles only.
- [DashDvbSettings](https://docs.aws.amazon.com/mediapackage/latest/APIReference/API_DashDvbSettings.html): For endpoints that use the DVB-DASH profile only.
- [DashProgramInformation](https://docs.aws.amazon.com/mediapackage/latest/APIReference/API_DashProgramInformation.html): Details about the content that you want MediaPackage to pass through in the manifest to the playback device.
- [DashSubtitleConfiguration](https://docs.aws.amazon.com/mediapackage/latest/APIReference/API_DashSubtitleConfiguration.html): The configuration for DASH subtitles.
- [DashTtmlConfiguration](https://docs.aws.amazon.com/mediapackage/latest/APIReference/API_DashTtmlConfiguration.html): The settings for TTML subtitles.
- [DashUtcTiming](https://docs.aws.amazon.com/mediapackage/latest/APIReference/API_DashUtcTiming.html): Determines the type of UTC timing included in the DASH Media Presentation Description (MPD).
- [Destination](https://docs.aws.amazon.com/mediapackage/latest/APIReference/API_Destination.html): The configuration for the destination where the harvested content will be exported.
- [Encryption](https://docs.aws.amazon.com/mediapackage/latest/APIReference/API_Encryption.html): The parameters for encrypting content.
- [EncryptionContractConfiguration](https://docs.aws.amazon.com/mediapackage/latest/APIReference/API_EncryptionContractConfiguration.html): Configure one or more content encryption keys for your endpoints that use SPEKE Version 2.0.
- [EncryptionMethod](https://docs.aws.amazon.com/mediapackage/latest/APIReference/API_EncryptionMethod.html): The encryption type.
- [FilterConfiguration](https://docs.aws.amazon.com/mediapackage/latest/APIReference/API_FilterConfiguration.html): Filter configuration includes settings for manifest filtering, start and end times, and time delay that apply to all of your egress requests for this manifest.
- [ForceEndpointErrorConfiguration](https://docs.aws.amazon.com/mediapackage/latest/APIReference/API_ForceEndpointErrorConfiguration.html): The failover settings for the endpoint.
- [GetDashManifestConfiguration](https://docs.aws.amazon.com/mediapackage/latest/APIReference/API_GetDashManifestConfiguration.html): Retrieve the DASH manifest configuration.
- [GetHlsManifestConfiguration](https://docs.aws.amazon.com/mediapackage/latest/APIReference/API_GetHlsManifestConfiguration.html): Retrieve the HTTP live streaming (HLS) manifest configuration.
- [GetLowLatencyHlsManifestConfiguration](https://docs.aws.amazon.com/mediapackage/latest/APIReference/API_GetLowLatencyHlsManifestConfiguration.html): Retrieve the low-latency HTTP live streaming (HLS) manifest configuration.
- [GetMssManifestConfiguration](https://docs.aws.amazon.com/mediapackage/latest/APIReference/API_GetMssManifestConfiguration.html): Configuration details for a Microsoft Smooth Streaming (MSS) manifest associated with an origin endpoint.
- [HarvestedDashManifest](https://docs.aws.amazon.com/mediapackage/latest/APIReference/API_HarvestedDashManifest.html): Information about a harvested DASH manifest.
- [HarvestedHlsManifest](https://docs.aws.amazon.com/mediapackage/latest/APIReference/API_HarvestedHlsManifest.html): Information about a harvested HLS manifest.
- [HarvestedLowLatencyHlsManifest](https://docs.aws.amazon.com/mediapackage/latest/APIReference/API_HarvestedLowLatencyHlsManifest.html): Information about a harvested Low-Latency HLS manifest.
- [HarvestedManifests](https://docs.aws.amazon.com/mediapackage/latest/APIReference/API_HarvestedManifests.html): A collection of harvested manifests of different types.
- [HarvesterScheduleConfiguration](https://docs.aws.amazon.com/mediapackage/latest/APIReference/API_HarvesterScheduleConfiguration.html): Defines the schedule configuration for a harvest job.
- [HarvestJob](https://docs.aws.amazon.com/mediapackage/latest/APIReference/API_HarvestJob.html): Represents a harvest job resource in MediaPackage v2, which is used to export content from an origin endpoint to an S3 bucket.
- [IngestEndpoint](https://docs.aws.amazon.com/mediapackage/latest/APIReference/API_IngestEndpoint.html): The ingest domain URL where the source stream should be sent.
- [InputSwitchConfiguration](https://docs.aws.amazon.com/mediapackage/latest/APIReference/API_InputSwitchConfiguration.html): The configuration for input switching based on the media quality confidence score (MQCS) as provided from AWS Elemental MediaLive.
- [ListDashManifestConfiguration](https://docs.aws.amazon.com/mediapackage/latest/APIReference/API_ListDashManifestConfiguration.html): List the DASH manifest configuration.
- [ListHlsManifestConfiguration](https://docs.aws.amazon.com/mediapackage/latest/APIReference/API_ListHlsManifestConfiguration.html): List the HTTP live streaming (HLS) manifest configuration.
- [ListLowLatencyHlsManifestConfiguration](https://docs.aws.amazon.com/mediapackage/latest/APIReference/API_ListLowLatencyHlsManifestConfiguration.html): List the low-latency HTTP live streaming (HLS) manifest configuration.
- [ListMssManifestConfiguration](https://docs.aws.amazon.com/mediapackage/latest/APIReference/API_ListMssManifestConfiguration.html): Summary information about a Microsoft Smooth Streaming (MSS) manifest configuration.
- [OriginEndpointListConfiguration](https://docs.aws.amazon.com/mediapackage/latest/APIReference/API_OriginEndpointListConfiguration.html): The configuration of the origin endpoint.
- [OutputHeaderConfiguration](https://docs.aws.amazon.com/mediapackage/latest/APIReference/API_OutputHeaderConfiguration.html): The settings for what common media server data (CMSD) headers AWS Elemental MediaPackage includes in responses to the CDN.
- [S3DestinationConfig](https://docs.aws.amazon.com/mediapackage/latest/APIReference/API_S3DestinationConfig.html): Configuration parameters for where in an S3 bucket to place the harvested content.
- [Scte](https://docs.aws.amazon.com/mediapackage/latest/APIReference/API_Scte.html): The SCTE configuration.
- [ScteDash](https://docs.aws.amazon.com/mediapackage/latest/APIReference/API_ScteDash.html): The SCTE configuration.
- [ScteHls](https://docs.aws.amazon.com/mediapackage/latest/APIReference/API_ScteHls.html): The SCTE configuration.
- [Segment](https://docs.aws.amazon.com/mediapackage/latest/APIReference/API_Segment.html): The segment configuration, including the segment name, duration, and other configuration values.
- [SpekeKeyProvider](https://docs.aws.amazon.com/mediapackage/latest/APIReference/API_SpekeKeyProvider.html): The parameters for the SPEKE key provider.
- [StartTag](https://docs.aws.amazon.com/mediapackage/latest/APIReference/API_StartTag.html): To insert an EXT-X-START tag in your HLS playlist, specify a StartTag configuration object with a valid TimeOffset.
