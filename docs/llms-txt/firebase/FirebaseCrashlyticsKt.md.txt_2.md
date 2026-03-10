# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/crashlytics/ktx/FirebaseCrashlyticsKt.md.txt

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
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/crashlytics/FirebaseCrashlytics` | `https://firebase.google.com/docs/reference/android/com/google/firebase/crashlytics/ktx/package-summary#(com.google.firebase.ktx.Firebase).crashlytics()` Accessing this object for Kotlin apps has changed; see the [migration guide](https://firebase.google.com/docs/android/kotlin-migration). |

| ### Public methods |
|---|---|
| `static final void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/crashlytics/ktx/FirebaseCrashlyticsKt.[setCustomKeys](https://firebase.google.com/docs/reference/android/com/google/firebase/crashlytics/ktx/FirebaseCrashlyticsKt#(com.google.firebase.crashlytics.FirebaseCrashlytics).setCustomKeys(kotlin.Function1))( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/crashlytics/FirebaseCrashlytics receiver, @https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-extension-function-type/index.html @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html Function1<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/crashlytics/ktx/KeyValueBuilder, https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html> init )` **This method is deprecated.** Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration. |

## Public fields

### crashlytics

```
public final @NonNull FirebaseCrashlytics crashlytics
```

Accessing this object for Kotlin apps has changed; see the [migration guide](https://firebase.google.com/docs/android/kotlin-migration).

Returns the `https://firebase.google.com/docs/reference/android/com/google/firebase/crashlytics/FirebaseCrashlytics` instance of the default `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp`.

**Important:** In July 2025, we stopped releasing KTX modules and removed the KTX libraries from the Firebase Android BoM (v34.0.0). **If you use KTX APIs from the KTX modules, we recommend that you migrate your app to use KTX APIs from the main modules instead** . For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)

## Public methods

### FirebaseCrashlyticsKt.setCustomKeys

```
public static final void FirebaseCrashlyticsKt.[setCustomKeys](https://firebase.google.com/docs/reference/android/com/google/firebase/crashlytics/ktx/FirebaseCrashlyticsKt#(com.google.firebase.crashlytics.FirebaseCrashlytics).setCustomKeys(kotlin.Function1))(
    @NonNull FirebaseCrashlytics receiver,
    @ExtensionFunctionType @NonNull Function1<@NonNull KeyValueBuilder, Unit> init
)
```

> [!CAUTION]
> **This method is deprecated.**   
> Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration.

Associates all key-value parameters with the reports

**Important:** In July 2025, we stopped releasing KTX modules and removed the KTX libraries from the Firebase Android BoM (v34.0.0). **If you use KTX APIs from the KTX modules, we recommend that you migrate your app to use KTX APIs from the main modules instead** . For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)