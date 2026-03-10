# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/ktx/package-summary.md.txt

# com.google.firebase.remoteconfig.ktx

# com.google.firebase.remoteconfig.ktx

## Top-level functions summary

|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigSettings` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/ktx/package-summary#remoteConfigSettings(kotlin.Function1)(init: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigSettings.Builder.() -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |

## Extension functions summary

|---|---|
| `operator https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigValue` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig.[get](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/ktx/package-summary#(com.google.firebase.remoteconfig.FirebaseRemoteConfig).get(kotlin.String))(key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` **This function is deprecated.** Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ktx/Firebase.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/ktx/package-summary#(com.google.firebase.ktx.Firebase).remoteConfig(com.google.firebase.FirebaseApp)(app: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp)` Accessing this object for Kotlin apps has changed; see the [migration guide](https://firebase.google.com/docs/android/kotlin-migration). |

## Extension properties summary

|---|---|
| `https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/ConfigUpdate>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/ktx/package-summary#(com.google.firebase.remoteconfig.FirebaseRemoteConfig).configUpdates()` **This property is deprecated.** Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ktx/Firebase.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/ktx/package-summary#(com.google.firebase.ktx.Firebase).remoteConfig()` Accessing this object for Kotlin apps has changed; see the [migration guide](https://firebase.google.com/docs/android/kotlin-migration). |

## Top-level functions

### remoteConfigSettings

```
fun remoteConfigSettings(init: FirebaseRemoteConfigSettings.Builder.() -> Unit): FirebaseRemoteConfigSettings
```

## Extension functions

### get

```
operator fun FirebaseRemoteConfig.[get](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/ktx/package-summary#(com.google.firebase.remoteconfig.FirebaseRemoteConfig).get(kotlin.String))(key: String): FirebaseRemoteConfigValue
```

> [!CAUTION]
> **This function is deprecated.**   
> Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration.

See FirebaseRemoteConfig#getValue

**Important** In July 2025, we stopped releasing KTX modules and removed the KTX libraries from the Firebase Android BoM (v34.0.0). **If you use KTX APIs from the KTX modules, we recommend that you migrate your app to use KTX APIs from the main modules instead** . For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)

### remoteConfig

```
fun Firebase.remoteConfig(app: FirebaseApp): FirebaseRemoteConfig
```

Accessing this object for Kotlin apps has changed; see the [migration guide](https://firebase.google.com/docs/android/kotlin-migration).

Returns the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig` instance of a given `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp`.

**Important** In July 2025, we stopped releasing KTX modules and removed the KTX libraries from the Firebase Android BoM (v34.0.0). **If you use KTX APIs from the KTX modules, we recommend that you migrate your app to use KTX APIs from the main modules instead** . For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)

## Extension properties

### configUpdates

```
val FirebaseRemoteConfig.configUpdates: Flow<ConfigUpdate>
```

> [!CAUTION]
> **This property is deprecated.**   
> Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration.

Starts listening for config updates from the Remote Config backend and emits `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/ConfigUpdate`s via a `https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html`. See `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig#addOnConfigUpdateListener(com.google.firebase.remoteconfig.ConfigUpdateListener)` for more information.

- When the returned flow starts being collected, an `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/ConfigUpdateListener` will be attached.

- When the flow completes, the listener will be removed. If there are no attached listeners, the connection to the Remote Config backend will be closed.

**Important** In July 2025, we stopped releasing KTX modules and removed the KTX libraries from the Firebase Android BoM (v34.0.0). **If you use KTX APIs from the KTX modules, we recommend that you migrate your app to use KTX APIs from the main modules instead** . For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)

### remoteConfig

```
val Firebase.remoteConfig: FirebaseRemoteConfig
```

Accessing this object for Kotlin apps has changed; see the [migration guide](https://firebase.google.com/docs/android/kotlin-migration).

Returns the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig` instance of the default `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp`.

**Important** In July 2025, we stopped releasing KTX modules and removed the KTX libraries from the Firebase Android BoM (v34.0.0). **If you use KTX APIs from the KTX modules, we recommend that you migrate your app to use KTX APIs from the main modules instead** . For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)