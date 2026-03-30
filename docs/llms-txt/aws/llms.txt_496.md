# Source: https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/llms.txt

# Amazon IVS Real-Time Streaming API Reference

> The Amazon Interactive Video Service (IVS) real-time API is REST compatible, using a standard HTTP API and an AWS EventBridge event stream for responses. JSON is used for both requests and responses, including errors.

- [Welcome](https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/Welcome.html)
- [Common Parameters](https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/CommonErrors.html)

## [Actions](https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_Operations.html)

- [CreateEncoderConfiguration](https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_CreateEncoderConfiguration.html): Creates an EncoderConfiguration object.
- [CreateIngestConfiguration](https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_CreateIngestConfiguration.html): Creates a new IngestConfiguration resource, used to specify the ingest protocol for a stage.
- [CreateParticipantToken](https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_CreateParticipantToken.html): Creates an additional token for a specified stage.
- [CreateStage](https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_CreateStage.html): Creates a new stage (and optionally participant tokens).
- [CreateStorageConfiguration](https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_CreateStorageConfiguration.html): Creates a new storage configuration, used to enable recording to Amazon S3.
- [DeleteEncoderConfiguration](https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_DeleteEncoderConfiguration.html): Deletes an EncoderConfiguration resource.
- [DeleteIngestConfiguration](https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_DeleteIngestConfiguration.html): Deletes a specified IngestConfiguration, so it can no longer be used to broadcast.
- [DeletePublicKey](https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_DeletePublicKey.html): Deletes the specified public key used to sign stage participant tokens.
- [DeleteStage](https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_DeleteStage.html): Shuts down and deletes the specified stage (disconnecting all participants).
- [DeleteStorageConfiguration](https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_DeleteStorageConfiguration.html): Deletes the storage configuration for the specified ARN.
- [DisconnectParticipant](https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_DisconnectParticipant.html): Disconnects a specified participant from a specified stage.
- [GetComposition](https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_GetComposition.html): Get information about the specified Composition resource.
- [GetEncoderConfiguration](https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_GetEncoderConfiguration.html): Gets information about the specified EncoderConfiguration resource.
- [GetIngestConfiguration](https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_GetIngestConfiguration.html): Gets information about the specified IngestConfiguration.
- [GetParticipant](https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_GetParticipant.html): Gets information about the specified participant token.
- [GetPublicKey](https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_GetPublicKey.html): Gets information for the specified public key.
- [GetStage](https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_GetStage.html): Gets information for the specified stage.
- [GetStageSession](https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_GetStageSession.html): Gets information for the specified stage session.
- [GetStorageConfiguration](https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_GetStorageConfiguration.html): Gets the storage configuration for the specified ARN.
- [ImportPublicKey](https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_ImportPublicKey.html): Import a public key to be used for signing stage participant tokens.
- [ListCompositions](https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_ListCompositions.html): Gets summary information about all Compositions in your account, in the AWS region where the API request is processed.
- [ListEncoderConfigurations](https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_ListEncoderConfigurations.html): Gets summary information about all EncoderConfigurations in your account, in the AWS region where the API request is processed.
- [ListIngestConfigurations](https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_ListIngestConfigurations.html): Lists all IngestConfigurations in your account, in the AWS region where the API request is processed.
- [ListParticipantEvents](https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_ListParticipantEvents.html): Lists events for a specified participant that occurred during a specified stage session.
- [ListParticipantReplicas](https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_ListParticipantReplicas.html): Lists all the replicas for a participant from a source stage.
- [ListParticipants](https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_ListParticipants.html): Lists all participants in a specified stage session.
- [ListPublicKeys](https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_ListPublicKeys.html): Gets summary information about all public keys in your account, in the AWS region where the API request is processed.
- [ListStages](https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_ListStages.html): Gets summary information about all stages in your account, in the AWS region where the API request is processed.
- [ListStageSessions](https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_ListStageSessions.html): Gets all sessions for a specified stage.
- [ListStorageConfigurations](https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_ListStorageConfigurations.html): Gets summary information about all storage configurations in your account, in the AWS region where the API request is processed.
- [ListTagsForResource](https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_ListTagsForResource.html): Gets information about AWS tags for the specified ARN.
- [StartComposition](https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_StartComposition.html): Starts a Composition from a stage based on the configuration provided in the request.
- [StartParticipantReplication](https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_StartParticipantReplication.html): Starts replicating a publishing participant from a source stage to a destination stage.
- [StopComposition](https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_StopComposition.html): Stops and deletes a Composition resource.
- [StopParticipantReplication](https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_StopParticipantReplication.html): Stops a replicated participant session.
- [TagResource](https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_TagResource.html): Adds or updates tags for the AWS resource with the specified ARN.
- [UntagResource](https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_UntagResource.html): Removes tags from the resource with the specified ARN.
- [UpdateIngestConfiguration](https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_UpdateIngestConfiguration.html): Updates a specified IngestConfiguration.
- [UpdateStage](https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_UpdateStage.html): Updates a stageâs configuration.


