# Source: https://docs.aws.amazon.com/kinesisvideostreams-webrtc-dg/latest/devguide/llms.txt

# Kinesis Video Streams Amazon Kinesis Video Streams WebRTC Developer Guide

- [Use IPv6/Dual-Stack endpoints with Amazon Kinesis Video WebRTC](https://docs.aws.amazon.com/kinesisvideostreams-webrtc-dg/latest/devguide/kvswebrtc-ipv6.html)
- [Multiviewer](https://docs.aws.amazon.com/kinesisvideostreams-webrtc-dg/latest/devguide/multiviewer.html)
- [Troubleshooting](https://docs.aws.amazon.com/kinesisvideostreams-webrtc-dg/latest/devguide/troubleshooting.html)
- [Document history](https://docs.aws.amazon.com/kinesisvideostreams-webrtc-dg/latest/devguide/doc-history.html)

## [What is Amazon Kinesis Video Streams with WebRTC?](https://docs.aws.amazon.com/kinesisvideostreams-webrtc-dg/latest/devguide/what-is-kvswebrtc.html)

- [Region availability](https://docs.aws.amazon.com/kinesisvideostreams-webrtc-dg/latest/devguide/availability.html): What regions support Amazon Kinesis Video Streams with WebRTC?
- [How it works](https://docs.aws.amazon.com/kinesisvideostreams-webrtc-dg/latest/devguide/kvswebrtc-how-it-works.html): How WebRTC works in Amazon Kinesis Video Streams.
- [System requirements](https://docs.aws.amazon.com/kinesisvideostreams-webrtc-dg/latest/devguide/kvswebrtc-requirements.html): This section covers basic system requirements for using Amazon Kinesis Video Streams with WebRTC, including network requirements and environment.
- [Quotas](https://docs.aws.amazon.com/kinesisvideostreams-webrtc-dg/latest/devguide/kvswebrtc-limits.html): API service quotas for Amazon Kinesis Video Streams with WebRTC.
- [Access Kinesis Video Streams with WebRTC](https://docs.aws.amazon.com/kinesisvideostreams-webrtc-dg/latest/devguide/kvswebrtc-accessing.html): You can work with Kinesis Video Streams with WebRTC in any of the following ways:


## [Getting started](https://docs.aws.amazon.com/kinesisvideostreams-webrtc-dg/latest/devguide/kvswebrtc-getting-started.html)

- [Set up an AWS account](https://docs.aws.amazon.com/kinesisvideostreams-webrtc-dg/latest/devguide/set-up-account.html): Set up an AWS account and start using Kinesis Video Streams.
- [Create a signaling channel](https://docs.aws.amazon.com/kinesisvideostreams-webrtc-dg/latest/devguide/create-channel.html): Use the Kinesis Video Streams console, AWS APIs, or the AWS CLI to create your first signaling channel.
- [Quick start: Ingenic T31](https://docs.aws.amazon.com/kinesisvideostreams-webrtc-dg/latest/devguide/quick-start-t31.html): Quick start guide for Amazon Kinesis Video Streams with WebRTC on Ingenic T31 hardware.


## [Stream live media (SDKs)](https://docs.aws.amazon.com/kinesisvideostreams-webrtc-dg/latest/devguide/webrtc-sdks.html)

- [C SDK for embedded devices](https://docs.aws.amazon.com/kinesisvideostreams-webrtc-dg/latest/devguide/kvswebrtc-sdk-c.html): WebRTC SDK in C for embedded devices
- [JavaScript SDK for web applications](https://docs.aws.amazon.com/kinesisvideostreams-webrtc-dg/latest/devguide/kvswebrtc-sdk-js.html): Kinesis Video Streams with WebRTC SDK in JavaScript for Web Applications
- [Android SDK](https://docs.aws.amazon.com/kinesisvideostreams-webrtc-dg/latest/devguide/kvswebrtc-sdk-android.html): Kinesis Video Streams with WebRTC SDK for Android.
- [iOS SDK](https://docs.aws.amazon.com/kinesisvideostreams-webrtc-dg/latest/devguide/kvswebrtc-sdk-ios.html): Amazon Kinesis Video Streams WebRTC SDK for iOS
- [Client metrics for the C SDK](https://docs.aws.amazon.com/kinesisvideostreams-webrtc-dg/latest/devguide/kvswebrtc-reference.html): Client metrics for the Amazon Kinesis Video Streams with WebRTC C SDK.


## [Ingest and store media](https://docs.aws.amazon.com/kinesisvideostreams-webrtc-dg/latest/devguide/webrtc-ingestion.html)

- [What is WebRTC ingestion and storage?](https://docs.aws.amazon.com/kinesisvideostreams-webrtc-dg/latest/devguide/getting-started-ingestion.html): Describes Amazon Kinesis Video Streams with WebRTC ingestion and storage.
- [Create a signaling channel](https://docs.aws.amazon.com/kinesisvideostreams-webrtc-dg/latest/devguide/ingestion-create-channel.html): A Kinesis Video Streams with WebRTC signaling channel facilitates the exchange of signaling messages required to establish and maintain peer-to-peer connections between WebRTC clients.
- [Create a video stream](https://docs.aws.amazon.com/kinesisvideostreams-webrtc-dg/latest/devguide/ingestion-create-stream.html): Follow these procedures to create a stream that the media will be ingested to.
- [Grant permission](https://docs.aws.amazon.com/kinesisvideostreams-webrtc-dg/latest/devguide/ingestion-grant-permission.html): You must grant stream permission to your IAM roles in order to ingest streams in Amazon Kinesis Video Streams with WebRTC.
- [Configure destination](https://docs.aws.amazon.com/kinesisvideostreams-webrtc-dg/latest/devguide/configure-ingestion.html): Once you've created the Kinesis Video Streams resources, you need to tell the signaling channel which stream to save it to.
- [Ingest media](https://docs.aws.amazon.com/kinesisvideostreams-webrtc-dg/latest/devguide/ingest-media.html): This page contains information about how to ingest media.
- [Playback ingested media](https://docs.aws.amazon.com/kinesisvideostreams-webrtc-dg/latest/devguide/ingestion-view-media.html): Follow these steps to playback ingested media from Amazon Kinesis Video Streams streams.
- [Connect to the storage session](https://docs.aws.amazon.com/kinesisvideostreams-webrtc-dg/latest/devguide/ingestion-initiate.html): Follow these procedures to create the storage session and start the WebRTC connection process.
- [Troubleshoot storage session connections](https://docs.aws.amazon.com/kinesisvideostreams-webrtc-dg/latest/devguide/troubleshoot-establish-storage.html): Use this information to troubleshoot issues when you're establishing a connection with the storage session.


## [Security](https://docs.aws.amazon.com/kinesisvideostreams-webrtc-dg/latest/devguide/kvswebrtc-security.html)

- [Control access to resources with IAM](https://docs.aws.amazon.com/kinesisvideostreams-webrtc-dg/latest/devguide/kvswebrtc-how-iam.html): How to use IAM roles and permissions to control access to Kinesis Video Streams with WebRTC resources
- [Compliance validation](https://docs.aws.amazon.com/kinesisvideostreams-webrtc-dg/latest/devguide/SERVICE-compliance.html): Learn what AWS services are in scope of a specific compliance program.
- [Resilience](https://docs.aws.amazon.com/kinesisvideostreams-webrtc-dg/latest/devguide/kvswebrtc-disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy and specific Kinesis Video Streams with WebRTC features for data resiliency.
- [Infrastructure security](https://docs.aws.amazon.com/kinesisvideostreams-webrtc-dg/latest/devguide/kvswebrtc-infrastructure-security.html): Learn how Kinesis Video Streams with WebRTC isolates service traffic.
- [Security best practices](https://docs.aws.amazon.com/kinesisvideostreams-webrtc-dg/latest/devguide/kvswebrtc-security-best-practices.html): Security best practices for Kinesis Video Streams with WebRTC.
- [WebRTC encryption](https://docs.aws.amazon.com/kinesisvideostreams-webrtc-dg/latest/devguide/kvswebrtc-encryption.html): End to end encryption is a mandatory feature of Amazon Kinesis Video Streams with WebRTC, and Kinesis Video Streams enforces it on all the components, including signaling and media or data streaming.


## [Monitor metrics and API calls](https://docs.aws.amazon.com/kinesisvideostreams-webrtc-dg/latest/devguide/kvswebrtc-monitoring.html)

- [Monitor Kinesis Video Streams with WebRTC](https://docs.aws.amazon.com/kinesisvideostreams-webrtc-dg/latest/devguide/kvswebrtc-monitoring-cw.html): Learn about how you can monitor Amazon Kinesis Video Streams with WebRTC using Amazon CloudWatch.
- [Log API calls with CloudTrail](https://docs.aws.amazon.com/kinesisvideostreams-webrtc-dg/latest/devguide/kvswebrtc-monitoring-ct.html): Log Kinesis Video Streams with WebRTC API Calls with AWS CloudTrail


## [API reference](https://docs.aws.amazon.com/kinesisvideostreams-webrtc-dg/latest/devguide/kvswebrtc-websocket-apis.html)

### [WebSocket endpoint APIs](https://docs.aws.amazon.com/kinesisvideostreams-webrtc-dg/latest/devguide/api-endpoint.html)

Amazon Kinesis Video Streams with WebRTC webSocket endpoint APIs: ConnectAsViewer and ConnectAsMaster.

- [ConnectAsMaster](https://docs.aws.amazon.com/kinesisvideostreams-webrtc-dg/latest/devguide/ConnectAsMaster.html): ConnectAsMaster
- [ConnectAsViewer](https://docs.aws.amazon.com/kinesisvideostreams-webrtc-dg/latest/devguide/ConnectAsViewer.html): ConnectAsViewer

### [Asynchronous message reception](https://docs.aws.amazon.com/kinesisvideostreams-webrtc-dg/latest/devguide/async-message-reception-api.html)

Asynchronous Message Reception

- [SendSdpOffer](https://docs.aws.amazon.com/kinesisvideostreams-webrtc-dg/latest/devguide/SendSdpOffer.html): SendSdpOffer
- [SendSdpAnswer](https://docs.aws.amazon.com/kinesisvideostreams-webrtc-dg/latest/devguide/SendSdpAnswer.html): SendSdpAnswer
- [SendIceCandidate](https://docs.aws.amazon.com/kinesisvideostreams-webrtc-dg/latest/devguide/SendIceCandidate.html): SendIceCandidate
- [Disconnect](https://docs.aws.amazon.com/kinesisvideostreams-webrtc-dg/latest/devguide/Disconnect.html): Disconnect
