# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/StreamResponse.Result.md.txt

# StreamResponse.Result

# StreamResponse.Result


```
class StreamResponse.Result : StreamResponse
```

<br />

|---|---|---|
| [kotlin.Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html) |||
| ↳ | [com.google.firebase.functions.StreamResponse](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/StreamResponse) ||
|   | ↳ | [com.google.firebase.functions.StreamResponse.Result](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/StreamResponse.Result) |

*** ** * ** ***

The final result of the computation, marking the end of the stream.

Unlike `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/StreamResponse.Message`, which represents intermediate data chunks, `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/StreamResponse.Result` contains the complete computation output. If clients only care about the final result, they can process this type alone and ignore intermediate messages.

Example SSE format:

```kotlin
data: { "result": { "text": "foo bar" } }
```

## Summary

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/StreamResponse.Result#Result(com.google.firebase.functions.HttpsCallableResult)(result: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/HttpsCallableResult)` |

| ### Public properties |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/HttpsCallableResult` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/StreamResponse.Result#result()` the final computed result received from the server. |

## Public constructors

### Result

```
Result(result: HttpsCallableResult)
```

## Public properties

### result

```
val result: HttpsCallableResult
```

the final computed result received from the server.