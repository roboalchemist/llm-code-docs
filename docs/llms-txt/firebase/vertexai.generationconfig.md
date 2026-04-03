# Source: https://firebase.google.com/docs/reference/js/vertexai.generationconfig.md.txt

# GenerationConfig interface

Config options for content-related requests

**Signature:**  

    export interface GenerationConfig 

## Properties

|                                                              Property                                                               |                                                                                                   Type                                                                                                   |                                                                                                                                                                                                                                                                                   Description                                                                                                                                                                                                                                                                                    |
|-------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [candidateCount](https://firebase.google.com/docs/reference/js/vertexai.generationconfig.md#generationconfigcandidatecount)         | number                                                                                                                                                                                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [frequencyPenalty](https://firebase.google.com/docs/reference/js/vertexai.generationconfig.md#generationconfigfrequencypenalty)     | number                                                                                                                                                                                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [maxOutputTokens](https://firebase.google.com/docs/reference/js/vertexai.generationconfig.md#generationconfigmaxoutputtokens)       | number                                                                                                                                                                                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [presencePenalty](https://firebase.google.com/docs/reference/js/vertexai.generationconfig.md#generationconfigpresencepenalty)       | number                                                                                                                                                                                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [responseMimeType](https://firebase.google.com/docs/reference/js/vertexai.generationconfig.md#generationconfigresponsemimetype)     | string                                                                                                                                                                                                   | Output response MIME type of the generated candidate text. Supported MIME types are `text/plain` (default, text output), `application/json` (JSON response in the candidates), and `text/x.enum`.                                                                                                                                                                                                                                                                                                                                                                                |
| [responseModalities](https://firebase.google.com/docs/reference/js/vertexai.generationconfig.md#generationconfigresponsemodalities) | [ResponseModality](https://firebase.google.com/docs/reference/js/vertexai.md#responsemodality)\[\]                                                                                                       | ***(Public Preview)*** Generation modalities to be returned in generation responses.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [responseSchema](https://firebase.google.com/docs/reference/js/vertexai.generationconfig.md#generationconfigresponseschema)         | [TypedSchema](https://firebase.google.com/docs/reference/js/vertexai.md#typedschema) \| [SchemaRequest](https://firebase.google.com/docs/reference/js/vertexai.schemarequest.md#schemarequest_interface) | Output response schema of the generated candidate text. This value can be a class generated with a [Schema](https://firebase.google.com/docs/reference/js/vertexai.schema.md#schema_class) static method like `Schema.string()` or `Schema.object()` or it can be a plain JS object matching the [SchemaRequest](https://firebase.google.com/docs/reference/js/vertexai.schemarequest.md#schemarequest_interface) interface. Note: This only applies when the specified `responseMIMEType` supports a schema; currently this is limited to `application/json` and `text/x.enum`. |
| [stopSequences](https://firebase.google.com/docs/reference/js/vertexai.generationconfig.md#generationconfigstopsequences)           | string\[\]                                                                                                                                                                                               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [temperature](https://firebase.google.com/docs/reference/js/vertexai.generationconfig.md#generationconfigtemperature)               | number                                                                                                                                                                                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [topK](https://firebase.google.com/docs/reference/js/vertexai.generationconfig.md#generationconfigtopk)                             | number                                                                                                                                                                                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [topP](https://firebase.google.com/docs/reference/js/vertexai.generationconfig.md#generationconfigtopp)                             | number                                                                                                                                                                                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |

## GenerationConfig.candidateCount

**Signature:**  

    candidateCount?: number;

## GenerationConfig.frequencyPenalty

**Signature:**  

    frequencyPenalty?: number;

## GenerationConfig.maxOutputTokens

**Signature:**  

    maxOutputTokens?: number;

## GenerationConfig.presencePenalty

**Signature:**  

    presencePenalty?: number;

## GenerationConfig.responseMimeType

Output response MIME type of the generated candidate text. Supported MIME types are `text/plain` (default, text output), `application/json` (JSON response in the candidates), and `text/x.enum`.

**Signature:**  

    responseMimeType?: string;

## GenerationConfig.responseModalities

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Generation modalities to be returned in generation responses.

- Multimodal response generation is only supported by some Gemini models and versions; see [model versions](https://firebase.google.com/docs/vertex-ai/models). - Only image generation (`ResponseModality.IMAGE`) is supported.

**Signature:**  

    responseModalities?: ResponseModality[];

## GenerationConfig.responseSchema

Output response schema of the generated candidate text. This value can be a class generated with a [Schema](https://firebase.google.com/docs/reference/js/vertexai.schema.md#schema_class) static method like `Schema.string()` or `Schema.object()` or it can be a plain JS object matching the [SchemaRequest](https://firebase.google.com/docs/reference/js/vertexai.schemarequest.md#schemarequest_interface) interface.   
Note: This only applies when the specified `responseMIMEType` supports a schema; currently this is limited to `application/json` and `text/x.enum`.

**Signature:**  

    responseSchema?: TypedSchema | SchemaRequest;

## GenerationConfig.stopSequences

**Signature:**  

    stopSequences?: string[];

## GenerationConfig.temperature

**Signature:**  

    temperature?: number;

## GenerationConfig.topK

**Signature:**  

    topK?: number;

## GenerationConfig.topP

**Signature:**  

    topP?: number;