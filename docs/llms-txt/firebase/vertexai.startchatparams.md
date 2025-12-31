# Source: https://firebase.google.com/docs/reference/js/vertexai.startchatparams.md.txt

# StartChatParams interface

Params for [GenerativeModel.startChat()](https://firebase.google.com/docs/reference/js/vertexai.generativemodel.md#generativemodelstartchat).

**Signature:**  

    export interface StartChatParams extends BaseParams 

**Extends:** [BaseParams](https://firebase.google.com/docs/reference/js/vertexai.baseparams.md#baseparams_interface)

## Properties

|                                                            Property                                                             |                                                                                        Type                                                                                        | Description |
|---------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| [history](https://firebase.google.com/docs/reference/js/vertexai.startchatparams.md#startchatparamshistory)                     | [Content](https://firebase.google.com/docs/reference/js/vertexai.content.md#content_interface)\[\]                                                                                 |             |
| [systemInstruction](https://firebase.google.com/docs/reference/js/vertexai.startchatparams.md#startchatparamssysteminstruction) | string \| [Part](https://firebase.google.com/docs/reference/js/vertexai.md#part) \| [Content](https://firebase.google.com/docs/reference/js/vertexai.content.md#content_interface) |             |
| [toolConfig](https://firebase.google.com/docs/reference/js/vertexai.startchatparams.md#startchatparamstoolconfig)               | [ToolConfig](https://firebase.google.com/docs/reference/js/vertexai.toolconfig.md#toolconfig_interface)                                                                            |             |
| [tools](https://firebase.google.com/docs/reference/js/vertexai.startchatparams.md#startchatparamstools)                         | [Tool](https://firebase.google.com/docs/reference/js/vertexai.md#tool)\[\]                                                                                                         |             |

## StartChatParams.history

**Signature:**  

    history?: Content[];

## StartChatParams.systemInstruction

**Signature:**  

    systemInstruction?: string | Part | Content;

## StartChatParams.toolConfig

**Signature:**  

    toolConfig?: ToolConfig;

## StartChatParams.tools

**Signature:**  

    tools?: Tool[];