# Source: https://firebase.google.com/docs/reference/js/ai.templategenerativemodel.md.txt

# TemplateGenerativeModel class

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

[GenerativeModel](https://firebase.google.com/docs/reference/js/ai.generativemodel.md#generativemodel_class) APIs that execute on a server-side template.

This class should only be instantiated with [getTemplateGenerativeModel()](https://firebase.google.com/docs/reference/js/ai.md#gettemplategenerativemodel_9476bbc).

**Signature:**

    export declare class TemplateGenerativeModel 

## Constructors

| Constructor | Modifiers | Description |
|---|---|---|
| [(constructor)(ai, requestOptions)](https://firebase.google.com/docs/reference/js/ai.templategenerativemodel.md#templategenerativemodelconstructor) |   | ***(Public Preview)*** Constructs a new instance of the `TemplateGenerativeModel` class |

## Properties

| Property | Modifiers | Type | Description |
|---|---|---|---|
| [requestOptions](https://firebase.google.com/docs/reference/js/ai.templategenerativemodel.md#templategenerativemodelrequestoptions) |   | [RequestOptions](https://firebase.google.com/docs/reference/js/ai.requestoptions.md#requestoptions_interface) | ***(Public Preview)*** Additional options to use when making requests. |

## Methods

| Method | Modifiers | Description |
|---|---|---|
| [generateContent(templateId, templateVariables, singleRequestOptions)](https://firebase.google.com/docs/reference/js/ai.templategenerativemodel.md#templategenerativemodelgeneratecontent) |   | ***(Public Preview)*** Makes a single non-streaming call to the model and returns an object containing a single [GenerateContentResponse](https://firebase.google.com/docs/reference/js/ai.generatecontentresponse.md#generatecontentresponse_interface). |
| [generateContentStream(templateId, templateVariables, singleRequestOptions)](https://firebase.google.com/docs/reference/js/ai.templategenerativemodel.md#templategenerativemodelgeneratecontentstream) |   | ***(Public Preview)*** Makes a single streaming call to the model and returns an object containing an iterable stream that iterates over all chunks in the streaming response as well as a promise that returns the final aggregated response. |

## TemplateGenerativeModel.(constructor)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Constructs a new instance of the `TemplateGenerativeModel` class

**Signature:**

    constructor(ai: AI, requestOptions?: RequestOptions);

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| ai | [AI](https://firebase.google.com/docs/reference/js/ai.ai.md#ai_interface) |   |
| requestOptions | [RequestOptions](https://firebase.google.com/docs/reference/js/ai.requestoptions.md#requestoptions_interface) |   |

## TemplateGenerativeModel.requestOptions

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Additional options to use when making requests.

**Signature:**

    requestOptions?: RequestOptions;

## TemplateGenerativeModel.generateContent()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Makes a single non-streaming call to the model and returns an object containing a single [GenerateContentResponse](https://firebase.google.com/docs/reference/js/ai.generatecontentresponse.md#generatecontentresponse_interface).

**Signature:**

    generateContent(templateId: string, templateVariables: object, singleRequestOptions?: SingleRequestOptions): Promise<GenerateContentResult>;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| templateId | string | The ID of the server-side template to execute. |
| templateVariables | object | A key-value map of variables to populate the template with. |
| singleRequestOptions | [SingleRequestOptions](https://firebase.google.com/docs/reference/js/ai.singlerequestoptions.md#singlerequestoptions_interface) |   |

**Returns:**

Promise\<[GenerateContentResult](https://firebase.google.com/docs/reference/js/ai.generatecontentresult.md#generatecontentresult_interface)\>

## TemplateGenerativeModel.generateContentStream()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Makes a single streaming call to the model and returns an object containing an iterable stream that iterates over all chunks in the streaming response as well as a promise that returns the final aggregated response.

**Signature:**

    generateContentStream(templateId: string, templateVariables: object, singleRequestOptions?: SingleRequestOptions): Promise<GenerateContentStreamResult>;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| templateId | string | The ID of the server-side template to execute. |
| templateVariables | object | A key-value map of variables to populate the template with. |
| singleRequestOptions | [SingleRequestOptions](https://firebase.google.com/docs/reference/js/ai.singlerequestoptions.md#singlerequestoptions_interface) |   |

**Returns:**

Promise\<[GenerateContentStreamResult](https://firebase.google.com/docs/reference/js/ai.generatecontentstreamresult.md#generatecontentstreamresult_interface)\>