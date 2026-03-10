# Source: https://firebase.google.com/docs/reference/js/ai.templateimagenmodel.md.txt

# TemplateImagenModel class

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Class for Imagen model APIs that execute on a server-side template.

This class should only be instantiated with [getTemplateImagenModel()](https://firebase.google.com/docs/reference/js/ai.md#gettemplateimagenmodel_9476bbc).

**Signature:**

    export declare class TemplateImagenModel 

## Constructors

| Constructor | Modifiers | Description |
|---|---|---|
| [(constructor)(ai, requestOptions)](https://firebase.google.com/docs/reference/js/ai.templateimagenmodel.md#templateimagenmodelconstructor) |   | ***(Public Preview)*** Constructs a new instance of the `TemplateImagenModel` class |

## Properties

| Property | Modifiers | Type | Description |
|---|---|---|---|
| [requestOptions](https://firebase.google.com/docs/reference/js/ai.templateimagenmodel.md#templateimagenmodelrequestoptions) |   | [RequestOptions](https://firebase.google.com/docs/reference/js/ai.requestoptions.md#requestoptions_interface) | ***(Public Preview)*** Additional options to use when making requests. |

## Methods

| Method | Modifiers | Description |
|---|---|---|
| [generateImages(templateId, templateVariables, singleRequestOptions)](https://firebase.google.com/docs/reference/js/ai.templateimagenmodel.md#templateimagenmodelgenerateimages) |   | ***(Public Preview)*** Makes a single call to the model and returns an object containing a single [ImagenGenerationResponse](https://firebase.google.com/docs/reference/js/ai.imagengenerationresponse.md#imagengenerationresponse_interface). |

## TemplateImagenModel.(constructor)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Constructs a new instance of the `TemplateImagenModel` class

**Signature:**

    constructor(ai: AI, requestOptions?: RequestOptions);

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| ai | [AI](https://firebase.google.com/docs/reference/js/ai.ai.md#ai_interface) |   |
| requestOptions | [RequestOptions](https://firebase.google.com/docs/reference/js/ai.requestoptions.md#requestoptions_interface) |   |

## TemplateImagenModel.requestOptions

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Additional options to use when making requests.

**Signature:**

    requestOptions?: RequestOptions;

## TemplateImagenModel.generateImages()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Makes a single call to the model and returns an object containing a single [ImagenGenerationResponse](https://firebase.google.com/docs/reference/js/ai.imagengenerationresponse.md#imagengenerationresponse_interface).

**Signature:**

    generateImages(templateId: string, templateVariables: object, singleRequestOptions?: SingleRequestOptions): Promise<ImagenGenerationResponse<ImagenInlineImage>>;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| templateId | string | The ID of the server-side template to execute. |
| templateVariables | object | A key-value map of variables to populate the template with. |
| singleRequestOptions | [SingleRequestOptions](https://firebase.google.com/docs/reference/js/ai.singlerequestoptions.md#singlerequestoptions_interface) |   |

**Returns:**

Promise\<[ImagenGenerationResponse](https://firebase.google.com/docs/reference/js/ai.imagengenerationresponse.md#imagengenerationresponse_interface)\<[ImagenInlineImage](https://firebase.google.com/docs/reference/js/ai.imageninlineimage.md#imageninlineimage_interface)\>\>