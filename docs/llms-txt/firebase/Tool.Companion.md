# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Tool.Companion.md.txt

# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Tool.Companion.md.txt

# Tool.Companion


```
public static class Tool.Companion
```

<br />

*** ** * ** ***

## Summary

|                                                                                            ### Public methods                                                                                            |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `static final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[Tool](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Tool) | [codeExecution](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Tool.Companion#codeExecution())`()` Creates a [Tool](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Tool) instance that allows the model to use code execution.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `static final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[Tool](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Tool) | [functionDeclarations](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Tool.Companion#functionDeclarations(kotlin.collections.List))`(` ` @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[List](https://developer.android.com/reference/kotlin/java/util/List.html)`<@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[FunctionDeclaration](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/FunctionDeclaration)`> functionDeclarations` `)` Creates a [Tool](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Tool) instance that provides the model with access to the [functionDeclarations](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Tool.Companion#functionDeclarations(kotlin.collections.List)). |
| `static final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[Tool](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Tool) | [googleSearch](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Tool.Companion#googleSearch(com.google.firebase.ai.type.GoogleSearch))`(@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[GoogleSearch](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GoogleSearch)` googleSearch)` Creates a [Tool](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Tool) instance that allows the model to use grounding with Google Search.                                                                                                                                                                                                                                                                                                                                                              |
| `static final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[Tool](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Tool) | `@`[PublicPreviewAPI](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/PublicPreviewAPI) [urlContext](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Tool.Companion#urlContext(com.google.firebase.ai.type.UrlContext))`(@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[UrlContext](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/UrlContext)` urlContext)` Creates a [Tool](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Tool) instance that allows you to provide additional context to the models in the form of public web URLs.                                                                                                                                                                                                                  |

## Public methods

### codeExecution

```
publicÂ staticÂ finalÂ @NonNull ToolÂ codeExecution()
```

Creates a [Tool](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Tool) instance that allows the model to use code execution.  

### functionDeclarations

```
publicÂ staticÂ finalÂ @NonNull ToolÂ functionDeclarations(
Â Â Â Â @NonNull List<@NonNull FunctionDeclaration>Â functionDeclarations
)
```

Creates a [Tool](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Tool) instance that provides the model with access to the [functionDeclarations](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Tool.Companion#functionDeclarations(kotlin.collections.List)).  

|                                                                                                                                                                                                          Parameters                                                                                                                                                                                                          |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------|
| `@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[List](https://developer.android.com/reference/kotlin/java/util/List.html)`<@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[FunctionDeclaration](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/FunctionDeclaration)`> functionDeclarations` | The list of functions that this tool allows the model access to. |

### googleSearch

```
publicÂ staticÂ finalÂ @NonNull ToolÂ googleSearch(@NonNull GoogleSearchÂ googleSearch)
```

Creates a [Tool](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Tool) instance that allows the model to use grounding with Google Search.

Grounding with Google Search can be used to allow the model to connect to Google Search to access and incorporate up-to-date information from the web into it's responses.

When using this feature, you are required to comply with the "grounding with Google Search" usage requirements for your chosen API provider: [Gemini Developer API](https://ai.google.dev/gemini-api/terms#grounding-with-google-search) or Vertex AI Gemini API (see [Service Terms](https://cloud.google.com/terms/service-terms) section within the Service Specific Terms).  

|                                                                                                         Parameters                                                                                                         |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[GoogleSearch](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GoogleSearch)` googleSearch` | An empty [GoogleSearch](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GoogleSearch) object. The presence of this object in the list of tools enables the model to use Google Search. |

|                                                                                           Returns                                                                                           |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------|
| `@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[Tool](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Tool) | A [Tool](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Tool) configured for Google Search. |

### urlContext

```
@PublicPreviewAPI
publicÂ staticÂ finalÂ @NonNull ToolÂ urlContext(@NonNull UrlContextÂ urlContext)
```

Creates a [Tool](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Tool) instance that allows you to provide additional context to the models in the form of public web URLs. By including URLs in your request, the Gemini model will access the content from those pages to inform and enhance its response.  

|                                                                                                      Parameters                                                                                                      |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------|
| `@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[UrlContext](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/UrlContext)` urlContext` | Specifies the URL context configuration. |

|                                                                                           Returns                                                                                           |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|
| `@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[Tool](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Tool) | A [Tool](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Tool) configured for URL context. |