# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/functions/StreamResponse.Result.md.txt

# StreamResponse.Result

# StreamResponse.Result


```
public final class StreamResponse.Result extends StreamResponse
```

<br />

|---|---|---|
| [java.lang.Object](https://developer.android.com/reference/kotlin/java/lang/Object.html) |||
| ↳ | [com.google.firebase.functions.StreamResponse](https://firebase.google.com/docs/reference/android/com/google/firebase/functions/StreamResponse) ||
|   | ↳ | [com.google.firebase.functions.StreamResponse.Result](https://firebase.google.com/docs/reference/android/com/google/firebase/functions/StreamResponse.Result) |

*** ** * ** ***

The final result of the computation, marking the end of the stream.

Unlike `https://firebase.google.com/docs/reference/android/com/google/firebase/functions/StreamResponse.Message`, which represents intermediate data chunks, `https://firebase.google.com/docs/reference/android/com/google/firebase/functions/StreamResponse.Result` contains the complete computation output. If clients only care about the final result, they can process this type alone and ignore intermediate messages.

Example SSE format:

```
data: { "result": { "text": "foo bar" } }
```

## Summary

| ### Public fields |
|---|---|
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/functions/HttpsCallableResult` | `https://firebase.google.com/docs/reference/android/com/google/firebase/functions/StreamResponse.Result#result()` the final computed result received from the server. |

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/functions/StreamResponse.Result#Result(com.google.firebase.functions.HttpsCallableResult)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/functions/HttpsCallableResult result)` |

## Public fields

### result

```
public final @NonNull HttpsCallableResult result
```

the final computed result received from the server.

## Public constructors

### Result

```
public Result(@NonNull HttpsCallableResult result)
```