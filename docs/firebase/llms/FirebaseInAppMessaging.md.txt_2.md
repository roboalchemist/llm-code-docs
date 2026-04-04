# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/FirebaseInAppMessaging.md.txt

# FirebaseInAppMessaging

# FirebaseInAppMessaging


```
class FirebaseInAppMessaging
```

<br />

*** ** * ** ***

The entry point of the Firebase In App Messaging headless SDK.

Firebase In-App Messaging will automatically initialize, and start listening for events.

This feature uses a Firebase Installation ID token to:

- identify the app instance
- fetch messages from the Firebase backend
- send usage metrics to the Firebase backend.

To delete the Installation ID and the data associated with it, see `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/installations/FirebaseInstallationsApi#delete()`.

## Summary

| ### Public functions |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/FirebaseInAppMessaging#addClickListener(com.google.firebase.inappmessaging.FirebaseInAppMessagingClickListener)(clickListener: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/FirebaseInAppMessagingClickListener)` Registers a click listener with FIAM, which will be notified on every FIAM click. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/FirebaseInAppMessaging#addClickListener(com.google.firebase.inappmessaging.FirebaseInAppMessagingClickListener,java.util.concurrent.Executor)( clickListener: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/FirebaseInAppMessagingClickListener, executor: https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html )` Registers a click listener with FIAM, which will be notified on every FIAM click, and triggered on the provided executor. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/FirebaseInAppMessaging#addDismissListener(com.google.firebase.inappmessaging.FirebaseInAppMessagingDismissListener)( dismissListener: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/FirebaseInAppMessagingDismissListener )` Registers a dismiss listener with FIAM, which will be notified on every FIAM dismiss. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/FirebaseInAppMessaging#addDismissListener(com.google.firebase.inappmessaging.FirebaseInAppMessagingDismissListener,java.util.concurrent.Executor)( dismissListener: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/FirebaseInAppMessagingDismissListener, executor: https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html )` Registers a dismiss listener with FIAM, which will be notified on every FIAM dismiss, and triggered on the provided executor. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/FirebaseInAppMessaging#addDisplayErrorListener(com.google.firebase.inappmessaging.FirebaseInAppMessagingDisplayErrorListener)( displayErrorListener: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/FirebaseInAppMessagingDisplayErrorListener )` Registers a display error listener with FIAM, which will be notified on every FIAM display error. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/FirebaseInAppMessaging#addDisplayErrorListener(com.google.firebase.inappmessaging.FirebaseInAppMessagingDisplayErrorListener,java.util.concurrent.Executor)( displayErrorListener: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/FirebaseInAppMessagingDisplayErrorListener, executor: https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html )` Registers a display error listener with FIAM, which will be notified on every FIAM display error, and triggered on the provided executor. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/FirebaseInAppMessaging#addImpressionListener(com.google.firebase.inappmessaging.FirebaseInAppMessagingImpressionListener)( impressionListener: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/FirebaseInAppMessagingImpressionListener )` Registers an impression listener with FIAM, which will be notified on every FIAM impression. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/FirebaseInAppMessaging#addImpressionListener(com.google.firebase.inappmessaging.FirebaseInAppMessagingImpressionListener,java.util.concurrent.Executor)( impressionListener: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/FirebaseInAppMessagingImpressionListener, executor: https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html )` Registers an impression listener with FIAM, which will be notified on every FIAM impression, and triggered on the provided executor. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/FirebaseInAppMessaging#areMessagesSuppressed()()` Determines whether messages are suppressed or not. |
| `java-static https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/FirebaseInAppMessaging` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/FirebaseInAppMessaging#getInstance()()` Gets FirebaseInAppMessaging instance using the firebase app returned by `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp#getInstance()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/FirebaseInAppMessaging#isAutomaticDataCollectionEnabled()()` Determines whether automatic data collection is enabled or not. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/FirebaseInAppMessaging#removeClickListener(com.google.firebase.inappmessaging.FirebaseInAppMessagingClickListener)(clickListener: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/FirebaseInAppMessagingClickListener)` Unregisters a click listener. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/FirebaseInAppMessaging#removeDismissListener(com.google.firebase.inappmessaging.FirebaseInAppMessagingDismissListener)( dismissListener: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/FirebaseInAppMessagingDismissListener )` Unregisters a dismiss listener. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/FirebaseInAppMessaging#removeDisplayErrorListener(com.google.firebase.inappmessaging.FirebaseInAppMessagingDisplayErrorListener)( displayErrorListener: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/FirebaseInAppMessagingDisplayErrorListener )` Unregisters a display error listener. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/FirebaseInAppMessaging#removeImpressionListener(com.google.firebase.inappmessaging.FirebaseInAppMessagingImpressionListener)( impressionListener: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/FirebaseInAppMessagingImpressionListener )` Unregisters an impression listener. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/FirebaseInAppMessaging#setAutomaticDataCollectionEnabled(java.lang.Boolean)( isAutomaticCollectionEnabled: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html? )` Enables, disables, or clears automatic data collection for Firebase In-App Messaging. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/FirebaseInAppMessaging#setAutomaticDataCollectionEnabled(boolean)( isAutomaticCollectionEnabled: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html )` Enables, disables, or clears automatic data collection for Firebase In-App Messaging. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/FirebaseInAppMessaging#setMessageDisplayComponent(com.google.firebase.inappmessaging.FirebaseInAppMessagingDisplay)( messageDisplay: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/FirebaseInAppMessagingDisplay )` Sets message display component for FIAM SDK. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/FirebaseInAppMessaging#setMessagesSuppressed(java.lang.Boolean)(areMessagesSuppressed: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` Enables or disables suppression of Firebase In App Messaging messages. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/FirebaseInAppMessaging#triggerEvent(java.lang.String)(eventName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Programmatically triggers a contextual trigger. |

