# Source: https://firebase.google.com/docs/cloud-messaging/send/firebase-console.md.txt

[Video](https://www.youtube.com/watch?v=R3cbfZKfmkE)

You can send notification messages using
[the Notifications composer](https://console.firebase.google.com/project/_/notification)
in the Firebase console. Though this does not
provide the same flexibility or scalability as sending messages with the
[Firebase Admin SDK](https://firebase.google.com/docs/cloud-messaging/send/admin-sdk) or the
[HTTP v1 API](https://firebase.google.com/docs/cloud-messaging/send/v1-api), it can be
very useful for testing or for highly targeted marketing and user engagement.
The Firebase console provides analytics-based
[A/B testing](https://firebase.google.com/docs/ab-testing/abtest-with-console) to help refine and
improve marketing messages.

After you have developed logic in your app to receive messages, you can allow
non-technical users to send messages with
[the Notifications composer](https://console.firebase.google.com/project/_/notification).

## About

When you send a notification message from
[the Notifications composer](https://console.firebase.google.com/project/_/notification),
FCM uses the values you enter in the form fields in these ways:

- Fields like **User segment** and **Expires** determine the message target and delivery options.
- Fields like **Notification text** and **Custom data** are sent to the client in a payload comprised of key-value pairs.

These fields map to keys available through the
[`Message`](https://firebase.google.com/docs/reference/fcm/rest/v1/projects.messages#resource:-message)
object. For example, key-value pairs entered in the **Custom data**
field of the composer are handled as a
[`data`](https://firebase.google.com/docs/reference/fcm/rest/v1/projects.messages#Message.FIELDS.data)
payload for the notification. Other fields map directly to keys in the
[`notification`](https://firebase.google.com/docs/reference/fcm/rest/v1/projects.messages#notification)
object or in the platform-specific
notification configuration.

Note that some fields in
[the Notifications composer](https://console.firebase.google.com/project/_/notification)
are *not* available through the FCM API. For example,
you can target user segments based on app version, language,
browser type and version, or user properties in ways that are
not available using the server API.

> [!CAUTION]
> **Caution:** In another important difference from programmatic messaging, the console lets you cancel any scheduled message that is not already in progress. **Once a message fanout is actually in progress, it is
> fully committed and cannot be canceled through the console nor by
> Firebase support.**

The keys that the Firebase console sends to clients are:

| Key | Console field label | Description |
|---|---|---|
| `notification.title` | Notification title | Indicates notification title. |
| `notification.body` | Notification text | Indicates notification body text. |
| `data` | Custom data | Key/value pairs that you define. These are delivered as a data payload for the app to handle. |

Keys that influence message delivery behavior include:

| Key | Console field label | Description |
|---|---|---|
| `sound` | Sound | Indicates a sound to play when the device receives a notification. |
| `time_to_live` | Expires | This parameter specifies how long (in seconds) the message should be kept in FCM storage if the device is offline. For more information, see [Setting the lifespan of a message](https://firebase.google.com/docs/cloud-messaging/customize-messages/setting-message-lifespan). |