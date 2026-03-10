# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/ImagenGenerationConfig.md.txt

# ImagenGenerationConfig

# ImagenGenerationConfig


```
@PublicPreviewAPI
class ImagenGenerationConfig
```

<br />

*** ** * ** ***

> [!CAUTION]
> **This class is deprecated.**   
> The Vertex AI in Firebase SDK (firebase-vertexai) has been replaced with the FirebaseAI SDK (firebase-ai) to accommodate the evolving set of supported features and services. For migration details, see the migration guide: https://firebase.google.com/docs/vertex-ai/migrate-to-latest-sdk

## Summary

| ### Nested types |
|---|
| `class https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/ImagenGenerationConfig.Builder` **This class is deprecated.** The Vertex AI in Firebase SDK (firebase-vertexai) has been replaced with the FirebaseAI SDK (firebase-ai) to accommodate the evolving set of supported features and services. |

| ### Public companion functions |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/ImagenGenerationConfig.Builder` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/ImagenGenerationConfig.Companion#builder()()` |

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/ImagenGenerationConfig#ImagenGenerationConfig(kotlin.String,kotlin.Int,com.google.firebase.vertexai.type.ImagenAspectRatio,com.google.firebase.vertexai.type.ImagenImageFormat,kotlin.Boolean)( negativePrompt: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?, numberOfImages: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html?, aspectRatio: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/ImagenAspectRatio?, imageFormat: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/ImagenImageFormat?, addWatermark: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html? )` |

| ### Public properties |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/ImagenGenerationConfig#addWatermark()` |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/ImagenAspectRatio?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/ImagenGenerationConfig#aspectRatio()` |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/ImagenImageFormat?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/ImagenGenerationConfig#imageFormat()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/ImagenGenerationConfig#negativePrompt()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/ImagenGenerationConfig#numberOfImages()` |

## Public companion functions

### builder

```
fun builder(): ImagenGenerationConfig.Builder
```

## Public constructors

### ImagenGenerationConfig

```
ImagenGenerationConfig(
    negativePrompt: String? = null,
    numberOfImages: Int? = 1,
    aspectRatio: ImagenAspectRatio? = null,
    imageFormat: ImagenImageFormat? = null,
    addWatermark: Boolean? = null
)
```

## Public properties

### addWatermark

```
val addWatermark: Boolean?
```

### aspectRatio

```
val aspectRatio: ImagenAspectRatio?
```

### imageFormat

```
val imageFormat: ImagenImageFormat?
```

### negativePrompt

```
val negativePrompt: String?
```

### numberOfImages

```
val numberOfImages: Int?
```