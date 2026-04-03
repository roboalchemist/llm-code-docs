# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/FirebaseInAppMessaging.md.txt

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

To delete the Installation ID and the data associated with it, see [delete](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/installations/FirebaseInstallationsApi#delete()).

## Summary

|                                                                ### Public functions                                                                 |
|-----------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)                                                                        | [addClickListener](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/FirebaseInAppMessaging#addClickListener(com.google.firebase.inappmessaging.FirebaseInAppMessagingClickListener))`(clickListener: `[FirebaseInAppMessagingClickListener](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/FirebaseInAppMessagingClickListener)`)` Registers a click listener with FIAM, which will be notified on every FIAM click.                                                                                                                                                                                                                                                    |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)                                                                        | [addClickListener](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/FirebaseInAppMessaging#addClickListener(com.google.firebase.inappmessaging.FirebaseInAppMessagingClickListener,java.util.concurrent.Executor))`(` ` clickListener: `[FirebaseInAppMessagingClickListener](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/FirebaseInAppMessagingClickListener)`,` ` executor: `[Executor](https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html) `)` Registers a click listener with FIAM, which will be notified on every FIAM click, and triggered on the provided executor.                                                           |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)                                                                        | [addDismissListener](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/FirebaseInAppMessaging#addDismissListener(com.google.firebase.inappmessaging.FirebaseInAppMessagingDismissListener))`(` ` dismissListener: `[FirebaseInAppMessagingDismissListener](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/FirebaseInAppMessagingDismissListener) `)` Registers a dismiss listener with FIAM, which will be notified on every FIAM dismiss.                                                                                                                                                                                                                               |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)                                                                        | [addDismissListener](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/FirebaseInAppMessaging#addDismissListener(com.google.firebase.inappmessaging.FirebaseInAppMessagingDismissListener,java.util.concurrent.Executor))`(` ` dismissListener: `[FirebaseInAppMessagingDismissListener](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/FirebaseInAppMessagingDismissListener)`,` ` executor: `[Executor](https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html) `)` Registers a dismiss listener with FIAM, which will be notified on every FIAM dismiss, and triggered on the provided executor.                                           |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)                                                                        | [addDisplayErrorListener](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/FirebaseInAppMessaging#addDisplayErrorListener(com.google.firebase.inappmessaging.FirebaseInAppMessagingDisplayErrorListener))`(` ` displayErrorListener: `[FirebaseInAppMessagingDisplayErrorListener](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/FirebaseInAppMessagingDisplayErrorListener) `)` Registers a display error listener with FIAM, which will be notified on every FIAM display error.                                                                                                                                                                                     |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)                                                                        | [addDisplayErrorListener](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/FirebaseInAppMessaging#addDisplayErrorListener(com.google.firebase.inappmessaging.FirebaseInAppMessagingDisplayErrorListener,java.util.concurrent.Executor))`(` ` displayErrorListener: `[FirebaseInAppMessagingDisplayErrorListener](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/FirebaseInAppMessagingDisplayErrorListener)`,` ` executor: `[Executor](https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html) `)` Registers a display error listener with FIAM, which will be notified on every FIAM display error, and triggered on the provided executor. |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)                                                                        | [addImpressionListener](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/FirebaseInAppMessaging#addImpressionListener(com.google.firebase.inappmessaging.FirebaseInAppMessagingImpressionListener))`(` ` impressionListener: `[FirebaseInAppMessagingImpressionListener](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/FirebaseInAppMessagingImpressionListener) `)` Registers an impression listener with FIAM, which will be notified on every FIAM impression.                                                                                                                                                                                                      |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)                                                                        | [addImpressionListener](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/FirebaseInAppMessaging#addImpressionListener(com.google.firebase.inappmessaging.FirebaseInAppMessagingImpressionListener,java.util.concurrent.Executor))`(` ` impressionListener: `[FirebaseInAppMessagingImpressionListener](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/FirebaseInAppMessagingImpressionListener)`,` ` executor: `[Executor](https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html) `)` Registers an impression listener with FIAM, which will be notified on every FIAM impression, and triggered on the provided executor.                  |
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)                                                                  | [areMessagesSuppressed](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/FirebaseInAppMessaging#areMessagesSuppressed())`()` Determines whether messages are suppressed or not.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `java-static `[FirebaseInAppMessaging](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/FirebaseInAppMessaging) | [getInstance](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/FirebaseInAppMessaging#getInstance())`()` Gets FirebaseInAppMessaging instance using the firebase app returned by [getInstance](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp#getInstance())                                                                                                                                                                                                                                                                                                                                                                                                               |
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)                                                                  | [isAutomaticDataCollectionEnabled](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/FirebaseInAppMessaging#isAutomaticDataCollectionEnabled())`()` Determines whether automatic data collection is enabled or not.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)                                                                        | [removeClickListener](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/FirebaseInAppMessaging#removeClickListener(com.google.firebase.inappmessaging.FirebaseInAppMessagingClickListener))`(clickListener: `[FirebaseInAppMessagingClickListener](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/FirebaseInAppMessagingClickListener)`)` Unregisters a click listener.                                                                                                                                                                                                                                                                                                  |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)                                                                        | [removeDismissListener](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/FirebaseInAppMessaging#removeDismissListener(com.google.firebase.inappmessaging.FirebaseInAppMessagingDismissListener))`(` ` dismissListener: `[FirebaseInAppMessagingDismissListener](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/FirebaseInAppMessagingDismissListener) `)` Unregisters a dismiss listener.                                                                                                                                                                                                                                                                               |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)                                                                        | [removeDisplayErrorListener](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/FirebaseInAppMessaging#removeDisplayErrorListener(com.google.firebase.inappmessaging.FirebaseInAppMessagingDisplayErrorListener))`(` ` displayErrorListener: `[FirebaseInAppMessagingDisplayErrorListener](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/FirebaseInAppMessagingDisplayErrorListener) `)` Unregisters a display error listener.                                                                                                                                                                                                                                           |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)                                                                        | [removeImpressionListener](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/FirebaseInAppMessaging#removeImpressionListener(com.google.firebase.inappmessaging.FirebaseInAppMessagingImpressionListener))`(` ` impressionListener: `[FirebaseInAppMessagingImpressionListener](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/FirebaseInAppMessagingImpressionListener) `)` Unregisters an impression listener.                                                                                                                                                                                                                                                         |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)                                                                        | [setAutomaticDataCollectionEnabled](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/FirebaseInAppMessaging#setAutomaticDataCollectionEnabled(java.lang.Boolean))`(` ` isAutomaticCollectionEnabled: `[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)`?` `)` Enables, disables, or clears automatic data collection for Firebase In-App Messaging.                                                                                                                                                                                                                                                                                                                         |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)                                                                        | [setAutomaticDataCollectionEnabled](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/FirebaseInAppMessaging#setAutomaticDataCollectionEnabled(boolean))`(` ` isAutomaticCollectionEnabled: `[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) `)` Enables, disables, or clears automatic data collection for Firebase In-App Messaging.                                                                                                                                                                                                                                                                                                                                      |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)                                                                        | [setMessageDisplayComponent](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/FirebaseInAppMessaging#setMessageDisplayComponent(com.google.firebase.inappmessaging.FirebaseInAppMessagingDisplay))`(` ` messageDisplay: `[FirebaseInAppMessagingDisplay](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/FirebaseInAppMessagingDisplay) `)` Sets message display component for FIAM SDK.                                                                                                                                                                                                                                                                                 |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)                                                                        | [setMessagesSuppressed](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/FirebaseInAppMessaging#setMessagesSuppressed(java.lang.Boolean))`(areMessagesSuppressed: `[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)`)` Enables or disables suppression of Firebase In App Messaging messages.                                                                                                                                                                                                                                                                                                                                                                               |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)                                                                        | [triggerEvent](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/FirebaseInAppMessaging#triggerEvent(java.lang.String))`(eventName: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`)` Programmatically triggers a contextual trigger.                                                                                                                                                                                                                                                                                                                                                                                                                                       |

## Public functions

### addClickListener

```
funÂ addClickListener(clickListener:Â FirebaseInAppMessagingClickListener):Â Unit
```

Registers a click listener with FIAM, which will be notified on every FIAM click.  

|                                                                                    Parameters                                                                                    |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---|
| `clickListener: `[FirebaseInAppMessagingClickListener](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/FirebaseInAppMessagingClickListener) |   |

### addClickListener

```
funÂ addClickListener(
Â Â Â Â clickListener:Â FirebaseInAppMessagingClickListener,
Â Â Â Â executor:Â Executor
):Â Unit
```

Registers a click listener with FIAM, which will be notified on every FIAM click, and triggered on the provided executor.  

|                                                                                    Parameters                                                                                    |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---|
| `clickListener: `[FirebaseInAppMessagingClickListener](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/FirebaseInAppMessagingClickListener) |   |
| `executor: `[Executor](https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html)                                                                        |   |

### addDismissListener

```
funÂ addDismissListener(
Â Â Â Â dismissListener:Â FirebaseInAppMessagingDismissListener
):Â Unit
```

Registers a dismiss listener with FIAM, which will be notified on every FIAM dismiss.  

|                                                                                       Parameters                                                                                       |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---|
| `dismissListener: `[FirebaseInAppMessagingDismissListener](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/FirebaseInAppMessagingDismissListener) |   |

### addDismissListener

```
funÂ addDismissListener(
Â Â Â Â dismissListener:Â FirebaseInAppMessagingDismissListener,
Â Â Â Â executor:Â Executor
):Â Unit
```

Registers a dismiss listener with FIAM, which will be notified on every FIAM dismiss, and triggered on the provided executor.  

|                                                                                       Parameters                                                                                       |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---|
| `dismissListener: `[FirebaseInAppMessagingDismissListener](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/FirebaseInAppMessagingDismissListener) |   |
| `executor: `[Executor](https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html)                                                                              |   |

### addDisplayErrorListener

```
funÂ addDisplayErrorListener(
Â Â Â Â displayErrorListener:Â FirebaseInAppMessagingDisplayErrorListener
):Â Unit
```

Registers a display error listener with FIAM, which will be notified on every FIAM display error.  

|                                                                                              Parameters                                                                                               |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---|
| `displayErrorListener: `[FirebaseInAppMessagingDisplayErrorListener](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/FirebaseInAppMessagingDisplayErrorListener) |   |

### addDisplayErrorListener

```
funÂ addDisplayErrorListener(
Â Â Â Â displayErrorListener:Â FirebaseInAppMessagingDisplayErrorListener,
Â Â Â Â executor:Â Executor
):Â Unit
```

Registers a display error listener with FIAM, which will be notified on every FIAM display error, and triggered on the provided executor.  

|                                                                                              Parameters                                                                                               |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---|
| `displayErrorListener: `[FirebaseInAppMessagingDisplayErrorListener](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/FirebaseInAppMessagingDisplayErrorListener) |   |
| `executor: `[Executor](https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html)                                                                                             |   |

### addImpressionListener

```
funÂ addImpressionListener(
Â Â Â Â impressionListener:Â FirebaseInAppMessagingImpressionListener
):Â Unit
```

Registers an impression listener with FIAM, which will be notified on every FIAM impression.  

|                                                                                           Parameters                                                                                            |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---|
| `impressionListener: `[FirebaseInAppMessagingImpressionListener](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/FirebaseInAppMessagingImpressionListener) |   |

### addImpressionListener

```
funÂ addImpressionListener(
Â Â Â Â impressionListener:Â FirebaseInAppMessagingImpressionListener,
Â Â Â Â executor:Â Executor
):Â Unit
```

Registers an impression listener with FIAM, which will be notified on every FIAM impression, and triggered on the provided executor.  

|                                                                                           Parameters                                                                                            |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---|
| `impressionListener: `[FirebaseInAppMessagingImpressionListener](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/FirebaseInAppMessagingImpressionListener) |   |
| `executor: `[Executor](https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html)                                                                                       |   |

### areMessagesSuppressed

```
funÂ areMessagesSuppressed():Â Boolean
```

Determines whether messages are suppressed or not. This is honored by the UI sdk, which handles rendering the in app message.  

|                                      Returns                                       |
|------------------------------------------------------------------------------------|---------------------------------------|
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | true if messages should be suppressed |

### getInstance

```
java-staticÂ funÂ getInstance():Â FirebaseInAppMessaging
```

Gets FirebaseInAppMessaging instance using the firebase app returned by [getInstance](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp#getInstance())  

### isAutomaticDataCollectionEnabled

```
funÂ isAutomaticDataCollectionEnabled():Â Boolean
```

Determines whether automatic data collection is enabled or not.  

|                                      Returns                                       |
|------------------------------------------------------------------------------------|-----------------------------------------|
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | true if auto initialization is required |

### removeClickListener

```
funÂ removeClickListener(clickListener:Â FirebaseInAppMessagingClickListener):Â Unit
```

Unregisters a click listener.  

|                                                                                    Parameters                                                                                    |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---|
| `clickListener: `[FirebaseInAppMessagingClickListener](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/FirebaseInAppMessagingClickListener) |   |

### removeDismissListener

```
funÂ removeDismissListener(
Â Â Â Â dismissListener:Â FirebaseInAppMessagingDismissListener
):Â Unit
```

Unregisters a dismiss listener.  

|                                                                                       Parameters                                                                                       |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------|
| `dismissListener: `[FirebaseInAppMessagingDismissListener](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/FirebaseInAppMessagingDismissListener) | the listener callback to be removed which was added using addDismissListener |

### removeDisplayErrorListener

```
funÂ removeDisplayErrorListener(
Â Â Â Â displayErrorListener:Â FirebaseInAppMessagingDisplayErrorListener
):Â Unit
```

Unregisters a display error listener.  

|                                                                                              Parameters                                                                                               |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---|
| `displayErrorListener: `[FirebaseInAppMessagingDisplayErrorListener](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/FirebaseInAppMessagingDisplayErrorListener) |   |

### removeImpressionListener

```
funÂ removeImpressionListener(
Â Â Â Â impressionListener:Â FirebaseInAppMessagingImpressionListener
):Â Unit
```

Unregisters an impression listener.  

|                                                                                           Parameters                                                                                            |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---|
| `impressionListener: `[FirebaseInAppMessagingImpressionListener](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/FirebaseInAppMessagingImpressionListener) |   |

### setAutomaticDataCollectionEnabled

```
funÂ setAutomaticDataCollectionEnabled(
Â Â Â Â isAutomaticCollectionEnabled:Â Boolean?
):Â Unit
```

Enables, disables, or clears automatic data collection for Firebase In-App Messaging.

When enabled, generates a registration token on app startup if there is no valid one and generates a new token when it is deleted (which prevents [delete](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/installations/FirebaseInstallationsApi#delete()) from stopping the periodic sending of data). This setting is persisted across app restarts and overrides the setting specified in your manifest.

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

|                                                      Parameters                                                       |
|-----------------------------------------------------------------------------------------------------------------------|-------------------|
| `isAutomaticCollectionEnabled: `[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)`?` | Whether isEnabled |

### setAutomaticDataCollectionEnabled

```
funÂ setAutomaticDataCollectionEnabled(
Â Â Â Â isAutomaticCollectionEnabled:Â Boolean
):Â Unit
```

Enables, disables, or clears automatic data collection for Firebase In-App Messaging.

When enabled, generates a registration token on app startup if there is no valid one and generates a new token when it is deleted (which prevents [delete](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/installations/FirebaseInstallationsApi#delete()) from stopping the periodic sending of data). This setting is persisted across app restarts and overrides the setting specified in your manifest.

By default, auto-initialization is enabled. If you need to change the default, (for example, because you want to prompt the user before generates/refreshes a registration token on app startup), add to your application's manifest:  

```kotlin
<meta-data android:name="firebase_inapp_messaging_auto_init_enabled" android:value="false" />
```

Note, this will require you to manually initialize Firebase In-App Messaging, via:  

```kotlin
FirebaseInAppMessaging.getInstance().setAutomaticDataCollectionEnabled(true)
```  

|                                                     Parameters                                                     |
|--------------------------------------------------------------------------------------------------------------------|-------------------|
| `isAutomaticCollectionEnabled: `[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | Whether isEnabled |

### setMessageDisplayComponent

```
funÂ setMessageDisplayComponent(
Â Â Â Â messageDisplay:Â FirebaseInAppMessagingDisplay
):Â Unit
```

Sets message display component for FIAM SDK. This is the method used by both the default FIAM display SDK or any app wanting to customize the message display.  

### setMessagesSuppressed

```
funÂ setMessagesSuppressed(areMessagesSuppressed:Â Boolean):Â Unit
```

Enables or disables suppression of Firebase In App Messaging messages.

When enabled, no in app messages will be rendered until either you either disable suppression, or the app restarts, as this state is not preserved over app restarts.

By default, messages are not suppressed.  

|                                                 Parameters                                                  |
|-------------------------------------------------------------------------------------------------------------|---------------------------------------|
| `areMessagesSuppressed: `[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | Whether messages should be suppressed |

### triggerEvent

```
funÂ triggerEvent(eventName:Â String):Â Unit
```

Programmatically triggers a contextual trigger. This will display any eligible in-app messages that are triggered by this event.  

|                                          Parameters                                           |
|-----------------------------------------------------------------------------------------------|---|
| `eventName: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html) |   |