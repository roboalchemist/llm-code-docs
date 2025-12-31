# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveContentResponse.Status.Companion.md.txt

# LiveContentResponse.Status.Companion

# LiveContentResponse.Status.Companion


```
public static class LiveContentResponse.Status.Companion
```

<br />

*** ** * ** ***

## Summary

|                                                                                                                     ### Public fields                                                                                                                      |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `static final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[LiveContentResponse.Status](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveContentResponse.Status) | [INTERRUPTED](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveContentResponse.Status.Companion#INTERRUPTED()) The server was interrupted while generating data.                   |
| `static final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[LiveContentResponse.Status](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveContentResponse.Status) | [NORMAL](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveContentResponse.Status.Companion#NORMAL()) The server is actively sending data for the current interaction.              |
| `static final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[LiveContentResponse.Status](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveContentResponse.Status) | [TURN_COMPLETE](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveContentResponse.Status.Companion#TURN_COMPLETE()) The model has finished sending data in the current interaction. |

## Public fields

### INTERRUPTED

```
publicÂ staticÂ finalÂ @NonNull LiveContentResponse.StatusÂ INTERRUPTED
```

The server was interrupted while generating data.

An interruption occurs when the client sends a message while the server is [actively](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveContentResponse.Status.Companion#NORMAL()) sending data.  

### NORMAL

```
publicÂ staticÂ finalÂ @NonNull LiveContentResponse.StatusÂ NORMAL
```

The server is actively sending data for the current interaction.  

### TURN_COMPLETE

```
publicÂ staticÂ finalÂ @NonNull LiveContentResponse.StatusÂ TURN_COMPLETE
```

The model has finished sending data in the current interaction.

Can be set alongside content, signifying that the content is the last in the turn.