# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenImageFormat.md.txt

# ImagenImageFormat

# ImagenImageFormat


```
class ImagenImageFormat
```

<br />

*** ** * ** ***

Represents the format an image should be returned in.

## Summary

| ### Public companion functions |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenImageFormat` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenImageFormat.Companion#jpeg(kotlin.Int)(compressionQuality: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html?)` An `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenImageFormat` representing a JPEG image. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenImageFormat` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenImageFormat.Companion#png()()` An `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenImageFormat` representing a PNG image |

| ### Public properties |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenImageFormat#compressionQuality()` an int (1-100) representing the quality of the image; a lower number means the image is permitted to be lower quality to reduce size. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenImageFormat#mimeType()` A string (like `"image/jpeg"`) specifying the encoding MIME type of the image. |

## Public companion functions

### jpeg

```
fun jpeg(compressionQuality: Int? = null): ImagenImageFormat
```

An `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenImageFormat` representing a JPEG image.

| Parameters |
|---|---|
| `compressionQuality: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html? = null` | an int (1-100) representing the quality of the image; a lower number means the image is permitted to be lower quality to reduce size. |

### png

```
fun png(): ImagenImageFormat
```

An `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenImageFormat` representing a PNG image

## Public properties

### compressionQuality

```
val compressionQuality: Int?
```

an int (1-100) representing the quality of the image; a lower number means the image is permitted to be lower quality to reduce size. This parameter is not relevant for every MIME type.

### mimeType

```
val mimeType: String
```

A string (like `"image/jpeg"`) specifying the encoding MIME type of the image.