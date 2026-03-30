# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/FirebaseAppDistribution.md.txt

# FirebaseAppDistribution

# FirebaseAppDistribution


```
interface FirebaseAppDistribution
```

<br />

*** ** * ** ***

The Firebase App Distribution API provides methods to update the app to the most recent pre-release build.

If you don't include the `com.google.firebase:firebase-appdistribution` artifact in your build, then all methods will be stubs and the `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html` and `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/UpdateTask` will fail with `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/FirebaseAppDistributionException.Status#NOT_IMPLEMENTED`.

By default, Firebase App Distribution is automatically initialized.

Call `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/FirebaseAppDistribution#getInstance()` to get the singleton instance of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/FirebaseAppDistribution`.

## Summary

| ### Public functions |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/FirebaseAppDistribution#cancelFeedbackNotification()()` Hides the notification shown with `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/FirebaseAppDistribution#showFeedbackNotification(int,com.google.firebase.appdistribution.InterruptionLevel)` or `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/FirebaseAppDistribution#showFeedbackNotification(java.lang.CharSequence,com.google.firebase.appdistribution.InterruptionLevel)`. |
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/AppDistributionRelease!>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/FirebaseAppDistribution#checkForNewRelease()()` Returns an `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/AppDistributionRelease` if an update is available for the current signed in tester, or `null` otherwise. |
| `java-static https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/FirebaseAppDistribution` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/FirebaseAppDistribution#getInstance()()` Gets the singleton `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/FirebaseAppDistribution` instance. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/FirebaseAppDistribution#isTesterSignedIn()()` Returns `true` if the App Distribution tester is signed in. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/FirebaseAppDistribution#showFeedbackNotification(java.lang.CharSequence,com.google.firebase.appdistribution.InterruptionLevel)( additionalFormText: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-char-sequence/index.html, interruptionLevel: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/InterruptionLevel )` Displays a notification that, when tapped, will take a screenshot of the current activity, then start a new activity to collect and submit feedback from the tester along with the screenshot. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/FirebaseAppDistribution#showFeedbackNotification(int,com.google.firebase.appdistribution.InterruptionLevel)( additionalFormText: @https://developer.android.com/reference/kotlin/androidx/annotation/StringRes.html https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html, interruptionLevel: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/InterruptionLevel )` Displays a notification that, when tapped, will take a screenshot of the current activity, then start a new activity to collect and submit feedback from the tester along with the screenshot. |
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/kotlin/java/lang/Void.html!>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/FirebaseAppDistribution#signInTester()()` Signs in the App Distribution tester. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/FirebaseAppDistribution#signOutTester()()` Signs out the App Distribution tester. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/FirebaseAppDistribution#startFeedback(java.lang.CharSequence)(additionalFormText: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-char-sequence/index.html)` Takes a screenshot, and starts an activity to collect and submit feedback from the tester. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/FirebaseAppDistribution#startFeedback(int)(additionalFormText: @https://developer.android.com/reference/kotlin/androidx/annotation/StringRes.html https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` Takes a screenshot, and starts an activity to collect and submit feedback from the tester. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/FirebaseAppDistribution#startFeedback(java.lang.CharSequence,android.net.Uri)(additionalFormText: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-char-sequence/index.html, screenshot: https://developer.android.com/reference/kotlin/android/net/Uri.html?)` Starts an activity to collect and submit feedback from the tester, along with the given screenshot. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/FirebaseAppDistribution#startFeedback(int,android.net.Uri)(additionalFormText: @https://developer.android.com/reference/kotlin/androidx/annotation/StringRes.html https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html, screenshot: https://developer.android.com/reference/kotlin/android/net/Uri.html?)` Starts an activity to collect and submit feedback from the tester, along with the given screenshot. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/UpdateTask` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/FirebaseAppDistribution#updateApp()()` Updates app to the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/AppDistributionRelease` returned by `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/FirebaseAppDistribution#checkForNewRelease()`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/UpdateTask` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/FirebaseAppDistribution#updateIfNewReleaseAvailable()()` Updates the app to the newest release, if one is available. |

## Public functions

### cancelFeedbackNotification

```
fun cancelFeedbackNotification(): Unit
```

Hides the notification shown with `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/FirebaseAppDistribution#showFeedbackNotification(int,com.google.firebase.appdistribution.InterruptionLevel)` or `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/FirebaseAppDistribution#showFeedbackNotification(java.lang.CharSequence,com.google.firebase.appdistribution.InterruptionLevel)`.

