# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/crashlytics/FirebaseCrashlytics.md.txt

# FirebaseCrashlytics

# FirebaseCrashlytics


```
class FirebaseCrashlytics
```

<br />

*** ** * ** ***

The Firebase Crashlytics API provides methods to annotate and manage fatal crashes, non-fatal errors, and ANRs captured and reported to Firebase Crashlytics.

By default, Firebase Crashlytics is automatically initialized.

Call `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/crashlytics/FirebaseCrashlytics#getInstance()` to get the singleton instance of FirebaseCrashlytics.

## Summary

| ### Public functions |
|---|---|
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html!>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/crashlytics/FirebaseCrashlytics#checkForUnsentReports()()` Checks a device for any fatal crash, non-fatal error, or ANR reports that haven't yet been sent to Crashlytics. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/crashlytics/FirebaseCrashlytics#deleteUnsentReports()()` If automatic data collection is disabled, this method queues up all the reports on a device for deletion. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/crashlytics/FirebaseCrashlytics#didCrashOnPreviousExecution()()` Checks whether the app crashed on its previous run. |
| `java-static https://firebase.google.com/docs/reference/kotlin/com/google/firebase/crashlytics/FirebaseCrashlytics` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/crashlytics/FirebaseCrashlytics#getInstance()()` Gets the singleton `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/crashlytics/FirebaseCrashlytics` instance. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/crashlytics/FirebaseCrashlytics#isCrashlyticsCollectionEnabled()()` Indicates whether or not automatic data collection is enabled. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/crashlytics/FirebaseCrashlytics#log(java.lang.String)(message: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Logs a message that's included in the next fatal, non-fatal, or ANR report. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/crashlytics/FirebaseCrashlytics#recordException(java.lang.Throwable)(throwable: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html)` Records a non-fatal report to send to Crashlytics. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/crashlytics/FirebaseCrashlytics#recordException(java.lang.Throwable,com.google.firebase.crashlytics.CustomKeysAndValues)(throwable: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html, keysAndValues: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/crashlytics/CustomKeysAndValues)` Records a non-fatal report to send to Crashlytics. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/crashlytics/FirebaseCrashlytics#sendUnsentReports()()` If automatic data collection is disabled, this method queues up all the reports on a device to send to Crashlytics. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/crashlytics/FirebaseCrashlytics#setCrashlyticsCollectionEnabled(java.lang.Boolean)(enabled: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html?)` Enables or disables the automatic data collection configuration for Crashlytics. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/crashlytics/FirebaseCrashlytics#setCrashlyticsCollectionEnabled(boolean)(enabled: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` Enables or disables the automatic data collection configuration for Crashlytics. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/crashlytics/FirebaseCrashlytics#setCustomKey(java.lang.String,java.lang.String)(key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Sets a custom key and value that are associated with subsequent fatal, non-fatal, and ANR reports. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/crashlytics/FirebaseCrashlytics#setCustomKey(java.lang.String,boolean)(key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` Sets a custom key and value that are associated with subsequent fatal, non-fatal, and ANR reports. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/crashlytics/FirebaseCrashlytics#setCustomKey(java.lang.String,double)(key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html)` Sets a custom key and value that are associated with subsequent fatal and non-fatal reports. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/crashlytics/FirebaseCrashlytics#setCustomKey(java.lang.String,float)(key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-float/index.html)` Sets a custom key and value that are associated with subsequent fatal, non-fatal, and ANR reports. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/crashlytics/FirebaseCrashlytics#setCustomKey(java.lang.String,int)(key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` Sets a custom key and value that are associated with subsequent fatal, non-fatal, and ANR reports. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/crashlytics/FirebaseCrashlytics#setCustomKey(java.lang.String,long)(key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html)` Records a custom key and value to be associated with subsequent fatal, non-fatal, and ANR reports. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/crashlytics/FirebaseCrashlytics#setCustomKeys(com.google.firebase.crashlytics.CustomKeysAndValues)(keysAndValues: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/crashlytics/CustomKeysAndValues)` Sets multiple custom keys and values that are associated with subsequent fatal, non-fatal, and ANR reports. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/crashlytics/FirebaseCrashlytics#setUserId(java.lang.String)(identifier: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Records a user ID (identifier) that's associated with subsequent fatal, non-fatal, and ANR reports. |

