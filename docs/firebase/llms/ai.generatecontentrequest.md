# Source: https://firebase.google.com/docs/reference/js/ai.generatecontentrequest.md.txt

# GenerateContentRequest interface

Request sent through [GenerativeModel.generateContent()](https://firebase.google.com/docs/reference/js/ai.generativemodel.md#generativemodelgeneratecontent)

**Signature:**  

    export interface GenerateContentRequest extends BaseParams 

**Extends:** [BaseParams](https://firebase.google.com/docs/reference/js/ai.baseparams.md#baseparams_interface)

## Properties

|                                                                Property                                                                 |                                                                                  Type                                                                                  | Description |
|-----------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| [contents](https://firebase.google.com/docs/reference/js/ai.generatecontentrequest.md#generatecontentrequestcontents)                   | [Content](https://firebase.google.com/docs/reference/js/ai.content.md#content_interface)\[\]                                                                           |             |
| [systemInstruction](https://firebase.google.com/docs/reference/js/ai.generatecontentrequest.md#generatecontentrequestsysteminstruction) | string \| [Part](https://firebase.google.com/docs/reference/js/ai.md#part) \| [Content](https://firebase.google.com/docs/reference/js/ai.content.md#content_interface) |             |
| [toolConfig](https://firebase.google.com/docs/reference/js/ai.generatecontentrequest.md#generatecontentrequesttoolconfig)               | [ToolConfig](https://firebase.google.com/docs/reference/js/ai.toolconfig.md#toolconfig_interface)                                                                      |             |
| [tools](https://firebase.google.com/docs/reference/js/ai.generatecontentrequest.md#generatecontentrequesttools)                         | [Tool](https://firebase.google.com/docs/reference/js/ai.md#tool)\[\]                                                                                                   |             |

## GenerateContentRequest.contents

**Signature:**  

    contents: Content[];

## GenerateContentRequest.systemInstruction

**Signature:**  

    systemInstruction?: string | Part | Content;

## GenerateContentRequest.toolConfig

**Signature:**  

    toolConfig?: ToolConfig;

## GenerateContentRequest.tools

**Signature:**  

    tools?: Tool[];