# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/ImagenGenerationConfig.md.txt

# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenGenerationConfig.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/ImagenGenerationConfig.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/ImagenGenerationConfig.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/ImagenGenerationConfig.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenGenerationConfig.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/ImagenGenerationConfig.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/ImagenGenerationConfig.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenGenerationConfig.md.txt

# ImagenGenerationConfig


```
class ImagenGenerationConfig
```

<br />

*** ** * ** ***

## Summary

|                                                                                                                                               ### Nested types                                                                                                                                                |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `class `[ImagenGenerationConfig.Builder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenGenerationConfig.Builder) Builder for creating a [ImagenGenerationConfig](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenGenerationConfig). |

|                                                         ### Public companion functions                                                         |
|------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| [ImagenGenerationConfig.Builder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenGenerationConfig.Builder) | [builder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenGenerationConfig.Companion#builder())`()` |

|                                                                                                                                                                                                                                                                                                                                                                                                                                       ### Public constructors                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [ImagenGenerationConfig](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenGenerationConfig#ImagenGenerationConfig(kotlin.String,kotlin.Int,com.google.firebase.ai.type.ImagenAspectRatio,com.google.firebase.ai.type.ImagenImageFormat,kotlin.Boolean))`(` ` negativePrompt: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?,` ` numberOfImages: `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)`?,` ` aspectRatio: `[ImagenAspectRatio](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenAspectRatio)`?,` ` imageFormat: `[ImagenImageFormat](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenImageFormat)`?,` ` addWatermark: `[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)`?` `)` |

|                                                  ### Public properties                                                  |
|-------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)`?`                                   | [addWatermark](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenGenerationConfig#addWatermark())     |
| [ImagenAspectRatio](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenAspectRatio)`?` | [aspectRatio](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenGenerationConfig#aspectRatio())       |
| [ImagenImageFormat](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenImageFormat)`?` | [imageFormat](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenGenerationConfig#imageFormat())       |
| [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?`                                     | [negativePrompt](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenGenerationConfig#negativePrompt()) |
| [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)`?`                                           | [numberOfImages](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenGenerationConfig#numberOfImages()) |

## Public companion functions

### builder

```
funÂ builder():Â ImagenGenerationConfig.Builder
```  

## Public constructors

### ImagenGenerationConfig

```
ImagenGenerationConfig(
Â Â Â Â negativePrompt:Â String? = null,
Â Â Â Â numberOfImages:Â Int? = 1,
Â Â Â Â aspectRatio:Â ImagenAspectRatio? = null,
Â Â Â Â imageFormat:Â ImagenImageFormat? = null,
Â Â Â Â addWatermark:Â Boolean? = null
)
```  

## Public properties

### addWatermark

```
valÂ addWatermark:Â Boolean?
```  

### aspectRatio

```
valÂ aspectRatio:Â ImagenAspectRatio?
```  

### imageFormat

```
valÂ imageFormat:Â ImagenImageFormat?
```  

### negativePrompt

```
valÂ negativePrompt:Â String?
```  

### numberOfImages

```
valÂ numberOfImages:Â Int?
```