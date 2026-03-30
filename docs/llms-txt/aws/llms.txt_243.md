# Source: https://docs.aws.amazon.com/connect-participant/latest/APIReference/llms.txt

# Amazon Connect Participant Service API Reference

> Amazon Connect is an easy-to-use omnichannel cloud contact center service that enables companies of any size to deliver superior customer service at a lower cost. Amazon Connect communications capabilities make it easy for companies to deliver personalized interactions across communication channels, including chat.

- [Welcome](https://docs.aws.amazon.com/connect-participant/latest/APIReference/Welcome.html)
- [Working with the ACPS API](https://docs.aws.amazon.com/connect-participant/latest/APIReference/working-with-acps-api.html)
- [Common Parameters](https://docs.aws.amazon.com/connect-participant/latest/APIReference/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/connect-participant/latest/APIReference/CommonErrors.html)

## [Actions](https://docs.aws.amazon.com/connect-participant/latest/APIReference/API_Operations.html)

- [CancelParticipantAuthentication](https://docs.aws.amazon.com/connect-participant/latest/APIReference/API_CancelParticipantAuthentication.html): Cancels the authentication session.
- [CompleteAttachmentUpload](https://docs.aws.amazon.com/connect-participant/latest/APIReference/API_CompleteAttachmentUpload.html): Allows you to confirm that the attachment has been uploaded using the pre-signed URL provided in StartAttachmentUpload API.
- [CreateParticipantConnection](https://docs.aws.amazon.com/connect-participant/latest/APIReference/API_CreateParticipantConnection.html): Creates the participant's connection.
- [DescribeView](https://docs.aws.amazon.com/connect-participant/latest/APIReference/API_DescribeView.html): Retrieves the view for the specified view token.
- [DisconnectParticipant](https://docs.aws.amazon.com/connect-participant/latest/APIReference/API_DisconnectParticipant.html): Disconnects a participant.
- [GetAttachment](https://docs.aws.amazon.com/connect-participant/latest/APIReference/API_GetAttachment.html): Provides a pre-signed URL for download of a completed attachment.
- [GetAuthenticationUrl](https://docs.aws.amazon.com/connect-participant/latest/APIReference/API_GetAuthenticationUrl.html): Retrieves the AuthenticationUrl for the current authentication session for the AuthenticateCustomer flow block.
- [GetTranscript](https://docs.aws.amazon.com/connect-participant/latest/APIReference/API_GetTranscript.html): Retrieves a transcript of the session, including details about any attachments.
- [SendEvent](https://docs.aws.amazon.com/connect-participant/latest/APIReference/API_SendEvent.html)
- [SendMessage](https://docs.aws.amazon.com/connect-participant/latest/APIReference/API_SendMessage.html): Sends a message.
- [StartAttachmentUpload](https://docs.aws.amazon.com/connect-participant/latest/APIReference/API_StartAttachmentUpload.html): Provides a pre-signed Amazon S3 URL in response for uploading the file directly to S3.


## [Data Types](https://docs.aws.amazon.com/connect-participant/latest/APIReference/API_Types.html)

- [AttachmentItem](https://docs.aws.amazon.com/connect-participant/latest/APIReference/API_AttachmentItem.html): The case-insensitive input to indicate standard MIME type that describes the format of the file that will be uploaded.
- [Attendee](https://docs.aws.amazon.com/connect-participant/latest/APIReference/API_Attendee.html): The attendee information, including attendee ID and join token.
- [AudioFeatures](https://docs.aws.amazon.com/connect-participant/latest/APIReference/API_AudioFeatures.html): Has audio-specific configurations as the operating parameter for Echo Reduction.
- [ConnectionCredentials](https://docs.aws.amazon.com/connect-participant/latest/APIReference/API_ConnectionCredentials.html): Connection credentials.
- [Item](https://docs.aws.amazon.com/connect-participant/latest/APIReference/API_Item.html): An item - message or event - that has been sent.
- [MeetingFeaturesConfiguration](https://docs.aws.amazon.com/connect-participant/latest/APIReference/API_MeetingFeaturesConfiguration.html): The configuration settings of the features available to a meeting.
- [MessageMetadata](https://docs.aws.amazon.com/connect-participant/latest/APIReference/API_MessageMetadata.html): Contains metadata related to a message.
- [MessageProcessingMetadata](https://docs.aws.amazon.com/connect-participant/latest/APIReference/API_MessageProcessingMetadata.html): Contains metadata for chat messages.
- [Receipt](https://docs.aws.amazon.com/connect-participant/latest/APIReference/API_Receipt.html): The receipt for the message delivered to the recipient.
- [StartPosition](https://docs.aws.amazon.com/connect-participant/latest/APIReference/API_StartPosition.html): A filtering option for where to start.
- [UploadMetadata](https://docs.aws.amazon.com/connect-participant/latest/APIReference/API_UploadMetadata.html): Fields to be used while uploading the attachment.
- [View](https://docs.aws.amazon.com/connect-participant/latest/APIReference/API_View.html): A view resource object.
- [ViewContent](https://docs.aws.amazon.com/connect-participant/latest/APIReference/API_ViewContent.html): View content containing all content necessary to render a view except for runtime input data.
- [WebRTCConnection](https://docs.aws.amazon.com/connect-participant/latest/APIReference/API_WebRTCConnection.html): Creates the participantâs WebRTC connection data required for the client application (mobile or web) to connect to the call.
- [WebRTCMediaPlacement](https://docs.aws.amazon.com/connect-participant/latest/APIReference/API_WebRTCMediaPlacement.html): A set of endpoints used by clients to connect to the media service group for an Amazon Chime SDK meeting.
- [WebRTCMeeting](https://docs.aws.amazon.com/connect-participant/latest/APIReference/API_WebRTCMeeting.html): A meeting created using the Amazon Chime SDK.
- [Websocket](https://docs.aws.amazon.com/connect-participant/latest/APIReference/API_Websocket.html): The websocket for the participant's connection.
