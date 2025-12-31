# Source: https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/model-content/function-response-part.md.txt

# Firebase.AI.ModelContent.FunctionResponsePart Struct Reference

# Firebase.AI.ModelContent.FunctionResponsePart

Result output from a function call.

## Summary

Contains a string representing the `FunctionDeclaration.name` and a structured JSON object containing any output from the function is used as context to the model. This should contain the result of a [FunctionCallPart](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/model-content/function-call-part#struct_firebase_1_1_a_i_1_1_model_content_1_1_function_call_part) made based on model prediction.

### Inheritance

Inherits from: [Firebase.AI.ModelContent.Part](https://firebase.google.com/docs/reference/unity/interface/firebase/a-i/model-content/part)

| ### Constructors and Destructors ||
|---|---|
| [FunctionResponsePart](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/model-content/function-response-part#struct_firebase_1_1_a_i_1_1_model_content_1_1_function_response_part_1a1887b9f5467808e744a51cb9cf75ce83)`(string name, IDictionary< string, object > response, string id)` Constructs a new [FunctionResponsePart](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/model-content/function-response-part#struct_firebase_1_1_a_i_1_1_model_content_1_1_function_response_part). ||

|                                                                                                                                                                                                                               ### Properties                                                                                                                                                                                                                                ||
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Id](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/model-content/function-response-part#struct_firebase_1_1_a_i_1_1_model_content_1_1_function_response_part_1ae3e7dc78829ed36bc62540d9956584e7)        | `string` The id from the [FunctionCallPart](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/model-content/function-call-part#struct_firebase_1_1_a_i_1_1_model_content_1_1_function_call_part) this is in response to. |
| [IsThought](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/model-content/function-response-part#struct_firebase_1_1_a_i_1_1_model_content_1_1_function_response_part_1a86368d0d5d343123d325eda939c58e78) | `bool`                                                                                                                                                                                                                                      |
| [Name](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/model-content/function-response-part#struct_firebase_1_1_a_i_1_1_model_content_1_1_function_response_part_1a1fd324223517f6e76468cf41d5d65ab5)      | `string` The name of the function that was called.                                                                                                                                                                                          |
| [Response](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/model-content/function-response-part#struct_firebase_1_1_a_i_1_1_model_content_1_1_function_response_part_1a6948bd115cbd89cbdb14ed4bc263dc28)  | `IReadOnlyDictionary< string, object >` The function's response or return value.                                                                                                                                                            |

|                                                                                                                         ### Public functions                                                                                                                          ||
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------|
| [ToJson](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/model-content/function-response-part#struct_firebase_1_1_a_i_1_1_model_content_1_1_function_response_part_1a8fb37c3228bd87ad45e7254732515fa4)`()` | `Dictionary< string, object > Part.` |

## Properties

### Id

```c#
string Firebase::AI::ModelContent::FunctionResponsePart::Id
```  
The id from the [FunctionCallPart](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/model-content/function-call-part#struct_firebase_1_1_a_i_1_1_model_content_1_1_function_call_part) this is in response to.  

### IsThought

```c#
bool Firebase::AI::ModelContent::FunctionResponsePart::IsThought
```  

### Name

```c#
string Firebase::AI::ModelContent::FunctionResponsePart::Name
```  
The name of the function that was called.  

### Response

```c#
IReadOnlyDictionary< string, object > Firebase::AI::ModelContent::FunctionResponsePart::Response
```  
The function's response or return value.

## Public functions

### FunctionResponsePart

```c#
 Firebase::AI::ModelContent::FunctionResponsePart::FunctionResponsePart(
  string name,
  IDictionary< string, object > response,
  string id
)
```  
Constructs a new [FunctionResponsePart](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/model-content/function-response-part#struct_firebase_1_1_a_i_1_1_model_content_1_1_function_response_part).

<br />

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           Details                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           ||
|------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `name`     | The name of the function that was called.                                                                                                                                                                                          | | `response` | The function's response.                                                                                                                                                                                                           | | `id`       | The id from the [FunctionCallPart](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/model-content/function-call-part#struct_firebase_1_1_a_i_1_1_model_content_1_1_function_call_part) this is in response to. | |

### ToJson

```c#
Dictionary< string, object > Part. Firebase::AI::ModelContent::FunctionResponsePart::ToJson()
```