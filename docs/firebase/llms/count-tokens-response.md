# Source: https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/count-tokens-response.md.txt

# Firebase.AI.CountTokensResponse Struct Reference

# Firebase.AI.CountTokensResponse

The model's response to a count tokens request.

## Summary

|                                                                                                                                                                                                                                           ### Properties                                                                                                                                                                                                                                            ||
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [PromptTokensDetails](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/count-tokens-response#struct_firebase_1_1_a_i_1_1_count_tokens_response_1a60965b6a6cf4790205e1a425786eed74)     | `IReadOnlyList< `[ModalityTokenCount](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/modality-token-count#struct_firebase_1_1_a_i_1_1_modality_token_count)` >` The breakdown, by modality, of how many tokens are consumed by the prompt.                        |
| [TotalBillableCharacters](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/count-tokens-response#struct_firebase_1_1_a_i_1_1_count_tokens_response_1a6eb175efeeae649f94f3d6e83e497bec) | `int` **[Deprecated.](https://firebase.google.com/docs/reference/unity/deprecated/deprecated)** Use TotalTokens instead; Gemini 2.0 series models and newer are always billed by token count. The total number of billable characters in the text input given to the model as a prompt. |
| [TotalTokens](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/count-tokens-response#struct_firebase_1_1_a_i_1_1_count_tokens_response_1a4cd653f744e15be9e5ea40748e3c2c39)             | `int` The total number of tokens in the input given to the model as a prompt.                                                                                                                                                                                                           |

## Properties

### PromptTokensDetails

```c#
IReadOnlyList< ModalityTokenCount > Firebase::AI::CountTokensResponse::PromptTokensDetails
```  
The breakdown, by modality, of how many tokens are consumed by the prompt.  

### TotalBillableCharacters

```c#
int Firebase::AI::CountTokensResponse::TotalBillableCharacters
```  
The total number of billable characters in the text input given to the model as a prompt.

Important: This does not include billable image, video or other non-text input. See [Firebase AI pricing](https://firebase.google.com/docs/vertex-ai/pricing) for details.

Use TotalTokens instead; Gemini 2.0 series models and newer are always billed by token count.

**[Deprecated.](https://firebase.google.com/docs/reference/unity/deprecated/deprecated)**Use TotalTokens instead; Gemini 2.0 series models and newer are always billed by token count.  

### TotalTokens

```c#
int Firebase::AI::CountTokensResponse::TotalTokens
```  
The total number of tokens in the input given to the model as a prompt.