# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenMaskReference.Companion.md.txt

# ImagenMaskReference.Companion

# ImagenMaskReference.Companion


```
public static class ImagenMaskReference.Companion
```

<br />

*** ** * ** ***

## Summary

|                                                                                                                                                                                                   ### Public methods                                                                                                                                                                                                   |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `static final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[List](https://developer.android.com/reference/kotlin/java/util/List.html)`<@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[ImagenReferenceImage](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenReferenceImage)`>` | [generateMaskAndPadForOutpainting](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenMaskReference.Companion#generateMaskAndPadForOutpainting(com.google.firebase.ai.type.ImagenInlineImage,com.google.firebase.ai.type.Dimensions,com.google.firebase.ai.type.ImagenImagePlacement))`(` ` @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[ImagenInlineImage](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenInlineImage)` image,` ` @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[Dimensions](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Dimensions)` newDimensions,` ` @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[ImagenImagePlacement](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenImagePlacement)` newPosition` `)` Generates two reference images of [ImagenRawImage](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenRawImage) and [ImagenRawMask](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenRawMask).                                   |
| `static final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[List](https://developer.android.com/reference/kotlin/java/util/List.html)`<@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[ImagenReferenceImage](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenReferenceImage)`>` | [generateMaskAndPadForOutpainting](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenMaskReference.Companion#generateMaskAndPadForOutpainting(com.google.firebase.ai.type.ImagenInlineImage,com.google.firebase.ai.type.Dimensions,com.google.firebase.ai.type.ImagenImagePlacement,kotlin.Double))`(` ` @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[ImagenInlineImage](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenInlineImage)` image,` ` @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[Dimensions](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Dimensions)` newDimensions,` ` @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[ImagenImagePlacement](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenImagePlacement)` newPosition,` ` double dilation` `)` Generates two reference images of [ImagenRawImage](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenRawImage) and [ImagenRawMask](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenRawMask). |

## Public methods

### generateMaskAndPadForOutpainting

```
publicÂ staticÂ finalÂ @NonNull List<@NonNull ImagenReferenceImage>Â generateMaskAndPadForOutpainting(
Â Â Â Â @NonNull ImagenInlineImageÂ image,
Â Â Â Â @NonNull DimensionsÂ newDimensions,
Â Â Â Â @NonNull ImagenImagePlacementÂ newPosition
)
```

Generates two reference images of [ImagenRawImage](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenRawImage) and [ImagenRawMask](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenRawMask). These images are generated in this order:

- One [ImagenRawImage](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenRawImage) containing the original image, padded out to the new dimensions with black pixels, with the original image placed at the given placement

- One [ImagenRawMask](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenRawMask) of the same dimensions containing white everywhere except at the placement original image. This is the format expected by Imagen for outpainting requests.

|                                                                                                                Parameters                                                                                                                 |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|
| `@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[ImagenInlineImage](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenInlineImage)` image`             | the original image                                                                               |
| `@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[Dimensions](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Dimensions)` newDimensions`                   | the new dimensions for outpainting. These new dimensions *must* be more than the original image. |
| `@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[ImagenImagePlacement](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenImagePlacement)` newPosition` | the placement of the original image within the new outpainted image.                             |

### generateMaskAndPadForOutpainting

```
publicÂ staticÂ finalÂ @NonNull List<@NonNull ImagenReferenceImage>Â generateMaskAndPadForOutpainting(
Â Â Â Â @NonNull ImagenInlineImageÂ image,
Â Â Â Â @NonNull DimensionsÂ newDimensions,
Â Â Â Â @NonNull ImagenImagePlacementÂ newPosition,
Â Â Â Â doubleÂ dilation
)
```

Generates two reference images of [ImagenRawImage](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenRawImage) and [ImagenRawMask](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenRawMask). These images are generated in this order:

- One [ImagenRawImage](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenRawImage) containing the original image, padded out to the new dimensions with black pixels, with the original image placed at the given placement

- One [ImagenRawMask](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenRawMask) of the same dimensions containing white everywhere except at the placement original image. This is the format expected by Imagen for outpainting requests.

|                                                                                                                Parameters                                                                                                                 |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[ImagenInlineImage](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenInlineImage)` image`             | the original image                                                                                                                                         |
| `@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[Dimensions](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Dimensions)` newDimensions`                   | the new dimensions for outpainting. These new dimensions *must* be more than the original image.                                                           |
| `@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[ImagenImagePlacement](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenImagePlacement)` newPosition` | the placement of the original image within the new outpainted image.                                                                                       |
| `double dilation`                                                                                                                                                                                                                         | the dilation for the outpainting mask. See: [ImagenRawMask](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenRawMask). |