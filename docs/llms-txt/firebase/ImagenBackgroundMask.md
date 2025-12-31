# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenBackgroundMask.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenBackgroundMask.md.txt

# ImagenBackgroundMask

# ImagenBackgroundMask


```
@PublicPreviewAPI
class ImagenBackgroundMask : ImagenMaskReference
```

<br />

|---|---|---|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| [kotlin.Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)                                                                               ||||
| â³ | [com.google.firebase.ai.type.ImagenReferenceImage](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenReferenceImage)       |||
|   | â³ | [com.google.firebase.ai.type.ImagenMaskReference](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenMaskReference)      ||
|   |   | â³ | [com.google.firebase.ai.type.ImagenBackgroundMask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenBackgroundMask) |

*** ** * ** ***

A generated mask image which will auto-detect and mask out the background. The background will be white, and the foreground black

## Summary

|                                                                                                                     ### Public constructors                                                                                                                     |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [ImagenBackgroundMask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenBackgroundMask#ImagenBackgroundMask(kotlin.Double))`(dilation: `[Double](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html)`?)` |

|                                                                                                                                                                                                                                                                                                                                                                                                                                                               ### Inherited properties                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| From [com.google.firebase.ai.type.ImagenReferenceImage](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenReferenceImage) |-------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------| | [ImagenInlineImage](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenInlineImage)`?` | [image](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenReferenceImage#image())             | | [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)`?`                                           | [referenceId](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenReferenceImage#referenceId()) | |

## Public constructors

### ImagenBackgroundMask

```
ImagenBackgroundMask(dilation:Â Double? = null)
```  

|                                               Parameters                                               |
|--------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| `dilation: `[Double](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html)`? = null` | the amount to dilate the mask. This can help smooth the borders of an edit and make it seem more convincing. For example, `0.05` will dilate the mask 5%. |