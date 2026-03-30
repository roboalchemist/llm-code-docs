# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/RemoteConfigKt.md.txt

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
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/ConfigUpdate>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/package-summary#(com.google.firebase.remoteconfig.FirebaseRemoteConfig).configUpdates()` Starts listening for config updates from the Remote Config backend and emits `https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/ConfigUpdate`s via a `https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html`. |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfig` | `https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/package-summary#(com.google.firebase.Firebase).remoteConfig()` Returns the `https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfig` instance of the default `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp`. |

| ### Public methods |
|---|---|
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/CustomSignals` | `https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/RemoteConfigKt#customSignals(kotlin.Function1)( @https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-extension-function-type/index.html @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html Function1<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/CustomSignals.Builder, https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html> builder )` |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfigValue` | `https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/RemoteConfigKt.https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/RemoteConfigKt#(com.google.firebase.remoteconfig.FirebaseRemoteConfig).get(kotlin.String)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfig receiver, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html key )` See FirebaseRemoteConfig#getValue |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfig` | `https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/RemoteConfigKt.https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/RemoteConfigKt#(com.google.firebase.Firebase).remoteConfig(com.google.firebase.FirebaseApp)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/Firebase receiver, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp app )` Returns the `https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfig` instance of a given `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp`. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfigSettings` | `https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/RemoteConfigKt#remoteConfigSettings(kotlin.Function1)( @https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-extension-function-type/index.html @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html Function1<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfigSettings.Builder, https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html> init )` |

## Public fields

### configUpdates

```
public final @NonNull Flow<@NonNull ConfigUpdate> configUpdates
```

Starts listening for config updates from the Remote Config backend and emits `https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/ConfigUpdate`s via a `https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html`. See `https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfig#addOnConfigUpdateListener(com.google.firebase.remoteconfig.ConfigUpdateListener)` for more information.

- When the returned flow starts being collected, an `https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/ConfigUpdateListener` will be attached.

- When the flow completes, the listener will be removed. If there are no attached listeners, the connection to the Remote Config backend will be closed.

### remoteConfig

```
public final @NonNull FirebaseRemoteConfig remoteConfig
```

Returns the `https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfig` instance of the default `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp`.

## Public methods

### customSignals

```
public static final @NonNull CustomSignals customSignals(
    @ExtensionFunctionType @NonNull Function1<@NonNull CustomSignals.Builder, Unit> builder
)
```

### RemoteConfigKt.get

```
public static final @NonNull FirebaseRemoteConfigValue RemoteConfigKt.get(
    @NonNull FirebaseRemoteConfig receiver,
    @NonNull String key
)
```

See FirebaseRemoteConfig#getValue

### RemoteConfigKt.remoteConfig

```
public static final @NonNull FirebaseRemoteConfig RemoteConfigKt.remoteConfig(
    @NonNull Firebase receiver,
    @NonNull FirebaseApp app
)
```

Returns the `https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfig` instance of a given `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp`.

### remoteConfigSettings

```
public static final @NonNull FirebaseRemoteConfigSettings remoteConfigSettings(
    @ExtensionFunctionType @NonNull Function1<@NonNull FirebaseRemoteConfigSettings.Builder, Unit> init
)
```