# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerateObjectResponse.md.txt

# GenerateObjectResponse

# GenerateObjectResponse


```
public final class GenerateObjectResponse<T extends Object>
```

<br />

*** ** * ** ***

A `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerateContentResponse` augmented with class information.

Use `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerateObjectResponse#getObject(kotlin.Int)` to parse the response and extract the strongly typed object.

## Summary

| ### Public fields |
|---|---|
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerateContentResponse` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerateObjectResponse#response()` |

| ### Public methods |
|---|---|
| `final T` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerateObjectResponse#getObject(kotlin.Int)(int candidateIndex)` Deserialize a candidate (default first) and convert it into the type associated with this response. |

## Public fields

### response

```
public final @NonNull GenerateContentResponse response
```

## Public methods

### getObject

```
public final T getObject(int candidateIndex)
```

Deserialize a candidate (default first) and convert it into the type associated with this response.

| Parameters |
|---|---|
| `int candidateIndex` | which candidate to deserialize |

| Throws |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-runtime-exception/index.html kotlin.RuntimeException` | if class is not @Serializable |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/SerializationException com.google.firebase.ai.type.SerializationException` | if an error occurs during deserialization |