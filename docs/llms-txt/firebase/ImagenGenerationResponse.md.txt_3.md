# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/ImagenGenerationResponse.md.txt

# ImagenGenerationResponse

# ImagenGenerationResponse


```
@PublicPreviewAPI
class ImagenGenerationResponse<T : Any?>
```

<br />

*** ** * ** ***

> [!CAUTION]
> **This class is deprecated.**   
> The Vertex AI in Firebase SDK (firebase-vertexai) has been replaced with the FirebaseAI SDK (firebase-ai) to accommodate the evolving set of supported features and services. For migration details, see the migration guide: https://firebase.google.com/docs/vertex-ai/migrate-to-latest-sdk

Represents a response from a call to `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/ImagenModel#generateImages(kotlin.String)`

## Summary

| ### Public properties |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/ImagenGenerationResponse#filteredReason()` if fewer images were generated than were requested, this field will contain the reason they were filtered out. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<T>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/ImagenGenerationResponse#images()` contains the generated images |

## Public properties

### filteredReason

```
val filteredReason: String?
```

if fewer images were generated than were requested, this field will contain the reason they were filtered out.

### images

```
val images: List<T>
```

contains the generated images