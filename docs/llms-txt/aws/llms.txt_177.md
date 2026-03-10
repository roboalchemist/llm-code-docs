# Source: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/llms.txt

# Amazon Chime SDK API Reference

> The Amazon Chime SDK Identity APIs in this section allow software developers to create and manage unique instances of their messaging applications. These APIs provide the overarching framework for creating and sending messages. For more information about the identity APIs, refer to Amazon Chime SDK identity.

- [Welcome](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/welcome.html)
- [Common Errors](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/CommonErrors.html)

## [Actions](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_Operations.html)

### [Amazon Chime SDK Identity](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_Operations_Amazon_Chime_SDK_Identity.html)

The following actions are supported by Amazon Chime SDK Identity:

- [CreateAppInstance](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_CreateAppInstance.html): Creates an Amazon Chime SDK messaging AppInstance under an AWS account.
- [CreateAppInstanceAdmin](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_CreateAppInstanceAdmin.html): Promotes an AppInstanceUser or AppInstanceBot to an AppInstanceAdmin.
- [CreateAppInstanceBot](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_CreateAppInstanceBot.html): Creates a bot under an Amazon Chime AppInstance.
- [CreateAppInstanceUser](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_CreateAppInstanceUser.html): Creates a user under an Amazon Chime AppInstance.
- [DeleteAppInstance](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_DeleteAppInstance.html): Deletes an AppInstance and all associated data asynchronously.
- [DeleteAppInstanceAdmin](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_DeleteAppInstanceAdmin.html): Demotes an AppInstanceAdmin to an AppInstanceUser or AppInstanceBot.
- [DeleteAppInstanceBot](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_DeleteAppInstanceBot.html): Deletes an AppInstanceBot.
- [DeleteAppInstanceUser](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_DeleteAppInstanceUser.html): Deletes an AppInstanceUser.
- [DeregisterAppInstanceUserEndpoint](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_DeregisterAppInstanceUserEndpoint.html): Deregisters an AppInstanceUserEndpoint.
- [DescribeAppInstance](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_DescribeAppInstance.html): Returns the full details of an AppInstance.
- [DescribeAppInstanceAdmin](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_DescribeAppInstanceAdmin.html): Returns the full details of an AppInstanceAdmin.
- [DescribeAppInstanceBot](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_DescribeAppInstanceBot.html): The AppInstanceBot's information.
- [DescribeAppInstanceUser](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_DescribeAppInstanceUser.html): Returns the full details of an AppInstanceUser.
- [DescribeAppInstanceUserEndpoint](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_DescribeAppInstanceUserEndpoint.html): Returns the full details of an AppInstanceUserEndpoint.
- [GetAppInstanceRetentionSettings](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_GetAppInstanceRetentionSettings.html): Gets the retention settings for an AppInstance.
- [ListAppInstanceAdmins](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_ListAppInstanceAdmins.html): Returns a list of the administrators in the AppInstance.
- [ListAppInstanceBots](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_ListAppInstanceBots.html): Lists all AppInstanceBots created under a single AppInstance.
- [ListAppInstances](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_ListAppInstances.html): Lists all Amazon Chime AppInstances created under a single AWS account.
- [ListAppInstanceUserEndpoints](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_ListAppInstanceUserEndpoints.html): Lists all the AppInstanceUserEndpoints created under a single AppInstanceUser.
- [ListAppInstanceUsers](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_ListAppInstanceUsers.html): List all AppInstanceUsers created under a single AppInstance.
- [ListTagsForResource](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_ListTagsForResource.html): Lists the tags applied to an Amazon Chime SDK identity resource.
- [PutAppInstanceRetentionSettings](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_PutAppInstanceRetentionSettings.html): Sets the amount of time in days that a given AppInstance retains data.
- [PutAppInstanceUserExpirationSettings](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_PutAppInstanceUserExpirationSettings.html): Sets the number of days before the AppInstanceUser is automatically deleted.
- [RegisterAppInstanceUserEndpoint](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_RegisterAppInstanceUserEndpoint.html): Registers an endpoint under an Amazon Chime AppInstanceUser.
- [TagResource](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_TagResource.html): Applies the specified tags to the specified Amazon Chime SDK identity resource.
- [UntagResource](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_UntagResource.html): Removes the specified tags from the specified Amazon Chime SDK identity resource.
- [UpdateAppInstance](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_UpdateAppInstance.html): Updates AppInstance metadata.
- [UpdateAppInstanceBot](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_UpdateAppInstanceBot.html): Updates the name and metadata of an AppInstanceBot.
- [UpdateAppInstanceUser](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_UpdateAppInstanceUser.html): Updates the details of an AppInstanceUser.
- [UpdateAppInstanceUserEndpoint](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_UpdateAppInstanceUserEndpoint.html): Updates the details of an AppInstanceUserEndpoint.

### [Amazon Chime SDK Media Pipelines](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_Operations_Amazon_Chime_SDK_Media_Pipelines.html)

The following actions are supported by Amazon Chime SDK Media Pipelines:

- [CreateMediaCapturePipeline](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_CreateMediaCapturePipeline.html): Creates a media pipeline.
- [CreateMediaConcatenationPipeline](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_CreateMediaConcatenationPipeline.html): Creates a media concatenation pipeline.
- [CreateMediaInsightsPipeline](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_CreateMediaInsightsPipeline.html): Creates a media insights pipeline.
- [CreateMediaInsightsPipelineConfiguration](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_CreateMediaInsightsPipelineConfiguration.html): A structure that contains the static configurations for a media insights pipeline.
- [CreateMediaLiveConnectorPipeline](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_CreateMediaLiveConnectorPipeline.html): Creates a media live connector pipeline in an Amazon Chime SDK meeting.
- [CreateMediaPipelineKinesisVideoStreamPool](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_CreateMediaPipelineKinesisVideoStreamPool.html): Creates an Amazon Kinesis Video Stream pool for use with media stream pipelines.
- [CreateMediaStreamPipeline](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_CreateMediaStreamPipeline.html): Creates a streaming media pipeline.
- [DeleteMediaCapturePipeline](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_DeleteMediaCapturePipeline.html): Deletes the media pipeline.
- [DeleteMediaInsightsPipelineConfiguration](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_DeleteMediaInsightsPipelineConfiguration.html): Deletes the specified configuration settings.
- [DeleteMediaPipeline](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_DeleteMediaPipeline.html): Deletes the media pipeline.
- [DeleteMediaPipelineKinesisVideoStreamPool](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_DeleteMediaPipelineKinesisVideoStreamPool.html): Deletes an Amazon Kinesis Video Stream pool.
- [GetMediaCapturePipeline](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_GetMediaCapturePipeline.html): Gets an existing media pipeline.
- [GetMediaInsightsPipelineConfiguration](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_GetMediaInsightsPipelineConfiguration.html): Gets the configuration settings for a media insights pipeline.
- [GetMediaPipeline](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_GetMediaPipeline.html): Gets an existing media pipeline.
- [GetMediaPipelineKinesisVideoStreamPool](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_GetMediaPipelineKinesisVideoStreamPool.html): Gets an Kinesis video stream pool.
- [GetSpeakerSearchTask](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_GetSpeakerSearchTask.html): Retrieves the details of the specified speaker search task.
- [GetVoiceToneAnalysisTask](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_GetVoiceToneAnalysisTask.html): Retrieves the details of a voice tone analysis task.
- [ListMediaCapturePipelines](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_ListMediaCapturePipelines.html): Returns a list of media pipelines.
- [ListMediaInsightsPipelineConfigurations](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_ListMediaInsightsPipelineConfigurations.html): Lists the available media insights pipeline configurations.
- [ListMediaPipelineKinesisVideoStreamPools](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_ListMediaPipelineKinesisVideoStreamPools.html): Lists the video stream pools in the media pipeline.
- [ListMediaPipelines](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_ListMediaPipelines.html): Returns a list of media pipelines.
- [ListTagsForResource](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_ListTagsForResource.html): Lists the tags available for a media pipeline.
- [StartSpeakerSearchTask](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_StartSpeakerSearchTask.html): Starts a speaker search task.
- [StartVoiceToneAnalysisTask](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_StartVoiceToneAnalysisTask.html): Starts a voice tone analysis task.
- [StopSpeakerSearchTask](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_StopSpeakerSearchTask.html): Stops a speaker search task.
- [StopVoiceToneAnalysisTask](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_StopVoiceToneAnalysisTask.html): Stops a voice tone analysis task.
- [TagResource](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_TagResource.html): The ARN of the media pipeline that you want to tag.
- [UntagResource](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_UntagResource.html): Removes any tags from a media pipeline.
- [UpdateMediaInsightsPipelineConfiguration](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_UpdateMediaInsightsPipelineConfiguration.html): Updates the media insights pipeline's configuration settings.
- [UpdateMediaInsightsPipelineStatus](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_UpdateMediaInsightsPipelineStatus.html): Updates the status of a media insights pipeline.
- [UpdateMediaPipelineKinesisVideoStreamPool](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_UpdateMediaPipelineKinesisVideoStreamPool.html): Updates an Amazon Kinesis Video Stream pool in a media pipeline.

