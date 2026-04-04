# Source: https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/generate-content-response.md.txt

# Firebase.AI.GenerateContentResponse Struct Reference

# Firebase.AI.GenerateContentResponse

The model's response to a generate content request.

## Summary

|                                                                                                                                                                                                                                                           ### Properties                                                                                                                                                                                                                                                            ||
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Candidates](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/generate-content-response#struct_firebase_1_1_a_i_1_1_generate_content_response_1acbb6ea188246f46459f9538297133697)     | `IReadOnlyList< `[Candidate](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/candidate#struct_firebase_1_1_a_i_1_1_candidate)` >` A list of candidate response content, ordered from best to worst.                                                                                                 |
| [FunctionCalls](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/generate-content-response#struct_firebase_1_1_a_i_1_1_generate_content_response_1a49535ea2092d86f0000b2b5ccf3ad9d6)  | `IReadOnlyList< `[ModelContent.FunctionCallPart](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/model-content/function-call-part#struct_firebase_1_1_a_i_1_1_model_content_1_1_function_call_part)` >` Returns function calls found in any `Part`s of the first candidate of the response, if any. |
| [PromptFeedback](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/generate-content-response#struct_firebase_1_1_a_i_1_1_generate_content_response_1a2af16c02c8dcdf061cde4edb9492f72e) | [PromptFeedback](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/prompt-feedback#struct_firebase_1_1_a_i_1_1_prompt_feedback) A value containing the safety ratings for the response, or, if the request was blocked, a reason for blocking the request.                                            |
| [Text](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/generate-content-response#struct_firebase_1_1_a_i_1_1_generate_content_response_1ad9e722a9dc514972d10c29f58fbc29ff)           | `string` The response's content as text, if it exists.                                                                                                                                                                                                                                                                   |
| [ThoughtSummary](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/generate-content-response#struct_firebase_1_1_a_i_1_1_generate_content_response_1a9c3525e17fb8778e1907e2d931892e2a) | `string` A summary of the model's thinking process, if available.                                                                                                                                                                                                                                                        |
| [UsageMetadata](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/generate-content-response#struct_firebase_1_1_a_i_1_1_generate_content_response_1a281dac07869b1a8df233df004641877a)  | [UsageMetadata](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/usage-metadata#struct_firebase_1_1_a_i_1_1_usage_metadata) Token usage metadata for processing the generate content request.                                                                                                        |

## Properties

### Candidates

```c#
IReadOnlyList< Candidate > Firebase::AI::GenerateContentResponse::Candidates
```  
A list of candidate response content, ordered from best to worst.  

### FunctionCalls

```c#
IReadOnlyList< ModelContent.FunctionCallPart > Firebase::AI::GenerateContentResponse::FunctionCalls
```  
Returns function calls found in any `Part`s of the first candidate of the response, if any.  

### PromptFeedback

```c#
PromptFeedback Firebase::AI::GenerateContentResponse::PromptFeedback
```  
A value containing the safety ratings for the response, or, if the request was blocked, a reason for blocking the request.  

### Text

```c#
string Firebase::AI::GenerateContentResponse::Text
```  
The response's content as text, if it exists.  

### ThoughtSummary

```c#
string Firebase::AI::GenerateContentResponse::ThoughtSummary
```  
A summary of the model's thinking process, if available.

Note that Thought Summaries are only available when `IncludeThoughts` is enabled in the [ThinkingConfig](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/thinking-config#struct_firebase_1_1_a_i_1_1_thinking_config). For more information, see the [Thinking](https://firebase.google.com/docs/ai-logic/thinking) documentation.  

### UsageMetadata

```c#
UsageMetadata Firebase::AI::GenerateContentResponse::UsageMetadata
```  
Token usage metadata for processing the generate content request.