# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/MessagingKt.md.txt

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
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/FirebaseMessaging` | `https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/package-summary#(com.google.firebase.Firebase).messaging()` Returns the `https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/FirebaseMessaging` instance of the default `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp`. |

| ### Public methods |
|---|---|
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/RemoteMessage` | `https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/MessagingKt#remoteMessage(kotlin.String,kotlin.Function1)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html to, @https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-extension-function-type/index.html @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html Function1<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/RemoteMessage.Builder, https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html> init )` Returns a `https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/RemoteMessage` instance initialized using the `https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/package-summary#remoteMessage(kotlin.String,kotlin.Function1)` function. |

## Public fields

### messaging

```
public final @NonNull FirebaseMessaging messaging
```

Returns the `https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/FirebaseMessaging` instance of the default `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp`.

## Public methods

### remoteMessage

```
public static final @NonNull RemoteMessage remoteMessage(
    @NonNull String to,
    @ExtensionFunctionType @NonNull Function1<@NonNull RemoteMessage.Builder, Unit> init
)
```

Returns a `https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/RemoteMessage` instance initialized using the `https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/package-summary#remoteMessage(kotlin.String,kotlin.Function1)` function.