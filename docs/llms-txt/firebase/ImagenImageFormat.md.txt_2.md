# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenImageFormat.md.txt

# ImagenImageFormat

# ImagenImageFormat


```
public final class ImagenImageFormat
```

<br />

*** ** * ** ***

Represents the format an image should be returned in.

## Summary

| ### Nested types |
|---|
| `public static class https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenImageFormat.Companion` |

| ### Public fields |
|---|---|
| `final https://developer.android.com/reference/kotlin/java/lang/Integer.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenImageFormat#compressionQuality()` an int (1-100) representing the quality of the image; a lower number means the image is permitted to be lower quality to reduce size. |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenImageFormat#mimeType()` A string (like `"image/jpeg"`) specifying the encoding MIME type of the image. |

| ### Public methods |
|---|---|
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenImageFormat` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenImageFormat.Companion#jpeg(kotlin.Int)(https://developer.android.com/reference/kotlin/java/lang/Integer.html compressionQuality)` An `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenImageFormat` representing a JPEG image. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenImageFormat` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenImageFormat.Companion#png()()` An `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenImageFormat` representing a PNG image |

## Public fields

### compressionQuality

```
public final Integer compressionQuality
```

an int (1-100) representing the quality of the image; a lower number means the image is permitted to be lower quality to reduce size. This parameter is not relevant for every MIME type.

### mimeType

```
public final @NonNull String mimeType
```

A string (like `"image/jpeg"`) specifying the encoding MIME type of the image.

## Public methods

### jpeg

```
public static final @NonNull ImagenImageFormat jpeg(Integer compressionQuality)
```

An `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenImageFormat` representing a JPEG image.

| Parameters |
|---|---|
| `https://developer.android.com/reference/kotlin/java/lang/Integer.html compressionQuality` | an int (1-100) representing the quality of the image; a lower number means the image is permitted to be lower quality to reduce size. |

### png

```
public static final @NonNull ImagenImageFormat png()
```

An `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenImageFormat` representing a PNG image