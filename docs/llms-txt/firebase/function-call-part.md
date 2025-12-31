# Source: https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/model-content/function-call-part.md.txt

# Firebase.AI.ModelContent.FunctionCallPart Struct Reference

# Firebase.AI.ModelContent.FunctionCallPart

A predicted function call returned from the model.

## Summary

### Inheritance

Inherits from: [Firebase.AI.ModelContent.Part](https://firebase.google.com/docs/reference/unity/interface/firebase/a-i/model-content/part)

|                                                                                                                                                                                                                                      ### Properties                                                                                                                                                                                                                                       ||
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Args](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/model-content/function-call-part#struct_firebase_1_1_a_i_1_1_model_content_1_1_function_call_part_1a9a81466f7b54875aea5bf14efe110d70)      | `IReadOnlyDictionary< string, object >` The function parameters and values, matching the registered schema.                                                                                                                                                       |
| [Id](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/model-content/function-call-part#struct_firebase_1_1_a_i_1_1_model_content_1_1_function_call_part_1a49d2462c27ddbfa89521f76b97e98dc3)        | `string` An identifier that should be passed along in the [FunctionResponsePart](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/model-content/function-response-part#struct_firebase_1_1_a_i_1_1_model_content_1_1_function_response_part). |
| [IsThought](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/model-content/function-call-part#struct_firebase_1_1_a_i_1_1_model_content_1_1_function_call_part_1ac787adde3d333a1151ba44cb8787e963) | `bool`                                                                                                                                                                                                                                                            |
| [Name](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/model-content/function-call-part#struct_firebase_1_1_a_i_1_1_model_content_1_1_function_call_part_1a0192cf50403b7314c165e75d4c17a6d1)      | `string` The name of the registered function to call.                                                                                                                                                                                                             |

|                                                                                                                     ### Public functions                                                                                                                      ||
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------|
| [ToJson](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/model-content/function-call-part#struct_firebase_1_1_a_i_1_1_model_content_1_1_function_call_part_1aff956e3102e3f041cb41deaffed064be)`()` | `Dictionary< string, object > Part.` |

## Properties

### Args

```c#
IReadOnlyDictionary< string, object > Firebase::AI::ModelContent::FunctionCallPart::Args
```  
The function parameters and values, matching the registered schema.  

### Id

```c#
string Firebase::AI::ModelContent::FunctionCallPart::Id
```  
An identifier that should be passed along in the [FunctionResponsePart](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/model-content/function-response-part#struct_firebase_1_1_a_i_1_1_model_content_1_1_function_response_part).  

### IsThought

```c#
bool Firebase::AI::ModelContent::FunctionCallPart::IsThought
```  

### Name

```c#
string Firebase::AI::ModelContent::FunctionCallPart::Name
```  
The name of the registered function to call.

## Public functions

### ToJson

```c#
Dictionary< string, object > Part. Firebase::AI::ModelContent::FunctionCallPart::ToJson()
```