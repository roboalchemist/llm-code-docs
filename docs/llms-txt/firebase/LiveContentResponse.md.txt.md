# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveContentResponse.md.txt

# LiveContentResponse

# LiveContentResponse


```
@PublicPreviewAPI
public final class LiveContentResponse
```

<br />

*** ** * ** ***

Represents the response from the model for live content updates.

This class encapsulates the content data, the status of the response, and any function calls included in the response.

## Summary

| ### Nested types |
|---|
| `value public final class https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveContentResponse.Status` Represents the status of a `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveContentResponse`, within a single interaction. |
| `public static class https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveContentResponse.Status.Companion` |

| ### Public fields |
|---|---|
| `final https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Content` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveContentResponse#data()` The main content data of the response. |
| `final https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FunctionCallPart>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveContentResponse#functionCalls()` A list of `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FunctionCallPart` included in the response, if any. |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveContentResponse.Status` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveContentResponse#status()` The status of the live content response. |
| `final https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveContentResponse#text()` Convenience field representing all the text parts in the response as a single string, if they exists. |

## Public fields

### data

```
public final Content data
```

The main content data of the response. This can be `null` if there is no content.

### functionCalls

```
public final List<@NonNull FunctionCallPart> functionCalls
```

A list of `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FunctionCallPart` included in the response, if any.

This list can be null or empty if no function calls are present.

### status

```
public final @NonNull LiveContentResponse.Status status
```

The status of the live content response. Indicates whether the response is normal, was interrupted, or signifies the completion of a turn.

### text

```
public final String text
```

Convenience field representing all the text parts in the response as a single string, if they exists.