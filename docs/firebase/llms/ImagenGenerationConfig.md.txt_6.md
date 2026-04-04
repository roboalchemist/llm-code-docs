# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenGenerationConfig.md.txt

# ImagenGenerationConfig

# ImagenGenerationConfig


```
class ImagenGenerationConfig
```

<br />

*** ** * ** ***

## Summary

| ### Nested types |
|---|
| `class https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenGenerationConfig.Builder` Builder for creating a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenGenerationConfig`. |

| ### Public companion functions |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenGenerationConfig.Builder` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenGenerationConfig.Companion#builder()()` |

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenGenerationConfig#ImagenGenerationConfig(kotlin.String,kotlin.Int,com.google.firebase.ai.type.ImagenAspectRatio,com.google.firebase.ai.type.ImagenImageFormat,kotlin.Boolean)( negativePrompt: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?, numberOfImages: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html?, aspectRatio: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenAspectRatio?, imageFormat: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenImageFormat?, addWatermark: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html? )` |

| ### Public properties |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenGenerationConfig#addWatermark()` |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenAspectRatio?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenGenerationConfig#aspectRatio()` |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenImageFormat?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenGenerationConfig#imageFormat()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenGenerationConfig#negativePrompt()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenGenerationConfig#numberOfImages()` |

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