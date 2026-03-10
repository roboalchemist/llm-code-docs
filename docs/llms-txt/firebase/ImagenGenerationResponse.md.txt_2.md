# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenGenerationResponse.md.txt

# ImagenGenerationResponse

# ImagenGenerationResponse


```
public final class ImagenGenerationResponse<T extends Object>
```

<br />

*** ** * ** ***

Represents a response from a call to `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/ImagenModel#generateImages(kotlin.String)`

## Summary

| ### Public fields |
|---|---|
| `final https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenGenerationResponse#filteredReason()` if fewer images were generated than were requested, this field will contain the reason they were filtered out. |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html T>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenGenerationResponse#images()` contains the generated images |

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