# Source: https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/model-content.md.txt

# Firebase.AI.ModelContent

A type describing data in media formats interpretable by an [AI](https://firebase.google.com/docs/reference/unity/namespace/firebase/a-i#namespace_firebase_1_1_a_i) model.

## Summary

Each generative [AI](https://firebase.google.com/docs/reference/unity/namespace/firebase/a-i#namespace_firebase_1_1_a_i) request or response contains a list of [ModelContent](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/model-content#struct_firebase_1_1_a_i_1_1_model_content)s, and each [ModelContent](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/model-content#struct_firebase_1_1_a_i_1_1_model_content) value may comprise multiple heterogeneous [ModelContent.Part](https://firebase.google.com/docs/reference/unity/interface/firebase/a-i/model-content/part#interface_firebase_1_1_a_i_1_1_model_content_1_1_part)s.

| ### Constructors and Destructors ||
|---|---|
| [ModelContent](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/model-content#struct_firebase_1_1_a_i_1_1_model_content_1a812b8f813f835686fa21746ef4afc66b)`(params `[Part](https://firebase.google.com/docs/reference/unity/interface/firebase/a-i/model-content/part#interface_firebase_1_1_a_i_1_1_model_content_1_1_part)`[] parts)` Creates a [ModelContent](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/model-content#struct_firebase_1_1_a_i_1_1_model_content) with the given [Part](https://firebase.google.com/docs/reference/unity/interface/firebase/a-i/model-content/part#interface_firebase_1_1_a_i_1_1_model_content_1_1_part)s, using the default `user` role. ||
| [ModelContent](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/model-content#struct_firebase_1_1_a_i_1_1_model_content_1a3bd07e67ac05acd09616e09ae0db928b)`(IEnumerable< `[Part](https://firebase.google.com/docs/reference/unity/interface/firebase/a-i/model-content/part#interface_firebase_1_1_a_i_1_1_model_content_1_1_part)` > parts)` Creates a [ModelContent](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/model-content#struct_firebase_1_1_a_i_1_1_model_content) with the given [Part](https://firebase.google.com/docs/reference/unity/interface/firebase/a-i/model-content/part#interface_firebase_1_1_a_i_1_1_model_content_1_1_part)s, using the default `user` role. ||
| [ModelContent](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/model-content#struct_firebase_1_1_a_i_1_1_model_content_1a029e0742a1c376a49369f0d34ba5bafd)`(string role, params `[Part](https://firebase.google.com/docs/reference/unity/interface/firebase/a-i/model-content/part#interface_firebase_1_1_a_i_1_1_model_content_1_1_part)`[] parts)` Creates a [ModelContent](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/model-content#struct_firebase_1_1_a_i_1_1_model_content) with the given role and [Part](https://firebase.google.com/docs/reference/unity/interface/firebase/a-i/model-content/part#interface_firebase_1_1_a_i_1_1_model_content_1_1_part)s. ||
| [ModelContent](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/model-content#struct_firebase_1_1_a_i_1_1_model_content_1af4fe935d651000f84ae3fa2ee7fa7de7)`(string role, IEnumerable< `[Part](https://firebase.google.com/docs/reference/unity/interface/firebase/a-i/model-content/part#interface_firebase_1_1_a_i_1_1_model_content_1_1_part)` > parts)` Creates a [ModelContent](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/model-content#struct_firebase_1_1_a_i_1_1_model_content) with the given role and [Part](https://firebase.google.com/docs/reference/unity/interface/firebase/a-i/model-content/part#interface_firebase_1_1_a_i_1_1_model_content_1_1_part)s. ||

|                                                                                                                                                                                                                                                               ### Properties                                                                                                                                                                                                                                                               ||
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Parts](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/model-content#struct_firebase_1_1_a_i_1_1_model_content_1ac4939692357f9eef2c7bec3470943de2) | `IReadOnlyList< `[Part](https://firebase.google.com/docs/reference/unity/interface/firebase/a-i/model-content/part#interface_firebase_1_1_a_i_1_1_model_content_1_1_part)` >` The data parts comprising this [ModelContent](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/model-content#struct_firebase_1_1_a_i_1_1_model_content) value. |
| [Role](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/model-content#struct_firebase_1_1_a_i_1_1_model_content_1afdffe87a4b19f503380eca867f16c5a5)  | `string` The role of the entity creating the [ModelContent](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/model-content#struct_firebase_1_1_a_i_1_1_model_content).                                                                                                                                                                       |

|                                                                                                                                                                                                                                                                                                                                                                                                          ### Public static functions                                                                                                                                                                                                                                                                                                                                                                                                          ||
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [FileData](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/model-content#struct_firebase_1_1_a_i_1_1_model_content_1a04ad68677efb7ab298acc1ad19b99c84)`(string mimeType, System.Uri uri)`                                        | [ModelContent](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/model-content#struct_firebase_1_1_a_i_1_1_model_content) Creates a new [ModelContent](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/model-content#struct_firebase_1_1_a_i_1_1_model_content) with the default `user` role, and a [FileDataPart](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/model-content/file-data-part#struct_firebase_1_1_a_i_1_1_model_content_1_1_file_data_part) containing the given mimeType and data.                     |
| [FunctionResponse](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/model-content#struct_firebase_1_1_a_i_1_1_model_content_1aa55a80a86347b9a9f1cb09e6fdb18da6)`(string name, IDictionary< string, object > response, string id)` | [ModelContent](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/model-content#struct_firebase_1_1_a_i_1_1_model_content) Creates a new [ModelContent](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/model-content#struct_firebase_1_1_a_i_1_1_model_content) with the default `user` role, and a [FunctionResponsePart](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/model-content/function-response-part#struct_firebase_1_1_a_i_1_1_model_content_1_1_function_response_part) containing the given name and args. |
| [InlineData](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/model-content#struct_firebase_1_1_a_i_1_1_model_content_1a6858dce77642ab44fa2c657a446662c2)`(string mimeType, byte[] data)`                                         | [ModelContent](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/model-content#struct_firebase_1_1_a_i_1_1_model_content) Creates a new [ModelContent](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/model-content#struct_firebase_1_1_a_i_1_1_model_content) with the default `user` role, and an [InlineDataPart](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/model-content/inline-data-part#struct_firebase_1_1_a_i_1_1_model_content_1_1_inline_data_part) containing the given mimeType and data.              |
| [Text](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/model-content#struct_firebase_1_1_a_i_1_1_model_content_1a780cca45b182699b9f8080ee43bcfdc9)`(string text)`                                                                | [ModelContent](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/model-content#struct_firebase_1_1_a_i_1_1_model_content) Creates a new [ModelContent](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/model-content#struct_firebase_1_1_a_i_1_1_model_content) with the default `user` role, and a [TextPart](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/model-content/text-part#struct_firebase_1_1_a_i_1_1_model_content_1_1_text_part) containing the given text.                                                |

|                                                                                                                                                                                                                   ### Structs                                                                                                                                                                                                                   ||
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Firebase.AI.ModelContent.CodeExecutionResultPart](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/model-content/code-execution-result-part) | A part containing the result of executing code.                                                                                                                                                                                                                              |
| [Firebase.AI.ModelContent.ExecutableCodePart](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/model-content/executable-code-part)            | A part containing code that was executed by the model.                                                                                                                                                                                                                       |
| [Firebase.AI.ModelContent.FileDataPart](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/model-content/file-data-part)                        | File data stored in Cloud [Storage](https://firebase.google.com/docs/reference/unity/namespace/firebase/storage#namespace_firebase_1_1_storage) for [Firebase](https://firebase.google.com/docs/reference/unity/namespace/firebase#namespace_firebase), referenced by a URI. |
| [Firebase.AI.ModelContent.FunctionCallPart](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/model-content/function-call-part)                | A predicted function call returned from the model.                                                                                                                                                                                                                           |
| [Firebase.AI.ModelContent.FunctionResponsePart](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/model-content/function-response-part)        | Result output from a function call.                                                                                                                                                                                                                                          |
| [Firebase.AI.ModelContent.InlineDataPart](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/model-content/inline-data-part)                    | Data with a specified media type.                                                                                                                                                                                                                                            |
| [Firebase.AI.ModelContent.TextPart](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/model-content/text-part)                                 | A text part containing a string value.                                                                                                                                                                                                                                       |

|                                                                                                                                               ### Interfaces                                                                                                                                                ||
|-----------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Firebase.AI.ModelContent.Part](https://firebase.google.com/docs/reference/unity/interface/firebase/a-i/model-content/part) | A discrete piece of data in a media format interpretable by an [AI](https://firebase.google.com/docs/reference/unity/namespace/firebase/a-i#namespace_firebase_1_1_a_i) model. |

## Properties

### Parts

```c#
IReadOnlyList< Part > Firebase::AI::ModelContent::Parts
```  
The data parts comprising this [ModelContent](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/model-content#struct_firebase_1_1_a_i_1_1_model_content) value.  

### Role

```c#
string Firebase::AI::ModelContent::Role
```  
The role of the entity creating the [ModelContent](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/model-content#struct_firebase_1_1_a_i_1_1_model_content).

For user-generated client requests, for example, the role is `user`.

## Public functions

### ModelContent

```c#
 Firebase::AI::ModelContent::ModelContent(
  params Part[] parts
)
```  
Creates a [ModelContent](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/model-content#struct_firebase_1_1_a_i_1_1_model_content) with the given [Part](https://firebase.google.com/docs/reference/unity/interface/firebase/a-i/model-content/part#interface_firebase_1_1_a_i_1_1_model_content_1_1_part)s, using the default `user` role.  

### ModelContent

```c#
 Firebase::AI::ModelContent::ModelContent(
  IEnumerable< Part > parts
)
```  
Creates a [ModelContent](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/model-content#struct_firebase_1_1_a_i_1_1_model_content) with the given [Part](https://firebase.google.com/docs/reference/unity/interface/firebase/a-i/model-content/part#interface_firebase_1_1_a_i_1_1_model_content_1_1_part)s, using the default `user` role.  

### ModelContent

```c#
 Firebase::AI::ModelContent::ModelContent(
  string role,
  params Part[] parts
)
```  
Creates a [ModelContent](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/model-content#struct_firebase_1_1_a_i_1_1_model_content) with the given role and [Part](https://firebase.google.com/docs/reference/unity/interface/firebase/a-i/model-content/part#interface_firebase_1_1_a_i_1_1_model_content_1_1_part)s.  

### ModelContent

```c#
 Firebase::AI::ModelContent::ModelContent(
  string role,
  IEnumerable< Part > parts
)
```  
Creates a [ModelContent](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/model-content#struct_firebase_1_1_a_i_1_1_model_content) with the given role and [Part](https://firebase.google.com/docs/reference/unity/interface/firebase/a-i/model-content/part#interface_firebase_1_1_a_i_1_1_model_content_1_1_part)s.

## Public static functions

### FileData

```c#
ModelContent Firebase::AI::ModelContent::FileData(
  string mimeType,
  System.Uri uri
)
```  
Creates a new [ModelContent](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/model-content#struct_firebase_1_1_a_i_1_1_model_content) with the default `user` role, and a [FileDataPart](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/model-content/file-data-part#struct_firebase_1_1_a_i_1_1_model_content_1_1_file_data_part) containing the given mimeType and data.  

### FunctionResponse

```c#
ModelContent Firebase::AI::ModelContent::FunctionResponse(
  string name,
  IDictionary< string, object > response,
  string id
)
```  
Creates a new [ModelContent](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/model-content#struct_firebase_1_1_a_i_1_1_model_content) with the default `user` role, and a [FunctionResponsePart](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/model-content/function-response-part#struct_firebase_1_1_a_i_1_1_model_content_1_1_function_response_part) containing the given name and args.  

### InlineData

```c#
ModelContent Firebase::AI::ModelContent::InlineData(
  string mimeType,
  byte[] data
)
```  
Creates a new [ModelContent](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/model-content#struct_firebase_1_1_a_i_1_1_model_content) with the default `user` role, and an [InlineDataPart](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/model-content/inline-data-part#struct_firebase_1_1_a_i_1_1_model_content_1_1_inline_data_part) containing the given mimeType and data.  

### Text

```c#
ModelContent Firebase::AI::ModelContent::Text(
  string text
)
```  
Creates a new [ModelContent](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/model-content#struct_firebase_1_1_a_i_1_1_model_content) with the default `user` role, and a [TextPart](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/model-content/text-part#struct_firebase_1_1_a_i_1_1_model_content_1_1_text_part) containing the given text.