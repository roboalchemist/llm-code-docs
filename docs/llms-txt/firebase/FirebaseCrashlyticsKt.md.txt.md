# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/crashlytics/FirebaseCrashlyticsKt.md.txt

# FirebaseCrashlyticsKt

# FirebaseCrashlyticsKt


```
public final class FirebaseCrashlyticsKt
```

<br />

*** ** * ** ***

## Summary

| ### Public fields |
|---|---|
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/crashlytics/FirebaseCrashlytics` | `https://firebase.google.com/docs/reference/android/com/google/firebase/crashlytics/package-summary#(com.google.firebase.Firebase).crashlytics()` Returns the `https://firebase.google.com/docs/reference/android/com/google/firebase/crashlytics/FirebaseCrashlytics` instance of the default `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp`. |

| ### Public methods |
|---|---|
| `static final void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/crashlytics/FirebaseCrashlyticsKt.https://firebase.google.com/docs/reference/android/com/google/firebase/crashlytics/FirebaseCrashlyticsKt#(com.google.firebase.crashlytics.FirebaseCrashlytics).recordException(kotlin.Throwable,kotlin.Function1)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/crashlytics/FirebaseCrashlytics receiver, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Throwable.html throwable, @https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-extension-function-type/index.html @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html Function1<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/crashlytics/KeyValueBuilder, https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html> init )` Records a non-fatal report to send to Crashlytics with additional custom keys |
| `static final void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/crashlytics/FirebaseCrashlyticsKt.https://firebase.google.com/docs/reference/android/com/google/firebase/crashlytics/FirebaseCrashlyticsKt#(com.google.firebase.crashlytics.FirebaseCrashlytics).setCustomKeys(kotlin.Function1)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/crashlytics/FirebaseCrashlytics receiver, @https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-extension-function-type/index.html @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html Function1<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/crashlytics/KeyValueBuilder, https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html> init )` Associates all key-value parameters with the reports |

## Public fields

### crashlytics

```
public final @NonNull FirebaseCrashlytics crashlytics
```

Returns the `https://firebase.google.com/docs/reference/android/com/google/firebase/crashlytics/FirebaseCrashlytics` instance of the default `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp`.

## Public methods

### FirebaseCrashlyticsKt.recordException

```
public static final void FirebaseCrashlyticsKt.recordException(
    @NonNull FirebaseCrashlytics receiver,
    @NonNull Throwable throwable,
    @ExtensionFunctionType @NonNull Function1<@NonNull KeyValueBuilder, Unit> init
)
```

Records a non-fatal report to send to Crashlytics with additional custom keys

### FirebaseCrashlyticsKt.setCustomKeys

```
public static final void FirebaseCrashlyticsKt.setCustomKeys(
    @NonNull FirebaseCrashlytics receiver,
    @ExtensionFunctionType @NonNull Function1<@NonNull KeyValueBuilder, Unit> init
)
```

Associates all key-value parameters with the reports