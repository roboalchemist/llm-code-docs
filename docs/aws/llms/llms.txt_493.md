# Source: https://docs.aws.amazon.com/ivs/latest/ChatUserGuide/llms.txt

# Amazon IVS Chat User Guide

> Introduces you to and helps you get started with Amazon IVS chat. Provides instructions on using various features with the console, API, and command-line interface.

- [What is IVS Chat?](https://docs.aws.amazon.com/ivs/latest/ChatUserGuide/what-is.html)
- [Chat Logging](https://docs.aws.amazon.com/ivs/latest/ChatUserGuide/chat-logging.html)
- [Chat Message Review Handler](https://docs.aws.amazon.com/ivs/latest/ChatUserGuide/chat-message-review-handler.html)
- [Monitoring](https://docs.aws.amazon.com/ivs/latest/ChatUserGuide/chat-health.html)
- [Service Quotas](https://docs.aws.amazon.com/ivs/latest/ChatUserGuide/service-quotas.html)
- [Troubleshooting](https://docs.aws.amazon.com/ivs/latest/ChatUserGuide/troubleshooting-faqs.html)
- [Glossary](https://docs.aws.amazon.com/ivs/latest/ChatUserGuide/ivs-glossary.html)
- [Document History](https://docs.aws.amazon.com/ivs/latest/ChatUserGuide/doc-history.html)
- [Release Notes](https://docs.aws.amazon.com/ivs/latest/ChatUserGuide/release-notes.html)

## [Getting Started with IVS Chat](https://docs.aws.amazon.com/ivs/latest/ChatUserGuide/getting-started-chat.html)

- [Step 1: Do Initial Setup](https://docs.aws.amazon.com/ivs/latest/ChatUserGuide/getting-started-chat-create-account.html): Before proceeding, you must:

### [Step 2: Create a Chat Room](https://docs.aws.amazon.com/ivs/latest/ChatUserGuide/getting-started-chat-create-room.html)

An Amazon IVS chat room has configuration information associated with it (e.g., maximum message length).

- [Console Instructions](https://docs.aws.amazon.com/ivs/latest/ChatUserGuide/create-room-console.html): These steps are divided into phases, starting with initial room setup and ending with final room creation.
- [CLI Instructions](https://docs.aws.amazon.com/ivs/latest/ChatUserGuide/create-room-cli.html): This document takes you through the steps involved in creating an Amazon IVS chat room using the AWS CLI.
- [Step 3: Create a Chat Token](https://docs.aws.amazon.com/ivs/latest/ChatUserGuide/getting-started-chat-auth.html): For a chat participant to connect to a room and start sending and receiving messages, a chat token must be created.
- [Step 4: Send and Receive Your First Message](https://docs.aws.amazon.com/ivs/latest/ChatUserGuide/getting-started-chat-send-and-receive.html): Use your chat token to connect to a chat room and send your first message.
- [Step 5: Check Your Service-Quota Limits (Optional)](https://docs.aws.amazon.com/ivs/latest/ChatUserGuide/getting-started-chat-check-service-quota.html): Your chat rooms will scale along with your Amazon IVS live stream, to enable all your viewers to engage in chat conversations.


## [IVS Chat Client Messaging SDK](https://docs.aws.amazon.com/ivs/latest/ChatUserGuide/chat-sdk.html)

### [Android Guide](https://docs.aws.amazon.com/ivs/latest/ChatUserGuide/chat-sdk-android.html)

Use the IVS Chat Client Messaging Android SDK to access interfaces that allow you to easily incorporate the IVS Chat Messaging API on platforms using Android.

- [Getting Started](https://docs.aws.amazon.com/ivs/latest/ChatUserGuide/chat-android-getting-started.html): Before starting, you should be familiar with Getting Started with Amazon IVS Chat.
- [Using the SDK](https://docs.aws.amazon.com/ivs/latest/ChatUserGuide/chat-android-using-sdk.html): This document takes you through the steps involved in using the Amazon IVS chat client messaging Android SDK.
- [Android Tutorial Part 1: Chat Rooms](https://docs.aws.amazon.com/ivs/latest/ChatUserGuide/chat-sdk-android-tutorial-chat-rooms.html): Learn the essentials of working with the Amazon IVS Chat Client Messaging Android SDK by building a fully functional Android app using the Kotlin programming language.
- [Android Tutorial Part 2: Messages and Events](https://docs.aws.amazon.com/ivs/latest/ChatUserGuide/chat-sdk-android-tutorial-messages-events.html): Learn the essentials of working with the Amazon IVS Chat Client Messaging Android SDK by building a fully functional Android app using the Kotlin programming language.
- [Kotlin Coroutines Tutorial Part 1: Chat Rooms](https://docs.aws.amazon.com/ivs/latest/ChatUserGuide/chat-sdk-kotlin-tutorial-chat-rooms.html): Learn the essentials of working with the Amazon IVS Chat Client Messaging SDK by building a fully functional app using Kotlin coroutines.
- [Kotlin Coroutines Tutorial Part 2: Messages and Events](https://docs.aws.amazon.com/ivs/latest/ChatUserGuide/chat-sdk-kotlin-tutorial-messages-events.html): Learn the essentials of working with the Amazon IVS Chat Client Messaging SDK by building a fully functional app using Kotlin coroutines.

### [iOS Guide](https://docs.aws.amazon.com/ivs/latest/ChatUserGuide/chat-sdk-ios.html)

Use the IVS Chat Client Messaging iOS SDK to access interfaces that allow you to easily incorporate the IVS Chat Messaging API on platforms using iOS.

- [Getting Started](https://docs.aws.amazon.com/ivs/latest/ChatUserGuide/chat-ios-getting-started.html): We recommend that you integrate the SDK via Swift Package Manager.
- [Using the SDK](https://docs.aws.amazon.com/ivs/latest/ChatUserGuide/chat-ios-using-sdk.html): This document takes you through the steps involved in using the Amazon IVS chat client messaging iOS SDK.
- [iOS Tutorial](https://docs.aws.amazon.com/ivs/latest/ChatUserGuide/chat-sdk-ios-tutorial.html): Learn how to bring the power of Amazonâs IVS Chat Messaging API to your own iOS app using Appleâs Swift programming language.

### [JavaScript Guide](https://docs.aws.amazon.com/ivs/latest/ChatUserGuide/chat-sdk-js.html)

Use the IVS Chat Client Messaging JavaScript SDK to access interfaces that allow you to easily incorporate the IVS Chat Messaging API on platforms using a Web browser.

- [Getting Started](https://docs.aws.amazon.com/ivs/latest/ChatUserGuide/chat-js-getting-started.html): Before starting, you should be familiar with Getting Started with Amazon IVS Chat.
- [Using the SDK](https://docs.aws.amazon.com/ivs/latest/ChatUserGuide/chat-js-using-sdk.html): This document takes you through the steps involved in using the Amazon IVS chat client messaging JavaScript SDK.
- [JavaScript Tutorial Part 1: Chat Rooms](https://docs.aws.amazon.com/ivs/latest/ChatUserGuide/chat-sdk-js-tutorial-chat-rooms.html): Learn the essentials of working with the Amazon IVS Chat Client Messaging JavaScript SDK by building a fully functional app using JavaScript/TypeScript.
- [JavaScript Tutorial Part 2: Messages and Events](https://docs.aws.amazon.com/ivs/latest/ChatUserGuide/chat-sdk-js-tutorial-messages-events.html): Learn the essentials of working with the Amazon IVS Chat Client Messaging JavaScript SDK by building a fully functional app using JavaScript/TypeScript.
- [React Native Tutorial Part 1: Chat Rooms](https://docs.aws.amazon.com/ivs/latest/ChatUserGuide/chat-sdk-react-tutorial-chat-rooms.html): Learn the essentials of working with the Amazon IVS Chat Client Messaging React Native SDK by building a fully functional app using React Native.
- [React Native Tutorial Part 2: Messages and Events](https://docs.aws.amazon.com/ivs/latest/ChatUserGuide/chat-sdk-react-tutorial-messages-events.html): Learn the essentials of working with the Amazon IVS Chat Client Messaging React Native SDK by building a fully functional app using React Native.
- [React & React Native Best Practices](https://docs.aws.amazon.com/ivs/latest/ChatUserGuide/chat-sdk-react-best-practices.html): Become familiar with the most important practices of using the Amazon IVS Chat Messaging SDK for React and React Native.


## [Security](https://docs.aws.amazon.com/ivs/latest/ChatUserGuide/security.html)

- [Chat Data Protection](https://docs.aws.amazon.com/ivs/latest/ChatUserGuide/security-data-protection.html): For data sent to Amazon Interactive Video Service (IVS) Chat, the following data protections are in place:
- [Identity and Access Management](https://docs.aws.amazon.com/ivs/latest/ChatUserGuide/security-iam.html): AWS Identity and Access Management (IAM) is an AWS service that helps an account administrator securely control access to AWS resources.
- [Managed Policies for IVS Chat](https://docs.aws.amazon.com/ivs/latest/ChatUserGuide/security-managed-policies.html): An AWS managed policy is a standalone policy that is created and administered by AWS.
- [Using Service-Linked Roles for IVS Chat](https://docs.aws.amazon.com/ivs/latest/ChatUserGuide/security-service-linked-roles.html): Amazon IVS uses AWS IAM service-linked roles.
- [Logging and Monitoring](https://docs.aws.amazon.com/ivs/latest/ChatUserGuide/security-logging-monitoring.html): To log performance and/or operations, use Amazon CloudTrail.
- [Incident Response](https://docs.aws.amazon.com/ivs/latest/ChatUserGuide/security-incident-response.html): To detect or alert for incidents, you can monitor your streamâs health via Amazon EventBridge events.
- [Resilience](https://docs.aws.amazon.com/ivs/latest/ChatUserGuide/security-resilience.html): IVS APIs use the AWS global infrastructure and is built around AWS Regions and Availability Zones.
- [Infrastructure Security](https://docs.aws.amazon.com/ivs/latest/ChatUserGuide/security-infrastructure.html): As a managed service, Amazon IVS is protected by the AWS global network security procedures.
