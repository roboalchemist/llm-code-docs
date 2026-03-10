# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/display/FirebaseInAppMessagingDisplay.md.txt

# FirebaseInAppMessagingDisplay

# FirebaseInAppMessagingDisplay


```
class FirebaseInAppMessagingDisplay : FirebaseInAppMessagingDisplay, Application.ActivityLifecycleCallbacks
```

<br />

*** ** * ** ***

The entry point of the Firebase In App Messaging display SDK.

Firebase In-App Messaging Display will automatically initialize, start listening for events, and display eligible in-app messages.

This feature uses a Firebase Installation ID token to:

- identify the app instance
- fetch messages from the Firebase backend
- send usage metrics to the Firebase backend.

## Summary

| ### Public functions |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/display/FirebaseInAppMessagingDisplay#displayMessage(com.google.firebase.inappmessaging.model.InAppMessage,com.google.firebase.inappmessaging.FirebaseInAppMessagingDisplayCallbacks)( inAppMessage: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/model/InAppMessage!, callbacks: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/FirebaseInAppMessagingDisplayCallbacks! )` |
| `java-static https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/display/FirebaseInAppMessagingDisplay` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/display/FirebaseInAppMessagingDisplay#getInstance()()` Get FirebaseInAppMessagingDisplay instance using the default firebase app, returned by `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp#getInstance()` |

