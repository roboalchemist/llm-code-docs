# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagePart.md.txt

# ImagePart

# ImagePart


```
class ImagePart : Part
```

<br />

*** ** * ** ***

Represents image data sent to and received from requests. The image is converted client-side to JPEG encoding at 80% quality before being sent to the server.

## Summary

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagePart#ImagePart(android.graphics.Bitmap)(image: https://developer.android.com/reference/kotlin/android/graphics/Bitmap.html)` |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagePart#ImagePart(android.graphics.Bitmap,kotlin.String)(image: https://developer.android.com/reference/kotlin/android/graphics/Bitmap.html, displayName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |

| ### Public properties |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagePart#displayName()` |
| `https://developer.android.com/reference/kotlin/android/graphics/Bitmap.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagePart#image()` |
| `open https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagePart#isThought()` |

## Public constructors

### ImagePart

```
ImagePart(image: Bitmap)
```

| Parameters |
|---|---|
| `image: https://developer.android.com/reference/kotlin/android/graphics/Bitmap.html` | `https://developer.android.com/reference/kotlin/android/graphics/Bitmap.html` to convert into a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Part` |

### ImagePart

```
ImagePart(image: Bitmap, displayName: String)
```

| Parameters |
|---|---|
| `image: https://developer.android.com/reference/kotlin/android/graphics/Bitmap.html` | `https://developer.android.com/reference/kotlin/android/graphics/Bitmap.html` to convert into a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Part` |

## Public properties

### displayName

```
val displayName: String?
```

### image

```
val image: Bitmap
```

### isThought

```
open val isThought: Boolean
```