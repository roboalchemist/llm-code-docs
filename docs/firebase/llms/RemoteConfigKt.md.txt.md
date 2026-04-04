# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/ktx/RemoteConfigKt.md.txt

# RemoteConfigKt

# RemoteConfigKt


```
public final class RemoteConfigKt
```

<br />

*** ** * ** ***

## Summary

| ### Public fields |
|---|---|
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/ConfigUpdate>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/ktx/package-summary#(com.google.firebase.remoteconfig.FirebaseRemoteConfig).configUpdates()` **This field is deprecated.** Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration. |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfig` | `https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/ktx/package-summary#(com.google.firebase.ktx.Firebase).remoteConfig()` Accessing this object for Kotlin apps has changed; see the [migration guide](https://firebase.google.com/docs/android/kotlin-migration). |

| ### Public methods |
|---|---|
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfigValue` | `https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/ktx/RemoteConfigKt.[get](https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/ktx/RemoteConfigKt#(com.google.firebase.remoteconfig.FirebaseRemoteConfig).get(kotlin.String))( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfig receiver, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html key )` **This method is deprecated.** Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfig` | `https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/ktx/RemoteConfigKt.https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/ktx/RemoteConfigKt#(com.google.firebase.ktx.Firebase).remoteConfig(com.google.firebase.FirebaseApp)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ktx/Firebase receiver, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp app )` Accessing this object for Kotlin apps has changed; see the [migration guide](https://firebase.google.com/docs/android/kotlin-migration). |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfigSettings` | `https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/ktx/RemoteConfigKt#remoteConfigSettings(kotlin.Function1)( @https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-extension-function-type/index.html @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html Function1<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfigSettings.Builder, https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html> init )` |

## Public fields

### configUpdates

```
public final @NonNull Flow<@NonNull ConfigUpdate> configUpdates
```

> [!CAUTION]
> **This field is deprecated.**   
> Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration.

Starts listening for config updates from the Remote Config backend and emits `https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/ConfigUpdate`s via a `https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html`. See `https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfig#addOnConfigUpdateListener(com.google.firebase.remoteconfig.ConfigUpdateListener)` for more information.

- When the returned flow starts being collected, an `https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/ConfigUpdateListener` will be attached.

- When the flow completes, the listener will be removed. If there are no attached listeners, the connection to the Remote Config backend will be closed.

**Important:** In July 2025, we stopped releasing KTX modules and removed the KTX libraries from the Firebase Android BoM (v34.0.0). **If you use KTX APIs from the KTX modules, we recommend that you migrate your app to use KTX APIs from the main modules instead** . For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)

### remoteConfig

```
public final @NonNull FirebaseRemoteConfig remoteConfig
```

Accessing this object for Kotlin apps has changed; see the [migration guide](https://firebase.google.com/docs/android/kotlin-migration).

Returns the `https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfig` instance of the default `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp`.

**Important:** In July 2025, we stopped releasing KTX modules and removed the KTX libraries from the Firebase Android BoM (v34.0.0). **If you use KTX APIs from the KTX modules, we recommend that you migrate your app to use KTX APIs from the main modules instead** . For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)

## Public methods

### RemoteConfigKt.get

```
public static final @NonNull FirebaseRemoteConfigValue RemoteConfigKt.[get](https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/ktx/RemoteConfigKt#(com.google.firebase.remoteconfig.FirebaseRemoteConfig).get(kotlin.String))(
    @NonNull FirebaseRemoteConfig receiver,
    @NonNull String key
)
```

> [!CAUTION]
> **This method is deprecated.**   
> Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration.

See FirebaseRemoteConfig#getValue

**Important:** In July 2025, we stopped releasing KTX modules and removed the KTX libraries from the Firebase Android BoM (v34.0.0). **If you use KTX APIs from the KTX modules, we recommend that you migrate your app to use KTX APIs from the main modules instead** . For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)

### RemoteConfigKt.remoteConfig

```
public static final @NonNull FirebaseRemoteConfig RemoteConfigKt.remoteConfig(
    @NonNull Firebase receiver,
    @NonNull FirebaseApp app
)
```

Accessing this object for Kotlin apps has changed; see the [migration guide](https://firebase.google.com/docs/android/kotlin-migration).

Returns the `https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfig` instance of a given `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp`.

**Important:** In July 2025, we stopped releasing KTX modules and removed the KTX libraries from the Firebase Android BoM (v34.0.0). **If you use KTX APIs from the KTX modules, we recommend that you migrate your app to use KTX APIs from the main modules instead** . For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)

### remoteConfigSettings

```
public static final @NonNull FirebaseRemoteConfigSettings remoteConfigSettings(
    @ExtensionFunctionType @NonNull Function1<@NonNull FirebaseRemoteConfigSettings.Builder, Unit> init
)
```