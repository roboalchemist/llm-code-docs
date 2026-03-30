# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenSemanticMask.md.txt

# ImagenSemanticMask

# ImagenSemanticMask


```
@PublicPreviewAPI
public final class ImagenSemanticMask extends ImagenMaskReference
```

<br />

|---|---|---|---|
| [java.lang.Object](https://developer.android.com/reference/kotlin/java/lang/Object.html) ||||
| ↳ | [com.google.firebase.ai.type.ImagenReferenceImage](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenReferenceImage) |||
|   | ↳ | [com.google.firebase.ai.type.ImagenMaskReference](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenMaskReference) ||
|   |   | ↳ | [com.google.firebase.ai.type.ImagenSemanticMask](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenSemanticMask) |

*** ** * ** ***

Represents a generated mask for Imagen editing which masks out certain objects using object detection.

## Summary

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenSemanticMask#ImagenSemanticMask(kotlin.collections.List,kotlin.Double)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Integer.html> classes, https://developer.android.com/reference/kotlin/java/lang/Double.html dilation )` |

| ### Inherited fields |
|---|
| From [com.google.firebase.ai.type.ImagenReferenceImage](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenReferenceImage) |---|---| | `final https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenInlineImage` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenReferenceImage#image()` | | `final https://developer.android.com/reference/kotlin/java/lang/Integer.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenReferenceImage#referenceId()` | |

## Public constructors

### ImagenSemanticMask

```
public ImagenSemanticMask(
    @NonNull List<@NonNull Integer> classes,
    Double dilation
)
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Integer.html> classes` | the list of segmentation IDs for objects to detect and mask out. Find a [list of segmentation IDs](https://cloud.google.com/vertex-ai/generative-ai/docs/model-reference/imagen-api-edit#segment-ids) in the Vertex AI documentation. |
| `https://developer.android.com/reference/kotlin/java/lang/Double.html dilation` | the amount to dilate the mask. This can help smooth the borders of an edit and make it seem more convincing. For example, `0.05` will dilate the mask 5%. |