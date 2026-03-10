# Source: https://firebase.google.com/docs/reference/cpp/namespace/firebase/messaging.md.txt

# firebase::messaging Namespace

# firebase::messaging

Firebase Cloud Messaging API.

## Summary

Firebase Cloud Messaging allows you to send data from your server to your users' devices, and receive messages from devices on the same connection if you're using a XMPP server.

The FCM service handles all aspects of queueing of messages and delivery to client applications running on target devices.

| ### Enumerations ||
|---|---|
| `https://firebase.google.com/docs/reference/cpp/namespace/firebase/messaging#namespacefirebase_1_1messaging_1a6678514e05b8faf6c0a5fc6b7a0dd52e{ https://firebase.google.com/docs/reference/cpp/namespace/firebase/messaging#namespacefirebase_1_1messaging_1a6678514e05b8faf6c0a5fc6b7a0dd52ea828ab8592fa5452102ef8866b5ac3ef0 = 0, https://firebase.google.com/docs/reference/cpp/namespace/firebase/messaging#namespacefirebase_1_1messaging_1a6678514e05b8faf6c0a5fc6b7a0dd52eae4b0e2f43c2a5743f8a3d3def9e6d6da, https://firebase.google.com/docs/reference/cpp/namespace/firebase/messaging#namespacefirebase_1_1messaging_1a6678514e05b8faf6c0a5fc6b7a0dd52ea14e31ee08c3c8f7e36643650af4c6c73, https://firebase.google.com/docs/reference/cpp/namespace/firebase/messaging#namespacefirebase_1_1messaging_1a6678514e05b8faf6c0a5fc6b7a0dd52ea5a44aae4e1e159f62bda25142f2b5732, https://firebase.google.com/docs/reference/cpp/namespace/firebase/messaging#namespacefirebase_1_1messaging_1a6678514e05b8faf6c0a5fc6b7a0dd52ea4894bb32277e0fe33507955b22779d07 }` | enumError code returned by Firebase Cloud Messaging C++ functions. |

