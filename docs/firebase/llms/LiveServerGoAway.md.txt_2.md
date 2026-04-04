# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveServerGoAway.md.txt

# LiveServerGoAway

# LiveServerGoAway


```
@PublicPreviewAPI
class LiveServerGoAway : LiveServerMessage
```

<br />

*** ** * ** ***

Notification that the server is initiating a disconnect of the session.

This message is sent by the server when it needs to close the connection, typically due to session timeout, resource constraints, or other server-side reasons.

When this message is received, the client should gracefully close the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveSession` by calling `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveSession#close()`.

## Summary

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveServerGoAway#LiveServerGoAway(kotlin.time.Duration)(timeLeft: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.time/-duration/index.html?)` |

| ### Public properties |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.time/-duration/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveServerGoAway#timeLeft()` The time remaining before the connection terminates. |

## Public constructors

### LiveServerGoAway

```
LiveServerGoAway(timeLeft: Duration?)
```

## Public properties

### timeLeft

```
val timeLeft: Duration?
```

The time remaining before the connection terminates.