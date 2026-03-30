# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/FirebaseInAppMessagingDisplayCallbacks.md.txt

# FirebaseInAppMessagingDisplayCallbacks

# FirebaseInAppMessagingDisplayCallbacks


```
public interface FirebaseInAppMessagingDisplayCallbacks
```

<br />

*** ** * ** ***

## Summary

| ### Nested types |
|---|
| `public enum https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/FirebaseInAppMessagingDisplayCallbacks.InAppMessagingDismissType` |
| `public enum https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/FirebaseInAppMessagingDisplayCallbacks.InAppMessagingErrorReason` |

| ### Public methods |
|---|---|
| `abstract @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/kotlin/java/lang/Void.html>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/FirebaseInAppMessagingDisplayCallbacks#displayErrorEncountered(com.google.firebase.inappmessaging.FirebaseInAppMessagingDisplayCallbacks.InAppMessagingErrorReason)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/FirebaseInAppMessagingDisplayCallbacks.InAppMessagingErrorReason inAppMessagingErrorReason )` |
| `abstract @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/kotlin/java/lang/Void.html>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/FirebaseInAppMessagingDisplayCallbacks#impressionDetected()()` |
| `abstract @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/kotlin/java/lang/Void.html>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/FirebaseInAppMessagingDisplayCallbacks#messageClicked(com.google.firebase.inappmessaging.model.Action)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/Action action)` |
| `abstract @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/kotlin/java/lang/Void.html>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/FirebaseInAppMessagingDisplayCallbacks#messageDismissed(com.google.firebase.inappmessaging.FirebaseInAppMessagingDisplayCallbacks.InAppMessagingDismissType)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/FirebaseInAppMessagingDisplayCallbacks.InAppMessagingDismissType dismissType )` |

## Public methods

### displayErrorEncountered

```
abstract @NonNull Task<Void> displayErrorEncountered(
    @NonNull FirebaseInAppMessagingDisplayCallbacks.InAppMessagingErrorReason inAppMessagingErrorReason
)
```

### impressionDetected

```
abstract @NonNull Task<Void> impressionDetected()
```

### messageClicked

```
abstract @NonNull Task<Void> messageClicked(@NonNull Action action)
```

### messageDismissed

```
abstract @NonNull Task<Void> messageDismissed(
    @NonNull FirebaseInAppMessagingDisplayCallbacks.InAppMessagingDismissType dismissType
)
```