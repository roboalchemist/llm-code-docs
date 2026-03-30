# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ai/TemplateImagenModel.md.txt

# TemplateImagenModel

# TemplateImagenModel


```
@PublicPreviewAPI
public final class TemplateImagenModel
```

<br />

*** ** * ** ***

Represents a generative model (like Imagen), capable of generating images based a template.

See the documentation for a list of [supported models](https://firebase.google.com/docs/ai-logic/models).

## Summary

| ### Public methods |
|---|---|
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenGenerationResponse<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenInlineImage>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/TemplateImagenModel#generateImages(kotlin.String,kotlin.collections.Map)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html templateId, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/Map.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Object.html> inputs )` Generates an image, returning the result directly to the caller. |

## Public methods

### generateImages

```
public final @NonNull ImagenGenerationResponse<@NonNull ImagenInlineImage> generateImages(
    @NonNull String templateId,
    @NonNull Map<@NonNull String, @NonNull Object> inputs
)
```

Generates an image, returning the result directly to the caller.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html templateId` | The ID of server prompt template. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/Map.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Object.html> inputs` | the inputs needed to fill in the prompt |