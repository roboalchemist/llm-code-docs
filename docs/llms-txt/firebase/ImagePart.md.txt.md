# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/ImagePart.md.txt

# ImagePart

# ImagePart


```
public final class ImagePart implements Part
```

<br />

*** ** * ** ***

> [!CAUTION]
> **This class is deprecated.**   
> The Vertex AI in Firebase SDK (firebase-vertexai) has been replaced with the FirebaseAI SDK (firebase-ai) to accommodate the evolving set of supported features and services. For migration details, see the migration guide: https://firebase.google.com/docs/vertex-ai/migrate-to-latest-sdk

Represents image data sent to and received from requests. The image is converted client-side to JPEG encoding at 80% quality before being sent to the server.

## Summary

| ### Public fields |
|---|---|
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/android/graphics/Bitmap.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/ImagePart#image()` `https://developer.android.com/reference/kotlin/android/graphics/Bitmap.html` to convert into a `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Part` |

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/ImagePart#ImagePart(android.graphics.Bitmap)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/android/graphics/Bitmap.html image)` |

## Public fields

### image

```
public final @NonNull Bitmap image
```

`https://developer.android.com/reference/kotlin/android/graphics/Bitmap.html` to convert into a `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Part`

## Public constructors

### ImagePart

```
public ImagePart(@NonNull Bitmap image)
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/android/graphics/Bitmap.html image` | `https://developer.android.com/reference/kotlin/android/graphics/Bitmap.html` to convert into a `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Part` |