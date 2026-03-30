# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/crashlytics/FirebaseCrashlytics.md.txt

# FirebaseCrashlytics

# FirebaseCrashlytics


```
public class FirebaseCrashlytics
```

<br />

*** ** * ** ***

The Firebase Crashlytics API provides methods to annotate and manage fatal crashes, non-fatal errors, and ANRs captured and reported to Firebase Crashlytics.

By default, Firebase Crashlytics is automatically initialized.

Call `https://firebase.google.com/docs/reference/android/com/google/firebase/crashlytics/FirebaseCrashlytics#getInstance()` to get the singleton instance of FirebaseCrashlytics.

## Summary

| ### Public methods |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/kotlin/java/lang/Boolean.html>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/crashlytics/FirebaseCrashlytics#checkForUnsentReports()()` Checks a device for any fatal crash, non-fatal error, or ANR reports that haven't yet been sent to Crashlytics. |
| `void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/crashlytics/FirebaseCrashlytics#deleteUnsentReports()()` If automatic data collection is disabled, this method queues up all the reports on a device for deletion. |
| `boolean` | `https://firebase.google.com/docs/reference/android/com/google/firebase/crashlytics/FirebaseCrashlytics#didCrashOnPreviousExecution()()` Checks whether the app crashed on its previous run. |
| `static @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/crashlytics/FirebaseCrashlytics` | `https://firebase.google.com/docs/reference/android/com/google/firebase/crashlytics/FirebaseCrashlytics#getInstance()()` Gets the singleton `https://firebase.google.com/docs/reference/android/com/google/firebase/crashlytics/FirebaseCrashlytics` instance. |
| `boolean` | `https://firebase.google.com/docs/reference/android/com/google/firebase/crashlytics/FirebaseCrashlytics#isCrashlyticsCollectionEnabled()()` Indicates whether or not automatic data collection is enabled. |
| `void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/crashlytics/FirebaseCrashlytics#log(java.lang.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html message)` Logs a message that's included in the next fatal, non-fatal, or ANR report. |
| `void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/crashlytics/FirebaseCrashlytics#recordException(java.lang.Throwable)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Throwable.html throwable)` Records a non-fatal report to send to Crashlytics. |
| `void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/crashlytics/FirebaseCrashlytics#recordException(java.lang.Throwable,com.google.firebase.crashlytics.CustomKeysAndValues)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Throwable.html throwable, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/crashlytics/CustomKeysAndValues keysAndValues )` Records a non-fatal report to send to Crashlytics. |
| `void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/crashlytics/FirebaseCrashlytics#sendUnsentReports()()` If automatic data collection is disabled, this method queues up all the reports on a device to send to Crashlytics. |
| `void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/crashlytics/FirebaseCrashlytics#setCrashlyticsCollectionEnabled(java.lang.Boolean)(@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/Boolean.html enabled)` Enables or disables the automatic data collection configuration for Crashlytics. |
| `void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/crashlytics/FirebaseCrashlytics#setCrashlyticsCollectionEnabled(boolean)(boolean enabled)` Enables or disables the automatic data collection configuration for Crashlytics. |
| `void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/crashlytics/FirebaseCrashlytics#setCustomKey(java.lang.String,java.lang.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html key, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html value)` Sets a custom key and value that are associated with subsequent fatal, non-fatal, and ANR reports. |
| `void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/crashlytics/FirebaseCrashlytics#setCustomKey(java.lang.String,boolean)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html key, boolean value)` Sets a custom key and value that are associated with subsequent fatal, non-fatal, and ANR reports. |
| `void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/crashlytics/FirebaseCrashlytics#setCustomKey(java.lang.String,double)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html key, double value)` Sets a custom key and value that are associated with subsequent fatal and non-fatal reports. |
| `void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/crashlytics/FirebaseCrashlytics#setCustomKey(java.lang.String,float)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html key, float value)` Sets a custom key and value that are associated with subsequent fatal, non-fatal, and ANR reports. |
| `void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/crashlytics/FirebaseCrashlytics#setCustomKey(java.lang.String,int)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html key, int value)` Sets a custom key and value that are associated with subsequent fatal, non-fatal, and ANR reports. |
| `void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/crashlytics/FirebaseCrashlytics#setCustomKey(java.lang.String,long)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html key, long value)` Records a custom key and value to be associated with subsequent fatal, non-fatal, and ANR reports. |
| `void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/crashlytics/FirebaseCrashlytics#setCustomKeys(com.google.firebase.crashlytics.CustomKeysAndValues)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/crashlytics/CustomKeysAndValues keysAndValues)` Sets multiple custom keys and values that are associated with subsequent fatal, non-fatal, and ANR reports. |
| `void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/crashlytics/FirebaseCrashlytics#setUserId(java.lang.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html identifier)` Records a user ID (identifier) that's associated with subsequent fatal, non-fatal, and ANR reports. |

