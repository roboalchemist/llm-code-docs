# Source: https://firebase.google.com/docs/reference/js/vertexai.safetyrating.md.txt

# SafetyRating interface

A safety rating associated with a [GenerateContentCandidate](https://firebase.google.com/docs/reference/js/vertexai.generatecontentcandidate.md#generatecontentcandidate_interface)

**Signature:**  

    export interface SafetyRating 

## Properties

|                                                        Property                                                         |                                             Type                                             |                                                                                                                                                                                                                        Description                                                                                                                                                                                                                         |
|-------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [blocked](https://firebase.google.com/docs/reference/js/vertexai.safetyrating.md#safetyratingblocked)                   | boolean                                                                                      |                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [category](https://firebase.google.com/docs/reference/js/vertexai.safetyrating.md#safetyratingcategory)                 | [HarmCategory](https://firebase.google.com/docs/reference/js/vertexai.md#harmcategory)       |                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [probability](https://firebase.google.com/docs/reference/js/vertexai.safetyrating.md#safetyratingprobability)           | [HarmProbability](https://firebase.google.com/docs/reference/js/vertexai.md#harmprobability) |                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [probabilityScore](https://firebase.google.com/docs/reference/js/vertexai.safetyrating.md#safetyratingprobabilityscore) | number                                                                                       | The probability score of the harm category.This property is only supported when using the Vertex AI Gemini API ([VertexAIBackend](https://firebase.google.com/docs/reference/js/vertexai.vertexaibackend.md#vertexaibackend_class)). When using the Gemini Developer API ([GoogleAIBackend](https://firebase.google.com/docs/reference/js/vertexai.googleaibackend.md#googleaibackend_class)), this property is not supported and will default to 0.       |
| [severity](https://firebase.google.com/docs/reference/js/vertexai.safetyrating.md#safetyratingseverity)                 | [HarmSeverity](https://firebase.google.com/docs/reference/js/vertexai.md#harmseverity)       | The harm severity level.This property is only supported when using the Vertex AI Gemini API ([VertexAIBackend](https://firebase.google.com/docs/reference/js/vertexai.vertexaibackend.md#vertexaibackend_class)). When using the Gemini Developer API ([GoogleAIBackend](https://firebase.google.com/docs/reference/js/vertexai.googleaibackend.md#googleaibackend_class)), this property is not supported and will default to `HarmSeverity.UNSUPPORTED`. |
| [severityScore](https://firebase.google.com/docs/reference/js/vertexai.safetyrating.md#safetyratingseverityscore)       | number                                                                                       | The severity score of the harm category.This property is only supported when using the Vertex AI Gemini API ([VertexAIBackend](https://firebase.google.com/docs/reference/js/vertexai.vertexaibackend.md#vertexaibackend_class)). When using the Gemini Developer API ([GoogleAIBackend](https://firebase.google.com/docs/reference/js/vertexai.googleaibackend.md#googleaibackend_class)), this property is not supported and will default to 0.          |

## SafetyRating.blocked

**Signature:**  

    blocked: boolean;

## SafetyRating.category

**Signature:**  

    category: HarmCategory;

## SafetyRating.probability

**Signature:**  

    probability: HarmProbability;

## SafetyRating.probabilityScore

The probability score of the harm category.

This property is only supported when using the Vertex AI Gemini API ([VertexAIBackend](https://firebase.google.com/docs/reference/js/vertexai.vertexaibackend.md#vertexaibackend_class)). When using the Gemini Developer API ([GoogleAIBackend](https://firebase.google.com/docs/reference/js/vertexai.googleaibackend.md#googleaibackend_class)), this property is not supported and will default to 0.

**Signature:**  

    probabilityScore: number;

## SafetyRating.severity

The harm severity level.

This property is only supported when using the Vertex AI Gemini API ([VertexAIBackend](https://firebase.google.com/docs/reference/js/vertexai.vertexaibackend.md#vertexaibackend_class)). When using the Gemini Developer API ([GoogleAIBackend](https://firebase.google.com/docs/reference/js/vertexai.googleaibackend.md#googleaibackend_class)), this property is not supported and will default to `HarmSeverity.UNSUPPORTED`.

**Signature:**  

    severity: HarmSeverity;

## SafetyRating.severityScore

The severity score of the harm category.

This property is only supported when using the Vertex AI Gemini API ([VertexAIBackend](https://firebase.google.com/docs/reference/js/vertexai.vertexaibackend.md#vertexaibackend_class)). When using the Gemini Developer API ([GoogleAIBackend](https://firebase.google.com/docs/reference/js/vertexai.googleaibackend.md#googleaibackend_class)), this property is not supported and will default to 0.

**Signature:**  

    severityScore: number;