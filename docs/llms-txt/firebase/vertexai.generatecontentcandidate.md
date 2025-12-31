# Source: https://firebase.google.com/docs/reference/js/vertexai.generatecontentcandidate.md.txt

# GenerateContentCandidate interface

A candidate returned as part of a [GenerateContentResponse](https://firebase.google.com/docs/reference/js/vertexai.generatecontentresponse.md#generatecontentresponse_interface).

**Signature:**  

    export interface GenerateContentCandidate 

## Properties

|                                                                     Property                                                                      |                                                             Type                                                             | Description |
|---------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------|-------------|
| [citationMetadata](https://firebase.google.com/docs/reference/js/vertexai.generatecontentcandidate.md#generatecontentcandidatecitationmetadata)   | [CitationMetadata](https://firebase.google.com/docs/reference/js/vertexai.citationmetadata.md#citationmetadata_interface)    |             |
| [content](https://firebase.google.com/docs/reference/js/vertexai.generatecontentcandidate.md#generatecontentcandidatecontent)                     | [Content](https://firebase.google.com/docs/reference/js/vertexai.content.md#content_interface)                               |             |
| [finishMessage](https://firebase.google.com/docs/reference/js/vertexai.generatecontentcandidate.md#generatecontentcandidatefinishmessage)         | string                                                                                                                       |             |
| [finishReason](https://firebase.google.com/docs/reference/js/vertexai.generatecontentcandidate.md#generatecontentcandidatefinishreason)           | [FinishReason](https://firebase.google.com/docs/reference/js/vertexai.md#finishreason)                                       |             |
| [groundingMetadata](https://firebase.google.com/docs/reference/js/vertexai.generatecontentcandidate.md#generatecontentcandidategroundingmetadata) | [GroundingMetadata](https://firebase.google.com/docs/reference/js/vertexai.groundingmetadata.md#groundingmetadata_interface) |             |
| [index](https://firebase.google.com/docs/reference/js/vertexai.generatecontentcandidate.md#generatecontentcandidateindex)                         | number                                                                                                                       |             |
| [safetyRatings](https://firebase.google.com/docs/reference/js/vertexai.generatecontentcandidate.md#generatecontentcandidatesafetyratings)         | [SafetyRating](https://firebase.google.com/docs/reference/js/vertexai.safetyrating.md#safetyrating_interface)\[\]            |             |

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