# Source: https://firebase.google.com/docs/ai-logic/chat.md.txt

# Source: https://firebase.google.com/docs/reference/unity/class/firebase/a-i/chat.md.txt

# Source: https://firebase.google.com/docs/ai-logic/chat.md.txt

# Source: https://firebase.google.com/docs/reference/unity/class/firebase/a-i/chat.md.txt

# Firebase.AI.Chat Class Reference

# Firebase.AI.Chat

An object that represents a back-and-forth chat with a model, capturing the history and saving the context in memory between each message sent.

## Summary

|                                                                                                                                                                                                           ### Public attributes                                                                                                                                                                                                            ||
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [History](https://firebase.google.com/docs/reference/unity/class/firebase/a-i/chat#class_firebase_1_1_a_i_1_1_chat_1a05028fea0b0e874140f820248af70083)` => chatHistory` | `IReadOnlyList< `[ModelContent](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/model-content#struct_firebase_1_1_a_i_1_1_model_content)` >` The previous content from the chat that has been successfully sent and received from the model. |

|                                                                                                                                                                                                                                                                                                                       ### Public functions                                                                                                                                                                                                                                                                                                                       ||
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [SendMessageAsync](https://firebase.google.com/docs/reference/unity/class/firebase/a-i/chat#class_firebase_1_1_a_i_1_1_chat_1ac4d00229031d70b0efcc876d89f578fe)`(`[ModelContent](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/model-content#struct_firebase_1_1_a_i_1_1_model_content)` content, CancellationToken cancellationToken)`                      | `Task< `[GenerateContentResponse](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/generate-content-response#struct_firebase_1_1_a_i_1_1_generate_content_response)` >` Sends a message using the existing history of this chat as context.             |
| [SendMessageAsync](https://firebase.google.com/docs/reference/unity/class/firebase/a-i/chat#class_firebase_1_1_a_i_1_1_chat_1a39af1f752707a26e505e0173f314b5f2)`(string text, CancellationToken cancellationToken)`                                                                                                                                                                 | `Task< `[GenerateContentResponse](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/generate-content-response#struct_firebase_1_1_a_i_1_1_generate_content_response)` >` Sends a message using the existing history of this chat as context.             |
| [SendMessageAsync](https://firebase.google.com/docs/reference/unity/class/firebase/a-i/chat#class_firebase_1_1_a_i_1_1_chat_1af1c13613e80fa5c671bbf5f3182bb7f5)`(IEnumerable< `[ModelContent](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/model-content#struct_firebase_1_1_a_i_1_1_model_content)` > content, CancellationToken cancellationToken)`       | `Task< `[GenerateContentResponse](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/generate-content-response#struct_firebase_1_1_a_i_1_1_generate_content_response)` >` Sends a message using the existing history of this chat as context.             |
| [SendMessageStreamAsync](https://firebase.google.com/docs/reference/unity/class/firebase/a-i/chat#class_firebase_1_1_a_i_1_1_chat_1a098f0d94daaa192b14cc5e957f7b0a94)`(`[ModelContent](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/model-content#struct_firebase_1_1_a_i_1_1_model_content)` content, CancellationToken cancellationToken)`                | `IAsyncEnumerable< `[GenerateContentResponse](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/generate-content-response#struct_firebase_1_1_a_i_1_1_generate_content_response)` >` Sends a message using the existing history of this chat as context. |
| [SendMessageStreamAsync](https://firebase.google.com/docs/reference/unity/class/firebase/a-i/chat#class_firebase_1_1_a_i_1_1_chat_1ade761641989fc007a27d622b02c8b28c)`(string text, CancellationToken cancellationToken)`                                                                                                                                                           | `IAsyncEnumerable< `[GenerateContentResponse](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/generate-content-response#struct_firebase_1_1_a_i_1_1_generate_content_response)` >` Sends a message using the existing history of this chat as context. |
| [SendMessageStreamAsync](https://firebase.google.com/docs/reference/unity/class/firebase/a-i/chat#class_firebase_1_1_a_i_1_1_chat_1a8123b684281c4024cc5953d6d4328e7a)`(IEnumerable< `[ModelContent](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/model-content#struct_firebase_1_1_a_i_1_1_model_content)` > content, CancellationToken cancellationToken)` | `IAsyncEnumerable< `[GenerateContentResponse](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/generate-content-response#struct_firebase_1_1_a_i_1_1_generate_content_response)` >` Sends a message using the existing history of this chat as context. |

## Public attributes

### History

```c#
IReadOnlyList< ModelContent > History => chatHistory
```  
The previous content from the chat that has been successfully sent and received from the model.

This will be provided to the model for each message sent as context for the discussion.

## Public functions

### SendMessageAsync

```c#
Task< GenerateContentResponse > SendMessageAsync(
  ModelContent content,
  CancellationToken cancellationToken
)
```  
Sends a message using the existing history of this chat as context.

If successful, the message and response will be added to the history. If unsuccessful, history will remain unchanged.

<br />

|                                                                                                           Details                                                                                                           ||
|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |---------------------|--------------------------------------------| | `content`           | The input given to the model as a prompt.  | | `cancellationToken` | An optional token to cancel the operation. | |
| Exceptions  | |------------------------|--------------------------------------------------------| | `HttpRequestException` | Thrown when an error occurs during content generation. |                                        |
| **Returns** | The model's response if no error occurred.                                                                                                                                                                     |

### SendMessageAsync

```c#
Task< GenerateContentResponse > SendMessageAsync(
  string text,
  CancellationToken cancellationToken
)
```  
Sends a message using the existing history of this chat as context.

If successful, the message and response will be added to the history. If unsuccessful, history will remain unchanged.

<br />

|                                                                                                           Details                                                                                                           ||
|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |---------------------|--------------------------------------------| | `text`              | The text given to the model as a prompt.   | | `cancellationToken` | An optional token to cancel the operation. | |
| Exceptions  | |------------------------|--------------------------------------------------------| | `HttpRequestException` | Thrown when an error occurs during content generation. |                                        |
| **Returns** | The model's response if no error occurred.                                                                                                                                                                     |

### SendMessageAsync

```c#
Task< GenerateContentResponse > SendMessageAsync(
  IEnumerable< ModelContent > content,
  CancellationToken cancellationToken
)
```  
Sends a message using the existing history of this chat as context.

If successful, the message and response will be added to the history. If unsuccessful, history will remain unchanged.

<br />

|                                                                                                           Details                                                                                                           ||
|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |---------------------|--------------------------------------------| | `content`           | The input given to the model as a prompt.  | | `cancellationToken` | An optional token to cancel the operation. | |
| Exceptions  | |------------------------|--------------------------------------------------------| | `HttpRequestException` | Thrown when an error occurs during content generation. |                                        |
| **Returns** | The model's response if no error occurred.                                                                                                                                                                     |

### SendMessageStreamAsync

```c#
IAsyncEnumerable< GenerateContentResponse > SendMessageStreamAsync(
  ModelContent content,
  CancellationToken cancellationToken
)
```  
Sends a message using the existing history of this chat as context.

If successful, the message and response will be added to the history. If unsuccessful, history will remain unchanged.

<br />

|                                                                                                           Details                                                                                                           ||
|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |---------------------|--------------------------------------------| | `content`           | The input given to the model as a prompt.  | | `cancellationToken` | An optional token to cancel the operation. | |
| Exceptions  | |------------------------|--------------------------------------------------------| | `HttpRequestException` | Thrown when an error occurs during content generation. |                                        |
| **Returns** | A stream of generated content responses from the model.                                                                                                                                                        |

### SendMessageStreamAsync

```c#
IAsyncEnumerable< GenerateContentResponse > SendMessageStreamAsync(
  string text,
  CancellationToken cancellationToken
)
```  
Sends a message using the existing history of this chat as context.

If successful, the message and response will be added to the history. If unsuccessful, history will remain unchanged.

<br />

|                                                                                                           Details                                                                                                           ||
|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |---------------------|--------------------------------------------| | `text`              | The text given to the model as a prompt.   | | `cancellationToken` | An optional token to cancel the operation. | |
| Exceptions  | |------------------------|--------------------------------------------------------| | `HttpRequestException` | Thrown when an error occurs during content generation. |                                        |
| **Returns** | A stream of generated content responses from the model.                                                                                                                                                        |

### SendMessageStreamAsync

```c#
IAsyncEnumerable< GenerateContentResponse > SendMessageStreamAsync(
  IEnumerable< ModelContent > content,
  CancellationToken cancellationToken
)
```  
Sends a message using the existing history of this chat as context.

If successful, the message and response will be added to the history. If unsuccessful, history will remain unchanged.

<br />

|                                                                                                           Details                                                                                                           ||
|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |---------------------|--------------------------------------------| | `content`           | The input given to the model as a prompt.  | | `cancellationToken` | An optional token to cancel the operation. | |
| Exceptions  | |------------------------|--------------------------------------------------------| | `HttpRequestException` | Thrown when an error occurs during content generation. |                                        |
| **Returns** | A stream of generated content responses from the model.                                                                                                                                                        |