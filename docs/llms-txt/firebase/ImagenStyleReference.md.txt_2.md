# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenStyleReference.md.txt

# ImagenStyleReference

# ImagenStyleReference


```
@PublicPreviewAPI
class ImagenStyleReference : ImagenReferenceImage
```

<br />

|---|---|---|
| [kotlin.Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html) |||
| ↳ | [com.google.firebase.ai.type.ImagenReferenceImage](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenReferenceImage) ||
|   | ↳ | [com.google.firebase.ai.type.ImagenStyleReference](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenStyleReference) |

*** ** * ** ***

A reference image for style transfer

## Summary

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenStyleReference#ImagenStyleReference(com.google.firebase.ai.type.ImagenInlineImage,kotlin.Int,kotlin.String)( image: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenInlineImage, referenceId: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html?, description: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html? )` |

| ### Inherited properties |
|---|
| From [com.google.firebase.ai.type.ImagenReferenceImage](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenReferenceImage) |---|---| | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenInlineImage?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenReferenceImage#image()` | | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenReferenceImage#referenceId()` | |

## Public constructors

### ImagenStyleReference

```
ImagenStyleReference(
    image: ImagenInlineImage,
    referenceId: Int? = null,
    description: String? = null
)
```

| Parameters |
|---|---|
| `image: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenInlineImage` | the image representing the style you want to transfer to your original images |
| `referenceId: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html? = null` | the reference ID you can use to reference this style in your prompt |
| `description: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html? = null` | the description you can use to reference this style in your prompt |