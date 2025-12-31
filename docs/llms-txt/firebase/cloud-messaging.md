# Source: https://firebase.google.com/docs/cloud-messaging.md.txt

# Firebase Cloud Messaging

plat_iosplat_androidplat_webplat_flutterplat_cppplat_unity  
Firebase Cloud Messaging(FCM) is a cross-platform messaging solution that lets you reliably send messages.  
UsingFCM, you can notify a client app that new email or other data is available to sync. You can send notification messages to drive user re-engagement and retention. For use cases such as instant messaging, a message can transfer a payload of up to 4096 bytes to a client app.

<br />

<br />

Ready to get started? Choose your platform:

[iOS+](https://firebase.google.com/docs/cloud-messaging/get-started?platform=ios)[Android](https://firebase.google.com/docs/cloud-messaging/get-started?platform=android)[Web](https://firebase.google.com/docs/cloud-messaging/get-started?platform=web)[Flutter](https://firebase.google.com/docs/cloud-messaging/get-started?platform=flutter)

[Unity](https://firebase.google.com/docs/cloud-messaging/get-started?platform=unity)[C++](https://firebase.google.com/docs/cloud-messaging/get-started?platform=cpp)

## Key capabilities

|---------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Send notification messages or data messages | Send notification messages that are displayed to your user. Or send data messages and determine completely what happens in your application code. See[Message types](https://firebase.google.com/docs/cloud-messaging/customize-messages/set-message-type). |
| Versatile message targeting                 | Distribute messages to your client app in any of 3 ways---to single devices, to groups of devices, or to devices subscribed to topics.                                                                                                                      |

## How does it work?

<br />

AnFCMimplementation includes two main components for sending and receiving:

1. A trusted environment such asCloud Functions for Firebaseor an app server on which to build, target, and send messages.
2. An Apple, Android, or web (JavaScript) client app that receives messages via the corresponding platform-specific transport service.

<br />

You can send messages via the[FirebaseAdmin SDK](https://firebase.google.com/docs/cloud-messaging/send/admin-sdk)or the[FCM server protocol](https://firebase.google.com/docs/cloud-messaging/send/v1-api). You can use[the Notifications composer](https://console.firebase.google.com/project/_/notification)for testing and to send marketing or engagement messages using powerful built-in targeting and analytics or custom[imported segments](https://firebase.google.com/docs/projects/import-segments).

<br />

<br />

See the[architectural overview](https://firebase.google.com/docs/cloud-messaging/fcm-architecture)for more detail and important information about the components ofFCM.

<br />

## Implementation path

|---|-------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|   | Set up theFCMSDK        | Set up Firebase andFCMon your app according to the setup instructions for your platform.                                                                                                                                                               |
|   | Develop your client app | Add message handling, topic subscription logic, or other optional features to your client app. During the development, you can easily send test messages from[the Notifications composer](https://console.firebase.google.com/project/_/notification). |
|   | Develop your app server | Decide whether you want to use theFirebaseAdmin SDKor the server protocol to create your sending logic---logic to authenticate, build send requests, handle responses, and so on. Then build out the logic in your trusted environment.                |

## Next steps

- Follow the[Get started guide](https://firebase.google.com/docs/cloud-messaging/get-started)to set up your client apps and learn to send messages withFCM.

- Run the[Android](https://github.com/firebase/quickstart-android/tree/master/messaging)or[iOS](https://github.com/firebase/quickstart-ios/tree/master/messaging/)Quickstart sample.

- Learn how to[receive messages](https://firebase.google.com/docs/cloud-messaging/receive-messages)in your client app.

- Set up your[server environment](https://firebase.google.com/docs/cloud-messaging/server-environment)to build and send message requests. You can write sending logic using the[Admin SDK](https://firebase.google.com/docs/cloud-messaging/send/admin-sdk)or the[FCM v1 API](https://firebase.google.com/docs/cloud-messaging/send/v1-api).

- Explore advanced features, such as targeting groups with[topic messaging](https://firebase.google.com/docs/cloud-messaging/topic-messaging), and learn how to[understand message delivery](https://firebase.google.com/docs/cloud-messaging/understand-delivery)with theFCMData API and BigQuery export.

- Learn more aboutFCMin the[architecture overview](https://firebase.google.com/docs/cloud-messaging/fcm-architecture)and review best practices for[sending messages at scale](https://firebase.google.com/docs/cloud-messaging/scale-fcm)and[managing registration tokens](https://firebase.google.com/docs/cloud-messaging/manage-tokens).