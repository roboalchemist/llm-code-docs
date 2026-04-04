# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/ImagenGenerationResponse.md.txt

# ImagenGenerationResponse

# ImagenGenerationResponse


```
@PublicPreviewAPI
public final class ImagenGenerationResponse<T extends Object>
```

<br />

*** ** * ** ***

> [!CAUTION]
> **This class is deprecated.**   
> The Vertex AI in Firebase SDK (firebase-vertexai) has been replaced with the FirebaseAI SDK (firebase-ai) to accommodate the evolving set of supported features and services. For migration details, see the migration guide: https://firebase.google.com/docs/vertex-ai/migrate-to-latest-sdk

Represents a response from a call to `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/ImagenModel#generateImages(kotlin.String)`

## Summary

| ### Public fields |
|---|---|
| `final https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/ImagenGenerationResponse#filteredReason()` if fewer images were generated than were requested, this field will contain the reason they were filtered out. |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html T>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/ImagenGenerationResponse#images()` contains the generated images |

## Public fields

### filteredReason

```
public final String filteredReason
```

if fewer images were generated than were requested, this field will contain the reason they were filtered out.

### images

```
public final @NonNull List<@NonNull T> images
```

contains the generated images