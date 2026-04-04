# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenReferenceImage.md.txt

# ImagenReferenceImage

# ImagenReferenceImage


```
@PublicPreviewAPI
abstract class ImagenReferenceImage
```

<br />

Known direct subclasses [ImagenControlReference](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenControlReference), [ImagenMaskReference](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenMaskReference), [ImagenRawImage](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenRawImage), [ImagenStyleReference](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenStyleReference), [ImagenSubjectReference](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenSubjectReference)

|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenControlReference` | Represents a reference image (provided or generated) to bound the created image via controlled generation. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenMaskReference` | Represents a mask for Imagen editing. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenRawImage` | Represents a base image for Imagen editing |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenStyleReference` | A reference image for style transfer |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenSubjectReference` | A reference image for generating an image with a specific subject |

Known indirect subclasses [ImagenBackgroundMask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenBackgroundMask), [ImagenForegroundMask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenForegroundMask), [ImagenRawMask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenRawMask), [ImagenSemanticMask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenSemanticMask)

|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenBackgroundMask` | A generated mask image which will auto-detect and mask out the background. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenForegroundMask` | A generated mask image which will auto-detect and mask out the foreground. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenRawMask` | Represents a mask for Imagen editing. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenSemanticMask` | Represents a generated mask for Imagen editing which masks out certain objects using object detection. |

*** ** * ** ***

Represents an reference image for an Imagen editing request

## Summary

| ### Public properties |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenInlineImage?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenReferenceImage#image()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenReferenceImage#referenceId()` |

## Public properties

### image

```
val image: ImagenInlineImage?
```

### referenceId

```
val referenceId: Int?
```