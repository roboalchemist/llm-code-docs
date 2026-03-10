# Source: https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/llms.txt

# Amazon IVS Real-Time Streaming User Guide

> Introduces you to and helps you get started with Amazon IVS real-time streaming. Provides instructions on using various features with the console, API, and command-line interface. Includes information about using the Amazon IVS Player on various platforms.

- [What is IVS Real-Time Streaming?](https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/what-is.html)
- [Monitoring](https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/stage-health.html)
- [Using Amazon EventBridge with IVS](https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/eventbridge.html)
- [Participant Replication](https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/rt-participant-replication.html)
- [Service Quotas](https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/service-quotas.html)
- [Streaming Optimizations](https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/real-time-streaming-optimization.html)
- [Network Requirements](https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/real-time-network-requirements.html)
- [Costs](https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/rt-costs.html)
- [Resources & Support](https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/resources-and-support.html)
- [Glossary](https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/ivs-glossary.html)
- [Document History](https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/doc-history.html)
- [Release Notes](https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/release-notes.html)

## [Getting Started with IVS](https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/getting-started.html)

- [Introduction](https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/getting-started-introduction.html): This section lists prerequisites for using real-time streaming and introduces key terminology.
- [Step 1: Set Up IAM Permissions](https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/getting-started-iam-permissions.html): Next, you must create an AWS Identity and Access Management (IAM) policy that gives users a basic set of permissions (e.g., to create an Amazon IVS stage and create participant tokens) and assign that policy to users.
- [Step 2: Create a Stage with Optional Participant Recording](https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/getting-started-create-stage.html): A stage is a virtual space where participants can exchange video in real time.
- [Step 3: Distribute Participant Tokens](https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/getting-started-distribute-tokens.html): Now that you have a stage, you need to create tokens and distribute them to participants, to enable the participants to join the stage and start sending and receiving video.
- [Step 4: Integrate the IVS Broadcast SDK](https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/getting-started-broadcast-sdk.html): IVS provides a broadcast SDK for web, Android, and iOS that you can integrate into your application.

### [Step 5: Publish and Subscribe to Video](https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/getting-started-pub-sub.html)

You can publish/subscribe (real-time) to IVS with:

- [Web](https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/getting-started-pub-sub-web.html): This section takes you through the steps involved in publishing and subscribing to a stage using your web app.
- [Android](https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/getting-started-pub-sub-android.html): This section takes you through the steps involved in publishing and subscribing to a stage using your Android app.
- [iOS](https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/getting-started-pub-sub-ios.html): This section takes you through the steps involved in publishing and subscribing to a stage using your iOS app.


## [IVS Broadcast SDK](https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/broadcast.html)

### [Web Guide](https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/broadcast-web.html)

Broadcast from web environments using WebRTC, with cross-browser and cross-platform support.

- [Getting Started](https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/broadcast-web-getting-started.html): This document takes you through the steps involved in getting started with the IVS real-time streaming Web broadcast SDK.
- [Publishing and Subscribing](https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/web-publish-subscribe.html): This document takes you through the steps involved in publishing and subscribing to a stage using the IVS real-time streaming Web broadcast SDK.
- [Known Issues and Workarounds](https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/broadcast-web-known-issues.html): This document lists known issues that you might encounter when using the Amazon IVS real-time streaming Web broadcast SDK and suggests potential workarounds.
- [Error Handling](https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/broadcast-web-error-handling.html): This section is an overview of error conditions, how the Web broadcast SDK reports them to the application, and what an application should do when those errors are encountered.

### [Android Guide](https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/broadcast-android.html)

Use the IVS Android broadcast SDK to create a broadcast configuration and session, start/stop broadcasts, attach/swap cameras, capture screen and system audio, and various other use cases.

- [Getting Started](https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/broadcast-android-getting-started.html): This document takes you through the steps involved in getting started with the IVS real-time streaming Android broadcast SDK.
- [Publishing and Subscribing](https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/android-publish-subscribe.html): This document takes you through the steps involved in publishing and subscribing to a stage using the IVS real-time streaming Android broadcast SDK.
- [Known Issues and Workarounds](https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/broadcast-android-known-issues.html): This document lists known issues that you might encounter when using the Amazon IVS real-time streaming Android broadcast SDK and suggests potential workarounds.
- [Error Handling](https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/broadcast-android-error-handling.html): This section is an overview of error conditions, how the IVS real-time streaming Android broadcast SDK reports them to the application, and what an application should do when those errors are encountered.

### [iOS Guide](https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/broadcast-ios.html)

Use the IVS iOS broadcast SDK to create a broadcast configuration and session, start/stop broadcasts, attach/swap cameras, capture screen and system audio, and various other use cases.

