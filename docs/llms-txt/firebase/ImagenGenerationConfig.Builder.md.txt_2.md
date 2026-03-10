# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenGenerationConfig.Builder.md.txt

# ImagenGenerationConfig.Builder

# ImagenGenerationConfig.Builder


```
public final class ImagenGenerationConfig.Builder
```

<br />

*** ** * ** ***

Builder for creating a `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenGenerationConfig`.

This is mainly intended for Java interop. For Kotlin, use `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/package-summary#imagenGenerationConfig(kotlin.Function1)` for a more idiomatic experience.

## Summary

| ### Public fields |
|---|---|
| `final https://developer.android.com/reference/kotlin/java/lang/Boolean.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenGenerationConfig.Builder#addWatermark()` |
| `final https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenAspectRatio` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenGenerationConfig.Builder#aspectRatio()` |
| `final https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenImageFormat` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenGenerationConfig.Builder#imageFormat()` |
| `final https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenGenerationConfig.Builder#negativePrompt()` |
| `final https://developer.android.com/reference/kotlin/java/lang/Integer.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenGenerationConfig.Builder#numberOfImages()` |

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenGenerationConfig.Builder#Builder()()` |

| ### Public methods |
|---|---|
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenGenerationConfig` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenGenerationConfig.Builder#build()()` Alternative casing for `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenGenerationConfig.Builder`: |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenGenerationConfig.Builder` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenGenerationConfig.Builder#setAddWatermark(kotlin.Boolean)(boolean addWatermark)` See `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenGenerationConfig#addWatermark()`. |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenGenerationConfig.Builder` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenGenerationConfig.Builder#setAspectRatio(com.google.firebase.ai.type.ImagenAspectRatio)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenAspectRatio aspectRatio)` See `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenGenerationConfig#aspectRatio()`. |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenGenerationConfig.Builder` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenGenerationConfig.Builder#setImageFormat(com.google.firebase.ai.type.ImagenImageFormat)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenImageFormat imageFormat)` See `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenGenerationConfig#imageFormat()`. |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenGenerationConfig.Builder` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenGenerationConfig.Builder#setNegativePrompt(kotlin.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html negativePrompt)` See `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenGenerationConfig#negativePrompt()`. |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenGenerationConfig.Builder` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenGenerationConfig.Builder#setNumberOfImages(kotlin.Int)(int numberOfImages)` See `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenGenerationConfig#numberOfImages()`. |

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

### Builder

```
public Builder()
```

## Public methods

### build

```
public final @NonNull ImagenGenerationConfig build()
```

Alternative casing for `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenGenerationConfig.Builder`:

```
val config = GenerationConfig.builder()
```

### setAddWatermark

```
public final @NonNull ImagenGenerationConfig.Builder setAddWatermark(boolean addWatermark)
```

See `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenGenerationConfig#addWatermark()`.

### setAspectRatio

```
public final @NonNull ImagenGenerationConfig.Builder setAspectRatio(@NonNull ImagenAspectRatio aspectRatio)
```

See `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenGenerationConfig#aspectRatio()`.

### setImageFormat

```
public final @NonNull ImagenGenerationConfig.Builder setImageFormat(@NonNull ImagenImageFormat imageFormat)
```

See `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenGenerationConfig#imageFormat()`.

### setNegativePrompt

```
public final @NonNull ImagenGenerationConfig.Builder setNegativePrompt(@NonNull String negativePrompt)
```

See `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenGenerationConfig#negativePrompt()`.

### setNumberOfImages

```
public final @NonNull ImagenGenerationConfig.Builder setNumberOfImages(int numberOfImages)
```

See `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenGenerationConfig#numberOfImages()`.