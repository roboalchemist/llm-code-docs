# Source: https://firebase.google.com/docs/cloud-messaging/customize-messages/collapsible-message-types.md.txt

A **non-collapsible message** means that each individual message is
delivered to the device. A non-collapsible message delivers some useful
content. While a collapsible message like a content-free "ping" to
a mobile app to contact the server to fetch data.

> [!CAUTION]
> FCM doesn't guarantee the order of delivery.

Some typical use cases of non-collapsible messages are chat messages or
critical messages. For Android, there is a limit of 100 messages that can be
stored without collapsing. If the
limit is reached, all stored messages are discarded. When the device is back
online, it receives a special message indicating that the limit was reached.
The app can then handle the situation by typically requesting a full
sync from the app server.

A **collapsible message** is a message that may be replaced by a
new message if it has yet to be delivered to the device.

A common use case of collapsible messages: messages used to tell
a mobile app to sync data from the server. An
example would be a sports app that updates users with the latest score.
Only the most recent message is relevant.

To mark a message as collapsible on Android, include the
`collapse_key` parameter in
the message payload. By default, the collapse key is the app package name
registered in the Firebase console. The FCM server can
simultaneously store four different collapsible messages per
device, each with a different collapse key. If you exceed this number,
FCM only keeps
four collapse keys, with no determining factor on which keys are kept.

Topic messages with no payload are collapsible by default. Notification messages
are always collapsible and will ignore the `collapse_key` parameter.

## Which should I use?

Collapsible messages are the preferred option from a performance standpoint,
provided your app doesn't need to use non-collapsible messages. However,
if you use collapsible messages, remember that
FCM only allows a maximum of four different collapse keys to be used
by FCM per
registration token at any given time.

<br />

|   | Use scenario | How to send |
|---|---|---|
| Non-collapsible | Every message is important to the client app and needs to be delivered. | Except for notification messages, all messages are non-collapsible by default. |
| Collapsible | When there is a newer message that renders an older, related message irrelevant to the client app, FCM replaces the older message. For example: outdated notification messages. | Set the appropriate parameter in your message request: - `collapseKey` on [AndroidConfig](https://firebase.google.com/docs/reference/fcm/rest/v1/projects.messages#androidconfig) - `apns-collapse-id` on [ApnsConfig](https://firebase.google.com/docs/reference/fcm/rest/v1/projects.messages#apnsconfig) - `Topic` on [WebpushConfig](https://firebase.google.com/docs/reference/fcm/rest/v1/projects.messages#webpushconfig) |

<br />