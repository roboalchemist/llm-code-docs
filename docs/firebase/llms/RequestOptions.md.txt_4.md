# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/RequestOptions.md.txt

# RequestOptions

# RequestOptions


```
class RequestOptions
```

<br />

*** ** * ** ***

> [!CAUTION]
> **This class is deprecated.**   
> The Vertex AI in Firebase SDK (firebase-vertexai) has been replaced with the FirebaseAI SDK (firebase-ai) to accommodate the evolving set of supported features and services. For migration details, see the migration guide: https://firebase.google.com/docs/vertex-ai/migrate-to-latest-sdk

Configurable options unique to how requests to the backend are performed.

## Summary

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/RequestOptions#RequestOptions(kotlin.Long)(timeoutInMillis: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html)` Constructor for RequestOptions. |

## Public constructors

### RequestOptions

```
RequestOptions(timeoutInMillis: Long = 180.seconds.inWholeMilliseconds)
```

Constructor for RequestOptions.

| Parameters |
|---|---|
| `timeoutInMillis: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html = 180.seconds.inWholeMilliseconds` | the maximum amount of time, in milliseconds, for a request to take, from the first request to first response. |