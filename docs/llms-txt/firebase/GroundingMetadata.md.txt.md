# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GroundingMetadata.md.txt

# GroundingMetadata

# GroundingMetadata


```
public final class GroundingMetadata
```

<br />

*** ** * ** ***

Metadata returned to the client when grounding is enabled.

If using grounding with Google Search, you are required to comply with the "Grounding with Google Search" usage requirements for your chosen API provider: [Gemini Developer API](https://ai.google.dev/gemini-api/terms#grounding-with-google-search) or Vertex AI Gemini API (see [Service Terms](https://cloud.google.com/terms/service-terms) section within the Service Specific Terms).

## Summary

| ### Public fields |
|---|---|
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GroundingAttribution>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GroundingMetadata#groundingAttribution()` **This field is deprecated.** Use groundingChunks instead |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GroundingChunk>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GroundingMetadata#groundingChunks()` The list of `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GroundingChunk` classes. |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GroundingSupport>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GroundingMetadata#groundingSupports()` The list of `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GroundingSupport` objects. |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GroundingMetadata#retrievalQueries()` |
| `final https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/SearchEntryPoint` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GroundingMetadata#searchEntryPoint()` Google Search entry point for web searches. |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GroundingMetadata#webSearchQueries()` The list of web search queries that the model performed to gather the grounding information. |

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GroundingMetadata#GroundingMetadata(kotlin.collections.List,com.google.firebase.ai.type.SearchEntryPoint,kotlin.collections.List,kotlin.collections.List,kotlin.collections.List,kotlin.collections.List)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html> webSearchQueries, https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/SearchEntryPoint searchEntryPoint, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html> retrievalQueries, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GroundingAttribution> groundingAttribution, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GroundingChunk> groundingChunks, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GroundingSupport> groundingSupports )` |

## Public fields

### groundingAttribution

```
public final @NonNull List<@NonNull GroundingAttribution> groundingAttribution
```

> [!CAUTION]
> **This field is deprecated.**   
> Use groundingChunks instead

### groundingChunks

```
public final @NonNull List<@NonNull GroundingChunk> groundingChunks
```

The list of `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GroundingChunk` classes. Each chunk represents a piece of retrieved content that the model used to ground its response.

### groundingSupports

```
public final @NonNull List<@NonNull GroundingSupport> groundingSupports
```

The list of `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GroundingSupport` objects. Each object details how specific segments of the model's response are supported by the `groundingChunks`.

### retrievalQueries

```
public final @NonNull List<@NonNull String> retrievalQueries
```

### searchEntryPoint

```
public final SearchEntryPoint searchEntryPoint
```

Google Search entry point for web searches. This contains an HTML/CSS snippet that **must** be embedded in an app to display a Google Search Entry point for follow-up web searches related to the model's "Grounded Response".

### webSearchQueries

```
public final @NonNull List<@NonNull String> webSearchQueries
```

The list of web search queries that the model performed to gather the grounding information. These can be used to allow users to explore the search results themselves.

## Public constructors

### GroundingMetadata

```
public GroundingMetadata(
    @NonNull List<@NonNull String> webSearchQueries,
    SearchEntryPoint searchEntryPoint,
    @NonNull List<@NonNull String> retrievalQueries,
    @NonNull List<@NonNull GroundingAttribution> groundingAttribution,
    @NonNull List<@NonNull GroundingChunk> groundingChunks,
    @NonNull List<@NonNull GroundingSupport> groundingSupports
)
```