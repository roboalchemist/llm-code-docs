# Source: https://firebase.google.com/docs/reference/js/vertexai.generativemodel.md.txt

# GenerativeModel class

Class for generative model APIs.

**Signature:**  

    export declare class GenerativeModel extends AIModel 

**Extends:** [AIModel](https://firebase.google.com/docs/reference/js/vertexai.aimodel.md#aimodel_class)

## Constructors

|                                                                      Constructor                                                                       | Modifiers |                       Description                        |
|--------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|----------------------------------------------------------|
| [(constructor)(ai, modelParams, requestOptions)](https://firebase.google.com/docs/reference/js/vertexai.generativemodel.md#generativemodelconstructor) |           | Constructs a new instance of the `GenerativeModel` class |

## Properties

|                                                            Property                                                             | Modifiers |                                                           Type                                                            | Description |
|---------------------------------------------------------------------------------------------------------------------------------|-----------|---------------------------------------------------------------------------------------------------------------------------|-------------|
| [generationConfig](https://firebase.google.com/docs/reference/js/vertexai.generativemodel.md#generativemodelgenerationconfig)   |           | [GenerationConfig](https://firebase.google.com/docs/reference/js/vertexai.generationconfig.md#generationconfig_interface) |             |
| [requestOptions](https://firebase.google.com/docs/reference/js/vertexai.generativemodel.md#generativemodelrequestoptions)       |           | [RequestOptions](https://firebase.google.com/docs/reference/js/vertexai.requestoptions.md#requestoptions_interface)       |             |
| [safetySettings](https://firebase.google.com/docs/reference/js/vertexai.generativemodel.md#generativemodelsafetysettings)       |           | [SafetySetting](https://firebase.google.com/docs/reference/js/vertexai.safetysetting.md#safetysetting_interface)\[\]      |             |
| [systemInstruction](https://firebase.google.com/docs/reference/js/vertexai.generativemodel.md#generativemodelsysteminstruction) |           | [Content](https://firebase.google.com/docs/reference/js/vertexai.content.md#content_interface)                            |             |
| [toolConfig](https://firebase.google.com/docs/reference/js/vertexai.generativemodel.md#generativemodeltoolconfig)               |           | [ToolConfig](https://firebase.google.com/docs/reference/js/vertexai.toolconfig.md#toolconfig_interface)                   |             |
| [tools](https://firebase.google.com/docs/reference/js/vertexai.generativemodel.md#generativemodeltools)                         |           | [Tool](https://firebase.google.com/docs/reference/js/vertexai.md#tool)\[\]                                                |             |

## Methods

|                                                                      Method                                                                      | Modifiers |                                                                                                               Description                                                                                                                |
|--------------------------------------------------------------------------------------------------------------------------------------------------|-----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [countTokens(request)](https://firebase.google.com/docs/reference/js/vertexai.generativemodel.md#generativemodelcounttokens)                     |           | Counts the tokens in the provided request.                                                                                                                                                                                               |
| [generateContent(request)](https://firebase.google.com/docs/reference/js/vertexai.generativemodel.md#generativemodelgeneratecontent)             |           | Makes a single non-streaming call to the model and returns an object containing a single [GenerateContentResponse](https://firebase.google.com/docs/reference/js/vertexai.generatecontentresponse.md#generatecontentresponse_interface). |
| [generateContentStream(request)](https://firebase.google.com/docs/reference/js/vertexai.generativemodel.md#generativemodelgeneratecontentstream) |           | Makes a single streaming call to the model and returns an object containing an iterable stream that iterates over all chunks in the streaming response as well as a promise that returns the final aggregated response.                  |
| [startChat(startChatParams)](https://firebase.google.com/docs/reference/js/vertexai.generativemodel.md#generativemodelstartchat)                 |           | Gets a new [ChatSession](https://firebase.google.com/docs/reference/js/vertexai.chatsession.md#chatsession_class) instance which can be used for multi-turn chats.                                                                       |

## GenerativeModel.(constructor)

Constructs a new instance of the `GenerativeModel` class

**Signature:**  

    constructor(ai: AI, modelParams: ModelParams, requestOptions?: RequestOptions);

#### Parameters

|   Parameter    |                                                        Type                                                         | Description |
|----------------|---------------------------------------------------------------------------------------------------------------------|-------------|
| ai             | [AI](https://firebase.google.com/docs/reference/js/vertexai.ai.md#ai_interface)                                     |             |
| modelParams    | [ModelParams](https://firebase.google.com/docs/reference/js/vertexai.modelparams.md#modelparams_interface)          |             |
| requestOptions | [RequestOptions](https://firebase.google.com/docs/reference/js/vertexai.requestoptions.md#requestoptions_interface) |             |

## GenerativeModel.generationConfig

**Signature:**  

    generationConfig: GenerationConfig;

## GenerativeModel.requestOptions

**Signature:**  

    requestOptions?: RequestOptions;

## GenerativeModel.safetySettings

**Signature:**  

    safetySettings: SafetySetting[];

## GenerativeModel.systemInstruction

**Signature:**  

    systemInstruction?: Content;

## GenerativeModel.toolConfig

**Signature:**  

    toolConfig?: ToolConfig;

## GenerativeModel.tools

**Signature:**  

    tools?: Tool[];

## GenerativeModel.countTokens()

Counts the tokens in the provided request.

**Signature:**  

    countTokens(request: CountTokensRequest | string | Array<string | Part>): Promise<CountTokensResponse>;

#### Parameters

| Parameter |                                                                                                                  Type                                                                                                                  | Description |
|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| request   | [CountTokensRequest](https://firebase.google.com/docs/reference/js/vertexai.counttokensrequest.md#counttokensrequest_interface) \| string \| Array\<string \| [Part](https://firebase.google.com/docs/reference/js/vertexai.md#part)\> |             |

**Returns:**

Promise\<[CountTokensResponse](https://firebase.google.com/docs/reference/js/vertexai.counttokensresponse.md#counttokensresponse_interface)\>

## GenerativeModel.generateContent()

Makes a single non-streaming call to the model and returns an object containing a single [GenerateContentResponse](https://firebase.google.com/docs/reference/js/vertexai.generatecontentresponse.md#generatecontentresponse_interface).

**Signature:**  

    generateContent(request: GenerateContentRequest | string | Array<string | Part>): Promise<GenerateContentResult>;

#### Parameters

| Parameter |                                                                                                                        Type                                                                                                                        | Description |
|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| request   | [GenerateContentRequest](https://firebase.google.com/docs/reference/js/vertexai.generatecontentrequest.md#generatecontentrequest_interface) \| string \| Array\<string \| [Part](https://firebase.google.com/docs/reference/js/vertexai.md#part)\> |             |

**Returns:**

Promise\<[GenerateContentResult](https://firebase.google.com/docs/reference/js/vertexai.generatecontentresult.md#generatecontentresult_interface)\>

## GenerativeModel.generateContentStream()

Makes a single streaming call to the model and returns an object containing an iterable stream that iterates over all chunks in the streaming response as well as a promise that returns the final aggregated response.

**Signature:**  

    generateContentStream(request: GenerateContentRequest | string | Array<string | Part>): Promise<GenerateContentStreamResult>;

#### Parameters

| Parameter |                                                                                                                        Type                                                                                                                        | Description |
|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| request   | [GenerateContentRequest](https://firebase.google.com/docs/reference/js/vertexai.generatecontentrequest.md#generatecontentrequest_interface) \| string \| Array\<string \| [Part](https://firebase.google.com/docs/reference/js/vertexai.md#part)\> |             |

**Returns:**

Promise\<[GenerateContentStreamResult](https://firebase.google.com/docs/reference/js/vertexai.generatecontentstreamresult.md#generatecontentstreamresult_interface)\>

## GenerativeModel.startChat()

Gets a new [ChatSession](https://firebase.google.com/docs/reference/js/vertexai.chatsession.md#chatsession_class) instance which can be used for multi-turn chats.

**Signature:**  

    startChat(startChatParams?: StartChatParams): ChatSession;

#### Parameters

|    Parameter    |                                                          Type                                                          | Description |
|-----------------|------------------------------------------------------------------------------------------------------------------------|-------------|
| startChatParams | [StartChatParams](https://firebase.google.com/docs/reference/js/vertexai.startchatparams.md#startchatparams_interface) |             |

**Returns:**

[ChatSession](https://firebase.google.com/docs/reference/js/vertexai.chatsession.md#chatsession_class)