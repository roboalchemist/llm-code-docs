# Source: https://firebase.google.com/docs/reference/js/ai.webgroundingchunk.md.txt

# WebGroundingChunk interface

A grounding chunk from the web.
| **Important:** If using Grounding with Google Search, you are required to comply with the [Service Specific Terms](https://cloud.google.com/terms/service-terms) for "Grounding with Google Search".

**Signature:**  

    export interface WebGroundingChunk 

## Properties

|                                                Property                                                 |  Type  |                                                                                                                                                                                                              Description                                                                                                                                                                                                               |
|---------------------------------------------------------------------------------------------------------|--------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [domain](https://firebase.google.com/docs/reference/js/ai.webgroundingchunk.md#webgroundingchunkdomain) | string | The domain of the original URI from which the content was retrieved.This property is only supported in the Vertex AI Gemini API ([VertexAIBackend](https://firebase.google.com/docs/reference/js/ai.vertexaibackend.md#vertexaibackend_class)). When using the Gemini Developer API ([GoogleAIBackend](https://firebase.google.com/docs/reference/js/ai.googleaibackend.md#googleaibackend_class)), this property will be `undefined`. |
| [title](https://firebase.google.com/docs/reference/js/ai.webgroundingchunk.md#webgroundingchunktitle)   | string | The title of the retrieved web page.                                                                                                                                                                                                                                                                                                                                                                                                   |
| [uri](https://firebase.google.com/docs/reference/js/ai.webgroundingchunk.md#webgroundingchunkuri)       | string | The URI of the retrieved web page.                                                                                                                                                                                                                                                                                                                                                                                                     |

## WebGroundingChunk.domain

The domain of the original URI from which the content was retrieved.

This property is only supported in the Vertex AI Gemini API ([VertexAIBackend](https://firebase.google.com/docs/reference/js/ai.vertexaibackend.md#vertexaibackend_class)). When using the Gemini Developer API ([GoogleAIBackend](https://firebase.google.com/docs/reference/js/ai.googleaibackend.md#googleaibackend_class)), this property will be `undefined`.

**Signature:**  

    domain?: string;

## WebGroundingChunk.title

The title of the retrieved web page.

**Signature:**  

    title?: string;

## WebGroundingChunk.uri

The URI of the retrieved web page.

**Signature:**  

    uri?: string;