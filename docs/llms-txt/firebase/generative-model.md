# Source: https://firebase.google.com/docs/reference/unity/class/firebase/a-i/generative-model.md.txt

# Firebase.AI.GenerativeModel Class Reference

# Firebase.AI.GenerativeModel

A type that represents a remote multimodal model (like Gemini), with the ability to generate content based on various input types.

## Summary

|                                                                                                                                                                                                                                                                                                                                                                                                                ### Public functions                                                                                                                                                                                                                                                                                                                                                                                                                ||
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [CountTokensAsync](https://firebase.google.com/docs/reference/unity/class/firebase/a-i/generative-model#class_firebase_1_1_a_i_1_1_generative_model_1a368f5b22db23acaf4082fd0eca963a70)`(`[ModelContent](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/model-content#struct_firebase_1_1_a_i_1_1_model_content)` content, CancellationToken cancellationToken)`                          | `Task< `[CountTokensResponse](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/count-tokens-response#struct_firebase_1_1_a_i_1_1_count_tokens_response)` >` Counts the number of tokens in a prompt using the model's tokenizer.                                                                                                                                                                              |
| [CountTokensAsync](https://firebase.google.com/docs/reference/unity/class/firebase/a-i/generative-model#class_firebase_1_1_a_i_1_1_generative_model_1ad3babb2b39ec975dbd05a7dcb7ff065d)`(string text, CancellationToken cancellationToken)`                                                                                                                                                                     | `Task< `[CountTokensResponse](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/count-tokens-response#struct_firebase_1_1_a_i_1_1_count_tokens_response)` >` Counts the number of tokens in a prompt using the model's tokenizer.                                                                                                                                                                              |
| [CountTokensAsync](https://firebase.google.com/docs/reference/unity/class/firebase/a-i/generative-model#class_firebase_1_1_a_i_1_1_generative_model_1a56f1ffcd076cf58febca9f889f410182)`(IEnumerable< `[ModelContent](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/model-content#struct_firebase_1_1_a_i_1_1_model_content)` > content, CancellationToken cancellationToken)`           | `Task< `[CountTokensResponse](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/count-tokens-response#struct_firebase_1_1_a_i_1_1_count_tokens_response)` >` Counts the number of tokens in a prompt using the model's tokenizer.                                                                                                                                                                              |
| [GenerateContentAsync](https://firebase.google.com/docs/reference/unity/class/firebase/a-i/generative-model#class_firebase_1_1_a_i_1_1_generative_model_1aeeac2a7d4f3e7478c2076e491b069e46)`(`[ModelContent](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/model-content#struct_firebase_1_1_a_i_1_1_model_content)` content, CancellationToken cancellationToken)`                      | `Task< `[GenerateContentResponse](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/generate-content-response#struct_firebase_1_1_a_i_1_1_generate_content_response)` >` Generates new content from input [ModelContent](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/model-content#struct_firebase_1_1_a_i_1_1_model_content) given to the model as a prompt.                         |
| [GenerateContentAsync](https://firebase.google.com/docs/reference/unity/class/firebase/a-i/generative-model#class_firebase_1_1_a_i_1_1_generative_model_1ad42e961e24915185c953ca96d003afd4)`(string text, CancellationToken cancellationToken)`                                                                                                                                                                 | `Task< `[GenerateContentResponse](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/generate-content-response#struct_firebase_1_1_a_i_1_1_generate_content_response)` >` Generates new content from input text given to the model as a prompt.                                                                                                                                                                 |
| [GenerateContentAsync](https://firebase.google.com/docs/reference/unity/class/firebase/a-i/generative-model#class_firebase_1_1_a_i_1_1_generative_model_1a0b7345502be1f0b1ceb3491a765a9f21)`(IEnumerable< `[ModelContent](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/model-content#struct_firebase_1_1_a_i_1_1_model_content)` > content, CancellationToken cancellationToken)`       | `Task< `[GenerateContentResponse](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/generate-content-response#struct_firebase_1_1_a_i_1_1_generate_content_response)` >` Generates new content from input [ModelContent](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/model-content#struct_firebase_1_1_a_i_1_1_model_content) given to the model as a prompt.                         |
| [GenerateContentStreamAsync](https://firebase.google.com/docs/reference/unity/class/firebase/a-i/generative-model#class_firebase_1_1_a_i_1_1_generative_model_1a2a7a7ea04478cdd8f946091b2b416076)`(`[ModelContent](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/model-content#struct_firebase_1_1_a_i_1_1_model_content)` content, CancellationToken cancellationToken)`                | `IAsyncEnumerable< `[GenerateContentResponse](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/generate-content-response#struct_firebase_1_1_a_i_1_1_generate_content_response)` >` Generates new content as a stream from input [ModelContent](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/model-content#struct_firebase_1_1_a_i_1_1_model_content) given to the model as a prompt. |
| [GenerateContentStreamAsync](https://firebase.google.com/docs/reference/unity/class/firebase/a-i/generative-model#class_firebase_1_1_a_i_1_1_generative_model_1a6ed42cafded4b4286881ba2a58603056)`(string text, CancellationToken cancellationToken)`                                                                                                                                                           | `IAsyncEnumerable< `[GenerateContentResponse](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/generate-content-response#struct_firebase_1_1_a_i_1_1_generate_content_response)` >` Generates new content as a stream from input text given to the model as a prompt.                                                                                                                                         |
| [GenerateContentStreamAsync](https://firebase.google.com/docs/reference/unity/class/firebase/a-i/generative-model#class_firebase_1_1_a_i_1_1_generative_model_1ad5d2c5e9917edde91c29125cd19a6039)`(IEnumerable< `[ModelContent](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/model-content#struct_firebase_1_1_a_i_1_1_model_content)` > content, CancellationToken cancellationToken)` | `IAsyncEnumerable< `[GenerateContentResponse](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/generate-content-response#struct_firebase_1_1_a_i_1_1_generate_content_response)` >` Generates new content as a stream from input [ModelContent](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/model-content#struct_firebase_1_1_a_i_1_1_model_content) given to the model as a prompt. |
| [StartChat](https://firebase.google.com/docs/reference/unity/class/firebase/a-i/generative-model#class_firebase_1_1_a_i_1_1_generative_model_1ad2ba1e6122860b77fa6b8d3a7afcb09a)`(params `[ModelContent](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/model-content#struct_firebase_1_1_a_i_1_1_model_content)`[] history)`                                                             | [Chat](https://firebase.google.com/docs/reference/unity/class/firebase/a-i/chat#class_firebase_1_1_a_i_1_1_chat) Creates a new chat conversation using this model with the provided history.                                                                                                                                                                                                                                      |
| [StartChat](https://firebase.google.com/docs/reference/unity/class/firebase/a-i/generative-model#class_firebase_1_1_a_i_1_1_generative_model_1a12da660c7e5236df5c4f25697f326ae7)`(IEnumerable< `[ModelContent](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/model-content#struct_firebase_1_1_a_i_1_1_model_content)` > history)`                                                       | [Chat](https://firebase.google.com/docs/reference/unity/class/firebase/a-i/chat#class_firebase_1_1_a_i_1_1_chat) Creates a new chat conversation using this model with the provided history.                                                                                                                                                                                                                                      |

## Public functions

### CountTokensAsync

```c#
Task< CountTokensResponse > CountTokensAsync(
  ModelContent content,
  CancellationToken cancellationToken
)
```  
Counts the number of tokens in a prompt using the model's tokenizer.

<br />

|                                                                                                               Details                                                                                                               ||
|-------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |-----------|-------------------------------------------| | `content` | The input given to the model as a prompt. |                                                                                                    |
| Exceptions  | |------------------------|-------------------------------------------------| | `HttpRequestException` | Thrown when an error occurs during the request. |                                                              |
| **Returns** | The [CountTokensResponse](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/count-tokens-response#struct_firebase_1_1_a_i_1_1_count_tokens_response) of running the model's tokenizer on the input. |

### CountTokensAsync

```c#
Task< CountTokensResponse > CountTokensAsync(
  string text,
  CancellationToken cancellationToken
)
```  
Counts the number of tokens in a prompt using the model's tokenizer.

<br />

|                                                                                                                 Details                                                                                                                 ||
|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |---------------------|------------------------------------------------| | `text`              | The text input given to the model as a prompt. | | `cancellationToken` | An optional token to cancel the operation.     | |
| Exceptions  | |------------------------|-------------------------------------------------| | `HttpRequestException` | Thrown when an error occurs during the request. |                                                                  |
| **Returns** | The [CountTokensResponse](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/count-tokens-response#struct_firebase_1_1_a_i_1_1_count_tokens_response) of running the model's tokenizer on the input.     |

### CountTokensAsync

```c#
Task< CountTokensResponse > CountTokensAsync(
  IEnumerable< ModelContent > content,
  CancellationToken cancellationToken
)
```  
Counts the number of tokens in a prompt using the model's tokenizer.

<br />

|                                                                                                               Details                                                                                                               ||
|-------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |---------------------|--------------------------------------------| | `content`           | The input given to the model as a prompt.  | | `cancellationToken` | An optional token to cancel the operation. |         |
| Exceptions  | |------------------------|-------------------------------------------------| | `HttpRequestException` | Thrown when an error occurs during the request. |                                                              |
| **Returns** | The [CountTokensResponse](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/count-tokens-response#struct_firebase_1_1_a_i_1_1_count_tokens_response) of running the model's tokenizer on the input. |

### GenerateContentAsync

```c#
Task< GenerateContentResponse > GenerateContentAsync(
  ModelContent content,
  CancellationToken cancellationToken
)
```  
Generates new content from input [ModelContent](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/model-content#struct_firebase_1_1_a_i_1_1_model_content) given to the model as a prompt.

<br />

|                                                                                                           Details                                                                                                           ||
|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |---------------------|--------------------------------------------| | `content`           | The input given to the model as a prompt.  | | `cancellationToken` | An optional token to cancel the operation. | |
| Exceptions  | |------------------------|--------------------------------------------------------| | `HttpRequestException` | Thrown when an error occurs during content generation. |                                        |
| **Returns** | The generated content response from the model.                                                                                                                                                                 |

### GenerateContentAsync

```c#
Task< GenerateContentResponse > GenerateContentAsync(
  string text,
  CancellationToken cancellationToken
)
```  
Generates new content from input text given to the model as a prompt.

<br />

|                                                                                                           Details                                                                                                           ||
|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |---------------------|--------------------------------------------| | `text`              | The text given to the model as a prompt.   | | `cancellationToken` | An optional token to cancel the operation. | |
| Exceptions  | |------------------------|--------------------------------------------------------| | `HttpRequestException` | Thrown when an error occurs during content generation. |                                        |
| **Returns** | The generated content response from the model.                                                                                                                                                                 |

### GenerateContentAsync

```c#
Task< GenerateContentResponse > GenerateContentAsync(
  IEnumerable< ModelContent > content,
  CancellationToken cancellationToken
)
```  
Generates new content from input [ModelContent](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/model-content#struct_firebase_1_1_a_i_1_1_model_content) given to the model as a prompt.

<br />

|                                                                                                           Details                                                                                                           ||
|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |---------------------|--------------------------------------------| | `content`           | The input given to the model as a prompt.  | | `cancellationToken` | An optional token to cancel the operation. | |
| Exceptions  | |------------------------|--------------------------------------------------------| | `HttpRequestException` | Thrown when an error occurs during content generation. |                                        |
| **Returns** | The generated content response from the model.                                                                                                                                                                 |

### GenerateContentStreamAsync

```c#
IAsyncEnumerable< GenerateContentResponse > GenerateContentStreamAsync(
  ModelContent content,
  CancellationToken cancellationToken
)
```  
Generates new content as a stream from input [ModelContent](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/model-content#struct_firebase_1_1_a_i_1_1_model_content) given to the model as a prompt.

<br />

|                                                                                                           Details                                                                                                           ||
|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |---------------------|--------------------------------------------| | `content`           | The input given to the model as a prompt.  | | `cancellationToken` | An optional token to cancel the operation. | |
| Exceptions  | |------------------------|--------------------------------------------------------| | `HttpRequestException` | Thrown when an error occurs during content generation. |                                        |
| **Returns** | A stream of generated content responses from the model.                                                                                                                                                        |

### GenerateContentStreamAsync

```c#
IAsyncEnumerable< GenerateContentResponse > GenerateContentStreamAsync(
  string text,
  CancellationToken cancellationToken
)
```  
Generates new content as a stream from input text given to the model as a prompt.

<br />

|                                                                                                           Details                                                                                                           ||
|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |---------------------|--------------------------------------------| | `text`              | The text given to the model as a prompt.   | | `cancellationToken` | An optional token to cancel the operation. | |
| Exceptions  | |------------------------|--------------------------------------------------------| | `HttpRequestException` | Thrown when an error occurs during content generation. |                                        |
| **Returns** | A stream of generated content responses from the model.                                                                                                                                                        |

### GenerateContentStreamAsync

```c#
IAsyncEnumerable< GenerateContentResponse > GenerateContentStreamAsync(
  IEnumerable< ModelContent > content,
  CancellationToken cancellationToken
)
```  
Generates new content as a stream from input [ModelContent](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/model-content#struct_firebase_1_1_a_i_1_1_model_content) given to the model as a prompt.

<br />

|                                                                                                           Details                                                                                                           ||
|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |---------------------|--------------------------------------------| | `content`           | The input given to the model as a prompt.  | | `cancellationToken` | An optional token to cancel the operation. | |
| Exceptions  | |------------------------|--------------------------------------------------------| | `HttpRequestException` | Thrown when an error occurs during content generation. |                                        |
| **Returns** | A stream of generated content responses from the model.                                                                                                                                                        |

### StartChat

```c#
Chat StartChat(
  params ModelContent[] history
)
```  
Creates a new chat conversation using this model with the provided history.

<br />

|                                                          Details                                                          ||
|------------|---------------------------------------------------------------------------------------------------------------|
| Parameters | |-----------|----------------------------------------| | `history` | Initial content history to start with. | |

### StartChat

```c#
Chat StartChat(
  IEnumerable< ModelContent > history
)
```  
Creates a new chat conversation using this model with the provided history.

<br />

|                                                          Details                                                          ||
|------------|---------------------------------------------------------------------------------------------------------------|
| Parameters | |-----------|----------------------------------------| | `history` | Initial content history to start with. | |