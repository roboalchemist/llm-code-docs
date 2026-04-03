# Source: https://firebase.google.com/docs/reference/js/ai.livesession.md.txt

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Represents an active, real-time, bidirectional conversation with the model.

This class should only be instantiated by calling[LiveGenerativeModel.connect()](https://firebase.google.com/docs/reference/js/ai.livegenerativemodel.md#livegenerativemodelconnect).

The constructor for this class is marked as internal. Third-party code should not call the constructor directly or create subclasses that extend the`LiveSession`class.

**Signature:**  

    export declare class LiveSession 

## Properties

|                                                  Property                                                   | Modifiers |  Type   |                                                    Description                                                     |
|-------------------------------------------------------------------------------------------------------------|-----------|---------|--------------------------------------------------------------------------------------------------------------------|
| [inConversation](https://firebase.google.com/docs/reference/js/ai.livesession.md#livesessioninconversation) |           | boolean | ***(Public Preview)*** Indicates whether this Live session is being controlled by an`AudioConversationController`. |
| [isClosed](https://firebase.google.com/docs/reference/js/ai.livesession.md#livesessionisclosed)             |           | boolean | ***(Public Preview)***Indicates whether this Live session is closed.                                               |

## Methods

|                                                                    Method                                                                    | Modifiers |                                                   Description                                                    |
|----------------------------------------------------------------------------------------------------------------------------------------------|-----------|------------------------------------------------------------------------------------------------------------------|
| [close()](https://firebase.google.com/docs/reference/js/ai.livesession.md#livesessionclose)                                                  |           | ***(Public Preview)***Closes this session. All methods on this session will throw an error once this resolves.   |
| [receive()](https://firebase.google.com/docs/reference/js/ai.livesession.md#livesessionreceive)                                              |           | ***(Public Preview)***Yields messages received from the server. This can only be used by one consumer at a time. |
| [send(request, turnComplete)](https://firebase.google.com/docs/reference/js/ai.livesession.md#livesessionsend)                               |           | ***(Public Preview)***Sends content to the server.                                                               |
| [sendAudioRealtime(blob)](https://firebase.google.com/docs/reference/js/ai.livesession.md#livesessionsendaudiorealtime)                      |           | ***(Public Preview)***Sends audio data to the server in realtime.                                                |
| [sendFunctionResponses(functionResponses)](https://firebase.google.com/docs/reference/js/ai.livesession.md#livesessionsendfunctionresponses) |           | ***(Public Preview)***Sends function responses to the server.                                                    |
| [sendMediaChunks(mediaChunks)](https://firebase.google.com/docs/reference/js/ai.livesession.md#livesessionsendmediachunks)                   |           | ***(Public Preview)***Sends realtime input to the server.                                                        |
| [sendMediaStream(mediaChunkStream)](https://firebase.google.com/docs/reference/js/ai.livesession.md#livesessionsendmediastream)              |           | ***(Public Preview)***                                                                                           |
| [sendTextRealtime(text)](https://firebase.google.com/docs/reference/js/ai.livesession.md#livesessionsendtextrealtime)                        |           | ***(Public Preview)***Sends text to the server in realtime.                                                      |
| [sendVideoRealtime(blob)](https://firebase.google.com/docs/reference/js/ai.livesession.md#livesessionsendvideorealtime)                      |           | ***(Public Preview)***Sends video data to the server in realtime.                                                |

## LiveSession.inConversation

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Indicates whether this Live session is being controlled by an`AudioConversationController`.

**Signature:**  

    inConversation: boolean;

## LiveSession.isClosed

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Indicates whether this Live session is closed.

**Signature:**  

    isClosed: boolean;

## LiveSession.close()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Closes this session. All methods on this session will throw an error once this resolves.

**Signature:**  

    close(): Promise<void>;

**Returns:**

Promise\<void\>

## LiveSession.receive()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Yields messages received from the server. This can only be used by one consumer at a time.

**Signature:**  

    receive(): AsyncGenerator<LiveServerContent | LiveServerToolCall | LiveServerToolCallCancellation>;

**Returns:**

AsyncGenerator\<[LiveServerContent](https://firebase.google.com/docs/reference/js/ai.liveservercontent.md#liveservercontent_interface)\|[LiveServerToolCall](https://firebase.google.com/docs/reference/js/ai.liveservertoolcall.md#liveservertoolcall_interface)\|[LiveServerToolCallCancellation](https://firebase.google.com/docs/reference/js/ai.liveservertoolcallcancellation.md#liveservertoolcallcancellation_interface)\>

An`AsyncGenerator`that yields server messages as they arrive.

#### Exceptions

If the session is already closed, or if we receive a response that we don't support.

## LiveSession.send()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Sends content to the server.

**Signature:**  

    send(request: string | Array<string | Part>, turnComplete?: boolean): Promise<void>;

#### Parameters

|  Parameter   |                                             Type                                             |                      Description                      |
|--------------|----------------------------------------------------------------------------------------------|-------------------------------------------------------|
| request      | string \| Array\<string \|[Part](https://firebase.google.com/docs/reference/js/ai.md#part)\> | The message to send to the model.                     |
| turnComplete | boolean                                                                                      | Indicates if the turn is complete. Defaults to false. |

**Returns:**

Promise\<void\>

#### Exceptions

If this session has been closed.

## LiveSession.sendAudioRealtime()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Sends audio data to the server in realtime.

The server requires that the audio data is base64-encoded 16-bit PCM at 16kHz little-endian.

**Signature:**  

    sendAudioRealtime(blob: GenerativeContentBlob): Promise<void>;

#### Parameters

| Parameter |                                                                Type                                                                |                          Description                           |
|-----------|------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------|
| blob      | [GenerativeContentBlob](https://firebase.google.com/docs/reference/js/ai.generativecontentblob.md#generativecontentblob_interface) | The base64-encoded PCM data to send to the server in realtime. |

**Returns:**

Promise\<void\>

#### Exceptions

If this session has been closed.

### Example

    // const pcmData = ... base64-encoded 16-bit PCM at 16kHz little-endian.
    const blob = { mimeType: "audio/pcm", data: pcmData };
    liveSession.sendAudioRealtime(blob);

## LiveSession.sendFunctionResponses()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Sends function responses to the server.

**Signature:**  

    sendFunctionResponses(functionResponses: FunctionResponse[]): Promise<void>;

#### Parameters

|     Parameter     |                                                          Type                                                           |           Description           |
|-------------------|-------------------------------------------------------------------------------------------------------------------------|---------------------------------|
| functionResponses | [FunctionResponse](https://firebase.google.com/docs/reference/js/ai.functionresponse.md#functionresponse_interface)\[\] | The function responses to send. |

**Returns:**

Promise\<void\>

#### Exceptions

If this session has been closed.

## LiveSession.sendMediaChunks()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.
> | **Warning:** This API is now obsolete.
>
> Use`sendTextRealtime()`,`sendAudioRealtime()`, and`sendVideoRealtime()`instead.

Sends realtime input to the server.

**Signature:**  

    sendMediaChunks(mediaChunks: GenerativeContentBlob[]): Promise<void>;

#### Parameters

|  Parameter  |                                                                  Type                                                                  |        Description        |
|-------------|----------------------------------------------------------------------------------------------------------------------------------------|---------------------------|
| mediaChunks | [GenerativeContentBlob](https://firebase.google.com/docs/reference/js/ai.generativecontentblob.md#generativecontentblob_interface)\[\] | The media chunks to send. |

**Returns:**

Promise\<void\>

#### Exceptions

If this session has been closed.

## LiveSession.sendMediaStream()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.
> | **Warning:** This API is now obsolete.
>
> Use`sendTextRealtime()`,`sendAudioRealtime()`, and`sendVideoRealtime()`instead.
>
> Sends a stream of[GenerativeContentBlob](https://firebase.google.com/docs/reference/js/ai.generativecontentblob.md#generativecontentblob_interface).

**Signature:**  

    sendMediaStream(mediaChunkStream: ReadableStream<GenerativeContentBlob>): Promise<void>;

#### Parameters

|    Parameter     |                                                                         Type                                                                         |                                                                       Description                                                                       |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| mediaChunkStream | ReadableStream\<[GenerativeContentBlob](https://firebase.google.com/docs/reference/js/ai.generativecontentblob.md#generativecontentblob_interface)\> | The stream of[GenerativeContentBlob](https://firebase.google.com/docs/reference/js/ai.generativecontentblob.md#generativecontentblob_interface)to send. |

**Returns:**

Promise\<void\>

#### Exceptions

If this session has been closed.

## LiveSession.sendTextRealtime()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Sends text to the server in realtime.

**Signature:**  

    sendTextRealtime(text: string): Promise<void>;

#### Parameters

| Parameter |  Type  |      Description       |
|-----------|--------|------------------------|
| text      | string | The text data to send. |

**Returns:**

Promise\<void\>

#### Exceptions

If this session has been closed.

### Example

    liveSession.sendTextRealtime("Hello, how are you?");

## LiveSession.sendVideoRealtime()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Sends video data to the server in realtime.

The server requires that the video is sent as individual video frames at 1 FPS. It is recommended to set`mimeType`to`image/jpeg`.

**Signature:**  

    sendVideoRealtime(blob: GenerativeContentBlob): Promise<void>;

#### Parameters

| Parameter |                                                                Type                                                                |                           Description                            |
|-----------|------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------|
| blob      | [GenerativeContentBlob](https://firebase.google.com/docs/reference/js/ai.generativecontentblob.md#generativecontentblob_interface) | The base64-encoded video data to send to the server in realtime. |

**Returns:**

Promise\<void\>

#### Exceptions

If this session has been closed.

### Example

    // const videoFrame = ... base64-encoded JPEG data
    const blob = { mimeType: "image/jpeg", data: videoFrame };
    liveSession.sendVideoRealtime(blob);