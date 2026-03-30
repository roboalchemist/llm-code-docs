# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/AutoFunctionDeclaration.md.txt

# AutoFunctionDeclaration

# AutoFunctionDeclaration


```
class AutoFunctionDeclaration<I : Any, O : Any>
```

<br />

*** ** * ** ***

Defines a function that the model can use as a tool. Including a function references to enable automatic function calling.

When generating responses, the model might need external information or require the application to perform an action. `AutoFunctionDeclaration` provides the necessary information for the model to create a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FunctionCallPart`, which instructs the client to execute the corresponding function. The client then sends the result back to the model as a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FunctionResponsePart`.

For example

```kotlin
val getExchangeRate = AutoFunctionDeclaration.create(
   name = "getExchangeRate",
   description = "Get the exchange rate for currencies between countries.",
   inputSchema = CurrencyRequest.schema,
   outputSchema = CurrencyResponse.schema,
) {
   // make an api request to convert currencies and return the result
}
```

| See also |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/JsonSchema` |   |

## Summary

| ### Public companion functions |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/AutoFunctionDeclaration<I, https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FunctionResponsePart>` | `<I : https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html> https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/AutoFunctionDeclaration.Companion#create(kotlin.String,kotlin.String,com.google.firebase.ai.type.JsonSchema,kotlin.coroutines.SuspendFunction1)( functionName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, description: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, inputSchema: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/JsonSchema<I>, functionReference: (suspend (I) -> https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FunctionResponsePart)? )` Create a strongly typed function declaration with an associated function reference. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/AutoFunctionDeclaration<I, O>` | `<I : https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html, O : https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html> https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/AutoFunctionDeclaration.Companion#create(kotlin.String,kotlin.String,com.google.firebase.ai.type.JsonSchema,com.google.firebase.ai.type.JsonSchema,kotlin.coroutines.SuspendFunction1)( functionName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, description: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, inputSchema: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/JsonSchema<I>, outputSchema: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/JsonSchema<O>, functionReference: (suspend (I) -> O)? )` Create a strongly typed function declaration with an associated function reference. |

| ### Public properties |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/AutoFunctionDeclaration#description()` |
| `(suspend (I) -> O)?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/AutoFunctionDeclaration#functionReference()` |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/JsonSchema<I>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/AutoFunctionDeclaration#inputSchema()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/AutoFunctionDeclaration#name()` |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/JsonSchema<O>?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/AutoFunctionDeclaration#outputSchema()` |

## Public companion functions

### create

```
fun <I : Any> create(
    functionName: String,
    description: String,
    inputSchema: JsonSchema<I>,
    functionReference: (suspend (I) -> FunctionResponsePart)? = null
): AutoFunctionDeclaration<I, FunctionResponsePart>
```

Create a strongly typed function declaration with an associated function reference. This version allows an arbitrary JsonObject as output rather than a strict schema.

| Parameters |
|---|---|
| `functionName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | the name of the function (to the model) |
| `description: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | the description of the function |
| `inputSchema: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/JsonSchema<I>` | the object the model must provide to you as input |
| `functionReference: (suspend (I) -> https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FunctionResponsePart)? = null` | the function that will be executed when requested by the model. |

### create

```
fun <I : Any, O : Any> create(
    functionName: String,
    description: String,
    inputSchema: JsonSchema<I>,
    outputSchema: JsonSchema<O>,
    functionReference: (suspend (I) -> O)? = null
): AutoFunctionDeclaration<I, O>
```

Create a strongly typed function declaration with an associated function reference.

| Parameters |
|---|---|
| `functionName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | the name of the function (to the model) |
| `description: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | the description of the function |
| `inputSchema: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/JsonSchema<I>` | the object the model must provide to you as input |
| `outputSchema: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/JsonSchema<O>` | the type that will be return to the model when the function is executed |
| `functionReference: (suspend (I) -> O)? = null` | the function that will be executed when requested by the model. |

## Public properties

### description

```
val description: String
```

### functionReference

```
val functionReference: (suspend (I) -> O)?
```

### inputSchema

```
val inputSchema: JsonSchema<I>
```

### name

```
val name: String
```

### outputSchema

```
val outputSchema: JsonSchema<O>?
```