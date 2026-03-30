# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/ImagenModel.md.txt

# ImagenModel

# ImagenModel


```
@PublicPreviewAPI
public final class ImagenModel
```

<br />

*** ** * ** ***

> [!CAUTION]
> **This class is deprecated.**   
> The Vertex AI in Firebase SDK (firebase-vertexai) has been replaced with the FirebaseAI SDK (firebase-ai) to accommodate the evolving set of supported features and services. For migration details, see the migration guide: https://firebase.google.com/docs/vertex-ai/migrate-to-latest-sdk

Represents a generative model (like Imagen), capable of generating images based on various input types.

## Summary

| ### Public methods |
|---|---|
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/ImagenGenerationResponse<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/ImagenInlineImage>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/ImagenModel#generateImages(kotlin.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html prompt)` Generates an image, returning the result directly to the caller. |

## Public methods

### generateImages

```
public final @NonNull ImagenGenerationResponse<@NonNull ImagenInlineImage> generateImages(@NonNull String prompt)
```

Generates an image, returning the result directly to the caller.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html prompt` | The input(s) given to the model as a prompt. |