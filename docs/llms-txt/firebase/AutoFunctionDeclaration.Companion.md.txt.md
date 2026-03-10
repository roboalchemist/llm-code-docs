# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/AutoFunctionDeclaration.Companion.md.txt

# AutoFunctionDeclaration.Companion

# AutoFunctionDeclaration.Companion


```
public static class AutoFunctionDeclaration.Companion
```

<br />

*** ** * ** ***

## Summary

| ### Public methods |
|---|---|
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/AutoFunctionDeclaration<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html I, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/FunctionResponsePart>` | `<I extends https://developer.android.com/reference/kotlin/java/lang/Object.html> https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/AutoFunctionDeclaration.Companion#create(kotlin.String,kotlin.String,com.google.firebase.ai.type.JsonSchema,kotlin.coroutines.SuspendFunction1)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html functionName, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html description, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/JsonSchema<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html I> inputSchema, https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.coroutines/-suspend-function1/index.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html I, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/FunctionResponsePart> functionReference )` Create a strongly typed function declaration with an associated function reference. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/AutoFunctionDeclaration<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html I, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html O>` | `<I extends https://developer.android.com/reference/kotlin/java/lang/Object.html, O extends https://developer.android.com/reference/kotlin/java/lang/Object.html> https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/AutoFunctionDeclaration.Companion#create(kotlin.String,kotlin.String,com.google.firebase.ai.type.JsonSchema,com.google.firebase.ai.type.JsonSchema,kotlin.coroutines.SuspendFunction1)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html functionName, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html description, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/JsonSchema<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html I> inputSchema, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/JsonSchema<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html O> outputSchema, https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.coroutines/-suspend-function1/index.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html I, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html O> functionReference )` Create a strongly typed function declaration with an associated function reference. |

## Public methods

### create

```
public static final @NonNull AutoFunctionDeclaration<@NonNull I, @NonNull FunctionResponsePart> <I extends Object> create(
    @NonNull String functionName,
    @NonNull String description,
    @NonNull JsonSchema<@NonNull I> inputSchema,
    SuspendFunction1<@NonNull I, @NonNull FunctionResponsePart> functionReference
)
```

Create a strongly typed function declaration with an associated function reference. This version allows an arbitrary JsonObject as output rather than a strict schema.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html functionName` | the name of the function (to the model) |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html description` | the description of the function |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/JsonSchema<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html I> inputSchema` | the object the model must provide to you as input |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.coroutines/-suspend-function1/index.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html I, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/FunctionResponsePart> functionReference` | the function that will be executed when requested by the model. |

### create

```
public static final @NonNull AutoFunctionDeclaration<@NonNull I, @NonNull O> <I extends Object, O extends Object> create(
    @NonNull String functionName,
    @NonNull String description,
    @NonNull JsonSchema<@NonNull I> inputSchema,
    @NonNull JsonSchema<@NonNull O> outputSchema,
    SuspendFunction1<@NonNull I, @NonNull O> functionReference
)
```

Create a strongly typed function declaration with an associated function reference.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html functionName` | the name of the function (to the model) |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html description` | the description of the function |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/JsonSchema<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html I> inputSchema` | the object the model must provide to you as input |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/JsonSchema<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html O> outputSchema` | the type that will be return to the model when the function is executed |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.coroutines/-suspend-function1/index.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html I, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html O> functionReference` | the function that will be executed when requested by the model. |