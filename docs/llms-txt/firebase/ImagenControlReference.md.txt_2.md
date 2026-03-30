# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenControlReference.md.txt

# ImagenControlReference

# ImagenControlReference


```
@PublicPreviewAPI
class ImagenControlReference : ImagenReferenceImage
```

<br />

|---|---|---|
| [kotlin.Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html) |||
| ↳ | [com.google.firebase.ai.type.ImagenReferenceImage](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenReferenceImage) ||
|   | ↳ | [com.google.firebase.ai.type.ImagenControlReference](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenControlReference) |

*** ** * ** ***

Represents a reference image (provided or generated) to bound the created image via controlled generation.

## Summary

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenControlReference#ImagenControlReference(com.google.firebase.ai.type.ImagenControlType,com.google.firebase.ai.type.ImagenInlineImage,kotlin.Int,kotlin.Boolean,kotlin.Int,kotlin.Int)( type: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenControlType, image: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenInlineImage?, referenceId: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html?, enableComputation: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html?, superpixelRegionSize: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html?, superpixelRuler: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html? )` |

| ### Inherited properties |
|---|
| From [com.google.firebase.ai.type.ImagenReferenceImage](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenReferenceImage) |---|---| | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenInlineImage?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenReferenceImage#image()` | | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenReferenceImage#referenceId()` | |

## Public constructors

### ImagenControlReference

```
ImagenControlReference(
    type: ImagenControlType,
    image: ImagenInlineImage? = null,
    referenceId: Int? = null,
    enableComputation: Boolean? = null,
    superpixelRegionSize: Int? = null,
    superpixelRuler: Int? = null
)
```

| Parameters |
|---|---|
| `type: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenControlType` | the type of control reference image |
| `image: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenInlineImage? = null` | the image provided, required if `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenControlReference#<init>(com.google.firebase.ai.type.ImagenControlType,com.google.firebase.ai.type.ImagenInlineImage,kotlin.Int,kotlin.Boolean,kotlin.Int,kotlin.Int)` is false |
| `referenceId: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html? = null` | the reference ID for this image, to be referenced in the prompt |
| `enableComputation: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html? = null` | requests that the reference image be generated serverside instead of provided |
| `superpixelRegionSize: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html? = null` | if type is `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenControlType.Companion#COLOR_SUPERPIXEL()` and `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenControlReference#<init>(com.google.firebase.ai.type.ImagenControlType,com.google.firebase.ai.type.ImagenInlineImage,kotlin.Int,kotlin.Boolean,kotlin.Int,kotlin.Int)` is true, this will control the size of each superpixel region in pixels for the generated referenced image |
| `superpixelRuler: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html? = null` | if type is `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenControlType.Companion#COLOR_SUPERPIXEL()` and `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenControlReference#<init>(com.google.firebase.ai.type.ImagenControlType,com.google.firebase.ai.type.ImagenInlineImage,kotlin.Int,kotlin.Boolean,kotlin.Int,kotlin.Int)` is true, this will control the superpixel smoothness factor for the generated referenced image |