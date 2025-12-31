# Source: https://firebase.google.com/docs/reference/js/ai.chromeadapter.md.txt

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Defines an inference "backend" that uses Chrome's on-device model, and encapsulates logic for detecting when on-device inference is possible.

These methods should not be called directly by the user.

**Signature:**  

    export interface ChromeAdapter 

## Methods

|                                                                 Method                                                                 |                                         Description                                          |
|----------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|
| [generateContent(request)](https://firebase.google.com/docs/reference/js/ai.chromeadapter.md#chromeadaptergeneratecontent)             | ***(Public Preview)*** Generates content using on-device inference.                          |
| [generateContentStream(request)](https://firebase.google.com/docs/reference/js/ai.chromeadapter.md#chromeadaptergeneratecontentstream) | ***(Public Preview)*** Generates a content stream using on-device inference.                 |
| [isAvailable(request)](https://firebase.google.com/docs/reference/js/ai.chromeadapter.md#chromeadapterisavailable)                     | ***(Public Preview)*** Checks if the on-device model is capable of handling a given request. |

## ChromeAdapter.generateContent()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Generates content using on-device inference.

This is comparable to [GenerativeModel.generateContent()](https://firebase.google.com/docs/reference/js/ai.generativemodel.md#generativemodelgeneratecontent) for generating content using in-cloud inference.

**Signature:**  

    generateContent(request: GenerateContentRequest): Promise<Response>;

#### Parameters

| Parameter |                                                                 Type                                                                  |                                                                         Description                                                                          |
|-----------|---------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| request   | [GenerateContentRequest](https://firebase.google.com/docs/reference/js/ai.generatecontentrequest.md#generatecontentrequest_interface) | a standard Firebase AI [GenerateContentRequest](https://firebase.google.com/docs/reference/js/ai.generatecontentrequest.md#generatecontentrequest_interface) |

**Returns:**

Promise\<Response\>

## ChromeAdapter.generateContentStream()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Generates a content stream using on-device inference.

This is comparable to [GenerativeModel.generateContentStream()](https://firebase.google.com/docs/reference/js/ai.generativemodel.md#generativemodelgeneratecontentstream) for generating a content stream using in-cloud inference.

**Signature:**  

    generateContentStream(request: GenerateContentRequest): Promise<Response>;

#### Parameters

| Parameter |                                                                 Type                                                                  |                                                                         Description                                                                          |
|-----------|---------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| request   | [GenerateContentRequest](https://firebase.google.com/docs/reference/js/ai.generatecontentrequest.md#generatecontentrequest_interface) | a standard Firebase AI [GenerateContentRequest](https://firebase.google.com/docs/reference/js/ai.generatecontentrequest.md#generatecontentrequest_interface) |

**Returns:**

Promise\<Response\>

## ChromeAdapter.isAvailable()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Checks if the on-device model is capable of handling a given request.

**Signature:**  

    isAvailable(request: GenerateContentRequest): Promise<boolean>;

#### Parameters

| Parameter |                                                                 Type                                                                  |                  Description                   |
|-----------|---------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------|
| request   | [GenerateContentRequest](https://firebase.google.com/docs/reference/js/ai.generatecontentrequest.md#generatecontentrequest_interface) | A potential request to be passed to the model. |

**Returns:**

Promise\<boolean\>