### [Amazon Chime SDK Meetings](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_Operations_Amazon_Chime_SDK_Meetings.html)

The following actions are supported by Amazon Chime SDK Meetings:

- [BatchCreateAttendee](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_BatchCreateAttendee.html): Creates up to 100 attendees for an active Amazon Chime SDK meeting.
- [BatchUpdateAttendeeCapabilitiesExcept](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_BatchUpdateAttendeeCapabilitiesExcept.html): Updates AttendeeCapabilities except the capabilities listed in an ExcludedAttendeeIds table.
- [CreateAttendee](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_CreateAttendee.html): Creates a new attendee for an active Amazon Chime SDK meeting.
- [CreateMeeting](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_CreateMeeting.html): Creates a new Amazon Chime SDK meeting in the specified media Region with no initial attendees.
- [CreateMeetingWithAttendees](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_CreateMeetingWithAttendees.html): Creates a new Amazon Chime SDK meeting in the specified media Region, with attendees.
- [DeleteAttendee](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_DeleteAttendee.html): Deletes an attendee from the specified Amazon Chime SDK meeting and deletes their JoinToken.
- [DeleteMeeting](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_DeleteMeeting.html): Deletes the specified Amazon Chime SDK meeting.
- [GetAttendee](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_GetAttendee.html): Gets the Amazon Chime SDK attendee details for a specified meeting ID and attendee ID.
- [GetMeeting](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_GetMeeting.html): Gets the Amazon Chime SDK meeting details for the specified meeting ID.
- [ListAttendees](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_ListAttendees.html): Lists the attendees for the specified Amazon Chime SDK meeting.
- [ListTagsForResource](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_ListTagsForResource.html): Returns a list of the tags available for the specified resource.
- [StartMeetingTranscription](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_StartMeetingTranscription.html): Starts transcription for the specified meetingId.
- [StopMeetingTranscription](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_StopMeetingTranscription.html): Stops transcription for the specified meetingId.
- [TagResource](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_TagResource.html): The resource that supports tags.
- [UntagResource](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_UntagResource.html): Removes the specified tags from the specified resources.
- [UpdateAttendeeCapabilities](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_UpdateAttendeeCapabilities.html): The capabilities that you want to update.

### [Amazon Chime SDK Messaging](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_Operations_Amazon_Chime_SDK_Messaging.html)

The following actions are supported by Amazon Chime SDK Messaging:

- [AssociateChannelFlow](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_AssociateChannelFlow.html): Associates a channel flow with a channel.
- [BatchCreateChannelMembership](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_BatchCreateChannelMembership.html): Adds a specified number of users and bots to a channel.
- [ChannelFlowCallback](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_ChannelFlowCallback.html): Calls back Amazon Chime SDK messaging with a processing response message.
- [CreateChannel](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_CreateChannel.html): Creates a channel to which you can add users and send messages.
- [CreateChannelBan](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_CreateChannelBan.html): Permanently bans a member from a channel.
- [CreateChannelFlow](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_CreateChannelFlow.html): Creates a channel flow, a container for processors.
- [CreateChannelMembership](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_CreateChannelMembership.html): Adds a member to a channel.
- [CreateChannelModerator](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_CreateChannelModerator.html): Creates a new ChannelModerator.
- [DeleteChannel](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_DeleteChannel.html): Immediately makes a channel and its memberships inaccessible and marks them for deletion.
- [DeleteChannelBan](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_DeleteChannelBan.html): Removes a member from a channel's ban list.
- [DeleteChannelFlow](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_DeleteChannelFlow.html): Deletes a channel flow, an irreversible process.
- [DeleteChannelMembership](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_DeleteChannelMembership.html): Removes a member from a channel.
- [DeleteChannelMessage](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_DeleteChannelMessage.html): Deletes a channel message.
- [DeleteChannelModerator](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_DeleteChannelModerator.html): Deletes a channel moderator.
- [DeleteMessagingStreamingConfigurations](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_DeleteMessagingStreamingConfigurations.html): Deletes the streaming configurations for an AppInstance.
- [DescribeChannel](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_DescribeChannel.html): Returns the full details of a channel in an Amazon Chime AppInstance.
- [DescribeChannelBan](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_DescribeChannelBan.html): Returns the full details of a channel ban.
- [DescribeChannelFlow](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_DescribeChannelFlow.html): Returns the full details of a channel flow in an Amazon Chime AppInstance.
- [DescribeChannelMembership](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_DescribeChannelMembership.html): Returns the full details of a user's channel membership.
- [DescribeChannelMembershipForAppInstanceUser](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_DescribeChannelMembershipForAppInstanceUser.html): Returns the details of a channel based on the membership of the specified AppInstanceUser or AppInstanceBot.
- [DescribeChannelModeratedByAppInstanceUser](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_DescribeChannelModeratedByAppInstanceUser.html): Returns the full details of a channel moderated by the specified AppInstanceUser or AppInstanceBot.
- [DescribeChannelModerator](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_DescribeChannelModerator.html): Returns the full details of a single ChannelModerator.
- [DisassociateChannelFlow](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_DisassociateChannelFlow.html): Disassociates a channel flow from all its channels.
- [GetChannelMembershipPreferences](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_GetChannelMembershipPreferences.html): Gets the membership preferences of an AppInstanceUser or AppInstanceBot for the specified channel.
- [GetChannelMessage](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_GetChannelMessage.html): Gets the full details of a channel message.
- [GetChannelMessageStatus](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_GetChannelMessageStatus.html): Gets message status for a specified messageId.
- [GetMessagingSessionEndpoint](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_GetMessagingSessionEndpoint.html): The details of the endpoint for the messaging session.
- [GetMessagingStreamingConfigurations](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_GetMessagingStreamingConfigurations.html): Retrieves the data streaming configuration for an AppInstance.
- [ListChannelBans](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_ListChannelBans.html): Lists all the users and bots banned from a particular channel.
- [ListChannelFlows](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_ListChannelFlows.html): Returns a paginated lists of all the channel flows created under a single Chime.
- [ListChannelMemberships](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_ListChannelMemberships.html): Lists all channel memberships in a channel.
- [ListChannelMembershipsForAppInstanceUser](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_ListChannelMembershipsForAppInstanceUser.html): Lists all channels that an AppInstanceUser or AppInstanceBot is a part of.
- [ListChannelMessages](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_ListChannelMessages.html): List all the messages in a channel.
- [ListChannelModerators](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_ListChannelModerators.html): Lists all the moderators for a channel.
- [ListChannels](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_ListChannels.html): Lists all Channels created under a single Chime App as a paginated list.
- [ListChannelsAssociatedWithChannelFlow](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_ListChannelsAssociatedWithChannelFlow.html): Lists all channels associated with a specified channel flow.
- [ListChannelsModeratedByAppInstanceUser](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_ListChannelsModeratedByAppInstanceUser.html): A list of the channels moderated by an AppInstanceUser.
- [ListSubChannels](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_ListSubChannels.html): Lists all the SubChannels in an elastic channel when given a channel ID.
- [ListTagsForResource](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_ListTagsForResource.html): Lists the tags applied to an Amazon Chime SDK messaging resource.
- [PutChannelExpirationSettings](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_PutChannelExpirationSettings.html): Sets the number of days before the channel is automatically deleted.
- [PutChannelMembershipPreferences](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_PutChannelMembershipPreferences.html): Sets the membership preferences of an AppInstanceUser or AppInstanceBot for the specified channel.
- [PutMessagingStreamingConfigurations](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_PutMessagingStreamingConfigurations.html): Sets the data streaming configuration for an AppInstance.
- [RedactChannelMessage](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_RedactChannelMessage.html): Redacts message content and metadata.
- [SearchChannels](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_SearchChannels.html): Allows the ChimeBearer to search channels by channel members.
- [SendChannelMessage](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_SendChannelMessage.html): Sends a message to a particular channel that the member is a part of.
- [TagResource](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_TagResource.html): Applies the specified tags to the specified Amazon Chime SDK messaging resource.
- [UntagResource](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_UntagResource.html): Removes the specified tags from the specified Amazon Chime SDK messaging resource.
- [UpdateChannel](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_UpdateChannel.html): Update a channel's attributes.
- [UpdateChannelFlow](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_UpdateChannelFlow.html): Updates channel flow attributes.
- [UpdateChannelMessage](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_UpdateChannelMessage.html): Updates the content of a message.
- [UpdateChannelReadMarker](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_UpdateChannelReadMarker.html): The details of the time when a user last read messages in a channel.

