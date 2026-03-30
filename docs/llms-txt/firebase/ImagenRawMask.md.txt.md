# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenRawMask.md.txt

# ImagenRawMask

# ImagenRawMask


```
@PublicPreviewAPI
public final class ImagenRawMask extends ImagenMaskReference
```

<br />

|---|---|---|---|
| [java.lang.Object](https://developer.android.com/reference/kotlin/java/lang/Object.html) ||||
| ↳ | [com.google.firebase.ai.type.ImagenReferenceImage](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenReferenceImage) |||
|   | ↳ | [com.google.firebase.ai.type.ImagenMaskReference](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenMaskReference) ||
|   |   | ↳ | [com.google.firebase.ai.type.ImagenRawMask](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenRawMask) |

*** ** * ** ***

Represents a mask for Imagen editing. This image should contain only black and white pixels, with black representing parts of the image which should not change.

## Summary

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenRawMask#ImagenRawMask(com.google.firebase.ai.type.ImagenInlineImage,kotlin.Double)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenInlineImage mask, https://developer.android.com/reference/kotlin/java/lang/Double.html dilation)` |

| ### Inherited fields |
|---|
| From [com.google.firebase.ai.type.ImagenReferenceImage](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenReferenceImage) |---|---| | `final https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenInlineImage` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenReferenceImage#image()` | | `final https://developer.android.com/reference/kotlin/java/lang/Integer.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenReferenceImage#referenceId()` | |

## Public constructors

### ImagenRawMask

```
public ImagenRawMask(@NonNull ImagenInlineImage mask, Double dilation)
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenInlineImage mask` | the mask image |
| `https://developer.android.com/reference/kotlin/java/lang/Double.html dilation` | the amount to dilate the mask. This can help smooth the borders of an edit and make it seem more convincing. For example, `0.05` will dilate the mask 5%. |