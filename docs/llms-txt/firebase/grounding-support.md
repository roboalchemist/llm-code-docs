# Source: https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/grounding-support.md.txt

# Firebase.AI.GroundingSupport Struct Reference

# Firebase.AI.GroundingSupport

Provides information about how a specific segment of the model's response is supported by the retrieved grounding chunks.

## Summary

|                                                                                                                                                                                                                                                                                                                        ### Properties                                                                                                                                                                                                                                                                                                                         ||
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [GroundingChunkIndices](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/grounding-support#struct_firebase_1_1_a_i_1_1_grounding_support_1a66091ad3578346f24e3a1bfab472789a) | `IReadOnlyList< int >` A list of indices that refer to specific [GroundingChunk](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/grounding-chunk#struct_firebase_1_1_a_i_1_1_grounding_chunk) structs within the [GroundingMetadata.GroundingChunks](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/grounding-metadata#struct_firebase_1_1_a_i_1_1_grounding_metadata_1ac10d0ba8af5e1f742a0e9978bd809ea5) array. |
| [Segment](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/grounding-support#struct_firebase_1_1_a_i_1_1_grounding_support_1adf486c17bf3aaf0b6bf3ac02f1e69dd1)               | [Segment](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/segment#struct_firebase_1_1_a_i_1_1_segment) Specifies the segment of the model's response content that this grounding support pertains to.                                                                                                                                                                                                                                  |

## Properties

### GroundingChunkIndices

```c#
IReadOnlyList< int > Firebase::AI::GroundingSupport::GroundingChunkIndices
```  
A list of indices that refer to specific [GroundingChunk](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/grounding-chunk#struct_firebase_1_1_a_i_1_1_grounding_chunk) structs within the [GroundingMetadata.GroundingChunks](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/grounding-metadata#struct_firebase_1_1_a_i_1_1_grounding_metadata_1ac10d0ba8af5e1f742a0e9978bd809ea5) array.

These referenced chunks are the sources that support the claim made in the associated `segment` of the response. For example, an array `[1, 3, 4]` means that `groundingChunks[1]`, `groundingChunks[3]`, `groundingChunks[4]` are the retrieved content supporting this part of the response.  

### Segment

```c#
Segment Firebase::AI::GroundingSupport::Segment
```  
Specifies the segment of the model's response content that this grounding support pertains to.