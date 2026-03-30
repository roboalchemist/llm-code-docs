# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/ImagenGenerationConfig.md.txt

# ImagenGenerationConfig

# ImagenGenerationConfig


```
@PublicPreviewAPI
public final class ImagenGenerationConfig
```

<br />

*** ** * ** ***

> [!CAUTION]
> **This class is deprecated.**   
> The Vertex AI in Firebase SDK (firebase-vertexai) has been replaced with the FirebaseAI SDK (firebase-ai) to accommodate the evolving set of supported features and services. For migration details, see the migration guide: https://firebase.google.com/docs/vertex-ai/migrate-to-latest-sdk

## Summary

| ### Nested types |
|---|
| `public final class https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/ImagenGenerationConfig.Builder` **This class is deprecated.** The Vertex AI in Firebase SDK (firebase-vertexai) has been replaced with the FirebaseAI SDK (firebase-ai) to accommodate the evolving set of supported features and services. |
| `public static class https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/ImagenGenerationConfig.Companion` |

| ### Public fields |
|---|---|
| `final https://developer.android.com/reference/kotlin/java/lang/Boolean.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/ImagenGenerationConfig#addWatermark()` |
| `final https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/ImagenAspectRatio` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/ImagenGenerationConfig#aspectRatio()` |
| `final https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/ImagenImageFormat` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/ImagenGenerationConfig#imageFormat()` |
| `final https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/ImagenGenerationConfig#negativePrompt()` |
| `final https://developer.android.com/reference/kotlin/java/lang/Integer.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/ImagenGenerationConfig#numberOfImages()` |

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/ImagenGenerationConfig#ImagenGenerationConfig(kotlin.String,kotlin.Int,com.google.firebase.vertexai.type.ImagenAspectRatio,com.google.firebase.vertexai.type.ImagenImageFormat,kotlin.Boolean)( https://developer.android.com/reference/kotlin/java/lang/String.html negativePrompt, https://developer.android.com/reference/kotlin/java/lang/Integer.html numberOfImages, https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/ImagenAspectRatio aspectRatio, https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/ImagenImageFormat imageFormat, https://developer.android.com/reference/kotlin/java/lang/Boolean.html addWatermark )` |

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