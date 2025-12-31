# Source: https://firebase.google.com/docs/reference/js/vertexai.generatecontentrequest.md.txt

# GenerateContentRequest interface

Request sent through [GenerativeModel.generateContent()](https://firebase.google.com/docs/reference/js/vertexai.generativemodel.md#generativemodelgeneratecontent)

**Signature:**  

    export interface GenerateContentRequest extends BaseParams 

**Extends:** [BaseParams](https://firebase.google.com/docs/reference/js/vertexai.baseparams.md#baseparams_interface)

## Properties

|                                                                   Property                                                                    |                                                                                        Type                                                                                        | Description |
|-----------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| [contents](https://firebase.google.com/docs/reference/js/vertexai.generatecontentrequest.md#generatecontentrequestcontents)                   | [Content](https://firebase.google.com/docs/reference/js/vertexai.content.md#content_interface)\[\]                                                                                 |             |
| [systemInstruction](https://firebase.google.com/docs/reference/js/vertexai.generatecontentrequest.md#generatecontentrequestsysteminstruction) | string \| [Part](https://firebase.google.com/docs/reference/js/vertexai.md#part) \| [Content](https://firebase.google.com/docs/reference/js/vertexai.content.md#content_interface) |             |
| [toolConfig](https://firebase.google.com/docs/reference/js/vertexai.generatecontentrequest.md#generatecontentrequesttoolconfig)               | [ToolConfig](https://firebase.google.com/docs/reference/js/vertexai.toolconfig.md#toolconfig_interface)                                                                            |             |
| [tools](https://firebase.google.com/docs/reference/js/vertexai.generatecontentrequest.md#generatecontentrequesttools)                         | [Tool](https://firebase.google.com/docs/reference/js/vertexai.md#tool)\[\]                                                                                                         |             |

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