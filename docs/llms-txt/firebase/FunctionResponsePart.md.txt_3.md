# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FunctionResponsePart.md.txt

# FunctionResponsePart

# FunctionResponsePart


```
class FunctionResponsePart : Part
```

<br />

*** ** * ** ***

Represents function call output to be returned to the model when it requests a function call.

## Summary

| ### Public companion functions |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FunctionResponsePart` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FunctionResponsePart.Companion#from(kotlinx.serialization.json.JsonObject,kotlin.collections.List)(jsonObject: https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-json/kotlinx.serialization.json/-json-object/index.html, parts: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Part>)` |

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FunctionResponsePart#FunctionResponsePart(kotlin.String,kotlinx.serialization.json.JsonObject,kotlin.String,kotlin.collections.List)( name: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, response: https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-json/kotlinx.serialization.json/-json-object/index.html, id: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?, parts: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Part> )` |

| ### Public properties |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FunctionResponsePart#id()` |
| `open https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FunctionResponsePart#isThought()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FunctionResponsePart#name()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Part>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FunctionResponsePart#parts()` |
| `https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-json/kotlinx.serialization.json/-json-object/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FunctionResponsePart#response()` |

## Public companion functions

### from

```
fun from(jsonObject: JsonObject, parts: List<Part> = emptyList()): FunctionResponsePart
```

## Public constructors

### FunctionResponsePart

```
FunctionResponsePart(
    name: String,
    response: JsonObject,
    id: String? = null,
    parts: List<Part> = emptyList()
)
```

| Parameters |
|---|---|
| `name: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The name of the called function. |
| `response: https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-json/kotlinx.serialization.json/-json-object/index.html` | The response produced by the function as a `https://developer.android.com/reference/kotlin/org/json/JSONObject.html`. |
| `id: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html? = null` | Matching `id` for a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FunctionCallPart`, if one was provided. |

## Public properties

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

### parts

```
val parts: List<Part>
```

### response

```
val response: JsonObject
```