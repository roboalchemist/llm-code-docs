# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/display/FirebaseInAppMessagingDisplay.md.txt

# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/FirebaseInAppMessagingDisplay.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/display/FirebaseInAppMessagingDisplay.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/FirebaseInAppMessagingDisplay.md.txt

# FirebaseInAppMessagingDisplay

# FirebaseInAppMessagingDisplay


```
@Keep
interface FirebaseInAppMessagingDisplay
```

<br />

*** ** * ** ***

The interface that a FIAM display class must implement. Note that the developer is responsible for calling the logging-related methods on FirebaseInAppMessaging to track user-related metrics.

## Summary

|                             ### Public functions                             |
|------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | `@`[Keep](https://developer.android.com/reference/kotlin/androidx/annotation/Keep.html) [displayMessage](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/FirebaseInAppMessagingDisplay#displayMessage(com.google.firebase.inappmessaging.model.InAppMessage,com.google.firebase.inappmessaging.FirebaseInAppMessagingDisplayCallbacks))`(` ` inAppMessage: `[InAppMessage](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/model/InAppMessage)`,` ` callbacks: `[FirebaseInAppMessagingDisplayCallbacks](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/FirebaseInAppMessagingDisplayCallbacks) `)` |

## Public functions

### displayMessage

```
@Keep
funÂ displayMessage(
Â Â Â Â inAppMessage:Â InAppMessage,
Â Â Â Â callbacks:Â FirebaseInAppMessagingDisplayCallbacks
):Â Unit
```