## Public functions

### addClickListener

```
fun addClickListener(clickListener: FirebaseInAppMessagingClickListener): Unit
```

Registers a click listener with FIAM, which will be notified on every FIAM click.

| Parameters |
|---|---|
| `clickListener: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/FirebaseInAppMessagingClickListener` |   |

### addClickListener

```
fun addClickListener(
    clickListener: FirebaseInAppMessagingClickListener,
    executor: Executor
): Unit
```

Registers a click listener with FIAM, which will be notified on every FIAM click, and triggered on the provided executor.

| Parameters |
|---|---|
| `clickListener: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/FirebaseInAppMessagingClickListener` |   |
| `executor: https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html` |   |

### addDismissListener

```
fun addDismissListener(
    dismissListener: FirebaseInAppMessagingDismissListener
): Unit
```

Registers a dismiss listener with FIAM, which will be notified on every FIAM dismiss.

| Parameters |
|---|---|
| `dismissListener: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/FirebaseInAppMessagingDismissListener` |   |

### addDismissListener

```
fun addDismissListener(
    dismissListener: FirebaseInAppMessagingDismissListener,
    executor: Executor
): Unit
```

Registers a dismiss listener with FIAM, which will be notified on every FIAM dismiss, and triggered on the provided executor.

| Parameters |
|---|---|
| `dismissListener: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/FirebaseInAppMessagingDismissListener` |   |
| `executor: https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html` |   |

### addDisplayErrorListener

```
fun addDisplayErrorListener(
    displayErrorListener: FirebaseInAppMessagingDisplayErrorListener
): Unit
```

Registers a display error listener with FIAM, which will be notified on every FIAM display error.

| Parameters |
|---|---|
| `displayErrorListener: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/FirebaseInAppMessagingDisplayErrorListener` |   |

### addDisplayErrorListener

```
fun addDisplayErrorListener(
    displayErrorListener: FirebaseInAppMessagingDisplayErrorListener,
    executor: Executor
): Unit
```

Registers a display error listener with FIAM, which will be notified on every FIAM display error, and triggered on the provided executor.

| Parameters |
|---|---|
| `displayErrorListener: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/FirebaseInAppMessagingDisplayErrorListener` |   |
| `executor: https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html` |   |

### addImpressionListener

```
fun addImpressionListener(
    impressionListener: FirebaseInAppMessagingImpressionListener
): Unit
```

Registers an impression listener with FIAM, which will be notified on every FIAM impression.

| Parameters |
|---|---|
| `impressionListener: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/FirebaseInAppMessagingImpressionListener` |   |

### addImpressionListener

```
fun addImpressionListener(
    impressionListener: FirebaseInAppMessagingImpressionListener,
    executor: Executor
): Unit
```

Registers an impression listener with FIAM, which will be notified on every FIAM impression, and triggered on the provided executor.

| Parameters |
|---|---|
| `impressionListener: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/FirebaseInAppMessagingImpressionListener` |   |
| `executor: https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html` |   |

### areMessagesSuppressed

```
fun areMessagesSuppressed(): Boolean
```

Determines whether messages are suppressed or not. This is honored by the UI sdk, which handles rendering the in app message.

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | true if messages should be suppressed |

### getInstance

```
java-static fun getInstance(): FirebaseInAppMessaging
```

Gets FirebaseInAppMessaging instance using the firebase app returned by `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp#getInstance()`

### isAutomaticDataCollectionEnabled

```
fun isAutomaticDataCollectionEnabled(): Boolean
```

