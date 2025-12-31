# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveContentResponse.Status.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveContentResponse.Status.md.txt

# LiveContentResponse.Status

# LiveContentResponse.Status


```
value class LiveContentResponse.Status
```

<br />

*** ** * ** ***

Represents the status of a [LiveContentResponse](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveContentResponse), within a single interaction.

## Summary

|                                                       ### Public companion properties                                                        |
|----------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [LiveContentResponse.Status](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveContentResponse.Status) | [INTERRUPTED](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveContentResponse.Status.Companion#INTERRUPTED()) The server was interrupted while generating data.                   |
| [LiveContentResponse.Status](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveContentResponse.Status) | [NORMAL](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveContentResponse.Status.Companion#NORMAL()) The server is actively sending data for the current interaction.              |
| [LiveContentResponse.Status](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveContentResponse.Status) | [TURN_COMPLETE](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveContentResponse.Status.Companion#TURN_COMPLETE()) The model has finished sending data in the current interaction. |

## Public companion properties

### INTERRUPTED

```
valÂ INTERRUPTED:Â LiveContentResponse.Status
```

The server was interrupted while generating data.

An interruption occurs when the client sends a message while the server is [actively](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveContentResponse.Status.Companion#NORMAL()) sending data.  

### NORMAL

```
valÂ NORMAL:Â LiveContentResponse.Status
```

The server is actively sending data for the current interaction.  

### TURN_COMPLETE

```
valÂ TURN_COMPLETE:Â LiveContentResponse.Status
```

The model has finished sending data in the current interaction.

Can be set alongside content, signifying that the content is the last in the turn.