### [Amazon Chime SDK Voice](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_Operations_Amazon_Chime_SDK_Voice.html)

The following actions are supported by Amazon Chime SDK Voice:

- [AssociatePhoneNumbersWithVoiceConnector](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_AssociatePhoneNumbersWithVoiceConnector.html): Associates phone numbers with the specified Amazon Chime SDK Voice Connector.
- [AssociatePhoneNumbersWithVoiceConnectorGroup](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_AssociatePhoneNumbersWithVoiceConnectorGroup.html): Associates phone numbers with the specified Amazon Chime SDK Voice Connector group.
- [BatchDeletePhoneNumber](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_BatchDeletePhoneNumber.html): Moves phone numbers into the Deletion queue.
- [BatchUpdatePhoneNumber](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_BatchUpdatePhoneNumber.html): Updates phone number product types, calling names, or phone number names.
- [CreatePhoneNumberOrder](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_CreatePhoneNumberOrder.html): Creates an order for phone numbers to be provisioned.
- [CreateProxySession](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_CreateProxySession.html): Creates a proxy session for the specified Amazon Chime SDK Voice Connector for the specified participant phone numbers.
- [CreateSipMediaApplication](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_CreateSipMediaApplication.html): Creates a SIP media application.
- [CreateSipMediaApplicationCall](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_CreateSipMediaApplicationCall.html): Creates an outbound call to a phone number from the phone number specified in the request, and it invokes the endpoint of the specified sipMediaApplicationId.
- [CreateSipRule](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_CreateSipRule.html): Creates a SIP rule, which can be used to run a SIP media application as a target for a specific trigger type.
- [CreateVoiceConnector](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_CreateVoiceConnector.html): Creates an Amazon Chime SDK Voice Connector.
- [CreateVoiceConnectorGroup](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_CreateVoiceConnectorGroup.html): Creates an Amazon Chime SDK Voice Connector group under the administrator's AWS account.
- [CreateVoiceProfile](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_CreateVoiceProfile.html): Creates a voice profile, which consists of an enrolled user and their latest voice print.
- [CreateVoiceProfileDomain](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_CreateVoiceProfileDomain.html): Creates a voice profile domain, a collection of voice profiles, their voice prints, and encrypted enrollment audio.
- [DeletePhoneNumber](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_DeletePhoneNumber.html): Moves the specified phone number into the Deletion queue.
- [DeleteProxySession](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_DeleteProxySession.html): Deletes the specified proxy session from the specified Amazon Chime SDK Voice Connector.
- [DeleteSipMediaApplication](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_DeleteSipMediaApplication.html): Deletes a SIP media application.
- [DeleteSipRule](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_DeleteSipRule.html): Deletes a SIP rule.
- [DeleteVoiceConnector](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_DeleteVoiceConnector.html): Deletes an Amazon Chime SDK Voice Connector.
- [DeleteVoiceConnectorEmergencyCallingConfiguration](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_DeleteVoiceConnectorEmergencyCallingConfiguration.html): Deletes the emergency calling details from the specified Amazon Chime SDK Voice Connector.
- [DeleteVoiceConnectorExternalSystemsConfiguration](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_DeleteVoiceConnectorExternalSystemsConfiguration.html): Deletes the external systems configuration for a Voice Connector.
- [DeleteVoiceConnectorGroup](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_DeleteVoiceConnectorGroup.html): Deletes an Amazon Chime SDK Voice Connector group.
- [DeleteVoiceConnectorOrigination](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_DeleteVoiceConnectorOrigination.html): Deletes the origination settings for the specified Amazon Chime SDK Voice Connector.
- [DeleteVoiceConnectorProxy](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_DeleteVoiceConnectorProxy.html): Deletes the proxy configuration from the specified Amazon Chime SDK Voice Connector.
- [DeleteVoiceConnectorStreamingConfiguration](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_DeleteVoiceConnectorStreamingConfiguration.html): Deletes a Voice Connector's streaming configuration.
- [DeleteVoiceConnectorTermination](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_DeleteVoiceConnectorTermination.html): Deletes the termination settings for the specified Amazon Chime SDK Voice Connector.
- [DeleteVoiceConnectorTerminationCredentials](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_DeleteVoiceConnectorTerminationCredentials.html): Deletes the specified SIP credentials used by your equipment to authenticate during call termination.
- [DeleteVoiceProfile](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_DeleteVoiceProfile.html): Deletes a voice profile, including its voice print and enrollment data.
- [DeleteVoiceProfileDomain](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_DeleteVoiceProfileDomain.html): Deletes all voice profiles in the domain.
- [DisassociatePhoneNumbersFromVoiceConnector](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_DisassociatePhoneNumbersFromVoiceConnector.html): Disassociates the specified phone numbers from the specified Amazon Chime SDK Voice Connector.
- [DisassociatePhoneNumbersFromVoiceConnectorGroup](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_DisassociatePhoneNumbersFromVoiceConnectorGroup.html): Disassociates the specified phone numbers from the specified Amazon Chime SDK Voice Connector group.
- [GetGlobalSettings](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_GetGlobalSettings.html): Retrieves the global settings for the Amazon Chime SDK Voice Connectors in an AWS account.
- [GetPhoneNumber](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_GetPhoneNumber.html): Retrieves details for the specified phone number ID, such as associations, capabilities, and product type.
- [GetPhoneNumberOrder](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_GetPhoneNumberOrder.html): Retrieves details for the specified phone number order, such as the order creation timestamp, phone numbers in E.164 format, product type, and order status.
- [GetPhoneNumberSettings](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_GetPhoneNumberSettings.html): Retrieves the phone number settings for the administrator's AWS account, such as the default outbound calling name.
- [GetProxySession](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_GetProxySession.html): Retrieves the specified proxy session details for the specified Amazon Chime SDK Voice Connector.
- [GetSipMediaApplication](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_GetSipMediaApplication.html): Retrieves the information for a SIP media application, including name, AWS Region, and endpoints.
- [GetSipMediaApplicationAlexaSkillConfiguration](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_GetSipMediaApplicationAlexaSkillConfiguration.html): Gets the Alexa Skill configuration for the SIP media application.
- [GetSipMediaApplicationLoggingConfiguration](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_GetSipMediaApplicationLoggingConfiguration.html): Retrieves the logging configuration for the specified SIP media application.
- [GetSipRule](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_GetSipRule.html): Retrieves the details of a SIP rule, such as the rule ID, name, triggers, and target endpoints.
- [GetSpeakerSearchTask](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_GetSpeakerSearchTask.html): Retrieves the details of the specified speaker search task.
- [GetVoiceConnector](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_GetVoiceConnector.html): Retrieves details for the specified Amazon Chime SDK Voice Connector, such as timestamps,name, outbound host, and encryption requirements.
- [GetVoiceConnectorEmergencyCallingConfiguration](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_GetVoiceConnectorEmergencyCallingConfiguration.html): Retrieves the emergency calling configuration details for the specified Voice Connector.
- [GetVoiceConnectorExternalSystemsConfiguration](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_GetVoiceConnectorExternalSystemsConfiguration.html): Gets information about an external systems configuration for a Voice Connector.
- [GetVoiceConnectorGroup](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_GetVoiceConnectorGroup.html): Retrieves details for the specified Amazon Chime SDK Voice Connector group, such as timestamps,name, and associated VoiceConnectorItems.
- [GetVoiceConnectorLoggingConfiguration](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_GetVoiceConnectorLoggingConfiguration.html): Retrieves the logging configuration settings for the specified Voice Connector.
- [GetVoiceConnectorOrigination](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_GetVoiceConnectorOrigination.html): Retrieves the origination settings for the specified Voice Connector.
- [GetVoiceConnectorProxy](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_GetVoiceConnectorProxy.html): Retrieves the proxy configuration details for the specified Amazon Chime SDK Voice Connector.
- [GetVoiceConnectorStreamingConfiguration](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_GetVoiceConnectorStreamingConfiguration.html): Retrieves the streaming configuration details for the specified Amazon Chime SDK Voice Connector.
- [GetVoiceConnectorTermination](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_GetVoiceConnectorTermination.html): Retrieves the termination setting details for the specified Voice Connector.
- [GetVoiceConnectorTerminationHealth](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_GetVoiceConnectorTerminationHealth.html): Retrieves information about the last time a SIP OPTIONS ping was received from your SIP infrastructure for the specified Amazon Chime SDK Voice Connector.
- [GetVoiceProfile](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_GetVoiceProfile.html): Retrieves the details of the specified voice profile.
- [GetVoiceProfileDomain](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_GetVoiceProfileDomain.html): Retrieves the details of the specified voice profile domain.
- [GetVoiceToneAnalysisTask](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_GetVoiceToneAnalysisTask.html): Retrieves the details of a voice tone analysis task.
- [ListAvailableVoiceConnectorRegions](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_ListAvailableVoiceConnectorRegions.html): Lists the available AWS Regions in which you can create an Amazon Chime SDK Voice Connector.
- [ListPhoneNumberOrders](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_ListPhoneNumberOrders.html): Lists the phone numbers for an administrator's Amazon Chime SDK account.
- [ListPhoneNumbers](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_ListPhoneNumbers.html): Lists the phone numbers for the specified Amazon Chime SDK account, Amazon Chime SDK user, Amazon Chime SDK Voice Connector, or Amazon Chime SDK Voice Connector group.
- [ListProxySessions](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_ListProxySessions.html): Lists the proxy sessions for the specified Amazon Chime SDK Voice Connector.
- [ListSipMediaApplications](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_ListSipMediaApplications.html): Lists the SIP media applications under the administrator's AWS account.
- [ListSipRules](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_ListSipRules.html): Lists the SIP rules under the administrator's AWS account.
- [ListSupportedPhoneNumberCountries](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_ListSupportedPhoneNumberCountries.html): Lists the countries that you can order phone numbers from.
- [ListTagsForResource](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_ListTagsForResource.html): Returns a list of the tags in a given resource.
- [ListVoiceConnectorGroups](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_ListVoiceConnectorGroups.html): Lists the Amazon Chime SDK Voice Connector groups in the administrator's AWS account.
- [ListVoiceConnectors](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_ListVoiceConnectors.html): Lists the Amazon Chime SDK Voice Connectors in the administrators AWS account.
- [ListVoiceConnectorTerminationCredentials](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_ListVoiceConnectorTerminationCredentials.html): Lists the SIP credentials for the specified Amazon Chime SDK Voice Connector.
- [ListVoiceProfileDomains](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_ListVoiceProfileDomains.html): Lists the specified voice profile domains in the administrator's AWS account.
- [ListVoiceProfiles](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_ListVoiceProfiles.html): Lists the voice profiles in a voice profile domain.
- [PutSipMediaApplicationAlexaSkillConfiguration](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_PutSipMediaApplicationAlexaSkillConfiguration.html): Updates the Alexa Skill configuration for the SIP media application.
- [PutSipMediaApplicationLoggingConfiguration](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_PutSipMediaApplicationLoggingConfiguration.html): Updates the logging configuration for the specified SIP media application.
- [PutVoiceConnectorEmergencyCallingConfiguration](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_PutVoiceConnectorEmergencyCallingConfiguration.html): Updates a Voice Connector's emergency calling configuration.
- [PutVoiceConnectorExternalSystemsConfiguration](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_PutVoiceConnectorExternalSystemsConfiguration.html): Adds an external systems configuration to a Voice Connector.
- [PutVoiceConnectorLoggingConfiguration](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_PutVoiceConnectorLoggingConfiguration.html): Updates a Voice Connector's logging configuration.
- [PutVoiceConnectorOrigination](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_PutVoiceConnectorOrigination.html): Updates a Voice Connector's origination settings.
- [PutVoiceConnectorProxy](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_PutVoiceConnectorProxy.html): Puts the specified proxy configuration to the specified Amazon Chime SDK Voice Connector.
- [PutVoiceConnectorStreamingConfiguration](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_PutVoiceConnectorStreamingConfiguration.html): Updates a Voice Connector's streaming configuration settings.
- [PutVoiceConnectorTermination](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_PutVoiceConnectorTermination.html): Updates a Voice Connector's termination settings.
- [PutVoiceConnectorTerminationCredentials](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_PutVoiceConnectorTerminationCredentials.html): Updates a Voice Connector's termination credentials.
- [RestorePhoneNumber](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_RestorePhoneNumber.html): Restores a deleted phone number.
- [SearchAvailablePhoneNumbers](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_SearchAvailablePhoneNumbers.html): Searches the provisioned phone numbers in an organization.
- [StartSpeakerSearchTask](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_StartSpeakerSearchTask.html): Starts a speaker search task.
- [StartVoiceToneAnalysisTask](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_StartVoiceToneAnalysisTask.html): Starts a voice tone analysis task.
- [StopSpeakerSearchTask](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_StopSpeakerSearchTask.html): Stops a speaker search task.
- [StopVoiceToneAnalysisTask](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_StopVoiceToneAnalysisTask.html): Stops a voice tone analysis task.
- [TagResource](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_TagResource.html): Adds a tag to the specified resource.
- [UntagResource](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_UntagResource.html): Removes tags from a resource.
- [UpdateGlobalSettings](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_UpdateGlobalSettings.html): Updates global settings for the Amazon Chime SDK Voice Connectors in an AWS account.
- [UpdatePhoneNumber](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_UpdatePhoneNumber.html): Updates phone number details, such as product type, calling name, or phone number name for the specified phone number ID.
- [UpdatePhoneNumberSettings](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_UpdatePhoneNumberSettings.html): Updates the phone number settings for the administrator's AWS account, such as the default outbound calling name.
- [UpdateProxySession](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_UpdateProxySession.html): Updates the specified proxy session details, such as voice or SMS capabilities.
- [UpdateSipMediaApplication](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_UpdateSipMediaApplication.html): Updates the details of the specified SIP media application.
- [UpdateSipMediaApplicationCall](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_UpdateSipMediaApplicationCall.html): Invokes the AWS Lambda function associated with the SIP media application and transaction ID in an update request.
- [UpdateSipRule](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_UpdateSipRule.html): Updates the details of the specified SIP rule.
- [UpdateVoiceConnector](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_UpdateVoiceConnector.html): Updates the details for the specified Amazon Chime SDK Voice Connector.
- [UpdateVoiceConnectorGroup](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_UpdateVoiceConnectorGroup.html): Updates the settings for the specified Amazon Chime SDK Voice Connector group.
- [UpdateVoiceProfile](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_UpdateVoiceProfile.html): Updates the specified voice profileâs voice print and refreshes its expiration timestamp.
- [UpdateVoiceProfileDomain](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_UpdateVoiceProfileDomain.html): Updates the settings for the specified voice profile domain.
- [ValidateE911Address](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_ValidateE911Address.html): Validates an address to be used for 911 calls made with Amazon Chime SDK Voice Connectors.


