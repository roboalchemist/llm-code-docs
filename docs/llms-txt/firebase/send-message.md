# Source: https://firebase.google.com/docs/cloud-messaging/send-message.md.txt

<br />

<br />

Using the Firebase Admin SDK or FCM app server protocols,
you can build message requests and send them to these types of targets:

- Topic name
- Condition
- Device registration token
- Device group name (protocol only)

You can send messages with a notification payload made up
of predefined fields, a data payload of your own user-defined fields, or a
message containing both types of payload.
See [Message types](https://firebase.google.com/docs/cloud-messaging/customize-messages/set-message-type)
for more information.
| **Important:** Send requests for both the Firebase Admin SDK and v1 HTTP protocol must contain the project ID of the Firebase project for your app, available in the [General project settings](https://console.firebase.google.com/project/_/settings/general/) tab of the Firebase console. Also, both methods of sending messages require you to [authorize send requests](https://firebase.google.com/docs/cloud-messaging/auth-server).

Examples in this page show how to send notification messages using the
Firebase Admin SDK
(which has support for
[Node](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging),
[Java](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/package-summary),
[Python](https://firebase.google.com/docs/reference/admin/python/firebase_admin.messaging),
[C#](https://firebase.google.com/docs/reference/admin/dotnet/namespace/firebase-admin/messaging),
and
[Go](https://godoc.org/firebase.google.com/go/messaging)) and the
[v1 HTTP protocol](https://firebase.google.com/docs/reference/fcm/rest/v1/projects.messages).

## Send direct boot-enabled messages (Android only)

You can send messages to devices in direct boot mode using the
HTTP v1 or legacy HTTP APIs. Before sending to
devices in direct boot mode, make sure you have completed the steps to
enable client devices to receive FCM messages in [direct boot mode](https://firebase.google.com/docs/cloud-messaging/android/receive#receive_fcm_messages_in_direct_boot_mode).
| **Caution:** It's important to consider the *visibility* of direct boot- enabled messages; any user with access to the device can view these messages without entering user credentials.

### Send using the FCM v1 HTTP API

The message request must include the key `"direct_boot_ok" : true` in the
`AndroidConfig` options of the request body. For example:  

    https://fcm.googleapis.com/v1/projects/myproject-b5ae1/messages:send
    Content-Type:application/json
    Authorization: Bearer ya29.ElqKBGN2Ri_Uz...HnS_uNreA

    {
      "message":{
        "token" : "bk3RNwTe3H0:CI2k_HHwgIpoDKCIZvvDMExUdFQ3P1..."
        "data": {
          "score": "5x1",
          "time": "15:10"
        },
        "android": {
          "direct_boot_ok": true,
        },
    }