# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ai/java/LiveModelFutures.md.txt

# LiveModelFutures

# LiveModelFutures


```
@PublicPreviewAPI
public abstract class LiveModelFutures
```

<br />

*** ** * ** ***

Wrapper class providing Java compatible methods for `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/LiveGenerativeModel`.

| See also |
|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/LiveGenerativeModel` |   |

## Summary

| ### Nested types |
|---|
| `public static class https://firebase.google.com/docs/reference/android/com/google/firebase/ai/java/LiveModelFutures.Companion` |

| ### Public methods |
|---|---|
| `abstract @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/common/util/concurrent/ListenableFuture<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/java/LiveSessionFutures>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/java/LiveModelFutures#connect()()` Start a `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/java/LiveSessionFutures` with the server for bidirectional streaming. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/java/LiveModelFutures` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/java/LiveModelFutures.Companion#from(com.google.firebase.ai.LiveGenerativeModel)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/LiveGenerativeModel model)` |

## Public methods

### connect

```
public abstract @NonNull ListenableFuture<@NonNull LiveSessionFutures> connect()
```

Start a `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/java/LiveSessionFutures` with the server for bidirectional streaming.

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/common/util/concurrent/ListenableFuture<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/java/LiveSessionFutures>` | A `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/java/LiveSessionFutures` that you can use to stream messages to and from the server. |

| Throws |
|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ServiceConnectionHandshakeFailedException com.google.firebase.ai.type.ServiceConnectionHandshakeFailedException` | If the client was not able to establish a connection with the server. |

### from

```
public static final @NonNull LiveModelFutures from(@NonNull LiveGenerativeModel model)
```

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/java/LiveModelFutures` | a `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/java/LiveModelFutures` created around the provided `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/LiveGenerativeModel` |