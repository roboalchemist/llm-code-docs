# Source: https://firebase.google.com/docs/cloud-messaging/server-environment.md.txt

<br />

The server side ofFirebase Cloud Messagingconsists of two components:

- The**FCMbackend**provided by Google.
- Your**app server** or other**trusted server environment** where your server logic runs, such as[Cloud Functions for Firebase](https://firebase.google.com/docs/functions)or other cloud environments managed by Google.

| **Tip:** If you need to configure your enterprise network or VPN to allow traffic to and fromFCMservers, see[Configure your Network forFCM](https://firebase.google.com/docs/cloud-messaging/network-configuration).

Your app server or trusted server environment sends message requests to theFCMbackend, which then routes messages to client apps running on users' devices.

Using theFirebaseAdmin SDKorFCMapp server protocols, you can build message requests and send them to these types of targets:

- Topic name
- Condition
- FCMregistration token
- Device group name (protocol only)

You can send messages with a notification payload made up of predefined fields, a data payload of your own user-defined fields, or a message containing both types of payload. See[Message types](https://firebase.google.com/docs/cloud-messaging/customize-messages/set-message-type)for more information.

## Requirements for the trusted server environment

Your app server environment must meet the following criteria:

- Able to send properly formatted message requests to theFCMbackend.
- Able to handle requests and resend them using[exponential back-off.](https://developers.google.com/api-client-library/java/google-http-java-client/backoff)
- Able to securely store server authorization credentials and client registration tokens.

## Required credentials for Firebase project

Depending on whichFCMfeatures you implement, you may need the following credentials from your Firebase project:

|     Credential     |                                                                                                                                                                             Description                                                                                                                                                                              |
|--------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Project ID         | A unique identifier for your Firebase project, used in requests to theFCMv1 HTTP endpoint. This value is available in the[Firebaseconsole**Settings**](https://console.firebase.google.com/project/_/settings/general)pane.                                                                                                                                          |
| Registration token | A unique token string that identifies each client app instance. The registration token is required for single app instance and device group messaging. Note that registration tokens must be kept secret.                                                                                                                                                            |
| Sender ID          | A unique numerical value created when you create your Firebase project, available in the[Cloud Messaging](https://console.firebase.google.com/project/_/settings/cloudmessaging/)tab of theFirebaseconsole**Settings**pane. The sender ID is the same as the project number. The sender ID is used to identify each sender that can send messages to the client app. |
| Access token       | A short-lived OAuth 2.0 token that authorizes requests to the HTTP v1 API. This token is associated with a service account that belongs to your Firebase project. To create and rotate access tokens, follow the steps described in[Authorize Send Requests](https://firebase.google.com/docs/cloud-messaging/send/v1-api#authorize-http-v1-send-requests).          |

| **Important:** Send requests for both theFirebaseAdmin SDKand v1 HTTP protocol must contain the project ID of the Firebase project for your app, available in the[General project settings](https://console.firebase.google.com/project/_/settings/general/)tab of theFirebaseconsole. Also, both methods of sending messages require you to[authorize send requests](https://firebase.google.com/docs/cloud-messaging/send/v1-api#authorize-http-v1-send-requests).

## Choose a server option

You'll need to decide on a way to interact withFCMservers: either using the[FirebaseAdmin SDK](https://firebase.google.com/docs/cloud-messaging/server-environment#admin-sdk)or the[FCMHTTP v1 API](https://firebase.google.com/docs/cloud-messaging/server-environment#http-v1-api). Because of its support across popular programming languages and its convenience methods for handling authentication and authorization, theFirebaseAdmin SDKis the recommended method.

Options for interacting withFCMservers include the following:

- TheFirebaseAdmin SDK, which has support for[Node](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging),[Java](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/package-summary),[Python](https://firebase.google.com/docs/reference/admin/python/firebase_admin.messaging),[C#](https://firebase.google.com/docs/reference/admin/dotnet/namespace/firebase-admin/messaging), and[Go](https://godoc.org/firebase.google.com/go/messaging).

- The[FCMHTTP v1 API](https://firebase.google.com/docs/reference/fcm/rest/v1/projects.messages), a REST API with secure authorization and flexible[cross-platform messaging capabilities](https://firebase.google.com/docs/cloud-messaging/send-message#customize-messages-across-platforms)(theFirebaseAdmin SDKis based on this protocol and provides all of its inherent advantages).

### FirebaseAdmin SDK

TheFirebaseAdmin SDKhandles authenticating with the backend and facilitates sending messages and managing topic subscriptions. With theFirebaseAdmin SDK, you can:

- Send messages to individual app instances
- Send messages to topics and condition statements that match one or more topics
- Send messages to device groups
- Subscribe and unsubscribe app instances to and from topics
- Construct message payloads tailored to different target platforms

To set up theFirebaseAdmin SDK, see[Add theFirebaseAdmin SDKto Your Server](https://firebase.google.com/docs/admin/setup). If you already have a Firebase project, start with[Add the SDK](https://firebase.google.com/docs/admin/setup#add-sdk). Also, make sure to enable the Firebase Cloud Messaging API (V1) in the[Cloud Messaging settings page](https://console.firebase.google.com/project/_/settings/cloudmessaging/)for your project. Then, once theFirebaseAdmin SDKis installed, you can start writing logic to[build send requests](https://firebase.google.com/docs/cloud-messaging/send/admin-sdk).

### FCMHTTP v1 API

FCMprovides the[FCMHTTP v1 API](https://firebase.google.com/docs/reference/fcm/rest/v1/projects.messages)for developers who prefer a raw server protocol.

To send a message, the app server issues a POST request with an HTTP header and an HTTP body comprised of JSON key value pairs. For details on the header and body options, see[Send a Message usingFCMHTTP v1 API](https://firebase.google.com/docs/cloud-messaging/send/v1-api).