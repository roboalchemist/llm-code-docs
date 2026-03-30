# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/FunctionCallPart.md.txt

# FunctionCallPart

# FunctionCallPart


```
class FunctionCallPart : Part
```

<br />

*** ** * ** ***

> [!CAUTION]
> **This class is deprecated.**   
> The Vertex AI in Firebase SDK (firebase-vertexai) has been replaced with the FirebaseAI SDK (firebase-ai) to accommodate the evolving set of supported features and services. For migration details, see the migration guide: https://firebase.google.com/docs/vertex-ai/migrate-to-latest-sdk

Represents function call name and params received from requests.

## Summary

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/FunctionCallPart#FunctionCallPart(kotlin.String,kotlin.collections.Map,kotlin.String)(name: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, args: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, https://firebase.google.com/docs/reference/kotlin/kotlinx/serialization/json/JsonElement>, id: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?)` |

| ### Public properties |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, https://firebase.google.com/docs/reference/kotlin/kotlinx/serialization/json/JsonElement>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/FunctionCallPart#args()` the function parameters and values as a `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/FunctionCallPart#id()` Unique id of the function call. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/FunctionCallPart#name()` the name of the function to call |

## Public constructors

### FunctionCallPart

```
FunctionCallPart(
    name: String,
    args: Map<String, JsonElement>,
    id: String? = null
)
```

| Parameters |
|---|---|
| `name: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | the name of the function to call |
| `args: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, https://firebase.google.com/docs/reference/kotlin/kotlinx/serialization/json/JsonElement>` | the function parameters and values as a `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html` |
| `id: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html? = null` | Unique id of the function call. If present, the returned `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/FunctionResponsePart` should have a matching `id` field. |

## Public properties

### args

```
val args: Map<String, JsonElement>
```

the function parameters and values as a `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html`

### id

```
val id: String?
```

Unique id of the function call. If present, the returned `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/FunctionResponsePart` should have a matching `id` field.

### name

```
val name: String
```

the name of the function to call