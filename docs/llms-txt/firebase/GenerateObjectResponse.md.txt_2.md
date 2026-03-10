# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerateObjectResponse.md.txt

# GenerateObjectResponse

# GenerateObjectResponse


```
class GenerateObjectResponse<T : Any>
```

<br />

*** ** * ** ***

A `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerateContentResponse` augmented with class information.

Use `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerateObjectResponse#getObject(kotlin.Int)` to parse the response and extract the strongly typed object.

## Summary

| ### Public functions |
|---|---|
| `T?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerateObjectResponse#getObject(kotlin.Int)(candidateIndex: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` Deserialize a candidate (default first) and convert it into the type associated with this response. |

| ### Public properties |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerateContentResponse` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerateObjectResponse#response()` |

## Public functions

### getObject

```
fun getObject(candidateIndex: Int = 0): T?
```

Deserialize a candidate (default first) and convert it into the type associated with this response.

| Parameters |
|---|---|
| `candidateIndex: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html = 0` | which candidate to deserialize |

| Throws |
|---|---|
| `kotlin.RuntimeException: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-runtime-exception/index.html` | if class is not @Serializable |
| `com.google.firebase.ai.type.SerializationException: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/SerializationException` | if an error occurs during deserialization |

## Public properties

### response

```
val response: GenerateContentResponse
```