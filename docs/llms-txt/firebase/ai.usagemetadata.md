# Source: https://firebase.google.com/docs/reference/js/ai.usagemetadata.md.txt

Usage metadata about a [GenerateContentResponse](https://firebase.google.com/docs/reference/js/ai.generatecontentresponse.md#generatecontentresponse_interface).

**Signature:**  

    export interface UsageMetadata 

## Properties

|                                                                Property                                                                 |                                                             Type                                                              |                              Description                              |
|-----------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------|
| [candidatesTokenCount](https://firebase.google.com/docs/reference/js/ai.usagemetadata.md#usagemetadatacandidatestokencount)             | number                                                                                                                        |                                                                       |
| [candidatesTokensDetails](https://firebase.google.com/docs/reference/js/ai.usagemetadata.md#usagemetadatacandidatestokensdetails)       | [ModalityTokenCount](https://firebase.google.com/docs/reference/js/ai.modalitytokencount.md#modalitytokencount_interface)\[\] |                                                                       |
| [promptTokenCount](https://firebase.google.com/docs/reference/js/ai.usagemetadata.md#usagemetadataprompttokencount)                     | number                                                                                                                        |                                                                       |
| [promptTokensDetails](https://firebase.google.com/docs/reference/js/ai.usagemetadata.md#usagemetadataprompttokensdetails)               | [ModalityTokenCount](https://firebase.google.com/docs/reference/js/ai.modalitytokencount.md#modalitytokencount_interface)\[\] |                                                                       |
| [thoughtsTokenCount](https://firebase.google.com/docs/reference/js/ai.usagemetadata.md#usagemetadatathoughtstokencount)                 | number                                                                                                                        | The number of tokens used by the model's internal "thinking" process. |
| [toolUsePromptTokenCount](https://firebase.google.com/docs/reference/js/ai.usagemetadata.md#usagemetadatatooluseprompttokencount)       | number                                                                                                                        | The number of tokens used by tools.                                   |
| [toolUsePromptTokensDetails](https://firebase.google.com/docs/reference/js/ai.usagemetadata.md#usagemetadatatooluseprompttokensdetails) | [ModalityTokenCount](https://firebase.google.com/docs/reference/js/ai.modalitytokencount.md#modalitytokencount_interface)\[\] | A list of tokens used by tools, broken down by modality.              |
| [totalTokenCount](https://firebase.google.com/docs/reference/js/ai.usagemetadata.md#usagemetadatatotaltokencount)                       | number                                                                                                                        |                                                                       |

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

## UsageMetadata.thoughtsTokenCount

The number of tokens used by the model's internal "thinking" process.

**Signature:**  

    thoughtsTokenCount?: number;

## UsageMetadata.toolUsePromptTokenCount

The number of tokens used by tools.

**Signature:**  

    toolUsePromptTokenCount?: number;

## UsageMetadata.toolUsePromptTokensDetails

A list of tokens used by tools, broken down by modality.

**Signature:**  

    toolUsePromptTokensDetails?: ModalityTokenCount[];

## UsageMetadata.totalTokenCount

**Signature:**  

    totalTokenCount: number;