## [Data Types](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_Types.html)

### [Amazon Chime SDK Identity](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_Types_Amazon_Chime_SDK_Identity.html)

The following data types are supported by Amazon Chime SDK Identity:

- [AppInstance](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_AppInstance.html): The details of an AppInstance, an instance of an Amazon Chime SDK messaging application.
- [AppInstanceAdmin](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_AppInstanceAdmin.html): The name and ARN of the admin for the AppInstance.
- [AppInstanceAdminSummary](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_AppInstanceAdminSummary.html): Summary of the details of an AppInstanceAdmin.
- [AppInstanceBot](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_AppInstanceBot.html): An Amazon Lex V2 chat bot created under an AppInstance.
- [AppInstanceBotSummary](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_AppInstanceBotSummary.html): High-level information about an AppInstanceBot.
- [AppInstanceRetentionSettings](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_AppInstanceRetentionSettings.html): The details of the data-retention settings for an AppInstance.
- [AppInstanceSummary](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_AppInstanceSummary.html): Summary of the data for an AppInstance.
- [AppInstanceUser](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_AppInstanceUser.html): The details of an AppInstanceUser.
- [AppInstanceUserEndpoint](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_AppInstanceUserEndpoint.html): An endpoint under an Amazon Chime AppInstanceUser that receives messages for a user.
- [AppInstanceUserEndpointSummary](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_AppInstanceUserEndpointSummary.html): Summary of the details of an AppInstanceUserEndpoint.
- [AppInstanceUserSummary](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_AppInstanceUserSummary.html): Summary of the details of an AppInstanceUser.
- [ChannelRetentionSettings](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_ChannelRetentionSettings.html): The details of the retention settings for a channel.
- [Configuration](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_Configuration.html): A structure that contains configuration data.
- [EndpointAttributes](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_EndpointAttributes.html): The attributes of an Endpoint.
- [EndpointState](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_EndpointState.html): A read-only field that represents the state of an AppInstanceUserEndpoint.
- [ExpirationSettings](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_ExpirationSettings.html): Determines the interval after which an AppInstanceUser is automatically deleted.
- [Identity](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_Identity.html): The details of a user or bot.
- [InvokedBy](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_InvokedBy.html): Specifies the type of message that triggers a bot.
- [LexConfiguration](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_LexConfiguration.html): The configuration for an Amazon Lex V2 bot.
- [Tag](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_Tag.html): A tag object containing a key-value pair.

