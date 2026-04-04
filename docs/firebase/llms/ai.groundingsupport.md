# Source: https://firebase.google.com/docs/reference/js/ai.groundingsupport.md.txt

# GroundingSupport interface

Provides information about how a specific segment of the model's response is supported by the retrieved grounding chunks.

**Signature:**  

    export interface GroundingSupport 

## Properties

|                                                              Property                                                               |                                           Type                                           |                                                                                                                                                                                                                                                                                                           Description                                                                                                                                                                                                                                                                                                           |
|-------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [groundingChunkIndices](https://firebase.google.com/docs/reference/js/ai.groundingsupport.md#groundingsupportgroundingchunkindices) | number\[\]                                                                               | A list of indices that refer to specific [GroundingChunk](https://firebase.google.com/docs/reference/js/ai.groundingchunk.md#groundingchunk_interface) objects within the [GroundingMetadata.groundingChunks](https://firebase.google.com/docs/reference/js/ai.groundingmetadata.md#groundingmetadatagroundingchunks) array. These referenced chunks are the sources that support the claim made in the associated `segment` of the response. For example, an array `[1, 3, 4]` means that `groundingChunks[1]`, `groundingChunks[3]`, and `groundingChunks[4]` are the retrieved content supporting this part of the response. |
| [segment](https://firebase.google.com/docs/reference/js/ai.groundingsupport.md#groundingsupportsegment)                             | [Segment](https://firebase.google.com/docs/reference/js/ai.segment.md#segment_interface) | Specifies the segment of the model's response content that this grounding support pertains to.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |

## GroundingSupport.groundingChunkIndices

A list of indices that refer to specific [GroundingChunk](https://firebase.google.com/docs/reference/js/ai.groundingchunk.md#groundingchunk_interface) objects within the [GroundingMetadata.groundingChunks](https://firebase.google.com/docs/reference/js/ai.groundingmetadata.md#groundingmetadatagroundingchunks) array. These referenced chunks are the sources that support the claim made in the associated `segment` of the response. For example, an array `[1, 3, 4]` means that `groundingChunks[1]`, `groundingChunks[3]`, and `groundingChunks[4]` are the retrieved content supporting this part of the response.

**Signature:**  

    groundingChunkIndices?: number[];

## GroundingSupport.segment

Specifies the segment of the model's response content that this grounding support pertains to.

**Signature:**  

    segment?: Segment;