# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/ktx/MessagingKt.md.txt

# MessagingKt

# MessagingKt


```
public final class MessagingKt
```

<br />

*** ** * ** ***

## Summary

| ### Public fields |
|---|---|
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/FirebaseMessaging` | `https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/ktx/package-summary#(com.google.firebase.ktx.Firebase).messaging()` Accessing this object for Kotlin apps has changed; see the [migration guide](https://firebase.google.com/docs/android/kotlin-migration). |

| ### Public methods |
|---|---|
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/RemoteMessage` | `[remoteMessage](https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/ktx/MessagingKt#remoteMessage(kotlin.String,kotlin.Function1))( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html to, @https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-extension-function-type/index.html @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html Function1<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/RemoteMessage.Builder, https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html> init )` **This method is deprecated.** Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration. |

## Public fields

### messaging

```
public final @NonNull FirebaseMessaging messaging
```

Accessing this object for Kotlin apps has changed; see the [migration guide](https://firebase.google.com/docs/android/kotlin-migration).

Returns the `https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/FirebaseMessaging` instance of the default `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp`.

**Important:** In July 2025, we stopped releasing KTX modules and removed the KTX libraries from the Firebase Android BoM (v34.0.0). **If you use KTX APIs from the KTX modules, we recommend that you migrate your app to use KTX APIs from the main modules instead** . For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)

## Public methods

### remoteMessage

```
public static final @NonNull RemoteMessage [remoteMessage](https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/ktx/MessagingKt#remoteMessage(kotlin.String,kotlin.Function1))(
    @NonNull String to,
    @ExtensionFunctionType @NonNull Function1<@NonNull RemoteMessage.Builder, Unit> init
)
```

> [!CAUTION]
> **This method is deprecated.**   
> Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration.

Returns a `https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/RemoteMessage` instance initialized using the `https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/ktx/package-summary#remoteMessage(kotlin.String,kotlin.Function1)` function.

**Important:** In July 2025, we stopped releasing KTX modules and removed the KTX libraries from the Firebase Android BoM (v34.0.0). **If you use KTX APIs from the KTX modules, we recommend that you migrate your app to use KTX APIs from the main modules instead** . For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)