# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/ImagenGenerationConfigKt.md.txt

# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenGenerationConfigKt.md.txt

# ImagenGenerationConfigKt


```
public final class ImagenGenerationConfigKt
```

<br />

*** ** * ** ***

## Summary

|                                                                                                              ### Public methods                                                                                                              |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `static final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[ImagenGenerationConfig](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenGenerationConfig) | [imagenGenerationConfig](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenGenerationConfigKt#imagenGenerationConfig(kotlin.Function1))`(` ` @`[ExtensionFunctionType](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-extension-function-type/index.html)` @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` Function1<@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[ImagenGenerationConfig.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenGenerationConfig.Builder)`, `[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)`> init` `)` Helper method to construct a [ImagenGenerationConfig](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenGenerationConfig) in a DSL-like manner. |

## Public methods

### imagenGenerationConfig

```
publicÂ staticÂ finalÂ @NonNull ImagenGenerationConfigÂ imagenGenerationConfig(
Â Â Â Â @ExtensionFunctionType @NonNull Function1<@NonNull ImagenGenerationConfig.Builder,Â Unit>Â init
)
```

Helper method to construct a [ImagenGenerationConfig](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenGenerationConfig) in a DSL-like manner.

Example Usage:  

```scdoc
imagenGenerationConfig {
  negativePrompt = "People, black and white, painting"
  numberOfImages = 1
  aspectRatio = ImagenAspecRatio.SQUARE_1x1
  imageFormat = ImagenImageFormat.png()
  addWatermark = false
}
```