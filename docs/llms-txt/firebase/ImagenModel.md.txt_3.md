# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/ImagenModel.md.txt

# ImagenModel

# ImagenModel


```
class ImagenModel
```

<br />

*** ** * ** ***

Represents a generative model (like Imagen), capable of generating images based on various input types.

See the documentation for a list of [supported models](https://firebase.google.com/docs/ai-logic/models).

## Summary

| ### Public functions |
|---|---|
| `suspend https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenGenerationResponse<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenInlineImage>` | `@https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/PublicPreviewAPI https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/ImagenModel#editImage(kotlin.collections.List,kotlin.String,com.google.firebase.ai.type.ImagenEditingConfig)( referenceImages: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenReferenceImage>, prompt: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, config: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenEditingConfig? )` Generates an image from a single or set of base images, returning the result directly to the caller. |
| `suspend https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenGenerationResponse<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenInlineImage>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/ImagenModel#generateImages(kotlin.String)(prompt: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Generates an image, returning the result directly to the caller. |
| `suspend https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenGenerationResponse<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenInlineImage>` | `@https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/PublicPreviewAPI https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/ImagenModel#inpaintImage(com.google.firebase.ai.type.ImagenInlineImage,kotlin.String,com.google.firebase.ai.type.ImagenMaskReference,com.google.firebase.ai.type.ImagenEditingConfig)( image: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenInlineImage, prompt: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, mask: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenMaskReference, config: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenEditingConfig )` Generates an image by inpainting a masked off part of a base image. |
| `suspend https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenGenerationResponse<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenInlineImage>` | `@https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/PublicPreviewAPI https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/ImagenModel#outpaintImage(com.google.firebase.ai.type.ImagenInlineImage,com.google.firebase.ai.type.Dimensions,com.google.firebase.ai.type.ImagenImagePlacement,kotlin.String,com.google.firebase.ai.type.ImagenEditingConfig)( image: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenInlineImage, newDimensions: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Dimensions, newPosition: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenImagePlacement, prompt: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, config: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenEditingConfig? )` Generates an image by outpainting the given image, extending its content beyond the original borders using context from the original image, and optionally, the prompt. |

## Public functions

### editImage

```
@PublicPreviewAPI
suspend fun editImage(
    referenceImages: List<ImagenReferenceImage>,
    prompt: String,
    config: ImagenEditingConfig? = null
): ImagenGenerationResponse<ImagenInlineImage>
```

Generates an image from a single or set of base images, returning the result directly to the caller.

| Parameters |
|---|---|
| `referenceImages: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenReferenceImage>` | the image inputs given to the model as a prompt |
| `prompt: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | the text input given to the model as a prompt |
| `config: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenEditingConfig? = null` | the editing configuration settings |

### generateImages

```
suspend fun generateImages(prompt: String): ImagenGenerationResponse<ImagenInlineImage>
```

Generates an image, returning the result directly to the caller.

| Parameters |
|---|---|
| `prompt: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The input(s) given to the model as a prompt. |

### inpaintImage

```
@PublicPreviewAPI
suspend fun inpaintImage(
    image: ImagenInlineImage,
    prompt: String,
    mask: ImagenMaskReference,
    config: ImagenEditingConfig
): ImagenGenerationResponse<ImagenInlineImage>
```

Generates an image by inpainting a masked off part of a base image. Inpainting is the process of filling in missing or masked off parts of the image using context from the original image and prompt.

| Parameters |
|---|---|
| `image: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenInlineImage` | the base image |
| `prompt: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | the text input given to the model as a prompt |
| `mask: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenMaskReference` | the mask which defines where in the image can be painted by Imagen. |
| `config: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenEditingConfig` | the editing configuration settings, it should include an `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenEditMode` |

### outpaintImage

```
@PublicPreviewAPI
suspend fun outpaintImage(
    image: ImagenInlineImage,
    newDimensions: Dimensions,
    newPosition: ImagenImagePlacement = ImagenImagePlacement.CENTER,
    prompt: String = "",
    config: ImagenEditingConfig? = null
): ImagenGenerationResponse<ImagenInlineImage>
```

Generates an image by outpainting the given image, extending its content beyond the original borders using context from the original image, and optionally, the prompt.

| Parameters |
|---|---|
| `image: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenInlineImage` | the base image |
| `newDimensions: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Dimensions` | the new dimensions for the image, *must* be larger than the original image. |
| `newPosition: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenImagePlacement = ImagenImagePlacement.CENTER` | the placement of the base image within the new image. This can either be coordinates (0,0 is the top left corner) or an alignment (ex: `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenImagePlacement.Companion#BOTTOM_CENTER()`) |
| `prompt: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html = ""` | optional, can be used to specify the background generated if context is insufficient |
| `config: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenEditingConfig? = null` | the editing configuration settings |

| See also |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenMaskReference.Companion#generateMaskAndPadForOutpainting(com.google.firebase.ai.type.ImagenInlineImage,com.google.firebase.ai.type.Dimensions,com.google.firebase.ai.type.ImagenImagePlacement)` |   |