# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenSemanticMask.md.txt

# ImagenSemanticMask

# ImagenSemanticMask


```
@PublicPreviewAPI
class ImagenSemanticMask : ImagenMaskReference
```

<br />

|---|---|---|---|
| [kotlin.Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html) ||||
| ↳ | [com.google.firebase.ai.type.ImagenReferenceImage](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenReferenceImage) |||
|   | ↳ | [com.google.firebase.ai.type.ImagenMaskReference](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenMaskReference) ||
|   |   | ↳ | [com.google.firebase.ai.type.ImagenSemanticMask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenSemanticMask) |

*** ** * ** ***

Represents a generated mask for Imagen editing which masks out certain objects using object detection.

## Summary

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenSemanticMask#ImagenSemanticMask(kotlin.collections.List,kotlin.Double)(classes: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html>, dilation: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html?)` |

| ### Inherited properties |
|---|
| From [com.google.firebase.ai.type.ImagenReferenceImage](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenReferenceImage) |---|---| | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenInlineImage?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenReferenceImage#image()` | | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenReferenceImage#referenceId()` | |

## Public constructors

### ImagenSemanticMask

```
ImagenSemanticMask(classes: List<Int>, dilation: Double? = null)
```

| Parameters |
|---|---|
| `classes: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html>` | the list of segmentation IDs for objects to detect and mask out. Find a [list of segmentation IDs](https://cloud.google.com/vertex-ai/generative-ai/docs/model-reference/imagen-api-edit#segment-ids) in the Vertex AI documentation. |
| `dilation: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html? = null` | the amount to dilate the mask. This can help smooth the borders of an edit and make it seem more convincing. For example, `0.05` will dilate the mask 5%. |