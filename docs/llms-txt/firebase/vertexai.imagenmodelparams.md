# Source: https://firebase.google.com/docs/reference/js/vertexai.imagenmodelparams.md.txt

# ImagenModelParams interface

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Parameters for configuring an [ImagenModel](https://firebase.google.com/docs/reference/js/vertexai.imagenmodel.md#imagenmodel_class).

**Signature:**  

    export interface ImagenModelParams 

## Properties

|                                                             Property                                                              |                                                                    Type                                                                     |                                                                                                                                         Description                                                                                                                                          |
|-----------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [generationConfig](https://firebase.google.com/docs/reference/js/vertexai.imagenmodelparams.md#imagenmodelparamsgenerationconfig) | [ImagenGenerationConfig](https://firebase.google.com/docs/reference/js/vertexai.imagengenerationconfig.md#imagengenerationconfig_interface) | ***(Public Preview)*** Configuration options for generating images with Imagen.                                                                                                                                                                                                              |
| [model](https://firebase.google.com/docs/reference/js/vertexai.imagenmodelparams.md#imagenmodelparamsmodel)                       | string                                                                                                                                      | ***(Public Preview)*** The Imagen model to use for generating images. For example: `imagen-3.0-generate-002`.Only Imagen 3 models (named `imagen-3.0-*`) are supported.See [model versions](https://firebase.google.com/docs/vertex-ai/models) for a full list of supported Imagen 3 models. |
| [safetySettings](https://firebase.google.com/docs/reference/js/vertexai.imagenmodelparams.md#imagenmodelparamssafetysettings)     | [ImagenSafetySettings](https://firebase.google.com/docs/reference/js/vertexai.imagensafetysettings.md#imagensafetysettings_interface)       | ***(Public Preview)*** Safety settings for filtering potentially inappropriate content.                                                                                                                                                                                                      |

## ImagenModelParams.generationConfig

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Configuration options for generating images with Imagen.

**Signature:**  

    generationConfig?: ImagenGenerationConfig;

## ImagenModelParams.model

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

The Imagen model to use for generating images. For example: `imagen-3.0-generate-002`.

Only Imagen 3 models (named `imagen-3.0-*`) are supported.

See [model versions](https://firebase.google.com/docs/vertex-ai/models) for a full list of supported Imagen 3 models.

**Signature:**  

    model: string;

## ImagenModelParams.safetySettings

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Safety settings for filtering potentially inappropriate content.

**Signature:**  

    safetySettings?: ImagenSafetySettings;