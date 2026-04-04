# Source: https://firebase.google.com/docs/reference/js/ai.imagengenerationconfig.md.txt

Configuration options for generating images with Imagen.

See the [documentation](http://firebase.google.com/docs/vertex-ai/generate-images-imagen) for more details.

**Signature:**  

    export interface ImagenGenerationConfig 

## Properties

|                                                             Property                                                              |                                                        Type                                                        |                                                                                                                                                                                                                                                                                                       Description                                                                                                                                                                                                                                                                                                       |
|-----------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [addWatermark](https://firebase.google.com/docs/reference/js/ai.imagengenerationconfig.md#imagengenerationconfigaddwatermark)     | boolean                                                                                                            | Whether to add an invisible watermark to generated images.If set to `true`, an invisible SynthID watermark is embedded in generated images to indicate that they are AI generated. If set to `false`, watermarking will be disabled.For Imagen 3 models, the default value is `true`; see the [addWatermark](http://firebase.google.com/docs/vertex-ai/model-parameters#imagen) documentation for more details.When using the Gemini Developer API ([GoogleAIBackend](https://firebase.google.com/docs/reference/js/ai.googleaibackend.md#googleaibackend_class)), this will default to true, and cannot be turned off. |
| [aspectRatio](https://firebase.google.com/docs/reference/js/ai.imagengenerationconfig.md#imagengenerationconfigaspectratio)       | [ImagenAspectRatio](https://firebase.google.com/docs/reference/js/ai.md#imagenaspectratio)                         | The aspect ratio of the generated images. The default value is square 1:1. Supported aspect ratios depend on the Imagen model, see [ImagenAspectRatio](https://firebase.google.com/docs/reference/js/ai.md#imagenaspectratio) for more details.                                                                                                                                                                                                                                                                                                                                                                         |
| [imageFormat](https://firebase.google.com/docs/reference/js/ai.imagengenerationconfig.md#imagengenerationconfigimageformat)       | [ImagenImageFormat](https://firebase.google.com/docs/reference/js/ai.imagenimageformat.md#imagenimageformat_class) | The image format of the generated images. The default is PNG.See [ImagenImageFormat](https://firebase.google.com/docs/reference/js/ai.imagenimageformat.md#imagenimageformat_class) for more details.                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [negativePrompt](https://firebase.google.com/docs/reference/js/ai.imagengenerationconfig.md#imagengenerationconfignegativeprompt) | string                                                                                                             | A description of what should be omitted from the generated images.Support for negative prompts depends on the Imagen model.See the [documentation](http://firebase.google.com/docs/vertex-ai/model-parameters#imagen) for more details.This is no longer supported in the Gemini Developer API ([GoogleAIBackend](https://firebase.google.com/docs/reference/js/ai.googleaibackend.md#googleaibackend_class)) in versions greater than `imagen-3.0-generate-002`.                                                                                                                                                       |
| [numberOfImages](https://firebase.google.com/docs/reference/js/ai.imagengenerationconfig.md#imagengenerationconfignumberofimages) | number                                                                                                             | The number of images to generate. The default value is 1.The number of sample images that may be generated in each request depends on the model (typically up to 4); see the [sampleCount](http://firebase.google.com/docs/vertex-ai/model-parameters#imagen) documentation for more details.                                                                                                                                                                                                                                                                                                                           |

## ImagenGenerationConfig.addWatermark

Whether to add an invisible watermark to generated images.

If set to `true`, an invisible SynthID watermark is embedded in generated images to indicate that they are AI generated. If set to `false`, watermarking will be disabled.

For Imagen 3 models, the default value is `true`; see the [addWatermark](http://firebase.google.com/docs/vertex-ai/model-parameters#imagen) documentation for more details.

When using the Gemini Developer API ([GoogleAIBackend](https://firebase.google.com/docs/reference/js/ai.googleaibackend.md#googleaibackend_class)), this will default to true, and cannot be turned off.

**Signature:**  

    addWatermark?: boolean;

## ImagenGenerationConfig.aspectRatio

The aspect ratio of the generated images. The default value is square 1:1. Supported aspect ratios depend on the Imagen model, see [ImagenAspectRatio](https://firebase.google.com/docs/reference/js/ai.md#imagenaspectratio) for more details.

**Signature:**  

    aspectRatio?: ImagenAspectRatio;

## ImagenGenerationConfig.imageFormat

The image format of the generated images. The default is PNG.

See [ImagenImageFormat](https://firebase.google.com/docs/reference/js/ai.imagenimageformat.md#imagenimageformat_class) for more details.

**Signature:**  

    imageFormat?: ImagenImageFormat;

## ImagenGenerationConfig.negativePrompt

A description of what should be omitted from the generated images.

Support for negative prompts depends on the Imagen model.

See the [documentation](http://firebase.google.com/docs/vertex-ai/model-parameters#imagen) for more details.

This is no longer supported in the Gemini Developer API ([GoogleAIBackend](https://firebase.google.com/docs/reference/js/ai.googleaibackend.md#googleaibackend_class)) in versions greater than `imagen-3.0-generate-002`.

**Signature:**  

    negativePrompt?: string;

## ImagenGenerationConfig.numberOfImages

The number of images to generate. The default value is 1.

The number of sample images that may be generated in each request depends on the model (typically up to 4); see the [sampleCount](http://firebase.google.com/docs/vertex-ai/model-parameters#imagen) documentation for more details.

**Signature:**  

    numberOfImages?: number;