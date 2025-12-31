# Source: https://firebase.google.com/docs/reference/js/ai.generativemodel.md.txt

# GenerativeModel class

Class for generative model APIs.

**Signature:**  

    export declare class GenerativeModel extends AIModel 

**Extends:** [AIModel](https://firebase.google.com/docs/reference/js/ai.aimodel.md#aimodel_class)

## Constructors

|                                                                           Constructor                                                                           | Modifiers |                       Description                        |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|----------------------------------------------------------|
| [(constructor)(ai, modelParams, requestOptions, chromeAdapter)](https://firebase.google.com/docs/reference/js/ai.generativemodel.md#generativemodelconstructor) |           | Constructs a new instance of the `GenerativeModel` class |

## Properties

|                                                         Property                                                          | Modifiers |                                                        Type                                                         | Description |
|---------------------------------------------------------------------------------------------------------------------------|-----------|---------------------------------------------------------------------------------------------------------------------|-------------|
| [generationConfig](https://firebase.google.com/docs/reference/js/ai.generativemodel.md#generativemodelgenerationconfig)   |           | [GenerationConfig](https://firebase.google.com/docs/reference/js/ai.generationconfig.md#generationconfig_interface) |             |
| [requestOptions](https://firebase.google.com/docs/reference/js/ai.generativemodel.md#generativemodelrequestoptions)       |           | [RequestOptions](https://firebase.google.com/docs/reference/js/ai.requestoptions.md#requestoptions_interface)       |             |
| [safetySettings](https://firebase.google.com/docs/reference/js/ai.generativemodel.md#generativemodelsafetysettings)       |           | [SafetySetting](https://firebase.google.com/docs/reference/js/ai.safetysetting.md#safetysetting_interface)\[\]      |             |
| [systemInstruction](https://firebase.google.com/docs/reference/js/ai.generativemodel.md#generativemodelsysteminstruction) |           | [Content](https://firebase.google.com/docs/reference/js/ai.content.md#content_interface)                            |             |
| [toolConfig](https://firebase.google.com/docs/reference/js/ai.generativemodel.md#generativemodeltoolconfig)               |           | [ToolConfig](https://firebase.google.com/docs/reference/js/ai.toolconfig.md#toolconfig_interface)                   |             |
| [tools](https://firebase.google.com/docs/reference/js/ai.generativemodel.md#generativemodeltools)                         |           | [Tool](https://firebase.google.com/docs/reference/js/ai.md#tool)\[\]                                                |             |

## Methods

|                                                                   Method                                                                   | Modifiers |                                                                                                            Description                                                                                                             |
|--------------------------------------------------------------------------------------------------------------------------------------------|-----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [countTokens(request)](https://firebase.google.com/docs/reference/js/ai.generativemodel.md#generativemodelcounttokens)                     |           | Counts the tokens in the provided request.                                                                                                                                                                                         |
| [generateContent(request)](https://firebase.google.com/docs/reference/js/ai.generativemodel.md#generativemodelgeneratecontent)             |           | Makes a single non-streaming call to the model and returns an object containing a single [GenerateContentResponse](https://firebase.google.com/docs/reference/js/ai.generatecontentresponse.md#generatecontentresponse_interface). |
| [generateContentStream(request)](https://firebase.google.com/docs/reference/js/ai.generativemodel.md#generativemodelgeneratecontentstream) |           | Makes a single streaming call to the model and returns an object containing an iterable stream that iterates over all chunks in the streaming response as well as a promise that returns the final aggregated response.            |
| [startChat(startChatParams)](https://firebase.google.com/docs/reference/js/ai.generativemodel.md#generativemodelstartchat)                 |           | Gets a new [ChatSession](https://firebase.google.com/docs/reference/js/ai.chatsession.md#chatsession_class) instance which can be used for multi-turn chats.                                                                       |

## GenerativeModel.(constructor)

Constructs a new instance of the `GenerativeModel` class

**Signature:**  

    constructor(ai: AI, modelParams: ModelParams, requestOptions?: RequestOptions, chromeAdapter?: ChromeAdapter | undefined);

#### Parameters

|   Parameter    |                                                          Type                                                           | Description |
|----------------|-------------------------------------------------------------------------------------------------------------------------|-------------|
| ai             | [AI](https://firebase.google.com/docs/reference/js/ai.ai.md#ai_interface)                                               |             |
| modelParams    | [ModelParams](https://firebase.google.com/docs/reference/js/ai.modelparams.md#modelparams_interface)                    |             |
| requestOptions | [RequestOptions](https://firebase.google.com/docs/reference/js/ai.requestoptions.md#requestoptions_interface)           |             |
| chromeAdapter  | [ChromeAdapter](https://firebase.google.com/docs/reference/js/ai.chromeadapter.md#chromeadapter_interface) \| undefined |             |

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

| Parameter |                                                                                                            Type                                                                                                            | Description |
|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| request   | [CountTokensRequest](https://firebase.google.com/docs/reference/js/ai.counttokensrequest.md#counttokensrequest_interface) \| string \| Array\<string \| [Part](https://firebase.google.com/docs/reference/js/ai.md#part)\> |             |

**Returns:**

Promise\<[CountTokensResponse](https://firebase.google.com/docs/reference/js/ai.counttokensresponse.md#counttokensresponse_interface)\>

## GenerativeModel.generateContent()

Makes a single non-streaming call to the model and returns an object containing a single [GenerateContentResponse](https://firebase.google.com/docs/reference/js/ai.generatecontentresponse.md#generatecontentresponse_interface).

**Signature:**  

    generateContent(request: GenerateContentRequest | string | Array<string | Part>): Promise<GenerateContentResult>;

#### Parameters

| Parameter |                                                                                                                  Type                                                                                                                  | Description |
|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| request   | [GenerateContentRequest](https://firebase.google.com/docs/reference/js/ai.generatecontentrequest.md#generatecontentrequest_interface) \| string \| Array\<string \| [Part](https://firebase.google.com/docs/reference/js/ai.md#part)\> |             |

**Returns:**

Promise\<[GenerateContentResult](https://firebase.google.com/docs/reference/js/ai.generatecontentresult.md#generatecontentresult_interface)\>

## GenerativeModel.generateContentStream()

Makes a single streaming call to the model and returns an object containing an iterable stream that iterates over all chunks in the streaming response as well as a promise that returns the final aggregated response.

**Signature:**  

    generateContentStream(request: GenerateContentRequest | string | Array<string | Part>): Promise<GenerateContentStreamResult>;

#### Parameters

| Parameter |                                                                                                                  Type                                                                                                                  | Description |
|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| request   | [GenerateContentRequest](https://firebase.google.com/docs/reference/js/ai.generatecontentrequest.md#generatecontentrequest_interface) \| string \| Array\<string \| [Part](https://firebase.google.com/docs/reference/js/ai.md#part)\> |             |

**Returns:**

Promise\<[GenerateContentStreamResult](https://firebase.google.com/docs/reference/js/ai.generatecontentstreamresult.md#generatecontentstreamresult_interface)\>

## GenerativeModel.startChat()

Gets a new [ChatSession](https://firebase.google.com/docs/reference/js/ai.chatsession.md#chatsession_class) instance which can be used for multi-turn chats.

**Signature:**  

    startChat(startChatParams?: StartChatParams): ChatSession;

#### Parameters

|    Parameter    |                                                       Type                                                       | Description |
|-----------------|------------------------------------------------------------------------------------------------------------------|-------------|
| startChatParams | [StartChatParams](https://firebase.google.com/docs/reference/js/ai.startchatparams.md#startchatparams_interface) |             |

**Returns:**

[ChatSession](https://firebase.google.com/docs/reference/js/ai.chatsession.md#chatsession_class)