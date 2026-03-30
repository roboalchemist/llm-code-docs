# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/java/ImagenModelFutures.md.txt

# ImagenModelFutures

# ImagenModelFutures


```
@PublicPreviewAPI
abstract class ImagenModelFutures
```

<br />

*** ** * ** ***

> [!CAUTION]
> **This class is deprecated.**   
> The Vertex AI in Firebase SDK (firebase-vertexai) has been replaced with the FirebaseAI SDK (firebase-ai) to accommodate the evolving set of supported features and services. For migration details, see the migration guide: https://firebase.google.com/docs/vertex-ai/migrate-to-latest-sdk

Wrapper class providing Java compatible methods for `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/ImagenModel`.

| See also |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/ImagenModel` |   |

## Summary

| ### Public companion functions |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/java/ImagenModelFutures` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/java/ImagenModelFutures.Companion#from(com.google.firebase.vertexai.ImagenModel)(model: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/ImagenModel)` |

| ### Public functions |
|---|---|
| `abstract https://firebase.google.com/docs/reference/kotlin/com/google/common/util/concurrent/ListenableFuture<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/ImagenGenerationResponse<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/ImagenInlineImage>>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/java/ImagenModelFutures#generateImages(kotlin.String)(prompt: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Generates an image, returning the result directly to the caller. |
| `abstract https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/ImagenModel` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/java/ImagenModelFutures#getImageModel()()` Returns the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/ImagenModel` object wrapped by this object. |

## Public companion functions

### from

```
fun from(model: ImagenModel): ImagenModelFutures
```

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/java/ImagenModelFutures` | a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/java/ImagenModelFutures` created around the provided `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/ImagenModel` |

## Public functions

### generateImages

```
abstract fun generateImages(prompt: String): ListenableFuture<ImagenGenerationResponse<ImagenInlineImage>>
```

Generates an image, returning the result directly to the caller.

| Parameters |
|---|---|
| `prompt: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The main text prompt from which the image is generated. |

### getImageModel

```
abstract fun getImageModel(): ImagenModel
```

Returns the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/ImagenModel` object wrapped by this object.