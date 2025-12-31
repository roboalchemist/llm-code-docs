# Source: https://firebase.google.com/docs/reference/js/vertexai.modelparams.md.txt

# ModelParams interface

Params passed to [getGenerativeModel()](https://firebase.google.com/docs/reference/js/vertexai.md#getgenerativemodel_80bd839).

**Signature:**  

    export interface ModelParams extends BaseParams 

**Extends:** [BaseParams](https://firebase.google.com/docs/reference/js/vertexai.baseparams.md#baseparams_interface)

## Properties

|                                                        Property                                                         |                                                                                        Type                                                                                        | Description |
|-------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| [model](https://firebase.google.com/docs/reference/js/vertexai.modelparams.md#modelparamsmodel)                         | string                                                                                                                                                                             |             |
| [systemInstruction](https://firebase.google.com/docs/reference/js/vertexai.modelparams.md#modelparamssysteminstruction) | string \| [Part](https://firebase.google.com/docs/reference/js/vertexai.md#part) \| [Content](https://firebase.google.com/docs/reference/js/vertexai.content.md#content_interface) |             |
| [toolConfig](https://firebase.google.com/docs/reference/js/vertexai.modelparams.md#modelparamstoolconfig)               | [ToolConfig](https://firebase.google.com/docs/reference/js/vertexai.toolconfig.md#toolconfig_interface)                                                                            |             |
| [tools](https://firebase.google.com/docs/reference/js/vertexai.modelparams.md#modelparamstools)                         | [Tool](https://firebase.google.com/docs/reference/js/vertexai.md#tool)\[\]                                                                                                         |             |

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