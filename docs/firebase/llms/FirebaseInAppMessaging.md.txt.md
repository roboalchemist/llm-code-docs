# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/FirebaseInAppMessaging.md.txt

# FirebaseInAppMessaging

# FirebaseInAppMessaging


```
public class FirebaseInAppMessaging
```

<br />

*** ** * ** ***

The entry point of the Firebase In App Messaging headless SDK.

Firebase In-App Messaging will automatically initialize, and start listening for events.

This feature uses a Firebase Installation ID token to:

- identify the app instance
- fetch messages from the Firebase backend
- send usage metrics to the Firebase backend.

To delete the Installation ID and the data associated with it, see `https://firebase.google.com/docs/reference/android/com/google/firebase/installations/FirebaseInstallationsApi#delete()`.

## Summary

| ### Public methods |
|---|---|
| `void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/FirebaseInAppMessaging#addClickListener(com.google.firebase.inappmessaging.FirebaseInAppMessagingClickListener)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/FirebaseInAppMessagingClickListener clickListener )` Registers a click listener with FIAM, which will be notified on every FIAM click. |
| `void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/FirebaseInAppMessaging#addClickListener(com.google.firebase.inappmessaging.FirebaseInAppMessagingClickListener,java.util.concurrent.Executor)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/FirebaseInAppMessagingClickListener clickListener, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html executor )` Registers a click listener with FIAM, which will be notified on every FIAM click, and triggered on the provided executor. |
| `void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/FirebaseInAppMessaging#addDismissListener(com.google.firebase.inappmessaging.FirebaseInAppMessagingDismissListener)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/FirebaseInAppMessagingDismissListener dismissListener )` Registers a dismiss listener with FIAM, which will be notified on every FIAM dismiss. |
| `void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/FirebaseInAppMessaging#addDismissListener(com.google.firebase.inappmessaging.FirebaseInAppMessagingDismissListener,java.util.concurrent.Executor)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/FirebaseInAppMessagingDismissListener dismissListener, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html executor )` Registers a dismiss listener with FIAM, which will be notified on every FIAM dismiss, and triggered on the provided executor. |
| `void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/FirebaseInAppMessaging#addDisplayErrorListener(com.google.firebase.inappmessaging.FirebaseInAppMessagingDisplayErrorListener)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/FirebaseInAppMessagingDisplayErrorListener displayErrorListener )` Registers a display error listener with FIAM, which will be notified on every FIAM display error. |
| `void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/FirebaseInAppMessaging#addDisplayErrorListener(com.google.firebase.inappmessaging.FirebaseInAppMessagingDisplayErrorListener,java.util.concurrent.Executor)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/FirebaseInAppMessagingDisplayErrorListener displayErrorListener, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html executor )` Registers a display error listener with FIAM, which will be notified on every FIAM display error, and triggered on the provided executor. |
| `void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/FirebaseInAppMessaging#addImpressionListener(com.google.firebase.inappmessaging.FirebaseInAppMessagingImpressionListener)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/FirebaseInAppMessagingImpressionListener impressionListener )` Registers an impression listener with FIAM, which will be notified on every FIAM impression. |
| `void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/FirebaseInAppMessaging#addImpressionListener(com.google.firebase.inappmessaging.FirebaseInAppMessagingImpressionListener,java.util.concurrent.Executor)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/FirebaseInAppMessagingImpressionListener impressionListener, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html executor )` Registers an impression listener with FIAM, which will be notified on every FIAM impression, and triggered on the provided executor. |
| `boolean` | `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/FirebaseInAppMessaging#areMessagesSuppressed()()` Determines whether messages are suppressed or not. |
| `static @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/FirebaseInAppMessaging` | `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/FirebaseInAppMessaging#getInstance()()` Gets FirebaseInAppMessaging instance using the firebase app returned by `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp#getInstance()` |
| `boolean` | `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/FirebaseInAppMessaging#isAutomaticDataCollectionEnabled()()` Determines whether automatic data collection is enabled or not. |
| `void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/FirebaseInAppMessaging#removeClickListener(com.google.firebase.inappmessaging.FirebaseInAppMessagingClickListener)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/FirebaseInAppMessagingClickListener clickListener )` Unregisters a click listener. |
| `void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/FirebaseInAppMessaging#removeDismissListener(com.google.firebase.inappmessaging.FirebaseInAppMessagingDismissListener)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/FirebaseInAppMessagingDismissListener dismissListener )` Unregisters a dismiss listener. |
| `void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/FirebaseInAppMessaging#removeDisplayErrorListener(com.google.firebase.inappmessaging.FirebaseInAppMessagingDisplayErrorListener)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/FirebaseInAppMessagingDisplayErrorListener displayErrorListener )` Unregisters a display error listener. |
| `void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/FirebaseInAppMessaging#removeImpressionListener(com.google.firebase.inappmessaging.FirebaseInAppMessagingImpressionListener)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/FirebaseInAppMessagingImpressionListener impressionListener )` Unregisters an impression listener. |
| `void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/FirebaseInAppMessaging#setAutomaticDataCollectionEnabled(java.lang.Boolean)( @https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/Boolean.html isAutomaticCollectionEnabled )` Enables, disables, or clears automatic data collection for Firebase In-App Messaging. |
| `void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/FirebaseInAppMessaging#setAutomaticDataCollectionEnabled(boolean)( boolean isAutomaticCollectionEnabled )` Enables, disables, or clears automatic data collection for Firebase In-App Messaging. |
| `void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/FirebaseInAppMessaging#setMessageDisplayComponent(com.google.firebase.inappmessaging.FirebaseInAppMessagingDisplay)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/FirebaseInAppMessagingDisplay messageDisplay )` Sets message display component for FIAM SDK. |
| `void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/FirebaseInAppMessaging#setMessagesSuppressed(java.lang.Boolean)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Boolean.html areMessagesSuppressed)` Enables or disables suppression of Firebase In App Messaging messages. |
| `void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/FirebaseInAppMessaging#triggerEvent(java.lang.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html eventName)` Programmatically triggers a contextual trigger. |

