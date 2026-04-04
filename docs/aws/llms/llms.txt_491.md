# Source: https://docs.aws.amazon.com/ivs/latest/BroadcastSWIntegAPIReference/llms.txt

# Amazon IVS Multitrack Video Integration API Reference

> Describes in detail all operations for the Amazon IVS multitrack integration API for broadcast software developers to implement client support for multitrack video. The API is REST compatible, using a standard HTTP API. JSON is used for both requests and responses, including errors.

- [Welcome](https://docs.aws.amazon.com/ivs/latest/BroadcastSWIntegAPIReference/integ-api-welcome.html)

## [Actions](https://docs.aws.amazon.com/ivs/latest/BroadcastSWIntegAPIReference/actions.html)

- [GetClientConfiguration](https://docs.aws.amazon.com/ivs/latest/BroadcastSWIntegAPIReference/actions-GetClientConfiguration.html): Returns video and audio configurations that optimize the viewing experience based on the clientâs hardware and software configuration, user preferences, and limits of the video service.
- [FindIngest](https://docs.aws.amazon.com/ivs/latest/BroadcastSWIntegAPIReference/actions-FindIngest.html): Returns a list of available ingest endpoints.


## [Data Types](https://docs.aws.amazon.com/ivs/latest/BroadcastSWIntegAPIReference/structures.html)

- [AudioConfiguration](https://docs.aws.amazon.com/ivs/latest/BroadcastSWIntegAPIReference/structures-AudioConfiguration.html): Complex type specifying the streamâs audio configuration to be used by the encoder.
- [AudioTrackConfiguration](https://docs.aws.amazon.com/ivs/latest/BroadcastSWIntegAPIReference/structures-AudioTrackConfiguration.html): Complex type specifying an audio track configuration to be used by the encoder.
- [AudioTrackSettings](https://docs.aws.amazon.com/ivs/latest/BroadcastSWIntegAPIReference/structures-AudioTrackSettings.html): Object specifying encoder-specific settings.
- [CapabilitiesDescription](https://docs.aws.amazon.com/ivs/latest/BroadcastSWIntegAPIReference/structures-CapabilitiesDescription.html): Complex type specifying client hardware and software characteristics.
- [Client](https://docs.aws.amazon.com/ivs/latest/BroadcastSWIntegAPIReference/structures-Client.html): Object specifying the client software.
- [ClientConfigurationStatus](https://docs.aws.amazon.com/ivs/latest/BroadcastSWIntegAPIReference/structures-ClientConfigurationStatus.html): Object specifying errors or warnings to be exposed to the broadcaster.
- [ClientDescription](https://docs.aws.amazon.com/ivs/latest/BroadcastSWIntegAPIReference/structures-ClientDescription.html): Complex type specifying client software and configuration.
- [ConfigurationMetadata](https://docs.aws.amazon.com/ivs/latest/BroadcastSWIntegAPIReference/structures-ConfigurationMetadata.html): Object specifying the metadata for the configuration returned by .
- [CpuDescription](https://docs.aws.amazon.com/ivs/latest/BroadcastSWIntegAPIReference/structures-CpuDescription.html): Object specifying client CPU characteristics
- [EncoderConfiguration](https://docs.aws.amazon.com/ivs/latest/BroadcastSWIntegAPIReference/structures-EncoderConfiguration.html): Complex type specifying the streamâs video configuration to be used by the encoder.
- [Framerate](https://docs.aws.amazon.com/ivs/latest/BroadcastSWIntegAPIReference/structures-Framerate.html): Object specifying a framerate.
- [GamingFeaturesDescription](https://docs.aws.amazon.com/ivs/latest/BroadcastSWIntegAPIReference/structures-GamingFeaturesDescription.html): Object specifying the gaming features of the client.
- [GpuDescription](https://docs.aws.amazon.com/ivs/latest/BroadcastSWIntegAPIReference/structures-GpuDescription.html): Object specifying client GPU characteristics.
- [Ingest](https://docs.aws.amazon.com/ivs/latest/BroadcastSWIntegAPIReference/structures-Ingest.html): Object specifying ingest endpoints returned by .
- [IngestEndpoint](https://docs.aws.amazon.com/ivs/latest/BroadcastSWIntegAPIReference/structures-IngestEndpoint.html): Object specifying ingest endpoints returned by .
- [MemoryDescription](https://docs.aws.amazon.com/ivs/latest/BroadcastSWIntegAPIReference/structures-MemoryDescription.html): Object specifying client memory characteristics.
- [PreferencesDescription](https://docs.aws.amazon.com/ivs/latest/BroadcastSWIntegAPIReference/structures-PreferencesDescription.html): Complex type specifying preferences configured on the client.
- [SystemDescription](https://docs.aws.amazon.com/ivs/latest/BroadcastSWIntegAPIReference/structures-SystemDescription.html): Object specifying client system characteristics.
- [VideoTrackSettings](https://docs.aws.amazon.com/ivs/latest/BroadcastSWIntegAPIReference/structures-VideoTrackSettings.html): Object specifying encoder-specific settings.
