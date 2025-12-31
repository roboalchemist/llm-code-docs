# Source: https://firebase.google.com/docs/reference/unity/interface/firebase/a-i/model-content/part.md.txt

# Firebase.AI.ModelContent.Part

A discrete piece of data in a media format interpretable by an [AI](https://firebase.google.com/docs/reference/unity/namespace/firebase/a-i#namespace_firebase_1_1_a_i) model.

## Summary

Within a single value of [Part](https://firebase.google.com/docs/reference/unity/interface/firebase/a-i/model-content/part#interface_firebase_1_1_a_i_1_1_model_content_1_1_part), different data types may not mix.

### Inheritance

Direct Known Subclasses:[Firebase.AI.ModelContent.CodeExecutionResultPart](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/model-content/code-execution-result-part), [Firebase.AI.ModelContent.ExecutableCodePart](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/model-content/executable-code-part), [Firebase.AI.ModelContent.FileDataPart](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/model-content/file-data-part), [Firebase.AI.ModelContent.FunctionCallPart](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/model-content/function-call-part), [Firebase.AI.ModelContent.FunctionResponsePart](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/model-content/function-response-part), [Firebase.AI.ModelContent.InlineDataPart](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/model-content/inline-data-part), [Firebase.AI.ModelContent.TextPart](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/model-content/text-part)

|                                                                                                                                                                                                                 ### Properties                                                                                                                                                                                                                  ||
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [IsThought](https://firebase.google.com/docs/reference/unity/interface/firebase/a-i/model-content/part#interface_firebase_1_1_a_i_1_1_model_content_1_1_part_1ae1d8730a875f65672468e0463938e9ca) | `bool` Indicates whether this [Part](https://firebase.google.com/docs/reference/unity/interface/firebase/a-i/model-content/part#interface_firebase_1_1_a_i_1_1_model_content_1_1_part) is a summary of the model's internal thinking process. |

## Properties

### IsThought

```c#
bool IsThought
```  
Indicates whether this [Part](https://firebase.google.com/docs/reference/unity/interface/firebase/a-i/model-content/part#interface_firebase_1_1_a_i_1_1_model_content_1_1_part) is a summary of the model's internal thinking process.

When `IncludeThoughts` is set to `true` in [ThinkingConfig](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/thinking-config#struct_firebase_1_1_a_i_1_1_thinking_config), the model may return one or more "thought" parts that provide insight into how it reasoned through the prompt to arrive at the final answer. These parts will have `IsThought` set to `true`.