| ### Extension functions |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/crashlytics/FirebaseCrashlytics.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/crashlytics/FirebaseCrashlytics#(com.google.firebase.crashlytics.FirebaseCrashlytics).recordException(kotlin.Throwable,kotlin.Function1)( throwable: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html, init: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/crashlytics/KeyValueBuilder.() -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html )` Records a non-fatal report to send to Crashlytics with additional custom keys |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/crashlytics/FirebaseCrashlytics.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/crashlytics/FirebaseCrashlytics#(com.google.firebase.crashlytics.FirebaseCrashlytics).setCustomKeys(kotlin.Function1)(init: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/crashlytics/KeyValueBuilder.() -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` Associates all key-value parameters with the reports |

## Public functions

### checkForUnsentReports

```
fun checkForUnsentReports(): Task<Boolean!>
```

Checks a device for any fatal crash, non-fatal error, or ANR reports that haven't yet been sent to Crashlytics. If automatic data collection is enabled, then reports are uploaded automatically and this always returns false. If automatic data collection is disabled, this method can be used to check whether the user opts-in to send crash reports from their device.

| Returns |
|---|---|
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html!>` | a Task that is resolved with the result. |

### deleteUnsentReports

```
fun deleteUnsentReports(): Unit
```

If automatic data collection is disabled, this method queues up all the reports on a device for deletion. Otherwise, this method is a no-op.

### didCrashOnPreviousExecution

```
fun didCrashOnPreviousExecution(): Boolean
```

Checks whether the app crashed on its previous run.

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | true if a crash was recorded during the previous run of the app. |

### getInstance

```
java-static fun getInstance(): FirebaseCrashlytics
```

Gets the singleton `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/crashlytics/FirebaseCrashlytics` instance.

The default `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp` instance must be initialized before this function is called. See [FirebaseApp](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp) for more information.

### isCrashlyticsCollectionEnabled

```
fun isCrashlyticsCollectionEnabled(): Boolean
```

Indicates whether or not automatic data collection is enabled.

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | In order of priority: - If `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/crashlytics/FirebaseCrashlytics#setCrashlyticsCollectionEnabled(boolean)` is called with a value, use it. - If the **firebase_crashlytics_collection_enabled** key is in your app's ` AndroidManifest.xml`, use it. - Otherwise, use the default `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp#isDataCollectionDefaultEnabled()` in `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp`. |

### log

```
fun log(message: String): Unit
```

Logs a message that's included in the next fatal, non-fatal, or ANR report.

Logs are visible in the session view on the Firebase Crashlytics console.

Newline characters are stripped and extremely long messages are truncated. The maximum log size is 64k. If exceeded, the log rolls such that messages are removed, starting from the oldest.

| Parameters |
|---|---|
| `message: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | the message to be logged |

### recordException

```
fun recordException(throwable: Throwable): Unit
```

Records a non-fatal report to send to Crashlytics.

| Parameters |
|---|---|
| `throwable: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html` | a `https://developer.android.com/reference/kotlin/java/lang/Throwable.html` to be recorded as a non-fatal event. |

### recordException

```
fun recordException(throwable: Throwable, keysAndValues: CustomKeysAndValues): Unit
```

Records a non-fatal report to send to Crashlytics.

Combined with app level custom keys, the event is restricted to a maximum of 64 key/value pairs. New keys beyond that limit are ignored. Keys or values that exceed 1024 characters are truncated.

The values of event keys override the values of app level custom keys if they're identical.

| Parameters |
|---|---|
| `throwable: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html` | a `https://developer.android.com/reference/kotlin/java/lang/Throwable.html` to be recorded as a non-fatal event. |
| `keysAndValues: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/crashlytics/CustomKeysAndValues` | A dictionary of keys and the values to associate with the non fatal exception, in addition to the app level custom keys. |

