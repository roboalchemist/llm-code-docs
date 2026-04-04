# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Tool.Companion.md.txt

# Tool.Companion

# Tool.Companion


```
public static class Tool.Companion
```

<br />

*** ** * ** ***

## Summary

| ### Public methods |
|---|---|
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Tool` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Tool.Companion#codeExecution()()` Creates a `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Tool` instance that allows the model to use code execution. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Tool` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Tool.Companion#functionDeclarations(kotlin.collections.List)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/FunctionDeclaration> functionDeclarations )` Creates a `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Tool` instance that provides the model with access to the `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Tool.Companion#functionDeclarations(kotlin.collections.List)`. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Tool` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Tool.Companion#functionDeclarations(kotlin.collections.List,kotlin.collections.List)( https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/FunctionDeclaration> functionDeclarations, https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/AutoFunctionDeclaration<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html ?, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html ?>> autoFunctionDeclarations )` Creates a `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Tool` instance that provides the model with access to the `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Tool.Companion#functionDeclarations(kotlin.collections.List,kotlin.collections.List)`. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Tool` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Tool.Companion#googleSearch(com.google.firebase.ai.type.GoogleSearch)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GoogleSearch googleSearch)` Creates a `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Tool` instance that allows the model to use grounding with Google Search. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Tool` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Tool.Companion#urlContext(com.google.firebase.ai.type.UrlContext)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/UrlContext urlContext)` Creates a `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Tool` instance that allows you to provide additional context to the models in the form of public web URLs. |

## Public methods

### codeExecution

```
public static final @NonNull Tool codeExecution()
```

Creates a `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Tool` instance that allows the model to use code execution.

### functionDeclarations

```
public static final @NonNull Tool functionDeclarations(
    @NonNull List<@NonNull FunctionDeclaration> functionDeclarations
)
```

Creates a `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Tool` instance that provides the model with access to the `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Tool.Companion#functionDeclarations(kotlin.collections.List)`.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/FunctionDeclaration> functionDeclarations` | The list of functions that this tool allows the model access to. |

### functionDeclarations

```
public static final @NonNull Tool functionDeclarations(
    List<@NonNull FunctionDeclaration> functionDeclarations,
    List<@NonNull AutoFunctionDeclaration<@NonNull ?, @NonNull ?>> autoFunctionDeclarations
)
```

Creates a `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Tool` instance that provides the model with access to the `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Tool.Companion#functionDeclarations(kotlin.collections.List,kotlin.collections.List)`.

| Parameters |
|---|---|
| `https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/FunctionDeclaration> functionDeclarations` | The list of functions that this tool allows the model access to. |
| `https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/AutoFunctionDeclaration<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html ?, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html ?>> autoFunctionDeclarations` | The list of functions that this tool has access to which should be executed automatically |

### googleSearch

```
public static final @NonNull Tool googleSearch(@NonNull GoogleSearch googleSearch)
```

Creates a `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Tool` instance that allows the model to use grounding with Google Search.

Grounding with Google Search can be used to allow the model to connect to Google Search to access and incorporate up-to-date information from the web into it's responses.

When using this feature, you are required to comply with the "grounding with Google Search" usage requirements for your chosen API provider: [Gemini Developer API](https://ai.google.dev/gemini-api/terms#grounding-with-google-search) or Vertex AI Gemini API (see [Service Terms](https://cloud.google.com/terms/service-terms) section within the Service Specific Terms).

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GoogleSearch googleSearch` | An empty `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GoogleSearch` object. The presence of this object in the list of tools enables the model to use Google Search. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Tool` | A `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Tool` configured for Google Search. |

### urlContext

```
public static final @NonNull Tool urlContext(@NonNull UrlContext urlContext)
```

Creates a `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Tool` instance that allows you to provide additional context to the models in the form of public web URLs. By including URLs in your request, the Gemini model will access the content from those pages to inform and enhance its response.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/UrlContext urlContext` | Specifies the URL context configuration. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Tool` | A `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Tool` configured for URL context. |