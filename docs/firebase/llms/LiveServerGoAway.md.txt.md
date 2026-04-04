# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveServerGoAway.md.txt

# LiveServerGoAway

# LiveServerGoAway


```
@PublicPreviewAPI
public final class LiveServerGoAway implements LiveServerMessage
```

<br />

*** ** * ** ***

Notification that the server is initiating a disconnect of the session.

This message is sent by the server when it needs to close the connection, typically due to session timeout, resource constraints, or other server-side reasons.

When this message is received, the client should gracefully close the `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveSession` by calling `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveSession#close()`.

## Summary

| ### Public fields |
|---|---|
| `final https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.time/-duration/index.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveServerGoAway#timeLeft()` The time remaining before the connection terminates. |

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveServerGoAway#LiveServerGoAway(kotlin.time.Duration)(https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.time/-duration/index.html timeLeft)` |

## Public fields

### timeLeft

```
public final Duration timeLeft
```

The time remaining before the connection terminates.

## Public constructors

### LiveServerGoAway

```
public LiveServerGoAway(Duration timeLeft)
```