# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenSubjectReference.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenSubjectReference.md.txt

# ImagenSubjectReference

# ImagenSubjectReference


```
@PublicPreviewAPI
class ImagenSubjectReference : ImagenReferenceImage
```

<br />

|---|---|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [kotlin.Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)                                                                                |||
| â³ | [com.google.firebase.ai.type.ImagenReferenceImage](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenReferenceImage)        ||
|   | â³ | [com.google.firebase.ai.type.ImagenSubjectReference](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenSubjectReference) |

*** ** * ** ***

A reference image for generating an image with a specific subject

## Summary

|                                                                                                                                                                                                                                                                                                                                                                                   ### Public constructors                                                                                                                                                                                                                                                                                                                                                                                   |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [ImagenSubjectReference](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenSubjectReference#ImagenSubjectReference(com.google.firebase.ai.type.ImagenInlineImage,kotlin.Int,kotlin.String,com.google.firebase.ai.type.ImagenSubjectReferenceType))`(` ` image: `[ImagenInlineImage](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenInlineImage)`,` ` referenceId: `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)`?,` ` description: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?,` ` subjectType: `[ImagenSubjectReferenceType](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenSubjectReferenceType)`?` `)` |

|                                                                                                                                                                                                                                                                                                                                                                                                                                                               ### Inherited properties                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| From [com.google.firebase.ai.type.ImagenReferenceImage](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenReferenceImage) |-------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------| | [ImagenInlineImage](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenInlineImage)`?` | [image](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenReferenceImage#image())             | | [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)`?`                                           | [referenceId](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenReferenceImage#referenceId()) | |

## Public constructors

### ImagenSubjectReference

```
ImagenSubjectReference(
Â Â Â Â image:Â ImagenInlineImage,
Â Â Â Â referenceId:Â Int? = null,
Â Â Â Â description:Â String? = null,
Â Â Â Â subjectType:Â ImagenSubjectReferenceType? = null
)
```  

|                                                                           Parameters                                                                            |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------|
| `image: `[ImagenInlineImage](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenInlineImage)                                   | the image of the subject                                              |
| `referenceId: `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)`? = null`                                                             | the reference ID you can use to reference this subject in your prompt |
| `description: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`? = null`                                                       | the description you can use to reference this subject in your prompt  |
| `subjectType: `[ImagenSubjectReferenceType](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenSubjectReferenceType)`? = null` | the type of the subject                                               |