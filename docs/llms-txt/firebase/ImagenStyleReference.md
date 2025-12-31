# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenStyleReference.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenStyleReference.md.txt

# ImagenStyleReference

# ImagenStyleReference


```
@PublicPreviewAPI
class ImagenStyleReference : ImagenReferenceImage
```

<br />

|---|---|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| [kotlin.Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)                                                                            |||
| â³ | [com.google.firebase.ai.type.ImagenReferenceImage](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenReferenceImage)    ||
|   | â³ | [com.google.firebase.ai.type.ImagenStyleReference](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenStyleReference) |

*** ** * ** ***

A reference image for style transfer

## Summary

|                                                                                                                                                                                                                                                                       ### Public constructors                                                                                                                                                                                                                                                                       |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [ImagenStyleReference](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenStyleReference#ImagenStyleReference(com.google.firebase.ai.type.ImagenInlineImage,kotlin.Int,kotlin.String))`(` ` image: `[ImagenInlineImage](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenInlineImage)`,` ` referenceId: `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)`?,` ` description: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?` `)` |

|                                                                                                                                                                                                                                                                                                                                                                                                                                                               ### Inherited properties                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| From [com.google.firebase.ai.type.ImagenReferenceImage](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenReferenceImage) |-------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------| | [ImagenInlineImage](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenInlineImage)`?` | [image](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenReferenceImage#image())             | | [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)`?`                                           | [referenceId](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenReferenceImage#referenceId()) | |

## Public constructors

### ImagenStyleReference

```
ImagenStyleReference(
Â Â Â Â image:Â ImagenInlineImage,
Â Â Â Â referenceId:Â Int? = null,
Â Â Â Â description:Â String? = null
)
```  

|                                                          Parameters                                                           |
|-------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------|
| `image: `[ImagenInlineImage](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenInlineImage) | the image representing the style you want to transfer to your original images |
| `referenceId: `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)`? = null`                           | the reference ID you can use to reference this style in your prompt           |
| `description: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`? = null`                     | the description you can use to reference this style in your prompt            |