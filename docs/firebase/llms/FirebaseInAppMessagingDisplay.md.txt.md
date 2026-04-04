# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/FirebaseInAppMessagingDisplay.md.txt

# FirebaseInAppMessagingDisplay

# FirebaseInAppMessagingDisplay


```
@Keep
public interface FirebaseInAppMessagingDisplay
```

<br />

*** ** * ** ***

The interface that a FIAM display class must implement. Note that the developer is responsible for calling the logging-related methods on FirebaseInAppMessaging to track user-related metrics.

## Summary

| ### Public methods |
|---|---|
| `abstract void` | `@https://developer.android.com/reference/kotlin/androidx/annotation/Keep.html https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/FirebaseInAppMessagingDisplay#displayMessage(com.google.firebase.inappmessaging.model.InAppMessage,com.google.firebase.inappmessaging.FirebaseInAppMessagingDisplayCallbacks)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/InAppMessage inAppMessage, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/FirebaseInAppMessagingDisplayCallbacks callbacks )` |

## Public methods

### displayMessage

```
@Keep
abstract void displayMessage(
    @NonNull InAppMessage inAppMessage,
    @NonNull FirebaseInAppMessagingDisplayCallbacks callbacks
)
```