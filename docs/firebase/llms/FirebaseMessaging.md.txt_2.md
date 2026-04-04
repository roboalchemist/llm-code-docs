# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/FirebaseMessaging.md.txt

# FirebaseMessaging

# FirebaseMessaging


```
public class FirebaseMessaging
```

<br />

*** ** * ** ***

Top level [Firebase Cloud Messaging](https://firebase.google.com/docs/cloud-messaging/) singleton that provides methods for generating tokens and subscribing to topics.

In order to receive messages, declare an implementation of `https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/FirebaseMessagingService` in the app manifest. To process messages, override base class methods to handle any events required by the application.

## Summary

| ### Constants |
|---|---|
| `static final https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/FirebaseMessaging#INSTANCE_ID_SCOPE() = "FCM"` **This field is deprecated.** Use `https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/FirebaseMessaging#getToken()` instead <br /> |

| ### Public methods |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/kotlin/java/lang/Void.html>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/FirebaseMessaging#deleteToken()()` Deletes the FCM registration token for this Firebase project. |
| `boolean` | `https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/FirebaseMessaging#deliveryMetricsExportToBigQueryEnabled()()` Determines whether Firebase Cloud Messaging exports message delivery metrics to BigQuery. |
| `synchronized static @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/FirebaseMessaging` | `https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/FirebaseMessaging#getInstance()()` |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/kotlin/java/lang/String.html>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/FirebaseMessaging#getToken()()` Returns the FCM registration token for this Firebase project. |
| `boolean` | `https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/FirebaseMessaging#isAutoInitEnabled()()` Determines whether FCM auto-initialization is enabled or disabled. |
| `boolean` | `https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/FirebaseMessaging#isNotificationDelegationEnabled()()` Returns whether notification delegation is enabled or not. |
| `void` | `[send](https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/FirebaseMessaging#send(com.google.firebase.messaging.RemoteMessage))(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/RemoteMessage message)` **This method is deprecated.** This function is actually **decommissioned** along with all of FCM upstream messaging. <br /> |
| `void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/FirebaseMessaging#setAutoInitEnabled(boolean)(boolean enable)` Enables or disables auto-initialization of Firebase Cloud Messaging. |
| `void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/FirebaseMessaging#setDeliveryMetricsExportToBigQuery(boolean)(boolean enable)` Enables or disables Firebase Cloud Messaging message delivery metrics export to BigQuery. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/kotlin/java/lang/Void.html>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/FirebaseMessaging#setNotificationDelegationEnabled(boolean)(boolean enable)` Sets notification delegation to enabled or disabled. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/kotlin/java/lang/Void.html>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/FirebaseMessaging#subscribeToTopic(java.lang.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html topic)` Subscribes to `topic` in the background. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/kotlin/java/lang/Void.html>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/FirebaseMessaging#unsubscribeFromTopic(java.lang.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html topic)` Unsubscribes from `topic` in the background. |

## Constants

### INSTANCE_ID_SCOPE

```
public static final String INSTANCE_ID_SCOPE = "FCM"
```

> [!CAUTION]
> **This field is deprecated.**   
>
> Use `https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/FirebaseMessaging#getToken()` instead

Specifies scope used in obtaining a registration token when calling `
FirebaseInstanceId.getToken()`

## Public methods

### deleteToken

```
public @NonNull Task<Void> deleteToken()
```

Deletes the FCM registration token for this Firebase project.

Note that if auto-init is enabled, a new token will be generated the next time the app is started. Disable auto-init (`https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/FirebaseMessaging#setAutoInitEnabled(boolean)`) to avoid this.

Note that this does not delete the Firebase Installations ID that may have been created when generating the token. See `FirebaseInstallations.delete()` for deleting that.

### deliveryMetricsExportToBigQueryEnabled

```
public boolean deliveryMetricsExportToBigQueryEnabled()
```

Determines whether Firebase Cloud Messaging exports message delivery metrics to BigQuery.

| Returns |
|---|---|
| `boolean` | true if Firebase Cloud Messaging exports message delivery metrics to BigQuery. |

### getInstance

```
synchronized public static @NonNull FirebaseMessaging getInstance()
```

### getToken

```
public @NonNull Task<String> getToken()
```

Returns the FCM registration token for this Firebase project.

This creates a Firebase Installations ID, if one does not exist, and sends information about the application and the device where it's running to the Firebase backend. See `https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/FirebaseMessaging#deleteToken()` for information on deleting the token and the Firebase Installations ID.

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/kotlin/java/lang/String.html>` | `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html` with the token. |

### isAutoInitEnabled

```
public boolean isAutoInitEnabled()
```

Determines whether FCM auto-initialization is enabled or disabled.

| Returns |
|---|---|
| `boolean` | true if auto-init is enabled and false if auto-init is disabled |

### isNotificationDelegationEnabled

```
public boolean isNotificationDelegationEnabled()
```

Returns whether notification delegation is enabled or not.

| Returns |
|---|---|
| `boolean` | true if enabled, false otherwise. |

### send

```
public void [send](https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/FirebaseMessaging#send(com.google.firebase.messaging.RemoteMessage))(@NonNull RemoteMessage message)
```

> [!CAUTION]
> **This method is deprecated.**   
>
> This function is actually **decommissioned** along with all of FCM upstream messaging. Learn more in the [FAQ about FCM features deprecated in June 2023](https://firebase.google.com/support/faq#fcm-23-deprecation).

Sends `message` upstream to your app server.

When there is an active connection the message will be sent immediately, otherwise the message will be queued up to the time to live (TTL) set in the message.

### setAutoInitEnabled

```
public void setAutoInitEnabled(boolean enable)
```

Enables or disables auto-initialization of Firebase Cloud Messaging.

When enabled, Firebase Cloud Messaging generates a registration token on app startup if there is no valid one (see `https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/FirebaseMessaging#getToken()`) and periodically sends data to the Firebase backend to validate the token. This setting is persisted across app restarts and overrides the setting specified in your manifest.

By default, Firebase Cloud Messaging auto-initialization is enabled. If you need to change the default, (for example, because you want to prompt the user before Firebase Cloud Messaging generates/refreshes a registration token on app startup), add to your application's manifest:

```
<meta-data android:name="firebase_messaging_auto_init_enabled" android:value="false" />
```

| Parameters |
|---|---|
| `boolean enable` | Whether Firebase Cloud Messaging should auto-initialize. |

### setDeliveryMetricsExportToBigQuery

```
public void setDeliveryMetricsExportToBigQuery(boolean enable)
```

Enables or disables Firebase Cloud Messaging message delivery metrics export to BigQuery.

By default, message delivery metrics are not exported to BigQuery. Use this method to enable or disable the export at runtime. In addition, you can enable the export by adding to your manifest. Note that the run-time method call will override the manifest value.

```
<meta-data android:name= "delivery_metrics_exported_to_big_query_enabled"
android:value="true"/>
```

| Parameters |
|---|---|
| `boolean enable` | Whether Firebase Cloud Messaging should export message delivery metrics to BigQuery. |

### setNotificationDelegationEnabled

```
public @NonNull Task<Void> setNotificationDelegationEnabled(boolean enable)
```

Sets notification delegation to enabled or disabled.

By default, notification delegation is enabled. You can also the following manifest entry to disable notification delegation:

```
<meta-data android:name="firebase_messaging_notification_delegation_enabled"
android:value="false"/>
```

Setting notification delegation using this method will override any value set in the manifest.

Notification delegation is supported from Android Q and above. See `https://developer.android.com/reference/kotlin/android/app/NotificationManager.html#setNotificationDelegate-java.lang.String-`

| Parameters |
|---|---|
| `boolean enable` | Whether to enable or disable notification delegation. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/kotlin/java/lang/Void.html>` | A Task that completes when the notification delegation has been set. |

### subscribeToTopic

```
public @NonNull Task<Void> subscribeToTopic(@NonNull String topic)
```

Subscribes to `topic` in the background.

The subscribe operation is persisted and will be retried until successful.

This uses an FCM registration token to identify the app instance, generating one if it does not exist (see `https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/FirebaseMessaging#getToken()`), which periodically sends data to the Firebase backend when auto-init is enabled. To delete the data, delete the token (`https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/FirebaseMessaging#deleteToken()`) and the Firebase Installations ID (`FirebaseInstallations.delete()`). To stop the periodic sending of data, disable auto-init (`https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/FirebaseMessaging#setAutoInitEnabled(boolean)`).

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html topic` | The name of the topic to subscribe. Must match the following regular expression: "\[a-zA-Z0-9-_.\~%\]{1,900}". |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/kotlin/java/lang/Void.html>` | A task that will be completed when the topic has been successfully subscribed to. |

### unsubscribeFromTopic

```
public @NonNull Task<Void> unsubscribeFromTopic(@NonNull String topic)
```

Unsubscribes from `topic` in the background.

The unsubscribe operation is persisted and will be retried until successful.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html topic` | The name of the topic to unsubscribe from. Must match the following regular expression: "\[a-zA-Z0-9-_.\~%\]{1,900}". |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/kotlin/java/lang/Void.html>` | A task that will be completed when the topic has been successfully unsubscribed from. |