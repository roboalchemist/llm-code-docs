# Source: https://firebase.google.com/docs/reference/js/vertexai.imagengenerationconfig.md.txt

# ImagenGenerationConfig interface

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Configuration options for generating images with Imagen.

See the [documentation](http://firebase.google.com/docs/vertex-ai/generate-images-imagen) for more details.

**Signature:**  

    export interface ImagenGenerationConfig 

## Properties

|                                                                Property                                                                 |                                                           Type                                                           |                                                                                                                                                                                                                                                                                                                     Description                                                                                                                                                                                                                                                                                                                      |
|-----------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [addWatermark](https://firebase.google.com/docs/reference/js/vertexai.imagengenerationconfig.md#imagengenerationconfigaddwatermark)     | boolean                                                                                                                  | ***(Public Preview)*** Whether to add an invisible watermark to generated images.If set to `true`, an invisible SynthID watermark is embedded in generated images to indicate that they are AI generated. If set to `false`, watermarking will be disabled.For Imagen 3 models, the default value is `true`; see the [addWatermark](http://firebase.google.com/docs/vertex-ai/model-parameters#imagen) documentation for more details.When using the Gemini Developer API ([GoogleAIBackend](https://firebase.google.com/docs/reference/js/vertexai.googleaibackend.md#googleaibackend_class)), this will default to true, and cannot be turned off. |
| [aspectRatio](https://firebase.google.com/docs/reference/js/vertexai.imagengenerationconfig.md#imagengenerationconfigaspectratio)       | [ImagenAspectRatio](https://firebase.google.com/docs/reference/js/vertexai.md#imagenaspectratio)                         | ***(Public Preview)*** The aspect ratio of the generated images. The default value is square 1:1. Supported aspect ratios depend on the Imagen model, see [ImagenAspectRatio](https://firebase.google.com/docs/reference/js/vertexai.md#imagenaspectratio) for more details.                                                                                                                                                                                                                                                                                                                                                                         |
| [imageFormat](https://firebase.google.com/docs/reference/js/vertexai.imagengenerationconfig.md#imagengenerationconfigimageformat)       | [ImagenImageFormat](https://firebase.google.com/docs/reference/js/vertexai.imagenimageformat.md#imagenimageformat_class) | ***(Public Preview)*** The image format of the generated images. The default is PNG.See [ImagenImageFormat](https://firebase.google.com/docs/reference/js/vertexai.imagenimageformat.md#imagenimageformat_class) for more details.                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [negativePrompt](https://firebase.google.com/docs/reference/js/vertexai.imagengenerationconfig.md#imagengenerationconfignegativeprompt) | string                                                                                                                   | ***(Public Preview)*** A description of what should be omitted from the generated images.Support for negative prompts depends on the Imagen model.See the [documentation](http://firebase.google.com/docs/vertex-ai/model-parameters#imagen) for more details.This is no longer supported in the Gemini Developer API ([GoogleAIBackend](https://firebase.google.com/docs/reference/js/vertexai.googleaibackend.md#googleaibackend_class)) in versions greater than `imagen-3.0-generate-002`.                                                                                                                                                       |
| [numberOfImages](https://firebase.google.com/docs/reference/js/vertexai.imagengenerationconfig.md#imagengenerationconfignumberofimages) | number                                                                                                                   | ***(Public Preview)*** The number of images to generate. The default value is 1.The number of sample images that may be generated in each request depends on the model (typically up to 4); see the [sampleCount](http://firebase.google.com/docs/vertex-ai/model-parameters#imagen) documentation for more details.                                                                                                                                                                                                                                                                                                                                 |

## ImagenGenerationConfig.addWatermark

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Whether to add an invisible watermark to generated images.

If set to `true`, an invisible SynthID watermark is embedded in generated images to indicate that they are AI generated. If set to `false`, watermarking will be disabled.

For Imagen 3 models, the default value is `true`; see the [addWatermark](http://firebase.google.com/docs/vertex-ai/model-parameters#imagen) documentation for more details.

When using the Gemini Developer API ([GoogleAIBackend](https://firebase.google.com/docs/reference/js/vertexai.googleaibackend.md#googleaibackend_class)), this will default to true, and cannot be turned off.

**Signature:**  

    addWatermark?: boolean;

## ImagenGenerationConfig.aspectRatio

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

The aspect ratio of the generated images. The default value is square 1:1. Supported aspect ratios depend on the Imagen model, see [ImagenAspectRatio](https://firebase.google.com/docs/reference/js/vertexai.md#imagenaspectratio) for more details.

**Signature:**  

    aspectRatio?: ImagenAspectRatio;

## ImagenGenerationConfig.imageFormat

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

The image format of the generated images. The default is PNG.

See [ImagenImageFormat](https://firebase.google.com/docs/reference/js/vertexai.imagenimageformat.md#imagenimageformat_class) for more details.

**Signature:**  

    imageFormat?: ImagenImageFormat;

## ImagenGenerationConfig.negativePrompt

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

A description of what should be omitted from the generated images.

Support for negative prompts depends on the Imagen model.

See the [documentation](http://firebase.google.com/docs/vertex-ai/model-parameters#imagen) for more details.

This is no longer supported in the Gemini Developer API ([GoogleAIBackend](https://firebase.google.com/docs/reference/js/vertexai.googleaibackend.md#googleaibackend_class)) in versions greater than `imagen-3.0-generate-002`.

**Signature:**  

    negativePrompt?: string;

## ImagenGenerationConfig.numberOfImages

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

The number of images to generate. The default value is 1.

The number of sample images that may be generated in each request depends on the model (typically up to 4); see the [sampleCount](http://firebase.google.com/docs/vertex-ai/model-parameters#imagen) documentation for more details.

**Signature:**  

    numberOfImages?: number;