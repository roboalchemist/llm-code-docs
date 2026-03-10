# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/FunctionDeclaration.md.txt

# FunctionDeclaration

# FunctionDeclaration


```
public final class FunctionDeclaration
```

<br />

*** ** * ** ***

Defines a function that the model can use as a tool.

When generating responses, the model might need external information or require the application to perform an action. `FunctionDeclaration` provides the necessary information for the model to create a `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/FunctionCallPart`, which instructs the client to execute the corresponding function. The client then sends the result back to the model as a `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/FunctionResponsePart`.

For example

```
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
| `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Schema` |   |

## Summary

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/FunctionDeclaration#FunctionDeclaration(kotlin.String,kotlin.String,kotlin.collections.Map,kotlin.collections.List)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html name, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html description, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/Map.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Schema> parameters, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html> optionalParameters )` |

## Public constructors

### FunctionDeclaration

```
public FunctionDeclaration(
    @NonNull String name,
    @NonNull String description,
    @NonNull Map<@NonNull String, @NonNull Schema> parameters,
    @NonNull List<@NonNull String> optionalParameters
)
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html name` | The name of the function. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html description` | The description of what the function does and its output. To improve the effectiveness of the model, the description should be clear and detailed. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/Map.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Schema> parameters` | The map of parameters names to their `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Schema` the function accepts as arguments. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html> optionalParameters` | The list of parameter names that the model can omit when invoking this function. |