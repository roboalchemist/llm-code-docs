# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/functions/StreamResponse.Result.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/StreamResponse.Result.md.txt

# StreamResponse.Result

# StreamResponse.Result


```
class StreamResponse.Result : StreamResponse
```

<br />

|---|---|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [kotlin.Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)                                                                                  |||
| â³ | [com.google.firebase.functions.StreamResponse](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/StreamResponse)                  ||
|   | â³ | [com.google.firebase.functions.StreamResponse.Result](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/StreamResponse.Result) |

*** ** * ** ***

The final result of the computation, marking the end of the stream.

Unlike [Message](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/StreamResponse.Message), which represents intermediate data chunks, [Result](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/StreamResponse.Result) contains the complete computation output. If clients only care about the final result, they can process this type alone and ignore intermediate messages.

Example SSE format:  

```kotlin
data: { "result": { "text": "foo bar" } }
```

## Summary

|                                                                                                                                              ### Public constructors                                                                                                                                              |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Result](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/StreamResponse.Result#Result(com.google.firebase.functions.HttpsCallableResult))`(result: `[HttpsCallableResult](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/HttpsCallableResult)`)` |

|                                                   ### Public properties                                                    |
|----------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [HttpsCallableResult](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/HttpsCallableResult) | [result](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/StreamResponse.Result#result()) the final computed result received from the server. |

## Public constructors

### Result

```
Result(result:Â HttpsCallableResult)
```  

## Public properties

### result

```
valÂ result:Â HttpsCallableResult
```

the final computed result received from the server.