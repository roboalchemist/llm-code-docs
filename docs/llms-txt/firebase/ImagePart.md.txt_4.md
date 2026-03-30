# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/ImagePart.md.txt

# ImagePart

# ImagePart


```
class ImagePart : Part
```

<br />

*** ** * ** ***

> [!CAUTION]
> **This class is deprecated.**   
> The Vertex AI in Firebase SDK (firebase-vertexai) has been replaced with the FirebaseAI SDK (firebase-ai) to accommodate the evolving set of supported features and services. For migration details, see the migration guide: https://firebase.google.com/docs/vertex-ai/migrate-to-latest-sdk

Represents image data sent to and received from requests. The image is converted client-side to JPEG encoding at 80% quality before being sent to the server.

## Summary

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/ImagePart#ImagePart(android.graphics.Bitmap)(image: https://developer.android.com/reference/kotlin/android/graphics/Bitmap.html)` |

| ### Public properties |
|---|---|
| `https://developer.android.com/reference/kotlin/android/graphics/Bitmap.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/ImagePart#image()` `https://developer.android.com/reference/kotlin/android/graphics/Bitmap.html` to convert into a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Part` |

## Public constructors

### ImagePart

```
ImagePart(image: Bitmap)
```

| Parameters |
|---|---|
| `image: https://developer.android.com/reference/kotlin/android/graphics/Bitmap.html` | `https://developer.android.com/reference/kotlin/android/graphics/Bitmap.html` to convert into a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Part` |

## Public properties

### image

```
val image: Bitmap
```

`https://developer.android.com/reference/kotlin/android/graphics/Bitmap.html` to convert into a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Part`