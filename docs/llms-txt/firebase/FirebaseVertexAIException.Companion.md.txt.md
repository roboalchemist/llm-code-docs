# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FirebaseVertexAIException.Companion.md.txt

# FirebaseVertexAIException.Companion

# FirebaseVertexAIException.Companion


```
public static class FirebaseVertexAIException.Companion
```

<br />

*** ** * ** ***

## Summary

| ### Public methods |
|---|---|
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FirebaseVertexAIException` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FirebaseVertexAIException.Companion#from(kotlin.Throwable)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Throwable.html cause)` Converts a `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html` to a `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FirebaseVertexAIException`. |

## Public methods

### from

```
public static final @NonNull FirebaseVertexAIException from(@NonNull Throwable cause)
```

Converts a `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html` to a `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FirebaseVertexAIException`.

Will populate default messages as expected, and propagate the provided `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FirebaseVertexAIException.Companion#from(kotlin.Throwable)` through the resulting exception.