# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ai/ImagenModel.md.txt

# ImagenModel

# ImagenModel


```
public final class ImagenModel
```

<br />

*** ** * ** ***

Represents a generative model (like Imagen), capable of generating images based on various input types.

See the documentation for a list of [supported models](https://firebase.google.com/docs/ai-logic/models).

## Summary

| ### Public methods |
|---|---|
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenGenerationResponse<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenInlineImage>` | `@https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/PublicPreviewAPI https://firebase.google.com/docs/reference/android/com/google/firebase/ai/ImagenModel#editImage(kotlin.collections.List,kotlin.String,com.google.firebase.ai.type.ImagenEditingConfig)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenReferenceImage> referenceImages, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html prompt, https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenEditingConfig config )` Generates an image from a single or set of base images, returning the result directly to the caller. |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenGenerationResponse<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenInlineImage>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/ImagenModel#generateImages(kotlin.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html prompt)` Generates an image, returning the result directly to the caller. |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenGenerationResponse<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenInlineImage>` | `@https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/PublicPreviewAPI https://firebase.google.com/docs/reference/android/com/google/firebase/ai/ImagenModel#inpaintImage(com.google.firebase.ai.type.ImagenInlineImage,kotlin.String,com.google.firebase.ai.type.ImagenMaskReference,com.google.firebase.ai.type.ImagenEditingConfig)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenInlineImage image, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html prompt, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenMaskReference mask, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenEditingConfig config )` Generates an image by inpainting a masked off part of a base image. |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenGenerationResponse<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenInlineImage>` | `@https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/PublicPreviewAPI https://firebase.google.com/docs/reference/android/com/google/firebase/ai/ImagenModel#outpaintImage(com.google.firebase.ai.type.ImagenInlineImage,com.google.firebase.ai.type.Dimensions,com.google.firebase.ai.type.ImagenImagePlacement,kotlin.String,com.google.firebase.ai.type.ImagenEditingConfig)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenInlineImage image, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Dimensions newDimensions, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenImagePlacement newPosition, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html prompt, https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenEditingConfig config )` Generates an image by outpainting the given image, extending its content beyond the original borders using context from the original image, and optionally, the prompt. |

## Public methods

### editImage

```
@PublicPreviewAPI
public final @NonNull ImagenGenerationResponse<@NonNull ImagenInlineImage> editImage(
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

### generateImages

```
public final @NonNull ImagenGenerationResponse<@NonNull ImagenInlineImage> generateImages(@NonNull String prompt)
```

Generates an image, returning the result directly to the caller.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html prompt` | The input(s) given to the model as a prompt. |

### inpaintImage

```
@PublicPreviewAPI
public final @NonNull ImagenGenerationResponse<@NonNull ImagenInlineImage> inpaintImage(
    @NonNull ImagenInlineImage image,
    @NonNull String prompt,
    @NonNull ImagenMaskReference mask,
    @NonNull ImagenEditingConfig config
)
```

Generates an image by inpainting a masked off part of a base image. Inpainting is the process of filling in missing or masked off parts of the image using context from the original image and prompt.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenInlineImage image` | the base image |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html prompt` | the text input given to the model as a prompt |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenMaskReference mask` | the mask which defines where in the image can be painted by Imagen. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenEditingConfig config` | the editing configuration settings, it should include an `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenEditMode` |

### outpaintImage

```
@PublicPreviewAPI
public final @NonNull ImagenGenerationResponse<@NonNull ImagenInlineImage> outpaintImage(
    @NonNull ImagenInlineImage image,
    @NonNull Dimensions newDimensions,
    @NonNull ImagenImagePlacement newPosition,
    @NonNull String prompt,
    ImagenEditingConfig config
)
```

Generates an image by outpainting the given image, extending its content beyond the original borders using context from the original image, and optionally, the prompt.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenInlineImage image` | the base image |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Dimensions newDimensions` | the new dimensions for the image, *must* be larger than the original image. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenImagePlacement newPosition` | the placement of the base image within the new image. This can either be coordinates (0,0 is the top left corner) or an alignment (ex: `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenImagePlacement.Companion#BOTTOM_CENTER()`) |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html prompt` | optional, can be used to specify the background generated if context is insufficient |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenEditingConfig config` | the editing configuration settings |

| See also |
|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenMaskReference.Companion#generateMaskAndPadForOutpainting(com.google.firebase.ai.type.ImagenInlineImage,com.google.firebase.ai.type.Dimensions,com.google.firebase.ai.type.ImagenImagePlacement)` |   |