Determines whether automatic data collection is enabled or not.

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | true if auto initialization is required |

### removeClickListener

```
fun removeClickListener(clickListener: FirebaseInAppMessagingClickListener): Unit
```

Unregisters a click listener.

| Parameters |
|---|---|
| `clickListener: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/FirebaseInAppMessagingClickListener` |   |

### removeDismissListener

```
fun removeDismissListener(
    dismissListener: FirebaseInAppMessagingDismissListener
): Unit
```

Unregisters a dismiss listener.

| Parameters |
|---|---|
| `dismissListener: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/FirebaseInAppMessagingDismissListener` | the listener callback to be removed which was added using addDismissListener |

### removeDisplayErrorListener

```
fun removeDisplayErrorListener(
    displayErrorListener: FirebaseInAppMessagingDisplayErrorListener
): Unit
```

Unregisters a display error listener.

| Parameters |
|---|---|
| `displayErrorListener: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/FirebaseInAppMessagingDisplayErrorListener` |   |

### removeImpressionListener

```
fun removeImpressionListener(
    impressionListener: FirebaseInAppMessagingImpressionListener
): Unit
```

Unregisters an impression listener.

| Parameters |
|---|---|
| `impressionListener: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/FirebaseInAppMessagingImpressionListener` |   |

### setAutomaticDataCollectionEnabled

```
fun setAutomaticDataCollectionEnabled(
    isAutomaticCollectionEnabled: Boolean?
): Unit
```

Enables, disables, or clears automatic data collection for Firebase In-App Messaging.

When enabled, generates a registration token on app startup if there is no valid one and generates a new token when it is deleted (which prevents `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/installations/FirebaseInstallationsApi#delete()` from stopping the periodic sending of data). This setting is persisted across app restarts and overrides the setting specified in your manifest.

When null, the enablement of the auto-initialization depends on the manifest and then on the global enablement setting in this order. If none of these settings are present then it is enabled by default.

If you need to change the default, (for example, because you want to prompt the user before generates/refreshes a registration token on app startup), add the following to your application's manifest:

```kotlin
<meta-data android:name="firebase_inapp_messaging_auto_init_enabled" android:value="false" />
```

Note, this will require you to manually initialize Firebase In-App Messaging, via:

```kotlin
FirebaseInAppMessaging.getInstance().setAutomaticDataCollectionEnabled(true)
```

Manual initialization will also be required in order to clear these settings and fall back on other settings, via:

```kotlin
FirebaseInAppMessaging.getInstance().setAutomaticDataCollectionEnabled(null)
```

| Parameters |
|---|---|
| `isAutomaticCollectionEnabled: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html?` | Whether isEnabled |

### setAutomaticDataCollectionEnabled

```
fun setAutomaticDataCollectionEnabled(
    isAutomaticCollectionEnabled: Boolean
): Unit
```

Enables, disables, or clears automatic data collection for Firebase In-App Messaging.

When enabled, generates a registration token on app startup if there is no valid one and generates a new token when it is deleted (which prevents `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/installations/FirebaseInstallationsApi#delete()` from stopping the periodic sending of data). This setting is persisted across app restarts and overrides the setting specified in your manifest.

By default, auto-initialization is enabled. If you need to change the default, (for example, because you want to prompt the user before generates/refreshes a registration token on app startup), add to your application's manifest:

```kotlin
<meta-data android:name="firebase_inapp_messaging_auto_init_enabled" android:value="false" />
```

Note, this will require you to manually initialize Firebase In-App Messaging, via:

```kotlin
FirebaseInAppMessaging.getInstance().setAutomaticDataCollectionEnabled(true)
```

| Parameters |
|---|---|
| `isAutomaticCollectionEnabled: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | Whether isEnabled |

### setMessageDisplayComponent

```
fun setMessageDisplayComponent(
    messageDisplay: FirebaseInAppMessagingDisplay
): Unit
```

Sets message display component for FIAM SDK. This is the method used by both the default FIAM display SDK or any app wanting to customize the message display.

### setMessagesSuppressed

```
fun setMessagesSuppressed(areMessagesSuppressed: Boolean): Unit
```

Enables or disables suppression of Firebase In App Messaging messages.

When enabled, no in app messages will be rendered until either you either disable suppression, or the app restarts, as this state is not preserved over app restarts.

By default, messages are not suppressed.

| Parameters |
|---|---|
| `areMessagesSuppressed: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | Whether messages should be suppressed |

### triggerEvent

```
fun triggerEvent(eventName: String): Unit
```

Programmatically triggers a contextual trigger. This will display any eligible in-app messages that are triggered by this event.

| Parameters |
|---|---|
| `eventName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` |   |