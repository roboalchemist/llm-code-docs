# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/ImagenModelFutures.md.txt

# ImagenModelFutures

# ImagenModelFutures


```
@PublicPreviewAPI
abstract class ImagenModelFutures
```

<br />

*** ** * ** ***

Wrapper class providing Java compatible methods for `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/ImagenModel`.

| See also |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/ImagenModel` |   |

## Summary

| ### Public companion functions |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/ImagenModelFutures` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/ImagenModelFutures.Companion#from(com.google.firebase.ai.ImagenModel)(model: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/ImagenModel)` |

| ### Public functions |
|---|---|
| `abstract https://firebase.google.com/docs/reference/kotlin/com/google/common/util/concurrent/ListenableFuture<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenGenerationResponse<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenInlineImage>>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/ImagenModelFutures#editImage(kotlin.collections.List,kotlin.String)(referenceImages: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenReferenceImage>, prompt: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Generates an image from a single or set of base images, returning the result directly to the caller. |
| `abstract https://firebase.google.com/docs/reference/kotlin/com/google/common/util/concurrent/ListenableFuture<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenGenerationResponse<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenInlineImage>>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/ImagenModelFutures#editImage(kotlin.collections.List,kotlin.String,com.google.firebase.ai.type.ImagenEditingConfig)( referenceImages: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenReferenceImage>, prompt: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, config: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenEditingConfig? )` Generates an image from a single or set of base images, returning the result directly to the caller. |
| `abstract https://firebase.google.com/docs/reference/kotlin/com/google/common/util/concurrent/ListenableFuture<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenGenerationResponse<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenInlineImage>>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/ImagenModelFutures#generateImages(kotlin.String)(prompt: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Generates an image, returning the result directly to the caller. |
| `abstract https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/ImagenModel` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/ImagenModelFutures#getImageModel()()` Returns the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/ImagenModel` object wrapped by this object. |
| `abstract https://firebase.google.com/docs/reference/kotlin/com/google/common/util/concurrent/ListenableFuture<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenGenerationResponse<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenInlineImage>>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/ImagenModelFutures#inpaintImage(com.google.firebase.ai.type.ImagenInlineImage,kotlin.String,com.google.firebase.ai.type.ImagenMaskReference,com.google.firebase.ai.type.ImagenEditingConfig)( image: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenInlineImage, prompt: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, mask: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenMaskReference, config: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenEditingConfig )` Generates an image by inpainting a masked off part of a base image. |
| `abstract https://firebase.google.com/docs/reference/kotlin/com/google/common/util/concurrent/ListenableFuture<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenGenerationResponse<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenInlineImage>>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/ImagenModelFutures#outpaintImage(com.google.firebase.ai.type.ImagenInlineImage,com.google.firebase.ai.type.Dimensions,com.google.firebase.ai.type.ImagenImagePlacement,kotlin.String,com.google.firebase.ai.type.ImagenEditingConfig)( image: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenInlineImage, newDimensions: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Dimensions, newPosition: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenImagePlacement, prompt: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, config: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenEditingConfig? )` Generates an image by outpainting the image, extending its borders |

## Public companion functions

### from

```
fun from(model: ImagenModel): ImagenModelFutures
```

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/ImagenModelFutures` | a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/ImagenModelFutures` created around the provided `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/ImagenModel` |

## Public functions

### editImage

```
abstract fun editImage(referenceImages: List<ImagenReferenceImage>, prompt: String): ListenableFuture<ImagenGenerationResponse<ImagenInlineImage>>
```

Generates an image from a single or set of base images, returning the result directly to the caller.

| Parameters |
|---|---|
| `referenceImages: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenReferenceImage>` | the image inputs given to the model as a prompt |
| `prompt: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | the text input given to the model as a prompt |

### editImage

```
abstract fun editImage(
    referenceImages: List<ImagenReferenceImage>,
    prompt: String,
    config: ImagenEditingConfig? = null
): ListenableFuture<ImagenGenerationResponse<ImagenInlineImage>>
```

Generates an image from a single or set of base images, returning the result directly to the caller.

| Parameters |
|---|---|
| `referenceImages: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenReferenceImage>` | the image inputs given to the model as a prompt |
| `prompt: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | the text input given to the model as a prompt |
| `config: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenEditingConfig? = null` | the editing configuration settings |

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

Returns the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/ImagenModel` object wrapped by this object.

### inpaintImage

```
abstract fun inpaintImage(
    image: ImagenInlineImage,
    prompt: String,
    mask: ImagenMaskReference,
    config: ImagenEditingConfig
): ListenableFuture<ImagenGenerationResponse<ImagenInlineImage>>
```

Generates an image by inpainting a masked off part of a base image.

| Parameters |
|---|---|
| `image: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenInlineImage` | the base image |
| `prompt: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | the text input given to the model as a prompt |
| `mask: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenMaskReference` | the mask which defines where in the image can be painted by imagen. |
| `config: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenEditingConfig` | the editing configuration settings, it should include an `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenEditMode` |

### outpaintImage

```
abstract fun outpaintImage(
    image: ImagenInlineImage,
    newDimensions: Dimensions,
    newPosition: ImagenImagePlacement = ImagenImagePlacement.CENTER,
    prompt: String = "",
    config: ImagenEditingConfig? = null
): ListenableFuture<ImagenGenerationResponse<ImagenInlineImage>>
```

Generates an image by outpainting the image, extending its borders

| Parameters |
|---|---|
| `image: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenInlineImage` | the base image |
| `newDimensions: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Dimensions` | the new dimensions for the image, *must* be larger than the original image. |
| `newPosition: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenImagePlacement = ImagenImagePlacement.CENTER` | the placement of the base image within the new image. This can either be coordinates (0,0 is the top left corner) or an alignment (ex: `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenImagePlacement.Companion#BOTTOM_CENTER()`) |
| `prompt: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html = ""` | optional, but can be used to specify the background generated if context is insufficient |
| `config: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenEditingConfig? = null` | the editing configuration settings |

| See also |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenMaskReference.Companion#generateMaskAndPadForOutpainting(com.google.firebase.ai.type.ImagenInlineImage,com.google.firebase.ai.type.Dimensions,com.google.firebase.ai.type.ImagenImagePlacement)` |   |