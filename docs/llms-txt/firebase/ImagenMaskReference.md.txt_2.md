# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenMaskReference.md.txt

# ImagenMaskReference

# ImagenMaskReference


```
@PublicPreviewAPI
abstract class ImagenMaskReference : ImagenReferenceImage
```

<br />

|---|---|---|
| [kotlin.Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html) |||
| ↳ | [com.google.firebase.ai.type.ImagenReferenceImage](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenReferenceImage) ||
|   | ↳ | [com.google.firebase.ai.type.ImagenMaskReference](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenMaskReference) |

Known direct subclasses [ImagenBackgroundMask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenBackgroundMask), [ImagenForegroundMask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenForegroundMask), [ImagenRawMask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenRawMask), [ImagenSemanticMask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenSemanticMask)

|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenBackgroundMask` | A generated mask image which will auto-detect and mask out the background. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenForegroundMask` | A generated mask image which will auto-detect and mask out the foreground. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenRawMask` | Represents a mask for Imagen editing. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenSemanticMask` | Represents a generated mask for Imagen editing which masks out certain objects using object detection. |

*** ** * ** ***

Represents a mask for Imagen editing. This image (generated or provided) should contain only black and white pixels, with black representing parts of the image which should not change.

## Summary

| ### Public companion functions |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenReferenceImage>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenMaskReference.Companion#generateMaskAndPadForOutpainting(com.google.firebase.ai.type.ImagenInlineImage,com.google.firebase.ai.type.Dimensions,com.google.firebase.ai.type.ImagenImagePlacement)( image: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenInlineImage, newDimensions: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Dimensions, newPosition: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenImagePlacement )` Generates two reference images of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenRawImage` and `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenRawMask`. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenReferenceImage>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenMaskReference.Companion#generateMaskAndPadForOutpainting(com.google.firebase.ai.type.ImagenInlineImage,com.google.firebase.ai.type.Dimensions,com.google.firebase.ai.type.ImagenImagePlacement,kotlin.Double)( image: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenInlineImage, newDimensions: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Dimensions, newPosition: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenImagePlacement, dilation: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html )` Generates two reference images of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenRawImage` and `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenRawMask`. |

| ### Inherited properties |
|---|
| From [com.google.firebase.ai.type.ImagenReferenceImage](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenReferenceImage) |---|---| | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenInlineImage?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenReferenceImage#image()` | | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenReferenceImage#referenceId()` | |

## Public companion functions

### generateMaskAndPadForOutpainting

```
fun generateMaskAndPadForOutpainting(
    image: ImagenInlineImage,
    newDimensions: Dimensions,
    newPosition: ImagenImagePlacement = ImagenImagePlacement.CENTER
): List<ImagenReferenceImage>
```

Generates two reference images of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenRawImage` and `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenRawMask`. These images are generated in this order:

- One `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenRawImage` containing the original image, padded out to the new dimensions with black pixels, with the original image placed at the given placement

- One `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenRawMask` of the same dimensions containing white everywhere except at the placement original image. This is the format expected by Imagen for outpainting requests.

| Parameters |
|---|---|
| `image: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenInlineImage` | the original image |
| `newDimensions: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Dimensions` | the new dimensions for outpainting. These new dimensions *must* be more than the original image. |
| `newPosition: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenImagePlacement = ImagenImagePlacement.CENTER` | the placement of the original image within the new outpainted image. |

### generateMaskAndPadForOutpainting

```
fun generateMaskAndPadForOutpainting(
    image: ImagenInlineImage,
    newDimensions: Dimensions,
    newPosition: ImagenImagePlacement = ImagenImagePlacement.CENTER,
    dilation: Double = 0.01
): List<ImagenReferenceImage>
```

Generates two reference images of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenRawImage` and `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenRawMask`. These images are generated in this order:

- One `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenRawImage` containing the original image, padded out to the new dimensions with black pixels, with the original image placed at the given placement

- One `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenRawMask` of the same dimensions containing white everywhere except at the placement original image. This is the format expected by Imagen for outpainting requests.

| Parameters |
|---|---|
| `image: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenInlineImage` | the original image |
| `newDimensions: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Dimensions` | the new dimensions for outpainting. These new dimensions *must* be more than the original image. |
| `newPosition: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenImagePlacement = ImagenImagePlacement.CENTER` | the placement of the original image within the new outpainted image. |
| `dilation: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html = 0.01` | the dilation for the outpainting mask. See: `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenRawMask`. |