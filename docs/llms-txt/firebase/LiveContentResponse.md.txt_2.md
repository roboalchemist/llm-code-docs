# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveContentResponse.md.txt

# LiveContentResponse

# LiveContentResponse


```
@PublicPreviewAPI
class LiveContentResponse
```

<br />

*** ** * ** ***

Represents the response from the model for live content updates.

This class encapsulates the content data, the status of the response, and any function calls included in the response.

## Summary

| ### Nested types |
|---|
| `value class https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveContentResponse.Status` Represents the status of a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveContentResponse`, within a single interaction. |

| ### Public properties |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Content?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveContentResponse#data()` The main content data of the response. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/FunctionCallPart>?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveContentResponse#functionCalls()` A list of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/FunctionCallPart` included in the response, if any. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveContentResponse.Status` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveContentResponse#status()` The status of the live content response. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveContentResponse#text()` Convenience field representing all the text parts in the response as a single string, if they exists. |

## Public properties

### data

```
val data: Content?
```

The main content data of the response. This can be `null` if there is no content.

### functionCalls

```
val functionCalls: List<FunctionCallPart>?
```

A list of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/FunctionCallPart` included in the response, if any.

This list can be null or empty if no function calls are present.

### status

```
val status: LiveContentResponse.Status
```

The status of the live content response. Indicates whether the response is normal, was interrupted, or signifies the completion of a turn.

### text

```
val text: String?
```

Convenience field representing all the text parts in the response as a single string, if they exists.