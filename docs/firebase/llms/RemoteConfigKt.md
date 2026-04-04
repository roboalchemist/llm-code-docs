# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/ktx/RemoteConfigKt.md.txt

# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/RemoteConfigKt.md.txt

# RemoteConfigKt

# RemoteConfigKt


```
public final class RemoteConfigKt
```

<br />

*** ** * ** ***

## Summary

|                                                                                                                                                                                                                ### Public fields                                                                                                                                                                                                                 |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[Flow](https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html)`<@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[ConfigUpdate](https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/ConfigUpdate)`>` | [configUpdates](https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/package-summary#(com.google.firebase.remoteconfig.FirebaseRemoteConfig).configUpdates()) Starts listening for config updates from the Remote Config backend and emits [ConfigUpdate](https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/ConfigUpdate)s via a [Flow](https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html). |
| `final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[FirebaseRemoteConfig](https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfig)                                                                                                                                                                                                           | [remoteConfig](https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/package-summary#(com.google.firebase.Firebase).remoteConfig()) Returns the [FirebaseRemoteConfig](https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfig) instance of the default [FirebaseApp](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp).                                                                                 |

|                                                                                                                      ### Public methods                                                                                                                       |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `static final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[CustomSignals](https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/CustomSignals)                               | [customSignals](https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/RemoteConfigKt#customSignals(kotlin.Function1))`(` ` @`[ExtensionFunctionType](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-extension-function-type/index.html)` @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` Function1<@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[CustomSignals.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/CustomSignals.Builder)`, `[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)`> builder` `)`                                                                                                                                                                                                                                                                                               |
| `static final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[FirebaseRemoteConfigValue](https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfigValue)       | [RemoteConfigKt](https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/RemoteConfigKt)`.`[get](https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/RemoteConfigKt#(com.google.firebase.remoteconfig.FirebaseRemoteConfig).get(kotlin.String))`(` ` @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[FirebaseRemoteConfig](https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfig)` receiver,` ` @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[String](https://developer.android.com/reference/kotlin/java/lang/String.html)` key` `)` See FirebaseRemoteConfig#getValue                                                                                                                                                                                                                            |
| `static final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[FirebaseRemoteConfig](https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfig)                 | [RemoteConfigKt](https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/RemoteConfigKt)`.`[remoteConfig](https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/RemoteConfigKt#(com.google.firebase.Firebase).remoteConfig(com.google.firebase.FirebaseApp))`(` ` @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[Firebase](https://firebase.google.com/docs/reference/android/com/google/firebase/Firebase)` receiver,` ` @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[FirebaseApp](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp)` app` `)` Returns the [FirebaseRemoteConfig](https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfig) instance of a given [FirebaseApp](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp). |
| `static final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[FirebaseRemoteConfigSettings](https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfigSettings) | [remoteConfigSettings](https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/RemoteConfigKt#remoteConfigSettings(kotlin.Function1))`(` ` @`[ExtensionFunctionType](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-extension-function-type/index.html)` @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` Function1<@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[FirebaseRemoteConfigSettings.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfigSettings.Builder)`, `[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)`> init` `)`                                                                                                                                                                                                                                                      |

## Public fields

### configUpdates

```
publicÂ finalÂ @NonNull Flow<@NonNull ConfigUpdate>Â configUpdates
```

Starts listening for config updates from the Remote Config backend and emits [ConfigUpdate](https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/ConfigUpdate)s via a [Flow](https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html). See [FirebaseRemoteConfig.addOnConfigUpdateListener](https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfig#addOnConfigUpdateListener(com.google.firebase.remoteconfig.ConfigUpdateListener)) for more information.

- When the returned flow starts being collected, an [ConfigUpdateListener](https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/ConfigUpdateListener) will be attached.

- When the flow completes, the listener will be removed. If there are no attached listeners, the connection to the Remote Config backend will be closed.

### remoteConfig

```
publicÂ finalÂ @NonNull FirebaseRemoteConfigÂ remoteConfig
```

Returns the [FirebaseRemoteConfig](https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfig) instance of the default [FirebaseApp](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp).  

## Public methods

### customSignals

```
publicÂ staticÂ finalÂ @NonNull CustomSignalsÂ customSignals(
Â Â Â Â @ExtensionFunctionType @NonNull Function1<@NonNull CustomSignals.Builder,Â Unit>Â builder
)
```  

### RemoteConfigKt.get

```
publicÂ staticÂ finalÂ @NonNull FirebaseRemoteConfigValueÂ RemoteConfigKt.get(
Â Â Â Â @NonNull FirebaseRemoteConfigÂ receiver,
Â Â Â Â @NonNull StringÂ key
)
```

See FirebaseRemoteConfig#getValue  

### RemoteConfigKt.remoteConfig

```
publicÂ staticÂ finalÂ @NonNull FirebaseRemoteConfigÂ RemoteConfigKt.remoteConfig(
Â Â Â Â @NonNull FirebaseÂ receiver,
Â Â Â Â @NonNull FirebaseAppÂ app
)
```

Returns the [FirebaseRemoteConfig](https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfig) instance of a given [FirebaseApp](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp).  

### remoteConfigSettings

```
publicÂ staticÂ finalÂ @NonNull FirebaseRemoteConfigSettingsÂ remoteConfigSettings(
Â Â Â Â @ExtensionFunctionType @NonNull Function1<@NonNull FirebaseRemoteConfigSettings.Builder,Â Unit>Â init
)
```