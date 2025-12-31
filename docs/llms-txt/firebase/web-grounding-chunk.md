# Source: https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/web-grounding-chunk.md.txt

# Firebase.AI.WebGroundingChunk Struct Reference

# Firebase.AI.WebGroundingChunk

A grounding chunk sourced from the web.

## Summary

|                                                                                                                            ### Properties                                                                                                                            ||
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------|
| [Domain](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/web-grounding-chunk#struct_firebase_1_1_a_i_1_1_web_grounding_chunk_1ac29cbc0bc4b2abe15cc35501c5e56bd5) | `string` The domain of the original URI from which the content was retrieved. |
| [Title](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/web-grounding-chunk#struct_firebase_1_1_a_i_1_1_web_grounding_chunk_1a6611e76483727b80237c64d4129bc4a3)  | `string` The title of the retrieved web page.                                 |
| [Uri](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/web-grounding-chunk#struct_firebase_1_1_a_i_1_1_web_grounding_chunk_1a2b8b0191f23377ab1c6b56e6c57abdba)    | `System.Uri` The URI of the retrieved web page.                               |

## Properties

### Domain

```c#
string Firebase::AI::WebGroundingChunk::Domain
```  
The domain of the original URI from which the content was retrieved.

This field is only populated when using the Vertex [AI](https://firebase.google.com/docs/reference/unity/namespace/firebase/a-i#namespace_firebase_1_1_a_i) Gemini API.  

### Title

```c#
string Firebase::AI::WebGroundingChunk::Title
```  
The title of the retrieved web page.  

### Uri

```c#
System.Uri Firebase::AI::WebGroundingChunk::Uri
```  
The URI of the retrieved web page.