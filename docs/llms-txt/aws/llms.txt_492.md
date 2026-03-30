# Source: https://docs.aws.amazon.com/ivs/latest/ChatAPIReference/llms.txt

# Amazon IVS Chat API Reference

> Introduction

- [Welcome](https://docs.aws.amazon.com/ivs/latest/ChatAPIReference/Welcome.html)
- [Common Parameters](https://docs.aws.amazon.com/ivs/latest/ChatAPIReference/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/ivs/latest/ChatAPIReference/CommonErrors.html)

## [Actions](https://docs.aws.amazon.com/ivs/latest/ChatAPIReference/API_Operations.html)

- [CreateChatToken](https://docs.aws.amazon.com/ivs/latest/ChatAPIReference/API_CreateChatToken.html): Creates an encrypted token that is used by a chat participant to establish an individual WebSocket chat connection to a room.
- [CreateLoggingConfiguration](https://docs.aws.amazon.com/ivs/latest/ChatAPIReference/API_CreateLoggingConfiguration.html): Creates a logging configuration that allows clients to store and record sent messages.
- [CreateRoom](https://docs.aws.amazon.com/ivs/latest/ChatAPIReference/API_CreateRoom.html): Creates a room that allows clients to connect and pass messages.
- [DeleteLoggingConfiguration](https://docs.aws.amazon.com/ivs/latest/ChatAPIReference/API_DeleteLoggingConfiguration.html): Deletes the specified logging configuration.
- [DeleteMessage](https://docs.aws.amazon.com/ivs/latest/ChatAPIReference/API_DeleteMessage.html): Sends an event to a specific room which directs clients to delete a specific message; that is, unrender it from view and delete it from the clientâs chat history.
- [DeleteRoom](https://docs.aws.amazon.com/ivs/latest/ChatAPIReference/API_DeleteRoom.html): Deletes the specified room.
- [DisconnectUser](https://docs.aws.amazon.com/ivs/latest/ChatAPIReference/API_DisconnectUser.html): Disconnects all connections using a specified user ID from a room.
- [GetLoggingConfiguration](https://docs.aws.amazon.com/ivs/latest/ChatAPIReference/API_GetLoggingConfiguration.html): Gets the specified logging configuration.
- [GetRoom](https://docs.aws.amazon.com/ivs/latest/ChatAPIReference/API_GetRoom.html): Gets the specified room.
- [ListLoggingConfigurations](https://docs.aws.amazon.com/ivs/latest/ChatAPIReference/API_ListLoggingConfigurations.html): Gets summary information about all your logging configurations in the AWS region where the API request is processed.
- [ListRooms](https://docs.aws.amazon.com/ivs/latest/ChatAPIReference/API_ListRooms.html): Gets summary information about all your rooms in the AWS region where the API request is processed.
- [ListTagsForResource](https://docs.aws.amazon.com/ivs/latest/ChatAPIReference/API_ListTagsForResource.html): Gets information about AWS tags for the specified ARN.
- [SendEvent](https://docs.aws.amazon.com/ivs/latest/ChatAPIReference/API_SendEvent.html): Sends an event to a room.
- [TagResource](https://docs.aws.amazon.com/ivs/latest/ChatAPIReference/API_TagResource.html): Adds or updates tags for the AWS resource with the specified ARN.
- [UntagResource](https://docs.aws.amazon.com/ivs/latest/ChatAPIReference/API_UntagResource.html): Removes tags from the resource with the specified ARN.
- [UpdateLoggingConfiguration](https://docs.aws.amazon.com/ivs/latest/ChatAPIReference/API_UpdateLoggingConfiguration.html): Updates a specified logging configuration.
- [UpdateRoom](https://docs.aws.amazon.com/ivs/latest/ChatAPIReference/API_UpdateRoom.html): Updates a roomâs configuration.


## [Data Types](https://docs.aws.amazon.com/ivs/latest/ChatAPIReference/API_Types.html)

- [CloudWatchLogsDestinationConfiguration](https://docs.aws.amazon.com/ivs/latest/ChatAPIReference/API_CloudWatchLogsDestinationConfiguration.html): Specifies a CloudWatch Logs location where chat logs will be stored.
- [DestinationConfiguration](https://docs.aws.amazon.com/ivs/latest/ChatAPIReference/API_DestinationConfiguration.html): A complex type that describes a location where chat logs will be stored.
- [FirehoseDestinationConfiguration](https://docs.aws.amazon.com/ivs/latest/ChatAPIReference/API_FirehoseDestinationConfiguration.html): Specifies a Kinesis Firehose location where chat logs will be stored.
- [LoggingConfigurationSummary](https://docs.aws.amazon.com/ivs/latest/ChatAPIReference/API_LoggingConfigurationSummary.html): Summary information about a logging configuration.
- [MessageReviewHandler](https://docs.aws.amazon.com/ivs/latest/ChatAPIReference/API_MessageReviewHandler.html): Configuration information for optional message review.
- [RoomSummary](https://docs.aws.amazon.com/ivs/latest/ChatAPIReference/API_RoomSummary.html): Summary information about a room.
- [S3DestinationConfiguration](https://docs.aws.amazon.com/ivs/latest/ChatAPIReference/API_S3DestinationConfiguration.html): Specifies an S3 location where chat logs will be stored.
- [ValidationExceptionField](https://docs.aws.amazon.com/ivs/latest/ChatAPIReference/API_ValidationExceptionField.html): This object is used in the ValidationException error.
