# Source: https://firebase.google.com/docs/reference/js/ai.modelparams.md.txt

# ModelParams interface

Params passed to [getGenerativeModel()](https://firebase.google.com/docs/reference/js/ai.md#getgenerativemodel_c63f46a).

**Signature:**  

    export interface ModelParams extends BaseParams 

**Extends:** [BaseParams](https://firebase.google.com/docs/reference/js/ai.baseparams.md#baseparams_interface)

## Properties

|                                                     Property                                                      |                                                                                  Type                                                                                  | Description |
|-------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| [model](https://firebase.google.com/docs/reference/js/ai.modelparams.md#modelparamsmodel)                         | string                                                                                                                                                                 |             |
| [systemInstruction](https://firebase.google.com/docs/reference/js/ai.modelparams.md#modelparamssysteminstruction) | string \| [Part](https://firebase.google.com/docs/reference/js/ai.md#part) \| [Content](https://firebase.google.com/docs/reference/js/ai.content.md#content_interface) |             |
| [toolConfig](https://firebase.google.com/docs/reference/js/ai.modelparams.md#modelparamstoolconfig)               | [ToolConfig](https://firebase.google.com/docs/reference/js/ai.toolconfig.md#toolconfig_interface)                                                                      |             |
| [tools](https://firebase.google.com/docs/reference/js/ai.modelparams.md#modelparamstools)                         | [Tool](https://firebase.google.com/docs/reference/js/ai.md#tool)\[\]                                                                                                   |             |

## ModelParams.model

**Signature:**  

    model: string;

## ModelParams.systemInstruction

**Signature:**  

    systemInstruction?: string | Part | Content;

## ModelParams.toolConfig

**Signature:**  

    toolConfig?: ToolConfig;

## ModelParams.tools

**Signature:**  

    tools?: Tool[];