- [Getting Started](https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/broadcast-ios-getting-started.html): This document takes you through the steps involved in getting started with the IVS real-time streaming iOS broadcast SDK.
- [Publishing and Subscribing](https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/ios-publish-subscribe.html): This document takes you through the steps involved in publishing and subscribing to a stage using the IVS real-time streaming iOS broadcast SDK.
- [How iOS Chooses Camera Resolution and Frame Rate](https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/ios-publish-subscribe-resolution-framerate.html): The camera managed by the broadcast SDK optimizes its resolution and frame rate (frames-per-second, or FPS) to minimize heat production and energy consumption.
- [Known Issues and Workarounds](https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/broadcast-ios-known-issues.html): This document lists known issues that you might encounter when using the Amazon IVS real-time streaming iOS broadcast SDK and suggests potential workarounds.
- [Error Handling](https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/broadcast-ios-error-handling.html): This section is an overview of error conditions, how the IVS real-time streaming iOS broadcast SDK reports them to the application, and what an application should do when those errors are encountered.
- [Mixed Devices](https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/broadcast-mixed-devices.html): Combine video and audio from multiple sources such as cameras, microphones, screen captures, and audio and video generated by your app.
- [Token Exchange](https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/broadcast-mobile-token-exchange.html): Token exchange enables you to upgrade or downgrade participant-token capabilities and update token attributes within the mobile broadcast SDK, without requiring participants to reconnect.
- [Custom Image Sources](https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/broadcast-custom-image-sources.html): Provide a custom image input to the broadcast SDK, instead of being limited to the preset cameras or screen share.
- [Custom Audio Sources](https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/broadcast-custom-audio-sources.html): Provide a custom audio input to the broadcast SDK, instead of being limited to the preset cameras or screen share.

### [Third-Party Camera Filters](https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/broadcast-3p-camera-filters.html)

Use camera filters to augment or alter facial or background appearance.

- [Integrating Third-Party Camera Filters](https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/broadcast-3p-camera-filters-integrating.html): You can integrate third-party camera filter SDKs with the IVS broadcast SDK by feeding the filter SDKâs output to a custom image input source.
- [BytePlus](https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/broadcast-3p-camera-filters-integrating-byteplus.html): This document explains how to use the BytePlus Effects SDK with the IVS broadcast SDK.
- [DeepAR](https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/broadcast-3p-camera-filters-integrating-deepar.html): This document explains how to use the DeepAR SDK with the IVS broadcast SDK.
- [Snap](https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/broadcast-3p-camera-filters-integrating-snap.html): This document explains how to use Snapâs Camera Kit SDK with the IVS broadcast SDK.
- [Background Replacement](https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/broadcast-3p-camera-filters-background-replacement.html): Background replacement is a type of camera filter that enables live-stream creators to change their backgrounds.
- [Mobile Audio Modes](https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/broadcast-mobile-audio-modes.html): Ensure that your users have the best experience when listening to an IVS real-time stream.


## [Server-Side Composition](https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/server-side-composition.html)

- [Overview](https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/ssc-overview.html): Overview of server-side composition, which uses an IVS server to mix audio and video from all stage participants and then sends this mixed video to an IVS channel.
- [Getting Started](https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/ssc-getting-started.html): Getting started with server-side composition, which uses an IVS server to mix audio and video from all stage participants and then sends this mixed video to an IVS channel.
- [Custom Participant Ordering](https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/ssc-getting-started-custom-participant-ordering.html): Custom participant ordering allows you to control the positioning of participants in both grid and PiP layouts based on custom attribute values in participant tokens, including the positioning of the featured participants and selection of participants for the PiP window.
- [Enabling Screen Share](https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/ssc-getting-started-screen-share.html): How to screen share using server-side composition, which uses an IVS server to mix audio and video from all stage participants and then sends this mixed video to an IVS channel.
- [Known Issues and Workarounds](https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/ssc-known-issues.html): Known issues that you might encounter when using IVS server-side composition and suggested potential workarounds.


## [Recording](https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/rt-recording.html)

- [Individual Participant Recording](https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/rt-individual-participant-recording.html): Individual participant recording allows IVS real-time streaming customers to record IVS stage publishers individually into S3 buckets.
- [Composite Recording](https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/rt-composite-recording.html): Optionally enable recording to Amazon S3 while using Service-Side Composition with an IVS stage.


## [Stream Ingest](https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/rt-stream-ingest.html)

- [RTMP](https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/rt-rtmp-publishing.html): This document outlines the process of publishing to an IVS stage using RTMP.
- [WHIP](https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/obs-whip-support.html): Use WHIP-compatible encoders to publish to IVS real-time streaming.
