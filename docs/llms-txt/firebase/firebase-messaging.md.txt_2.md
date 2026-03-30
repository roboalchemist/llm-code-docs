# Source: https://firebase.google.com/docs/reference/unity/class/firebase/messaging/firebase-messaging.md.txt

# Firebase.Messaging.FirebaseMessaging Class Reference

# Firebase.Messaging.FirebaseMessaging

[Firebase](https://firebase.google.com/docs/reference/unity/namespace/firebase#namespace_firebase) Cloud [Messaging](https://firebase.google.com/docs/reference/unity/namespace/firebase/messaging#namespace_firebase_1_1_messaging) API.

## Summary

[Firebase](https://firebase.google.com/docs/reference/unity/namespace/firebase#namespace_firebase) Cloud [Messaging](https://firebase.google.com/docs/reference/unity/namespace/firebase/messaging#namespace_firebase_1_1_messaging) allows you to send data from your server to your users' devices, and receive messages from devices on the same connection if you're using a XMPP server.

The FCM service handles all aspects of queueing of messages and delivery to client applications running on target devices.

| ### Properties ||
|---|---|
| `https://firebase.google.com/docs/reference/unity/class/firebase/messaging/firebase-messaging#class_firebase_1_1_messaging_1_1_firebase_messaging_1aadeb4ed18340c6cf44a7a9c5ce913f8c` | `static bool` Enables or disables [Firebase](https://firebase.google.com/docs/reference/unity/namespace/firebase#namespace_firebase) Cloud [Messaging](https://firebase.google.com/docs/reference/unity/namespace/firebase/messaging#namespace_firebase_1_1_messaging) message delivery metrics export to BigQuery. |
| `https://firebase.google.com/docs/reference/unity/class/firebase/messaging/firebase-messaging#class_firebase_1_1_messaging_1_1_firebase_messaging_1a8d605092353b87ff4100965650e53018` | `static bool` Enable or disable token registration during initialization of [Firebase](https://firebase.google.com/docs/reference/unity/namespace/firebase#namespace_firebase) Cloud [Messaging](https://firebase.google.com/docs/reference/unity/namespace/firebase/messaging#namespace_firebase_1_1_messaging). |

| ### Events ||
|---|---|
| `https://firebase.google.com/docs/reference/unity/class/firebase/messaging/firebase-messaging#class_firebase_1_1_messaging_1_1_firebase_messaging_1aa23b4ab44c1727df94708c99639afc1d` | `static System.EventHandler< https://firebase.google.com/docs/reference/unity/class/firebase/messaging/message-received-event-args#class_firebase_1_1_messaging_1_1_message_received_event_args >` Called on the client when a message arrives. |
| `https://firebase.google.com/docs/reference/unity/class/firebase/messaging/firebase-messaging#class_firebase_1_1_messaging_1_1_firebase_messaging_1a0cc2dfe98a6bc05ee5a7aad63f45a86b` | `static System.EventHandler< https://firebase.google.com/docs/reference/unity/class/firebase/messaging/token-received-event-args#class_firebase_1_1_messaging_1_1_token_received_event_args >` Called on the client when a registration token message arrives. |

| ### Public static functions ||
|---|---|
| `https://firebase.google.com/docs/reference/unity/class/firebase/messaging/firebase-messaging#class_firebase_1_1_messaging_1_1_firebase_messaging_1a2220798a7afdb78ac200223f93638e9a()` | `System.Threading.Tasks.Task` Deletes the default token for this [Firebase](https://firebase.google.com/docs/reference/unity/namespace/firebase#namespace_firebase) project. |
| `https://firebase.google.com/docs/reference/unity/class/firebase/messaging/firebase-messaging#class_firebase_1_1_messaging_1_1_firebase_messaging_1ab3a6bd25b8efe25fa8a6cf5019b9b9f7()` | `System.Threading.Tasks.Task< string >` This creates a [Firebase](https://firebase.google.com/docs/reference/unity/namespace/firebase#namespace_firebase)[Installations](https://firebase.google.com/docs/reference/unity/namespace/firebase/installations#namespace_firebase_1_1_installations) ID, if one does not exist, and sends information about the application and the device where it's running to the [Firebase](https://firebase.google.com/docs/reference/unity/namespace/firebase#namespace_firebase) backend. |
| `https://firebase.google.com/docs/reference/unity/class/firebase/messaging/firebase-messaging#class_firebase_1_1_messaging_1_1_firebase_messaging_1a68dc94778094f82d2913ed3ddcd1892f()` | `System.Threading.Tasks.Task` Displays a prompt to the user requesting permission to display notifications. |
| `https://firebase.google.com/docs/reference/unity/class/firebase/messaging/firebase-messaging#class_firebase_1_1_messaging_1_1_firebase_messaging_1ab26a58be39dfbeebe3babc24412c11a6(string topic)` | `System.Threading.Tasks.Task` Subscribe to receive all messages to the specified topic. |
| `https://firebase.google.com/docs/reference/unity/class/firebase/messaging/firebase-messaging#class_firebase_1_1_messaging_1_1_firebase_messaging_1a38f618b6a0132cdfc72ca64e28f422d6(string topic)` | `System.Threading.Tasks.Task` Unsubscribe from a topic. |

## Properties

### DeliveryMetricsExportedToBigQueryEnabled

```c#
static bool DeliveryMetricsExportedToBigQueryEnabled
```
Enables or disables [Firebase](https://firebase.google.com/docs/reference/unity/namespace/firebase#namespace_firebase) Cloud [Messaging](https://firebase.google.com/docs/reference/unity/namespace/firebase/messaging#namespace_firebase_1_1_messaging) message delivery metrics export to BigQuery.

By default, message delivery metrics are not exported to BigQuery. Use this method to enable or disable the export at runtime. In addition, you can enable the export by adding to your manifest. Note that the run-time method call will override the manifest value.


```c#

```

<br />


> [!NOTE]
> **Note:** This function is currently only implemented on Android, and has no behavior on other platforms.

<br />

### TokenRegistrationOnInitEnabled

```c#
static bool TokenRegistrationOnInitEnabled
```
Enable or disable token registration during initialization of [Firebase](https://firebase.google.com/docs/reference/unity/namespace/firebase#namespace_firebase) Cloud [Messaging](https://firebase.google.com/docs/reference/unity/namespace/firebase/messaging#namespace_firebase_1_1_messaging).

This token is what identifies the user to [Firebase](https://firebase.google.com/docs/reference/unity/namespace/firebase#namespace_firebase), so disabling this avoids creating any new identity and automatically sending it to [Firebase](https://firebase.google.com/docs/reference/unity/namespace/firebase#namespace_firebase), unless consent has been granted.

If this setting is enabled, it triggers the token registration refresh immediately. This setting is persisted across app restarts and overrides the setting "firebase_messaging_auto_init_enabled" specified in your Android manifest (on Android) or Info.plist (on iOS and tvOS).

By default, token registration during initialization is enabled.

The registration happens before you can programmatically disable it, so if you need to change the default, (for example, because you want to prompt the user before FCM generates/refreshes a registration token on app startup), add to your application's manifest:


```c#
<meta-data android:name="firebase_messaging_auto_init_enabled"
android:value="false" />
```

<br />

or on iOS or tvOS to your Info.plist:


```c#
<key>FirebaseMessagingAutoInitEnabled</key>
<false/>
```

<br />

## Events

### MessageReceived

```c#
static System.EventHandler< MessageReceivedEventArgs > MessageReceived
```
Called on the client when a message arrives.

### TokenReceived

```c#
static System.EventHandler< TokenReceivedEventArgs > TokenReceived
```
Called on the client when a registration token message arrives.

## Public static functions

### DeleteTokenAsync

```c#
System.Threading.Tasks.Task DeleteTokenAsync()
```
Deletes the default token for this [Firebase](https://firebase.google.com/docs/reference/unity/namespace/firebase#namespace_firebase) project.

Note that this does not delete the [Firebase](https://firebase.google.com/docs/reference/unity/namespace/firebase#namespace_firebase)[Installations](https://firebase.google.com/docs/reference/unity/namespace/firebase/installations#namespace_firebase_1_1_installations) ID that may have been created when generating the token. See Installations.Delete() for deleting that.

<br />

| Details ||
|---|---|
| **Returns** | A task that completes when the token is deleted. |

### GetTokenAsync

```c#
System.Threading.Tasks.Task< string > GetTokenAsync()
```
This creates a [Firebase](https://firebase.google.com/docs/reference/unity/namespace/firebase#namespace_firebase)[Installations](https://firebase.google.com/docs/reference/unity/namespace/firebase/installations#namespace_firebase_1_1_installations) ID, if one does not exist, and sends information about the application and the device where it's running to the [Firebase](https://firebase.google.com/docs/reference/unity/namespace/firebase#namespace_firebase) backend.

<br />

| Details ||
|---|---|
| **Returns** | A task with the token. |

### RequestPermissionAsync

```c#
System.Threading.Tasks.Task RequestPermissionAsync()
```
Displays a prompt to the user requesting permission to display notifications.

The permission prompt only appears on iOS and tvOS. If the user has already agreed to allow notifications, no prompt is displayed and the returned future is completed immediately.

<br />

| Details ||
|---|---|
| **Returns** | A Task that completes when the notification prompt has been dismissed. |

### SubscribeAsync

```c#
System.Threading.Tasks.Task SubscribeAsync(
  string topic
)
```
Subscribe to receive all messages to the specified topic.

Subscribes an app instance to a topic, enabling it to receive messages sent to that topic.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `topic` | The name of the topic to subscribe. Must match the following regular expression: `[a-zA-Z0-9-_.~%]{1,900}`. | |

### UnsubscribeAsync

```c#
System.Threading.Tasks.Task UnsubscribeAsync(
  string topic
)
```
Unsubscribe from a topic.

Unsubscribes an app instance from a topic, stopping it from receiving any further messages sent to that topic.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `topic` | The name of the topic to unsubscribe from. Must match the following regular expression: `[a-zA-Z0-9-_.~%]{1,900}`. | |