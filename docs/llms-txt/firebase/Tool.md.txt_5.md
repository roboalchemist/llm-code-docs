# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Tool.md.txt

# Tool

# Tool


```
class Tool
```

<br />

*** ** * ** ***

Contains a set of tools (like function declarations) that the model has access to. These tools can be used to gather information or complete tasks.

## Summary

| ### Public companion functions |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Tool` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Tool.Companion#codeExecution()()` Creates a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Tool` instance that allows the model to use code execution. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Tool` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Tool.Companion#functionDeclarations(kotlin.collections.List)(functionDeclarations: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FunctionDeclaration>)` Creates a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Tool` instance that provides the model with access to the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Tool.Companion#functionDeclarations(kotlin.collections.List)`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Tool` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Tool.Companion#functionDeclarations(kotlin.collections.List,kotlin.collections.List)( functionDeclarations: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FunctionDeclaration>?, autoFunctionDeclarations: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/AutoFunctionDeclaration<*, *>>? )` Creates a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Tool` instance that provides the model with access to the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Tool.Companion#functionDeclarations(kotlin.collections.List,kotlin.collections.List)`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Tool` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Tool.Companion#googleSearch(com.google.firebase.ai.type.GoogleSearch)(googleSearch: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GoogleSearch)` Creates a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Tool` instance that allows the model to use grounding with Google Search. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Tool` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Tool.Companion#urlContext(com.google.firebase.ai.type.UrlContext)(urlContext: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/UrlContext)` Creates a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Tool` instance that allows you to provide additional context to the models in the form of public web URLs. |

## Public companion functions

### codeExecution

```
fun codeExecution(): Tool
```

Creates a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Tool` instance that allows the model to use code execution.

### functionDeclarations

```
fun functionDeclarations(functionDeclarations: List<FunctionDeclaration>): Tool
```

Creates a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Tool` instance that provides the model with access to the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Tool.Companion#functionDeclarations(kotlin.collections.List)`.

| Parameters |
|---|---|
| `functionDeclarations: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FunctionDeclaration>` | The list of functions that this tool allows the model access to. |

### functionDeclarations

```
fun functionDeclarations(
    functionDeclarations: List<FunctionDeclaration>? = null,
    autoFunctionDeclarations: List<AutoFunctionDeclaration<*, *>>?
): Tool
```

Creates a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Tool` instance that provides the model with access to the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Tool.Companion#functionDeclarations(kotlin.collections.List,kotlin.collections.List)`.

| Parameters |
|---|---|
| `functionDeclarations: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FunctionDeclaration>? = null` | The list of functions that this tool allows the model access to. |
| `autoFunctionDeclarations: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/AutoFunctionDeclaration<*, *>>?` | The list of functions that this tool has access to which should be executed automatically |

### googleSearch

```
fun googleSearch(googleSearch: GoogleSearch = GoogleSearch()): Tool
```

Creates a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Tool` instance that allows the model to use grounding with Google Search.

Grounding with Google Search can be used to allow the model to connect to Google Search to access and incorporate up-to-date information from the web into it's responses.

When using this feature, you are required to comply with the "grounding with Google Search" usage requirements for your chosen API provider: [Gemini Developer API](https://ai.google.dev/gemini-api/terms#grounding-with-google-search) or Vertex AI Gemini API (see [Service Terms](https://cloud.google.com/terms/service-terms) section within the Service Specific Terms).

| Parameters |
|---|---|
| `googleSearch: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GoogleSearch = GoogleSearch()` | An empty `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GoogleSearch` object. The presence of this object in the list of tools enables the model to use Google Search. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Tool` | A `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Tool` configured for Google Search. |

### urlContext

```
fun urlContext(urlContext: UrlContext = UrlContext()): Tool
```

Creates a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Tool` instance that allows you to provide additional context to the models in the form of public web URLs. By including URLs in your request, the Gemini model will access the content from those pages to inform and enhance its response.

| Parameters |
|---|---|
| `urlContext: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/UrlContext = UrlContext()` | Specifies the URL context configuration. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Tool` | A `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Tool` configured for URL context. |