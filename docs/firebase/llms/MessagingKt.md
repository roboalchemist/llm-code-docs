# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/MessagingKt.md.txt

# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/ktx/MessagingKt.md.txt

# MessagingKt

# MessagingKt


```
public final class MessagingKt
```

<br />

*** ** * ** ***

## Summary

|                                                                                                       ### Public fields                                                                                                       |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[FirebaseMessaging](https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/FirebaseMessaging) | [messaging](https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/ktx/package-summary#(com.google.firebase.ktx.Firebase).messaging()) Accessing this object for Kotlin apps has changed; see the [migration guide](https://firebase.google.com/docs/android/kotlin-migration). |

|                                                                                                      ### Public methods                                                                                                      |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `static final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[RemoteMessage](https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/RemoteMessage) | ~~[remoteMessage](https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/ktx/MessagingKt#remoteMessage(kotlin.String,kotlin.Function1))~~`(` ` @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[String](https://developer.android.com/reference/kotlin/java/lang/String.html)` to,` ` @`[ExtensionFunctionType](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-extension-function-type/index.html)` @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` Function1<@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[RemoteMessage.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/RemoteMessage.Builder)`, `[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)`> init` `)` **This method is deprecated.** Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration. |

## Public fields

### messaging

```
publicÂ finalÂ @NonNull FirebaseMessagingÂ messaging
```

Accessing this object for Kotlin apps has changed; see the [migration guide](https://firebase.google.com/docs/android/kotlin-migration).

Returns the [FirebaseMessaging](https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/FirebaseMessaging) instance of the default [FirebaseApp](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp).

**Important:** In July 2025, we stopped releasing KTX modules and removed the KTX libraries from the Firebase Android BoM (v34.0.0). **If you use KTX APIs from the KTX modules, we recommend that you migrate your app to use KTX APIs from the main modules instead** . For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)  

## Public methods

### remoteMessage

```
publicÂ staticÂ finalÂ @NonNull RemoteMessageÂ [remoteMessage](https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/ktx/MessagingKt#remoteMessage(kotlin.String,kotlin.Function1))(
Â Â Â Â @NonNull StringÂ to,
Â Â Â Â @ExtensionFunctionType @NonNull Function1<@NonNull RemoteMessage.Builder,Â Unit>Â init
)
```
| **This method is deprecated.**   
| Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration.

Returns a [RemoteMessage](https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/RemoteMessage) instance initialized using the [init](https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/ktx/package-summary#remoteMessage(kotlin.String,kotlin.Function1)) function.

**Important:** In July 2025, we stopped releasing KTX modules and removed the KTX libraries from the Firebase Android BoM (v34.0.0). **If you use KTX APIs from the KTX modules, we recommend that you migrate your app to use KTX APIs from the main modules instead** . For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)