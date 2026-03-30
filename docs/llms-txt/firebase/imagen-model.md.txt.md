# Source: https://firebase.google.com/docs/reference/unity/class/firebase/a-i/imagen-model.md.txt

# Firebase.AI.ImagenModel Class Reference

# Firebase.AI.ImagenModel

Represents a remote Imagen model with the ability to generate images using text prompts.

## Summary

See the [generate images documentation](https://firebase.google.com/docs/vertex-ai/generate-images-imagen?platform=unity) for more details about the image generation capabilities offered by the Imagen model in the [Firebase](https://firebase.google.com/docs/reference/unity/namespace/firebase#namespace_firebase)[AI](https://firebase.google.com/docs/reference/unity/namespace/firebase/a-i#namespace_firebase_1_1_a_i) SDK SDK.

| ### Public functions ||
|---|---|
| `https://firebase.google.com/docs/reference/unity/class/firebase/a-i/imagen-model#class_firebase_1_1_a_i_1_1_imagen_model_1a2b4250567f13d08014d733880a0ee228(string prompt, CancellationToken cancellationToken)` | `Task< ImagenGenerationResponse< https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/imagen-inline-image#struct_firebase_1_1_a_i_1_1_imagen_inline_image > >` Generates images using the Imagen model and returns them as inline data. |

## Public functions

### GenerateImagesAsync

```c#
Task< ImagenGenerationResponse< ImagenInlineImage > > GenerateImagesAsync(
  string prompt,
  CancellationToken cancellationToken
)
```
Generates images using the Imagen model and returns them as inline data.

Warning: For [Firebase](https://firebase.google.com/docs/reference/unity/namespace/firebase#namespace_firebase)[AI](https://firebase.google.com/docs/reference/unity/namespace/firebase/a-i#namespace_firebase_1_1_a_i) SDK, image generation using Imagen 3 models is in Public Preview, which means that the feature is not subject to any SLA or deprecation policy and could change in backwards-incompatible ways.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `prompt` | A text prompt describing the image(s) to generate. | | `cancellationToken` | An optional token to cancel the operation. | |
| Exceptions | |---|---| | `HttpRequestException` | Thrown when an error occurs during content generation. | |
| **Returns** | The generated content response from the model. |