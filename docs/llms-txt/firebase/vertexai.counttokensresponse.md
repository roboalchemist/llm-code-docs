# Source: https://firebase.google.com/docs/reference/js/vertexai.counttokensresponse.md.txt

# CountTokensResponse interface

Response from calling [GenerativeModel.countTokens()](https://firebase.google.com/docs/reference/js/vertexai.generativemodel.md#generativemodelcounttokens).

**Signature:**  

    export interface CountTokensResponse 

## Properties

|                                                                      Property                                                                       |                                                                Type                                                                 |                                                                                                                                                                                                                                           Description                                                                                                                                                                                                                                           |
|-----------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [promptTokensDetails](https://firebase.google.com/docs/reference/js/vertexai.counttokensresponse.md#counttokensresponseprompttokensdetails)         | [ModalityTokenCount](https://firebase.google.com/docs/reference/js/vertexai.modalitytokencount.md#modalitytokencount_interface)\[\] | The breakdown, by modality, of how many tokens are consumed by the prompt.                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [totalBillableCharacters](https://firebase.google.com/docs/reference/js/vertexai.counttokensresponse.md#counttokensresponsetotalbillablecharacters) | number                                                                                                                              | The total number of billable characters counted across all instances from the request.This property is only supported when using the Vertex AI Gemini API ([VertexAIBackend](https://firebase.google.com/docs/reference/js/vertexai.vertexaibackend.md#vertexaibackend_class)). When using the Gemini Developer API ([GoogleAIBackend](https://firebase.google.com/docs/reference/js/vertexai.googleaibackend.md#googleaibackend_class)), this property is not supported and will default to 0. |
| [totalTokens](https://firebase.google.com/docs/reference/js/vertexai.counttokensresponse.md#counttokensresponsetotaltokens)                         | number                                                                                                                              | The total number of tokens counted across all instances from the request.                                                                                                                                                                                                                                                                                                                                                                                                                       |

## CountTokensResponse.promptTokensDetails

The breakdown, by modality, of how many tokens are consumed by the prompt.

**Signature:**  

    promptTokensDetails?: ModalityTokenCount[];

## CountTokensResponse.totalBillableCharacters

The total number of billable characters counted across all instances from the request.

This property is only supported when using the Vertex AI Gemini API ([VertexAIBackend](https://firebase.google.com/docs/reference/js/vertexai.vertexaibackend.md#vertexaibackend_class)). When using the Gemini Developer API ([GoogleAIBackend](https://firebase.google.com/docs/reference/js/vertexai.googleaibackend.md#googleaibackend_class)), this property is not supported and will default to 0.

**Signature:**  

    totalBillableCharacters?: number;

## CountTokensResponse.totalTokens

The total number of tokens counted across all instances from the request.

**Signature:**  

    totalTokens: number;