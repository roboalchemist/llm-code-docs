# Source: https://docs.aws.amazon.com/chime-sdk/latest/dg/llms.txt

# Amazon Chime SDK Developer Guide

> Helps you use Amazon Chime SDK as a developer through the AWS SDK.

- [What is the Amazon Chime SDK?](https://docs.aws.amazon.com/chime-sdk/latest/dg/what-is-chime-sdk.html)
- [Using the Amazon Chime SDK client library for Android](https://docs.aws.amazon.com/chime-sdk/latest/dg/sdk-for-android.html)
- [Using the Amazon Chime SDK client library for iOS](https://docs.aws.amazon.com/chime-sdk/latest/dg/sdk-for-ios.html)
- [Using the Amazon Chime SDK client library for Windows](https://docs.aws.amazon.com/chime-sdk/latest/dg/client-lib-windows.html)
- [Frequently asked questions](https://docs.aws.amazon.com/chime-sdk/latest/dg/chime-sdk-faq.html)
- [Document history](https://docs.aws.amazon.com/chime-sdk/latest/dg/doc-history.html)

## [Using the Amazon Chime SDK](https://docs.aws.amazon.com/chime-sdk/latest/dg/meetings-sdk.html)

- [Available AWS Regions](https://docs.aws.amazon.com/chime-sdk/latest/dg/sdk-available-regions.html): Tables that list the control, data, and media Regions available for use with Amazon Chime SDK meetings.
- [Learn about the client libraries](https://docs.aws.amazon.com/chime-sdk/latest/dg/mtgs-sdk-client-lib.html): Learn how to integrate your custom messaging application with an Amazon Chime SDK client library.
- [Understanding SIP integration](https://docs.aws.amazon.com/chime-sdk/latest/dg/mtgs-sdk-cvc.html): Learn how to integrate SIP-compatible voice infrastructure with an Amazon Chime SDK Voice Connector.
- [Understanding event notifications](https://docs.aws.amazon.com/chime-sdk/latest/dg/mtgs-sdk-notifications.html): How to send meeting even notifications to Amazon EventBridge, Amazon Simple Queue Service (Amazon SQS), and Amazon Simple Notification Service (Amazon SNS).
- [Migrating from the Amazon Chime namespace](https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html): How to migrate from the Chime namespace to the ChimeSDK namespace.


## [Using Amazon Chime SDK meetings](https://docs.aws.amazon.com/chime-sdk/latest/dg/mtgs-sdk-mtgs.html)

- [Migrating to the Amazon Chime SDK meetings namespace](https://docs.aws.amazon.com/chime-sdk/latest/dg/meeting-namespace-migration.html): How to migrate to the Amazon Chime SDK Meetings namespace from the current Chime namespace.
- [Using meeting Regions](https://docs.aws.amazon.com/chime-sdk/latest/dg/chime-sdk-meetings-regions.html): Learn how to select and use the available Amazon Chime SDK meeting Regions.
- [Creating meetings](https://docs.aws.amazon.com/chime-sdk/latest/dg/create-mtgs.html): Procedural steps for creating an Amazon Chime SDK meeting.
- [Selecting meeting features](https://docs.aws.amazon.com/chime-sdk/latest/dg/js-meeting-features.html): The meeting features that you can use in your Amazon Chime SDK JavaScript solutions.
- [How Amazon Chime SDK meetings use WebRTC media](https://docs.aws.amazon.com/chime-sdk/latest/dg/webrtc-media.html): How the Amazon Chime SDK client libraries for JavaScript, React, iOS, and Android support media.
- [Configuring video codecs](https://docs.aws.amazon.com/chime-sdk/latest/dg/js-meeting-manage-codecs.html): The supported video codecs and how to use them in Amazon Chime SDK for JavaScript applications.

### [Configuring your network](https://docs.aws.amazon.com/chime-sdk/latest/dg/network-config.html)

Learn how to configure your network to connect to the Amazon Chime SDK service when regular access is blocked.

- [Using AppKeys and TenantIDs](https://docs.aws.amazon.com/chime-sdk/latest/dg/app-keys-tenant-ids.html): How to limit access to Amazon Chime SDK WebRTC media sessions.
- [Understanding meeting lifecycle events](https://docs.aws.amazon.com/chime-sdk/latest/dg/using-events.html): Learn how to use EventBridge and Amazon SNS to capture and log programmatic events from your Amazon Chime SDK meetings.
- [Understanding CloudWatch metrics](https://docs.aws.amazon.com/chime-sdk/latest/dg/sdk-usage-metrics.html): The meeting metrics that the Amazon Chime SDK can publish to Amazon CloudWatch.

### [Creating media pipelines](https://docs.aws.amazon.com/chime-sdk/latest/dg/media-pipelines.html)

Learn how to create media pipelines for Amazon Chime SDK meetings and capture, audio, video, and other meeting artifacts.

- [Considerations for creating media pipelines](https://docs.aws.amazon.com/chime-sdk/latest/dg/creating-media-pipelines-considerations.html): Learn about the things to consider when creating media pipelines in the Amazon Chime SDK.
- [Understanding limits for active media pipelines](https://docs.aws.amazon.com/chime-sdk/latest/dg/media-pipelines-limits.html): Learn about the default limits for active media pipelines the Amazon Chime SDK
- [Migrating to the Amazon Chime SDK media pipelines namespace](https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-pipelines.html): Learn how to migrate your Amazon Chime media pipelines to the new ChimeSdkMediaPipelines namespace.
- [Understanding media pipeline creation](https://docs.aws.amazon.com/chime-sdk/latest/dg/create-pipeline.html): The broad steps that you follow to create an Amazon Chime SDK media capture pipeline.

### [Creating media capture pipelines](https://docs.aws.amazon.com/chime-sdk/latest/dg/capture-pipe-config.html)

The steps for creating media capture pipelines in Amazon Chime SDK meetings.

- [Creating an Amazon S3 bucket](https://docs.aws.amazon.com/chime-sdk/latest/dg/create-s3-bucket.html): Learn how to create an Amazon S3 bucket that works with a media capture pipeline to store artifacts from an Amazon Chime SDK meeting.
- [Enabling server-side encryption for an Amazon S3 bucket](https://docs.aws.amazon.com/chime-sdk/latest/dg/sse-kms.html): How to enable server-side encryption for an Amazon S3 bucket used with media pipelines in an Amazon Chime SDK meeting.
- [Enabling object level server-side encryption](https://docs.aws.amazon.com/chime-sdk/latest/dg/using-kms-keys-for-encryption.html): Learn how to use AWS KMS keys for server-side encryption.
- [Creating the media capture pipeline](https://docs.aws.amazon.com/chime-sdk/latest/dg/create-capture-pipe.html): The steps for creating an Amazon Chime SDK media capture pipeline.
- [Working with media capture artifacts](https://docs.aws.amazon.com/chime-sdk/latest/dg/artifacts.html): Learn the folder structure of, and the artifacts captured by, an Amazon Chime SDK media capture pipeline.
- [Configuring the audio folder](https://docs.aws.amazon.com/chime-sdk/latest/dg/configure-audio.html): How to configure the audio folder in the Amazon S3 bucket of an Amazon Chime SDK media concatenation pipeline.
- [Configuring the video folder](https://docs.aws.amazon.com/chime-sdk/latest/dg/configure-video.html): How to configure the video folder in the Amazon S3 bucket of an Amazon Chime SDK media capture pipeline.
- [Understanding messages in the data-channel folder](https://docs.aws.amazon.com/chime-sdk/latest/dg/data-channel.html): The content of the messages in the data-channel folder of a media concatenation pipeline's Amazon S3 bucket.
- [Understanding the Amazon S3 bucket folder structure](https://docs.aws.amazon.com/chime-sdk/latest/dg/capture-folder-structure.html): The folder structure of an Amazon S3 bucket for a media capture pipeline.
- [Understanding meeting event files](https://docs.aws.amazon.com/chime-sdk/latest/dg/meeting-events.html): Background information about the files in the meeting-events folder.
- [Understanding transcription files](https://docs.aws.amazon.com/chime-sdk/latest/dg/transcription-messages.html): Background information about the text files that land in the transcription-messages folder.
- [Concatenating data streams](https://docs.aws.amazon.com/chime-sdk/latest/dg/concatenate-streams.html): Code for concatenating video and audio files into a single MP4 file.

### [Creating media concatenation pipelines](https://docs.aws.amazon.com/chime-sdk/latest/dg/create-concat-pipe.html)

How to create media concatenation pipelines.

- [Concatenation pipeline architecture](https://docs.aws.amazon.com/chime-sdk/latest/dg/concat-architecture.html): The architecture of an Amazon Chime SDK media concatenation pipeline.
- [Building a media concatenation pipeline](https://docs.aws.amazon.com/chime-sdk/latest/dg/create-concat-pipe-steps.html): The steps for building an Amazon Chime SDK media concatenation pipeline.
- [Understanding the Amazon S3 bucket folder structure](https://docs.aws.amazon.com/chime-sdk/latest/dg/concat-folder-structure.html): The folder structure of an Amazon S3 bucket for a media concatenation pipeline.
- [Creating media live connector pipelines](https://docs.aws.amazon.com/chime-sdk/latest/dg/connector-pipe-config.html): How to create media live connector pipelines and connect to streaming services.

### [Creating media stream pipelines](https://docs.aws.amazon.com/chime-sdk/latest/dg/create-media-stream-pipeline.html)

Learn how to create Amazon Chime SDK media stream pipelines and capture all attendee audio during an Amazon Chime SDK meeting.

- [Creating a Kinesis Video Streams pool](https://docs.aws.amazon.com/chime-sdk/latest/dg/create-kvs-pool.html): Learn how to create an Amazon Kinesis Video Streams pool, part of creating an Amazon Chime SDK media stream pipeline.
- [Example code for Kinesis Video Streams pools](https://docs.aws.amazon.com/chime-sdk/latest/dg/pool-creation-code.html): How how to create, update, get, list, and delete Kinesis Video Streams pools for use with Amazon Chime SDK media stream pipelines.
- [Creating media stream pipelines](https://docs.aws.amazon.com/chime-sdk/latest/dg/create-stream-pipeline.html): The process for creating an Amazon Chime SDK media stream pipeline.
- [Example code for media stream pipelines](https://docs.aws.amazon.com/chime-sdk/latest/dg/pipeline-creation-code.html): Code examples show how to create Amazon Chime SDK media stream pipelines.

### [Using Event Bridge notifications](https://docs.aws.amazon.com/chime-sdk/latest/dg/media-stream-event-bridge.html)

Learn how to Amazon Chime SDK media stream pipelines use Event Bridge notifications.

- [Understanding media stream pipeline events](https://docs.aws.amazon.com/chime-sdk/latest/dg/stream-pipe-events.html): The events that Amazon Chime SDK media stream pipelines send when Abstract here
- [Understanding Kinesis Video Streams pool events for media stream pipelines](https://docs.aws.amazon.com/chime-sdk/latest/dg/media-stream-pool-events.html): The events that Amazon Chime SDK media pipelines send to Event Bridge when Amazon Kinesis Video Streams pools change their states.
- [Using media stream pipeline data](https://docs.aws.amazon.com/chime-sdk/latest/dg/media-stream-tips-tricks.html): Tips for processing audio and reading data from Amazon Kinesis Video Streams pools.

### [Compositing audio and video into a single view](https://docs.aws.amazon.com/chime-sdk/latest/dg/pipeline-compositing.html)

How to composit the audio, webcam video, and content share streams from an Amazon Chime SDK media pipeline into a single view.

- [Setting canvas orientation](https://docs.aws.amazon.com/chime-sdk/latest/dg/canvas-orientation.html): How to set a landscape or portrait orientation for the Amazon Chime SDK compositing canvas.
- [Setting border and corner attributes](https://docs.aws.amazon.com/chime-sdk/latest/dg/video-attribute.html): How to configure the borders for the video tiles in Amazon Chime SDK compositing.
- [Using the layout configurations](https://docs.aws.amazon.com/chime-sdk/latest/dg/compositing-layouts.html): How to use the layout configurations provided by Amazon Chime SDK compositing.
- [Creating a service-linked role for media pipelines](https://docs.aws.amazon.com/chime-sdk/latest/dg/create-pipeline-role.html): How to create a service-linked role that allows media pipelines to access meetings on your behalf.

### [Using media pipeline events](https://docs.aws.amazon.com/chime-sdk/latest/dg/media-pipe-events.html)

The logging and monitoring messages provided during Amazon Chime SDK media pipeline operations.

- [Setting Amazon S3 bucket permissions](https://docs.aws.amazon.com/chime-sdk/latest/dg/s3-permissions.html): Best practices for setting Amazon S3 bucket permissions for use with AWS CloudTrail.
- [Sending media pipeline events to CloudTrail](https://docs.aws.amazon.com/chime-sdk/latest/dg/pipeline-cloudtrail.html): The media pipeline events that you can send to AWS CloudTrail as an Amazon Chime SDK media capture pipeline is created, used, and deleted.
- [Best practices for stopping media pipelines](https://docs.aws.amazon.com/chime-sdk/latest/dg/stop-pipe-best-practices.html): The best practices for stopping media capture pipelines.

### [Using Amazon Chime SDK live transcription](https://docs.aws.amazon.com/chime-sdk/latest/dg/meeting-transcription.html)

Learn how to add meeting transcription to your Amazon Chime SDK meeting applications.

- [Configuring your account](https://docs.aws.amazon.com/chime-sdk/latest/dg/configure-transcribe.html): Learn how to create a Service Linked role and configure your Amazon Chime SDK account to use live transcription.
- [Choosing transcription options](https://docs.aws.amazon.com/chime-sdk/latest/dg/transcription-options.html): Set the options for your Amazon Chime SDK meeting transcripts: Amazon Transcribe, Amazon Transcribe Medical, and a Region.
- [Starting and stopping transcription](https://docs.aws.amazon.com/chime-sdk/latest/dg/initiate-transcription.html): Learn how to start and stop Amazon Chime SDK meeting transcription operations.
- [Understanding live transcription events](https://docs.aws.amazon.com/chime-sdk/latest/dg/transcription-events.html): The events that EventBridge and Amazon SNS emit when the status of a live transcription operation changes.
- [Understanding live transcription messages](https://docs.aws.amazon.com/chime-sdk/latest/dg/process-msgs.html): Learn how to process Amazon Chime SDK live transcription messages.
- [Processing a received live transcript event](https://docs.aws.amazon.com/chime-sdk/latest/dg/delivery-examples.html): These examples how to process a TranscriptEvent in Amazon Chime SDK live transcription.
- [Parsing transcripts](https://docs.aws.amazon.com/chime-sdk/latest/dg/parse-transcripts.html): Code for parsing complete sentences from transcript files.
- [Using media replication](https://docs.aws.amazon.com/chime-sdk/latest/dg/media-replication.html): Learn how to use media replication to create WebRTC media sessions with more than 250 attendees.

### [Troubleshooting and debugging Amazon Chime SDK meetings](https://docs.aws.amazon.com/chime-sdk/latest/dg/troubleshoot-sdk-meetings.html)

How to troubleshoot and debug your Amazon Chime SDK meeting code.

- [Understanding the system requirements](https://docs.aws.amazon.com/chime-sdk/latest/dg/ts-supported-browsers.html): As part of troubleshooting and debugging Amazon Chime SDK meetings, make sure you code for supported browsers.
- [Setting up logging and monitoring](https://docs.aws.amazon.com/chime-sdk/latest/dg/ts-log-monitor.html): Learn how logging and monitoring can help you debug and troubleshoot an Amazon Chime SDK application.
- [Troubleshooting Amazon Chime SDK meetings](https://docs.aws.amazon.com/chime-sdk/latest/dg/self-troubleshooting.html): Advice and steps for self-troubleshooting Amazon Chime SDK meetings.

### [Understanding common issues](https://docs.aws.amazon.com/chime-sdk/latest/dg/common-issues.html)

Learn how to troubleshoot common Amazon Chime SDK meeting issues, such as audio quality and API throttling.

- [Verifying SDK quotas and API throttling](https://docs.aws.amazon.com/chime-sdk/latest/dg/quotas-throttling.html): The Amazon Chime SDK endpoints and quotas page lists the service quotas, API rates, and whether you can adjust them.
- [Opening support cases](https://docs.aws.amazon.com/chime-sdk/latest/dg/open-support-cases.html): If you have more questions, or require support for your business, you can reach out to AWS Customer support.


## [Using Amazon Chime SDK messaging](https://docs.aws.amazon.com/chime-sdk/latest/dg/using-the-messaging-sdk.html)

- [Migrating to the Amazon Chime SDK identity namespace](https://docs.aws.amazon.com/chime-sdk/latest/dg/identity-namespace-migration.html): How to migrate to the Amazon Chime SDK identity namespace from the current Chime namespace.
- [Migrating to the Amazon Chime SDK messaging namespace](https://docs.aws.amazon.com/chime-sdk/latest/dg/messaging-namespace-migration.html): How to migrate to the Amazon Chime SDK messaging namespace from the current Chime namespace.
- [Understanding messaging prerequisites](https://docs.aws.amazon.com/chime-sdk/latest/dg/messaging-prerequisites.html): Learn the prerequisites for using Amazon Chime SDK messaging.
- [Understanding messaging concepts](https://docs.aws.amazon.com/chime-sdk/latest/dg/messaging-concepts.html): Learn the terms and concepts behind Amazon Chime SDK messaging.
- [Understanding messaging architecture](https://docs.aws.amazon.com/chime-sdk/latest/dg/messaging-architecture.html): Learn the architecture of a basic Amazon Chime SDK messaging application.
- [Understanding message types](https://docs.aws.amazon.com/chime-sdk/latest/dg/msg-types.html): The types of messages you can send through an Amazon Chime SDK messaging channel.

### [Getting started](https://docs.aws.amazon.com/chime-sdk/latest/dg/getting-started.html)

Learn how to get started building an Amazon Chime SDK messaging application.

- [Creating an AppInstance](https://docs.aws.amazon.com/chime-sdk/latest/dg/create-app-instance.html): Learn how to create an AppInstance in Amazon Chime SDK messaging.
- [Making SDK calls from a back-end service](https://docs.aws.amazon.com/chime-sdk/latest/dg/call-from-backend.html): How to call Amazon Chime SDK messaging from a back-end service.
- [Authenticating end-user client applications](https://docs.aws.amazon.com/chime-sdk/latest/dg/auth-client-apps.html): Learn how to authenticate the end-user client applications that you build using Amazon Chime SDK messaging.
- [Creating channels](https://docs.aws.amazon.com/chime-sdk/latest/dg/creating-channels.html): Learn how to create an Amazon Chime SDK messaging channel.
- [Sending messages](https://docs.aws.amazon.com/chime-sdk/latest/dg/send-messages.html): Learn how to send messages in an Amazon Chime SDK messaging application.
- [Using ExpirationSettings](https://docs.aws.amazon.com/chime-sdk/latest/dg/expiration.html): Learn how to use expiration settings and automatically delete unneeded user and channel resources.
- [Using WebSockets to receive messages](https://docs.aws.amazon.com/chime-sdk/latest/dg/websockets.html): Learn how to use WebSockets in an Amazon Chime SDK messaging app.
- [Configuring attachments](https://docs.aws.amazon.com/chime-sdk/latest/dg/configure-attachments.html): Learn how to configure attachments for an Amazon Chime SDK messaging application.
- [Understanding system messages](https://docs.aws.amazon.com/chime-sdk/latest/dg/system-messages.html): Learn how an Amazon Chime SDK messaging application uses system messages.
- [Example IAM roles](https://docs.aws.amazon.com/chime-sdk/latest/dg/iam-roles.html): Learn how to configure the IAM roles and policies for an AppInstanceUser in an Amazon Chime SDK messaging instance.
- [Understanding authorization by role](https://docs.aws.amazon.com/chime-sdk/latest/dg/auth-by-role.html): Learn how an Amazon Chime SDK messaging application authorizes users based on their roles.
- [Streaming messaging data](https://docs.aws.amazon.com/chime-sdk/latest/dg/streaming-export.html): How to configure an Amazon Chime SDK messaging AppInstance to receive streamed data.

### [Using elastic channels to host live events](https://docs.aws.amazon.com/chime-sdk/latest/dg/elastic-channels.html)

How to use Amazon Chime SDK Messaging elastic channels to host chat during live events with up to 1-million users.

- [Creating elastic channels](https://docs.aws.amazon.com/chime-sdk/latest/dg/create-elastic-channel.html): How to create elastic channels in Amazon Chime SDK Messaging applications.
- [Managing elastic channel members](https://docs.aws.amazon.com/chime-sdk/latest/dg/manage-elastic-members.html): How to manage the members in a Amazon Chime SDK Messaging elastic channel.
- [Sending elastic channel messages](https://docs.aws.amazon.com/chime-sdk/latest/dg/send-messages-elastic.html): How to send messages on an Amazon Chime SDK Messaging elastic channel.
- [Understanding WebSocket system messages in elastic channels](https://docs.aws.amazon.com/chime-sdk/latest/dg/websocket-messages-elastic.html): How to update WebSocket messages in an Amazon Chime SDK Messaging elastic channel.
- [Using Kinesis streams to receive system messages](https://docs.aws.amazon.com/chime-sdk/latest/dg/elastic-onboard-streams.html): How to configure a Amazon Chime SDK Messaging AppInstance to receive system messages in the form of a stream.
- [Testing elastic channels in our demo app](https://docs.aws.amazon.com/chime-sdk/latest/dg/elastic-testing.html): How to use the Amazon Chime SDK Messaging demo app to test elastic channels.

### [Using mobile push notifications to receive messages](https://docs.aws.amazon.com/chime-sdk/latest/dg/using-push-notifications.html)

Learn how to use push notifications to receive messages in an Amazon Chime SDK application.

- [Create an Amazon Pinpoint application](https://docs.aws.amazon.com/chime-sdk/latest/dg/create-pinpoint.html): Learn how to create an Amazon Pinpoint application, the the first step in using push notifications in Amazon Chime SDK.
- [Create a service role](https://docs.aws.amazon.com/chime-sdk/latest/dg/create-service-role.html): Learn how to create a service role, the second step in using push notifications in Amazon Chime SDK.
- [Register a mobile device endpoint as an App Instance user](https://docs.aws.amazon.com/chime-sdk/latest/dg/register-endpoint.html): Insert section abstract text here.
- [Send a channel message with notifications enabled](https://docs.aws.amazon.com/chime-sdk/latest/dg/send-channel-msg-with-notifications.html): Learn how to use the SendChannelMessage API to send Amazon Chime SDK channel messages with push notifications enabled.
- [Receiving push notifications](https://docs.aws.amazon.com/chime-sdk/latest/dg/receive-notifications.html): Learn how to Amazon Chime SDK receive push notifications.
- [Debugging push notification failures](https://docs.aws.amazon.com/chime-sdk/latest/dg/debug-notifications.html): Learn how to use EventBridge notifications to help debug message delivery failures in Amazon Chime SDK push notifications.
- [Using filter rules to filter messages](https://docs.aws.amazon.com/chime-sdk/latest/dg/filter-msgs.html): Learn how to use filter rules to limit the messages that users receive.

### [Using service-linked roles](https://docs.aws.amazon.com/chime-sdk/latest/dg/using-roles.html)

Learn how to use service-linked roles to stream Amazon Chime SDK for Messaging data.

- [Using service-linked roles for data streaming](https://docs.aws.amazon.com/chime-sdk/latest/dg/stream-service-linked.html): Learn how to use service-linked roles for data streaming.

### [Using channel flows to process messages](https://docs.aws.amazon.com/chime-sdk/latest/dg/using-channel-flows.html)

Learn how to use channel flows and automatically perform actions on chat messages.

- [Setting up a Channel Processor](https://docs.aws.amazon.com/chime-sdk/latest/dg/processor-setup.html): Learn how to set up a channel processor, and Lambda function the performs actions on chat messages before they're delivered.
- [Creating a channel flow](https://docs.aws.amazon.com/chime-sdk/latest/dg/create-channel-flow.html): Learn how to create a channel flow and take action on messages before they're delivered.
- [Associating and disassociating channel flows](https://docs.aws.amazon.com/chime-sdk/latest/dg/associate-channel-flow.html): Learn how to start and stop using a channel flow by associating and disassociating it with a channel.
- [Sending messages](https://docs.aws.amazon.com/chime-sdk/latest/dg/sending-msgs.html): Learn how to send messages to chat channels that are associated with a channel flow.
- [Creating failure alerts by automating with EventBridge](https://docs.aws.amazon.com/chime-sdk/latest/dg/event-bridge-events.html): Information and code sample for using EventBridge with channel flows.

### [Using bots as channel agents](https://docs.aws.amazon.com/chime-sdk/latest/dg/appinstance-bots.html)

Learn how to use AppInstanceBots as channel agents in Amazon Chime SDK Messaging solutions.

### [Creating an Amazon Lex V2 bot](https://docs.aws.amazon.com/chime-sdk/latest/dg/create-lex-bot.html)

Learn how to create an Amazon Lex V2 bot, the prerequisite for using AppInstance bots as agents.

- [Creating a welcome intent](https://docs.aws.amazon.com/chime-sdk/latest/dg/welcome-intent.html): Learn how to create an optional welcome intent that enables an AppInstanceBot to announce itself and its capabilities.
- [Creating Amazon Lex V2 bot versions](https://docs.aws.amazon.com/chime-sdk/latest/dg/lex-versions.html): Learn how to create versions of an Amazon Lex V2 bot.
- [Creating Amazon Lex V2 bot aliases](https://docs.aws.amazon.com/chime-sdk/latest/dg/lex-aliases.html): Learn how to create aliases for an Amazon Lex V2 bot.
- [Setting up AppInstance bots](https://docs.aws.amazon.com/chime-sdk/latest/dg/appinstance-bot-setup.html): Learn how to use set up Amazon Chime SDK messaging AppInstance bots.
- [Channel membership for AppInstanceBots](https://docs.aws.amazon.com/chime-sdk/latest/dg/channel-membership.html): Learn how to create a channel membership for an AppInstanceBot.
- [Sending messages to an AppInstanceBot](https://docs.aws.amazon.com/chime-sdk/latest/dg/message-appinstancebot.html): Learn how to send messages to an AppInstanceBot.
- [Processing messages from Amazon Lex](https://docs.aws.amazon.com/chime-sdk/latest/dg/process-from-lexv2.html): How to process messages from Amazon Lex Abstract here
- [Processing responses from an AppInstanceBot](https://docs.aws.amazon.com/chime-sdk/latest/dg/process-response.html): How to process the responses from an AppInstanceBot.
- [Using rules to send events to Amazon EventBridge](https://docs.aws.amazon.com/chime-sdk/latest/dg/event-bridge-alerts.html): Learn how to create rules that send events to Amazon EventBridge when the Amazon Chime SDK can't invoke an Amazon Lex V2 bot.
- [Troubleshooting AppInstanceBots](https://docs.aws.amazon.com/chime-sdk/latest/dg/troubleshoot-lex-bots.html): Learn how to troubleshoot AppInstanceBots configured with Amazon Lex V2 bots.
- [Managing message retention](https://docs.aws.amazon.com/chime-sdk/latest/dg/manage-retention.html): Learn how to manage data retention in an Amazon Chime SDK messaging application.
- [User interface components for messaging](https://docs.aws.amazon.com/chime-sdk/latest/dg/ui-components.html): Learn the user-interface components available for an Amazon Chime SDK messaging application.
- [Integrating with client libraries](https://docs.aws.amazon.com/chime-sdk/latest/dg/integrate-client-library.html): Learn how to integrate your messaging client application with the AWS SDK and the Amazon Chime SDK client libraries.
- [Using Amazon Chime SDK messaging with JavaScript](https://docs.aws.amazon.com/chime-sdk/latest/dg/use-javascript.html): Learn how to use JavaScript in an Amazon Chime SDK messaging application.


## [Using the Amazon Chime SDK PSTN audio service](https://docs.aws.amazon.com/chime-sdk/latest/dg/sdk-use-pstn-service.html)

- [Migrating to the Amazon Chime SDK voice namespace](https://docs.aws.amazon.com/chime-sdk/latest/dg/voice-namespace-migration.html): How to migrate to the Amazon Chime SDK Voice namespace, including reasons to migrate, plus the endpoints, service principals, and more.
- [Understanding phone numbers, SIP rules, SIP media applications, and AWS Lambda functions](https://docs.aws.amazon.com/chime-sdk/latest/dg/using-lambda.html): Learn how Amazon Chime SDK SIP rules and the PSTN audio service work with AWS Lambda functions.
- [Understanding the PSTN audio service programming model](https://docs.aws.amazon.com/chime-sdk/latest/dg/pstn-model.html): Learn the PSTN audio service programming model, a call/response model that uses AWS Lambda functions.
- [Routing calls and events to AWS Lambda functions](https://docs.aws.amazon.com/chime-sdk/latest/dg/route-calls-events.html): Learn the program flow between SIP rules and AWS Lambda functions.
- [Routing calls to AWS Lambda functions (AWS CLI)](https://docs.aws.amazon.com/chime-sdk/latest/dg/route-calls-events-cli.html): Use the AWS CLI with the Amazon Chime SDK to route incoming phone calls to your AWS Lambda function for treatment.
- [Learn about using PSTN audio service call legs](https://docs.aws.amazon.com/chime-sdk/latest/dg/call-architecture.html): An overview of the SIP media application call legs.
- [Understanding call flow](https://docs.aws.amazon.com/chime-sdk/latest/dg/call-flow.html): A high-level diagram showing the flow of a call through a SIP media application and associated AWS Lambda functions.

### [Building AWS Lambda functions for the PSTN audio service](https://docs.aws.amazon.com/chime-sdk/latest/dg/writing-lambdas.html)

Conceptual information and example code for building the AWS Lambda functions used by the PSTN audio service.

- [Understanding telephony events](https://docs.aws.amazon.com/chime-sdk/latest/dg/pstn-invocations.html): Understand the events that cause the Audio Service to invoke an AWS AWS Lambda function.
- [Understanding PSTN audio service actions](https://docs.aws.amazon.com/chime-sdk/latest/dg/about-actions.html): Learn how the PSTN audio service uses actions, items that you want to run on a phone call, such as receiving DTMF digits or joining a meeting.

### [Learn about the telephony events that invoke Lambda functions](https://docs.aws.amazon.com/chime-sdk/latest/dg/invoking-Lambda.html)

Learn the Audio Service events that invoke AWS Lambda functions.

- [Making an outbound call](https://docs.aws.amazon.com/chime-sdk/latest/dg/use-create-call-api.html): Learn the flow of invocations and events that take place when you invoke the CreateSipMediaApplicationCall API.
- [Receiving an inbound call](https://docs.aws.amazon.com/chime-sdk/latest/dg/case-1.html): Learn how a SIP media application invokes an AWS Lambda function that responds to inbound calls.
- [Specifying actions in response to telephony events](https://docs.aws.amazon.com/chime-sdk/latest/dg/use-case-2.html): Learn how a SIP media application calls the next actions in an AWS Lambda function after the application connects to a call.
- [Receiving caller input](https://docs.aws.amazon.com/chime-sdk/latest/dg/case-4.html): Learn how a SIP media application receives DTMF digits, and invokes AWS Lambda functions in response to the input.
- [Updating in-progress calls](https://docs.aws.amazon.com/chime-sdk/latest/dg/update-sip-call.html): Learn how to use the UpdateSipMediaApplicationCall API to update calls placed to the PSTN audio service.
- [Ending a call](https://docs.aws.amazon.com/chime-sdk/latest/dg/case-5.html): Learn how Audio Service and AWS Lambda functions respond when a user ends a one-legged or two-legged call.
- [Understanding end-to-end calls](https://docs.aws.amazon.com/chime-sdk/latest/dg/use-cases.html): Example AWS Lambda functions and sample code for receiving a call, playing a greeting, accepting PINs, and joining an Amazon Chime SDK meeting.
- [Responding to invocations with action lists](https://docs.aws.amazon.com/chime-sdk/latest/dg/invoke-on-call-leg.html): Learn how an AWS Lambda function responds to an invocation event type with a list of actions, such as playing hello or goodbye messages.

### [Supported actions for the PSTN audio service](https://docs.aws.amazon.com/chime-sdk/latest/dg/specify-actions.html)

Learn the signaling and media actions available for the PSTN audio service.

### [Using TransactionAttributes](https://docs.aws.amazon.com/chime-sdk/latest/dg/transaction-attributes.html)

Use TransactionAttributes structures to store data in SIP media applications instead of external databases.

- [Setting TransactionAttributes](https://docs.aws.amazon.com/chime-sdk/latest/dg/set-trans-attributes.html): Learn how to set TransactionAttributes and begin storing data in SIP media applications.
- [Updating TransactionAttributes](https://docs.aws.amazon.com/chime-sdk/latest/dg/update-trans-attributes.html): Learn how to update the TransactionAttributes stored in SIP media applications.
- [Clearing TransactionAttributes](https://docs.aws.amazon.com/chime-sdk/latest/dg/clear-trans-attributes.html): Learn how to clear the TransactionAttributes data stored in SIP media applications.
- [Handling ACTION_SUCCESSFUL events](https://docs.aws.amazon.com/chime-sdk/latest/dg/attribute-trans-success.html): Learn how handle ACTION_SUCCESSFUL events when using TransactionAttributes structures.
- [Invalid inputs](https://docs.aws.amazon.com/chime-sdk/latest/dg/attribute-trans-invalid.html): Learn how to recognize invalid inputs in Amazon Chime SDK TransactionAttributes structures.

### [Using call recording](https://docs.aws.amazon.com/chime-sdk/latest/dg/sip-apps-call-record.html)

Learn how to use call recording with your SIP media applications to record any combination of incoming and outgoing call legs.

- [Recording audio tracks](https://docs.aws.amazon.com/chime-sdk/latest/dg/record-legs.html): Learn how to record any combination of incoming and outgoing audio tracks.
- [Sample use cases](https://docs.aws.amazon.com/chime-sdk/latest/dg/recording-use-cases.html): Use cases that show the program flow for recording one or more call legs with a SIP media application.

### [Call recording actions for SIP media applications](https://docs.aws.amazon.com/chime-sdk/latest/dg/use-recording-apis.html)

Learn how to use the call recording actions with your SIP media applications.

- [StartCallRecording](https://docs.aws.amazon.com/chime-sdk/latest/dg/start-call-recording.html): Learn how to use the StartCallRecording action to begin recording phone calls with your SIP media application.
- [StopCallRecording](https://docs.aws.amazon.com/chime-sdk/latest/dg/stop-call-recording.html): Learn how to use the StopCallRecording action to stop recording on a call leg.
- [PauseCallRecording](https://docs.aws.amazon.com/chime-sdk/latest/dg/pause-call-recording.html): Learn how to use the PauseCallRecording action to begin recording phone calls with your SIP media application.
- [ResumeCallRecording](https://docs.aws.amazon.com/chime-sdk/latest/dg/resume-call-recording.html): The ResumeCallRecording action resumes the recording of a call leg.
- [CallAndBridge](https://docs.aws.amazon.com/chime-sdk/latest/dg/call-and-bridge.html): Learn how to use the CallAndBridge action to bridge an incoming PSTN call with another call leg.
- [Hangup](https://docs.aws.amazon.com/chime-sdk/latest/dg/hangup.html): Learn how to write an AWS Lambda function that ends a call when a meeting attendee hangs up.
- [JoinChimeMeeting](https://docs.aws.amazon.com/chime-sdk/latest/dg/join-chime-meeting.html): Learn how to write a AWS Lambda function that joins an Amazon Chime SDK meeting.
- [ModifyChimeMeetingAttendee (muting and unmuting audio)](https://docs.aws.amazon.com/chime-sdk/latest/dg/mute-unmute.html): Learn how to use the ModifyChimeMeetingAttendee action to mute and unmute audio during a meeting.
- [Pause](https://docs.aws.amazon.com/chime-sdk/latest/dg/pause.html): Learn how to write an AWS Lambda function that uses the Pause audio action.
- [PlayAudio](https://docs.aws.amazon.com/chime-sdk/latest/dg/play-audio.html): Learn how to write a AWS Lambda function that plays audio, including audio files such as welcome messages, during an Amazon Chime SDK meeting.
- [PlayAudioAndGetDigits](https://docs.aws.amazon.com/chime-sdk/latest/dg/play-audio-get-digits.html): Learn how to write an AWS Lambda function that plays a greeting message and captures DTMF digits.
- [ReceiveDigits](https://docs.aws.amazon.com/chime-sdk/latest/dg/listen-to-digits.html): Learn how to invoke an AWS Lambda function when a user enters digits that match a regular expression pattern specified in an action.
- [RecordAudio](https://docs.aws.amazon.com/chime-sdk/latest/dg/record-audio.html): Learn how to use the RecordAudio event to record audio during an Amazon Chime SDK meeting.
- [SendDigits](https://docs.aws.amazon.com/chime-sdk/latest/dg/send-digits.html): Learn how to use the SendDigits action and send up to 50 digits on any call leg.
- [Speak](https://docs.aws.amazon.com/chime-sdk/latest/dg/speak.html): Learn how to use the Speak action to play speech in your communications application.
- [SpeakAndGetDigits](https://docs.aws.amazon.com/chime-sdk/latest/dg/speak-and-get-digits.html): Learn how to use the SpeakAndGetDigits action to play speech and capture digits in your communications application.
- [StartBotConversation](https://docs.aws.amazon.com/chime-sdk/latest/dg/start-bot-conversation.html): Learn how to use the StartBotConversation action to establish voice conversations between users and Amazon Lex v2 bots.
- [Using SIP headers](https://docs.aws.amazon.com/chime-sdk/latest/dg/sip-headers.html): Learn how to use custom SIP headers to pass non-standard SIP information in an AWS Lambda function.
- [Using call detail records](https://docs.aws.amazon.com/chime-sdk/latest/dg/attributes.html): Learn how to configure Amazon Chime SDK Voice Connectors to store call detail records.
- [Understanding timeouts and retries](https://docs.aws.amazon.com/chime-sdk/latest/dg/timeouts.html): Learn how the PSTN audio service handles timeouts and 4XX error codes.

### [Debugging and troubleshooting](https://docs.aws.amazon.com/chime-sdk/latest/dg/debug-pstn.html)

Use the following information to help you diagnose and fix common issues that you might encounter when working with the Amazon Chime SDK PSTN audio service.

- [Checking the logs for the Amazon Chime SDK PTSN audio service](https://docs.aws.amazon.com/chime-sdk/latest/dg/check-logs.html): Learn how to use Cloudwatch logs to help debug the AWS Lambda functions and SIP media applications used in Amazon Chime SDK meetings.
- [Debugging unexpected hangups](https://docs.aws.amazon.com/chime-sdk/latest/dg/unexpected-hangups.html): Learn how to debug unexpected hangup error messages in the Amazon Chime SDK PTSN audio service.
- [Debugging unexpected ACTION_FAILED events](https://docs.aws.amazon.com/chime-sdk/latest/dg/unexpected-action-fail.html): Learn how to debug the most common ACTION_FAILED events for Amazon Chime SDK meetings.
- [Understanding VoiceFocus](https://docs.aws.amazon.com/chime-sdk/latest/dg/voice-focus.html): Learn how to use the VoiceFocus action to reduce foreground and background noises.
- [Amazon Chime SDK PSTN audio service glossary](https://docs.aws.amazon.com/chime-sdk/latest/dg/chm-dg-glossary.html): A glossary of the terms that you find in the PSTN audio service section of the Amazon Chime SDK Developer Guide and the Amazon Chime SDK.


## [Generating insights from calls](https://docs.aws.amazon.com/chime-sdk/latest/dg/call-analytics.html)

- [What is call analytics](https://docs.aws.amazon.com/chime-sdk/latest/dg/what-is-amazon-chime-sdk-call-analytics.html): An overview of Amazon Chime SDK call analytics and the components needed to use it.
- [Understanding call analytics terminology](https://docs.aws.amazon.com/chime-sdk/latest/dg/ca-terms-concepts.html): Learn the concepts and terms needed to use Amazon Chime SDK call analytics effectively.

### [Creating call analytics configurations](https://docs.aws.amazon.com/chime-sdk/latest/dg/creating-ca-configuration.html)

How to create an Amazon Chime SDK call analytics configuration.

- [Understanding the prerequisites](https://docs.aws.amazon.com/chime-sdk/latest/dg/ca-prerequisites.html): The components and services needed to create an Amazon Chime SDK call analytics configuration.
- [Using the console to create configurations](https://docs.aws.amazon.com/chime-sdk/latest/dg/create-config-console.html): The steps for creating an Amazon Chime SDK call analytics configuration.
- [Using APIs to create call analytics configurations](https://docs.aws.amazon.com/chime-sdk/latest/dg/create-config-apis.html): Learn how to create Voice Connectors and call analytics configurations programmatically.
- [Associating a configuration with a Voice Connector](https://docs.aws.amazon.com/chime-sdk/latest/dg/ca-associate-vc-steps.html): Learn how to start call Amazon Chime SDK call analytics automatically by associate a Voice Connector with call analytics configuration.

### [Using call analytics configurations](https://docs.aws.amazon.com/chime-sdk/latest/dg/using-call-analytics-configurations.html)

How to use call analytics configurations to create call analytics pipelines.

- [Understanding workflows for recording calls](https://docs.aws.amazon.com/chime-sdk/latest/dg/recording-workflows.html): A set of suggested Amazon Chime SDK call analytics workflows for recording
- [Understanding workflows for machine-learning based analytics](https://docs.aws.amazon.com/chime-sdk/latest/dg/ml-based-analytics.html): Suggested ways for using Amazon Chime SDK call analytics with machine
- [Managing call analytics pipelines](https://docs.aws.amazon.com/chime-sdk/latest/dg/managing-call-analytics-pipelines.html): How to manage Amazon Chime SDK call analytics pipelines.
- [Pausing and resuming call analytics pipelines](https://docs.aws.amazon.com/chime-sdk/latest/dg/pausing-and-resuming-call-analytics-pipelines.html): Learn how to pause and resume Amazon Chime SDK call analytics pipelines.
- [Using the call analytics resource access role](https://docs.aws.amazon.com/chime-sdk/latest/dg/call-analytics-resource-access-role.html): The calling account must create the resource access role used by a media insights pipeline configuration.
- [Understanding the call analytics statuses](https://docs.aws.amazon.com/chime-sdk/latest/dg/call-analytics-statuses.html): Learn how to get statuses for Amazon Chime SDK call analytics.
- [Monitoring call analytics pipelines with Amazon CloudWatch](https://docs.aws.amazon.com/chime-sdk/latest/dg/monitoring-with-cloudwatch.html): How to monitor Amazon Chime SDK call analytics pipelines by publishing metrics to Amazon CloudWatch.

### [Call analytics processor and output destinations](https://docs.aws.amazon.com/chime-sdk/latest/dg/call-analytics-processor-and-output-destinations.html)

The destinations for Amazon Chime SDK call analytics processors and Amazon Kinesis streams, and code for using the destinations.

- [Combining transcription with recording sinks](https://docs.aws.amazon.com/chime-sdk/latest/dg/combining-recording-transcription.html): Learn how to use Amazon Transcribe or Amazon Transcribe Call Analytics with an Amazon S3 recording sink.
- [Using Amazon EventBridge notifications](https://docs.aws.amazon.com/chime-sdk/latest/dg/using-eventbridge-notifications.html): Learn how to use Amazon EventBridge notifications with Amazon Chime SDK call analytics.
- [Creating an Amazon Chime SDK data lake](https://docs.aws.amazon.com/chime-sdk/latest/dg/ca-data-lake.html): Learn how to create an Amazon Chime SDK data lake that houses your analytics data.
- [Configuring an Quick dashboard](https://docs.aws.amazon.com/chime-sdk/latest/dg/quicksight-setup-setup.html): How to configure a QuickSights dashboard and visualize the information in an Amazon Chime SDK data lake.

### [Call analytics data model](https://docs.aws.amazon.com/chime-sdk/latest/dg/ca-data-model.html)

The data model that underlies Amazon Chime SDK call analytics.

- [Understanding the AWS Glue data catalog table structure](https://docs.aws.amazon.com/chime-sdk/latest/dg/ca-data-model-diagram.html): A diagram of the tables in the Amazon Chime SDK call analytics Glue data catalog.
- [Understanding the AWS Glue data catalog tables](https://docs.aws.amazon.com/chime-sdk/latest/dg/glue-tables.html): This reference lists the columns, data types, and elements in the Amazon Chime SDK call analytics Glue data catalog.
- [Extracting data in your AWS Glue data catalog](https://docs.aws.amazon.com/chime-sdk/latest/dg/ca-data-model-queries.html): Sample queries for extracting data from the Amazon Chime SDK call analytics Glue data catalog.

### [Using Amazon Chime SDK voice analytics](https://docs.aws.amazon.com/chime-sdk/latest/dg/voice-analytics.html)

Amazon Chime SDK voice analytics enables you to identify new and returning callers, predict caller sentiments, and analyze conversations in real time.

- [Understanding voice analytics architecture](https://docs.aws.amazon.com/chime-sdk/latest/dg/va-architecture.html): Learn how data flows through the Amazon Chime SDK voice analytics system.
- [Understanding speaker search workflow](https://docs.aws.amazon.com/chime-sdk/latest/dg/va-data-flow.html): Learn the data and program flow for an Amazon Chime SDK speaker search analysis.
- [Sample voice tone analysis workflow](https://docs.aws.amazon.com/chime-sdk/latest/dg/va-tone-flow.html): Learn the program and data flow for an Amazon Chime SDK voice tone analysis.
- [Polling for task results](https://docs.aws.amazon.com/chime-sdk/latest/dg/va-task-result-poll.html): Learn how to use a set of "Get" APIs to poll for Amazon Chime SDK voice analytics task results.

### [Understanding notifications](https://docs.aws.amazon.com/chime-sdk/latest/dg/va-notification-targets.html)

Learn how to set up notification targets for task results in Amazon Chime SDK voice analytics.

- [Understanding IAM policies for notification targets](https://docs.aws.amazon.com/chime-sdk/latest/dg/va-iam-target-policies.html): How to use IAM policies that allow Amazon Chime SDK voice analytics to access your SQS, SNS, or Kinesis Data Stream notification targets.
- [Voice analytics example Lambda function](https://docs.aws.amazon.com/chime-sdk/latest/dg/va-sample-lambda.html): An example AWS Lambda function that process notifications sent from an Amazon Chime SDK Voice Connector.

### [Understanding data storage, opt-out, and data-retention policies](https://docs.aws.amazon.com/chime-sdk/latest/dg/va-opt-out.html)

How to opt-out of having your Amazon Chime SDK voice analytics data used to improve machine learning models.

- [Understanding data storage for speaker search](https://docs.aws.amazon.com/chime-sdk/latest/dg/speaker-search-data-storage.html): The types of data stored for use by the Amazon Chime SDK speaker search function.
- [Handling opt outs for speaker search](https://docs.aws.amazon.com/chime-sdk/latest/dg/va-handle-opt-outs.html): Learn how to delete voice profiles and voice profile domains when users withdraw their consent for Amazon Chime SDK voice analysis.
- [Understanding data retention](https://docs.aws.amazon.com/chime-sdk/latest/dg/va-data-retention.html): Learn how the Amazon Chime SDK voice analytics service retains data.
- [Using voice APIs to run voice analytics](https://docs.aws.amazon.com/chime-sdk/latest/dg/va-in-voice-namespace.html): Learn why you should use Amazon Chime SDK media insights pipeline APIs to start voice analytics tasks.
- [Call analytics service quotas](https://docs.aws.amazon.com/chime-sdk/latest/dg/ca-regions.html): The Amazon Chime SDK call analytics and voice analytics service quotas.


## [Using the Amazon Chime SDK client library for JavaScript](https://docs.aws.amazon.com/chime-sdk/latest/dg/js-sdk-intro.html)

- [Understanding components](https://docs.aws.amazon.com/chime-sdk/latest/dg/components.html): The components needed embed audio, video, and screen sharing in your Amazon Chime SDK web app.
- [Understanding key concepts](https://docs.aws.amazon.com/chime-sdk/latest/dg/key-concepts.html): The concepts that you need to understand before you start building an Amazon Chime application.
- [Understanding service architecture](https://docs.aws.amazon.com/chime-sdk/latest/dg/service-architecture-java.html): The architecture of the Amazon Chime SDK client library for JavaScript components and how they work with other AWS services.
- [Understanding web application architecture](https://docs.aws.amazon.com/chime-sdk/latest/dg/web-architecture.html): Learn the architecture of an Amazon Chime SDK web application.
- [Understanding server application architecture](https://docs.aws.amazon.com/chime-sdk/latest/dg/server-app-architecture.html): The architecture of an Amazon Chime SDK server application.
- [Understanding the media control plane](https://docs.aws.amazon.com/chime-sdk/latest/dg/media-control-plane-java.html): An overview of the Amazon Chime SDK media control plane.
- [Understanding the media data plane](https://docs.aws.amazon.com/chime-sdk/latest/dg/media-data-plane.html): An overview of the Amazon Chime SDK media data plane.
- [Understanding web application component architecture](https://docs.aws.amazon.com/chime-sdk/latest/dg/web-app-comp-arch-java.html): Learn the architecture of an Amazon Chime SDK web client application.

### [Building a server application](https://docs.aws.amazon.com/chime-sdk/latest/dg/build-server-app.html)

Learn how to build an Amazon Chime SDK server application.

- [Creating IAM users or roles](https://docs.aws.amazon.com/chime-sdk/latest/dg/create-iam-users-roles.html): Learn how to create IAM users or roles and assign them to Amazon Chime SDK meeting attendees.
- [Configuring the AWS SDK to invoke the APIs](https://docs.aws.amazon.com/chime-sdk/latest/dg/invoke-apis.html): Code sample that shows how to pass credentials and set the correct endpoint.
- [Creating a meeting](https://docs.aws.amazon.com/chime-sdk/latest/dg/create-meeting.html): Learn the API call and parameter needed to create an Amazon Chime SDK meeting.
- [Creating an attendee](https://docs.aws.amazon.com/chime-sdk/latest/dg/create-attendee.html): Learn the API calls and parameters needed to create an Amazon Chime SDK meeting attendee.
- [Sending a response to the client](https://docs.aws.amazon.com/chime-sdk/latest/dg/send-response-to-client.html): Instructions for encoding and sending Amazon Chime SDK meeting and attendee objects to a client application.
- [Building a client application](https://docs.aws.amazon.com/chime-sdk/latest/dg/build-client-app.html): The Amazon Chime SDK client library for JavaScript API Overview on GitHub provides the steps and code samples needed to build an Amazon Chime SDK client application.

### [Integrating background filters into a client application](https://docs.aws.amazon.com/chime-sdk/latest/dg/background-filters.html)

How to integrate background blur and background replacement filters into an Amazon Chime SDK JavaScript application.

- [About using background filters](https://docs.aws.amazon.com/chime-sdk/latest/dg/about-bg-filters.html): The information needed to use background filters effectively.
- [Using a content-security policy](https://docs.aws.amazon.com/chime-sdk/latest/dg/content-security.html): Policies that grant the Amazon Chime SDK access the resources needed to run background blur and background replacement at runtime.

### [Adding background filters to your application](https://docs.aws.amazon.com/chime-sdk/latest/dg/add-filters.html)

The steps for adding the background blur and background replacement filters to your Amazon Chime SDK application.

- [Checking for support before offering a filter](https://docs.aws.amazon.com/chime-sdk/latest/dg/support-check.html): The Amazon Chime SDK provides an asynchronous static method that checks for supported browsers and attempts to download the required assets.
- [Creating a VideoFxConfig object](https://docs.aws.amazon.com/chime-sdk/latest/dg/create-videofxconfig.html): You can define configurations for backgroundBlur and backgroundReplacement in the same object.
- [Creating a VideoFxProcessor object](https://docs.aws.amazon.com/chime-sdk/latest/dg/create-videofxprocessor.html): When creating the VideoFxProcessor object, AWS servers download the runtime assets, or a browser cache loads the assets.
- [Configuring the VideoFxProcessor object](https://docs.aws.amazon.com/chime-sdk/latest/dg/configure-videofxprocessor.html): The following tables list the VideoFxProcessor properties that you can configure.
- [Creating the VideoTransformDevice object](https://docs.aws.amazon.com/chime-sdk/latest/dg/create-video-transform.html): The following example shows how to create a VideoTransformDevice object that contains the VideoFxProcessor.
- [Starting video input](https://docs.aws.amazon.com/chime-sdk/latest/dg/start-video-input.html): The following example shows how to use the VideoTransformDevice object to start video input.
- [Tuning resource utilization](https://docs.aws.amazon.com/chime-sdk/latest/dg/tuning.html): How to tune an Amazon Chime SDK VideoFxProcessor object.
- [Example background filter](https://docs.aws.amazon.com/chime-sdk/latest/dg/example-bg-filter.html): Example code that demonstrates how to implement the Amazon Chime SDK background blur and background replacement filters.