## Public methods

### addClickListener

```
public void addClickListener(
    @NonNull FirebaseInAppMessagingClickListener clickListener
)
```

Registers a click listener with FIAM, which will be notified on every FIAM click.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/FirebaseInAppMessagingClickListener clickListener` |   |

### addClickListener

```
public void addClickListener(
    @NonNull FirebaseInAppMessagingClickListener clickListener,
    @NonNull Executor executor
)
```

Registers a click listener with FIAM, which will be notified on every FIAM click, and triggered on the provided executor.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/FirebaseInAppMessagingClickListener clickListener` |   |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html executor` |   |

### addDismissListener

```
public void addDismissListener(
    @NonNull FirebaseInAppMessagingDismissListener dismissListener
)
```

Registers a dismiss listener with FIAM, which will be notified on every FIAM dismiss.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/FirebaseInAppMessagingDismissListener dismissListener` |   |

### addDismissListener

```
public void addDismissListener(
    @NonNull FirebaseInAppMessagingDismissListener dismissListener,
    @NonNull Executor executor
)
```

Registers a dismiss listener with FIAM, which will be notified on every FIAM dismiss, and triggered on the provided executor.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/FirebaseInAppMessagingDismissListener dismissListener` |   |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html executor` |   |

### addDisplayErrorListener

```
public void addDisplayErrorListener(
    @NonNull FirebaseInAppMessagingDisplayErrorListener displayErrorListener
)
```

Registers a display error listener with FIAM, which will be notified on every FIAM display error.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/FirebaseInAppMessagingDisplayErrorListener displayErrorListener` |   |

### addDisplayErrorListener

```
public void addDisplayErrorListener(
    @NonNull FirebaseInAppMessagingDisplayErrorListener displayErrorListener,
    @NonNull Executor executor
)
```

Registers a display error listener with FIAM, which will be notified on every FIAM display error, and triggered on the provided executor.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/FirebaseInAppMessagingDisplayErrorListener displayErrorListener` |   |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html executor` |   |

### addImpressionListener

```
public void addImpressionListener(
    @NonNull FirebaseInAppMessagingImpressionListener impressionListener
)
```

Registers an impression listener with FIAM, which will be notified on every FIAM impression.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/FirebaseInAppMessagingImpressionListener impressionListener` |   |

### addImpressionListener

```
public void addImpressionListener(
    @NonNull FirebaseInAppMessagingImpressionListener impressionListener,
    @NonNull Executor executor
)
```

Registers an impression listener with FIAM, which will be notified on every FIAM impression, and triggered on the provided executor.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/FirebaseInAppMessagingImpressionListener impressionListener` |   |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html executor` |   |

### areMessagesSuppressed

```
public boolean areMessagesSuppressed()
```

Determines whether messages are suppressed or not. This is honored by the UI sdk, which handles rendering the in app message.

| Returns |
|---|---|
| `boolean` | true if messages should be suppressed |

### getInstance

```
public static @NonNull FirebaseInAppMessaging getInstance()
```

Gets FirebaseInAppMessaging instance using the firebase app returned by `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp#getInstance()`

### isAutomaticDataCollectionEnabled

