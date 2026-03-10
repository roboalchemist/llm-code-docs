# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/FunctionResponsePart.md.txt

# FunctionResponsePart

# FunctionResponsePart


```
class FunctionResponsePart : Part
```

<br />

*** ** * ** ***

> [!CAUTION]
> **This class is deprecated.**   
> The Vertex AI in Firebase SDK (firebase-vertexai) has been replaced with the FirebaseAI SDK (firebase-ai) to accommodate the evolving set of supported features and services. For migration details, see the migration guide: https://firebase.google.com/docs/vertex-ai/migrate-to-latest-sdk

Represents function call output to be returned to the model when it requests a function call.

## Summary

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/FunctionResponsePart#FunctionResponsePart(kotlin.String,kotlinx.serialization.json.JsonObject,kotlin.String)(name: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, response: https://firebase.google.com/docs/reference/kotlin/kotlinx/serialization/json/JsonObject, id: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?)` |

| ### Public properties |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/FunctionResponsePart#id()` Matching `id` for a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/FunctionCallPart`, if one was provided. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/FunctionResponsePart#name()` The name of the called function. |
| `https://firebase.google.com/docs/reference/kotlin/kotlinx/serialization/json/JsonObject` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/FunctionResponsePart#response()` The response produced by the function as a `https://developer.android.com/reference/kotlin/org/json/JSONObject.html`. |

## Public constructors

### FunctionResponsePart

```
FunctionResponsePart(name: String, response: JsonObject, id: String? = null)
```

| Parameters |
|---|---|
| `name: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The name of the called function. |
| `response: https://firebase.google.com/docs/reference/kotlin/kotlinx/serialization/json/JsonObject` | The response produced by the function as a `https://developer.android.com/reference/kotlin/org/json/JSONObject.html`. |
| `id: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html? = null` | Matching `id` for a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/FunctionCallPart`, if one was provided. |

## Public properties

### id

```
val id: String?
```

Matching `id` for a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/FunctionCallPart`, if one was provided.

### name

```
val name: String
```

The name of the called function.

### response

```
val response: JsonObject
```

The response produced by the function as a `https://developer.android.com/reference/kotlin/org/json/JSONObject.html`.