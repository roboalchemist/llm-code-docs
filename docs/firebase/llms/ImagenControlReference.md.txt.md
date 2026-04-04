# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenControlReference.md.txt

# ImagenControlReference

# ImagenControlReference


```
@PublicPreviewAPI
public final class ImagenControlReference extends ImagenReferenceImage
```

<br />

|---|---|---|
| [java.lang.Object](https://developer.android.com/reference/kotlin/java/lang/Object.html) |||
| ↳ | [com.google.firebase.ai.type.ImagenReferenceImage](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenReferenceImage) ||
|   | ↳ | [com.google.firebase.ai.type.ImagenControlReference](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenControlReference) |

*** ** * ** ***

Represents a reference image (provided or generated) to bound the created image via controlled generation.

## Summary

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenControlReference#ImagenControlReference(com.google.firebase.ai.type.ImagenControlType,com.google.firebase.ai.type.ImagenInlineImage,kotlin.Int,kotlin.Boolean,kotlin.Int,kotlin.Int)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenControlType type, https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenInlineImage image, https://developer.android.com/reference/kotlin/java/lang/Integer.html referenceId, https://developer.android.com/reference/kotlin/java/lang/Boolean.html enableComputation, https://developer.android.com/reference/kotlin/java/lang/Integer.html superpixelRegionSize, https://developer.android.com/reference/kotlin/java/lang/Integer.html superpixelRuler )` |

| ### Inherited fields |
|---|
| From [com.google.firebase.ai.type.ImagenReferenceImage](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenReferenceImage) |---|---| | `final https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenInlineImage` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenReferenceImage#image()` | | `final https://developer.android.com/reference/kotlin/java/lang/Integer.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenReferenceImage#referenceId()` | |

## Public constructors

### ImagenControlReference

```
public ImagenControlReference(
    @NonNull ImagenControlType type,
    ImagenInlineImage image,
    Integer referenceId,
    Boolean enableComputation,
    Integer superpixelRegionSize,
    Integer superpixelRuler
)
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenControlType type` | the type of control reference image |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenInlineImage image` | the image provided, required if `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenControlReference#<init>(com.google.firebase.ai.type.ImagenControlType,com.google.firebase.ai.type.ImagenInlineImage,kotlin.Int,kotlin.Boolean,kotlin.Int,kotlin.Int)` is false |
| `https://developer.android.com/reference/kotlin/java/lang/Integer.html referenceId` | the reference ID for this image, to be referenced in the prompt |
| `https://developer.android.com/reference/kotlin/java/lang/Boolean.html enableComputation` | requests that the reference image be generated serverside instead of provided |
| `https://developer.android.com/reference/kotlin/java/lang/Integer.html superpixelRegionSize` | if type is `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenControlType.Companion#COLOR_SUPERPIXEL()` and `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenControlReference#<init>(com.google.firebase.ai.type.ImagenControlType,com.google.firebase.ai.type.ImagenInlineImage,kotlin.Int,kotlin.Boolean,kotlin.Int,kotlin.Int)` is true, this will control the size of each superpixel region in pixels for the generated referenced image |
| `https://developer.android.com/reference/kotlin/java/lang/Integer.html superpixelRuler` | if type is `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenControlType.Companion#COLOR_SUPERPIXEL()` and `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenControlReference#<init>(com.google.firebase.ai.type.ImagenControlType,com.google.firebase.ai.type.ImagenInlineImage,kotlin.Int,kotlin.Boolean,kotlin.Int,kotlin.Int)` is true, this will control the superpixel smoothness factor for the generated referenced image |