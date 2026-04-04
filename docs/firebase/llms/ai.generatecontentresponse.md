# Source: https://firebase.google.com/docs/reference/js/ai.generatecontentresponse.md.txt

# GenerateContentResponse interface

Individual response from [GenerativeModel.generateContent()](https://firebase.google.com/docs/reference/js/ai.generativemodel.md#generativemodelgeneratecontent) and [GenerativeModel.generateContentStream()](https://firebase.google.com/docs/reference/js/ai.generativemodel.md#generativemodelgeneratecontentstream). `generateContentStream()` will return one in each chunk until the stream is done.

**Signature:**  

    export interface GenerateContentResponse 

## Properties

|                                                              Property                                                               |                                                                      Type                                                                       | Description |
|-------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| [candidates](https://firebase.google.com/docs/reference/js/ai.generatecontentresponse.md#generatecontentresponsecandidates)         | [GenerateContentCandidate](https://firebase.google.com/docs/reference/js/ai.generatecontentcandidate.md#generatecontentcandidate_interface)\[\] |             |
| [promptFeedback](https://firebase.google.com/docs/reference/js/ai.generatecontentresponse.md#generatecontentresponsepromptfeedback) | [PromptFeedback](https://firebase.google.com/docs/reference/js/ai.promptfeedback.md#promptfeedback_interface)                                   |             |
| [usageMetadata](https://firebase.google.com/docs/reference/js/ai.generatecontentresponse.md#generatecontentresponseusagemetadata)   | [UsageMetadata](https://firebase.google.com/docs/reference/js/ai.usagemetadata.md#usagemetadata_interface)                                      |             |

## GenerateContentResponse.candidates

**Signature:**  

    candidates?: GenerateContentCandidate[];

## GenerateContentResponse.promptFeedback

**Signature:**  

    promptFeedback?: PromptFeedback;

## GenerateContentResponse.usageMetadata

**Signature:**  

    usageMetadata?: UsageMetadata;