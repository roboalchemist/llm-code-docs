# Source: https://firebase.google.com/docs/reference/unity/class/firebase/a-i/template-imagen-model.md.txt

# Firebase.AI.TemplateImagenModel Class Reference

# Firebase.AI.TemplateImagenModel

Represents a remote Imagen model with the ability to generate images using server template prompts.

## Summary

| ### Public functions ||
|---|---|
| `https://firebase.google.com/docs/reference/unity/class/firebase/a-i/template-imagen-model#class_firebase_1_1_a_i_1_1_template_imagen_model_1a4e7e642f9350bbd9a0ced31c6fd06f54(string templateId, IDictionary< string, object > inputs, CancellationToken cancellationToken)` | `async Task< ImagenGenerationResponse< https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/imagen-inline-image#struct_firebase_1_1_a_i_1_1_imagen_inline_image > >` Generates images using the Template Imagen model and returns them as inline data. |

## Public functions

### GenerateImagesAsync

```c#
async Task< ImagenGenerationResponse< ImagenInlineImage > > GenerateImagesAsync(
  string templateId,
  IDictionary< string, object > inputs,
  CancellationToken cancellationToken
)
```
Generates images using the Template Imagen model and returns them as inline data.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `templateId` | The id of the server prompt template to use. | | `inputs` | Any input parameters expected by the server prompt template. | | `cancellationToken` | An optional token to cancel the operation. | |
| Exceptions | |---|---| | `HttpRequestException` | Thrown when an error occurs during content generation. | |
| **Returns** | The generated content response from the model. |