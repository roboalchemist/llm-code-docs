# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenMaskReference.md.txt

# ImagenMaskReference

# ImagenMaskReference


```
@PublicPreviewAPI
public abstract class ImagenMaskReference extends ImagenReferenceImage
```

<br />

|---|---|---|
| [java.lang.Object](https://developer.android.com/reference/kotlin/java/lang/Object.html) |||
| ↳ | [com.google.firebase.ai.type.ImagenReferenceImage](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenReferenceImage) ||
|   | ↳ | [com.google.firebase.ai.type.ImagenMaskReference](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenMaskReference) |

Known direct subclasses [ImagenBackgroundMask](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenBackgroundMask), [ImagenForegroundMask](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenForegroundMask), [ImagenRawMask](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenRawMask), [ImagenSemanticMask](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenSemanticMask)

|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenBackgroundMask` | A generated mask image which will auto-detect and mask out the background. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenForegroundMask` | A generated mask image which will auto-detect and mask out the foreground. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenRawMask` | Represents a mask for Imagen editing. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenSemanticMask` | Represents a generated mask for Imagen editing which masks out certain objects using object detection. |

*** ** * ** ***

Represents a mask for Imagen editing. This image (generated or provided) should contain only black and white pixels, with black representing parts of the image which should not change.

## Summary

| ### Nested types |
|---|
| `public static class https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenMaskReference.Companion` |

| ### Public methods |
|---|---|
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenReferenceImage>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenMaskReference.Companion#generateMaskAndPadForOutpainting(com.google.firebase.ai.type.ImagenInlineImage,com.google.firebase.ai.type.Dimensions,com.google.firebase.ai.type.ImagenImagePlacement)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenInlineImage image, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Dimensions newDimensions, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenImagePlacement newPosition )` Generates two reference images of `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenRawImage` and `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenRawMask`. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenReferenceImage>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenMaskReference.Companion#generateMaskAndPadForOutpainting(com.google.firebase.ai.type.ImagenInlineImage,com.google.firebase.ai.type.Dimensions,com.google.firebase.ai.type.ImagenImagePlacement,kotlin.Double)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenInlineImage image, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Dimensions newDimensions, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenImagePlacement newPosition, double dilation )` Generates two reference images of `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenRawImage` and `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenRawMask`. |

| ### Inherited fields |
|---|
| From [com.google.firebase.ai.type.ImagenReferenceImage](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenReferenceImage) |---|---| | `final https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenInlineImage` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenReferenceImage#image()` | | `final https://developer.android.com/reference/kotlin/java/lang/Integer.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenReferenceImage#referenceId()` | |

## Public methods

### generateMaskAndPadForOutpainting

```
public static final @NonNull List<@NonNull ImagenReferenceImage> generateMaskAndPadForOutpainting(
    @NonNull ImagenInlineImage image,
    @NonNull Dimensions newDimensions,
    @NonNull ImagenImagePlacement newPosition
)
```

Generates two reference images of `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenRawImage` and `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenRawMask`. These images are generated in this order:

- One `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenRawImage` containing the original image, padded out to the new dimensions with black pixels, with the original image placed at the given placement

- One `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenRawMask` of the same dimensions containing white everywhere except at the placement original image. This is the format expected by Imagen for outpainting requests.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenInlineImage image` | the original image |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Dimensions newDimensions` | the new dimensions for outpainting. These new dimensions *must* be more than the original image. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenImagePlacement newPosition` | the placement of the original image within the new outpainted image. |

### generateMaskAndPadForOutpainting

```
public static final @NonNull List<@NonNull ImagenReferenceImage> generateMaskAndPadForOutpainting(
    @NonNull ImagenInlineImage image,
    @NonNull Dimensions newDimensions,
    @NonNull ImagenImagePlacement newPosition,
    double dilation
)
```

Generates two reference images of `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenRawImage` and `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenRawMask`. These images are generated in this order:

- One `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenRawImage` containing the original image, padded out to the new dimensions with black pixels, with the original image placed at the given placement

- One `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenRawMask` of the same dimensions containing white everywhere except at the placement original image. This is the format expected by Imagen for outpainting requests.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenInlineImage image` | the original image |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Dimensions newDimensions` | the new dimensions for outpainting. These new dimensions *must* be more than the original image. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenImagePlacement newPosition` | the placement of the original image within the new outpainted image. |
| `double dilation` | the dilation for the outpainting mask. See: `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenRawMask`. |