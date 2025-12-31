# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenSemanticMask.md.txt

# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenSemanticMask.md.txt

# ImagenSemanticMask

# ImagenSemanticMask


```
@PublicPreviewAPI
public final class ImagenSemanticMask extends ImagenMaskReference
```

<br />

|---|---|---|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| [java.lang.Object](https://developer.android.com/reference/kotlin/java/lang/Object.html)                                                                     ||||
| â³ | [com.google.firebase.ai.type.ImagenReferenceImage](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenReferenceImage)   |||
|   | â³ | [com.google.firebase.ai.type.ImagenMaskReference](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenMaskReference)  ||
|   |   | â³ | [com.google.firebase.ai.type.ImagenSemanticMask](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenSemanticMask) |

*** ** * ** ***

Represents a generated mask for Imagen editing which masks out certain objects using object detection.

## Summary

|                                                                                                                                                                                                                                                                                                                    ### Public constructors                                                                                                                                                                                                                                                                                                                     |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [ImagenSemanticMask](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenSemanticMask#ImagenSemanticMask(kotlin.collections.List,kotlin.Double))`(` ` @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[List](https://developer.android.com/reference/kotlin/java/util/List.html)`<@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[Integer](https://developer.android.com/reference/kotlin/java/lang/Integer.html)`> classes,` ` `[Double](https://developer.android.com/reference/kotlin/java/lang/Double.html)` dilation` `)` |

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                            ### Inherited fields                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| From [com.google.firebase.ai.type.ImagenReferenceImage](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenReferenceImage) |-------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------| | `final `[ImagenInlineImage](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenInlineImage) | [image](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenReferenceImage#image())             | | `final `[Integer](https://developer.android.com/reference/kotlin/java/lang/Integer.html)                                      | [referenceId](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenReferenceImage#referenceId()) | |

## Public constructors

### ImagenSemanticMask

```
publicÂ ImagenSemanticMask(
Â Â Â Â @NonNull List<@NonNull Integer>Â classes,
Â Â Â Â DoubleÂ dilation
)
```  

|                                                                                                                                                                               Parameters                                                                                                                                                                               |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[List](https://developer.android.com/reference/kotlin/java/util/List.html)`<@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[Integer](https://developer.android.com/reference/kotlin/java/lang/Integer.html)`> classes` | the list of segmentation IDs for objects to detect and mask out. Find a [list of segmentation IDs](https://cloud.google.com/vertex-ai/generative-ai/docs/model-reference/imagen-api-edit#segment-ids) in the Vertex AI documentation. |
| [Double](https://developer.android.com/reference/kotlin/java/lang/Double.html)` dilation`                                                                                                                                                                                                                                                                              | the amount to dilate the mask. This can help smooth the borders of an edit and make it seem more convincing. For example, `0.05` will dilate the mask 5%.                                                                             |