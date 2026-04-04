# Source: https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/prompt-feedback.md.txt

# Firebase.AI.PromptFeedback Struct Reference

# Firebase.AI.PromptFeedback

A metadata struct containing any feedback the model had on the prompt it was provided.

## Summary

|                                                                                                                                                                                           ### Properties                                                                                                                                                                                            ||
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [BlockReason](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/prompt-feedback#struct_firebase_1_1_a_i_1_1_prompt_feedback_1ac93dd6bac5e884307ba658e871c878fd)        | [BlockReason](https://firebase.google.com/docs/reference/unity/namespace/firebase/a-i#namespace_firebase_1_1_a_i_1a9aa40ab7c18d8663cba0699bb4f67d8a) The reason a prompt was blocked, if it was blocked. |
| [BlockReasonMessage](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/prompt-feedback#struct_firebase_1_1_a_i_1_1_prompt_feedback_1a81b13d80669f30403f01c80321314a35) | `string` A human-readable description of the `BlockReason`.                                                                                                                                              |
| [SafetyRatings](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/prompt-feedback#struct_firebase_1_1_a_i_1_1_prompt_feedback_1a2f0b5f4e90d8280220da0bce3bd30f40)      | `IReadOnlyList< `[SafetyRating](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/safety-rating#struct_firebase_1_1_a_i_1_1_safety_rating)` >` The safety ratings of the prompt.      |

## Properties

### BlockReason

```c#
BlockReason Firebase::AI::PromptFeedback::BlockReason
```  
The reason a prompt was blocked, if it was blocked.  

### BlockReasonMessage

```c#
string Firebase::AI::PromptFeedback::BlockReasonMessage
```  
A human-readable description of the `BlockReason`.  

### SafetyRatings

```c#
IReadOnlyList< SafetyRating > Firebase::AI::PromptFeedback::SafetyRatings
```  
The safety ratings of the prompt.