### [Amazon Chime SDK Media Pipelines](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_Types_Amazon_Chime_SDK_Media_Pipelines.html)

The following data types are supported by Amazon Chime SDK Media Pipelines:

- [ActiveSpeakerOnlyConfiguration](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_ActiveSpeakerOnlyConfiguration.html): Defines the configuration for an ActiveSpeakerOnly video tile.
- [AmazonTranscribeCallAnalyticsProcessorConfiguration](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_AmazonTranscribeCallAnalyticsProcessorConfiguration.html): A structure that contains the configuration settings for an Amazon Transcribe call analytics processor.
- [AmazonTranscribeProcessorConfiguration](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_AmazonTranscribeProcessorConfiguration.html): A structure that contains the configuration settings for an Amazon Transcribe processor.
- [ArtifactsConcatenationConfiguration](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_ArtifactsConcatenationConfiguration.html): The configuration for the artifacts concatenation.
- [ArtifactsConfiguration](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_ArtifactsConfiguration.html): The configuration for the artifacts.
- [AudioArtifactsConfiguration](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_AudioArtifactsConfiguration.html): The audio artifact configuration object.
- [AudioConcatenationConfiguration](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_AudioConcatenationConfiguration.html): The audio artifact concatenation configuration object.
- [ChannelDefinition](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_ChannelDefinition.html): Defines an audio channel in a Kinesis video stream.
- [ChimeSdkMeetingConcatenationConfiguration](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_ChimeSdkMeetingConcatenationConfiguration.html): The configuration object of the Amazon Chime SDK meeting concatenation for a specified media pipeline.
- [ChimeSdkMeetingConfiguration](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_ChimeSdkMeetingConfiguration.html): The configuration object of the Amazon Chime SDK meeting for a specified media pipeline.
- [ChimeSdkMeetingLiveConnectorConfiguration](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_ChimeSdkMeetingLiveConnectorConfiguration.html): The media pipeline's configuration object.
- [CompositedVideoArtifactsConfiguration](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_CompositedVideoArtifactsConfiguration.html): Specifies the configuration for compositing video artifacts.
- [CompositedVideoConcatenationConfiguration](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_CompositedVideoConcatenationConfiguration.html): The composited video configuration object for a specified media pipeline.
- [ConcatenationSink](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_ConcatenationSink.html): The data sink of the configuration object.
- [ConcatenationSource](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_ConcatenationSource.html): The source type and media pipeline configuration settings in a configuration object.
- [ContentArtifactsConfiguration](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_ContentArtifactsConfiguration.html): The content artifact object.
- [ContentConcatenationConfiguration](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_ContentConcatenationConfiguration.html): The composited content configuration object for a specified media pipeline.
- [DataChannelConcatenationConfiguration](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_DataChannelConcatenationConfiguration.html): The content configuration object's data channel.
- [FragmentSelector](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_FragmentSelector.html): Describes the timestamp range and timestamp origin of a range of fragments.
- [GridViewConfiguration](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_GridViewConfiguration.html): Specifies the type of grid layout.
- [HorizontalLayoutConfiguration](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_HorizontalLayoutConfiguration.html): Defines the configuration settings for the horizontal layout.
- [IssueDetectionConfiguration](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_IssueDetectionConfiguration.html): A structure that contains the configuration settings for an issue detection task.
- [KeywordMatchConfiguration](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_KeywordMatchConfiguration.html): A structure that contains the settings for a keyword match task.
- [KinesisDataStreamSinkConfiguration](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_KinesisDataStreamSinkConfiguration.html): A structure that contains the configuration settings for a Kinesis Data Stream sink.
- [KinesisVideoStreamConfiguration](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_KinesisVideoStreamConfiguration.html): The configuration of an Kinesis video stream.
- [KinesisVideoStreamConfigurationUpdate](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_KinesisVideoStreamConfigurationUpdate.html): The updated Kinesis video stream configuration object.
- [KinesisVideoStreamPoolConfiguration](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_KinesisVideoStreamPoolConfiguration.html): The video stream pool configuration object.
- [KinesisVideoStreamPoolSummary](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_KinesisVideoStreamPoolSummary.html): A summary of the Kinesis video stream pool.
- [KinesisVideoStreamRecordingSourceRuntimeConfiguration](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_KinesisVideoStreamRecordingSourceRuntimeConfiguration.html): A structure that contains the runtime settings for recording a Kinesis video stream.
- [KinesisVideoStreamSourceRuntimeConfiguration](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_KinesisVideoStreamSourceRuntimeConfiguration.html): The runtime configuration settings for the Kinesis video stream source.
- [KinesisVideoStreamSourceTaskConfiguration](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_KinesisVideoStreamSourceTaskConfiguration.html): The task configuration settings for the Kinesis video stream source.
- [LambdaFunctionSinkConfiguration](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_LambdaFunctionSinkConfiguration.html): A structure that contains the configuration settings for an AWS Lambda function's data sink.
- [LiveConnectorRTMPConfiguration](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_LiveConnectorRTMPConfiguration.html): The media pipeline's RTMP configuration object.
- [LiveConnectorSinkConfiguration](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_LiveConnectorSinkConfiguration.html): The media pipeline's sink configuration settings.
- [LiveConnectorSourceConfiguration](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_LiveConnectorSourceConfiguration.html): The data source configuration object of a streaming media pipeline.
- [MediaCapturePipeline](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_MediaCapturePipeline.html): A media pipeline object consisting of an ID, source type, source ARN, a sink type, a sink ARN, and a configuration object.
- [MediaCapturePipelineSourceConfiguration](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_MediaCapturePipelineSourceConfiguration.html): The source configuration object of a media capture pipeline.
- [MediaCapturePipelineSummary](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_MediaCapturePipelineSummary.html): The summary data of a media capture pipeline.
- [MediaConcatenationPipeline](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_MediaConcatenationPipeline.html): Concatenates audio and video data from one or more data streams.
- [MediaInsightsPipeline](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_MediaInsightsPipeline.html): A media pipeline that streams call analytics data.
- [MediaInsightsPipelineConfiguration](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_MediaInsightsPipelineConfiguration.html): A structure that contains the configuration settings for a media insights pipeline.
- [MediaInsightsPipelineConfigurationElement](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_MediaInsightsPipelineConfigurationElement.html): An element in a media insights pipeline configuration.
- [MediaInsightsPipelineConfigurationSummary](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_MediaInsightsPipelineConfigurationSummary.html): A summary of the media insights pipeline configuration.
- [MediaInsightsPipelineElementStatus](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_MediaInsightsPipelineElementStatus.html): The status of the pipeline element.
- [MediaLiveConnectorPipeline](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_MediaLiveConnectorPipeline.html): The connector pipeline.
- [MediaPipeline](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_MediaPipeline.html): A pipeline consisting of a media capture, media concatenation, or live-streaming pipeline.
- [MediaPipelineSummary](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_MediaPipelineSummary.html): The summary of the media pipeline.
- [MediaStreamPipeline](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_MediaStreamPipeline.html): Structure that contains the settings for a media stream pipeline.
- [MediaStreamSink](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_MediaStreamSink.html): Structure that contains the settings for a media stream sink.
- [MediaStreamSource](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_MediaStreamSource.html): Structure that contains the settings for media stream sources.
- [MeetingEventsConcatenationConfiguration](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_MeetingEventsConcatenationConfiguration.html): The configuration object for an event concatenation pipeline.
- [PostCallAnalyticsSettings](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_PostCallAnalyticsSettings.html): Allows you to specify additional settings for your Call Analytics post-call request, including output locations for your redacted transcript, which IAM role to use, and which encryption key to use.
- [PresenterOnlyConfiguration](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_PresenterOnlyConfiguration.html): Defines the configuration for a presenter-only video tile.
- [RealTimeAlertConfiguration](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_RealTimeAlertConfiguration.html): A structure that contains the configuration settings for real-time alerts.
- [RealTimeAlertRule](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_RealTimeAlertRule.html): Specifies the words or phrases that trigger an alert.
- [RecordingStreamConfiguration](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_RecordingStreamConfiguration.html): A structure that holds the settings for recording media.
- [S3BucketSinkConfiguration](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_S3BucketSinkConfiguration.html): The configuration settings for the S3 bucket.
- [S3RecordingSinkConfiguration](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_S3RecordingSinkConfiguration.html): The structure that holds the settings for transmitting media to the Amazon S3 bucket.
- [S3RecordingSinkRuntimeConfiguration](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_S3RecordingSinkRuntimeConfiguration.html): A structure that holds the settings for transmitting media files to the Amazon S3 bucket.
- [SelectedVideoStreams](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_SelectedVideoStreams.html): The video streams for a specified media pipeline.
- [SentimentConfiguration](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_SentimentConfiguration.html): A structure that contains the configuration settings for a sentiment analysis task.
- [SnsTopicSinkConfiguration](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_SnsTopicSinkConfiguration.html): The configuration settings for the SNS topic sink.
- [SourceConfiguration](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_SourceConfiguration.html): Source configuration for a specified media pipeline.
- [SpeakerSearchTask](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_SpeakerSearchTask.html): A representation of an asynchronous request to perform speaker search analysis on a media insights pipeline.
- [SqsQueueSinkConfiguration](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_SqsQueueSinkConfiguration.html): The configuration settings for the SQS sink.
- [SseAwsKeyManagementParams](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_SseAwsKeyManagementParams.html): Contains server side encryption parameters to be used by media capture pipeline.
- [StreamChannelDefinition](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_StreamChannelDefinition.html): Defines a streaming channel.
- [StreamConfiguration](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_StreamConfiguration.html): The configuration settings for a stream.
- [Tag](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_Tag.html): A key/value pair that grants users access to meeting resources.
- [TimestampRange](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_TimestampRange.html): The range of timestamps to return.
- [TranscriptionMessagesConcatenationConfiguration](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_TranscriptionMessagesConcatenationConfiguration.html): The configuration object for concatenating transcription messages.
- [VerticalLayoutConfiguration](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_VerticalLayoutConfiguration.html): Defines the configuration settings for a vertical layout.
- [VideoArtifactsConfiguration](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_VideoArtifactsConfiguration.html): The video artifact configuration object.
- [VideoAttribute](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_VideoAttribute.html): Defines the settings for a video tile.
- [VideoConcatenationConfiguration](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_VideoConcatenationConfiguration.html): The configuration object of a video concatenation pipeline.
- [VoiceAnalyticsProcessorConfiguration](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_VoiceAnalyticsProcessorConfiguration.html): The configuration settings for a voice analytics processor.
- [VoiceEnhancementSinkConfiguration](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_VoiceEnhancementSinkConfiguration.html): A static structure that contains the configuration data for a VoiceEnhancementSinkConfiguration element.
- [VoiceToneAnalysisTask](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_VoiceToneAnalysisTask.html): A representation of an asynchronous request to perform voice tone analysis on a media insights pipeline.

