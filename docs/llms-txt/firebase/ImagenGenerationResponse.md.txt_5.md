# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenGenerationResponse.md.txt

# ImagenGenerationResponse

# ImagenGenerationResponse


```
class ImagenGenerationResponse<T : Any?>
```

<br />

*** ** * ** ***

Represents a response from a call to `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/ImagenModel#generateImages(kotlin.String)`

## Summary

| ### Public properties |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenGenerationResponse#filteredReason()` if fewer images were generated than were requested, this field will contain the reason they were filtered out. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<T>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenGenerationResponse#images()` contains the generated images |

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