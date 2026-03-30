# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenForegroundMask.md.txt

# ImagenForegroundMask

# ImagenForegroundMask


```
@PublicPreviewAPI
class ImagenForegroundMask : ImagenMaskReference
```

<br />

|---|---|---|---|
| [kotlin.Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html) ||||
| ↳ | [com.google.firebase.ai.type.ImagenReferenceImage](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenReferenceImage) |||
|   | ↳ | [com.google.firebase.ai.type.ImagenMaskReference](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenMaskReference) ||
|   |   | ↳ | [com.google.firebase.ai.type.ImagenForegroundMask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenForegroundMask) |

*** ** * ** ***

A generated mask image which will auto-detect and mask out the foreground. The background will be black, and the foreground white

## Summary

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenForegroundMask#ImagenForegroundMask(kotlin.Double)(dilation: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html?)` |

| ### Inherited properties |
|---|
| From [com.google.firebase.ai.type.ImagenReferenceImage](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenReferenceImage) |---|---| | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenInlineImage?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenReferenceImage#image()` | | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenReferenceImage#referenceId()` | |

## Public constructors

### ImagenForegroundMask

```
ImagenForegroundMask(dilation: Double? = null)
```

| Parameters |
|---|---|
| `dilation: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html? = null` | the amount to dilate the mask. This can help smooth the borders of an edit and make it seem more convincing. For example, `0.05` will dilate the mask 5%. |