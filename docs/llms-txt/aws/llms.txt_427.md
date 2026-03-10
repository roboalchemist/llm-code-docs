# Source: https://docs.aws.amazon.com/ground-station/latest/APIReference/llms.txt

# AWS Ground Station API Reference

> Welcome to the AWS Ground Station API Reference. AWS Ground Station is a fully managed service that enables you to control satellite communications, downlink and process satellite data, and scale your satellite operations efficiently and cost-effectively without having to build or manage your own ground station infrastructure.

- [Welcome](https://docs.aws.amazon.com/ground-station/latest/APIReference/Welcome.html)
- [Common Parameters](https://docs.aws.amazon.com/ground-station/latest/APIReference/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/ground-station/latest/APIReference/CommonErrors.html)

## [Actions](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_Operations.html)

- [CancelContact](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_CancelContact.html): Cancels or stops a contact with a specified contact ID based on its position in the contact lifecycle.
- [CreateConfig](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_CreateConfig.html): Creates a Config with the specified configData parameters.
- [CreateDataflowEndpointGroup](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_CreateDataflowEndpointGroup.html): Creates a DataflowEndpoint group containing the specified list of DataflowEndpoint objects.
- [CreateDataflowEndpointGroupV2](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_CreateDataflowEndpointGroupV2.html): Creates a DataflowEndpoint group containing the specified list of Ground Station Agent based endpoints.
- [CreateEphemeris](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_CreateEphemeris.html): Create an ephemeris with your specified .
- [CreateMissionProfile](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_CreateMissionProfile.html): Creates a mission profile.
- [DeleteConfig](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_DeleteConfig.html): Deletes a Config.
- [DeleteDataflowEndpointGroup](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_DeleteDataflowEndpointGroup.html): Deletes a dataflow endpoint group.
- [DeleteEphemeris](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_DeleteEphemeris.html): Delete an ephemeris.
- [DeleteMissionProfile](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_DeleteMissionProfile.html): Deletes a mission profile.
- [DescribeContact](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_DescribeContact.html): Describes an existing contact.
- [DescribeEphemeris](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_DescribeEphemeris.html): Retrieve information about an existing ephemeris.
- [GetAgentConfiguration](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_GetAgentConfiguration.html)
- [GetAgentTaskResponseUrl](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_GetAgentTaskResponseUrl.html)
- [GetConfig](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_GetConfig.html): Returns Config information.
- [GetDataflowEndpointGroup](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_GetDataflowEndpointGroup.html): Returns the dataflow endpoint group.
- [GetMinuteUsage](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_GetMinuteUsage.html): Returns the number of reserved minutes used by account.
- [GetMissionProfile](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_GetMissionProfile.html): Returns a mission profile.
- [GetSatellite](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_GetSatellite.html): Returns a satellite.
- [ListConfigs](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_ListConfigs.html): Returns a list of Config objects.
- [ListContacts](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_ListContacts.html): Returns a list of contacts.
- [ListDataflowEndpointGroups](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_ListDataflowEndpointGroups.html): Returns a list of DataflowEndpoint groups.
- [ListEphemerides](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_ListEphemerides.html): List your existing ephemerides.
- [ListGroundStations](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_ListGroundStations.html): Returns a list of ground stations.
- [ListMissionProfiles](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_ListMissionProfiles.html): Returns a list of mission profiles.
- [ListSatellites](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_ListSatellites.html): Returns a list of satellites.
- [ListTagsForResource](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_ListTagsForResource.html): Returns a list of tags for a specified resource.
- [RegisterAgent](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_RegisterAgent.html)
- [ReserveContact](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_ReserveContact.html): Reserves a contact using specified parameters.
- [TagResource](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_TagResource.html): Assigns a tag to a resource.
- [UntagResource](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_UntagResource.html): Deassigns a resource tag.
- [UpdateAgentStatus](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_UpdateAgentStatus.html)
- [UpdateConfig](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_UpdateConfig.html): Updates the Config used when scheduling contacts.
- [UpdateEphemeris](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_UpdateEphemeris.html): Update an existing ephemeris.
- [UpdateMissionProfile](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_UpdateMissionProfile.html): Updates a mission profile.


## [Data Types](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_Types.html)

- [AgentDetails](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_AgentDetails.html): Detailed information about the agent.
- [AggregateStatus](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_AggregateStatus.html): Aggregate status of Agent components.
- [AntennaDemodDecodeDetails](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_AntennaDemodDecodeDetails.html): Details about an antenna demod decode Config used in a contact.
- [AntennaDownlinkConfig](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_AntennaDownlinkConfig.html): Information about how AWS Ground Station should configure an antenna for downlink during a contact.
- [AntennaDownlinkDemodDecodeConfig](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_AntennaDownlinkDemodDecodeConfig.html): Information about how AWS Ground Station should conï¬gure an antenna for downlink demod decode during a contact.
- [AntennaUplinkConfig](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_AntennaUplinkConfig.html): Information about the uplink Config of an antenna.
- [AwsGroundStationAgentEndpoint](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_AwsGroundStationAgentEndpoint.html): Information about AwsGroundStationAgentEndpoint.
- [AzElEphemeris](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_AzElEphemeris.html): Azimuth elevation ephemeris data.
- [AzElEphemerisFilter](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_AzElEphemerisFilter.html): Filter for selecting contacts that use a specific .
- [AzElProgramTrackSettings](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_AzElProgramTrackSettings.html): Program track settings for .
- [AzElSegment](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_AzElSegment.html): A time segment containing azimuth elevation pointing data.
- [AzElSegments](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_AzElSegments.html): Azimuth elevation segment collection.
- [AzElSegmentsData](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_AzElSegmentsData.html): Container for azimuth elevation segment data.
- [ComponentStatusData](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_ComponentStatusData.html): Data on the status of agent components.
- [ComponentVersion](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_ComponentVersion.html): Version information for agent components.
- [ConfigDetails](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_ConfigDetails.html): Details for certain Config object types in a contact.
- [ConfigListItem](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_ConfigListItem.html): An item in a list of Config objects.
- [ConfigTypeData](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_ConfigTypeData.html): Object containing the parameters of a Config.
- [ConnectionDetails](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_ConnectionDetails.html): Egress address of AgentEndpoint with an optional mtu.
- [ContactData](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_ContactData.html): Data describing a contact.
- [CreateEndpointDetails](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_CreateEndpointDetails.html): Endpoint definition used for creating a dataflow endpoint
- [DataflowDetail](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_DataflowDetail.html): Information about a dataflow edge used in a contact.
- [DataflowEndpoint](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_DataflowEndpoint.html): Information about a dataflow endpoint.
- [DataflowEndpointConfig](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_DataflowEndpointConfig.html): Information about the dataflow endpoint Config.
- [DataflowEndpointListItem](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_DataflowEndpointListItem.html): Item in a list of DataflowEndpoint groups.
- [DecodeConfig](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_DecodeConfig.html): Information about the decode Config.
- [DemodulationConfig](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_DemodulationConfig.html): Information about the demodulation Config.
- [Destination](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_Destination.html): Dataflow details for the destination side.
- [DiscoveryData](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_DiscoveryData.html): Data for agent discovery.
- [DownlinkAwsGroundStationAgentEndpoint](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_DownlinkAwsGroundStationAgentEndpoint.html): Definition for a downlink agent endpoint
- [DownlinkAwsGroundStationAgentEndpointDetails](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_DownlinkAwsGroundStationAgentEndpointDetails.html): Details for a downlink agent endpoint
- [DownlinkConnectionDetails](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_DownlinkConnectionDetails.html): Connection details for Ground Station to Agent and Agent to customer
- [DownlinkDataflowDetails](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_DownlinkDataflowDetails.html): Dataflow details for a downlink endpoint
- [Eirp](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_Eirp.html): Object that represents EIRP.
- [Elevation](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_Elevation.html): Elevation angle of the satellite in the sky during a contact.
- [EndpointDetails](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_EndpointDetails.html): Information about the endpoint details.
- [EphemerisData](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_EphemerisData.html): Ephemeris data.
- [EphemerisDescription](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_EphemerisDescription.html): Description of ephemeris.
- [EphemerisErrorReason](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_EphemerisErrorReason.html): Detailed error information for ephemeris validation failures.
- [EphemerisFilter](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_EphemerisFilter.html): Filter for selecting contacts that use a specific ephemeris".
- [EphemerisItem](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_EphemerisItem.html): Ephemeris item.
- [EphemerisMetaData](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_EphemerisMetaData.html): Metadata describing a particular ephemeris.
- [EphemerisResponseData](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_EphemerisResponseData.html): Ephemeris data for a contact.
- [EphemerisTypeDescription](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_EphemerisTypeDescription.html)
- [Frequency](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_Frequency.html): Object that describes the frequency.
- [FrequencyBandwidth](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_FrequencyBandwidth.html): Object that describes the frequency bandwidth.
- [GroundStationData](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_GroundStationData.html): Information about the ground station data.
- [IntegerRange](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_IntegerRange.html): An integer range that has a minimum and maximum value.
- [ISO8601TimeRange](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_ISO8601TimeRange.html): Time range specified using ISO 8601 format timestamps.
- [KinesisDataStreamData](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_KinesisDataStreamData.html): Information for telemetry delivery to Kinesis Data Streams.
- [KmsKey](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_KmsKey.html): KMS key info.
- [MissionProfileListItem](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_MissionProfileListItem.html): Item in a list of mission profiles.
- [OEMEphemeris](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_OEMEphemeris.html): Ephemeris data in Orbit Ephemeris Message (OEM) format.
- [ProgramTrackSettings](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_ProgramTrackSettings.html): Program track settings for an antenna during a contact.
- [RangedConnectionDetails](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_RangedConnectionDetails.html): Ingress address of AgentEndpoint with a port range and an optional mtu.
- [RangedSocketAddress](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_RangedSocketAddress.html): A socket address with a port range.
- [S3Object](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_S3Object.html): Object stored in Amazon S3 containing ephemeris data.
- [S3RecordingConfig](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_S3RecordingConfig.html): Information about an S3 recording Config.
- [S3RecordingDetails](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_S3RecordingDetails.html): Details about an S3 recording Config used in a contact.
- [SatelliteListItem](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_SatelliteListItem.html): Item in a list of satellites.
- [SecurityDetails](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_SecurityDetails.html): Information about endpoints.
- [SocketAddress](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_SocketAddress.html): Information about the socket address.
- [Source](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_Source.html): Dataflow details for the source side.
- [SpectrumConfig](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_SpectrumConfig.html): Object that describes a spectral Config.
- [TelemetrySinkConfig](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_TelemetrySinkConfig.html): Information about a telemetry sink Config.
- [TelemetrySinkData](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_TelemetrySinkData.html): Information about a telemetry sink.
- [TimeAzEl](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_TimeAzEl.html): Time-tagged azimuth elevation pointing data.
- [TimeRange](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_TimeRange.html): A time range with a start and end time.
- [TLEData](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_TLEData.html): Two-line element set (TLE) data.
- [TLEEphemeris](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_TLEEphemeris.html): Two-line element set (TLE) ephemeris.
- [TrackingConfig](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_TrackingConfig.html): Object that determines whether tracking should be used during a contact executed with this Config in the mission profile.
- [TrackingOverrides](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_TrackingOverrides.html): Overrides the default tracking configuration on an antenna during a contact.
- [UplinkAwsGroundStationAgentEndpoint](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_UplinkAwsGroundStationAgentEndpoint.html): Definition for an uplink agent endpoint
- [UplinkAwsGroundStationAgentEndpointDetails](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_UplinkAwsGroundStationAgentEndpointDetails.html): Details for an uplink agent endpoint
- [UplinkConnectionDetails](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_UplinkConnectionDetails.html): Connection details for customer to Agent and Agent to Ground Station
- [UplinkDataflowDetails](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_UplinkDataflowDetails.html): Dataflow details for an uplink endpoint
- [UplinkEchoConfig](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_UplinkEchoConfig.html): Information about an uplink echo Config.
- [UplinkSpectrumConfig](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_UplinkSpectrumConfig.html): Information about the uplink spectral Config.