### [Amazon Chime SDK Meetings](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_Types_Amazon_Chime_SDK_Meetings.html)

The following data types are supported by Amazon Chime SDK Meetings:

- [Attendee](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_Attendee.html): An Amazon Chime SDK meeting attendee.
- [AttendeeCapabilities](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_AttendeeCapabilities.html): The media capabilities of an attendee: audio, video, or content.
- [AttendeeFeatures](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_AttendeeFeatures.html): Lists the maximum number of attendees allowed into the meeting.
- [AttendeeIdItem](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_AttendeeIdItem.html): A structure that contains one or more attendee IDs.
- [AudioFeatures](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_AudioFeatures.html): An optional category of meeting features that contains audio-specific configurations, such as operating parameters for Amazon Voice Focus.
- [ContentFeatures](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_ContentFeatures.html): Lists the content (screen share) features for the meeting.
- [CreateAttendeeError](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_CreateAttendeeError.html): The list of errors returned when errors are encountered during the BatchCreateAttendee and CreateAttendee actions.
- [CreateAttendeeRequestItem](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_CreateAttendeeRequestItem.html): The Amazon Chime SDK attendee fields to create, used with the BatchCreateAttendee action.
- [EngineTranscribeMedicalSettings](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_EngineTranscribeMedicalSettings.html): Settings specific to the Amazon Transcribe Medical engine.
- [EngineTranscribeSettings](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_EngineTranscribeSettings.html): Settings specific for Amazon Transcribe as the live transcription engine.
- [MediaPlacement](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_MediaPlacement.html): A set of endpoints used by clients to connect to the media service group for an Amazon Chime SDK meeting.
- [Meeting](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_Meeting.html): A meeting created using the Amazon Chime SDK.
- [MeetingFeaturesConfiguration](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_MeetingFeaturesConfiguration.html): The configuration settings of the features available to a meeting.
- [NotificationsConfiguration](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_NotificationsConfiguration.html): The configuration for resource targets to receive notifications when meeting and attendee events occur.
- [Tag](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_Tag.html): A key-value pair that you define.
- [TranscriptionConfiguration](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_TranscriptionConfiguration.html): The configuration for the current transcription operation.
- [VideoFeatures](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_VideoFeatures.html): The video features set for the meeting.

