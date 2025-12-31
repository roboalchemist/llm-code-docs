# Source: https://firebase.google.com/docs/reference/js/ai.imagenmodelparams.md.txt

Parameters for configuring an [ImagenModel](https://firebase.google.com/docs/reference/js/ai.imagenmodel.md#imagenmodel_class).

**Signature:**  

    export interface ImagenModelParams 

## Properties

|                                                          Property                                                           |                                                                 Type                                                                  |                                                                                                                              Description                                                                                                                              |
|-----------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [generationConfig](https://firebase.google.com/docs/reference/js/ai.imagenmodelparams.md#imagenmodelparamsgenerationconfig) | [ImagenGenerationConfig](https://firebase.google.com/docs/reference/js/ai.imagengenerationconfig.md#imagengenerationconfig_interface) | Configuration options for generating images with Imagen.                                                                                                                                                                                                              |
| [model](https://firebase.google.com/docs/reference/js/ai.imagenmodelparams.md#imagenmodelparamsmodel)                       | string                                                                                                                                | The Imagen model to use for generating images. For example: `imagen-3.0-generate-002`.Only Imagen 3 models (named `imagen-3.0-*`) are supported.See [model versions](https://firebase.google.com/docs/vertex-ai/models) for a full list of supported Imagen 3 models. |
| [safetySettings](https://firebase.google.com/docs/reference/js/ai.imagenmodelparams.md#imagenmodelparamssafetysettings)     | [ImagenSafetySettings](https://firebase.google.com/docs/reference/js/ai.imagensafetysettings.md#imagensafetysettings_interface)       | Safety settings for filtering potentially inappropriate content.                                                                                                                                                                                                      |

## ImagenModelParams.generationConfig

Configuration options for generating images with Imagen.

**Signature:**  

    generationConfig?: ImagenGenerationConfig;

## ImagenModelParams.model

The Imagen model to use for generating images. For example: `imagen-3.0-generate-002`.

Only Imagen 3 models (named `imagen-3.0-*`) are supported.

See [model versions](https://firebase.google.com/docs/vertex-ai/models) for a full list of supported Imagen 3 models.

**Signature:**  

    model: string;

## ImagenModelParams.safetySettings

Safety settings for filtering potentially inappropriate content.

**Signature:**  

    safetySettings?: ImagenSafetySettings;