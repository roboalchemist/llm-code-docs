# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/ImagenInlineImage.md.txt

# ImagenInlineImage

# ImagenInlineImage


```
@PublicPreviewAPI
public final class ImagenInlineImage
```

<br />

*** ** * ** ***

> [!CAUTION]
> **This class is deprecated.**   
> The Vertex AI in Firebase SDK (firebase-vertexai) has been replaced with the FirebaseAI SDK (firebase-ai) to accommodate the evolving set of supported features and services. For migration details, see the migration guide: https://firebase.google.com/docs/vertex-ai/migrate-to-latest-sdk

Represents an Imagen-generated image that is returned as inline data.

## Summary

| ### Public fields |
|---|---|
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html byte[]` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/ImagenInlineImage#data()` The raw image bytes in JPEG or PNG format, as specified by `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/ImagenInlineImage#mimeType()`. |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/ImagenInlineImage#mimeType()` The IANA standard MIME type of the image data; either `"image/png"` or `"image/jpeg"`; to request a different format, see `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/ImagenGenerationConfig#imageFormat()`. |

| ### Public methods |
|---|---|
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/android/graphics/Bitmap.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/ImagenInlineImage#asBitmap()()` Returns the image as an Android OS native `https://developer.android.com/reference/kotlin/android/graphics/Bitmap.html` so that it can be saved or sent to the UI. |

## Public fields

### data

```
public final @NonNull byte[] data
```

The raw image bytes in JPEG or PNG format, as specified by `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/ImagenInlineImage#mimeType()`.

### mimeType

```
public final @NonNull String mimeType
```

The IANA standard MIME type of the image data; either `"image/png"` or `"image/jpeg"`; to request a different format, see `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/ImagenGenerationConfig#imageFormat()`.

## Public methods

### asBitmap

```
public final @NonNull Bitmap asBitmap()
```

Returns the image as an Android OS native `https://developer.android.com/reference/kotlin/android/graphics/Bitmap.html` so that it can be saved or sent to the UI.