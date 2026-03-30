# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenSubjectReference.md.txt

# ImagenSubjectReference

# ImagenSubjectReference


```
@PublicPreviewAPI
class ImagenSubjectReference : ImagenReferenceImage
```

<br />

|---|---|---|
| [kotlin.Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html) |||
| ↳ | [com.google.firebase.ai.type.ImagenReferenceImage](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenReferenceImage) ||
|   | ↳ | [com.google.firebase.ai.type.ImagenSubjectReference](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenSubjectReference) |

*** ** * ** ***

A reference image for generating an image with a specific subject

## Summary

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenSubjectReference#ImagenSubjectReference(com.google.firebase.ai.type.ImagenInlineImage,kotlin.Int,kotlin.String,com.google.firebase.ai.type.ImagenSubjectReferenceType)( image: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenInlineImage, referenceId: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html?, description: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?, subjectType: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenSubjectReferenceType? )` |

| ### Inherited properties |
|---|
| From [com.google.firebase.ai.type.ImagenReferenceImage](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenReferenceImage) |---|---| | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenInlineImage?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenReferenceImage#image()` | | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenReferenceImage#referenceId()` | |

## Public constructors

### ImagenSubjectReference

```
ImagenSubjectReference(
    image: ImagenInlineImage,
    referenceId: Int? = null,
    description: String? = null,
    subjectType: ImagenSubjectReferenceType? = null
)
```

| Parameters |
|---|---|
| `image: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenInlineImage` | the image of the subject |
| `referenceId: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html? = null` | the reference ID you can use to reference this subject in your prompt |
| `description: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html? = null` | the description you can use to reference this subject in your prompt |
| `subjectType: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenSubjectReferenceType? = null` | the type of the subject |