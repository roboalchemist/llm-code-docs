# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenMaskReference.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenMaskReference.md.txt

# ImagenMaskReference

# ImagenMaskReference


```
@PublicPreviewAPI
abstract class ImagenMaskReference : ImagenReferenceImage
```

<br />

|---|---|------------------------------------------------------------------------------------------------------------------------------------------------------|
| [kotlin.Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)                                                                          |||
| â³ | [com.google.firebase.ai.type.ImagenReferenceImage](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenReferenceImage)  ||
|   | â³ | [com.google.firebase.ai.type.ImagenMaskReference](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenMaskReference) |

Known direct subclasses  
[ImagenBackgroundMask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenBackgroundMask), [ImagenForegroundMask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenForegroundMask), [ImagenRawMask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenRawMask), [ImagenSemanticMask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenSemanticMask)  

|----------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|
| [ImagenBackgroundMask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenBackgroundMask) | A generated mask image which will auto-detect and mask out the background.                             |
| [ImagenForegroundMask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenForegroundMask) | A generated mask image which will auto-detect and mask out the foreground.                             |
| [ImagenRawMask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenRawMask)               | Represents a mask for Imagen editing.                                                                  |
| [ImagenSemanticMask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenSemanticMask)     | Represents a generated mask for Imagen editing which masks out certain objects using object detection. |

*** ** * ** ***

Represents a mask for Imagen editing. This image (generated or provided) should contain only black and white pixels, with black representing parts of the image which should not change.

## Summary

|                                                                                              ### Public companion functions                                                                                              |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)`<`[ImagenReferenceImage](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenReferenceImage)`>` | [generateMaskAndPadForOutpainting](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenMaskReference.Companion#generateMaskAndPadForOutpainting(com.google.firebase.ai.type.ImagenInlineImage,com.google.firebase.ai.type.Dimensions,com.google.firebase.ai.type.ImagenImagePlacement))`(` ` image: `[ImagenInlineImage](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenInlineImage)`,` ` newDimensions: `[Dimensions](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Dimensions)`,` ` newPosition: `[ImagenImagePlacement](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenImagePlacement) `)` Generates two reference images of [ImagenRawImage](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenRawImage) and [ImagenRawMask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenRawMask).                                                                                                                |
| [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)`<`[ImagenReferenceImage](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenReferenceImage)`>` | [generateMaskAndPadForOutpainting](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenMaskReference.Companion#generateMaskAndPadForOutpainting(com.google.firebase.ai.type.ImagenInlineImage,com.google.firebase.ai.type.Dimensions,com.google.firebase.ai.type.ImagenImagePlacement,kotlin.Double))`(` ` image: `[ImagenInlineImage](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenInlineImage)`,` ` newDimensions: `[Dimensions](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Dimensions)`,` ` newPosition: `[ImagenImagePlacement](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenImagePlacement)`,` ` dilation: `[Double](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html) `)` Generates two reference images of [ImagenRawImage](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenRawImage) and [ImagenRawMask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenRawMask). |

|                                                                                                                                                                                                                                                                                                                                                                                                                                                               ### Inherited properties                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| From [com.google.firebase.ai.type.ImagenReferenceImage](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenReferenceImage) |-------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------| | [ImagenInlineImage](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenInlineImage)`?` | [image](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenReferenceImage#image())             | | [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)`?`                                           | [referenceId](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenReferenceImage#referenceId()) | |

## Public companion functions

### generateMaskAndPadForOutpainting

```
funÂ generateMaskAndPadForOutpainting(
Â Â Â Â image:Â ImagenInlineImage,
Â Â Â Â newDimensions:Â Dimensions,
Â Â Â Â newPosition:Â ImagenImagePlacement = ImagenImagePlacement.CENTER
):Â List<ImagenReferenceImage>
```

Generates two reference images of [ImagenRawImage](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenRawImage) and [ImagenRawMask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenRawMask). These images are generated in this order:

- One [ImagenRawImage](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenRawImage) containing the original image, padded out to the new dimensions with black pixels, with the original image placed at the given placement

- One [ImagenRawMask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenRawMask) of the same dimensions containing white everywhere except at the placement original image. This is the format expected by Imagen for outpainting requests.

|                                                                                Parameters                                                                                 |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|
| `image: `[ImagenInlineImage](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenInlineImage)                                             | the original image                                                                               |
| `newDimensions: `[Dimensions](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Dimensions)                                                   | the new dimensions for outpainting. These new dimensions *must* be more than the original image. |
| `newPosition: `[ImagenImagePlacement](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenImagePlacement)` = ImagenImagePlacement.CENTER` | the placement of the original image within the new outpainted image.                             |

### generateMaskAndPadForOutpainting

```
funÂ generateMaskAndPadForOutpainting(
Â Â Â Â image:Â ImagenInlineImage,
Â Â Â Â newDimensions:Â Dimensions,
Â Â Â Â newPosition:Â ImagenImagePlacement = ImagenImagePlacement.CENTER,
Â Â Â Â dilation:Â Double = 0.01
):Â List<ImagenReferenceImage>
```

Generates two reference images of [ImagenRawImage](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenRawImage) and [ImagenRawMask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenRawMask). These images are generated in this order:

- One [ImagenRawImage](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenRawImage) containing the original image, padded out to the new dimensions with black pixels, with the original image placed at the given placement

- One [ImagenRawMask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenRawMask) of the same dimensions containing white everywhere except at the placement original image. This is the format expected by Imagen for outpainting requests.

|                                                                                Parameters                                                                                 |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| `image: `[ImagenInlineImage](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenInlineImage)                                             | the original image                                                                                                                                        |
| `newDimensions: `[Dimensions](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Dimensions)                                                   | the new dimensions for outpainting. These new dimensions *must* be more than the original image.                                                          |
| `newPosition: `[ImagenImagePlacement](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenImagePlacement)` = ImagenImagePlacement.CENTER` | the placement of the original image within the new outpainted image.                                                                                      |
| `dilation: `[Double](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html)` = 0.01`                                                                     | the dilation for the outpainting mask. See: [ImagenRawMask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenRawMask). |