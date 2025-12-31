# Source: https://firebase.google.com/docs/cloud-messaging/concept-options.md.txt

<br />

Firebase Cloud Messaging (FCM) offers a broad range of messaging options
and capabilities. The information in this page is intended to
help you understand the different types of FCM messages and what you
can do with them.

### Notification messages with optional data payload

Both programmatically or via the Firebase console, you can send notification
messages that contain an optional payload of custom key-value pairs. In
the [Notifications composer](https://console.firebase.google.com/project/_/notification), use the **Custom data** fields in
**Advanced options**.

App behavior when receiving messages that include both notification and data
payloads depends on whether the app is in the background or the
foreground---essentially, whether or not it is active at the time of
receipt.

- **When in the
  background**, apps receive the notification payload in the notification tray, and only handle the data payload when the user taps on the notification.
- **When in the foreground**, your app receives a message object with both payloads available.

Here is a JSON-formatted message containing both the
`notification` key and the `data` key:

<br />

```scdoc
{
  "message":{
    "token":"bk3RNwTe3H0:CI2k_HHwgIpoDKCIZvvDMExUdFQ3P1...",
    "notification":{
      "title":"Portugal vs. Denmark",
      "body":"great match!"
    },
    "data" : {
      "Nick" : "Mario",
      "Room" : "PortugalVSDenmark"
    }
  }
}
```

<br />

## Delivery options

FCM provides a specific set of delivery options for messages sent to
Android devices, and allows for similar options on
Apple platforms and web. For example, "collapsible" message behavior is supported on
Android via FCM's `collapse_key`, on Apple via
`apns-collapse-id`, and on JavaScript/Web via `Topic`. For details, see
descriptions in this section and related reference documentation.

<br />

### Setting the priority of a message

<br />

<br />

You have two options for assigning delivery priority to downstream messages:
normal and high priority. Though the behavior differs slightly across
platforms, delivery of normal and high priority messages works
like this:

- **Normal priority.**
  Normal priority messages are delivered immediately when the app is in the
  foreground. For backgrounded apps, delivery may be
  delayed. For less time-sensitive messages, such as
  notifications of new email, keeping your UI in sync, or syncing app data in
  the background, choose normal delivery priority.

- **High priority.**FCM attempts to deliver high priority
  messages immediately even if the device is in Doze mode.
  High priority messages are for time-sensitive, user visible content.

<br />

| When sending data messages to Apple devices, the priority **must** be set to 5, or normal priority. Messages sent with high priority are rejected by the FCM backend with the error `INVALID_ARGUMENT`.

Here is an example of a normal priority message sent via the FCM
HTTP v1 protocol to notify a magazine
subscriber that new content is available to download:  

```text
{
  "message":{
    "topic":"subscriber-updates",
    "notification":{
      "body" : "This week's edition is now available.",
      "title" : "NewsMagazine.com",
    },
    "data" : {
      "volume" : "3.21.15",
      "contents" : "http://www.news-magazine.com/world-week/21659772"
    },
    "android":{
      "priority":"normal"
    },
    "apns":{
      "headers":{
        "apns-priority":"5"
      }
    },
    "webpush": {
      "headers": {
        "Urgency": "high"
      }
    }
  }
}
```

For more platform-specific detail on setting message priority:

- [APNs documentation](https://developer.apple.com/library/prerelease/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/CommunicatingwithAPNs.html#//apple_ref/doc/uid/TP40008194-CH11-SW1)
- [Set and manage message priority](https://firebase.google.com/docs/cloud-messaging/android/message-priority) (Android)
- [Web push message urgency](https://tools.ietf.org/html/rfc8030#section-5.3)

<br />

#### Life critical use cases

The FCM APIs are not
designed for emergency alerts or other high-risk activities where the use or
failure of the APIs could result in death, personal injury, or environmental
damage (such as the operation of nuclear facilities, air traffic control, or
life support systems). Any such use is expressly prohibited under
[Section 4. a.
7](https://developers.google.com/terms/#a_api_prohibitions) of the Terms of Service. You are solely responsible for managing your
app's compliance with the Terms, and any damages resulting from your
noncompliance.

Google provides the APIs "as is," and reserves the right to discontinue the APIs
or any portion or feature or your access thereto, for any reason and at any
time, without liability or other obligation to you or your users.

<br />

### Setting the lifespan of a message

<br />

<br />

FCM usually delivers messages immediately after they are sent.
However, this might not always be possible. For example, if the platform is
Android, the device could be turned off, offline, or otherwise unavailable.
Or FCM might intentionally delay messages
to prevent an app from consuming excessive resources and negatively
affecting battery life.

<br />

<br />

When this happens, FCM stores the message and delivers it as soon
as it's feasible. While this is fine in most cases, there are some apps for
which a late message might as well never be delivered. For example, if the
message is an incoming call or video chat notification, it is meaningful only
for a short period of time before the call is terminated. Or if the message is
an invitation to an event, it is useless if received after the event has ended.

<br />

<br />

On Android and Web/JavaScript, you can specify the maximum lifespan of a
message. The value must be a duration from 0 to 2,419,200 seconds (28
days), and it corresponds to the maximum period of time for which FCM
stores and attempts to deliver the message. Requests that don't contain this
field default to the maximum period of four weeks.

<br />

<br />

Here are some possible uses for this feature:

- Video chat incoming calls
- Expiring invitation events
- Calendar events

<br />

<br />

Another advantage of specifying the lifespan of a message is that
FCM doesn't apply collapsible message throttling to messages with a
time-to-live value of 0 seconds.
FCM provides best effort handling of messages that must be
delivered "now or never." Keep in mind that a
`time_to_live` value of
0 means messages that can't be delivered immediately are discarded. However,
because such messages are never stored, this provides the best latency for
sending notification messages.

<br />

<br />

Here is an example of a request that includes TTL:  

```scdoc
{
  "message":{
    "token":"bk3RNwTe3H0:CI2k_HHwgIpoDKCIZvvDMExUdFQ3P1...",
    "data":{
      "Nick" : "Mario",
      "body" : "great match!",
      "Room" : "PortugalVSDenmark"
    },
    "apns":{
      "headers":{
        "apns-expiration":"1604750400"
      }
    },
    "android":{
      "ttl":"4500s"
    },
    "webpush":{
      "headers":{
        "TTL":"4500"
      }
    }
  }
}
```

<br />

## Lifetime of a message

When an app server posts a message to FCM and receives a message
ID back, it does not mean that the message was already delivered to the
device. Rather, it means that it was accepted for delivery. What happens to
the message after it is accepted depends on many factors.

In the best-case scenario, if the device is connected to FCM,
the screen is on and there are no throttling restrictions, the message is
delivered right away.

If the device is connected but in Doze, a low priority message is stored
by FCM until the device is out of Doze. And
that's where the `collapse_key` flag plays a role: if there is
already a message with the same collapse key (and registration token) stored
and waiting for
delivery, the old message is discarded and the new message takes its place
(that is, the old message is collapsed by the new one). However, if the collapse
key is not set, both the new and old messages are stored for future delivery.

If the device is not connected to FCM, the message is stored until
a connection is established (again respecting the collapse key rules). When a
connection is established, FCM delivers all pending messages to the
device. If the device never gets connected again
(for instance, if it was factory reset), the message eventually times out and
is discarded from FCM storage. The default timeout is four weeks,
unless the `time_to_live` flag is set.

To get more insight into the delivery of a message:

- To get more insight into the delivery of messages on Android or Apple platforms, see the [FCM reporting dashboard](https://console.firebase.google.com/project/_/notification/reporting), which records the number of messages sent and opened on Apple and Android devices, along with data for "impressions" (notifications seen by users) for Android apps.

<br />

For Android devices with direct channel messaging enabled, if the
device has not connected to FCM for more than one month,
FCM still accepts the message but immediately discards it. If the
device connects within four weeks of the last data message you sent to it,
your client receives the [onDeletedMessages()](https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/FirebaseMessagingService#onDeletedMessages()) callback.
The app can then handle the situation properly, typically by requesting a full
sync from the app server.

Finally, when FCM attempts to deliver a message to the device and
the app was uninstalled, FCM discards that message right away and
invalidates the registration token. Future attempts to send a message to that
device results in a `NotRegistered` error.