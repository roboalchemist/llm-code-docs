# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/ImagenImageFormat.Companion.md.txt

# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenImageFormat.Companion.md.txt

# ImagenImageFormat.Companion

# ImagenImageFormat.Companion


```
public static class ImagenImageFormat.Companion
```

<br />

*** ** * ** ***

## Summary

|                                                                                                         ### Public methods                                                                                                         |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `static final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[ImagenImageFormat](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenImageFormat) | [jpeg](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenImageFormat.Companion#jpeg(kotlin.Int))`(`[Integer](https://developer.android.com/reference/kotlin/java/lang/Integer.html)` compressionQuality)` An [ImagenImageFormat](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenImageFormat) representing a JPEG image. |
| `static final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[ImagenImageFormat](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenImageFormat) | [png](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenImageFormat.Companion#png())`()` An [ImagenImageFormat](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenImageFormat) representing a PNG image                                                                                                                    |

## Public methods

### jpeg

```
publicÂ staticÂ finalÂ @NonNull ImagenImageFormatÂ jpeg(IntegerÂ compressionQuality)
```

An [ImagenImageFormat](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenImageFormat) representing a JPEG image.  

|                                              Parameters                                               |
|-------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| [Integer](https://developer.android.com/reference/kotlin/java/lang/Integer.html)` compressionQuality` | an int (1-100) representing the quality of the image; a lower number means the image is permitted to be lower quality to reduce size. |

### png

```
publicÂ staticÂ finalÂ @NonNull ImagenImageFormatÂ png()
```

An [ImagenImageFormat](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenImageFormat) representing a PNG image