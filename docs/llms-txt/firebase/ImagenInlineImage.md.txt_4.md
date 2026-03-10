# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/ImagenInlineImage.md.txt

# ImagenInlineImage

# ImagenInlineImage


```
@PublicPreviewAPI
class ImagenInlineImage
```

<br />

*** ** * ** ***

> [!CAUTION]
> **This class is deprecated.**   
> The Vertex AI in Firebase SDK (firebase-vertexai) has been replaced with the FirebaseAI SDK (firebase-ai) to accommodate the evolving set of supported features and services. For migration details, see the migration guide: https://firebase.google.com/docs/vertex-ai/migrate-to-latest-sdk

Represents an Imagen-generated image that is returned as inline data.

## Summary

| ### Public functions |
|---|---|
| `https://developer.android.com/reference/kotlin/android/graphics/Bitmap.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/ImagenInlineImage#asBitmap()()` Returns the image as an Android OS native `https://developer.android.com/reference/kotlin/android/graphics/Bitmap.html` so that it can be saved or sent to the UI. |

| ### Public properties |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-byte-array/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/ImagenInlineImage#data()` The raw image bytes in JPEG or PNG format, as specified by `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/ImagenInlineImage#mimeType()`. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/ImagenInlineImage#mimeType()` The IANA standard MIME type of the image data; either `"image/png"` or `"image/jpeg"`; to request a different format, see `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/ImagenGenerationConfig#imageFormat()`. |

## Public functions

### asBitmap

```
fun asBitmap(): Bitmap
```

Returns the image as an Android OS native `https://developer.android.com/reference/kotlin/android/graphics/Bitmap.html` so that it can be saved or sent to the UI.

## Public properties

### data

```
val data: ByteArray
```

The raw image bytes in JPEG or PNG format, as specified by `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/ImagenInlineImage#mimeType()`.

### mimeType

```
val mimeType: String
```

The IANA standard MIME type of the image data; either `"image/png"` or `"image/jpeg"`; to request a different format, see `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/ImagenGenerationConfig#imageFormat()`.