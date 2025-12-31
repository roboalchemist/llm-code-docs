# Source: https://firebase.google.com/docs/reference/js/ai.enhancedgeneratecontentresponse.md.txt

Response object wrapped with helper methods.

**Signature:**  

    export interface EnhancedGenerateContentResponse extends GenerateContentResponse 

**Extends:** [GenerateContentResponse](https://firebase.google.com/docs/reference/js/ai.generatecontentresponse.md#generatecontentresponse_interface)

## Properties

|                                                                       Property                                                                        |                                                                 Type                                                                 |                                                                                                                                                             Description                                                                                                                                                             |
|-------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [functionCalls](https://firebase.google.com/docs/reference/js/ai.enhancedgeneratecontentresponse.md#enhancedgeneratecontentresponsefunctioncalls)     | () =\>[FunctionCall](https://firebase.google.com/docs/reference/js/ai.functioncall.md#functioncall_interface)\[\] \| undefined       | Aggregates and returns every[FunctionCall](https://firebase.google.com/docs/reference/js/ai.functioncall.md#functioncall_interface)from the first candidate of[GenerateContentResponse](https://firebase.google.com/docs/reference/js/ai.generatecontentresponse.md#generatecontentresponse_interface).                             |
| [inferenceSource](https://firebase.google.com/docs/reference/js/ai.enhancedgeneratecontentresponse.md#enhancedgeneratecontentresponseinferencesource) | [InferenceSource](https://firebase.google.com/docs/reference/js/ai.md#inferencesource)                                               | ***(Public Preview)***Indicates whether inference happened on-device or in-cloud.                                                                                                                                                                                                                                                   |
| [inlineDataParts](https://firebase.google.com/docs/reference/js/ai.enhancedgeneratecontentresponse.md#enhancedgeneratecontentresponseinlinedataparts) | () =\>[InlineDataPart](https://firebase.google.com/docs/reference/js/ai.inlinedatapart.md#inlinedatapart_interface)\[\] \| undefined | Aggregates and returns every[InlineDataPart](https://firebase.google.com/docs/reference/js/ai.inlinedatapart.md#inlinedatapart_interface)from the first candidate of[GenerateContentResponse](https://firebase.google.com/docs/reference/js/ai.generatecontentresponse.md#generatecontentresponse_interface).                       |
| [text](https://firebase.google.com/docs/reference/js/ai.enhancedgeneratecontentresponse.md#enhancedgeneratecontentresponsetext)                       | () =\> string                                                                                                                        | Returns the text string from the response, if available. Throws if the prompt or candidate was blocked.                                                                                                                                                                                                                             |
| [thoughtSummary](https://firebase.google.com/docs/reference/js/ai.enhancedgeneratecontentresponse.md#enhancedgeneratecontentresponsethoughtsummary)   | () =\> string \| undefined                                                                                                           | Aggregates and returns every[TextPart](https://firebase.google.com/docs/reference/js/ai.textpart.md#textpart_interface)with their`thought`property set to`true`from the first candidate of[GenerateContentResponse](https://firebase.google.com/docs/reference/js/ai.generatecontentresponse.md#generatecontentresponse_interface). |

## EnhancedGenerateContentResponse.functionCalls

Aggregates and returns every[FunctionCall](https://firebase.google.com/docs/reference/js/ai.functioncall.md#functioncall_interface)from the first candidate of[GenerateContentResponse](https://firebase.google.com/docs/reference/js/ai.generatecontentresponse.md#generatecontentresponse_interface).

**Signature:**  

    functionCalls: () => FunctionCall[] | undefined;

## EnhancedGenerateContentResponse.inferenceSource

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Indicates whether inference happened on-device or in-cloud.

**Signature:**  

    inferenceSource?: InferenceSource;

## EnhancedGenerateContentResponse.inlineDataParts

Aggregates and returns every[InlineDataPart](https://firebase.google.com/docs/reference/js/ai.inlinedatapart.md#inlinedatapart_interface)from the first candidate of[GenerateContentResponse](https://firebase.google.com/docs/reference/js/ai.generatecontentresponse.md#generatecontentresponse_interface).

**Signature:**  

    inlineDataParts: () => InlineDataPart[] | undefined;

## EnhancedGenerateContentResponse.text

Returns the text string from the response, if available. Throws if the prompt or candidate was blocked.

**Signature:**  

    text: () => string;

## EnhancedGenerateContentResponse.thoughtSummary

Aggregates and returns every[TextPart](https://firebase.google.com/docs/reference/js/ai.textpart.md#textpart_interface)with their`thought`property set to`true`from the first candidate of[GenerateContentResponse](https://firebase.google.com/docs/reference/js/ai.generatecontentresponse.md#generatecontentresponse_interface).

Thought summaries provide a brief overview of the model's internal thinking process, offering insight into how it arrived at the final answer. This can be useful for debugging, understanding the model's reasoning, and verifying its accuracy.

Thoughts will only be included if[ThinkingConfig.includeThoughts](https://firebase.google.com/docs/reference/js/ai.thinkingconfig.md#thinkingconfigincludethoughts)is set to`true`.

**Signature:**  

    thoughtSummary: () => string | undefined;