# Source: https://docs.aws.amazon.com/gameliftstreams/latest/apireference/llms.txt

# Amazon GameLift Streams API Reference

> Amazon GameLift Streams provides a global cloud solution for content streaming experiences. Use Amazon GameLift Streams tools to upload and configure content for streaming, deploy and scale computing resources to host streams, and manage stream session placement to meet customer demand.

- [Welcome](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/Welcome.html)
- [Common Parameters](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/CommonErrors.html)

## [Actions](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_Operations.html)

- [AddStreamGroupLocations](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_AddStreamGroupLocations.html): Add locations that can host stream sessions.
- [AssociateApplications](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_AssociateApplications.html): When you associate, or link, an application with a stream group, then Amazon GameLift Streams can launch the application using the stream group's allocated compute resources.
- [CreateApplication](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_CreateApplication.html): Creates an application resource in Amazon GameLift Streams, which specifies the application content you want to stream, such as a game build or other software, and configures the settings to run it.
- [CreateStreamGroup](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_CreateStreamGroup.html): Stream groups manage how Amazon GameLift Streams allocates resources and handles concurrent streams, allowing you to effectively manage capacity and costs.
- [CreateStreamSessionConnection](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_CreateStreamSessionConnection.html): Enables clients to reconnect to a stream session while preserving all session state and data in the disconnected session.
- [DeleteApplication](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_DeleteApplication.html): Permanently deletes an Amazon GameLift Streams application resource.
- [DeleteStreamGroup](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_DeleteStreamGroup.html): Permanently deletes all compute resources and information related to a stream group.
- [DisassociateApplications](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_DisassociateApplications.html): When you disassociate, or unlink, an application from a stream group, you can no longer stream this application by using that stream group's allocated compute resources.
- [ExportStreamSessionFiles](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_ExportStreamSessionFiles.html): Export the files that your application modifies or generates in a stream session, which can help you debug or verify your application.
- [GetApplication](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_GetApplication.html): Retrieves properties for an Amazon GameLift Streams application resource.
- [GetStreamGroup](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_GetStreamGroup.html): Retrieves properties for a Amazon GameLift Streams stream group resource.
- [GetStreamSession](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_GetStreamSession.html): Retrieves properties for a Amazon GameLift Streams stream session resource.
- [ListApplications](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_ListApplications.html): Retrieves a list of all Amazon GameLift Streams applications that are associated with the AWS account in use.
- [ListStreamGroups](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_ListStreamGroups.html): Retrieves a list of all Amazon GameLift Streams stream groups that are associated with the AWS account in use.
- [ListStreamSessions](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_ListStreamSessions.html): Retrieves a list of Amazon GameLift Streams stream sessions that a stream group is hosting.
- [ListStreamSessionsByAccount](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_ListStreamSessionsByAccount.html): Retrieves a list of Amazon GameLift Streams stream sessions that this user account has access to.
- [ListTagsForResource](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_ListTagsForResource.html): Retrieves all tags assigned to a Amazon GameLift Streams resource.
- [RemoveStreamGroupLocations](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_RemoveStreamGroupLocations.html): Removes a set of remote locations from this stream group.
- [StartStreamSession](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_StartStreamSession.html): This action initiates a new stream session and outputs connection information that clients can use to access the stream.
- [TagResource](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_TagResource.html): Assigns one or more tags to a Amazon GameLift Streams resource.
- [TerminateStreamSession](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_TerminateStreamSession.html): Permanently terminates an active stream session.
- [UntagResource](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_UntagResource.html): Removes one or more tags from a Amazon GameLift Streams resource.
- [UpdateApplication](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_UpdateApplication.html): Updates the mutable configuration settings for a Amazon GameLift Streams application resource.
- [UpdateStreamGroup](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_UpdateStreamGroup.html): Updates the configuration settings for an Amazon GameLift Streams stream group resource.


## [Data Types](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_Types.html)

- [ApplicationSummary](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_ApplicationSummary.html): Describes an application resource that represents a collection of content for streaming with Amazon GameLift Streams.
- [DefaultApplication](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_DefaultApplication.html): Represents the default Amazon GameLift Streams application that a stream group hosts.
- [ExportFilesMetadata](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_ExportFilesMetadata.html): Provides details about the stream session's exported files.
- [LocationConfiguration](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_LocationConfiguration.html): Configuration settings that define a stream group's stream capacity for a location.
- [LocationState](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_LocationState.html): Represents a location and its corresponding stream capacity and status.
- [PerformanceStatsConfiguration](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_PerformanceStatsConfiguration.html): Configuration settings for sharing the stream session's performance stats with the client
- [ReplicationStatus](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_ReplicationStatus.html): Represents the status of the replication of an application to a location.
- [RuntimeEnvironment](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_RuntimeEnvironment.html): Configuration settings that identify the operating system for an application resource.
- [StreamGroupSummary](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_StreamGroupSummary.html): Describes a Amazon GameLift Streams stream group resource for hosting content streams.
- [StreamSessionSummary](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_StreamSessionSummary.html): Describes an Amazon GameLift Streams stream session.


## [Service-specific Errors](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_Errors.html)

- [AccessDeniedException](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_AccessDeniedException.html): You don't have the required permissions to access this Amazon GameLift Streams resource.
- [ConflictException](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_ConflictException.html): The requested operation would cause a conflict with the current state of a service resource associated with the request.
- [InternalServerException](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_InternalServerException.html): The service encountered an internal error and is unable to complete the request.
- [ResourceNotFoundException](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_ResourceNotFoundException.html): The resource specified in the request was not found.
- [ServiceQuotaExceededException](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_ServiceQuotaExceededException.html): The request would cause the resource to exceed an allowed service quota.
- [ThrottlingException](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_ThrottlingException.html): The request was denied due to request throttling.
- [ValidationException](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_ValidationException.html): One or more parameter values in the request fail to satisfy the specified constraints.
