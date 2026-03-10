# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenBackgroundMask.md.txt

# ImagenBackgroundMask

# ImagenBackgroundMask


```
@PublicPreviewAPI
public final class ImagenBackgroundMask extends ImagenMaskReference
```

<br />

|---|---|---|---|
| [java.lang.Object](https://developer.android.com/reference/kotlin/java/lang/Object.html) ||||
| ↳ | [com.google.firebase.ai.type.ImagenReferenceImage](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenReferenceImage) |||
|   | ↳ | [com.google.firebase.ai.type.ImagenMaskReference](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenMaskReference) ||
|   |   | ↳ | [com.google.firebase.ai.type.ImagenBackgroundMask](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenBackgroundMask) |

*** ** * ** ***

A generated mask image which will auto-detect and mask out the background. The background will be white, and the foreground black

## Summary

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenBackgroundMask#ImagenBackgroundMask(kotlin.Double)(https://developer.android.com/reference/kotlin/java/lang/Double.html dilation)` |

| ### Inherited fields |
|---|
| From [com.google.firebase.ai.type.ImagenReferenceImage](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenReferenceImage) |---|---| | `final https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenInlineImage` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenReferenceImage#image()` | | `final https://developer.android.com/reference/kotlin/java/lang/Integer.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenReferenceImage#referenceId()` | |

## Public constructors

### ImagenBackgroundMask

```
public ImagenBackgroundMask(Double dilation)
```

| Parameters |
|---|---|
| `https://developer.android.com/reference/kotlin/java/lang/Double.html dilation` | the amount to dilate the mask. This can help smooth the borders of an edit and make it seem more convincing. For example, `0.05` will dilate the mask 5%. |