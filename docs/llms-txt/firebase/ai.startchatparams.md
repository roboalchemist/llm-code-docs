# Source: https://firebase.google.com/docs/reference/js/ai.startchatparams.md.txt

# StartChatParams interface

Params for [GenerativeModel.startChat()](https://firebase.google.com/docs/reference/js/ai.generativemodel.md#generativemodelstartchat).

**Signature:**  

    export interface StartChatParams extends BaseParams 

**Extends:** [BaseParams](https://firebase.google.com/docs/reference/js/ai.baseparams.md#baseparams_interface)

## Properties

|                                                         Property                                                          |                                                                                  Type                                                                                  | Description |
|---------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| [history](https://firebase.google.com/docs/reference/js/ai.startchatparams.md#startchatparamshistory)                     | [Content](https://firebase.google.com/docs/reference/js/ai.content.md#content_interface)\[\]                                                                           |             |
| [systemInstruction](https://firebase.google.com/docs/reference/js/ai.startchatparams.md#startchatparamssysteminstruction) | string \| [Part](https://firebase.google.com/docs/reference/js/ai.md#part) \| [Content](https://firebase.google.com/docs/reference/js/ai.content.md#content_interface) |             |
| [toolConfig](https://firebase.google.com/docs/reference/js/ai.startchatparams.md#startchatparamstoolconfig)               | [ToolConfig](https://firebase.google.com/docs/reference/js/ai.toolconfig.md#toolconfig_interface)                                                                      |             |
| [tools](https://firebase.google.com/docs/reference/js/ai.startchatparams.md#startchatparamstools)                         | [Tool](https://firebase.google.com/docs/reference/js/ai.md#tool)\[\]                                                                                                   |             |

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