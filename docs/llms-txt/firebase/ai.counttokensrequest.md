# Source: https://firebase.google.com/docs/reference/js/ai.counttokensrequest.md.txt

# CountTokensRequest interface

Params for calling [GenerativeModel.countTokens()](https://firebase.google.com/docs/reference/js/ai.generativemodel.md#generativemodelcounttokens)

**Signature:**  

    export interface CountTokensRequest 

## Properties

|                                                            Property                                                             |                                                                                  Type                                                                                  |                                   Description                                   |
|---------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------|
| [contents](https://firebase.google.com/docs/reference/js/ai.counttokensrequest.md#counttokensrequestcontents)                   | [Content](https://firebase.google.com/docs/reference/js/ai.content.md#content_interface)\[\]                                                                           |                                                                                 |
| [generationConfig](https://firebase.google.com/docs/reference/js/ai.counttokensrequest.md#counttokensrequestgenerationconfig)   | [GenerationConfig](https://firebase.google.com/docs/reference/js/ai.generationconfig.md#generationconfig_interface)                                                    | Configuration options that control how the model generates a response.          |
| [systemInstruction](https://firebase.google.com/docs/reference/js/ai.counttokensrequest.md#counttokensrequestsysteminstruction) | string \| [Part](https://firebase.google.com/docs/reference/js/ai.md#part) \| [Content](https://firebase.google.com/docs/reference/js/ai.content.md#content_interface) | Instructions that direct the model to behave a certain way.                     |
| [tools](https://firebase.google.com/docs/reference/js/ai.counttokensrequest.md#counttokensrequesttools)                         | [Tool](https://firebase.google.com/docs/reference/js/ai.md#tool)\[\]                                                                                                   | [Tool](https://firebase.google.com/docs/reference/js/ai.md#tool) configuration. |

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

[Tool](https://firebase.google.com/docs/reference/js/ai.md#tool) configuration.

**Signature:**  

    tools?: Tool[];