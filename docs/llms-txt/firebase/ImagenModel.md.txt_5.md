# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/ImagenModel.md.txt

# ImagenModel

# ImagenModel


```
@PublicPreviewAPI
class ImagenModel
```

<br />

*** ** * ** ***

> [!CAUTION]
> **This class is deprecated.**   
> The Vertex AI in Firebase SDK (firebase-vertexai) has been replaced with the FirebaseAI SDK (firebase-ai) to accommodate the evolving set of supported features and services. For migration details, see the migration guide: https://firebase.google.com/docs/vertex-ai/migrate-to-latest-sdk

Represents a generative model (like Imagen), capable of generating images based on various input types.

## Summary

| ### Public functions |
|---|---|
| `suspend https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/ImagenGenerationResponse<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/ImagenInlineImage>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/ImagenModel#generateImages(kotlin.String)(prompt: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Generates an image, returning the result directly to the caller. |

## Public functions

### generateImages

```
suspend fun generateImages(prompt: String): ImagenGenerationResponse<ImagenInlineImage>
```

Generates an image, returning the result directly to the caller.

| Parameters |
|---|---|
| `prompt: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The input(s) given to the model as a prompt. |