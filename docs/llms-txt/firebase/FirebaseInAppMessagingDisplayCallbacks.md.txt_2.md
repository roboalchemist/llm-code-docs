# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/FirebaseInAppMessagingDisplayCallbacks.md.txt

# FirebaseInAppMessagingDisplayCallbacks

# FirebaseInAppMessagingDisplayCallbacks


```
interface FirebaseInAppMessagingDisplayCallbacks
```

<br />

*** ** * ** ***

## Summary

| ### Nested types |
|---|
| `enum https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/FirebaseInAppMessagingDisplayCallbacks.InAppMessagingDismissType` |
| `enum https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/FirebaseInAppMessagingDisplayCallbacks.InAppMessagingErrorReason` |

| ### Public functions |
|---|---|
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/kotlin/java/lang/Void.html!>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/FirebaseInAppMessagingDisplayCallbacks#displayErrorEncountered(com.google.firebase.inappmessaging.FirebaseInAppMessagingDisplayCallbacks.InAppMessagingErrorReason)( inAppMessagingErrorReason: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/FirebaseInAppMessagingDisplayCallbacks.InAppMessagingErrorReason )` |
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/kotlin/java/lang/Void.html!>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/FirebaseInAppMessagingDisplayCallbacks#impressionDetected()()` |
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/kotlin/java/lang/Void.html!>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/FirebaseInAppMessagingDisplayCallbacks#messageClicked(com.google.firebase.inappmessaging.model.Action)(action: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/model/Action)` |
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/kotlin/java/lang/Void.html!>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/FirebaseInAppMessagingDisplayCallbacks#messageDismissed(com.google.firebase.inappmessaging.FirebaseInAppMessagingDisplayCallbacks.InAppMessagingDismissType)( dismissType: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/FirebaseInAppMessagingDisplayCallbacks.InAppMessagingDismissType )` |

## Public functions

### displayErrorEncountered

```
fun displayErrorEncountered(
    inAppMessagingErrorReason: FirebaseInAppMessagingDisplayCallbacks.InAppMessagingErrorReason
): Task<Void!>
```

### impressionDetected

```
fun impressionDetected(): Task<Void!>
```

### messageClicked

```
fun messageClicked(action: Action): Task<Void!>
```

### messageDismissed

```
fun messageDismissed(
    dismissType: FirebaseInAppMessagingDisplayCallbacks.InAppMessagingDismissType
): Task<Void!>
```