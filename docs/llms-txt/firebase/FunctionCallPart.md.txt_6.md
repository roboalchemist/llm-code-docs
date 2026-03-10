# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FunctionCallPart.md.txt

# FunctionCallPart

# FunctionCallPart


```
class FunctionCallPart : Part
```

<br />

*** ** * ** ***

Represents function call name and params received from requests.

## Summary

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FunctionCallPart#FunctionCallPart(kotlin.String,kotlin.collections.Map,kotlin.String)(name: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, args: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-json/kotlinx.serialization.json/-json-element/index.html>, id: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?)` |

| ### Public properties |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-json/kotlinx.serialization.json/-json-element/index.html>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FunctionCallPart#args()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FunctionCallPart#id()` |
| `open https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FunctionCallPart#isThought()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FunctionCallPart#name()` |

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
| `args: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-json/kotlinx.serialization.json/-json-element/index.html>` | the function parameters and values as a `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html` |
| `id: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html? = null` | Unique id of the function call. If present, the returned `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FunctionResponsePart` should have a matching `id` field. |

## Public properties

### args

```
val args: Map<String, JsonElement>
```

### id

```
val id: String?
```

### isThought

```
open val isThought: Boolean
```

### name

```
val name: String
```