| ### Extension functions |
|---|---|
| `final void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/crashlytics/FirebaseCrashlyticsKt.https://firebase.google.com/docs/reference/android/com/google/firebase/crashlytics/FirebaseCrashlytics#(com.google.firebase.crashlytics.FirebaseCrashlytics).recordException(kotlin.Throwable,kotlin.Function1)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/crashlytics/FirebaseCrashlytics receiver, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Throwable.html throwable, @https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-extension-function-type/index.html @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html Function1<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/crashlytics/KeyValueBuilder, https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html> init )` Records a non-fatal report to send to Crashlytics with additional custom keys |
| `final void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/crashlytics/FirebaseCrashlyticsKt.https://firebase.google.com/docs/reference/android/com/google/firebase/crashlytics/FirebaseCrashlytics#(com.google.firebase.crashlytics.FirebaseCrashlytics).setCustomKeys(kotlin.Function1)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/crashlytics/FirebaseCrashlytics receiver, @https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-extension-function-type/index.html @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html Function1<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/crashlytics/KeyValueBuilder, https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html> init )` Associates all key-value parameters with the reports |

## Public methods

### checkForUnsentReports

```
public @NonNull Task<Boolean> checkForUnsentReports()
```

Checks a device for any fatal crash, non-fatal error, or ANR reports that haven't yet been sent to Crashlytics. If automatic data collection is enabled, then reports are uploaded automatically and this always returns false. If automatic data collection is disabled, this method can be used to check whether the user opts-in to send crash reports from their device.

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/kotlin/java/lang/Boolean.html>` | a Task that is resolved with the result. |

### deleteUnsentReports

```
public void deleteUnsentReports()
```

If automatic data collection is disabled, this method queues up all the reports on a device for deletion. Otherwise, this method is a no-op.

### didCrashOnPreviousExecution

```
public boolean didCrashOnPreviousExecution()
```

Checks whether the app crashed on its previous run.

| Returns |
|---|---|
| `boolean` | true if a crash was recorded during the previous run of the app. |

### getInstance

```
public static @NonNull FirebaseCrashlytics getInstance()
```

Gets the singleton `https://firebase.google.com/docs/reference/android/com/google/firebase/crashlytics/FirebaseCrashlytics` instance.

The default `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp` instance must be initialized before this function is called. See [FirebaseApp](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp) for more information.

### isCrashlyticsCollectionEnabled

```
public boolean isCrashlyticsCollectionEnabled()
```

Indicates whether or not automatic data collection is enabled.

| Returns |
|---|---|
| `boolean` | In order of priority: - If `https://firebase.google.com/docs/reference/android/com/google/firebase/crashlytics/FirebaseCrashlytics#setCrashlyticsCollectionEnabled(boolean)` is called with a value, use it. - If the **firebase_crashlytics_collection_enabled** key is in your app's ` AndroidManifest.xml`, use it. - Otherwise, use the default `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp#isDataCollectionDefaultEnabled()` in `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp`. |

### log

```
public void log(@NonNull String message)
```

Logs a message that's included in the next fatal, non-fatal, or ANR report.

Logs are visible in the session view on the Firebase Crashlytics console.

Newline characters are stripped and extremely long messages are truncated. The maximum log size is 64k. If exceeded, the log rolls such that messages are removed, starting from the oldest.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html message` | the message to be logged |

### recordException

```
public void recordException(@NonNull Throwable throwable)
```

Records a non-fatal report to send to Crashlytics.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Throwable.html throwable` | a `https://developer.android.com/reference/kotlin/java/lang/Throwable.html` to be recorded as a non-fatal event. |

### recordException

```
public void recordException(
    @NonNull Throwable throwable,
    @NonNull CustomKeysAndValues keysAndValues
)
```

Records a non-fatal report to send to Crashlytics.

