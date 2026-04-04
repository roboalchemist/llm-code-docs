# Source: https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/imagen-safety-settings.md.txt

# Firebase.AI.ImagenSafetySettings Struct Reference

# Firebase.AI.ImagenSafetySettings

Settings for controlling the aggressiveness of filtering out sensitive content.

## Summary

See the [Responsible AI and usage guidelines](https://cloud.google.com/vertex-ai/generative-ai/docs/image/responsible-ai-imagen#config-safety-filters) for more details.

| ### Constructors and Destructors ||
|---|---|
| `https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/imagen-safety-settings#struct_firebase_1_1_a_i_1_1_imagen_safety_settings_1a4605c4032ef2a97495023dd1b3aec0b4(https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/imagen-safety-settings#struct_firebase_1_1_a_i_1_1_imagen_safety_settings_1af395579bebd9268f2d350aa012e56769? safetyFilterLevel, https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/imagen-safety-settings#struct_firebase_1_1_a_i_1_1_imagen_safety_settings_1a9332d84da8da109154ab3fb066c64378? personFilterLevel)` Initializes safety settings for the Imagen model. ||

| ### Public types ||
|---|---|
| `https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/imagen-safety-settings#struct_firebase_1_1_a_i_1_1_imagen_safety_settings_1a9332d84da8da109154ab3fb066c64378{ https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/imagen-safety-settings#struct_firebase_1_1_a_i_1_1_imagen_safety_settings_1a9332d84da8da109154ab3fb066c64378a67f6f87b0f7648202d47f623939d7d9b, https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/imagen-safety-settings#struct_firebase_1_1_a_i_1_1_imagen_safety_settings_1a9332d84da8da109154ab3fb066c64378acd11f81c5cdd45913bafa0e478dd0fab, https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/imagen-safety-settings#struct_firebase_1_1_a_i_1_1_imagen_safety_settings_1a9332d84da8da109154ab3fb066c64378ac31c7129f53f2a590242ce0fa819f931 }` | enumA filter level controlling whether generation of images containing people or faces is allowed. |
| `https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/imagen-safety-settings#struct_firebase_1_1_a_i_1_1_imagen_safety_settings_1af395579bebd9268f2d350aa012e56769{ https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/imagen-safety-settings#struct_firebase_1_1_a_i_1_1_imagen_safety_settings_1af395579bebd9268f2d350aa012e56769a5451a478ab1ea25a26f8f0b5c6bb8a6a, https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/imagen-safety-settings#struct_firebase_1_1_a_i_1_1_imagen_safety_settings_1af395579bebd9268f2d350aa012e56769ae427415fe0f02d9a85081ed93bac3438, https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/imagen-safety-settings#struct_firebase_1_1_a_i_1_1_imagen_safety_settings_1af395579bebd9268f2d350aa012e56769a7295c0405cd90b6aac78f08259e2e731, https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/imagen-safety-settings#struct_firebase_1_1_a_i_1_1_imagen_safety_settings_1af395579bebd9268f2d350aa012e56769a513fe3ab17da44705f9eaecbfcff2504 }` | enumA filter level controlling how aggressively to filter sensitive content. |

## Public types

### PersonFilterLevel

```c#
 Firebase::AI::ImagenSafetySettings::PersonFilterLevel
```
A filter level controlling whether generation of images containing people or faces is allowed.

See the [\`personGeneration\`](https://cloud.google.com/vertex-ai/generative-ai/docs/model-reference/imagen-api#parameter_list) documentation for more details.

| Properties ||
|---|---|
| `AllowAdult` | Allow generation of images containing adults only; images of children are filtered out. Important: Generation of images containing people or faces may require your use case to be reviewed and approved by Cloud support; see the [Responsible AI and usage guidelines](https://cloud.google.com/vertex-ai/generative-ai/docs/image/responsible-ai-imagen#person-face-gen) for more details. |
| `AllowAll` | Allow generation of images containing people of all ages. Important: Generation of images containing people or faces may require your use case to be reviewed and approved; see the [Responsible AI and usage guidelines](https://cloud.google.com/vertex-ai/generative-ai/docs/image/responsible-ai-imagen#person-face-gen) for more details. |
| `BlockAll` | Disallow generation of images containing people or faces; images of people are filtered out. |

### SafetyFilterLevel

```c#
 Firebase::AI::ImagenSafetySettings::SafetyFilterLevel
```
A filter level controlling how aggressively to filter sensitive content.

Text prompts provided as inputs and images (generated or uploaded) through Imagen on Vertex [AI](https://firebase.google.com/docs/reference/unity/namespace/firebase/a-i#namespace_firebase_1_1_a_i) are assessed against a list of safety filters, which include 'harmful categories' (for example, `violence`, `sexual`, `derogatory`, and `toxic`). This filter level controls how aggressively to filter out potentially harmful content from responses. See the [\`safetySetting\`](https://cloud.google.com/vertex-ai/generative-ai/docs/model-reference/imagen-api#parameter_list) documentation and the [Responsible AI and usage guidelines](https://cloud.google.com/vertex-ai/generative-ai/docs/image/responsible-ai-imagen#safety-filters) for more details.

| Properties ||
|---|---|
| `BlockLowAndAbove` | The most aggressive filtering level; most strict blocking. |
| `BlockMediumAndAbove` | Blocks some problematic prompts and responses. |
| `BlockNone` | The least aggressive filtering level; blocks very few problematic prompts and responses. Important: Access to this feature is restricted and may require your use case to be reviewed and approved by Cloud support. |
| `BlockOnlyHigh` | Reduces the number of requests blocked due to safety filters. Important: This may increase objectionable content generated by Imagen. |

## Public functions

### ImagenSafetySettings

```c#
 Firebase::AI::ImagenSafetySettings::ImagenSafetySettings(
  SafetyFilterLevel? safetyFilterLevel,
  PersonFilterLevel? personFilterLevel
)
```
Initializes safety settings for the Imagen model.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `safetyFilterLevel` | A filter level controlling how aggressively to filter out sensitive content from generated images. | | `personFilterLevel` | A filter level controlling whether generation of images containing people or faces is allowed. | |