### [Amazon Chime SDK Messaging](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_Types_Amazon_Chime_SDK_Messaging.html)

The following data types are supported by Amazon Chime SDK Messaging:

- [AppInstanceUserMembershipSummary](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_AppInstanceUserMembershipSummary.html): Summary of the membership details of an AppInstanceUser.
- [BatchChannelMemberships](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_BatchChannelMemberships.html): The membership information, including member ARNs, the channel ARN, and membership types.
- [BatchCreateChannelMembershipError](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_BatchCreateChannelMembershipError.html): A list of failed member ARNs, error codes, and error messages.
- [Channel](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_Channel.html): The details of a channel.
- [ChannelAssociatedWithFlowSummary](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_ChannelAssociatedWithFlowSummary.html): Summary of details of a channel associated with channel flow.
- [ChannelBan](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_ChannelBan.html): The details of a channel ban.
- [ChannelBanSummary](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_ChannelBanSummary.html): Summary of the details of a ChannelBan.
- [ChannelFlow](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_ChannelFlow.html): The details of a channel flow.
- [ChannelFlowSummary](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_ChannelFlowSummary.html): Summary of details of a channel flow.
- [ChannelMembership](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_ChannelMembership.html): The details of a channel member.
- [ChannelMembershipForAppInstanceUserSummary](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_ChannelMembershipForAppInstanceUserSummary.html): Summary of the channel membership details of an AppInstanceUser.
- [ChannelMembershipPreferences](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_ChannelMembershipPreferences.html): The channel membership preferences for an AppInstanceUser.
- [ChannelMembershipSummary](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_ChannelMembershipSummary.html): Summary of the details of a ChannelMembership.
- [ChannelMessage](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_ChannelMessage.html): The details of a message in a channel.
- [ChannelMessageCallback](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_ChannelMessageCallback.html): Stores information about a callback.
- [ChannelMessageStatusStructure](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_ChannelMessageStatusStructure.html): Stores information about a message status.
- [ChannelMessageSummary](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_ChannelMessageSummary.html): Summary of the messages in a Channel.
- [ChannelModeratedByAppInstanceUserSummary](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_ChannelModeratedByAppInstanceUserSummary.html): Summary of the details of a moderated channel.
- [ChannelModerator](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_ChannelModerator.html): The details of a channel moderator.
- [ChannelModeratorSummary](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_ChannelModeratorSummary.html): Summary of the details of a ChannelModerator.
- [ChannelSummary](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_ChannelSummary.html): Summary of the details of a Channel.
- [ElasticChannelConfiguration](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_ElasticChannelConfiguration.html): The attributes required to configure and create an elastic channel.
- [ExpirationSettings](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_ExpirationSettings.html): Settings that control the interval after which a channel is deleted.
- [Identity](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_Identity.html): The details of a user or bot.
- [LambdaConfiguration](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_LambdaConfiguration.html): Stores metadata about a Lambda processor.
- [MessageAttributeValue](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_MessageAttributeValue.html): A list of message attribute values.
- [MessagingSessionEndpoint](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_MessagingSessionEndpoint.html): The websocket endpoint used to connect to Amazon Chime SDK messaging.
- [Processor](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_Processor.html): The information about a processor in a channel flow.
- [ProcessorConfiguration](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_ProcessorConfiguration.html): A processor's metadata.
- [PushNotificationConfiguration](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_PushNotificationConfiguration.html): The push notification configuration of the message.
- [PushNotificationPreferences](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_PushNotificationPreferences.html): The channel membership preferences for push notification.
- [SearchField](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_SearchField.html): A Field of the channel that you want to search.
- [StreamingConfiguration](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_StreamingConfiguration.html): The configuration for connecting a messaging stream to Amazon Kinesis.
- [SubChannelSummary](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_SubChannelSummary.html): Summary of the sub-channels associated with the elastic channel.
- [Tag](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_Tag.html): A tag object containing a key-value pair.
- [Target](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_Target.html): The target of a message, a sender, a user, or a bot.

