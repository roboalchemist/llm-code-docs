# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveContentResponse.Status.Companion.md.txt

# LiveContentResponse.Status.Companion

# LiveContentResponse.Status.Companion


```
public static class LiveContentResponse.Status.Companion
```

<br />

*** ** * ** ***

## Summary

| ### Public fields |
|---|---|
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveContentResponse.Status` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveContentResponse.Status.Companion#INTERRUPTED()` The server was interrupted while generating data. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveContentResponse.Status` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveContentResponse.Status.Companion#NORMAL()` The server is actively sending data for the current interaction. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveContentResponse.Status` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveContentResponse.Status.Companion#TURN_COMPLETE()` The model has finished sending data in the current interaction. |

## Public fields

### INTERRUPTED

```
public static final @NonNull LiveContentResponse.Status INTERRUPTED
```

The server was interrupted while generating data.

An interruption occurs when the client sends a message while the server is `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveContentResponse.Status.Companion#NORMAL()` sending data.

### NORMAL

```
public static final @NonNull LiveContentResponse.Status NORMAL
```

The server is actively sending data for the current interaction.

### TURN_COMPLETE

```
public static final @NonNull LiveContentResponse.Status TURN_COMPLETE
```

The model has finished sending data in the current interaction.

Can be set alongside content, signifying that the content is the last in the turn.