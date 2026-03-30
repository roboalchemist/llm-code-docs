# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/ktx/FirebaseAppCheckKt.md.txt

# FirebaseAppCheckKt

# FirebaseAppCheckKt


```
public final class FirebaseAppCheckKt
```

<br />

*** ** * ** ***

## Summary

| ### Public fields |
|---|---|
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/FirebaseAppCheck` | `https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/ktx/package-summary#(com.google.firebase.ktx.Firebase).appCheck()` Accessing this object for Kotlin apps has changed; see the [migration guide](https://firebase.google.com/docs/android/kotlin-migration). |

| ### Public methods |
|---|---|
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/FirebaseAppCheck` | `https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/ktx/FirebaseAppCheckKt.https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/ktx/FirebaseAppCheckKt#(com.google.firebase.ktx.Firebase).appCheck(com.google.firebase.FirebaseApp)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ktx/Firebase receiver, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp app )` Accessing this object for Kotlin apps has changed; see the [migration guide](https://firebase.google.com/docs/android/kotlin-migration). |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/ktx/FirebaseAppCheckKt.[component1](https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/ktx/FirebaseAppCheckKt#(com.google.firebase.appcheck.AppCheckToken).component1())(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/AppCheckToken receiver)` **This method is deprecated.** Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration. |
| `static final long` | `https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/ktx/FirebaseAppCheckKt.[component2](https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/ktx/FirebaseAppCheckKt#(com.google.firebase.appcheck.AppCheckToken).component2())(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/AppCheckToken receiver)` **This method is deprecated.** Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration. |

## Public fields

### appCheck

```
public final @NonNull FirebaseAppCheck appCheck
```

Accessing this object for Kotlin apps has changed; see the [migration guide](https://firebase.google.com/docs/android/kotlin-migration).

Returns the `https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/FirebaseAppCheck` instance of the default `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp`.

**Important:** In July 2025, we stopped releasing KTX modules and removed the KTX libraries from the Firebase Android BoM (v34.0.0). **If you use KTX APIs from the KTX modules, we recommend that you migrate your app to use KTX APIs from the main modules instead** . For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)

## Public methods

### FirebaseAppCheckKt.appCheck

```
public static final @NonNull FirebaseAppCheck FirebaseAppCheckKt.appCheck(
    @NonNull Firebase receiver,
    @NonNull FirebaseApp app
)
```

Accessing this object for Kotlin apps has changed; see the [migration guide](https://firebase.google.com/docs/android/kotlin-migration).

Returns the `https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/FirebaseAppCheck` instance of a given `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp`.

**Important:** In July 2025, we stopped releasing KTX modules and removed the KTX libraries from the Firebase Android BoM (v34.0.0). **If you use KTX APIs from the KTX modules, we recommend that you migrate your app to use KTX APIs from the main modules instead** . For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)

### FirebaseAppCheckKt.component1

```
public static final @NonNull String FirebaseAppCheckKt.[component1](https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/ktx/FirebaseAppCheckKt#(com.google.firebase.appcheck.AppCheckToken).component1())(@NonNull AppCheckToken receiver)
```

> [!CAUTION]
> **This method is deprecated.**   
> Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration.

Destructuring declaration for `https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/AppCheckToken` to provide token.

**Important:** In July 2025, we stopped releasing KTX modules and removed the KTX libraries from the Firebase Android BoM (v34.0.0). **If you use KTX APIs from the KTX modules, we recommend that you migrate your app to use KTX APIs from the main modules instead** . For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html` | the token of the `https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/AppCheckToken` |

### FirebaseAppCheckKt.component2

```
public static final long FirebaseAppCheckKt.[component2](https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/ktx/FirebaseAppCheckKt#(com.google.firebase.appcheck.AppCheckToken).component2())(@NonNull AppCheckToken receiver)
```

> [!CAUTION]
> **This method is deprecated.**   
> Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration.

Destructuring declaration for `https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/AppCheckToken` to provide expireTimeMillis.

**Important:** In July 2025, we stopped releasing KTX modules and removed the KTX libraries from the Firebase Android BoM (v34.0.0). **If you use KTX APIs from the KTX modules, we recommend that you migrate your app to use KTX APIs from the main modules instead** . For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)

| Returns |
|---|---|
| `long` | the expireTimeMillis of the `https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/AppCheckToken` |