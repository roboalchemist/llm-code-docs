# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenGenerationConfig.Builder.md.txt

# ImagenGenerationConfig.Builder

# ImagenGenerationConfig.Builder


```
class ImagenGenerationConfig.Builder
```

<br />

*** ** * ** ***

Builder for creating a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenGenerationConfig`.

This is mainly intended for Java interop. For Kotlin, use `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/package-summary#imagenGenerationConfig(kotlin.Function1)` for a more idiomatic experience.

## Summary

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenGenerationConfig.Builder#Builder()()` |

| ### Public functions |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenGenerationConfig` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenGenerationConfig.Builder#build()()` Alternative casing for `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenGenerationConfig.Builder`: |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenGenerationConfig.Builder` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenGenerationConfig.Builder#setAddWatermark(kotlin.Boolean)(addWatermark: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` See `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenGenerationConfig#addWatermark()`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenGenerationConfig.Builder` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenGenerationConfig.Builder#setAspectRatio(com.google.firebase.ai.type.ImagenAspectRatio)(aspectRatio: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenAspectRatio)` See `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenGenerationConfig#aspectRatio()`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenGenerationConfig.Builder` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenGenerationConfig.Builder#setImageFormat(com.google.firebase.ai.type.ImagenImageFormat)(imageFormat: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenImageFormat)` See `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenGenerationConfig#imageFormat()`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenGenerationConfig.Builder` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenGenerationConfig.Builder#setNegativePrompt(kotlin.String)(negativePrompt: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` See `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenGenerationConfig#negativePrompt()`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenGenerationConfig.Builder` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenGenerationConfig.Builder#setNumberOfImages(kotlin.Int)(numberOfImages: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` See `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenGenerationConfig#numberOfImages()`. |

| ### Public properties |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenGenerationConfig.Builder#addWatermark()` |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenAspectRatio?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenGenerationConfig.Builder#aspectRatio()` |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenImageFormat?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenGenerationConfig.Builder#imageFormat()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenGenerationConfig.Builder#negativePrompt()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenGenerationConfig.Builder#numberOfImages()` |

## Public constructors

### Builder

```
Builder()
```

## Public functions

### build

```
fun build(): ImagenGenerationConfig
```

Alternative casing for `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenGenerationConfig.Builder`:

```kotlin
val config = GenerationConfig.builder()
```

### setAddWatermark

```
fun setAddWatermark(addWatermark: Boolean): ImagenGenerationConfig.Builder
```

See `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenGenerationConfig#addWatermark()`.

### setAspectRatio

```
fun setAspectRatio(aspectRatio: ImagenAspectRatio): ImagenGenerationConfig.Builder
```

See `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenGenerationConfig#aspectRatio()`.

### setImageFormat

```
fun setImageFormat(imageFormat: ImagenImageFormat): ImagenGenerationConfig.Builder
```

See `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenGenerationConfig#imageFormat()`.

### setNegativePrompt

```
fun setNegativePrompt(negativePrompt: String): ImagenGenerationConfig.Builder
```

See `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenGenerationConfig#negativePrompt()`.

### setNumberOfImages

```
fun setNumberOfImages(numberOfImages: Int): ImagenGenerationConfig.Builder
```

See `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenGenerationConfig#numberOfImages()`.

## Public properties

### addWatermark

```
var addWatermark: Boolean?
```

### aspectRatio

```
var aspectRatio: ImagenAspectRatio?
```

### imageFormat

```
var imageFormat: ImagenImageFormat?
```

### negativePrompt

```
var negativePrompt: String?
```

### numberOfImages

```
var numberOfImages: Int?
```