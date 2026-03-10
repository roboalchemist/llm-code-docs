# Source: https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/imagen-generation-config.md.txt

# Firebase.AI.ImagenGenerationConfig Struct Reference

# Firebase.AI.ImagenGenerationConfig

Configuration options for generating images with Imagen.

## Summary

See [Parameters for Imagen models](https://firebase.google.com/docs/vertex-ai/model-parameters?platform=unity#imagen) to learn about parameters available for use with Imagen models, including how to configure them.

| ### Constructors and Destructors ||
|---|---|
| `https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/imagen-generation-config#struct_firebase_1_1_a_i_1_1_imagen_generation_config_1ad040d03b1e3ae4f6f57917d855396df1(string negativePrompt, int? numberOfImages, https://firebase.google.com/docs/reference/unity/namespace/firebase/a-i#namespace_firebase_1_1_a_i_1a5d5f4e589e2b1874e727d94c55a014f2? aspectRatio, https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/imagen-image-format#struct_firebase_1_1_a_i_1_1_imagen_image_format? imageFormat, bool? addWatermark)` Initializes configuration options for generating images with Imagen. ||

## Public functions

### ImagenGenerationConfig

```c#
 Firebase::AI::ImagenGenerationConfig::ImagenGenerationConfig(
  string negativePrompt,
  int? numberOfImages,
  ImagenAspectRatio? aspectRatio,
  ImagenImageFormat? imageFormat,
  bool? addWatermark
)
```
Initializes configuration options for generating images with Imagen.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `negativePrompt` | Specifies elements to exclude from the generated image; disabled if not specified. | | `numberOfImages` | The number of image samples to generate; defaults to 1 if not specified. | | `aspectRatio` | The aspect ratio of generated images; defaults to to square, 1:1. | | `imageFormat` | The image format of generated images; defaults to PNG. | | `addWatermark` | Whether to add an invisible watermark to generated images; the default value depends on the model. | |