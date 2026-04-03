# Source: https://firebase.google.com/docs/reference/js/ai.livemodelparams.md.txt

# LiveModelParams interface

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Params passed to [getLiveGenerativeModel()](https://firebase.google.com/docs/reference/js/ai.md#getlivegenerativemodel_f2099ac).

**Signature:**  

    export interface LiveModelParams 

## Properties

|                                                         Property                                                          |                                                                                  Type                                                                                  |      Description       |
|---------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------|
| [generationConfig](https://firebase.google.com/docs/reference/js/ai.livemodelparams.md#livemodelparamsgenerationconfig)   | [LiveGenerationConfig](https://firebase.google.com/docs/reference/js/ai.livegenerationconfig.md#livegenerationconfig_interface)                                        | ***(Public Preview)*** |
| [model](https://firebase.google.com/docs/reference/js/ai.livemodelparams.md#livemodelparamsmodel)                         | string                                                                                                                                                                 | ***(Public Preview)*** |
| [systemInstruction](https://firebase.google.com/docs/reference/js/ai.livemodelparams.md#livemodelparamssysteminstruction) | string \| [Part](https://firebase.google.com/docs/reference/js/ai.md#part) \| [Content](https://firebase.google.com/docs/reference/js/ai.content.md#content_interface) | ***(Public Preview)*** |
| [toolConfig](https://firebase.google.com/docs/reference/js/ai.livemodelparams.md#livemodelparamstoolconfig)               | [ToolConfig](https://firebase.google.com/docs/reference/js/ai.toolconfig.md#toolconfig_interface)                                                                      | ***(Public Preview)*** |
| [tools](https://firebase.google.com/docs/reference/js/ai.livemodelparams.md#livemodelparamstools)                         | [Tool](https://firebase.google.com/docs/reference/js/ai.md#tool)\[\]                                                                                                   | ***(Public Preview)*** |

## LiveModelParams.generationConfig

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

**Signature:**  

    generationConfig?: LiveGenerationConfig;

## LiveModelParams.model

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

**Signature:**  

    model: string;

## LiveModelParams.systemInstruction

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

**Signature:**  

    systemInstruction?: string | Part | Content;

## LiveModelParams.toolConfig

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

**Signature:**  

    toolConfig?: ToolConfig;

## LiveModelParams.tools

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

**Signature:**  

    tools?: Tool[];