# Source: https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/grounding-metadata.md.txt

# Firebase.AI.GroundingMetadata Struct Reference

# Firebase.AI.GroundingMetadata

Metadata returned to the client when grounding is enabled.

## Summary

Important: If using Grounding with Google Search, you are required to comply with the "Grounding with Google Search" usage requirements for your chosen API provider: [Gemini Developer API](https://ai.google.dev/gemini-api/terms#grounding-with-google-search) or Vertex [AI](https://firebase.google.com/docs/reference/unity/namespace/firebase/a-i#namespace_firebase_1_1_a_i) Gemini API (see [Service Terms](https://cloud.google.com/terms/service-terms) section within the Service Specific Terms).

|                                                                                                                                                                                                                                                                      ### Properties                                                                                                                                                                                                                                                                       ||
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [GroundingChunks](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/grounding-metadata#struct_firebase_1_1_a_i_1_1_grounding_metadata_1ac10d0ba8af5e1f742a0e9978bd809ea5)   | `IReadOnlyList< `[GroundingChunk](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/grounding-chunk#struct_firebase_1_1_a_i_1_1_grounding_chunk)` >` A list of [GroundingChunk](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/grounding-chunk#struct_firebase_1_1_a_i_1_1_grounding_chunk) structs.             |
| [GroundingSupports](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/grounding-metadata#struct_firebase_1_1_a_i_1_1_grounding_metadata_1ae105e8e1d2a03af11eff5dbfedca6eb3) | `IReadOnlyList< `[GroundingSupport](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/grounding-support#struct_firebase_1_1_a_i_1_1_grounding_support)` >` A list of [GroundingSupport](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/grounding-support#struct_firebase_1_1_a_i_1_1_grounding_support) structs. |
| [SearchEntryPoint](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/grounding-metadata#struct_firebase_1_1_a_i_1_1_grounding_metadata_1a2cd951761d448f0cd6a4da15fde292e0)  | [SearchEntryPoint](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/search-entry-point#struct_firebase_1_1_a_i_1_1_search_entry_point) Google Search entry point for web searches.                                                                                                                                                    |
| [WebSearchQueries](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/grounding-metadata#struct_firebase_1_1_a_i_1_1_grounding_metadata_1a77c935a95b0a23ffc096575640177745)  | `IReadOnlyList< string >` A list of web search queries that the model performed to gather the grounding information.                                                                                                                                                                                                                                      |

## Properties

### GroundingChunks

```c#
IReadOnlyList< GroundingChunk > Firebase::AI::GroundingMetadata::GroundingChunks
```  
A list of [GroundingChunk](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/grounding-chunk#struct_firebase_1_1_a_i_1_1_grounding_chunk) structs.

Each chunk represents a piece of retrieved content (e.g., from a web page) that the model used to ground its response.  

### GroundingSupports

```c#
IReadOnlyList< GroundingSupport > Firebase::AI::GroundingMetadata::GroundingSupports
```  
A list of [GroundingSupport](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/grounding-support#struct_firebase_1_1_a_i_1_1_grounding_support) structs.

Each object details how specific segments of the model's response are supported by the `groundingChunks`.  

### SearchEntryPoint

```c#
SearchEntryPoint Firebase::AI::GroundingMetadata::SearchEntryPoint
```  
Google Search entry point for web searches.

This contains an HTML/CSS snippet that **must** be embedded in an app to display a Google Search entry point for follow-up web searches related to the model's "Grounded Response".  

### WebSearchQueries

```c#
IReadOnlyList< string > Firebase::AI::GroundingMetadata::WebSearchQueries
```  
A list of web search queries that the model performed to gather the grounding information.

These can be used to allow users to explore the search results themselves.