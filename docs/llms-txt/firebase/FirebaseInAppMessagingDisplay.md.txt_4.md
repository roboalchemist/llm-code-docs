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

| ### Public functions |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `@https://developer.android.com/reference/kotlin/androidx/annotation/Keep.html https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/FirebaseInAppMessagingDisplay#displayMessage(com.google.firebase.inappmessaging.model.InAppMessage,com.google.firebase.inappmessaging.FirebaseInAppMessagingDisplayCallbacks)( inAppMessage: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/model/InAppMessage, callbacks: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/FirebaseInAppMessagingDisplayCallbacks )` |

## Public functions

### displayMessage

```
@Keep
fun displayMessage(
    inAppMessage: InAppMessage,
    callbacks: FirebaseInAppMessagingDisplayCallbacks
): Unit
```