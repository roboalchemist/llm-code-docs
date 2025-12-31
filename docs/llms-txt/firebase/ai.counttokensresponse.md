# Source: https://firebase.google.com/docs/reference/js/ai.counttokensresponse.md.txt

# CountTokensResponse interface

Response from calling [GenerativeModel.countTokens()](https://firebase.google.com/docs/reference/js/ai.generativemodel.md#generativemodelcounttokens).

**Signature:**  

    export interface CountTokensResponse 

## Properties

|                                                                   Property                                                                    |                                                             Type                                                              |                                Description                                 |
|-----------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------|
| [promptTokensDetails](https://firebase.google.com/docs/reference/js/ai.counttokensresponse.md#counttokensresponseprompttokensdetails)         | [ModalityTokenCount](https://firebase.google.com/docs/reference/js/ai.modalitytokencount.md#modalitytokencount_interface)\[\] | The breakdown, by modality, of how many tokens are consumed by the prompt. |
| [totalBillableCharacters](https://firebase.google.com/docs/reference/js/ai.counttokensresponse.md#counttokensresponsetotalbillablecharacters) | number                                                                                                                        |                                                                            |
| [totalTokens](https://firebase.google.com/docs/reference/js/ai.counttokensresponse.md#counttokensresponsetotaltokens)                         | number                                                                                                                        | The total number of tokens counted across all instances from the request.  |

## CountTokensResponse.promptTokensDetails

The breakdown, by modality, of how many tokens are consumed by the prompt.

**Signature:**  

    promptTokensDetails?: ModalityTokenCount[];

## CountTokensResponse.totalBillableCharacters

> | **Warning:** This API is now obsolete.
>
> Use `totalTokens` instead. This property is undefined when using models greater than `gemini-1.5-*`.
>
> The total number of billable characters counted across all instances from the request.

**Signature:**  

    totalBillableCharacters?: number;

## CountTokensResponse.totalTokens

The total number of tokens counted across all instances from the request.

**Signature:**  

    totalTokens: number;