Combined with app level custom keys, the event is restricted to a maximum of 64 key/value pairs. New keys beyond that limit are ignored. Keys or values that exceed 1024 characters are truncated.

The values of event keys override the values of app level custom keys if they're identical.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Throwable.html throwable` | a `https://developer.android.com/reference/kotlin/java/lang/Throwable.html` to be recorded as a non-fatal event. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/crashlytics/CustomKeysAndValues keysAndValues` | A dictionary of keys and the values to associate with the non fatal exception, in addition to the app level custom keys. |

### sendUnsentReports

```
public void sendUnsentReports()
```

If automatic data collection is disabled, this method queues up all the reports on a device to send to Crashlytics. Otherwise, this method is a no-op.

### setCrashlyticsCollectionEnabled

```
public void setCrashlyticsCollectionEnabled(@Nullable Boolean enabled)
```

Enables or disables the automatic data collection configuration for Crashlytics.

If this is set, it overrides any automatic data collection settings configured in the `
AndroidManifest.xml` as well as any Firebase-wide settings. If set to `null`, the override is cleared.

If automatic data collection is disabled for Crashlytics, crash reports are stored on the device. To check for reports, use the `https://firebase.google.com/docs/reference/android/com/google/firebase/crashlytics/FirebaseCrashlytics#checkForUnsentReports()` method. Use `https://firebase.google.com/docs/reference/android/com/google/firebase/crashlytics/FirebaseCrashlytics#sendUnsentReports()` to upload existing reports even when automatic data collection is disabled. Use `https://firebase.google.com/docs/reference/android/com/google/firebase/crashlytics/FirebaseCrashlytics#deleteUnsentReports()` to delete any reports stored on the device without sending them to Crashlytics.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/Boolean.html enabled` | whether to enable or disable automatic data collection. When set to ` false`, the new value does not apply until the next run of the app. When set to ` null`, the override is cleared and automatic data collection settings are determined by the configuration in your `AndroidManifest.xml` or other Firebase-wide settings. |

### setCrashlyticsCollectionEnabled

```
public void setCrashlyticsCollectionEnabled(boolean enabled)
```

Enables or disables the automatic data collection configuration for Crashlytics.

If this is set, it overrides any automatic data collection settings configured in the `
AndroidManifest.xml` as well as any Firebase-wide settings.

If automatic data collection is disabled for Crashlytics, crash reports are stored on the device. To check for reports, use the `https://firebase.google.com/docs/reference/android/com/google/firebase/crashlytics/FirebaseCrashlytics#checkForUnsentReports()` method. Use `https://firebase.google.com/docs/reference/android/com/google/firebase/crashlytics/FirebaseCrashlytics#sendUnsentReports()` to upload existing reports even when automatic data collection is disabled. Use `https://firebase.google.com/docs/reference/android/com/google/firebase/crashlytics/FirebaseCrashlytics#deleteUnsentReports()` to delete any reports stored on the device without sending them to Crashlytics.

| Parameters |
|---|---|
| `boolean enabled` | whether to enable automatic data collection. When set to `false`, the new value does not apply until the next run of the app. To disable data collection by default for all app runs, add the `firebase_crashlytics_collection_enabled` flag to your app's `AndroidManifest.xml`. |

### setCustomKey

```
public void setCustomKey(@NonNull String key, @NonNull String value)
```

Sets a custom key and value that are associated with subsequent fatal, non-fatal, and ANR reports.

Multiple calls to this method with the same key update the value for that key.

The value of any key at the time of a fatal, non-fatal, or ANR event is associated with that event.

Keys and associated values are visible in the session view on the Firebase Crashlytics console.

Accepts a maximum of 64 key/value pairs. New keys beyond that limit are ignored. Keys or values that exceed 1024 characters are truncated.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html key` | A unique key |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html value` | A value to be associated with the given key |

### setCustomKey

```
public void setCustomKey(@NonNull String key, boolean value)
```

Sets a custom key and value that are associated with subsequent fatal, non-fatal, and ANR reports.

Multiple calls to this method with the same key update the value for that key.

The value of any key at the time of a fatal, non-fatal, or ANR event is associated with that event.

Keys and associated values are visible in the session view on the Firebase Crashlytics console.

