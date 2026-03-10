# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenGenerationConfig.md.txt

# ImagenGenerationConfig

# ImagenGenerationConfig


```
public final class ImagenGenerationConfig
```

<br />

*** ** * ** ***

## Summary

| ### Nested types |
|---|
| `public final class https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenGenerationConfig.Builder` Builder for creating a `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenGenerationConfig`. |
| `public static class https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenGenerationConfig.Companion` |

| ### Public fields |
|---|---|
| `final https://developer.android.com/reference/kotlin/java/lang/Boolean.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenGenerationConfig#addWatermark()` |
| `final https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenAspectRatio` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenGenerationConfig#aspectRatio()` |
| `final https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenImageFormat` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenGenerationConfig#imageFormat()` |
| `final https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenGenerationConfig#negativePrompt()` |
| `final https://developer.android.com/reference/kotlin/java/lang/Integer.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenGenerationConfig#numberOfImages()` |

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenGenerationConfig#ImagenGenerationConfig(kotlin.String,kotlin.Int,com.google.firebase.ai.type.ImagenAspectRatio,com.google.firebase.ai.type.ImagenImageFormat,kotlin.Boolean)( https://developer.android.com/reference/kotlin/java/lang/String.html negativePrompt, https://developer.android.com/reference/kotlin/java/lang/Integer.html numberOfImages, https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenAspectRatio aspectRatio, https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenImageFormat imageFormat, https://developer.android.com/reference/kotlin/java/lang/Boolean.html addWatermark )` |

## Public fields

### addWatermark

```
public final Boolean addWatermark
```

### aspectRatio

```
public final ImagenAspectRatio aspectRatio
```

### imageFormat

```
public final ImagenImageFormat imageFormat
```

### negativePrompt

```
public final String negativePrompt
```

### numberOfImages

```
public final Integer numberOfImages
```

## Public constructors

### ImagenGenerationConfig

```
public ImagenGenerationConfig(
    String negativePrompt,
    Integer numberOfImages,
    ImagenAspectRatio aspectRatio,
    ImagenImageFormat imageFormat,
    Boolean addWatermark
)
```