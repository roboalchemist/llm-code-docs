# Source: https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/candidate.md.txt

# Firebase.AI.Candidate

A struct representing a possible reply to a content generation prompt.

## Summary

Each content generation prompt may produce multiple candidate responses.

|                                                                                                                                                                                                                           ### Properties                                                                                                                                                                                                                            ||
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [CitationMetadata](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/candidate#struct_firebase_1_1_a_i_1_1_candidate_1a46a5266aa61b973482cfef8bfd233069)   | [CitationMetadata](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/citation-metadata#struct_firebase_1_1_a_i_1_1_citation_metadata) Cited works in the model's response content, if it exists.                                                                  |
| [Content](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/candidate#struct_firebase_1_1_a_i_1_1_candidate_1ab6fc4a3c799f977cd6259b27856e4e22)            | [ModelContent](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/model-content#struct_firebase_1_1_a_i_1_1_model_content) The response's content.                                                                                                                 |
| [FinishReason](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/candidate#struct_firebase_1_1_a_i_1_1_candidate_1ab0438648e017e9ae0a7e02ec9c3b52bd)       | [FinishReason](https://firebase.google.com/docs/reference/unity/namespace/firebase/a-i#namespace_firebase_1_1_a_i_1ab636544c199b4ff23cce90300815c455) The reason the model stopped generating content, if it exists; for example, if the model generated a predefined stop sequence. |
| [GroundingMetadata](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/candidate#struct_firebase_1_1_a_i_1_1_candidate_1adb692b2d9e18559ac3af2da27cc3b078)  | [GroundingMetadata](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/grounding-metadata#struct_firebase_1_1_a_i_1_1_grounding_metadata) Grounding metadata for the response, if any.                                                                             |
| [SafetyRatings](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/candidate#struct_firebase_1_1_a_i_1_1_candidate_1a967e1a2467ce46436abe9279891ee1af)      | `IReadOnlyList< `[SafetyRating](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/safety-rating#struct_firebase_1_1_a_i_1_1_safety_rating)` >` The safety rating of the response content.                                                                         |
| [UrlContextMetadata](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/candidate#struct_firebase_1_1_a_i_1_1_candidate_1a6bd9df2f24278ed5627cb4453eebb533) | [UrlContextMetadata](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/url-context-metadata#struct_firebase_1_1_a_i_1_1_url_context_metadata) Metadata related to the `URLContext` tool.                                                                          |

## Properties

### CitationMetadata

```c#
CitationMetadata Firebase::AI::Candidate::CitationMetadata
```  
Cited works in the model's response content, if it exists.  

### Content

```c#
ModelContent Firebase::AI::Candidate::Content
```  
The response's content.  

### FinishReason

```c#
FinishReason Firebase::AI::Candidate::FinishReason
```  
The reason the model stopped generating content, if it exists; for example, if the model generated a predefined stop sequence.  

### GroundingMetadata

```c#
GroundingMetadata Firebase::AI::Candidate::GroundingMetadata
```  
Grounding metadata for the response, if any.  

### SafetyRatings

```c#
IReadOnlyList< SafetyRating > Firebase::AI::Candidate::SafetyRatings
```  
The safety rating of the response content.  

### UrlContextMetadata

```c#
UrlContextMetadata Firebase::AI::Candidate::UrlContextMetadata
```  
Metadata related to the `URLContext` tool.