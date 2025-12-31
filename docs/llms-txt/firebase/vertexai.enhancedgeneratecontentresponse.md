# Source: https://firebase.google.com/docs/reference/js/vertexai.enhancedgeneratecontentresponse.md.txt

# EnhancedGenerateContentResponse interface

Response object wrapped with helper methods.

**Signature:**  

    export interface EnhancedGenerateContentResponse extends GenerateContentResponse 

**Extends:** [GenerateContentResponse](https://firebase.google.com/docs/reference/js/vertexai.generatecontentresponse.md#generatecontentresponse_interface)

## Properties

|                                                                          Property                                                                           |                                                                    Type                                                                     |                                                                                                                                                        Description                                                                                                                                                         |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [functionCalls](https://firebase.google.com/docs/reference/js/vertexai.enhancedgeneratecontentresponse.md#enhancedgeneratecontentresponsefunctioncalls)     | () =\> [FunctionCall](https://firebase.google.com/docs/reference/js/vertexai.functioncall.md#functioncall_interface)\[\] \| undefined       |                                                                                                                                                                                                                                                                                                                            |
| [inlineDataParts](https://firebase.google.com/docs/reference/js/vertexai.enhancedgeneratecontentresponse.md#enhancedgeneratecontentresponseinlinedataparts) | () =\> [InlineDataPart](https://firebase.google.com/docs/reference/js/vertexai.inlinedatapart.md#inlinedatapart_interface)\[\] \| undefined | Aggregates and returns all [InlineDataPart](https://firebase.google.com/docs/reference/js/vertexai.inlinedatapart.md#inlinedatapart_interface)s from the [GenerateContentResponse](https://firebase.google.com/docs/reference/js/vertexai.generatecontentresponse.md#generatecontentresponse_interface)'s first candidate. |
| [text](https://firebase.google.com/docs/reference/js/vertexai.enhancedgeneratecontentresponse.md#enhancedgeneratecontentresponsetext)                       | () =\> string                                                                                                                               | Returns the text string from the response, if available. Throws if the prompt or candidate was blocked.                                                                                                                                                                                                                    |

## EnhancedGenerateContentResponse.functionCalls

**Signature:**  

    functionCalls: () => FunctionCall[] | undefined;

## EnhancedGenerateContentResponse.inlineDataParts

Aggregates and returns all [InlineDataPart](https://firebase.google.com/docs/reference/js/vertexai.inlinedatapart.md#inlinedatapart_interface)s from the [GenerateContentResponse](https://firebase.google.com/docs/reference/js/vertexai.generatecontentresponse.md#generatecontentresponse_interface)'s first candidate.

**Signature:**  

    inlineDataParts: () => InlineDataPart[] | undefined;

## EnhancedGenerateContentResponse.text

Returns the text string from the response, if available. Throws if the prompt or candidate was blocked.

**Signature:**  

    text: () => string;