## [Data Types](https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_Types.html)

- [AutoParticipantRecordingConfiguration](https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_AutoParticipantRecordingConfiguration.html): Object specifying a configuration for individual participant recording.
- [ChannelDestinationConfiguration](https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_ChannelDestinationConfiguration.html): Object specifying a channel as a destination.
- [Composition](https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_Composition.html): Object specifying a Composition resource.
- [CompositionRecordingHlsConfiguration](https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_CompositionRecordingHlsConfiguration.html): An object representing a configuration of HLS recordings for server-side composition.
- [CompositionSummary](https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_CompositionSummary.html): Summary information about a Composition.
- [CompositionThumbnailConfiguration](https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_CompositionThumbnailConfiguration.html): An object representing a configuration of thumbnails for recorded video for a .
- [Destination](https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_Destination.html): Object specifying the status of a Destination.
- [DestinationConfiguration](https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_DestinationConfiguration.html): Complex data type that defines destination-configuration objects.
- [DestinationDetail](https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_DestinationDetail.html): Complex data type that defines destination-detail objects.
- [DestinationSummary](https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_DestinationSummary.html): Summary information about a Destination.
- [EncoderConfiguration](https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_EncoderConfiguration.html): Settings for transcoding.
- [EncoderConfigurationSummary](https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_EncoderConfigurationSummary.html): Summary information about an EncoderConfiguration.
- [Event](https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_Event.html): An occurrence during a stage session.
- [ExchangedParticipantToken](https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_ExchangedParticipantToken.html): Object specifying an exchanged participant token in a stage, created when an original participant token is updated.
- [GridConfiguration](https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_GridConfiguration.html): Configuration information specific to Grid layout, for server-side composition.
- [IngestConfiguration](https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_IngestConfiguration.html): Object specifying an ingest configuration.
- [IngestConfigurationSummary](https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_IngestConfigurationSummary.html): Summary information about an IngestConfiguration.
- [LayoutConfiguration](https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_LayoutConfiguration.html): Configuration information of supported layouts for server-side composition.
- [Participant](https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_Participant.html): Object describing a participant that has joined a stage.
- [ParticipantRecordingHlsConfiguration](https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_ParticipantRecordingHlsConfiguration.html): An object representing a configuration of participant HLS recordings for individual participant recording.
- [ParticipantReplica](https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_ParticipantReplica.html): Information about the replicated destination stage for a participant.
- [ParticipantSummary](https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_ParticipantSummary.html): Summary object describing a participant that has joined a stage.
- [ParticipantThumbnailConfiguration](https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_ParticipantThumbnailConfiguration.html): An object representing a configuration of thumbnails for recorded video from an individual participant.
- [ParticipantToken](https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_ParticipantToken.html): Object specifying a participant token in a stage.
- [ParticipantTokenConfiguration](https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_ParticipantTokenConfiguration.html): Object specifying a participant token configuration in a stage.
- [PipConfiguration](https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_PipConfiguration.html): Configuration information specific to Picture-in-Picture (PiP) layout, for server-side composition.
- [PublicKey](https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_PublicKey.html): Object specifying a public key used to sign stage participant tokens.
- [PublicKeySummary](https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_PublicKeySummary.html): Summary information about a public key.
- [RecordingConfiguration](https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_RecordingConfiguration.html): An object representing a configuration to record a stage stream.
- [S3DestinationConfiguration](https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_S3DestinationConfiguration.html): A complex type that describes an S3 location where recorded videos will be stored.
- [S3Detail](https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_S3Detail.html): Complex data type that defines S3Detail objects.
- [S3StorageConfiguration](https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_S3StorageConfiguration.html): A complex type that describes an S3 location where recorded videos will be stored.
- [Stage](https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_Stage.html): Object specifying a stage.
- [StageEndpoints](https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_StageEndpoints.html): Summary information about various endpoints for a stage.
- [StageSession](https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_StageSession.html): A stage session begins when the first participant joins a stage and ends after the last participant leaves the stage.
- [StageSessionSummary](https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_StageSessionSummary.html): Summary information about a stage session.
- [StageSummary](https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_StageSummary.html): Summary information about a stage.
- [StorageConfiguration](https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_StorageConfiguration.html): A complex type that describes a location where recorded videos will be stored.
- [StorageConfigurationSummary](https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_StorageConfigurationSummary.html): Summary information about a storage configuration.
- [Video](https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_Video.html): Settings for video.
