# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/installations/InstallationsKt.md.txt

# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/installations/ktx/InstallationsKt.md.txt

# InstallationsKt

# InstallationsKt


```
public final class InstallationsKt
```

<br />

*** ** * ** ***

## Summary

|                                                                                                             ### Public fields                                                                                                             |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[FirebaseInstallations](https://firebase.google.com/docs/reference/android/com/google/firebase/installations/FirebaseInstallations) | [installations](https://firebase.google.com/docs/reference/android/com/google/firebase/installations/ktx/package-summary#(com.google.firebase.ktx.Firebase).installations()) Accessing this object for Kotlin apps has changed; see the [migration guide](https://firebase.google.com/docs/android/kotlin-migration). |

|                                                                                                                ### Public methods                                                                                                                |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `static final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[FirebaseInstallations](https://firebase.google.com/docs/reference/android/com/google/firebase/installations/FirebaseInstallations) | [InstallationsKt](https://firebase.google.com/docs/reference/android/com/google/firebase/installations/ktx/InstallationsKt)`.`[installations](https://firebase.google.com/docs/reference/android/com/google/firebase/installations/ktx/InstallationsKt#(com.google.firebase.ktx.Firebase).installations(com.google.firebase.FirebaseApp))`(` ` @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[Firebase](https://firebase.google.com/docs/reference/android/com/google/firebase/ktx/Firebase)` receiver,` ` @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[FirebaseApp](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp)` app` `)` Accessing this object for Kotlin apps has changed; see the [migration guide](https://firebase.google.com/docs/android/kotlin-migration). |

## Public fields

### installations

```
publicÂ finalÂ @NonNull FirebaseInstallationsÂ installations
```

Accessing this object for Kotlin apps has changed; see the [migration guide](https://firebase.google.com/docs/android/kotlin-migration).

Returns the [FirebaseInstallations](https://firebase.google.com/docs/reference/android/com/google/firebase/installations/FirebaseInstallations) instance of the default [FirebaseApp](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp).

**Important:** In July 2025, we stopped releasing KTX modules and removed the KTX libraries from the Firebase Android BoM (v34.0.0). **If you use KTX APIs from the KTX modules, we recommend that you migrate your app to use KTX APIs from the main modules instead** . For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)  

## Public methods

### InstallationsKt.installations

```
publicÂ staticÂ finalÂ @NonNull FirebaseInstallationsÂ InstallationsKt.installations(
Â Â Â Â @NonNull FirebaseÂ receiver,
Â Â Â Â @NonNull FirebaseAppÂ app
)
```

Accessing this object for Kotlin apps has changed; see the [migration guide](https://firebase.google.com/docs/android/kotlin-migration).

Returns the [FirebaseInstallations](https://firebase.google.com/docs/reference/android/com/google/firebase/installations/FirebaseInstallations) instance of a given [FirebaseApp](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp).

**Important:** In July 2025, we stopped releasing KTX modules and removed the KTX libraries from the Firebase Android BoM (v34.0.0). **If you use KTX APIs from the KTX modules, we recommend that you migrate your app to use KTX APIs from the main modules instead** . For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)