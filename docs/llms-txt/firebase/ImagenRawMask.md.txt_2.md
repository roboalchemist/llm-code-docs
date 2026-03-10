# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenRawMask.md.txt

# ImagenRawMask

# ImagenRawMask


```
@PublicPreviewAPI
class ImagenRawMask : ImagenMaskReference
```

<br />

|---|---|---|---|
| [kotlin.Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html) ||||
| ↳ | [com.google.firebase.ai.type.ImagenReferenceImage](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenReferenceImage) |||
|   | ↳ | [com.google.firebase.ai.type.ImagenMaskReference](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenMaskReference) ||
|   |   | ↳ | [com.google.firebase.ai.type.ImagenRawMask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenRawMask) |

*** ** * ** ***

Represents a mask for Imagen editing. This image should contain only black and white pixels, with black representing parts of the image which should not change.

## Summary

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenRawMask#ImagenRawMask(com.google.firebase.ai.type.ImagenInlineImage,kotlin.Double)(mask: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenInlineImage, dilation: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html?)` |

| ### Inherited properties |
|---|
| From [com.google.firebase.ai.type.ImagenReferenceImage](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenReferenceImage) |---|---| | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenInlineImage?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenReferenceImage#image()` | | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenReferenceImage#referenceId()` | |

## Public constructors

### ImagenRawMask

```
ImagenRawMask(mask: ImagenInlineImage, dilation: Double? = null)
```

| Parameters |
|---|---|
| `mask: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenInlineImage` | the mask image |
| `dilation: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html? = null` | the amount to dilate the mask. This can help smooth the borders of an edit and make it seem more convincing. For example, `0.05` will dilate the mask 5%. |