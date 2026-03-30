# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/java/ImagenModelFutures.md.txt

# ImagenModelFutures

# ImagenModelFutures


```
@PublicPreviewAPI
public abstract class ImagenModelFutures
```

<br />

*** ** * ** ***

> [!CAUTION]
> **This class is deprecated.**   
> The Vertex AI in Firebase SDK (firebase-vertexai) has been replaced with the FirebaseAI SDK (firebase-ai) to accommodate the evolving set of supported features and services. For migration details, see the migration guide: https://firebase.google.com/docs/vertex-ai/migrate-to-latest-sdk

Wrapper class providing Java compatible methods for `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/ImagenModel`.

| See also |
|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/ImagenModel` |   |

## Summary

| ### Nested types |
|---|
| `public static class https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/java/ImagenModelFutures.Companion` |

| ### Public methods |
|---|---|
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/java/ImagenModelFutures` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/java/ImagenModelFutures.Companion#from(com.google.firebase.vertexai.ImagenModel)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/ImagenModel model)` |
| `abstract @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/common/util/concurrent/ListenableFuture<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/ImagenGenerationResponse<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/ImagenInlineImage>>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/java/ImagenModelFutures#generateImages(kotlin.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html prompt)` Generates an image, returning the result directly to the caller. |
| `abstract @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/ImagenModel` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/java/ImagenModelFutures#getImageModel()()` Returns the `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/ImagenModel` object wrapped by this object. |

## Public methods

### from

```
public static final @NonNull ImagenModelFutures from(@NonNull ImagenModel model)
```

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/java/ImagenModelFutures` | a `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/java/ImagenModelFutures` created around the provided `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/ImagenModel` |

### generateImages

```
public abstract @NonNull ListenableFuture<@NonNull ImagenGenerationResponse<@NonNull ImagenInlineImage>> generateImages(@NonNull String prompt)
```

Generates an image, returning the result directly to the caller.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html prompt` | The main text prompt from which the image is generated. |

### getImageModel

```
public abstract @NonNull ImagenModel getImageModel()
```

Returns the `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/ImagenModel` object wrapped by this object.