### checkForNewRelease

```
fun checkForNewRelease(): Task<AppDistributionRelease!>
```

Returns an `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/AppDistributionRelease` if an update is available for the current signed in tester, or `null` otherwise.

If you don't include the `com.google.firebase:firebase-appdistribution` artifact in your build, then this method returns a failed `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html` with `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/FirebaseAppDistributionException.Status#NOT_IMPLEMENTED`.

### getInstance

```
java-static fun getInstance(): FirebaseAppDistribution
```

Gets the singleton `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/FirebaseAppDistribution` instance.

### isTesterSignedIn

```
fun isTesterSignedIn(): Boolean
```

Returns `true` if the App Distribution tester is signed in.

If you don't include the `com.google.firebase:firebase-appdistribution` artifact in your build, then this method always returns `false`.

### showFeedbackNotification

```
fun showFeedbackNotification(
    additionalFormText: CharSequence,
    interruptionLevel: InterruptionLevel
): Unit
```

Displays a notification that, when tapped, will take a screenshot of the current activity, then start a new activity to collect and submit feedback from the tester along with the screenshot.

On Android 13 and above, this method requires the runtime permission for sending notifications: [`
POST_NOTIFICATIONS`](https://developer.android.com/develop/ui/views/notifications/notification-permission). If your app targets Android 13 (API level 33) or above, you should [request the permission](https://developer.android.com/training/permissions/requesting).

When the notification is tapped:

1. If the app is open, takes a screenshot of the current activity.
2. If the tester is not signed in, presents the tester with a Google Sign-in UI.
3. Starts a full screen activity for the tester to compose and submit the feedback.

| Parameters |
|---|---|
| `additionalFormText: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-char-sequence/index.html` | text that will be shown to the tester before they submit feedback. If you're a customer who would like to provide notice to your testers about collection and processing of their feedback data, you can use this text to provide such notice. |
| `interruptionLevel: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/InterruptionLevel` | the level of interruption for the feedback notification. On platforms below Android 8, this corresponds to a [notification channel importance](https://developer.android.com/develop/ui/views/notifications/channels#importance) and once set cannot be changed except by the tester. |

### showFeedbackNotification

```
fun showFeedbackNotification(
    additionalFormText: @StringRes Int,
    interruptionLevel: InterruptionLevel
): Unit
```

Displays a notification that, when tapped, will take a screenshot of the current activity, then start a new activity to collect and submit feedback from the tester along with the screenshot.

On Android 13 and above, this method requires the runtime permission for sending notifications: [`
POST_NOTIFICATIONS`](https://developer.android.com/develop/ui/views/notifications/notification-permission). If your app targets Android 13 (API level 33) or above, you should [request the permission](https://developer.android.com/training/permissions/requesting).

When the notification is tapped:

1. If the app is open, takes a screenshot of the current activity.
2. If the tester is not signed in, presents the tester with a Google Sign-in UI.
3. Starts a full screen activity for the tester to compose and submit the feedback.

| Parameters |
|---|---|
| `additionalFormText: @https://developer.android.com/reference/kotlin/androidx/annotation/StringRes.html https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | string resource ID of text that will be shown to the tester before they submit feedback. If you're a customer who would like to provide notice to your testers about collection and processing of their feedback data, you can use this text to provide such notice. |
| `interruptionLevel: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/InterruptionLevel` | the level of interruption for the feedback notification. On platforms below Android 8, this corresponds to a [notification channel importance](https://developer.android.com/develop/ui/views/notifications/channels#importance) and once set cannot be changed except by the tester. |

### signInTester

```
fun signInTester(): Task<Void!>
```

Signs in the App Distribution tester. Presents the tester with a Google sign in UI.

If you don't include the `com.google.firebase:firebase-appdistribution` artifact in your build, then this method returns a failed `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html` with `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/FirebaseAppDistributionException.Status#NOT_IMPLEMENTED`.

### signOutTester

```
fun signOutTester(): Unit
```

Signs out the App Distribution tester.

If you don't include the `com.google.firebase:firebase-appdistribution` artifact in your build, then this method is a no-op.

### startFeedback

```
fun startFeedback(additionalFormText: CharSequence): Unit
```

Takes a screenshot, and starts an activity to collect and submit feedback from the tester.

Performs the following actions:

1. Takes a screenshot of the current activity.
2. If the tester is not signed in, presents the tester with a Google Sign-in UI.
3. Starts a full screen activity for the tester to compose and submit the feedback.

| Parameters |
|---|---|
| `additionalFormText: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-char-sequence/index.html` | text that will be shown to the tester before they submit feedback. If you're a customer who would like to provide notice to your testers about collection and processing of their feedback data, you can use this text to provide such notice. |

### startFeedback

```
fun startFeedback(additionalFormText: @StringRes Int): Unit
```

Takes a screenshot, and starts an activity to collect and submit feedback from the tester.

Performs the following actions:

1. Takes a screenshot of the current activity.
2. If the tester is not signed in, presents the tester with a Google Sign-in UI.
3. Starts a full screen activity for the tester to compose and submit the feedback.

| Parameters |
|---|---|
| `additionalFormText: @https://developer.android.com/reference/kotlin/androidx/annotation/StringRes.html https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | string resource ID of text that will be shown to the tester before they submit feedback. If you're a customer who would like to provide notice to your testers about collection and processing of their feedback data, you can use this text to provide such notice. |

### startFeedback

```
fun startFeedback(additionalFormText: CharSequence, screenshot: Uri?): Unit
```

Starts an activity to collect and submit feedback from the tester, along with the given screenshot.

Performs the following actions:

1. If the tester is not signed in, presents the tester with a Google Sign-in UI.
2. Starts a full screen activity for the tester to compose and submit the feedback.

| Parameters |
|---|---|
| `additionalFormText: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-char-sequence/index.html` | text that will be shown to the tester before they submit feedback. If you're a customer who would like to provide notice to your testers about collection and processing of their feedback data, you can use this text to provide such notice. |
| `screenshot: https://developer.android.com/reference/kotlin/android/net/Uri.html?` | URI to a bitmap containing a screenshot that will be included with the report, or null to not include a screenshot |

### startFeedback

```
fun startFeedback(additionalFormText: @StringRes Int, screenshot: Uri?): Unit
```

Starts an activity to collect and submit feedback from the tester, along with the given screenshot.

Performs the following actions:

1. If the tester is not signed in, presents the tester with a Google Sign-in UI.
2. Starts a full screen activity for the tester to compose and submit the feedback.

| Parameters |
|---|---|
| `additionalFormText: @https://developer.android.com/reference/kotlin/androidx/annotation/StringRes.html https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | string resource ID of text that will be shown to the tester before they submit feedback. If you're a customer who would like to provide notice to your testers about collection and processing of their feedback data, you can use this text to provide such notice. |
| `screenshot: https://developer.android.com/reference/kotlin/android/net/Uri.html?` | URI to a bitmap containing a screenshot that will be included with the report, or null to not include a screenshot |

### updateApp

```
fun updateApp(): UpdateTask
```

Updates app to the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/AppDistributionRelease` returned by `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/FirebaseAppDistribution#checkForNewRelease()`.

If the newest release is an APK, downloads the binary and starts an installation. If the newest release is an AAB, directs the tester to the Play app to complete the download and installation.

Fails the `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html` with `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/FirebaseAppDistributionException.Status#UPDATE_NOT_AVAILABLE` if no new release is cached from `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/FirebaseAppDistribution#checkForNewRelease()`.

If you don't include the `com.google.firebase:firebase-appdistribution` artifact in your build, then this method returns a failed `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/UpdateTask` with `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/FirebaseAppDistributionException.Status#NOT_IMPLEMENTED`.

### updateIfNewReleaseAvailable

```
fun updateIfNewReleaseAvailable(): UpdateTask
```

Updates the app to the newest release, if one is available.

Returns the release information or `null` if no update is found. Performs the following actions:

1. If the tester is not signed in, presents the tester with a Google Sign-in UI.
2. Checks if a newer release is available. If so, presents the tester with a confirmation dialog to begin the download.
3. If the newest release is an APK, downloads the binary and starts an installation. If the newest release is an AAB, directs the tester to the Play app to complete the download and installation.

If you don't include the `com.google.firebase:firebase-appdistribution` artifact in your build, then this method returns a failed `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html` with `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/FirebaseAppDistributionException.Status#NOT_IMPLEMENTED`.