### sendUnsentReports

```
fun sendUnsentReports(): Unit
```

If automatic data collection is disabled, this method queues up all the reports on a device to send to Crashlytics. Otherwise, this method is a no-op.

### setCrashlyticsCollectionEnabled

```
fun setCrashlyticsCollectionEnabled(enabled: Boolean?): Unit
```

Enables or disables the automatic data collection configuration for Crashlytics.

If this is set, it overrides any automatic data collection settings configured in the `
AndroidManifest.xml` as well as any Firebase-wide settings. If set to `null`, the override is cleared.

If automatic data collection is disabled for Crashlytics, crash reports are stored on the device. To check for reports, use the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/crashlytics/FirebaseCrashlytics#checkForUnsentReports()` method. Use `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/crashlytics/FirebaseCrashlytics#sendUnsentReports()` to upload existing reports even when automatic data collection is disabled. Use `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/crashlytics/FirebaseCrashlytics#deleteUnsentReports()` to delete any reports stored on the device without sending them to Crashlytics.

| Parameters |
|---|---|
| `enabled: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html?` | whether to enable or disable automatic data collection. When set to ` false`, the new value does not apply until the next run of the app. When set to ` null`, the override is cleared and automatic data collection settings are determined by the configuration in your `AndroidManifest.xml` or other Firebase-wide settings. |

### setCrashlyticsCollectionEnabled

```
fun setCrashlyticsCollectionEnabled(enabled: Boolean): Unit
```

Enables or disables the automatic data collection configuration for Crashlytics.

If this is set, it overrides any automatic data collection settings configured in the `
AndroidManifest.xml` as well as any Firebase-wide settings.

If automatic data collection is disabled for Crashlytics, crash reports are stored on the device. To check for reports, use the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/crashlytics/FirebaseCrashlytics#checkForUnsentReports()` method. Use `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/crashlytics/FirebaseCrashlytics#sendUnsentReports()` to upload existing reports even when automatic data collection is disabled. Use `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/crashlytics/FirebaseCrashlytics#deleteUnsentReports()` to delete any reports stored on the device without sending them to Crashlytics.

| Parameters |
|---|---|
| `enabled: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | whether to enable automatic data collection. When set to `false`, the new value does not apply until the next run of the app. To disable data collection by default for all app runs, add the `firebase_crashlytics_collection_enabled` flag to your app's `AndroidManifest.xml`. |

### setCustomKey

```
fun setCustomKey(key: String, value: String): Unit
```

Sets a custom key and value that are associated with subsequent fatal, non-fatal, and ANR reports.

Multiple calls to this method with the same key update the value for that key.

The value of any key at the time of a fatal, non-fatal, or ANR event is associated with that event.

Keys and associated values are visible in the session view on the Firebase Crashlytics console.

Accepts a maximum of 64 key/value pairs. New keys beyond that limit are ignored. Keys or values that exceed 1024 characters are truncated.

| Parameters |
|---|---|
| `key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | A unique key |
| `value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | A value to be associated with the given key |

### setCustomKey

```
fun setCustomKey(key: String, value: Boolean): Unit
```

Sets a custom key and value that are associated with subsequent fatal, non-fatal, and ANR reports.

Multiple calls to this method with the same key update the value for that key.

The value of any key at the time of a fatal, non-fatal, or ANR event is associated with that event.

Keys and associated values are visible in the session view on the Firebase Crashlytics console.

Accepts a maximum of 64 key/value pairs. New keys beyond that limit are ignored. Keys or values that exceed 1024 characters are truncated.

| Parameters |
|---|---|
| `key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | A unique key |
| `value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | A value to be associated with the given key |

### setCustomKey

```
fun setCustomKey(key: String, value: Double): Unit
```

Sets a custom key and value that are associated with subsequent fatal and non-fatal reports.

Multiple calls to this method with the same key update the value for that key.

The value of any key at the time of a fatal or non-fatal event is associated with that event.

Keys and associated values are visible in the session view on the Firebase Crashlytics console.

Accepts a maximum of 64 key/value pairs. New keys beyond that limit are ignored. Keys or values that exceed 1024 characters are truncated.

| Parameters |
|---|---|
| `key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | A unique key |
| `value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html` | A value to be associated with the given key |

