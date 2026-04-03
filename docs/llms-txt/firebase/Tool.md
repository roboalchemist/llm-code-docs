# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Tool.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/Tool.md.txt

# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Tool.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/Tool.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Tool.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Tool.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/Tool.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Tool.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Tool.md.txt

# Tool


```
class Tool
```

<br />

*** ** * ** ***

Contains a set of tools (like function declarations) that the model has access to. These tools can be used to gather information or complete tasks.

## Summary

|                               ### Public companion functions                               |
|--------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Tool](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Tool) | [codeExecution](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Tool.Companion#codeExecution())`()` Creates a [Tool](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Tool) instance that allows the model to use code execution.                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [Tool](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Tool) | [functionDeclarations](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Tool.Companion#functionDeclarations(kotlin.collections.List))`(functionDeclarations: `[List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)`<`[FunctionDeclaration](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FunctionDeclaration)`>)` Creates a [Tool](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Tool) instance that provides the model with access to the [functionDeclarations](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Tool.Companion#functionDeclarations(kotlin.collections.List)). |
| [Tool](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Tool) | [googleSearch](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Tool.Companion#googleSearch(com.google.firebase.ai.type.GoogleSearch))`(googleSearch: `[GoogleSearch](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GoogleSearch)`)` Creates a [Tool](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Tool) instance that allows the model to use grounding with Google Search.                                                                                                                                                                                                                                                                      |
| [Tool](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Tool) | `@`[PublicPreviewAPI](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/PublicPreviewAPI) [urlContext](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Tool.Companion#urlContext(com.google.firebase.ai.type.UrlContext))`(urlContext: `[UrlContext](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/UrlContext)`)` Creates a [Tool](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Tool) instance that allows you to provide additional context to the models in the form of public web URLs.                                                                                                                           |

## Public companion functions

### codeExecution

```
funÂ codeExecution():Â Tool
```

Creates a [Tool](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Tool) instance that allows the model to use code execution.  

### functionDeclarations

```
funÂ functionDeclarations(functionDeclarations:Â List<FunctionDeclaration>):Â Tool
```

Creates a [Tool](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Tool) instance that provides the model with access to the [functionDeclarations](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Tool.Companion#functionDeclarations(kotlin.collections.List)).  

|                                                                                                                   Parameters                                                                                                                   |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------|
| `functionDeclarations: `[List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)`<`[FunctionDeclaration](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FunctionDeclaration)`>` | The list of functions that this tool allows the model access to. |

### googleSearch

```
funÂ googleSearch(googleSearch:Â GoogleSearch = GoogleSearch()):Â Tool
```

Creates a [Tool](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Tool) instance that allows the model to use grounding with Google Search.

Grounding with Google Search can be used to allow the model to connect to Google Search to access and incorporate up-to-date information from the web into it's responses.

When using this feature, you are required to comply with the "grounding with Google Search" usage requirements for your chosen API provider: [Gemini Developer API](https://ai.google.dev/gemini-api/terms#grounding-with-google-search) or Vertex AI Gemini API (see [Service Terms](https://cloud.google.com/terms/service-terms) section within the Service Specific Terms).  

|                                                                  Parameters                                                                   |
|-----------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `googleSearch: `[GoogleSearch](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GoogleSearch)` = GoogleSearch()` | An empty [GoogleSearch](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GoogleSearch) object. The presence of this object in the list of tools enables the model to use Google Search. |

|                                          Returns                                           |
|--------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|
| [Tool](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Tool) | A [Tool](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Tool) configured for Google Search. |

### urlContext

```
@PublicPreviewAPI
funÂ urlContext(urlContext:Â UrlContext = UrlContext()):Â Tool
```

Creates a [Tool](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Tool) instance that allows you to provide additional context to the models in the form of public web URLs. By including URLs in your request, the Gemini model will access the content from those pages to inform and enhance its response.  

|                                                              Parameters                                                               |
|---------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------|
| `urlContext: `[UrlContext](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/UrlContext)` = UrlContext()` | Specifies the URL context configuration. |

|                                          Returns                                           |
|--------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------|
| [Tool](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Tool) | A [Tool](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Tool) configured for URL context. |