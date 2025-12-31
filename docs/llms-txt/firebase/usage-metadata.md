# Source: https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/usage-metadata.md.txt

# Firebase.AI.UsageMetadata

Token usage metadata for processing the generate content request.

## Summary

|                                                                                                                                                                                                                                        ### Properties                                                                                                                                                                                                                                         ||
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [CandidatesTokenCount](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/usage-metadata#struct_firebase_1_1_a_i_1_1_usage_metadata_1a1a9311b39b3ab4c4e61bf29c73acc1d7)       | `int` The total number of tokens across the generated response candidates.                                                                                                                                                                                                                   |
| [CandidatesTokensDetails](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/usage-metadata#struct_firebase_1_1_a_i_1_1_usage_metadata_1a08e64629da60525ff5ca21e95e8aaf74)    | `IReadOnlyList< `[ModalityTokenCount](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/modality-token-count#struct_firebase_1_1_a_i_1_1_modality_token_count)` >` The breakdown, by modality, of how many tokens are consumed by the candidates.                         |
| [PromptTokenCount](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/usage-metadata#struct_firebase_1_1_a_i_1_1_usage_metadata_1a70d6d8aa346e3e942727455279126141)           | `int` The number of tokens in the request prompt.                                                                                                                                                                                                                                            |
| [PromptTokensDetails](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/usage-metadata#struct_firebase_1_1_a_i_1_1_usage_metadata_1af0068e8110b0ea2b0a9a56ebf7fa7c98)        | `IReadOnlyList< `[ModalityTokenCount](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/modality-token-count#struct_firebase_1_1_a_i_1_1_modality_token_count)` >` The breakdown, by modality, of how many tokens are consumed by the prompt.                             |
| [ThoughtsTokenCount](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/usage-metadata#struct_firebase_1_1_a_i_1_1_usage_metadata_1ae2c96b232aa5271e53bb88387df52ceb)         | `int` The number of tokens used by the model's internal "thinking" process.                                                                                                                                                                                                                  |
| [ToolUsePromptTokenCount](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/usage-metadata#struct_firebase_1_1_a_i_1_1_usage_metadata_1af020fb9108707375c1ba6397ccb3bd4d)    | `int` The number of tokens used by any enabled tools.                                                                                                                                                                                                                                        |
| [ToolUsePromptTokensDetails](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/usage-metadata#struct_firebase_1_1_a_i_1_1_usage_metadata_1a9a27dcd428d1de35bf21136b6182b0c3) | `IReadOnlyList< `[ModalityTokenCount](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/modality-token-count#struct_firebase_1_1_a_i_1_1_modality_token_count)` >` The breakdown, by modality, of how many tokens were consumed by the tools used to process the request. |
| [TotalTokenCount](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/usage-metadata#struct_firebase_1_1_a_i_1_1_usage_metadata_1a9e6744b8d57eb6e2321d7658b20346c2)            | `int` The total number of tokens in both the request and response.                                                                                                                                                                                                                           |

## Properties

### CandidatesTokenCount

```c#
int Firebase::AI::UsageMetadata::CandidatesTokenCount
```  
The total number of tokens across the generated response candidates.  

### CandidatesTokensDetails

```c#
IReadOnlyList< ModalityTokenCount > Firebase::AI::UsageMetadata::CandidatesTokensDetails
```  
The breakdown, by modality, of how many tokens are consumed by the candidates.  

### PromptTokenCount

```c#
int Firebase::AI::UsageMetadata::PromptTokenCount
```  
The number of tokens in the request prompt.  

### PromptTokensDetails

```c#
IReadOnlyList< ModalityTokenCount > Firebase::AI::UsageMetadata::PromptTokensDetails
```  
The breakdown, by modality, of how many tokens are consumed by the prompt.  

### ThoughtsTokenCount

```c#
int Firebase::AI::UsageMetadata::ThoughtsTokenCount
```  
The number of tokens used by the model's internal "thinking" process.

For models that support thinking (like Gemini 2.5 Pro and Flash), this represents the actual number of tokens consumed for reasoning before the model generated a response. For models that do not support thinking, this value will be `0`.

When thinking is used, this count will be less than or equal to the `thinkingBudget` set in the [ThinkingConfig](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/thinking-config#struct_firebase_1_1_a_i_1_1_thinking_config).  

### ToolUsePromptTokenCount

```c#
int Firebase::AI::UsageMetadata::ToolUsePromptTokenCount
```  
The number of tokens used by any enabled tools.  

### ToolUsePromptTokensDetails

```c#
IReadOnlyList< ModalityTokenCount > Firebase::AI::UsageMetadata::ToolUsePromptTokensDetails
```  
The breakdown, by modality, of how many tokens were consumed by the tools used to process the request.  

### TotalTokenCount

```c#
int Firebase::AI::UsageMetadata::TotalTokenCount
```  
The total number of tokens in both the request and response.