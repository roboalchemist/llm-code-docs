# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenSubjectReference.md.txt

# ImagenSubjectReference

# ImagenSubjectReference


```
@PublicPreviewAPI
public final class ImagenSubjectReference extends ImagenReferenceImage
```

<br />

|---|---|---|
| [java.lang.Object](https://developer.android.com/reference/kotlin/java/lang/Object.html) |||
| ↳ | [com.google.firebase.ai.type.ImagenReferenceImage](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenReferenceImage) ||
|   | ↳ | [com.google.firebase.ai.type.ImagenSubjectReference](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenSubjectReference) |

*** ** * ** ***

A reference image for generating an image with a specific subject

## Summary

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenSubjectReference#ImagenSubjectReference(com.google.firebase.ai.type.ImagenInlineImage,kotlin.Int,kotlin.String,com.google.firebase.ai.type.ImagenSubjectReferenceType)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenInlineImage image, https://developer.android.com/reference/kotlin/java/lang/Integer.html referenceId, https://developer.android.com/reference/kotlin/java/lang/String.html description, https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenSubjectReferenceType subjectType )` |

| ### Inherited fields |
|---|
| From [com.google.firebase.ai.type.ImagenReferenceImage](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenReferenceImage) |---|---| | `final https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenInlineImage` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenReferenceImage#image()` | | `final https://developer.android.com/reference/kotlin/java/lang/Integer.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenReferenceImage#referenceId()` | |

## Public constructors

### ImagenSubjectReference

```
public ImagenSubjectReference(
    @NonNull ImagenInlineImage image,
    Integer referenceId,
    String description,
    ImagenSubjectReferenceType subjectType
)
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenInlineImage image` | the image of the subject |
| `https://developer.android.com/reference/kotlin/java/lang/Integer.html referenceId` | the reference ID you can use to reference this subject in your prompt |
| `https://developer.android.com/reference/kotlin/java/lang/String.html description` | the description you can use to reference this subject in your prompt |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenSubjectReferenceType subjectType` | the type of the subject |