### [Amazon Chime SDK Voice](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_Types_Amazon_Chime_SDK_Voice.html)

The following data types are supported by Amazon Chime SDK Voice:

- [Address](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_Address.html): A validated address.
- [CallDetails](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_CallDetails.html): The details of an Amazon Chime SDK Voice Connector call.
- [CandidateAddress](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_CandidateAddress.html): A suggested address.
- [Credential](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_Credential.html): The SIP credentials used to authenticate requests to an Amazon Chime SDK Voice Connector.
- [DNISEmergencyCallingConfiguration](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_DNISEmergencyCallingConfiguration.html): The Dialed Number Identification Service (DNIS) emergency calling configuration details associated with an Amazon Chime SDK Voice Connector's emergency calling configuration.
- [EmergencyCallingConfiguration](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_EmergencyCallingConfiguration.html): The emergency calling configuration details associated with an Amazon Chime SDK Voice Connector.
- [ExternalSystemsConfiguration](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_ExternalSystemsConfiguration.html): Contains information about an external systems configuration for a Voice Connector.
- [GeoMatchParams](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_GeoMatchParams.html): The country and area code for a proxy phone number in a proxy phone session.
- [LoggingConfiguration](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_LoggingConfiguration.html): The logging configuration associated with an Amazon Chime SDK Voice Connector.
- [MediaInsightsConfiguration](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_MediaInsightsConfiguration.html): The configuration for a call analytics task.
- [OrderedPhoneNumber](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_OrderedPhoneNumber.html): A phone number for which an order has been placed.
- [Origination](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_Origination.html): Origination settings enable your SIP hosts to receive inbound calls using your Amazon Chime SDK Voice Connector.
- [OriginationRoute](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_OriginationRoute.html): Origination routes define call distribution properties for your SIP hosts to receive inbound calls using an Amazon Chime SDK Voice Connector.
- [Participant](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_Participant.html): The phone number and proxy phone number for a participant in an Amazon Chime SDK Voice Connector proxy session.
- [PhoneNumber](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_PhoneNumber.html): A phone number used to call an Amazon Chime SDK Voice Connector.
- [PhoneNumberAssociation](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_PhoneNumberAssociation.html): The phone number associations, such as an Amazon Chime SDK account ID, user ID, Voice Connector ID, or Voice Connector group ID.
- [PhoneNumberCapabilities](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_PhoneNumberCapabilities.html): The phone number capabilities for Amazon Chime SDK phone numbers, such as enabled inbound and outbound calling, and text messaging.
- [PhoneNumberCountry](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_PhoneNumberCountry.html): The phone number's country.
- [PhoneNumberError](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_PhoneNumberError.html): If a phone number action fails for one or more of the phone numbers in a request, a list of the failed phone numbers is returned, along with error codes and error messages.
- [PhoneNumberOrder](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_PhoneNumberOrder.html): The details of an Amazon Chime SDK phone number order.
- [Proxy](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_Proxy.html): The proxy configuration for an Amazon Chime SDK Voice Connector.
- [ProxySession](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_ProxySession.html): The proxy session for an Amazon Chime SDK Voice Connector.
- [ServerSideEncryptionConfiguration](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_ServerSideEncryptionConfiguration.html): A structure that contains the configuration settings for server-side encryption.
- [SipMediaApplication](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_SipMediaApplication.html): The details of the SIP media application, including name and endpoints.
- [SipMediaApplicationAlexaSkillConfiguration](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_SipMediaApplicationAlexaSkillConfiguration.html): The Alexa Skill configuration of a SIP media application.
- [SipMediaApplicationCall](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_SipMediaApplicationCall.html): A Call instance for a SIP media application.
- [SipMediaApplicationEndpoint](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_SipMediaApplicationEndpoint.html): The endpoint assigned to a SIP media application.
- [SipMediaApplicationLoggingConfiguration](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_SipMediaApplicationLoggingConfiguration.html): The logging configuration of a SIP media application.
- [SipRule](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_SipRule.html): The details of a SIP rule, including name, triggers, and target applications.
- [SipRuleTargetApplication](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_SipRuleTargetApplication.html): A target SIP media application and other details, such as priority and AWS Region, to be specified in the SIP rule.
- [SpeakerSearchDetails](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_SpeakerSearchDetails.html): The details of a speaker search task.
- [SpeakerSearchResult](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_SpeakerSearchResult.html): The result of a speaker search analysis.
- [SpeakerSearchTask](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_SpeakerSearchTask.html): A representation of an asynchronous request to perform speaker search analysis on a Voice Connector call.
- [StreamingConfiguration](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_StreamingConfiguration.html): The streaming configuration associated with an Amazon Chime SDK Voice Connector.
- [StreamingNotificationTarget](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_StreamingNotificationTarget.html): The target recipient for a streaming configuration notification.
- [Tag](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_Tag.html): Describes a tag applied to a resource.
- [Termination](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_Termination.html): Termination settings enable SIP hosts to make outbound calls using an Amazon Chime SDK Voice Connector.
- [TerminationHealth](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_TerminationHealth.html): The termination health details, including the source IP address and timestamp of the last successful SIP OPTIONS message from your SIP infrastructure.
- [UpdatePhoneNumberRequestItem](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_UpdatePhoneNumberRequestItem.html): The phone number ID, product type, or calling name fields to update, used with the and actions.
- [VoiceConnector](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_VoiceConnector.html): The Amazon Chime SDK Voice Connector configuration, including outbound host name and encryption settings.
- [VoiceConnectorGroup](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_VoiceConnectorGroup.html): The Amazon Chime SDK Voice Connector group configuration, including associated Voice Connectors.
- [VoiceConnectorItem](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_VoiceConnectorItem.html): For Amazon Chime SDK Voice Connector groups, the Amazon Chime SDK Voice Connectors to which you route inbound calls.
- [VoiceConnectorSettings](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_VoiceConnectorSettings.html): The Amazon Chime SDK Voice Connector settings.
- [VoiceProfile](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_VoiceProfile.html): The combination of a voice print and caller ID.
- [VoiceProfileDomain](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_VoiceProfileDomain.html): A collection of voice profiles.
- [VoiceProfileDomainSummary](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_VoiceProfileDomainSummary.html): A high-level overview of a voice profile domain.
- [VoiceProfileSummary](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_VoiceProfileSummary.html): A high-level summary of a voice profile.
- [VoiceToneAnalysisTask](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_VoiceToneAnalysisTask.html): A representation of an asynchronous request to perform voice tone analysis on a Voice Connector call.
