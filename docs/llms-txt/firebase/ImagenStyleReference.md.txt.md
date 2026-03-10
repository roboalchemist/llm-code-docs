# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenStyleReference.md.txt

# ImagenStyleReference

# ImagenStyleReference


```
@PublicPreviewAPI
public final class ImagenStyleReference extends ImagenReferenceImage
```

<br />

|---|---|---|
| [java.lang.Object](https://developer.android.com/reference/kotlin/java/lang/Object.html) |||
| ↳ | [com.google.firebase.ai.type.ImagenReferenceImage](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenReferenceImage) ||
|   | ↳ | [com.google.firebase.ai.type.ImagenStyleReference](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenStyleReference) |

*** ** * ** ***

A reference image for style transfer

## Summary

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenStyleReference#ImagenStyleReference(com.google.firebase.ai.type.ImagenInlineImage,kotlin.Int,kotlin.String)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenInlineImage image, https://developer.android.com/reference/kotlin/java/lang/Integer.html referenceId, https://developer.android.com/reference/kotlin/java/lang/String.html description )` |

| ### Inherited fields |
|---|
| From [com.google.firebase.ai.type.ImagenReferenceImage](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenReferenceImage) |---|---| | `final https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenInlineImage` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenReferenceImage#image()` | | `final https://developer.android.com/reference/kotlin/java/lang/Integer.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenReferenceImage#referenceId()` | |

## Public constructors

### ImagenStyleReference

```
public ImagenStyleReference(
    @NonNull ImagenInlineImage image,
    Integer referenceId,
    String description
)
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenInlineImage image` | the image representing the style you want to transfer to your original images |
| `https://developer.android.com/reference/kotlin/java/lang/Integer.html referenceId` | the reference ID you can use to reference this style in your prompt |
| `https://developer.android.com/reference/kotlin/java/lang/String.html description` | the description you can use to reference this style in your prompt |