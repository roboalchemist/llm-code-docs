# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/FirebaseMessaging.md.txt

# Source: https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/FirebaseMessaging.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/FirebaseMessaging.md.txt

# FirebaseMessaging

# FirebaseMessaging


```
class FirebaseMessaging
```

<br />

*** ** * ** ***

Top level [Firebase Cloud Messaging](https://firebase.google.com/docs/cloud-messaging/) singleton that provides methods for generating tokens and subscribing to topics.

In order to receive messages, declare an implementation of [FirebaseMessagingService](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/FirebaseMessagingService) in the app manifest. To process messages, override base class methods to handle any events required by the application.

## Summary

|                                        ### Constants                                        |
|---------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `const `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!` | [INSTANCE_ID_SCOPE](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/FirebaseMessaging#INSTANCE_ID_SCOPE())` = "FCM"` **This property is deprecated.** Use [getToken](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/FirebaseMessaging#getToken()) instead <br /> |

|                                                                                 ### Public functions                                                                                  |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)`<`[Void](https://developer.android.com/reference/kotlin/java/lang/Void.html)`!>`       | [deleteToken](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/FirebaseMessaging#deleteToken())`()` Deletes the FCM registration token for this Firebase project.                                                                                                                                                                                                                            |
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)                                                                                                    | [deliveryMetricsExportToBigQueryEnabled](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/FirebaseMessaging#deliveryMetricsExportToBigQueryEnabled())`()` Determines whether Firebase Cloud Messaging exports message delivery metrics to BigQuery.                                                                                                                                          |
| `synchronized java-static `[FirebaseMessaging](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/FirebaseMessaging)                                     | [getInstance](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/FirebaseMessaging#getInstance())`()`                                                                                                                                                                                                                                                                                          |
| [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)`<`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!>` | [getToken](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/FirebaseMessaging#getToken())`()` Returns the FCM registration token for this Firebase project.                                                                                                                                                                                                                                  |
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)                                                                                                    | [isAutoInitEnabled](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/FirebaseMessaging#isAutoInitEnabled())`()` Determines whether FCM auto-initialization is enabled or disabled.                                                                                                                                                                                                           |
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)                                                                                                    | [isNotificationDelegationEnabled](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/FirebaseMessaging#isNotificationDelegationEnabled())`()` Returns whether notification delegation is enabled or not.                                                                                                                                                                                       |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)                                                                                                          | ~~[send](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/FirebaseMessaging#send(com.google.firebase.messaging.RemoteMessage))~~`(message: `[RemoteMessage](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/RemoteMessage)`)` **This function is deprecated.** This function is actually **decommissioned** along with all of FCM upstream messaging. <br /> |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)                                                                                                          | [setAutoInitEnabled](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/FirebaseMessaging#setAutoInitEnabled(boolean))`(enable: `[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)`)` Enables or disables auto-initialization of Firebase Cloud Messaging.                                                                                                    |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)                                                                                                          | [setDeliveryMetricsExportToBigQuery](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/FirebaseMessaging#setDeliveryMetricsExportToBigQuery(boolean))`(enable: `[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)`)` Enables or disables Firebase Cloud Messaging message delivery metrics export to BigQuery.                                               |
| [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)`<`[Void](https://developer.android.com/reference/kotlin/java/lang/Void.html)`!>`       | [setNotificationDelegationEnabled](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/FirebaseMessaging#setNotificationDelegationEnabled(boolean))`(enable: `[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)`)` Sets notification delegation to enabled or disabled.                                                                                        |
| [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)`<`[Void](https://developer.android.com/reference/kotlin/java/lang/Void.html)`!>`       | [subscribeToTopic](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/FirebaseMessaging#subscribeToTopic(java.lang.String))`(topic: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`)` Subscribes to `topic` in the background.                                                                                                                              |
| [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)`<`[Void](https://developer.android.com/reference/kotlin/java/lang/Void.html)`!>`       | [unsubscribeFromTopic](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/FirebaseMessaging#unsubscribeFromTopic(java.lang.String))`(topic: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`)` Unsubscribes from `topic` in the background.                                                                                                                  |

## Constants

### INSTANCE_ID_SCOPE

```
constÂ valÂ INSTANCE_ID_SCOPE = "FCM":Â String!
```
| **This property is deprecated.**   
|
| Use [getToken](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/FirebaseMessaging#getToken()) instead

Specifies scope used in obtaining a registration token when calling `
FirebaseInstanceId.getToken()`  

## Public functions

### deleteToken

```
funÂ deleteToken():Â Task<Void!>
```

Deletes the FCM registration token for this Firebase project.

Note that if auto-init is enabled, a new token will be generated the next time the app is started. Disable auto-init ([setAutoInitEnabled](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/FirebaseMessaging#setAutoInitEnabled(boolean))) to avoid this.

Note that this does not delete the Firebase Installations ID that may have been created when generating the token. See `FirebaseInstallations.delete()` for deleting that.  

### deliveryMetricsExportToBigQueryEnabled

```
funÂ deliveryMetricsExportToBigQueryEnabled():Â Boolean
```

Determines whether Firebase Cloud Messaging exports message delivery metrics to BigQuery.  

|                                      Returns                                       |
|------------------------------------------------------------------------------------|--------------------------------------------------------------------------------|
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | true if Firebase Cloud Messaging exports message delivery metrics to BigQuery. |

### getInstance

```
synchronizedÂ java-staticÂ funÂ getInstance():Â FirebaseMessaging
```  

### getToken

```
funÂ getToken():Â Task<String!>
```

Returns the FCM registration token for this Firebase project.

This creates a Firebase Installations ID, if one does not exist, and sends information about the application and the device where it's running to the Firebase backend. See [deleteToken](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/FirebaseMessaging#deleteToken()) for information on deleting the token and the Firebase Installations ID.  

|                                                                                        Returns                                                                                        |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|
| [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)`<`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!>` | [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html) with the token. |

### isAutoInitEnabled

```
funÂ isAutoInitEnabled():Â Boolean
```

Determines whether FCM auto-initialization is enabled or disabled.  

|                                      Returns                                       |
|------------------------------------------------------------------------------------|-----------------------------------------------------------------|
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | true if auto-init is enabled and false if auto-init is disabled |

### isNotificationDelegationEnabled

```
funÂ isNotificationDelegationEnabled():Â Boolean
```

Returns whether notification delegation is enabled or not.  

|                                      Returns                                       |
|------------------------------------------------------------------------------------|-----------------------------------|
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | true if enabled, false otherwise. |

### send

```
funÂ [send](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/FirebaseMessaging#send(com.google.firebase.messaging.RemoteMessage))(message:Â RemoteMessage):Â Unit
```
| **This function is deprecated.**   
|
| This function is actually **decommissioned** along with all of FCM upstream messaging. Learn more in the [FAQ about FCM features deprecated in June 2023](https://firebase.google.com/support/faq#fcm-23-deprecation).

Sends `message` upstream to your app server.

When there is an active connection the message will be sent immediately, otherwise the message will be queued up to the time to live (TTL) set in the message.  

### setAutoInitEnabled

```
funÂ setAutoInitEnabled(enable:Â Boolean):Â Unit
```

Enables or disables auto-initialization of Firebase Cloud Messaging.

When enabled, Firebase Cloud Messaging generates a registration token on app startup if there is no valid one (see [getToken](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/FirebaseMessaging#getToken())) and periodically sends data to the Firebase backend to validate the token. This setting is persisted across app restarts and overrides the setting specified in your manifest.

By default, Firebase Cloud Messaging auto-initialization is enabled. If you need to change the default, (for example, because you want to prompt the user before Firebase Cloud Messaging generates/refreshes a registration token on app startup), add to your application's manifest:  

```kotlin
<meta-data android:name="firebase_messaging_auto_init_enabled" android:value="false" />
```  

|                                          Parameters                                          |
|----------------------------------------------------------------------------------------------|----------------------------------------------------------|
| `enable: `[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | Whether Firebase Cloud Messaging should auto-initialize. |

### setDeliveryMetricsExportToBigQuery

```
funÂ setDeliveryMetricsExportToBigQuery(enable:Â Boolean):Â Unit
```

Enables or disables Firebase Cloud Messaging message delivery metrics export to BigQuery.

By default, message delivery metrics are not exported to BigQuery. Use this method to enable or disable the export at runtime. In addition, you can enable the export by adding to your manifest. Note that the run-time method call will override the manifest value.  

```kotlin
<meta-data android:name= "delivery_metrics_exported_to_big_query_enabled"
android:value="true"/>
```  

|                                          Parameters                                          |
|----------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
| `enable: `[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | Whether Firebase Cloud Messaging should export message delivery metrics to BigQuery. |

### setNotificationDelegationEnabled

```
funÂ setNotificationDelegationEnabled(enable:Â Boolean):Â Task<Void!>
```

Sets notification delegation to enabled or disabled.

By default, notification delegation is enabled. You can also the following manifest entry to disable notification delegation:  

```kotlin
<meta-data android:name="firebase_messaging_notification_delegation_enabled"
android:value="false"/>
```

Setting notification delegation using this method will override any value set in the manifest.

Notification delegation is supported from Android Q and above. See [setNotificationDelegate](https://developer.android.com/reference/kotlin/android/app/NotificationManager.html#setNotificationDelegate-java.lang.String-)  

|                                          Parameters                                          |
|----------------------------------------------------------------------------------------------|-------------------------------------------------------|
| `enable: `[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | Whether to enable or disable notification delegation. |

|                                                                                     Returns                                                                                     |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------|
| [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)`<`[Void](https://developer.android.com/reference/kotlin/java/lang/Void.html)`!>` | A Task that completes when the notification delegation has been set. |

### subscribeToTopic

```
funÂ subscribeToTopic(topic:Â String):Â Task<Void!>
```

Subscribes to `topic` in the background.

The subscribe operation is persisted and will be retried until successful.

This uses an FCM registration token to identify the app instance, generating one if it does not exist (see [getToken](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/FirebaseMessaging#getToken())), which periodically sends data to the Firebase backend when auto-init is enabled. To delete the data, delete the token ([deleteToken](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/FirebaseMessaging#deleteToken())) and the Firebase Installations ID (`FirebaseInstallations.delete()`). To stop the periodic sending of data, disable auto-init ([setAutoInitEnabled](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/FirebaseMessaging#setAutoInitEnabled(boolean))).  

|                                        Parameters                                         |
|-------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|
| `topic: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html) | The name of the topic to subscribe. Must match the following regular expression: "\[a-zA-Z0-9-_.\~%\]{1,900}". |

|                                                                                     Returns                                                                                     |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|
| [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)`<`[Void](https://developer.android.com/reference/kotlin/java/lang/Void.html)`!>` | A task that will be completed when the topic has been successfully subscribed to. |

### unsubscribeFromTopic

```
funÂ unsubscribeFromTopic(topic:Â String):Â Task<Void!>
```

Unsubscribes from `topic` in the background.

The unsubscribe operation is persisted and will be retried until successful.  

|                                        Parameters                                         |
|-------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| `topic: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html) | The name of the topic to unsubscribe from. Must match the following regular expression: "\[a-zA-Z0-9-_.\~%\]{1,900}". |

|                                                                                     Returns                                                                                     |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------|
| [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)`<`[Void](https://developer.android.com/reference/kotlin/java/lang/Void.html)`!>` | A task that will be completed when the topic has been successfully unsubscribed from. |