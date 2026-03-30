# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ai/java/ImagenModelFutures.md.txt

# ImagenModelFutures

# ImagenModelFutures


```
@PublicPreviewAPI
public abstract class ImagenModelFutures
```

<br />

*** ** * ** ***

Wrapper class providing Java compatible methods for `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/ImagenModel`.

| See also |
|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/ImagenModel` |   |

## Summary

| ### Nested types |
|---|
| `public static class https://firebase.google.com/docs/reference/android/com/google/firebase/ai/java/ImagenModelFutures.Companion` |

| ### Public methods |
|---|---|
| `abstract @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/common/util/concurrent/ListenableFuture<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenGenerationResponse<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenInlineImage>>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/java/ImagenModelFutures#editImage(kotlin.collections.List,kotlin.String)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenReferenceImage> referenceImages, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html prompt )` Generates an image from a single or set of base images, returning the result directly to the caller. |
| `abstract @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/common/util/concurrent/ListenableFuture<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenGenerationResponse<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenInlineImage>>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/java/ImagenModelFutures#editImage(kotlin.collections.List,kotlin.String,com.google.firebase.ai.type.ImagenEditingConfig)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenReferenceImage> referenceImages, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html prompt, https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenEditingConfig config )` Generates an image from a single or set of base images, returning the result directly to the caller. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/java/ImagenModelFutures` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/java/ImagenModelFutures.Companion#from(com.google.firebase.ai.ImagenModel)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/ImagenModel model)` |
| `abstract @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/common/util/concurrent/ListenableFuture<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenGenerationResponse<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenInlineImage>>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/java/ImagenModelFutures#generateImages(kotlin.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html prompt)` Generates an image, returning the result directly to the caller. |
| `abstract @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/ImagenModel` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/java/ImagenModelFutures#getImageModel()()` Returns the `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/ImagenModel` object wrapped by this object. |
| `abstract @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/common/util/concurrent/ListenableFuture<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenGenerationResponse<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenInlineImage>>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/java/ImagenModelFutures#inpaintImage(com.google.firebase.ai.type.ImagenInlineImage,kotlin.String,com.google.firebase.ai.type.ImagenMaskReference,com.google.firebase.ai.type.ImagenEditingConfig)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenInlineImage image, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html prompt, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenMaskReference mask, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenEditingConfig config )` Generates an image by inpainting a masked off part of a base image. |
| `abstract @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/common/util/concurrent/ListenableFuture<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenGenerationResponse<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenInlineImage>>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/java/ImagenModelFutures#outpaintImage(com.google.firebase.ai.type.ImagenInlineImage,com.google.firebase.ai.type.Dimensions,com.google.firebase.ai.type.ImagenImagePlacement,kotlin.String,com.google.firebase.ai.type.ImagenEditingConfig)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenInlineImage image, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Dimensions newDimensions, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenImagePlacement newPosition, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html prompt, https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenEditingConfig config )` Generates an image by outpainting the image, extending its borders |

## Public methods

### editImage

```
public abstract @NonNull ListenableFuture<@NonNull ImagenGenerationResponse<@NonNull ImagenInlineImage>> editImage(
    @NonNull List<@NonNull ImagenReferenceImage> referenceImages,
    @NonNull String prompt
)
```

Generates an image from a single or set of base images, returning the result directly to the caller.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenReferenceImage> referenceImages` | the image inputs given to the model as a prompt |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html prompt` | the text input given to the model as a prompt |

### editImage

```
public abstract @NonNull ListenableFuture<@NonNull ImagenGenerationResponse<@NonNull ImagenInlineImage>> editImage(
    @NonNull List<@NonNull ImagenReferenceImage> referenceImages,
    @NonNull String prompt,
    ImagenEditingConfig config
)
```

Generates an image from a single or set of base images, returning the result directly to the caller.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenReferenceImage> referenceImages` | the image inputs given to the model as a prompt |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html prompt` | the text input given to the model as a prompt |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenEditingConfig config` | the editing configuration settings |

### from

```
public static final @NonNull ImagenModelFutures from(@NonNull ImagenModel model)
```

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/java/ImagenModelFutures` | a `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/java/ImagenModelFutures` created around the provided `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/ImagenModel` |

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

Returns the `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/ImagenModel` object wrapped by this object.

### inpaintImage

```
public abstract @NonNull ListenableFuture<@NonNull ImagenGenerationResponse<@NonNull ImagenInlineImage>> inpaintImage(
    @NonNull ImagenInlineImage image,
    @NonNull String prompt,
    @NonNull ImagenMaskReference mask,
    @NonNull ImagenEditingConfig config
)
```

Generates an image by inpainting a masked off part of a base image.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenInlineImage image` | the base image |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html prompt` | the text input given to the model as a prompt |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenMaskReference mask` | the mask which defines where in the image can be painted by imagen. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenEditingConfig config` | the editing configuration settings, it should include an `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenEditMode` |

### outpaintImage

```
public abstract @NonNull ListenableFuture<@NonNull ImagenGenerationResponse<@NonNull ImagenInlineImage>> outpaintImage(
    @NonNull ImagenInlineImage image,
    @NonNull Dimensions newDimensions,
    @NonNull ImagenImagePlacement newPosition,
    @NonNull String prompt,
    ImagenEditingConfig config
)
```

Generates an image by outpainting the image, extending its borders

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenInlineImage image` | the base image |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Dimensions newDimensions` | the new dimensions for the image, *must* be larger than the original image. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenImagePlacement newPosition` | the placement of the base image within the new image. This can either be coordinates (0,0 is the top left corner) or an alignment (ex: `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenImagePlacement.Companion#BOTTOM_CENTER()`) |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html prompt` | optional, but can be used to specify the background generated if context is insufficient |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenEditingConfig config` | the editing configuration settings |

| See also |
|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenMaskReference.Companion#generateMaskAndPadForOutpainting(com.google.firebase.ai.type.ImagenInlineImage,com.google.firebase.ai.type.Dimensions,com.google.firebase.ai.type.ImagenImagePlacement)` |   |