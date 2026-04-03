# Source: https://firebase.google.com/docs/reference/js/ai.imagenmodel.md.txt

Class for Imagen model APIs.

This class provides methods for generating images using the Imagen model.

**Signature:**  

    export declare class ImagenModel extends AIModel 

**Extends:** [AIModel](https://firebase.google.com/docs/reference/js/ai.aimodel.md#aimodel_class)

## Constructors

|                                                               Constructor                                                                | Modifiers |                                                               Description                                                                |
|------------------------------------------------------------------------------------------------------------------------------------------|-----------|------------------------------------------------------------------------------------------------------------------------------------------|
| [(constructor)(ai, modelParams, requestOptions)](https://firebase.google.com/docs/reference/js/ai.imagenmodel.md#imagenmodelconstructor) |           | Constructs a new instance of the [ImagenModel](https://firebase.google.com/docs/reference/js/ai.imagenmodel.md#imagenmodel_class) class. |

## Properties

|                                                    Property                                                     | Modifiers |                                                                 Type                                                                  |                     Description                      |
|-----------------------------------------------------------------------------------------------------------------|-----------|---------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------|
| [generationConfig](https://firebase.google.com/docs/reference/js/ai.imagenmodel.md#imagenmodelgenerationconfig) |           | [ImagenGenerationConfig](https://firebase.google.com/docs/reference/js/ai.imagengenerationconfig.md#imagengenerationconfig_interface) | The Imagen generation configuration.                 |
| [requestOptions](https://firebase.google.com/docs/reference/js/ai.imagenmodel.md#imagenmodelrequestoptions)     |           | [RequestOptions](https://firebase.google.com/docs/reference/js/ai.requestoptions.md#requestoptions_interface) \| undefined            |                                                      |
| [safetySettings](https://firebase.google.com/docs/reference/js/ai.imagenmodel.md#imagenmodelsafetysettings)     |           | [ImagenSafetySettings](https://firebase.google.com/docs/reference/js/ai.imagensafetysettings.md#imagensafetysettings_interface)       | Safety settings for filtering inappropriate content. |

## Methods

|                                                       Method                                                        | Modifiers |                                     Description                                     |
|---------------------------------------------------------------------------------------------------------------------|-----------|-------------------------------------------------------------------------------------|
| [generateImages(prompt)](https://firebase.google.com/docs/reference/js/ai.imagenmodel.md#imagenmodelgenerateimages) |           | Generates images using the Imagen model and returns them as base64-encoded strings. |

## ImagenModel.(constructor)

Constructs a new instance of the [ImagenModel](https://firebase.google.com/docs/reference/js/ai.imagenmodel.md#imagenmodel_class) class.

**Signature:**  

    constructor(ai: AI, modelParams: ImagenModelParams, requestOptions?: RequestOptions | undefined);

#### Parameters

|   Parameter    |                                                            Type                                                            |                                      Description                                       |
|----------------|----------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| ai             | [AI](https://firebase.google.com/docs/reference/js/ai.ai.md#ai_interface)                                                  | an [AI](https://firebase.google.com/docs/reference/js/ai.ai.md#ai_interface) instance. |
| modelParams    | [ImagenModelParams](https://firebase.google.com/docs/reference/js/ai.imagenmodelparams.md#imagenmodelparams_interface)     | Parameters to use when making requests to Imagen.                                      |
| requestOptions | [RequestOptions](https://firebase.google.com/docs/reference/js/ai.requestoptions.md#requestoptions_interface) \| undefined | Additional options to use when making requests.                                        |

#### Exceptions

If the `apiKey` or `projectId` fields are missing in your Firebase config.

## ImagenModel.generationConfig

The Imagen generation configuration.

**Signature:**  

    generationConfig?: ImagenGenerationConfig;

## ImagenModel.requestOptions

**Signature:**  

    requestOptions?: RequestOptions | undefined;

## ImagenModel.safetySettings

Safety settings for filtering inappropriate content.

**Signature:**  

    safetySettings?: ImagenSafetySettings;

## ImagenModel.generateImages()

Generates images using the Imagen model and returns them as base64-encoded strings.

If the prompt was not blocked, but one or more of the generated images were filtered, the returned object will have a `filteredReason` property. If all images are filtered, the `images` array will be empty.

**Signature:**  

    generateImages(prompt: string): Promise<ImagenGenerationResponse<ImagenInlineImage>>;

#### Parameters

| Parameter |  Type  |                    Description                     |
|-----------|--------|----------------------------------------------------|
| prompt    | string | A text prompt describing the image(s) to generate. |

**Returns:**

Promise\<[ImagenGenerationResponse](https://firebase.google.com/docs/reference/js/ai.imagengenerationresponse.md#imagengenerationresponse_interface)\<[ImagenInlineImage](https://firebase.google.com/docs/reference/js/ai.imageninlineimage.md#imageninlineimage_interface)\>\>

A promise that resolves to an [ImagenGenerationResponse](https://firebase.google.com/docs/reference/js/ai.imagengenerationresponse.md#imagengenerationresponse_interface) object containing the generated images.

#### Exceptions

If the request to generate images fails. This happens if the prompt is blocked.

### Example

    const imagen = new ImagenModel(
      ai,
      {
        model: 'imagen-3.0-generate-002'
      }
    );

    const response = await imagen.generateImages('A photo of a cat');
    if (response.images.length > 0) {
      console.log(response.images[0].bytesBase64Encoded);
    }