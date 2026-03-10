# Source: https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/llms.txt

# Amazon IVS Low-Latency Streaming API Reference

> Introduction

- [Welcome](https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/Welcome.html)
- [Channel Types](https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/channel-types.html)
- [Common Parameters](https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/CommonErrors.html)

## [Actions](https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_Operations.html)

- [BatchGetChannel](https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_BatchGetChannel.html): Performs on multiple ARNs simultaneously.
- [BatchGetStreamKey](https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_BatchGetStreamKey.html): Performs on multiple ARNs simultaneously.
- [BatchStartViewerSessionRevocation](https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_BatchStartViewerSessionRevocation.html): Performs on multiple channel ARN and viewer ID pairs simultaneously.
- [CreateChannel](https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_CreateChannel.html): Creates a new channel and an associated stream key to start streaming.
- [CreatePlaybackRestrictionPolicy](https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_CreatePlaybackRestrictionPolicy.html): Creates a new playback restriction policy, for constraining playback by countries and/or origins.
- [CreateRecordingConfiguration](https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_CreateRecordingConfiguration.html): Creates a new recording configuration, used to enable recording to Amazon S3.
- [CreateStreamKey](https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_CreateStreamKey.html): Creates a stream key, used to initiate a stream, for the specified channel ARN.
- [DeleteChannel](https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_DeleteChannel.html): Deletes the specified channel and its associated stream keys.
- [DeletePlaybackKeyPair](https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_DeletePlaybackKeyPair.html): Deletes a specified authorization key pair.
- [DeletePlaybackRestrictionPolicy](https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_DeletePlaybackRestrictionPolicy.html): Deletes the specified playback restriction policy.
- [DeleteRecordingConfiguration](https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_DeleteRecordingConfiguration.html): Deletes the recording configuration for the specified ARN.
- [DeleteStreamKey](https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_DeleteStreamKey.html): Deletes the stream key for the specified ARN, so it can no longer be used to stream.
- [GetChannel](https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_GetChannel.html): Gets the channel configuration for the specified channel ARN.
- [GetPlaybackKeyPair](https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_GetPlaybackKeyPair.html): Gets a specified playback authorization key pair and returns the arn and fingerprint.
- [GetPlaybackRestrictionPolicy](https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_GetPlaybackRestrictionPolicy.html): Gets the specified playback restriction policy.
- [GetRecordingConfiguration](https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_GetRecordingConfiguration.html): Gets the recording configuration for the specified ARN.
- [GetStream](https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_GetStream.html): Gets information about the active (live) stream on a specified channel.
- [GetStreamKey](https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_GetStreamKey.html): Gets stream-key information for a specified ARN.
- [GetStreamSession](https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_GetStreamSession.html): Gets metadata on a specified stream.
- [ImportPlaybackKeyPair](https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_ImportPlaybackKeyPair.html): Imports the public portion of a new key pair and returns its arn and fingerprint.
- [ListChannels](https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_ListChannels.html): Gets summary information about all channels in your account, in the AWS region where the API request is processed.
- [ListPlaybackKeyPairs](https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_ListPlaybackKeyPairs.html): Gets summary information about playback key pairs.
- [ListPlaybackRestrictionPolicies](https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_ListPlaybackRestrictionPolicies.html): Gets summary information about playback restriction policies.
- [ListRecordingConfigurations](https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_ListRecordingConfigurations.html): Gets summary information about all recording configurations in your account, in the AWS region where the API request is processed.
- [ListStreamKeys](https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_ListStreamKeys.html): Gets summary information about stream keys for the specified channel.
- [ListStreams](https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_ListStreams.html): Gets summary information about live streams in your account, in the AWS region where the API request is processed.
- [ListStreamSessions](https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_ListStreamSessions.html): Gets a summary of current and previous streams for a specified channel in your account, in the AWS region where the API request is processed.
- [ListTagsForResource](https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_ListTagsForResource.html): Gets information about AWS tags for the specified ARN.
- [PutMetadata](https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_PutMetadata.html): Inserts metadata into the active stream of the specified channel.
- [StartViewerSessionRevocation](https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_StartViewerSessionRevocation.html): Starts the process of revoking the viewer session associated with a specified channel ARN and viewer ID.
- [StopStream](https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_StopStream.html): Disconnects the incoming RTMPS stream for the specified channel.
- [TagResource](https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_TagResource.html): Adds or updates tags for the AWS resource with the specified ARN.
- [UntagResource](https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_UntagResource.html): Removes tags from the resource with the specified ARN.
- [UpdateChannel](https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_UpdateChannel.html): Updates a channel's configuration.
- [UpdatePlaybackRestrictionPolicy](https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_UpdatePlaybackRestrictionPolicy.html): Updates a specified playback restriction policy.


