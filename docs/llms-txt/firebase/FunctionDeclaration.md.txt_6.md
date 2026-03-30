# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/FunctionDeclaration.md.txt

# FunctionDeclaration

# FunctionDeclaration


```
class FunctionDeclaration
```

<br />

*** ** * ** ***

> [!CAUTION]
> **This class is deprecated.**   
> The Vertex AI in Firebase SDK (firebase-vertexai) has been replaced with the FirebaseAI SDK (firebase-ai) to accommodate the evolving set of supported features and services. For migration details, see the migration guide: https://firebase.google.com/docs/vertex-ai/migrate-to-latest-sdk

Defines a function that the model can use as a tool.

When generating responses, the model might need external information or require the application to perform an action. `FunctionDeclaration` provides the necessary information for the model to create a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/FunctionCallPart`, which instructs the client to execute the corresponding function. The client then sends the result back to the model as a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/FunctionResponsePart`.

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

| See also |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Schema` |   |

## Summary

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/FunctionDeclaration#FunctionDeclaration(kotlin.String,kotlin.String,kotlin.collections.Map,kotlin.collections.List)( name: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, description: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, parameters: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Schema>, optionalParameters: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html> )` |

## Public constructors

### FunctionDeclaration

```
FunctionDeclaration(
    name: String,
    description: String,
    parameters: Map<String, Schema>,
    optionalParameters: List<String> = emptyList()
)
```

| Parameters |
|---|---|
| `name: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The name of the function. |
| `description: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The description of what the function does and its output. To improve the effectiveness of the model, the description should be clear and detailed. |
| `parameters: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Schema>` | The map of parameters names to their `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Schema` the function accepts as arguments. |
| `optionalParameters: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html> = emptyList()` | The list of parameter names that the model can omit when invoking this function. |