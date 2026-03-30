# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/RequestOptions.md.txt

# RequestOptions

# RequestOptions


```
class RequestOptions
```

<br />

*** ** * ** ***

Configurable options unique to how requests to the backend are performed.

## Summary

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/RequestOptions#RequestOptions(kotlin.Long,kotlin.Int)(timeoutInMillis: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html, autoFunctionCallingTurnLimit: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` Constructor for RequestOptions. |

## Public constructors

### RequestOptions

```
RequestOptions(
    timeoutInMillis: Long = 180.seconds.inWholeMilliseconds,
    autoFunctionCallingTurnLimit: Int = 10
)
```

Constructor for RequestOptions.

| Parameters |
|---|---|
| `timeoutInMillis: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html = 180.seconds.inWholeMilliseconds` | the maximum amount of time, in milliseconds, for a request to take, from the first request to first response. |