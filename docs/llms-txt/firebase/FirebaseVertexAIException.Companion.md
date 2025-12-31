# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FirebaseVertexAIException.Companion.md.txt

# FirebaseVertexAIException.Companion

# FirebaseVertexAIException.Companion


```
public static class FirebaseVertexAIException.Companion
```

<br />

*** ** * ** ***

## Summary

|                                                                                                                    ### Public methods                                                                                                                    |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `static final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[FirebaseVertexAIException](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FirebaseVertexAIException) | [from](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FirebaseVertexAIException.Companion#from(kotlin.Throwable))`(@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[Throwable](https://developer.android.com/reference/kotlin/java/lang/Throwable.html)` cause)` Converts a [Throwable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html) to a [FirebaseVertexAIException](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FirebaseVertexAIException). |

## Public methods

### from

```
publicÂ staticÂ finalÂ @NonNull FirebaseVertexAIExceptionÂ from(@NonNull ThrowableÂ cause)
```

Converts a [Throwable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html) to a [FirebaseVertexAIException](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FirebaseVertexAIException).

Will populate default messages as expected, and propagate the provided [cause](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FirebaseVertexAIException.Companion#from(kotlin.Throwable)) through the resulting exception.