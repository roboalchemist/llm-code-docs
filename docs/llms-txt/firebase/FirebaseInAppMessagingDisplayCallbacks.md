# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/FirebaseInAppMessagingDisplayCallbacks.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/FirebaseInAppMessagingDisplayCallbacks.md.txt

# FirebaseInAppMessagingDisplayCallbacks

# FirebaseInAppMessagingDisplayCallbacks


```
interface FirebaseInAppMessagingDisplayCallbacks
```

<br />

*** ** * ** ***

## Summary

|                                                                                                         ### Nested types                                                                                                         |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `enum `[FirebaseInAppMessagingDisplayCallbacks.InAppMessagingDismissType](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/FirebaseInAppMessagingDisplayCallbacks.InAppMessagingDismissType) |
| `enum `[FirebaseInAppMessagingDisplayCallbacks.InAppMessagingErrorReason](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/FirebaseInAppMessagingDisplayCallbacks.InAppMessagingErrorReason) |

|                                                                              ### Public functions                                                                               |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)`<`[Void](https://developer.android.com/reference/kotlin/java/lang/Void.html)`!>` | [displayErrorEncountered](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/FirebaseInAppMessagingDisplayCallbacks#displayErrorEncountered(com.google.firebase.inappmessaging.FirebaseInAppMessagingDisplayCallbacks.InAppMessagingErrorReason))`(` ` inAppMessagingErrorReason: `[FirebaseInAppMessagingDisplayCallbacks.InAppMessagingErrorReason](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/FirebaseInAppMessagingDisplayCallbacks.InAppMessagingErrorReason) `)` |
| [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)`<`[Void](https://developer.android.com/reference/kotlin/java/lang/Void.html)`!>` | [impressionDetected](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/FirebaseInAppMessagingDisplayCallbacks#impressionDetected())`()`                                                                                                                                                                                                                                                                                                                                                                         |
| [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)`<`[Void](https://developer.android.com/reference/kotlin/java/lang/Void.html)`!>` | [messageClicked](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/FirebaseInAppMessagingDisplayCallbacks#messageClicked(com.google.firebase.inappmessaging.model.Action))`(action: `[Action](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/model/Action)`)`                                                                                                                                                                                                             |
| [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)`<`[Void](https://developer.android.com/reference/kotlin/java/lang/Void.html)`!>` | [messageDismissed](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/FirebaseInAppMessagingDisplayCallbacks#messageDismissed(com.google.firebase.inappmessaging.FirebaseInAppMessagingDisplayCallbacks.InAppMessagingDismissType))`(` ` dismissType: `[FirebaseInAppMessagingDisplayCallbacks.InAppMessagingDismissType](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/FirebaseInAppMessagingDisplayCallbacks.InAppMessagingDismissType) `)`                             |

## Public functions

### displayErrorEncountered

```
funÂ displayErrorEncountered(
Â Â Â Â inAppMessagingErrorReason:Â FirebaseInAppMessagingDisplayCallbacks.InAppMessagingErrorReason
):Â Task<Void!>
```  

### impressionDetected

```
funÂ impressionDetected():Â Task<Void!>
```  

### messageClicked

```
funÂ messageClicked(action:Â Action):Â Task<Void!>
```  

### messageDismissed

```
funÂ messageDismissed(
Â Â Â Â dismissType:Â FirebaseInAppMessagingDisplayCallbacks.InAppMessagingDismissType
):Â Task<Void!>
```