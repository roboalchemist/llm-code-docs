# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/ImagenGenerationConfig.Builder.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/ImagenGenerationConfig.Builder.md.txt

# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenGenerationConfig.Builder.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenGenerationConfig.Builder.md.txt

# ImagenGenerationConfig.Builder

# ImagenGenerationConfig.Builder


```
class ImagenGenerationConfig.Builder
```

<br />

*** ** * ** ***

Builder for creating a [ImagenGenerationConfig](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenGenerationConfig).

This is mainly intended for Java interop. For Kotlin, use [imagenGenerationConfig](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/package-summary#imagenGenerationConfig(kotlin.Function1)) for a more idiomatic experience.

## Summary

|                                                        ### Public constructors                                                        |
|---------------------------------------------------------------------------------------------------------------------------------------|
| [Builder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenGenerationConfig.Builder#Builder())`()` |

|                                                              ### Public functions                                                              |
|------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [ImagenGenerationConfig](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenGenerationConfig)                 | [build](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenGenerationConfig.Builder#build())`()` Alternative casing for [ImagenGenerationConfig.Builder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenGenerationConfig.Builder):                                                                                                                                                                                          |
| [ImagenGenerationConfig.Builder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenGenerationConfig.Builder) | [setAddWatermark](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenGenerationConfig.Builder#setAddWatermark(kotlin.Boolean))`(addWatermark: `[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)`)` See [ImagenGenerationConfig.addWatermark](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenGenerationConfig#addWatermark()).                                                             |
| [ImagenGenerationConfig.Builder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenGenerationConfig.Builder) | [setAspectRatio](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenGenerationConfig.Builder#setAspectRatio(com.google.firebase.ai.type.ImagenAspectRatio))`(aspectRatio: `[ImagenAspectRatio](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenAspectRatio)`)` See [ImagenGenerationConfig.aspectRatio](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenGenerationConfig#aspectRatio()). |
| [ImagenGenerationConfig.Builder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenGenerationConfig.Builder) | [setImageFormat](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenGenerationConfig.Builder#setImageFormat(com.google.firebase.ai.type.ImagenImageFormat))`(imageFormat: `[ImagenImageFormat](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenImageFormat)`)` See [ImagenGenerationConfig.imageFormat](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenGenerationConfig#imageFormat()). |
| [ImagenGenerationConfig.Builder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenGenerationConfig.Builder) | [setNegativePrompt](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenGenerationConfig.Builder#setNegativePrompt(kotlin.String))`(negativePrompt: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`)` See [ImagenGenerationConfig.negativePrompt](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenGenerationConfig#negativePrompt()).                                                      |
| [ImagenGenerationConfig.Builder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenGenerationConfig.Builder) | [setNumberOfImages](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenGenerationConfig.Builder#setNumberOfImages(kotlin.Int))`(numberOfImages: `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)`)` See [ImagenGenerationConfig.numberOfImages](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenGenerationConfig#numberOfImages()).                                                               |

|                                                  ### Public properties                                                  |
|-------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)`?`                                   | [addWatermark](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenGenerationConfig.Builder#addWatermark())     |
| [ImagenAspectRatio](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenAspectRatio)`?` | [aspectRatio](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenGenerationConfig.Builder#aspectRatio())       |
| [ImagenImageFormat](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenImageFormat)`?` | [imageFormat](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenGenerationConfig.Builder#imageFormat())       |
| [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?`                                     | [negativePrompt](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenGenerationConfig.Builder#negativePrompt()) |
| [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)`?`                                           | [numberOfImages](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenGenerationConfig.Builder#numberOfImages()) |

## Public constructors

### Builder

```
Builder()
```  

## Public functions

### build

```
funÂ build():Â ImagenGenerationConfig
```

Alternative casing for [ImagenGenerationConfig.Builder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenGenerationConfig.Builder):  

```kotlin
val config = GenerationConfig.builder()
```  

### setAddWatermark

```
funÂ setAddWatermark(addWatermark:Â Boolean):Â ImagenGenerationConfig.Builder
```

See [ImagenGenerationConfig.addWatermark](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenGenerationConfig#addWatermark()).  

### setAspectRatio

```
funÂ setAspectRatio(aspectRatio:Â ImagenAspectRatio):Â ImagenGenerationConfig.Builder
```

See [ImagenGenerationConfig.aspectRatio](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenGenerationConfig#aspectRatio()).  

### setImageFormat

```
funÂ setImageFormat(imageFormat:Â ImagenImageFormat):Â ImagenGenerationConfig.Builder
```

See [ImagenGenerationConfig.imageFormat](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenGenerationConfig#imageFormat()).  

### setNegativePrompt

```
funÂ setNegativePrompt(negativePrompt:Â String):Â ImagenGenerationConfig.Builder
```

See [ImagenGenerationConfig.negativePrompt](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenGenerationConfig#negativePrompt()).  

### setNumberOfImages

```
funÂ setNumberOfImages(numberOfImages:Â Int):Â ImagenGenerationConfig.Builder
```

See [ImagenGenerationConfig.numberOfImages](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenGenerationConfig#numberOfImages()).  

## Public properties

### addWatermark

```
varÂ addWatermark:Â Boolean?
```  

### aspectRatio

```
varÂ aspectRatio:Â ImagenAspectRatio?
```  

### imageFormat

```
varÂ imageFormat:Â ImagenImageFormat?
```  

### negativePrompt

```
varÂ negativePrompt:Â String?
```  

### numberOfImages

```
varÂ numberOfImages:Â Int?
```