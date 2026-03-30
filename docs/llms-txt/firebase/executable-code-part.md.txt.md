# Source: https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/model-content/executable-code-part.md.txt

# Firebase.AI.ModelContent.ExecutableCodePart Struct Reference

# Firebase.AI.ModelContent.ExecutableCodePart

A part containing code that was executed by the model.

## Summary

### Inheritance

Inherits from: [Firebase.AI.ModelContent.Part](https://firebase.google.com/docs/reference/unity/interface/firebase/a-i/model-content/part)

| ### Public types ||
|---|---|
| `https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/model-content/executable-code-part#struct_firebase_1_1_a_i_1_1_model_content_1_1_executable_code_part_1ae9a3c6cb485b9fe7a3bd4a38d0f24e66` | enum |

| ### Properties ||
|---|---|
| `https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/model-content/executable-code-part#struct_firebase_1_1_a_i_1_1_model_content_1_1_executable_code_part_1abfde4b56a3127764a2127028950f8b2b` | `string` The code that was executed. |
| `https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/model-content/executable-code-part#struct_firebase_1_1_a_i_1_1_model_content_1_1_executable_code_part_1a6b67ac0d234fb5d53ecd19a3692fb103` | `bool` |
| `https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/model-content/executable-code-part#struct_firebase_1_1_a_i_1_1_model_content_1_1_executable_code_part_1a7ffd5ba2f2949a8b2b93881d45c8378a` | `CodeLanguage` The language |

| ### Public functions ||
|---|---|
| `https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/model-content/executable-code-part#struct_firebase_1_1_a_i_1_1_model_content_1_1_executable_code_part_1a6e7aac81be9e245bd8cae4e4475b90eb()` | `Dictionary< string, object > Part.` |

## Public types

### CodeLanguage

```c#
 Firebase::AI::ModelContent::ExecutableCodePart::CodeLanguage
```

## Properties

### Code

```c#
string Firebase::AI::ModelContent::ExecutableCodePart::Code
```
The code that was executed.

### IsThought

```c#
bool Firebase::AI::ModelContent::ExecutableCodePart::IsThought
```

### Language

```c#
CodeLanguage Firebase::AI::ModelContent::ExecutableCodePart::Language
```
The language

## Public functions

### ToJson

```c#
Dictionary< string, object > Part. Firebase::AI::ModelContent::ExecutableCodePart::ToJson()
```