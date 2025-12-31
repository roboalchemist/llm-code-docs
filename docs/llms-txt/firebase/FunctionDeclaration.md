# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/FunctionDeclaration.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/FunctionDeclaration.md.txt

# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FunctionDeclaration.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/FunctionDeclaration.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/FunctionDeclaration.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FunctionDeclaration.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/FunctionDeclaration.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/FunctionDeclaration.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FunctionDeclaration.md.txt

# FunctionDeclaration

# FunctionDeclaration


```
class FunctionDeclaration
```

<br />

*** ** * ** ***

Defines a function that the model can use as a tool.

When generating responses, the model might need external information or require the application to perform an action. `FunctionDeclaration` provides the necessary information for the model to create a [FunctionCallPart](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FunctionCallPart), which instructs the client to execute the corresponding function. The client then sends the result back to the model as a [FunctionResponsePart](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FunctionResponsePart).

For example  

```kotlin
val getExchangeRate = FunctionDeclaration(
   name = "getExchangeRate",
   description = "Get the exchange rate for currencies between countries.",
   parameters = mapOf(
     "currencyFrom" to Schema.str("The currency to convert from."),
     "currencyTo" to Schema.str("The currency to convert to.")
   )
)
```

See the [Use the Gemini API for function calling](https://firebase.google.com/docs/vertex-ai/function-calling?platform=android) guide for more information on function calling.  

|                                            See also                                            |
|------------------------------------------------------------------------------------------------|---|
| [Schema](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Schema) |   |

## Summary

|                                                                                                                                                                                                                                                                                                                                                                                                                                                        ### Public constructors                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [FunctionDeclaration](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FunctionDeclaration#FunctionDeclaration(kotlin.String,kotlin.String,kotlin.collections.Map,kotlin.collections.List))`(` ` name: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`,` ` description: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`,` ` parameters: `[Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html)`<`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`, `[Schema](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Schema)`>,` ` optionalParameters: `[List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)`<`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`>` `)` |

## Public constructors

### FunctionDeclaration

```
FunctionDeclaration(
Â Â Â Â name:Â String,
Â Â Â Â description:Â String,
Â Â Â Â parameters:Â Map<String,Â Schema>,
Â Â Â Â optionalParameters:Â List<String> = emptyList()
)
```  

|                                                                                                                                          Parameters                                                                                                                                          |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `name: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)                                                                                                                                                                                                     | The name of the function.                                                                                                                                              |
| `description: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)                                                                                                                                                                                              | The description of what the function does and its output. To improve the effectiveness of the model, the description should be clear and detailed.                     |
| `parameters: `[Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html)`<`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`, `[Schema](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Schema)`>` | The map of parameters names to their [Schema](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Schema) the function accepts as arguments. |
| `optionalParameters: `[List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)`<`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`> = emptyList()`                                                                           | The list of parameter names that the model can omit when invoking this function.                                                                                       |