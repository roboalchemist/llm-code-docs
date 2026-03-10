# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GroundingMetadata.md.txt

# GroundingMetadata

# GroundingMetadata


```
class GroundingMetadata
```

<br />

*** ** * ** ***

Metadata returned to the client when grounding is enabled.

If using grounding with Google Search, you are required to comply with the "Grounding with Google Search" usage requirements for your chosen API provider: [Gemini Developer API](https://ai.google.dev/gemini-api/terms#grounding-with-google-search) or Vertex AI Gemini API (see [Service Terms](https://cloud.google.com/terms/service-terms) section within the Service Specific Terms).

## Summary

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GroundingMetadata#GroundingMetadata(kotlin.collections.List,com.google.firebase.ai.type.SearchEntryPoint,kotlin.collections.List,kotlin.collections.List,kotlin.collections.List,kotlin.collections.List)( webSearchQueries: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html>, searchEntryPoint: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/SearchEntryPoint?, retrievalQueries: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html>, groundingAttribution: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GroundingAttribution>, groundingChunks: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GroundingChunk>, groundingSupports: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GroundingSupport> )` |

| ### Public properties |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GroundingAttribution>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GroundingMetadata#groundingAttribution()` **This property is deprecated.** Use groundingChunks instead |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GroundingChunk>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GroundingMetadata#groundingChunks()` The list of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GroundingChunk` classes. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GroundingSupport>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GroundingMetadata#groundingSupports()` The list of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GroundingSupport` objects. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GroundingMetadata#retrievalQueries()` |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/SearchEntryPoint?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GroundingMetadata#searchEntryPoint()` Google Search entry point for web searches. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GroundingMetadata#webSearchQueries()` The list of web search queries that the model performed to gather the grounding information. |

## Public constructors

### GroundingMetadata

```
GroundingMetadata(
    webSearchQueries: List<String>,
    searchEntryPoint: SearchEntryPoint?,
    retrievalQueries: List<String>,
    groundingAttribution: List<GroundingAttribution>,
    groundingChunks: List<GroundingChunk>,
    groundingSupports: List<GroundingSupport>
)
```

## Public properties

### groundingAttribution

```
val groundingAttribution: List<GroundingAttribution>
```

> [!CAUTION]
> **This property is deprecated.**   
> Use groundingChunks instead

### groundingChunks

```
val groundingChunks: List<GroundingChunk>
```

The list of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GroundingChunk` classes. Each chunk represents a piece of retrieved content that the model used to ground its response.

### groundingSupports

```
val groundingSupports: List<GroundingSupport>
```

The list of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GroundingSupport` objects. Each object details how specific segments of the model's response are supported by the `groundingChunks`.

### retrievalQueries

```
val retrievalQueries: List<String>
```

### searchEntryPoint

```
val searchEntryPoint: SearchEntryPoint?
```

Google Search entry point for web searches. This contains an HTML/CSS snippet that **must** be embedded in an app to display a Google Search Entry point for follow-up web searches related to the model's "Grounded Response".

### webSearchQueries

```
val webSearchQueries: List<String>
```

The list of web search queries that the model performed to gather the grounding information. These can be used to allow users to explore the search results themselves.