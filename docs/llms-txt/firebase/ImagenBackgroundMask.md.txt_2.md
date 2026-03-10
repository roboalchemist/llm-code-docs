# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenBackgroundMask.md.txt

# ImagenBackgroundMask

# ImagenBackgroundMask


```
@PublicPreviewAPI
class ImagenBackgroundMask : ImagenMaskReference
```

<br />

|---|---|---|---|
| [kotlin.Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html) ||||
| ↳ | [com.google.firebase.ai.type.ImagenReferenceImage](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenReferenceImage) |||
|   | ↳ | [com.google.firebase.ai.type.ImagenMaskReference](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenMaskReference) ||
|   |   | ↳ | [com.google.firebase.ai.type.ImagenBackgroundMask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenBackgroundMask) |

*** ** * ** ***

A generated mask image which will auto-detect and mask out the background. The background will be white, and the foreground black

## Summary

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenBackgroundMask#ImagenBackgroundMask(kotlin.Double)(dilation: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html?)` |

| ### Inherited properties |
|---|
| From [com.google.firebase.ai.type.ImagenReferenceImage](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenReferenceImage) |---|---| | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenInlineImage?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenReferenceImage#image()` | | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenReferenceImage#referenceId()` | |

## Public constructors

### ImagenBackgroundMask

```
ImagenBackgroundMask(dilation: Double? = null)
```

| Parameters |
|---|---|
| `dilation: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html? = null` | the amount to dilate the mask. This can help smooth the borders of an edit and make it seem more convincing. For example, `0.05` will dilate the mask 5%. |