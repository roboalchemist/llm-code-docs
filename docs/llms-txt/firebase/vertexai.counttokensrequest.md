# Source: https://firebase.google.com/docs/reference/js/vertexai.counttokensrequest.md.txt

# CountTokensRequest interface

Params for calling [GenerativeModel.countTokens()](https://firebase.google.com/docs/reference/js/vertexai.generativemodel.md#generativemodelcounttokens)

**Signature:**  

    export interface CountTokensRequest 

## Properties

|                                                               Property                                                                |                                                                                        Type                                                                                        |                                      Description                                      |
|---------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------|
| [contents](https://firebase.google.com/docs/reference/js/vertexai.counttokensrequest.md#counttokensrequestcontents)                   | [Content](https://firebase.google.com/docs/reference/js/vertexai.content.md#content_interface)\[\]                                                                                 |                                                                                       |
| [generationConfig](https://firebase.google.com/docs/reference/js/vertexai.counttokensrequest.md#counttokensrequestgenerationconfig)   | [GenerationConfig](https://firebase.google.com/docs/reference/js/vertexai.generationconfig.md#generationconfig_interface)                                                          | Configuration options that control how the model generates a response.                |
| [systemInstruction](https://firebase.google.com/docs/reference/js/vertexai.counttokensrequest.md#counttokensrequestsysteminstruction) | string \| [Part](https://firebase.google.com/docs/reference/js/vertexai.md#part) \| [Content](https://firebase.google.com/docs/reference/js/vertexai.content.md#content_interface) | Instructions that direct the model to behave a certain way.                           |
| [tools](https://firebase.google.com/docs/reference/js/vertexai.counttokensrequest.md#counttokensrequesttools)                         | [Tool](https://firebase.google.com/docs/reference/js/vertexai.md#tool)\[\]                                                                                                         | [Tool](https://firebase.google.com/docs/reference/js/vertexai.md#tool) configuration. |

## CountTokensRequest.contents

**Signature:**  

    contents: Content[];

## CountTokensRequest.generationConfig

Configuration options that control how the model generates a response.

**Signature:**  

    generationConfig?: GenerationConfig;

## CountTokensRequest.systemInstruction

Instructions that direct the model to behave a certain way.

**Signature:**  

    systemInstruction?: string | Part | Content;

## CountTokensRequest.tools

[Tool](https://firebase.google.com/docs/reference/js/vertexai.md#tool) configuration.

**Signature:**  

    tools?: Tool[];