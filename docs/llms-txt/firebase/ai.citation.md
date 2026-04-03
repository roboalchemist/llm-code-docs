# Source: https://firebase.google.com/docs/reference/js/ai.citation.md.txt

# Citation interface

A single citation.

**Signature:**  

    export interface Citation 

## Properties

|                                                Property                                                 |  Type  |                                                                                                            Description                                                                                                             |
|---------------------------------------------------------------------------------------------------------|--------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [endIndex](https://firebase.google.com/docs/reference/js/ai.citation.md#citationendindex)               | number |                                                                                                                                                                                                                                    |
| [license](https://firebase.google.com/docs/reference/js/ai.citation.md#citationlicense)                 | string |                                                                                                                                                                                                                                    |
| [publicationDate](https://firebase.google.com/docs/reference/js/ai.citation.md#citationpublicationdate) | Date   | The publication date of the cited source, if available.This property is only supported in the Vertex AI Gemini API ([VertexAIBackend](https://firebase.google.com/docs/reference/js/ai.vertexaibackend.md#vertexaibackend_class)). |
| [startIndex](https://firebase.google.com/docs/reference/js/ai.citation.md#citationstartindex)           | number |                                                                                                                                                                                                                                    |
| [title](https://firebase.google.com/docs/reference/js/ai.citation.md#citationtitle)                     | string | The title of the cited source, if available.This property is only supported in the Vertex AI Gemini API ([VertexAIBackend](https://firebase.google.com/docs/reference/js/ai.vertexaibackend.md#vertexaibackend_class)).            |
| [uri](https://firebase.google.com/docs/reference/js/ai.citation.md#citationuri)                         | string |                                                                                                                                                                                                                                    |

## Citation.endIndex

**Signature:**  

    endIndex?: number;

## Citation.license

**Signature:**  

    license?: string;

## Citation.publicationDate

The publication date of the cited source, if available.

This property is only supported in the Vertex AI Gemini API ([VertexAIBackend](https://firebase.google.com/docs/reference/js/ai.vertexaibackend.md#vertexaibackend_class)).

**Signature:**  

    publicationDate?: Date;

## Citation.startIndex

**Signature:**  

    startIndex?: number;

## Citation.title

The title of the cited source, if available.

This property is only supported in the Vertex AI Gemini API ([VertexAIBackend](https://firebase.google.com/docs/reference/js/ai.vertexaibackend.md#vertexaibackend_class)).

**Signature:**  

    title?: string;

## Citation.uri

**Signature:**  

    uri?: string;