# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/crashlytics/FirebaseCrashlyticsKt.md.txt

# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/crashlytics/ktx/FirebaseCrashlyticsKt.md.txt

# FirebaseCrashlyticsKt

# FirebaseCrashlyticsKt


```
public final class FirebaseCrashlyticsKt
```

<br />

*** ** * ** ***

## Summary

|                                                                                                          ### Public fields                                                                                                          |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[FirebaseCrashlytics](https://firebase.google.com/docs/reference/android/com/google/firebase/crashlytics/FirebaseCrashlytics) | [crashlytics](https://firebase.google.com/docs/reference/android/com/google/firebase/crashlytics/ktx/package-summary#(com.google.firebase.ktx.Firebase).crashlytics()) Accessing this object for Kotlin apps has changed; see the [migration guide](https://firebase.google.com/docs/android/kotlin-migration). |

| ### Public methods  |
|---------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `static final void` | [FirebaseCrashlyticsKt](https://firebase.google.com/docs/reference/android/com/google/firebase/crashlytics/ktx/FirebaseCrashlyticsKt)`.`~~[setCustomKeys](https://firebase.google.com/docs/reference/android/com/google/firebase/crashlytics/ktx/FirebaseCrashlyticsKt#(com.google.firebase.crashlytics.FirebaseCrashlytics).setCustomKeys(kotlin.Function1))~~`(` ` @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[FirebaseCrashlytics](https://firebase.google.com/docs/reference/android/com/google/firebase/crashlytics/FirebaseCrashlytics)` receiver,` ` @`[ExtensionFunctionType](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-extension-function-type/index.html)` @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` Function1<@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[KeyValueBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/crashlytics/ktx/KeyValueBuilder)`, `[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)`> init` `)` **This method is deprecated.** Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration. |

## Public fields

### crashlytics

```
publicÂ finalÂ @NonNull FirebaseCrashlyticsÂ crashlytics
```

Accessing this object for Kotlin apps has changed; see the [migration guide](https://firebase.google.com/docs/android/kotlin-migration).

Returns the [FirebaseCrashlytics](https://firebase.google.com/docs/reference/android/com/google/firebase/crashlytics/FirebaseCrashlytics) instance of the default [FirebaseApp](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp).

**Important:** In July 2025, we stopped releasing KTX modules and removed the KTX libraries from the Firebase Android BoM (v34.0.0). **If you use KTX APIs from the KTX modules, we recommend that you migrate your app to use KTX APIs from the main modules instead** . For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)  

## Public methods

### FirebaseCrashlyticsKt.setCustomKeys

```
publicÂ staticÂ finalÂ voidÂ FirebaseCrashlyticsKt.[setCustomKeys](https://firebase.google.com/docs/reference/android/com/google/firebase/crashlytics/ktx/FirebaseCrashlyticsKt#(com.google.firebase.crashlytics.FirebaseCrashlytics).setCustomKeys(kotlin.Function1))(
Â Â Â Â @NonNull FirebaseCrashlyticsÂ receiver,
Â Â Â Â @ExtensionFunctionType @NonNull Function1<@NonNull KeyValueBuilder,Â Unit>Â init
)
```
| **This method is deprecated.**   
| Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration.

Associates all key-value parameters with the reports

**Important:** In July 2025, we stopped releasing KTX modules and removed the KTX libraries from the Firebase Android BoM (v34.0.0). **If you use KTX APIs from the KTX modules, we recommend that you migrate your app to use KTX APIs from the main modules instead** . For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)