### setCustomKey

```
fun setCustomKey(key: String, value: Float): Unit
```

Sets a custom key and value that are associated with subsequent fatal, non-fatal, and ANR reports.

Multiple calls to this method with the same key update the value for that key.

The value of any key at the time of a fatal, non-fatal, or ANR event is associated with that event.

Keys and associated values are visible in the session view on the Firebase Crashlytics console.

Accepts a maximum of 64 key/value pairs. New keys beyond that limit are ignored. Keys or values that exceed 1024 characters are truncated.

| Parameters |
|---|---|
| `key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | A unique key |
| `value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-float/index.html` | A value to be associated with the given key |

### setCustomKey

```
fun setCustomKey(key: String, value: Int): Unit
```

Sets a custom key and value that are associated with subsequent fatal, non-fatal, and ANR reports.

Multiple calls to this method with the same key update the value for that key.

The value of any key at the time of a fatal, non-fatal, or ANR event is associated with that event.

Keys and associated values are visible in the session view on the Firebase Crashlytics console.

Accepts a maximum of 64 key/value pairs. New keys beyond that limit are ignored. Keys or values that exceed 1024 characters are truncated.

| Parameters |
|---|---|
| `key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | A unique key |
| `value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | A value to be associated with the given key |

### setCustomKey

```
fun setCustomKey(key: String, value: Long): Unit
```

Records a custom key and value to be associated with subsequent fatal, non-fatal, and ANR reports.

Multiple calls to this method with the same key will update the value for that key.

The value of any key at the time of a fatal, non-fatal, or ANR event will be associated with that event.

Keys and associated values are visible in the session view on the Firebase Crashlytics console.

A maximum of 64 key/value pairs can be written, and new keys added beyond that limit will be ignored. Keys or values that exceed 1024 characters will be truncated.

| Parameters |
|---|---|
| `key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | A unique key |
| `value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` | A value to be associated with the given key |

### setCustomKeys

```
fun setCustomKeys(keysAndValues: CustomKeysAndValues): Unit
```

Sets multiple custom keys and values that are associated with subsequent fatal, non-fatal, and ANR reports. This method is intended as an alternative to `setCustomKey` in order to reduce the computational load of writing out multiple key/value pairs at the same time.

Multiple calls to this method with the same key update the value for that key.

The value of any key at the time of a fatal, non-fatal, or ANR event is associated with that event.

Keys and associated values are visible in the session view on the Firebase Crashlytics console.

Accepts a maximum of 64 key/value pairs. If calling this method results in the number of custom keys exceeding this limit, only some of the keys will be logged (however many are needed to get to 64). Which keys are logged versus dropped is unpredictable as there is no intrinsic sorting of keys. Keys or values that exceed 1024 characters are truncated.

| Parameters |
|---|---|
| `keysAndValues: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/crashlytics/CustomKeysAndValues` | A dictionary of keys and the values to associate with each key |

### setUserId

```
fun setUserId(identifier: String): Unit
```

Records a user ID (identifier) that's associated with subsequent fatal, non-fatal, and ANR reports.

The user ID is visible in the session view on the Firebase Crashlytics console.

Identifiers longer than 1024 characters will be truncated.

| Parameters |
|---|---|
| `identifier: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | a unique identifier for the current user |

## Extension functions

### recordException

```
fun FirebaseCrashlytics.recordException(
    throwable: Throwable,
    init: KeyValueBuilder.() -> Unit
): Unit
```

Records a non-fatal report to send to Crashlytics with additional custom keys

### setCustomKeys

```
fun FirebaseCrashlytics.setCustomKeys(init: KeyValueBuilder.() -> Unit): Unit
```

Associates all key-value parameters with the reports