## [Data Types](https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_Types.html)

- [AudioConfiguration](https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_AudioConfiguration.html): Object specifying a streamâs audio configuration, as set up by the broadcaster (usually in an encoder).
- [BatchError](https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_BatchError.html): Error related to a specific channel, specified by its ARN.
- [BatchStartViewerSessionRevocationError](https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_BatchStartViewerSessionRevocationError.html): Error for a request in the batch for BatchStartViewerSessionRevocation.
- [BatchStartViewerSessionRevocationViewerSession](https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_BatchStartViewerSessionRevocationViewerSession.html): A viewer session to revoke in the call to .
- [Channel](https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_Channel.html): Object specifying a channel.
- [ChannelSummary](https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_ChannelSummary.html): Summary information about a channel.
- [DestinationConfiguration](https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_DestinationConfiguration.html): A complex type that describes a location where recorded videos will be stored.
- [IngestConfiguration](https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_IngestConfiguration.html): Object specifying the ingest configuration set up by the broadcaster, usually in an encoder.
- [IngestConfigurations](https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_IngestConfigurations.html): Object specifying the ingest configuration set up by the broadcaster, usually in an encoder.
- [MultitrackInputConfiguration](https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_MultitrackInputConfiguration.html): A complex type that specifies multitrack input configuration.
- [PlaybackKeyPair](https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_PlaybackKeyPair.html): A key pair used to sign and validate a playback authorization token.
- [PlaybackKeyPairSummary](https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_PlaybackKeyPairSummary.html): Summary information about a playback key pair.
- [PlaybackRestrictionPolicy](https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_PlaybackRestrictionPolicy.html): An object representing a policy to constrain playback by country and/or origin sites.
- [PlaybackRestrictionPolicySummary](https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_PlaybackRestrictionPolicySummary.html): Summary information about a PlaybackRestrictionPolicy.
- [RecordingConfiguration](https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_RecordingConfiguration.html): An object representing a configuration to record a channel stream.
- [RecordingConfigurationSummary](https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_RecordingConfigurationSummary.html): Summary information about a RecordingConfiguration.
- [RenditionConfiguration](https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_RenditionConfiguration.html): Object that describes which renditions should be recorded for a stream.
- [S3DestinationConfiguration](https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_S3DestinationConfiguration.html): A complex type that describes an S3 location where recorded videos will be stored.
- [Srt](https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_Srt.html): Specifies information needed to stream using the SRT protocol.
- [Stream](https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_Stream.html): Specifies a live video stream that has been ingested and distributed.
- [StreamEvent](https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_StreamEvent.html): Object specifying a streamâs events.
- [StreamFilters](https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_StreamFilters.html): Object specifying the stream attribute on which to filter.
- [StreamKey](https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_StreamKey.html): Object specifying a stream key.
- [StreamKeySummary](https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_StreamKeySummary.html): Summary information about a stream key.
- [StreamSession](https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_StreamSession.html): Object that captures the Amazon IVS configuration that the customer provisioned, the ingest configurations that the broadcaster used, and the most recent Amazon IVS stream events it encountered.
- [StreamSessionSummary](https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_StreamSessionSummary.html): Summary information about a stream session.
- [StreamSummary](https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_StreamSummary.html): Summary information about a stream.
- [ThumbnailConfiguration](https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_ThumbnailConfiguration.html): An object representing a configuration of thumbnails for recorded video.
- [VideoConfiguration](https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_VideoConfiguration.html): Object specifying a streamâs video configuration, as set up by the broadcaster (usually in an encoder).
