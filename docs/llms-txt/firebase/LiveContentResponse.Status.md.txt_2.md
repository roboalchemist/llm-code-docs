# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveContentResponse.Status.md.txt

# LiveContentResponse.Status

# LiveContentResponse.Status


```
value class LiveContentResponse.Status
```

<br />

*** ** * ** ***

Represents the status of a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveContentResponse`, within a single interaction.

## Summary

| ### Public companion properties |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveContentResponse.Status` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveContentResponse.Status.Companion#INTERRUPTED()` The server was interrupted while generating data. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveContentResponse.Status` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveContentResponse.Status.Companion#NORMAL()` The server is actively sending data for the current interaction. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveContentResponse.Status` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveContentResponse.Status.Companion#TURN_COMPLETE()` The model has finished sending data in the current interaction. |

## Public companion properties

### INTERRUPTED

```
val INTERRUPTED: LiveContentResponse.Status
```

The server was interrupted while generating data.

An interruption occurs when the client sends a message while the server is `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveContentResponse.Status.Companion#NORMAL()` sending data.

### NORMAL

```
val NORMAL: LiveContentResponse.Status
```

The server is actively sending data for the current interaction.

### TURN_COMPLETE

```
val TURN_COMPLETE: LiveContentResponse.Status
```

The model has finished sending data in the current interaction.

Can be set alongside content, signifying that the content is the last in the turn.