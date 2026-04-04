# Source: https://firebase.google.com/docs/reference/js/vertexai.groundingmetadata.md.txt

# GroundingMetadata interface

Metadata returned to client when grounding is enabled.

**Signature:**  

    export interface GroundingMetadata 

## Properties

|                                                                  Property                                                                   |                                                                   Type                                                                    | Description |
|---------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| [groundingAttributions](https://firebase.google.com/docs/reference/js/vertexai.groundingmetadata.md#groundingmetadatagroundingattributions) | [GroundingAttribution](https://firebase.google.com/docs/reference/js/vertexai.groundingattribution.md#groundingattribution_interface)\[\] |             |
| [retrievalQueries](https://firebase.google.com/docs/reference/js/vertexai.groundingmetadata.md#groundingmetadataretrievalqueries)           | string\[\]                                                                                                                                |             |
| [webSearchQueries](https://firebase.google.com/docs/reference/js/vertexai.groundingmetadata.md#groundingmetadatawebsearchqueries)           | string\[\]                                                                                                                                |             |

## GroundingMetadata.groundingAttributions

> | **Warning:** This API is now obsolete.

**Signature:**  

    groundingAttributions: GroundingAttribution[];

## GroundingMetadata.retrievalQueries

**Signature:**  

    retrievalQueries?: string[];

## GroundingMetadata.webSearchQueries

**Signature:**  

    webSearchQueries?: string[];