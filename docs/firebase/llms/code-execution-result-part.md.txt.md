# Source: https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/model-content/code-execution-result-part.md.txt

# Firebase.AI.ModelContent.CodeExecutionResultPart Struct Reference

# Firebase.AI.ModelContent.CodeExecutionResultPart

A part containing the result of executing code.

## Summary

### Inheritance

Inherits from: [Firebase.AI.ModelContent.Part](https://firebase.google.com/docs/reference/unity/interface/firebase/a-i/model-content/part)

| ### Public types ||
|---|---|
| `https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/model-content/code-execution-result-part#struct_firebase_1_1_a_i_1_1_model_content_1_1_code_execution_result_part_1a9cf72eb2ecd6fa871744a433d70f2f1b{ https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/model-content/code-execution-result-part#struct_firebase_1_1_a_i_1_1_model_content_1_1_code_execution_result_part_1a9cf72eb2ecd6fa871744a433d70f2f1baa60852f204ed8028c1c58808b746d115, https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/model-content/code-execution-result-part#struct_firebase_1_1_a_i_1_1_model_content_1_1_code_execution_result_part_1a9cf72eb2ecd6fa871744a433d70f2f1bad7c8c85bf79bbe1b7188497c32c3b0ca, https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/model-content/code-execution-result-part#struct_firebase_1_1_a_i_1_1_model_content_1_1_code_execution_result_part_1a9cf72eb2ecd6fa871744a433d70f2f1babfe21264466e240bec5a8f8e6c4e2487 }` | enumThe outcome of a code execution. |

| ### Properties ||
|---|---|
| `https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/model-content/code-execution-result-part#struct_firebase_1_1_a_i_1_1_model_content_1_1_code_execution_result_part_1a2bd39de7d2786a0d4955ca89fad55063` | `bool` |
| `https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/model-content/code-execution-result-part#struct_firebase_1_1_a_i_1_1_model_content_1_1_code_execution_result_part_1a96f745313cf902d6e22d70ba40980fac` | `https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/model-content/code-execution-result-part#struct_firebase_1_1_a_i_1_1_model_content_1_1_code_execution_result_part_1a9cf72eb2ecd6fa871744a433d70f2f1b` The outcome of the code execution. |
| `https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/model-content/code-execution-result-part#struct_firebase_1_1_a_i_1_1_model_content_1_1_code_execution_result_part_1aff5fc653a558debe1b89e43fdc77bc33` | `string` The output of the code execution. |

| ### Public functions ||
|---|---|
| `https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/model-content/code-execution-result-part#struct_firebase_1_1_a_i_1_1_model_content_1_1_code_execution_result_part_1a2abd3adf3eae206b12060241df35f4bb()` | `Dictionary< string, object > Part.` |

## Public types

### ExecutionOutcome

```c#
 Firebase::AI::ModelContent::CodeExecutionResultPart::ExecutionOutcome
```
The outcome of a code execution.

| Properties ||
|---|---|
| `DeadlineExceeded` | The code took too long to execute. |
| `Failed` | The code failed to execute. |
| `Ok` | The code executed without errors. |

## Properties

### IsThought

```c#
bool Firebase::AI::ModelContent::CodeExecutionResultPart::IsThought
```

### Outcome

```c#
ExecutionOutcome Firebase::AI::ModelContent::CodeExecutionResultPart::Outcome
```
The outcome of the code execution.

### Output

```c#
string Firebase::AI::ModelContent::CodeExecutionResultPart::Output
```
The output of the code execution.

## Public functions

### ToJson

```c#
Dictionary< string, object > Part. Firebase::AI::ModelContent::CodeExecutionResultPart::ToJson()
```