```
public boolean isAutomaticDataCollectionEnabled()
```

Determines whether automatic data collection is enabled or not.

| Returns |
|---|---|
| `boolean` | true if auto initialization is required |

### removeClickListener

```
public void removeClickListener(
    @NonNull FirebaseInAppMessagingClickListener clickListener
)
```

Unregisters a click listener.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/FirebaseInAppMessagingClickListener clickListener` |   |

### removeDismissListener

```
public void removeDismissListener(
    @NonNull FirebaseInAppMessagingDismissListener dismissListener
)
```

Unregisters a dismiss listener.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/FirebaseInAppMessagingDismissListener dismissListener` | the listener callback to be removed which was added using addDismissListener |

### removeDisplayErrorListener

```
public void removeDisplayErrorListener(
    @NonNull FirebaseInAppMessagingDisplayErrorListener displayErrorListener
)
```

Unregisters a display error listener.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/FirebaseInAppMessagingDisplayErrorListener displayErrorListener` |   |

### removeImpressionListener

```
public void removeImpressionListener(
    @NonNull FirebaseInAppMessagingImpressionListener impressionListener
)
```

Unregisters an impression listener.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/FirebaseInAppMessagingImpressionListener impressionListener` |   |

### setAutomaticDataCollectionEnabled

```
public void setAutomaticDataCollectionEnabled(
    @Nullable Boolean isAutomaticCollectionEnabled
)
```

Enables, disables, or clears automatic data collection for Firebase In-App Messaging.

When enabled, generates a registration token on app startup if there is no valid one and generates a new token when it is deleted (which prevents `https://firebase.google.com/docs/reference/android/com/google/firebase/installations/FirebaseInstallationsApi#delete()` from stopping the periodic sending of data). This setting is persisted across app restarts and overrides the setting specified in your manifest.

When null, the enablement of the auto-initialization depends on the manifest and then on the global enablement setting in this order. If none of these settings are present then it is enabled by default.

If you need to change the default, (for example, because you want to prompt the user before generates/refreshes a registration token on app startup), add the following to your application's manifest:

```
<meta-data android:name="firebase_inapp_messaging_auto_init_enabled" android:value="false" />
```

Note, this will require you to manually initialize Firebase In-App Messaging, via:

```
FirebaseInAppMessaging.getInstance().setAutomaticDataCollectionEnabled(true)
```

Manual initialization will also be required in order to clear these settings and fall back on other settings, via:

```
FirebaseInAppMessaging.getInstance().setAutomaticDataCollectionEnabled(null)
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/Boolean.html isAutomaticCollectionEnabled` | Whether isEnabled |

### setAutomaticDataCollectionEnabled

```
public void setAutomaticDataCollectionEnabled(
    boolean isAutomaticCollectionEnabled
)
```

Enables, disables, or clears automatic data collection for Firebase In-App Messaging.

When enabled, generates a registration token on app startup if there is no valid one and generates a new token when it is deleted (which prevents `https://firebase.google.com/docs/reference/android/com/google/firebase/installations/FirebaseInstallationsApi#delete()` from stopping the periodic sending of data). This setting is persisted across app restarts and overrides the setting specified in your manifest.

By default, auto-initialization is enabled. If you need to change the default, (for example, because you want to prompt the user before generates/refreshes a registration token on app startup), add to your application's manifest:

```
<meta-data android:name="firebase_inapp_messaging_auto_init_enabled" android:value="false" />
```

Note, this will require you to manually initialize Firebase In-App Messaging, via:

```
FirebaseInAppMessaging.getInstance().setAutomaticDataCollectionEnabled(true)
```

| Parameters |
|---|---|
| `boolean isAutomaticCollectionEnabled` | Whether isEnabled |

### setMessageDisplayComponent

```
public void setMessageDisplayComponent(
    @NonNull FirebaseInAppMessagingDisplay messageDisplay
)
```

Sets message display component for FIAM SDK. This is the method used by both the default FIAM display SDK or any app wanting to customize the message display.

### setMessagesSuppressed

```
public void setMessagesSuppressed(@NonNull Boolean areMessagesSuppressed)
```

Enables or disables suppression of Firebase In App Messaging messages.

When enabled, no in app messages will be rendered until either you either disable suppression, or the app restarts, as this state is not preserved over app restarts.

By default, messages are not suppressed.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Boolean.html areMessagesSuppressed` | Whether messages should be suppressed |

### triggerEvent

```
public void triggerEvent(@NonNull String eventName)
```

Programmatically triggers a contextual trigger. This will display any eligible in-app messages that are triggered by this event.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html eventName` |   |