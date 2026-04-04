# Source: https://firebase.google.com/docs/reference/unity/class/firebase/a-i/live-session.md.txt

# Firebase.AI.LiveSession

Manages asynchronous communication with Gemini model over a WebSocket connection.

## Summary

### Inheritance

Inherits from: IDisposable

|                                                                                         ### Protected functions                                                                                          ||
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------|
| [Dispose](https://firebase.google.com/docs/reference/unity/class/firebase/a-i/live-session#class_firebase_1_1_a_i_1_1_live_session_1a278d1927b09ed231da5b7cd9ab062527)`(bool disposing)` | `virtual void` |

|                                                                                                                                                                                                                                                                                                                                          ### Public functions                                                                                                                                                                                                                                                                                                                                          ||
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [CloseAsync](https://firebase.google.com/docs/reference/unity/class/firebase/a-i/live-session#class_firebase_1_1_a_i_1_1_live_session_1a3f3e7e81c5b44e3d7e902594dc38603e)`(CancellationToken cancellationToken)`                                                                                                                                                                                                                                    | `Task` Close the [LiveSession](https://firebase.google.com/docs/reference/unity/class/firebase/a-i/live-session#class_firebase_1_1_a_i_1_1_live_session).                                                                                         |
| [Dispose](https://firebase.google.com/docs/reference/unity/class/firebase/a-i/live-session#class_firebase_1_1_a_i_1_1_live_session_1aa8a0e611e516105fc2bef48673c24cff)`()`                                                                                                                                                                                                                                                                          | `void`                                                                                                                                                                                                                                            |
| [ReceiveAsync](https://firebase.google.com/docs/reference/unity/class/firebase/a-i/live-session#class_firebase_1_1_a_i_1_1_live_session_1aacedbd79d0cb1c39e6df6654c243e96f)`(CancellationToken cancellationToken)`                                                                                                                                                                                                                                  | `async IAsyncEnumerable< `[LiveSessionResponse](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/live-session-response#struct_firebase_1_1_a_i_1_1_live_session_response)` >` Receives a stream of responses from the server. |
| [SendAsync](https://firebase.google.com/docs/reference/unity/class/firebase/a-i/live-session#class_firebase_1_1_a_i_1_1_live_session_1a8f64581b489c7ffad5e30a242cabdffa)`(`[ModelContent](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/model-content#struct_firebase_1_1_a_i_1_1_model_content)`? content, bool turnComplete, CancellationToken cancellationToken)`                                                         | `async Task` Sends a single piece of content to the server.                                                                                                                                                                                       |
| [SendAudioAsync](https://firebase.google.com/docs/reference/unity/class/firebase/a-i/live-session#class_firebase_1_1_a_i_1_1_live_session_1a1fa43af8e9a84ea5022a493a30274bb4)`(float[] audioData, CancellationToken cancellationToken)`                                                                                                                                                                                                             | `Task` Convenience function for sending audio data in a float\[\] to the server.                                                                                                                                                                  |
| [SendAudioRealtimeAsync](https://firebase.google.com/docs/reference/unity/class/firebase/a-i/live-session#class_firebase_1_1_a_i_1_1_live_session_1af83aedfba2095ff47e9be54042f19635)`(`[ModelContent.InlineDataPart](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/model-content/inline-data-part#struct_firebase_1_1_a_i_1_1_model_content_1_1_inline_data_part)` audio, CancellationToken cancellationToken)`             | `async Task` Sends audio data to the server in realtime.                                                                                                                                                                                          |
| [SendMediaChunksAsync](https://firebase.google.com/docs/reference/unity/class/firebase/a-i/live-session#class_firebase_1_1_a_i_1_1_live_session_1afd03a3dfb47b89b0e802d0e6c5430183)`(List< `[ModelContent.InlineDataPart](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/model-content/inline-data-part#struct_firebase_1_1_a_i_1_1_model_content_1_1_inline_data_part)` > mediaChunks, CancellationToken cancellationToken)` | `async Task` **[Deprecated.](https://firebase.google.com/docs/reference/unity/deprecated/deprecated)** Use SendAudioRealtimeAsync, SendVideoRealtimeAsync, or SendTextRealtimeAsync instead. Send realtime input to the server.                   |
| [SendTextRealtimeAsync](https://firebase.google.com/docs/reference/unity/class/firebase/a-i/live-session#class_firebase_1_1_a_i_1_1_live_session_1a2e4e32c4dc0f57e2c0bada4534da7b9d)`(string text, CancellationToken cancellationToken)`                                                                                                                                                                                                            | `async Task` Sends text data to the server in realtime.                                                                                                                                                                                           |
| [SendVideoRealtimeAsync](https://firebase.google.com/docs/reference/unity/class/firebase/a-i/live-session#class_firebase_1_1_a_i_1_1_live_session_1af42e4167bcb7a2fe84dc2f8e2bb451b3)`(`[ModelContent.InlineDataPart](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/model-content/inline-data-part#struct_firebase_1_1_a_i_1_1_model_content_1_1_inline_data_part)` video, CancellationToken cancellationToken)`             | `async Task` Sends video data to the server in realtime.                                                                                                                                                                                          |

## Protected functions

### Dispose

```c#
virtual void Dispose(
  bool disposing
)
```  

## Public functions

### CloseAsync

```c#
Task CloseAsync(
  CancellationToken cancellationToken
)
```  
Close the [LiveSession](https://firebase.google.com/docs/reference/unity/class/firebase/a-i/live-session#class_firebase_1_1_a_i_1_1_live_session).

<br />

|                                                              Details                                                              ||
|------------|-----------------------------------------------------------------------------------------------------------------------|
| Parameters | |---------------------|----------------------------------| | `cancellationToken` | A token to cancel the operation. | |

### Dispose

```c#
void Dispose()
```  

### ReceiveAsync

```c#
async IAsyncEnumerable< LiveSessionResponse > ReceiveAsync(
  CancellationToken cancellationToken
)
```  
Receives a stream of responses from the server.

Having multiple of these ongoing will result in unexpected behavior. Closes upon receiving a TurnComplete from the server.

<br />

|                                                              Details                                                               ||
|-------------|-----------------------------------------------------------------------------------------------------------------------|
| Parameters  | |---------------------|----------------------------------| | `cancellationToken` | A token to cancel the operation. | |
| **Returns** | A stream of `LiveContentResponse`s from the backend.                                                                  |

### SendAsync

```c#
async Task SendAsync(
  ModelContent? content,
  bool turnComplete,
  CancellationToken cancellationToken
)
```  
Sends a single piece of content to the server.

<br />

|                                                                                                                                                                               Details                                                                                                                                                                               ||
|------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |---------------------|-------------------------------------------------------------| | `content`           | The content to send.                                        | | `turnComplete`      | Indicates to the server that the client's turn is complete. | | `cancellationToken` | A token to cancel the send operation.                       | |

### SendAudioAsync

```c#
Task SendAudioAsync(
  float[] audioData,
  CancellationToken cancellationToken
)
```  
Convenience function for sending audio data in a float\[\] to the server.

<br />

|                                                                                                                                                                     Details                                                                                                                                                                     ||
|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |---------------------|-----------------------------------------------------------------------------------| | `audioData`         | The audio data to send. Expected format: 16 bit PCM audio at 16kHz little-endian. | | `cancellationToken` | A token to cancel the send operation.                                             | |

### SendAudioRealtimeAsync

```c#
async Task SendAudioRealtimeAsync(
  ModelContent.InlineDataPart audio,
  CancellationToken cancellationToken
)
```  
Sends audio data to the server in realtime.

Check <https://ai.google.dev/api/live#bidigeneratecontentrealtimeinput> for details about the realtime input usage.

<br />

|                                                                                                   Details                                                                                                   ||
|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |---------------------|---------------------------------------| | `audio`             | The audio data to send.               | | `cancellationToken` | A token to cancel the send operation. | |

### SendMediaChunksAsync

```c#
async Task SendMediaChunksAsync(
  List< ModelContent.InlineDataPart > mediaChunks,
  CancellationToken cancellationToken
)
```  
Send realtime input to the server.

<br />

|                                                                                                   Details                                                                                                   ||
|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |---------------------|---------------------------------------| | `mediaChunks`       | A list of media chunks to send.       | | `cancellationToken` | A token to cancel the send operation. | |

Use SendAudioRealtimeAsync, SendVideoRealtimeAsync, or SendTextRealtimeAsync instead.

**[Deprecated.](https://firebase.google.com/docs/reference/unity/deprecated/deprecated)**Use SendAudioRealtimeAsync, SendVideoRealtimeAsync, or SendTextRealtimeAsync instead.  

### SendTextRealtimeAsync

```c#
async Task SendTextRealtimeAsync(
  string text,
  CancellationToken cancellationToken
)
```  
Sends text data to the server in realtime.

Check <https://ai.google.dev/api/live#bidigeneratecontentrealtimeinput> for details about the realtime input usage.

<br />

|                                                                                                   Details                                                                                                   ||
|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |---------------------|---------------------------------------| | `text`              | The text data to send.                | | `cancellationToken` | A token to cancel the send operation. | |

### SendVideoRealtimeAsync

```c#
async Task SendVideoRealtimeAsync(
  ModelContent.InlineDataPart video,
  CancellationToken cancellationToken
)
```  
Sends video data to the server in realtime.

Check <https://ai.google.dev/api/live#bidigeneratecontentrealtimeinput> for details about the realtime input usage.

<br />

|                                                                                                   Details                                                                                                   ||
|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |---------------------|---------------------------------------| | `video`             | The video data to send.               | | `cancellationToken` | A token to cancel the send operation. | |