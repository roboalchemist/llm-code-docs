# Source: https://firebase.google.com/docs/reference/js/vertexai.usagemetadata.md.txt

# UsageMetadata interface

Usage metadata about a [GenerateContentResponse](https://firebase.google.com/docs/reference/js/vertexai.generatecontentresponse.md#generatecontentresponse_interface).

**Signature:**  

    export interface UsageMetadata 

## Properties

|                                                                Property                                                                 |                                                                Type                                                                 | Description |
|-----------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------|-------------|
| [candidatesTokenCount](https://firebase.google.com/docs/reference/js/vertexai.usagemetadata.md#usagemetadatacandidatestokencount)       | number                                                                                                                              |             |
| [candidatesTokensDetails](https://firebase.google.com/docs/reference/js/vertexai.usagemetadata.md#usagemetadatacandidatestokensdetails) | [ModalityTokenCount](https://firebase.google.com/docs/reference/js/vertexai.modalitytokencount.md#modalitytokencount_interface)\[\] |             |
| [promptTokenCount](https://firebase.google.com/docs/reference/js/vertexai.usagemetadata.md#usagemetadataprompttokencount)               | number                                                                                                                              |             |
| [promptTokensDetails](https://firebase.google.com/docs/reference/js/vertexai.usagemetadata.md#usagemetadataprompttokensdetails)         | [ModalityTokenCount](https://firebase.google.com/docs/reference/js/vertexai.modalitytokencount.md#modalitytokencount_interface)\[\] |             |
| [totalTokenCount](https://firebase.google.com/docs/reference/js/vertexai.usagemetadata.md#usagemetadatatotaltokencount)                 | number                                                                                                                              |             |

## UsageMetadata.candidatesTokenCount

**Signature:**  

    candidatesTokenCount: number;

## UsageMetadata.candidatesTokensDetails

**Signature:**  

    candidatesTokensDetails?: ModalityTokenCount[];

## UsageMetadata.promptTokenCount

**Signature:**  

    promptTokenCount: number;

## UsageMetadata.promptTokensDetails

**Signature:**  

    promptTokensDetails?: ModalityTokenCount[];

## UsageMetadata.totalTokenCount

**Signature:**  

    totalTokenCount: number;