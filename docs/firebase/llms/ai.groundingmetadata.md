# Source: https://firebase.google.com/docs/reference/js/ai.groundingmetadata.md.txt

# GroundingMetadata interface

Metadata returned when grounding is enabled.

Currently, only Grounding with Google Search is supported (see [GoogleSearchTool](https://firebase.google.com/docs/reference/js/ai.googlesearchtool.md#googlesearchtool_interface)).
| **Important:** If using Grounding with Google Search, you are required to comply with the "Grounding with Google Search" usage requirements for your chosen API provider: [Gemini Developer API](https://ai.google.dev/gemini-api/terms#grounding-with-google-search) or Vertex AI Gemini API (see [Service Terms](https://cloud.google.com/terms/service-terms) section within the Service Specific Terms).

**Signature:**  

    export interface GroundingMetadata 

## Properties

|                                                           Property                                                            |                                                          Type                                                           |                                                                                                                           Description                                                                                                                           |
|-------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [groundingChunks](https://firebase.google.com/docs/reference/js/ai.groundingmetadata.md#groundingmetadatagroundingchunks)     | [GroundingChunk](https://firebase.google.com/docs/reference/js/ai.groundingchunk.md#groundingchunk_interface)\[\]       | A list of [GroundingChunk](https://firebase.google.com/docs/reference/js/ai.groundingchunk.md#groundingchunk_interface) objects. Each chunk represents a piece of retrieved content (for example, from a web page). that the model used to ground its response. |
| [groundingSupports](https://firebase.google.com/docs/reference/js/ai.groundingmetadata.md#groundingmetadatagroundingsupports) | [GroundingSupport](https://firebase.google.com/docs/reference/js/ai.groundingsupport.md#groundingsupport_interface)\[\] | A list of [GroundingSupport](https://firebase.google.com/docs/reference/js/ai.groundingsupport.md#groundingsupport_interface) objects. Each object details how specific segments of the model's response are supported by the `groundingChunks`.                |
| [retrievalQueries](https://firebase.google.com/docs/reference/js/ai.groundingmetadata.md#groundingmetadataretrievalqueries)   | string\[\]                                                                                                              |                                                                                                                                                                                                                                                                 |
| [searchEntryPoint](https://firebase.google.com/docs/reference/js/ai.groundingmetadata.md#groundingmetadatasearchentrypoint)   | [SearchEntrypoint](https://firebase.google.com/docs/reference/js/ai.searchentrypoint.md#searchentrypoint_interface)     | Google Search entry point for web searches. This contains an HTML/CSS snippet that must be embedded in an app to display a Google Search entry point for follow-up web searches related to a model's "Grounded Response".                                       |
| [webSearchQueries](https://firebase.google.com/docs/reference/js/ai.groundingmetadata.md#groundingmetadatawebsearchqueries)   | string\[\]                                                                                                              | A list of web search queries that the model performed to gather the grounding information. These can be used to allow users to explore the search results themselves.                                                                                           |

## GroundingMetadata.groundingChunks

A list of [GroundingChunk](https://firebase.google.com/docs/reference/js/ai.groundingchunk.md#groundingchunk_interface) objects. Each chunk represents a piece of retrieved content (for example, from a web page). that the model used to ground its response.

**Signature:**  

    groundingChunks?: GroundingChunk[];

## GroundingMetadata.groundingSupports

A list of [GroundingSupport](https://firebase.google.com/docs/reference/js/ai.groundingsupport.md#groundingsupport_interface) objects. Each object details how specific segments of the model's response are supported by the `groundingChunks`.

**Signature:**  

    groundingSupports?: GroundingSupport[];

## GroundingMetadata.retrievalQueries

> | **Warning:** This API is now obsolete.
>
> Use [GroundingSupport](https://firebase.google.com/docs/reference/js/ai.groundingsupport.md#groundingsupport_interface) instead.

**Signature:**  

    retrievalQueries?: string[];

## GroundingMetadata.searchEntryPoint

Google Search entry point for web searches. This contains an HTML/CSS snippet that must be embedded in an app to display a Google Search entry point for follow-up web searches related to a model's "Grounded Response".

**Signature:**  

    searchEntryPoint?: SearchEntrypoint;

## GroundingMetadata.webSearchQueries

A list of web search queries that the model performed to gather the grounding information. These can be used to allow users to explore the search results themselves.

**Signature:**  

    webSearchQueries?: string[];