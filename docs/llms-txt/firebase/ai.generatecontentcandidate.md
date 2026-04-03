# Source: https://firebase.google.com/docs/reference/js/ai.generatecontentcandidate.md.txt

A candidate returned as part of a [GenerateContentResponse](https://firebase.google.com/docs/reference/js/ai.generatecontentresponse.md#generatecontentresponse_interface).

**Signature:**  

    export interface GenerateContentCandidate 

## Properties

|                                                                   Property                                                                    |                                                           Type                                                            | Description |
|-----------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|-------------|
| [citationMetadata](https://firebase.google.com/docs/reference/js/ai.generatecontentcandidate.md#generatecontentcandidatecitationmetadata)     | [CitationMetadata](https://firebase.google.com/docs/reference/js/ai.citationmetadata.md#citationmetadata_interface)       |             |
| [content](https://firebase.google.com/docs/reference/js/ai.generatecontentcandidate.md#generatecontentcandidatecontent)                       | [Content](https://firebase.google.com/docs/reference/js/ai.content.md#content_interface)                                  |             |
| [finishMessage](https://firebase.google.com/docs/reference/js/ai.generatecontentcandidate.md#generatecontentcandidatefinishmessage)           | string                                                                                                                    |             |
| [finishReason](https://firebase.google.com/docs/reference/js/ai.generatecontentcandidate.md#generatecontentcandidatefinishreason)             | [FinishReason](https://firebase.google.com/docs/reference/js/ai.md#finishreason)                                          |             |
| [groundingMetadata](https://firebase.google.com/docs/reference/js/ai.generatecontentcandidate.md#generatecontentcandidategroundingmetadata)   | [GroundingMetadata](https://firebase.google.com/docs/reference/js/ai.groundingmetadata.md#groundingmetadata_interface)    |             |
| [index](https://firebase.google.com/docs/reference/js/ai.generatecontentcandidate.md#generatecontentcandidateindex)                           | number                                                                                                                    |             |
| [safetyRatings](https://firebase.google.com/docs/reference/js/ai.generatecontentcandidate.md#generatecontentcandidatesafetyratings)           | [SafetyRating](https://firebase.google.com/docs/reference/js/ai.safetyrating.md#safetyrating_interface)\[\]               |             |
| [urlContextMetadata](https://firebase.google.com/docs/reference/js/ai.generatecontentcandidate.md#generatecontentcandidateurlcontextmetadata) | [URLContextMetadata](https://firebase.google.com/docs/reference/js/ai.urlcontextmetadata.md#urlcontextmetadata_interface) |             |

## GenerateContentCandidate.citationMetadata

**Signature:**  

    citationMetadata?: CitationMetadata;

## GenerateContentCandidate.content

**Signature:**  

    content: Content;

## GenerateContentCandidate.finishMessage

**Signature:**  

    finishMessage?: string;

## GenerateContentCandidate.finishReason

**Signature:**  

    finishReason?: FinishReason;

## GenerateContentCandidate.groundingMetadata

**Signature:**  

    groundingMetadata?: GroundingMetadata;

## GenerateContentCandidate.index

**Signature:**  

    index: number;

## GenerateContentCandidate.safetyRatings

**Signature:**  

    safetyRatings?: SafetyRating[];

## GenerateContentCandidate.urlContextMetadata

**Signature:**  

    urlContextMetadata?: URLContextMetadata;