# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FunctionCallPart.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/FunctionCallPart.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/FunctionCallPart.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/FunctionCallPart.md.txt

# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/FunctionCallPart.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FunctionCallPart.md.txt

# FunctionCallPart


```
class FunctionCallPart : Part
```

<br />

*** ** * ** ***

Represents function call name and params received from requests.

## Summary

|                                                                                                                                                                                                                                                                                                                                              ### Public constructors                                                                                                                                                                                                                                                                                                                                               |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [FunctionCallPart](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FunctionCallPart#FunctionCallPart(kotlin.String,kotlin.collections.Map,kotlin.String))`(name: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`, args: `[Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html)`<`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`, `[JsonElement](https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-json/kotlinx.serialization.json/-json-element/index.html)`>, id: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?)` |

|                                                                                                                                                     ### Public properties                                                                                                                                                      |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|
| [Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html)`<`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`, `[JsonElement](https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-json/kotlinx.serialization.json/-json-element/index.html)`>` | [args](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FunctionCallPart#args())           |
| [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?`                                                                                                                                                                                                                                            | [id](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FunctionCallPart#id())               |
| `open `[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)                                                                                                                                                                                                                                      | [isThought](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FunctionCallPart#isThought()) |
| [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)                                                                                                                                                                                                                                               | [name](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FunctionCallPart#name())           |

## Public constructors

### FunctionCallPart

```
FunctionCallPart(
Â Â Â Â name:Â String,
Â Â Â Â args:Â Map<String,Â JsonElement>,
Â Â Â Â id:Â String? = null
)
```  

|                                                                                                                                                               Parameters                                                                                                                                                               |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `name: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)                                                                                                                                                                                                                                               | the name of the function to call                                                                                                                                                                                       |
| `args: `[Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html)`<`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`, `[JsonElement](https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-json/kotlinx.serialization.json/-json-element/index.html)`>` | the function parameters and values as a [Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html)                                                                                         |
| `id: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`? = null`                                                                                                                                                                                                                                       | Unique id of the function call. If present, the returned [FunctionResponsePart](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FunctionResponsePart) should have a matching `id` field. |

## Public properties

### args

```
valÂ args:Â Map<String,Â JsonElement>
```  

### id

```
valÂ id:Â String?
```  

### isThought

```
openÂ valÂ isThought:Â Boolean
```  

### name

```
valÂ name:Â String
```