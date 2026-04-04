# Source: https://firebase.google.com/docs/reference/js/ai.promptfeedback.md.txt

# PromptFeedback interface

If the prompt was blocked, this will be populated with `blockReason` and the relevant `safetyRatings`.

**Signature:**  

    export interface PromptFeedback 

## Properties

|                                                         Property                                                          |                                                    Type                                                     |                                                                                                          Description                                                                                                          |
|---------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [blockReason](https://firebase.google.com/docs/reference/js/ai.promptfeedback.md#promptfeedbackblockreason)               | [BlockReason](https://firebase.google.com/docs/reference/js/ai.md#blockreason)                              |                                                                                                                                                                                                                               |
| [blockReasonMessage](https://firebase.google.com/docs/reference/js/ai.promptfeedback.md#promptfeedbackblockreasonmessage) | string                                                                                                      | A human-readable description of the `blockReason`.This property is only supported in the Vertex AI Gemini API ([VertexAIBackend](https://firebase.google.com/docs/reference/js/ai.vertexaibackend.md#vertexaibackend_class)). |
| [safetyRatings](https://firebase.google.com/docs/reference/js/ai.promptfeedback.md#promptfeedbacksafetyratings)           | [SafetyRating](https://firebase.google.com/docs/reference/js/ai.safetyrating.md#safetyrating_interface)\[\] |                                                                                                                                                                                                                               |

## PromptFeedback.blockReason

**Signature:**  

    blockReason?: BlockReason;

## PromptFeedback.blockReasonMessage

A human-readable description of the `blockReason`.

This property is only supported in the Vertex AI Gemini API ([VertexAIBackend](https://firebase.google.com/docs/reference/js/ai.vertexaibackend.md#vertexaibackend_class)).

**Signature:**  

    blockReasonMessage?: string;

## PromptFeedback.safetyRatings

**Signature:**  

    safetyRatings: SafetyRating[];