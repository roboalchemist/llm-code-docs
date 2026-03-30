# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenGenerationConfigKt.md.txt

# ImagenGenerationConfigKt

# ImagenGenerationConfigKt


```
public final class ImagenGenerationConfigKt
```

<br />

*** ** * ** ***

## Summary

| ### Public methods |
|---|---|
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenGenerationConfig` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenGenerationConfigKt#imagenGenerationConfig(kotlin.Function1)( @https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-extension-function-type/index.html @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html Function1<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenGenerationConfig.Builder, https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html> init )` Helper method to construct a `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenGenerationConfig` in a DSL-like manner. |

## Public methods

### imagenGenerationConfig

```
public static final @NonNull ImagenGenerationConfig imagenGenerationConfig(
    @ExtensionFunctionType @NonNull Function1<@NonNull ImagenGenerationConfig.Builder, Unit> init
)
```

Helper method to construct a `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenGenerationConfig` in a DSL-like manner.

Example Usage:

```
imagenGenerationConfig {
  negativePrompt = "People, black and white, painting"
  numberOfImages = 1
  aspectRatio = ImagenAspecRatio.SQUARE_1x1
  imageFormat = ImagenImageFormat.png()
  addWatermark = false
}
```