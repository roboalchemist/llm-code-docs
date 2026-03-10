# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/AutoFunctionDeclaration.md.txt

# AutoFunctionDeclaration

# AutoFunctionDeclaration


```
public final class AutoFunctionDeclaration<I extends Object, O extends Object>
```

<br />

*** ** * ** ***

Defines a function that the model can use as a tool. Including a function references to enable automatic function calling.

When generating responses, the model might need external information or require the application to perform an action. `AutoFunctionDeclaration` provides the necessary information for the model to create a `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/FunctionCallPart`, which instructs the client to execute the corresponding function. The client then sends the result back to the model as a `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/FunctionResponsePart`.

For example

```
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
| `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/JsonSchema` |   |

## Summary

| ### Nested types |
|---|
| `public static class https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/AutoFunctionDeclaration.Companion` |

| ### Public fields |
|---|---|
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/AutoFunctionDeclaration#description()` |
| `final https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.coroutines/-suspend-function1/index.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html I, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html O>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/AutoFunctionDeclaration#functionReference()` |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/JsonSchema<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html I>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/AutoFunctionDeclaration#inputSchema()` |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/AutoFunctionDeclaration#name()` |
| `final https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/JsonSchema<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html O>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/AutoFunctionDeclaration#outputSchema()` |

## Public fields

### description

```
public final @NonNull String description
```

### functionReference

```
public final SuspendFunction1<@NonNull I, @NonNull O> functionReference
```

### inputSchema

```
public final @NonNull JsonSchema<@NonNull I> inputSchema
```

### name

```
public final @NonNull String name
```

### outputSchema

```
public final JsonSchema<@NonNull O> outputSchema
```