| ### Functions ||
|---|---|
| `https://firebase.google.com/docs/reference/cpp/namespace/firebase/messaging#namespacefirebase_1_1messaging_1a29c47ffad63d6d20ab4019b4ee1dd0af()` | `https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future< void >` Deletes the default token for this Firebase project. |
| `https://firebase.google.com/docs/reference/cpp/namespace/firebase/messaging#namespacefirebase_1_1messaging_1a105b4b7c6d789b7877bd0859b3b7e531()` | `https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future< void >` Gets the result of the most recent call to [DeleteToken()](https://firebase.google.com/docs/reference/cpp/namespace/firebase/messaging#namespacefirebase_1_1messaging_1a29c47ffad63d6d20ab4019b4ee1dd0af);. |
| `https://firebase.google.com/docs/reference/cpp/namespace/firebase/messaging#namespacefirebase_1_1messaging_1a13025fea4aecb5ba5f6a8ae7e1be2cae()` | `bool` Determines whether Firebase Cloud Messaging exports message delivery metrics to BigQuery. |
| `https://firebase.google.com/docs/reference/cpp/namespace/firebase/messaging#namespacefirebase_1_1messaging_1a73538af5a6035eb7140e62e3bff6bc62()` | `https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future< std::string >` This creates a Firebase Installations ID, if one does not exist, and sends information about the application and the device where it's running to the Firebase backend. |
| `https://firebase.google.com/docs/reference/cpp/namespace/firebase/messaging#namespacefirebase_1_1messaging_1a72a15489ec416d967b77b270d24f8229()` | `https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future< std::string >` Gets the result of the most recent call to [GetToken()](https://firebase.google.com/docs/reference/cpp/namespace/firebase/messaging#namespacefirebase_1_1messaging_1a73538af5a6035eb7140e62e3bff6bc62);. |
| `https://firebase.google.com/docs/reference/cpp/namespace/firebase/messaging#namespacefirebase_1_1messaging_1a5e3bd7545d50f7877ce9f72909718750(const https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app & app, https://firebase.google.com/docs/reference/cpp/class/firebase/messaging/listener#classfirebase_1_1messaging_1_1_listener *listener)` | `https://firebase.google.com/docs/reference/cpp/namespace/firebase#namespacefirebase_1a8f058cad989f8f1a6c5b42a77a8c3478` Initialize Firebase Cloud Messaging. |
| `https://firebase.google.com/docs/reference/cpp/namespace/firebase/messaging#namespacefirebase_1_1messaging_1ae664cb21b945aafbb02833f08b03d5f6(const https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app & app, https://firebase.google.com/docs/reference/cpp/class/firebase/messaging/listener#classfirebase_1_1messaging_1_1_listener *listener, const https://firebase.google.com/docs/reference/cpp/struct/firebase/messaging/messaging-options#structfirebase_1_1messaging_1_1_messaging_options & options)` | `https://firebase.google.com/docs/reference/cpp/namespace/firebase#namespacefirebase_1a8f058cad989f8f1a6c5b42a77a8c3478` Initialize Firebase Cloud Messaging. |
| `https://firebase.google.com/docs/reference/cpp/namespace/firebase/messaging#namespacefirebase_1_1messaging_1a59e78159e30437b9ee0616a9627d27b5()` | `bool` Determines if automatic token registration during initalization is enabled. |
| `https://firebase.google.com/docs/reference/cpp/namespace/firebase/messaging#namespacefirebase_1_1messaging_1abb0bdae9b9173ae0eb7901401f5f8a51()` | `https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future< void >` Displays a prompt to the user requesting permission to display notifications. |
| `https://firebase.google.com/docs/reference/cpp/namespace/firebase/messaging#namespacefirebase_1_1messaging_1aaf3bbc2282a20b2ff5d35a4bf45c1c90()` | `https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future< void >` Gets the result of the most recent call to [RequestPermission()](https://firebase.google.com/docs/reference/cpp/namespace/firebase/messaging#namespacefirebase_1_1messaging_1abb0bdae9b9173ae0eb7901401f5f8a51);. |
| `https://firebase.google.com/docs/reference/cpp/namespace/firebase/messaging#namespacefirebase_1_1messaging_1a9e2061da1c885ecdaac79fb24db33094(bool enable)` | `void` Enables or disables Firebase Cloud Messaging message delivery metrics export to BigQuery. |
| `https://firebase.google.com/docs/reference/cpp/namespace/firebase/messaging#namespacefirebase_1_1messaging_1ae6532e44f18dbda751e969241da61d1b(https://firebase.google.com/docs/reference/cpp/class/firebase/messaging/listener#classfirebase_1_1messaging_1_1_listener *listener)` | `https://firebase.google.com/docs/reference/cpp/class/firebase/messaging/listener#classfirebase_1_1messaging_1_1_listener *` Set the listener for events from the Firebase Cloud Messaging servers. |
| `https://firebase.google.com/docs/reference/cpp/namespace/firebase/messaging#namespacefirebase_1_1messaging_1a65a14f20d60814d8a280517ffccff6ab(bool enable)` | `void` Enable or disable token registration during initialization of Firebase Cloud Messaging. |
| `https://firebase.google.com/docs/reference/cpp/namespace/firebase/messaging#namespacefirebase_1_1messaging_1a15095b80bd0a42e1f0d4cf4fdf75d906(const char *topic)` | `https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future< void >` Subscribe to receive all messages to the specified topic. |
| `https://firebase.google.com/docs/reference/cpp/namespace/firebase/messaging#namespacefirebase_1_1messaging_1a440445869a16a75aff25ba54e169f212()` | `https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future< void >` Gets the result of the most recent call to [Unsubscribe()](https://firebase.google.com/docs/reference/cpp/namespace/firebase/messaging#namespacefirebase_1_1messaging_1aed11305eace7bb459e446853c1641615);. |
| `https://firebase.google.com/docs/reference/cpp/namespace/firebase/messaging#namespacefirebase_1_1messaging_1adff0925cf22b170e5f1b7c487abff3d6()` | `void` Terminate Firebase Cloud Messaging. |
| `https://firebase.google.com/docs/reference/cpp/namespace/firebase/messaging#namespacefirebase_1_1messaging_1aed11305eace7bb459e446853c1641615(const char *topic)` | `https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future< void >` Unsubscribe from a topic. |
| `https://firebase.google.com/docs/reference/cpp/namespace/firebase/messaging#namespacefirebase_1_1messaging_1abe560e66d8e3fc0a21adcd852b31d8dc()` | `https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future< void >` Gets the result of the most recent call to [Unsubscribe()](https://firebase.google.com/docs/reference/cpp/namespace/firebase/messaging#namespacefirebase_1_1messaging_1aed11305eace7bb459e446853c1641615);. |

| ### Classes ||
|---|---|
| [firebase::messaging::Listener](https://firebase.google.com/docs/reference/cpp/class/firebase/messaging/listener) | Base class used to receive messages from Firebase Cloud Messaging. |
| [firebase::messaging::PollableListener](https://firebase.google.com/docs/reference/cpp/class/firebase/messaging/pollable-listener) | A listener that can be polled to consume pending `https://firebase.google.com/docs/reference/cpp/struct/firebase/messaging/message#structfirebase_1_1messaging_1_1_message`s. |

| ### Structs ||
|---|---|
| [firebase::messaging::AndroidNotificationParams](https://firebase.google.com/docs/reference/cpp/struct/firebase/messaging/android-notification-params) | Data structure for parameters that are unique to the Android implementation. |
| [firebase::messaging::Message](https://firebase.google.com/docs/reference/cpp/struct/firebase/messaging/message) | Data structure used to receive messages from cloud messaging. |
| [firebase::messaging::MessagingOptions](https://firebase.google.com/docs/reference/cpp/struct/firebase/messaging/messaging-options) | A class to configure the behavior of Firebase Cloud Messaging. |
| [firebase::messaging::Notification](https://firebase.google.com/docs/reference/cpp/struct/firebase/messaging/notification) | Used for messages that display a notification. |

## Enumerations

### Error

```c++
 Error
```
Error code returned by Firebase Cloud Messaging C++ functions.

| Properties ||
|---|---|
| `kErrorFailedToRegisterForRemoteNotifications` | Permission to receive notifications was not granted. |
| `kErrorInvalidTopicName` | Topic name is invalid for subscription/unsubscription. |
| `kErrorNoRegistrationToken` | Could not subscribe/unsubscribe because there is no registration token. |
| `kErrorNone` | The operation was a success, no error occurred. |
| `kErrorUnknown` | Unknown error. |

## Functions

### DeleteToken

```c++
Future< void > DeleteToken()
```
Deletes the default token for this Firebase project.

Note that this does not delete the Firebase Installations ID that may have been created when generating the token. See Installations.Delete() for deleting that.

<br />

| Details ||
|---|---|
| **Returns** | A future that completes when the token is deleted. |

### DeleteTokenLastResult

```c++
Future< void > DeleteTokenLastResult()
```
Gets the result of the most recent call to [DeleteToken()](https://firebase.google.com/docs/reference/cpp/namespace/firebase/messaging#namespacefirebase_1_1messaging_1a29c47ffad63d6d20ab4019b4ee1dd0af);.

<br />

| Details ||
|---|---|
| **Returns** | Result of the most recent call to [DeleteToken()](https://firebase.google.com/docs/reference/cpp/namespace/firebase/messaging#namespacefirebase_1_1messaging_1a29c47ffad63d6d20ab4019b4ee1dd0af). |

### DeliveryMetricsExportToBigQueryEnabled

```c++
bool DeliveryMetricsExportToBigQueryEnabled()
```
Determines whether Firebase Cloud Messaging exports message delivery metrics to BigQuery.

This function is currently only implemented on Android, and returns false with no other behavior on other platforms.

<br />

| Details ||
|---|---|
| **Returns** | true if Firebase Cloud Messaging exports message delivery metrics to BigQuery. |

### GetToken

```c++
Future< std::string > GetToken()
```
This creates a Firebase Installations ID, if one does not exist, and sends information about the application and the device where it's running to the Firebase backend.

<br />

| Details ||
|---|---|
| **Returns** | A future with the token. |

### GetTokenLastResult

```c++
Future< std::string > GetTokenLastResult()
```
Gets the result of the most recent call to [GetToken()](https://firebase.google.com/docs/reference/cpp/namespace/firebase/messaging#namespacefirebase_1_1messaging_1a73538af5a6035eb7140e62e3bff6bc62);.

<br />

| Details ||
|---|---|
| **Returns** | Result of the most recent call to [GetToken()](https://firebase.google.com/docs/reference/cpp/namespace/firebase/messaging#namespacefirebase_1_1messaging_1a73538af5a6035eb7140e62e3bff6bc62). |

### Initialize

```c++
InitResult Initialize(
  const App & app,
  Listener *listener
)
```
Initialize Firebase Cloud Messaging.

After Initialize is called, the implementation may call functions on the [Listener](https://firebase.google.com/docs/reference/cpp/class/firebase/messaging/listener#classfirebase_1_1messaging_1_1_listener) provided at any time.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `app` | The Firebase [App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app) object for this application. | | `listener` | A [Listener](https://firebase.google.com/docs/reference/cpp/class/firebase/messaging/listener#classfirebase_1_1messaging_1_1_listener) object that listens for events from the Firebase Cloud Messaging servers. | |
| **Returns** | kInitResultSuccess if initialization succeeded, or kInitResultFailedMissingDependency on Android if Google Play services is not available on the current device. |

### Initialize

```c++
InitResult Initialize(
  const App & app,
  Listener *listener,
  const MessagingOptions & options
)
```
Initialize Firebase Cloud Messaging.

After Initialize is called, the implementation may call functions on the [Listener](https://firebase.google.com/docs/reference/cpp/class/firebase/messaging/listener#classfirebase_1_1messaging_1_1_listener) provided at any time.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `app` | The Firebase [App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app) object for this application. | | `listener` | A [Listener](https://firebase.google.com/docs/reference/cpp/class/firebase/messaging/listener#classfirebase_1_1messaging_1_1_listener) object that listens for events from the Firebase Cloud Messaging servers. | | `options` | A set of options that configure the initialzation behavior of Firebase Cloud Messaging. | |
| **Returns** | kInitResultSuccess if initialization succeeded, or kInitResultFailedMissingDependency on Android if Google Play services is not available on the current device. |

### IsTokenRegistrationOnInitEnabled

```c++
bool IsTokenRegistrationOnInitEnabled()
```
Determines if automatic token registration during initalization is enabled.

<br />

| Details ||
|---|---|
| **Returns** | true if auto token registration is enabled and false if disabled. |

### RequestPermission

```c++
Future< void > RequestPermission()
```
Displays a prompt to the user requesting permission to display notifications.

The permission prompt only appears on iOS and tvOS. If the user has already agreed to allow notifications, no prompt is displayed and the returned future is completed immediately.

<br />

| Details ||
|---|---|
| **Returns** | A future that completes when the notification prompt has been dismissed. |

### RequestPermissionLastResult

```c++
Future< void > RequestPermissionLastResult()
```
Gets the result of the most recent call to [RequestPermission()](https://firebase.google.com/docs/reference/cpp/namespace/firebase/messaging#namespacefirebase_1_1messaging_1abb0bdae9b9173ae0eb7901401f5f8a51);.

<br />

| Details ||
|---|---|
| **Returns** | Result of the most recent call to [RequestPermission()](https://firebase.google.com/docs/reference/cpp/namespace/firebase/messaging#namespacefirebase_1_1messaging_1abb0bdae9b9173ae0eb7901401f5f8a51). |

### SetDeliveryMetricsExportToBigQuery

```c++
void SetDeliveryMetricsExportToBigQuery(
  bool enable
)
```
Enables or disables Firebase Cloud Messaging message delivery metrics export to BigQuery.

By default, message delivery metrics are not exported to BigQuery. Use this method to enable or disable the export at runtime. In addition, you can enable the export by adding to your manifest. Note that the run-time method call will override the manifest value.

This function is currently only implemented on Android, and has no behavior on other platforms.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `enable` | Whether Firebase Cloud Messaging should export message delivery metrics to BigQuery. | |

### SetListener

```c++
Listener * SetListener(
  Listener *listener
)
```
Set the listener for events from the Firebase Cloud Messaging servers.

A listener must be set for the application to receive messages from the Firebase Cloud Messaging servers. The implementation may call functions on the [Listener](https://firebase.google.com/docs/reference/cpp/class/firebase/messaging/listener#classfirebase_1_1messaging_1_1_listener) provided at any time.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `listener` | A [Listener](https://firebase.google.com/docs/reference/cpp/class/firebase/messaging/listener#classfirebase_1_1messaging_1_1_listener) object that listens for events from the Firebase Cloud Messaging servers. | |
| **Returns** | Pointer to the previously set listener. |

### SetTokenRegistrationOnInitEnabled

```c++
void SetTokenRegistrationOnInitEnabled(
  bool enable
)
```
Enable or disable token registration during initialization of Firebase Cloud Messaging.

This token is what identifies the user to Firebase, so disabling this avoids creating any new identity and automatically sending it to Firebase, unless consent has been granted.

If this setting is enabled, it triggers the token registration refresh immediately. This setting is persisted across app restarts and overrides the setting "firebase_messaging_auto_init_enabled" specified in your Android manifest (on Android) or Info.plist (on iOS and tvOS).

By default, token registration during initialization is enabled.

The registration happens before you can programmatically disable it, so if you need to change the default, (for example, because you want to prompt the user before FCM generates/refreshes a registration token on app startup), add to your application's manifest:


```c++
<meta-data android:name="firebase_messaging_auto_init_enabled"
android:value="false" />
```

<br />

or on iOS or tvOS to your Info.plist:


```c++
<key>FirebaseMessagingAutoInitEnabled</key>
<false/>
```

<br />

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `enable` | sets if a registration token should be requested on initialization. | |

### Subscribe

```c++
Future< void > Subscribe(
  const char *topic
)
```
Subscribe to receive all messages to the specified topic.

Subscribes an app instance to a topic, enabling it to receive messages sent to that topic.

Call this function from the main thread. FCM is not thread safe.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `topic` | The name of the topic to subscribe. Must match the following regular expression: `[a-zA-Z0-9-_.~%]{1,900}`. | |

### SubscribeLastResult

```c++
Future< void > SubscribeLastResult()
```
Gets the result of the most recent call to [Unsubscribe()](https://firebase.google.com/docs/reference/cpp/namespace/firebase/messaging#namespacefirebase_1_1messaging_1aed11305eace7bb459e446853c1641615);.

<br />

| Details ||
|---|---|
| **Returns** | Result of the most recent call to [Unsubscribe()](https://firebase.google.com/docs/reference/cpp/namespace/firebase/messaging#namespacefirebase_1_1messaging_1aed11305eace7bb459e446853c1641615). |

### Terminate

```c++
void Terminate()
```
Terminate Firebase Cloud Messaging.

Frees resources associated with Firebase Cloud Messaging.


> [!NOTE]
> **Note:** On Android, the services will not be shut down by this method.

<br />

### Unsubscribe

```c++
Future< void > Unsubscribe(
  const char *topic
)
```
Unsubscribe from a topic.

Unsubscribes an app instance from a topic, stopping it from receiving any further messages sent to that topic.

Call this function from the main thread. FCM is not thread safe.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `topic` | The name of the topic to unsubscribe from. Must match the following regular expression: `[a-zA-Z0-9-_.~%]{1,900}`. | |

### UnsubscribeLastResult

```c++
Future< void > UnsubscribeLastResult()
```
Gets the result of the most recent call to [Unsubscribe()](https://firebase.google.com/docs/reference/cpp/namespace/firebase/messaging#namespacefirebase_1_1messaging_1aed11305eace7bb459e446853c1641615);.

<br />

| Details ||
|---|---|
| **Returns** | Result of the most recent call to [Unsubscribe()](https://firebase.google.com/docs/reference/cpp/namespace/firebase/messaging#namespacefirebase_1_1messaging_1aed11305eace7bb459e446853c1641615). |