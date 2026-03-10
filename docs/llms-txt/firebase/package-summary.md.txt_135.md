# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/ktx/package-summary.md.txt

# com.google.firebase.messaging.ktx

# com.google.firebase.messaging.ktx

## Top-level functions summary

|---|---|
| `inline https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/RemoteMessage` | `[remoteMessage](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/ktx/package-summary#remoteMessage(kotlin.String,kotlin.Function1))(to: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, crossinline init: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/RemoteMessage.Builder.() -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` **This function is deprecated.** Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration. |

## Extension properties summary

|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/FirebaseMessaging` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ktx/Firebase.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/ktx/package-summary#(com.google.firebase.ktx.Firebase).messaging()` Accessing this object for Kotlin apps has changed; see the [migration guide](https://firebase.google.com/docs/android/kotlin-migration). |

## Top-level functions

### remoteMessage

```
inline fun [remoteMessage](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/ktx/package-summary#remoteMessage(kotlin.String,kotlin.Function1))(to: String, crossinline init: RemoteMessage.Builder.() -> Unit): RemoteMessage
```

> [!CAUTION]
> **This function is deprecated.**   
> Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration.

Returns a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/RemoteMessage` instance initialized using the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/ktx/package-summary#remoteMessage(kotlin.String,kotlin.Function1)` function.

**Important** In July 2025, we stopped releasing KTX modules and removed the KTX libraries from the Firebase Android BoM (v34.0.0). **If you use KTX APIs from the KTX modules, we recommend that you migrate your app to use KTX APIs from the main modules instead** . For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)

## Extension properties

### messaging

```
val Firebase.messaging: FirebaseMessaging
```

Accessing this object for Kotlin apps has changed; see the [migration guide](https://firebase.google.com/docs/android/kotlin-migration).

Returns the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/FirebaseMessaging` instance of the default `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp`.

**Important** In July 2025, we stopped releasing KTX modules and removed the KTX libraries from the Firebase Android BoM (v34.0.0). **If you use KTX APIs from the KTX modules, we recommend that you migrate your app to use KTX APIs from the main modules instead** . For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)