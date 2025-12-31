# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveContentResponse.md.txt

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

|                                                                                                                                                                         ### Nested types                                                                                                                                                                          |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `value public final class `[LiveContentResponse.Status](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveContentResponse.Status) Represents the status of a [LiveContentResponse](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveContentResponse), within a single interaction. |
| `public static class `[LiveContentResponse.Status.Companion](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveContentResponse.Status.Companion)                                                                                                                                                                           |

|                                                                                                                                                ### Public fields                                                                                                                                                |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `final `[Content](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Content)                                                                                                                                                                                                 | [data](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveContentResponse#data()) The main content data of the response.                                                                                                                                                  |
| `final `[List](https://developer.android.com/reference/kotlin/java/util/List.html)`<@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[FunctionCallPart](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FunctionCallPart)`>` | [functionCalls](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveContentResponse#functionCalls()) A list of [FunctionCallPart](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FunctionCallPart) included in the response, if any. |
| `final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[LiveContentResponse.Status](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveContentResponse.Status)                                                             | [status](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveContentResponse#status()) The status of the live content response.                                                                                                                                            |
| `final `[String](https://developer.android.com/reference/kotlin/java/lang/String.html)                                                                                                                                                                                                                          | [text](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveContentResponse#text()) Convenience field representing all the text parts in the response as a single string, if they exists.                                                                                   |

## Public fields

### data

```
publicÂ finalÂ ContentÂ data
```

The main content data of the response. This can be `null` if there is no content.  

### functionCalls

```
publicÂ finalÂ List<@NonNull FunctionCallPart>Â functionCalls
```

A list of [FunctionCallPart](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FunctionCallPart) included in the response, if any.

This list can be null or empty if no function calls are present.  

### status

```
publicÂ finalÂ @NonNull LiveContentResponse.StatusÂ status
```

The status of the live content response. Indicates whether the response is normal, was interrupted, or signifies the completion of a turn.  

### text

```
publicÂ finalÂ StringÂ text
```

Convenience field representing all the text parts in the response as a single string, if they exists.