# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/TemplateImagenModel.md.txt

# TemplateImagenModel

# TemplateImagenModel


```
@PublicPreviewAPI
class TemplateImagenModel
```

<br />

*** ** * ** ***

Represents a generative model (like Imagen), capable of generating images based a template.

See the documentation for a list of [supported models](https://firebase.google.com/docs/ai-logic/models).

## Summary

| ### Public functions |
|---|---|
| `suspend https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenGenerationResponse<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenInlineImage>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/TemplateImagenModel#generateImages(kotlin.String,kotlin.collections.Map)(templateId: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, inputs: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html>)` Generates an image, returning the result directly to the caller. |

## Public functions

### generateImages

```
suspend fun generateImages(templateId: String, inputs: Map<String, Any>): ImagenGenerationResponse<ImagenInlineImage>
```

Generates an image, returning the result directly to the caller.

| Parameters |
|---|---|
| `templateId: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The ID of server prompt template. |
| `inputs: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html>` | the inputs needed to fill in the prompt |