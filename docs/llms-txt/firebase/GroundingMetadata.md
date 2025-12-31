# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GroundingMetadata.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/GroundingMetadata.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GroundingMetadata.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/GroundingMetadata.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GroundingMetadata.md.txt

# GroundingMetadata


```
class GroundingMetadata
```

<br />

*** ** * ** ***

Metadata returned to the client when grounding is enabled.

If using grounding with Google Search, you are required to comply with the "Grounding with Google Search" usage requirements for your chosen API provider: [Gemini Developer API](https://ai.google.dev/gemini-api/terms#grounding-with-google-search) or Vertex AI Gemini API (see [Service Terms](https://cloud.google.com/terms/service-terms) section within the Service Specific Terms).

## Summary

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        ### Public constructors                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [GroundingMetadata](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GroundingMetadata#GroundingMetadata(kotlin.collections.List,com.google.firebase.ai.type.SearchEntryPoint,kotlin.collections.List,kotlin.collections.List,kotlin.collections.List,kotlin.collections.List))`(` ` webSearchQueries: `[List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)`<`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`>,` ` searchEntryPoint: `[SearchEntryPoint](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/SearchEntryPoint)`?,` ` retrievalQueries: `[List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)`<`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`>,` ` groundingAttribution: `[List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)`<`[GroundingAttribution](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GroundingAttribution)`>,` ` groundingChunks: `[List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)`<`[GroundingChunk](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GroundingChunk)`>,` ` groundingSupports: `[List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)`<`[GroundingSupport](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GroundingSupport)`>` `)` |

|                                                                                                  ### Public properties                                                                                                   |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)`<`[GroundingAttribution](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GroundingAttribution)`>` | [groundingAttribution](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GroundingMetadata#groundingAttribution()) **This property is deprecated.** Use groundingChunks instead                                                                      |
| [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)`<`[GroundingChunk](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GroundingChunk)`>`             | [groundingChunks](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GroundingMetadata#groundingChunks()) The list of [GroundingChunk](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GroundingChunk) classes.         |
| [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)`<`[GroundingSupport](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GroundingSupport)`>`         | [groundingSupports](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GroundingMetadata#groundingSupports()) The list of [GroundingSupport](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GroundingSupport) objects. |
| [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)`<`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`>`                                           | [retrievalQueries](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GroundingMetadata#retrievalQueries())                                                                                                                                           |
| [SearchEntryPoint](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/SearchEntryPoint)`?`                                                                                                    | [searchEntryPoint](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GroundingMetadata#searchEntryPoint()) Google Search entry point for web searches.                                                                                               |
| [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)`<`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`>`                                           | [webSearchQueries](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GroundingMetadata#webSearchQueries()) The list of web search queries that the model performed to gather the grounding information.                                              |

## Public constructors

### GroundingMetadata

```
GroundingMetadata(
Â Â Â Â webSearchQueries:Â List<String>,
Â Â Â Â searchEntryPoint:Â SearchEntryPoint?,
Â Â Â Â retrievalQueries:Â List<String>,
Â Â Â Â groundingAttribution:Â List<GroundingAttribution>,
Â Â Â Â groundingChunks:Â List<GroundingChunk>,
Â Â Â Â groundingSupports:Â List<GroundingSupport>
)
```  

## Public properties

### groundingAttribution

```
valÂ groundingAttribution:Â List<GroundingAttribution>
```
| **This property is deprecated.**   
Use groundingChunks instead  

### groundingChunks

```
valÂ groundingChunks:Â List<GroundingChunk>
```

The list of [GroundingChunk](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GroundingChunk) classes. Each chunk represents a piece of retrieved content that the model used to ground its response.  

### groundingSupports

```
valÂ groundingSupports:Â List<GroundingSupport>
```

The list of [GroundingSupport](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GroundingSupport) objects. Each object details how specific segments of the model's response are supported by the `groundingChunks`.  

### retrievalQueries

```
valÂ retrievalQueries:Â List<String>
```  

### searchEntryPoint

```
valÂ searchEntryPoint:Â SearchEntryPoint?
```

Google Search entry point for web searches. This contains an HTML/CSS snippet that **must** be embedded in an app to display a Google Search Entry point for follow-up web searches related to the model's "Grounded Response".  

### webSearchQueries

```
valÂ webSearchQueries:Â List<String>
```

The list of web search queries that the model performed to gather the grounding information. These can be used to allow users to explore the search results themselves.