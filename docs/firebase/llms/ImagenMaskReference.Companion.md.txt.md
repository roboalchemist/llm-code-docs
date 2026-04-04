# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenMaskReference.Companion.md.txt

# ImagenMaskReference.Companion

# ImagenMaskReference.Companion


```
public static class ImagenMaskReference.Companion
```

<br />

*** ** * ** ***

## Summary

| ### Public methods |
|---|---|
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenReferenceImage>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenMaskReference.Companion#generateMaskAndPadForOutpainting(com.google.firebase.ai.type.ImagenInlineImage,com.google.firebase.ai.type.Dimensions,com.google.firebase.ai.type.ImagenImagePlacement)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenInlineImage image, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Dimensions newDimensions, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenImagePlacement newPosition )` Generates two reference images of `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenRawImage` and `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenRawMask`. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenReferenceImage>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenMaskReference.Companion#generateMaskAndPadForOutpainting(com.google.firebase.ai.type.ImagenInlineImage,com.google.firebase.ai.type.Dimensions,com.google.firebase.ai.type.ImagenImagePlacement,kotlin.Double)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenInlineImage image, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Dimensions newDimensions, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenImagePlacement newPosition, double dilation )` Generates two reference images of `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenRawImage` and `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenRawMask`. |

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