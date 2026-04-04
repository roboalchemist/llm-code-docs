# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/ImagenImageFormat.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/ImagenImageFormat.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/ImagenImageFormat.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/ImagenImageFormat.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenImageFormat.md.txt

# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenImageFormat.md.txt

# ImagenImageFormat


```
public final class ImagenImageFormat
```

<br />

*** ** * ** ***

Represents the format an image should be returned in.

## Summary

|                                                                        ### Nested types                                                                         |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `public static class `[ImagenImageFormat.Companion](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenImageFormat.Companion) |

|                                                                                  ### Public fields                                                                                   |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `final `[Integer](https://developer.android.com/reference/kotlin/java/lang/Integer.html)                                                                                             | [compressionQuality](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenImageFormat#compressionQuality()) an int (1-100) representing the quality of the image; a lower number means the image is permitted to be lower quality to reduce size. |
| `final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[String](https://developer.android.com/reference/kotlin/java/lang/String.html) | [mimeType](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenImageFormat#mimeType()) A string (like `"image/jpeg"`) specifying the encoding MIME type of the image.                                                                            |

|                                                                                                         ### Public methods                                                                                                         |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `static final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[ImagenImageFormat](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenImageFormat) | [jpeg](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenImageFormat.Companion#jpeg(kotlin.Int))`(`[Integer](https://developer.android.com/reference/kotlin/java/lang/Integer.html)` compressionQuality)` An [ImagenImageFormat](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenImageFormat) representing a JPEG image. |
| `static final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[ImagenImageFormat](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenImageFormat) | [png](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenImageFormat.Companion#png())`()` An [ImagenImageFormat](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenImageFormat) representing a PNG image                                                                                                                    |

## Public fields

### compressionQuality

```
publicÂ finalÂ IntegerÂ compressionQuality
```

an int (1-100) representing the quality of the image; a lower number means the image is permitted to be lower quality to reduce size. This parameter is not relevant for every MIME type.  

### mimeType

```
publicÂ finalÂ @NonNull StringÂ mimeType
```

A string (like `"image/jpeg"`) specifying the encoding MIME type of the image.  

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