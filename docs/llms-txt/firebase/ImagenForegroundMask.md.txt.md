# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenForegroundMask.md.txt

# ImagenForegroundMask

# ImagenForegroundMask


```
@PublicPreviewAPI
public final class ImagenForegroundMask extends ImagenMaskReference
```

<br />

|---|---|---|---|
| [java.lang.Object](https://developer.android.com/reference/kotlin/java/lang/Object.html) ||||
| ↳ | [com.google.firebase.ai.type.ImagenReferenceImage](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenReferenceImage) |||
|   | ↳ | [com.google.firebase.ai.type.ImagenMaskReference](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenMaskReference) ||
|   |   | ↳ | [com.google.firebase.ai.type.ImagenForegroundMask](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenForegroundMask) |

*** ** * ** ***

A generated mask image which will auto-detect and mask out the foreground. The background will be black, and the foreground white

## Summary

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenForegroundMask#ImagenForegroundMask(kotlin.Double)(https://developer.android.com/reference/kotlin/java/lang/Double.html dilation)` |

| ### Inherited fields |
|---|
| From [com.google.firebase.ai.type.ImagenReferenceImage](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenReferenceImage) |---|---| | `final https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenInlineImage` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenReferenceImage#image()` | | `final https://developer.android.com/reference/kotlin/java/lang/Integer.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenReferenceImage#referenceId()` | |

## Public constructors

### ImagenForegroundMask

```
public ImagenForegroundMask(Double dilation)
```

| Parameters |
|---|---|
| `https://developer.android.com/reference/kotlin/java/lang/Double.html dilation` | the amount to dilate the mask. This can help smooth the borders of an edit and make it seem more convincing. For example, `0.05` will dilate the mask 5%. |