Accepts a maximum of 64 key/value pairs. New keys beyond that limit are ignored. Keys or values that exceed 1024 characters are truncated.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html key` | A unique key |
| `boolean value` | A value to be associated with the given key |

### setCustomKey

```
public void setCustomKey(@NonNull String key, double value)
```

Sets a custom key and value that are associated with subsequent fatal and non-fatal reports.

Multiple calls to this method with the same key update the value for that key.

The value of any key at the time of a fatal or non-fatal event is associated with that event.

Keys and associated values are visible in the session view on the Firebase Crashlytics console.

Accepts a maximum of 64 key/value pairs. New keys beyond that limit are ignored. Keys or values that exceed 1024 characters are truncated.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html key` | A unique key |
| `double value` | A value to be associated with the given key |

### setCustomKey

```
public void setCustomKey(@NonNull String key, float value)
```

Sets a custom key and value that are associated with subsequent fatal, non-fatal, and ANR reports.

Multiple calls to this method with the same key update the value for that key.

The value of any key at the time of a fatal, non-fatal, or ANR event is associated with that event.

Keys and associated values are visible in the session view on the Firebase Crashlytics console.

Accepts a maximum of 64 key/value pairs. New keys beyond that limit are ignored. Keys or values that exceed 1024 characters are truncated.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html key` | A unique key |
| `float value` | A value to be associated with the given key |

### setCustomKey

```
public void setCustomKey(@NonNull String key, int value)
```

Sets a custom key and value that are associated with subsequent fatal, non-fatal, and ANR reports.

Multiple calls to this method with the same key update the value for that key.

The value of any key at the time of a fatal, non-fatal, or ANR event is associated with that event.

Keys and associated values are visible in the session view on the Firebase Crashlytics console.

Accepts a maximum of 64 key/value pairs. New keys beyond that limit are ignored. Keys or values that exceed 1024 characters are truncated.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html key` | A unique key |
| `int value` | A value to be associated with the given key |

### setCustomKey

```
public void setCustomKey(@NonNull String key, long value)
```

Records a custom key and value to be associated with subsequent fatal, non-fatal, and ANR reports.

Multiple calls to this method with the same key will update the value for that key.

The value of any key at the time of a fatal, non-fatal, or ANR event will be associated with that event.

Keys and associated values are visible in the session view on the Firebase Crashlytics console.

A maximum of 64 key/value pairs can be written, and new keys added beyond that limit will be ignored. Keys or values that exceed 1024 characters will be truncated.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html key` | A unique key |
| `long value` | A value to be associated with the given key |

### setCustomKeys

```
public void setCustomKeys(@NonNull CustomKeysAndValues keysAndValues)
```

Sets multiple custom keys and values that are associated with subsequent fatal, non-fatal, and ANR reports. This method is intended as an alternative to `setCustomKey` in order to reduce the computational load of writing out multiple key/value pairs at the same time.

Multiple calls to this method with the same key update the value for that key.

The value of any key at the time of a fatal, non-fatal, or ANR event is associated with that event.

Keys and associated values are visible in the session view on the Firebase Crashlytics console.

Accepts a maximum of 64 key/value pairs. If calling this method results in the number of custom keys exceeding this limit, only some of the keys will be logged (however many are needed to get to 64). Which keys are logged versus dropped is unpredictable as there is no intrinsic sorting of keys. Keys or values that exceed 1024 characters are truncated.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/crashlytics/CustomKeysAndValues keysAndValues` | A dictionary of keys and the values to associate with each key |

### setUserId

```
public void setUserId(@NonNull String identifier)
```

Records a user ID (identifier) that's associated with subsequent fatal, non-fatal, and ANR reports.

The user ID is visible in the session view on the Firebase Crashlytics console.

Identifiers longer than 1024 characters will be truncated.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html identifier` | a unique identifier for the current user |

## Extension functions

### FirebaseCrashlyticsKt.recordException

```
public final void FirebaseCrashlyticsKt.recordException(
    @NonNull FirebaseCrashlytics receiver,
    @NonNull Throwable throwable,
    @ExtensionFunctionType @NonNull Function1<@NonNull KeyValueBuilder, Unit> init
)
```

Records a non-fatal report to send to Crashlytics with additional custom keys

### FirebaseCrashlyticsKt.setCustomKeys

```
public final void FirebaseCrashlyticsKt.setCustomKeys(
    @NonNull FirebaseCrashlytics receiver,
    @ExtensionFunctionType @NonNull Function1<@NonNull KeyValueBuilder, Unit> init
)
```

Associates all key-value parameters with the reports