| ### Inherited functions |
|---|
| From [android.app.Application.ActivityLifecycleCallbacks](https://developer.android.com/reference/kotlin/android/app/Application.ActivityLifecycleCallbacks.html) |---|---| | `abstract https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://developer.android.com/reference/kotlin/android/app/Application.ActivityLifecycleCallbacks.html#onActivityCreated-android.app.Activity-android.os.Bundle-(p: https://developer.android.com/reference/kotlin/android/app/Activity.html!, p1: https://developer.android.com/reference/kotlin/android/os/Bundle.html!)` | | `abstract https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://developer.android.com/reference/kotlin/android/app/Application.ActivityLifecycleCallbacks.html#onActivityDestroyed-android.app.Activity-(p: https://developer.android.com/reference/kotlin/android/app/Activity.html!)` | | `abstract https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://developer.android.com/reference/kotlin/android/app/Application.ActivityLifecycleCallbacks.html#onActivityPaused-android.app.Activity-(p: https://developer.android.com/reference/kotlin/android/app/Activity.html!)` | | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://developer.android.com/reference/kotlin/android/app/Application.ActivityLifecycleCallbacks.html#onActivityPostCreated-android.app.Activity-android.os.Bundle-(activity: https://developer.android.com/reference/kotlin/android/app/Activity.html!, savedInstanceState: https://developer.android.com/reference/kotlin/android/os/Bundle.html!)` | | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://developer.android.com/reference/kotlin/android/app/Application.ActivityLifecycleCallbacks.html#onActivityPostDestroyed-android.app.Activity-(activity: https://developer.android.com/reference/kotlin/android/app/Activity.html!)` | | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://developer.android.com/reference/kotlin/android/app/Application.ActivityLifecycleCallbacks.html#onActivityPostPaused-android.app.Activity-(activity: https://developer.android.com/reference/kotlin/android/app/Activity.html!)` | | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://developer.android.com/reference/kotlin/android/app/Application.ActivityLifecycleCallbacks.html#onActivityPostResumed-android.app.Activity-(activity: https://developer.android.com/reference/kotlin/android/app/Activity.html!)` | | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://developer.android.com/reference/kotlin/android/app/Application.ActivityLifecycleCallbacks.html#onActivityPostSaveInstanceState-android.app.Activity-android.os.Bundle-(activity: https://developer.android.com/reference/kotlin/android/app/Activity.html!, outState: https://developer.android.com/reference/kotlin/android/os/Bundle.html!)` | | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://developer.android.com/reference/kotlin/android/app/Application.ActivityLifecycleCallbacks.html#onActivityPostStarted-android.app.Activity-(activity: https://developer.android.com/reference/kotlin/android/app/Activity.html!)` | | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://developer.android.com/reference/kotlin/android/app/Application.ActivityLifecycleCallbacks.html#onActivityPostStopped-android.app.Activity-(activity: https://developer.android.com/reference/kotlin/android/app/Activity.html!)` | | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://developer.android.com/reference/kotlin/android/app/Application.ActivityLifecycleCallbacks.html#onActivityPreCreated-android.app.Activity-android.os.Bundle-(activity: https://developer.android.com/reference/kotlin/android/app/Activity.html!, savedInstanceState: https://developer.android.com/reference/kotlin/android/os/Bundle.html!)` | | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://developer.android.com/reference/kotlin/android/app/Application.ActivityLifecycleCallbacks.html#onActivityPreDestroyed-android.app.Activity-(activity: https://developer.android.com/reference/kotlin/android/app/Activity.html!)` | | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://developer.android.com/reference/kotlin/android/app/Application.ActivityLifecycleCallbacks.html#onActivityPrePaused-android.app.Activity-(activity: https://developer.android.com/reference/kotlin/android/app/Activity.html!)` | | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://developer.android.com/reference/kotlin/android/app/Application.ActivityLifecycleCallbacks.html#onActivityPreResumed-android.app.Activity-(activity: https://developer.android.com/reference/kotlin/android/app/Activity.html!)` | | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://developer.android.com/reference/kotlin/android/app/Application.ActivityLifecycleCallbacks.html#onActivityPreSaveInstanceState-android.app.Activity-android.os.Bundle-(activity: https://developer.android.com/reference/kotlin/android/app/Activity.html!, outState: https://developer.android.com/reference/kotlin/android/os/Bundle.html!)` | | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://developer.android.com/reference/kotlin/android/app/Application.ActivityLifecycleCallbacks.html#onActivityPreStarted-android.app.Activity-(activity: https://developer.android.com/reference/kotlin/android/app/Activity.html!)` | | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://developer.android.com/reference/kotlin/android/app/Application.ActivityLifecycleCallbacks.html#onActivityPreStopped-android.app.Activity-(activity: https://developer.android.com/reference/kotlin/android/app/Activity.html!)` | | `abstract https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://developer.android.com/reference/kotlin/android/app/Application.ActivityLifecycleCallbacks.html#onActivityResumed-android.app.Activity-(p: https://developer.android.com/reference/kotlin/android/app/Activity.html!)` | | `abstract https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://developer.android.com/reference/kotlin/android/app/Application.ActivityLifecycleCallbacks.html#onActivitySaveInstanceState-android.app.Activity-android.os.Bundle-(p: https://developer.android.com/reference/kotlin/android/app/Activity.html!, p1: https://developer.android.com/reference/kotlin/android/os/Bundle.html!)` | | `abstract https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://developer.android.com/reference/kotlin/android/app/Application.ActivityLifecycleCallbacks.html#onActivityStarted-android.app.Activity-(p: https://developer.android.com/reference/kotlin/android/app/Activity.html!)` | | `abstract https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://developer.android.com/reference/kotlin/android/app/Application.ActivityLifecycleCallbacks.html#onActivityStopped-android.app.Activity-(p: https://developer.android.com/reference/kotlin/android/app/Activity.html!)` | |
| From [com.google.firebase.inappmessaging.FirebaseInAppMessagingDisplay](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/FirebaseInAppMessagingDisplay) |---|---| | `abstract https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/FirebaseInAppMessagingDisplay#displayMessage(com.google.firebase.inappmessaging.model.InAppMessage,com.google.firebase.inappmessaging.FirebaseInAppMessagingDisplayCallbacks)( p: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/model/InAppMessage!, p1: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/FirebaseInAppMessagingDisplayCallbacks! )` | |

## Public functions

### displayMessage

```
fun displayMessage(
    inAppMessage: InAppMessage!,
    callbacks: FirebaseInAppMessagingDisplayCallbacks!
): Unit
```

### getInstance

```
java-static fun getInstance(): FirebaseInAppMessagingDisplay
```

Get FirebaseInAppMessagingDisplay instance using the default firebase app, returned by `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp#getInstance()`