# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/display/FirebaseInAppMessagingDisplay.md.txt

# FirebaseInAppMessagingDisplay

# FirebaseInAppMessagingDisplay


```
public class FirebaseInAppMessagingDisplay implements FirebaseInAppMessagingDisplay, Application.ActivityLifecycleCallbacks
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

| ### Public methods |
|---|---|
| `void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/display/FirebaseInAppMessagingDisplay#displayMessage(com.google.firebase.inappmessaging.model.InAppMessage,com.google.firebase.inappmessaging.FirebaseInAppMessagingDisplayCallbacks)( https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/InAppMessage inAppMessage, https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/FirebaseInAppMessagingDisplayCallbacks callbacks )` |
| `static @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/display/FirebaseInAppMessagingDisplay` | `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/display/FirebaseInAppMessagingDisplay#getInstance()()` Get FirebaseInAppMessagingDisplay instance using the default firebase app, returned by `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp#getInstance()` |

| ### Inherited methods |
|---|
| From [android.app.Application.ActivityLifecycleCallbacks](https://developer.android.com/reference/kotlin/android/app/Application.ActivityLifecycleCallbacks.html) |---|---| | `abstract void` | `https://developer.android.com/reference/kotlin/android/app/Application.ActivityLifecycleCallbacks.html#onActivityCreated-android.app.Activity-android.os.Bundle-(https://developer.android.com/reference/kotlin/android/app/Activity.html p, https://developer.android.com/reference/kotlin/android/os/Bundle.html p1)` | | `abstract void` | `https://developer.android.com/reference/kotlin/android/app/Application.ActivityLifecycleCallbacks.html#onActivityDestroyed-android.app.Activity-(https://developer.android.com/reference/kotlin/android/app/Activity.html p)` | | `abstract void` | `https://developer.android.com/reference/kotlin/android/app/Application.ActivityLifecycleCallbacks.html#onActivityPaused-android.app.Activity-(https://developer.android.com/reference/kotlin/android/app/Activity.html p)` | | `void` | `https://developer.android.com/reference/kotlin/android/app/Application.ActivityLifecycleCallbacks.html#onActivityPostCreated-android.app.Activity-android.os.Bundle-(https://developer.android.com/reference/kotlin/android/app/Activity.html activity, https://developer.android.com/reference/kotlin/android/os/Bundle.html savedInstanceState)` | | `void` | `https://developer.android.com/reference/kotlin/android/app/Application.ActivityLifecycleCallbacks.html#onActivityPostDestroyed-android.app.Activity-(https://developer.android.com/reference/kotlin/android/app/Activity.html activity)` | | `void` | `https://developer.android.com/reference/kotlin/android/app/Application.ActivityLifecycleCallbacks.html#onActivityPostPaused-android.app.Activity-(https://developer.android.com/reference/kotlin/android/app/Activity.html activity)` | | `void` | `https://developer.android.com/reference/kotlin/android/app/Application.ActivityLifecycleCallbacks.html#onActivityPostResumed-android.app.Activity-(https://developer.android.com/reference/kotlin/android/app/Activity.html activity)` | | `void` | `https://developer.android.com/reference/kotlin/android/app/Application.ActivityLifecycleCallbacks.html#onActivityPostSaveInstanceState-android.app.Activity-android.os.Bundle-(https://developer.android.com/reference/kotlin/android/app/Activity.html activity, https://developer.android.com/reference/kotlin/android/os/Bundle.html outState)` | | `void` | `https://developer.android.com/reference/kotlin/android/app/Application.ActivityLifecycleCallbacks.html#onActivityPostStarted-android.app.Activity-(https://developer.android.com/reference/kotlin/android/app/Activity.html activity)` | | `void` | `https://developer.android.com/reference/kotlin/android/app/Application.ActivityLifecycleCallbacks.html#onActivityPostStopped-android.app.Activity-(https://developer.android.com/reference/kotlin/android/app/Activity.html activity)` | | `void` | `https://developer.android.com/reference/kotlin/android/app/Application.ActivityLifecycleCallbacks.html#onActivityPreCreated-android.app.Activity-android.os.Bundle-(https://developer.android.com/reference/kotlin/android/app/Activity.html activity, https://developer.android.com/reference/kotlin/android/os/Bundle.html savedInstanceState)` | | `void` | `https://developer.android.com/reference/kotlin/android/app/Application.ActivityLifecycleCallbacks.html#onActivityPreDestroyed-android.app.Activity-(https://developer.android.com/reference/kotlin/android/app/Activity.html activity)` | | `void` | `https://developer.android.com/reference/kotlin/android/app/Application.ActivityLifecycleCallbacks.html#onActivityPrePaused-android.app.Activity-(https://developer.android.com/reference/kotlin/android/app/Activity.html activity)` | | `void` | `https://developer.android.com/reference/kotlin/android/app/Application.ActivityLifecycleCallbacks.html#onActivityPreResumed-android.app.Activity-(https://developer.android.com/reference/kotlin/android/app/Activity.html activity)` | | `void` | `https://developer.android.com/reference/kotlin/android/app/Application.ActivityLifecycleCallbacks.html#onActivityPreSaveInstanceState-android.app.Activity-android.os.Bundle-(https://developer.android.com/reference/kotlin/android/app/Activity.html activity, https://developer.android.com/reference/kotlin/android/os/Bundle.html outState)` | | `void` | `https://developer.android.com/reference/kotlin/android/app/Application.ActivityLifecycleCallbacks.html#onActivityPreStarted-android.app.Activity-(https://developer.android.com/reference/kotlin/android/app/Activity.html activity)` | | `void` | `https://developer.android.com/reference/kotlin/android/app/Application.ActivityLifecycleCallbacks.html#onActivityPreStopped-android.app.Activity-(https://developer.android.com/reference/kotlin/android/app/Activity.html activity)` | | `abstract void` | `https://developer.android.com/reference/kotlin/android/app/Application.ActivityLifecycleCallbacks.html#onActivityResumed-android.app.Activity-(https://developer.android.com/reference/kotlin/android/app/Activity.html p)` | | `abstract void` | `https://developer.android.com/reference/kotlin/android/app/Application.ActivityLifecycleCallbacks.html#onActivitySaveInstanceState-android.app.Activity-android.os.Bundle-(https://developer.android.com/reference/kotlin/android/app/Activity.html p, https://developer.android.com/reference/kotlin/android/os/Bundle.html p1)` | | `abstract void` | `https://developer.android.com/reference/kotlin/android/app/Application.ActivityLifecycleCallbacks.html#onActivityStarted-android.app.Activity-(https://developer.android.com/reference/kotlin/android/app/Activity.html p)` | | `abstract void` | `https://developer.android.com/reference/kotlin/android/app/Application.ActivityLifecycleCallbacks.html#onActivityStopped-android.app.Activity-(https://developer.android.com/reference/kotlin/android/app/Activity.html p)` | |
| From [com.google.firebase.inappmessaging.FirebaseInAppMessagingDisplay](https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/FirebaseInAppMessagingDisplay) |---|---| | `abstract void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/FirebaseInAppMessagingDisplay#displayMessage(com.google.firebase.inappmessaging.model.InAppMessage,com.google.firebase.inappmessaging.FirebaseInAppMessagingDisplayCallbacks)( https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/InAppMessage p, https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/FirebaseInAppMessagingDisplayCallbacks p1 )` | |

## Public methods

### displayMessage

```
public void displayMessage(
    InAppMessage inAppMessage,
    FirebaseInAppMessagingDisplayCallbacks callbacks
)
```

### getInstance

```
public static @NonNull FirebaseInAppMessagingDisplay getInstance()
```

Get FirebaseInAppMessagingDisplay instance using the default firebase app, returned by `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp#getInstance()`