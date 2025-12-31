# Source: https://firebase.google.com/docs/reference/js/ai.chatsession.md.txt

# ChatSession class that enables sending chat messages and stores history of sent and received messages so far.

**Signature:**  

    export declare class ChatSession 

## Constructors

|                                                                            Constructor                                                                             | Modifiers |                     Description                      |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|------------------------------------------------------|
| [(constructor)(apiSettings, model, chromeAdapter, params, requestOptions)](https://firebase.google.com/docs/reference/js/ai.chatsession.md#chatsessionconstructor) |           | Constructs a new instance of the `ChatSession` class |

## Properties

|                                                  Property                                                   | Modifiers |                                                             Type                                                              | Description |
|-------------------------------------------------------------------------------------------------------------|-----------|-------------------------------------------------------------------------------------------------------------------------------|-------------|
| [model](https://firebase.google.com/docs/reference/js/ai.chatsession.md#chatsessionmodel)                   |           | string                                                                                                                        |             |
| [params](https://firebase.google.com/docs/reference/js/ai.chatsession.md#chatsessionparams)                 |           | [StartChatParams](https://firebase.google.com/docs/reference/js/ai.startchatparams.md#startchatparams_interface) \| undefined |             |
| [requestOptions](https://firebase.google.com/docs/reference/js/ai.chatsession.md#chatsessionrequestoptions) |           | [RequestOptions](https://firebase.google.com/docs/reference/js/ai.requestoptions.md#requestoptions_interface) \| undefined    |             |

## Methods

|                                                           Method                                                           | Modifiers |                                                                                                                          Description                                                                                                                           |
|----------------------------------------------------------------------------------------------------------------------------|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [getHistory()](https://firebase.google.com/docs/reference/js/ai.chatsession.md#chatsessiongethistory)                      |           | Gets the chat history so far. Blocked prompts are not added to history. Neither blocked candidates nor the prompts that generated them are added to history.                                                                                                   |
| [sendMessage(request)](https://firebase.google.com/docs/reference/js/ai.chatsession.md#chatsessionsendmessage)             |           | Sends a chat message and receives a non-streaming [GenerateContentResult](https://firebase.google.com/docs/reference/js/ai.generatecontentresult.md#generatecontentresult_interface)                                                                           |
| [sendMessageStream(request)](https://firebase.google.com/docs/reference/js/ai.chatsession.md#chatsessionsendmessagestream) |           | Sends a chat message and receives the response as a [GenerateContentStreamResult](https://firebase.google.com/docs/reference/js/ai.generatecontentstreamresult.md#generatecontentstreamresult_interface) containing an iterable stream and a response promise. |

## ChatSession.(constructor)

Constructs a new instance of the `ChatSession` class

**Signature:**  

    constructor(apiSettings: ApiSettings, model: string, chromeAdapter?: ChromeAdapter | undefined, params?: StartChatParams | undefined, requestOptions?: RequestOptions | undefined);

#### Parameters

|   Parameter    |                                                             Type                                                              | Description |
|----------------|-------------------------------------------------------------------------------------------------------------------------------|-------------|
| apiSettings    | ApiSettings                                                                                                                   |             |
| model          | string                                                                                                                        |             |
| chromeAdapter  | [ChromeAdapter](https://firebase.google.com/docs/reference/js/ai.chromeadapter.md#chromeadapter_interface) \| undefined       |             |
| params         | [StartChatParams](https://firebase.google.com/docs/reference/js/ai.startchatparams.md#startchatparams_interface) \| undefined |             |
| requestOptions | [RequestOptions](https://firebase.google.com/docs/reference/js/ai.requestoptions.md#requestoptions_interface) \| undefined    |             |

## ChatSession.model

**Signature:**  

    model: string;

## ChatSession.params

**Signature:**  

    params?: StartChatParams | undefined;

## ChatSession.requestOptions

**Signature:**  

    requestOptions?: RequestOptions | undefined;

## ChatSession.getHistory()

Gets the chat history so far. Blocked prompts are not added to history. Neither blocked candidates nor the prompts that generated them are added to history.

**Signature:**  

    getHistory(): Promise<Content[]>;

**Returns:**

Promise\<[Content](https://firebase.google.com/docs/reference/js/ai.content.md#content_interface)\[\]\>

## ChatSession.sendMessage()

Sends a chat message and receives a non-streaming [GenerateContentResult](https://firebase.google.com/docs/reference/js/ai.generatecontentresult.md#generatecontentresult_interface)

**Signature:**  

    sendMessage(request: string | Array<string | Part>): Promise<GenerateContentResult>;

#### Parameters

| Parameter |                                             Type                                              | Description |
|-----------|-----------------------------------------------------------------------------------------------|-------------|
| request   | string \| Array\<string \| [Part](https://firebase.google.com/docs/reference/js/ai.md#part)\> |             |

**Returns:**

Promise\<[GenerateContentResult](https://firebase.google.com/docs/reference/js/ai.generatecontentresult.md#generatecontentresult_interface)\>

## ChatSession.sendMessageStream()

Sends a chat message and receives the response as a [GenerateContentStreamResult](https://firebase.google.com/docs/reference/js/ai.generatecontentstreamresult.md#generatecontentstreamresult_interface) containing an iterable stream and a response promise.

**Signature:**  

    sendMessageStream(request: string | Array<string | Part>): Promise<GenerateContentStreamResult>;

#### Parameters

| Parameter |                                             Type                                              | Description |
|-----------|-----------------------------------------------------------------------------------------------|-------------|
| request   | string \| Array\<string \| [Part](https://firebase.google.com/docs/reference/js/ai.md#part)\> |             |

**Returns:**

Promise\<[GenerateContentStreamResult](https://firebase.google.com/docs/reference/js/ai.generatecontentstreamresult.md#generatecontentstreamresult_interface)\>