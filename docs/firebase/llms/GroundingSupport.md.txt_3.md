# Source: https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/GroundingMetadata/GroundingSupport.md.txt

# FirebaseAILogic Framework Reference

# GroundingSupport

    @available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
    public struct GroundingSupport : Sendable, Equatable, Hashable

Provides information about how a specific segment of the model's response is supported by the
retrieved grounding chunks.
- `


  ### [segment](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/GroundingMetadata/GroundingSupport#/s:15FirebaseAILogic17GroundingMetadataV0C7SupportV7segmentAA7SegmentVvp)


  ` Specifies the segment of the model's response content that this grounding support pertains
  to.

  #### Declaration

  Swift

      public let segment: https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/Segment.html

- `


  ### [groundingChunkIndices](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/GroundingMetadata/GroundingSupport#/s:15FirebaseAILogic17GroundingMetadataV0C7SupportV21groundingChunkIndicesSaySiGvp)


  ` A list of indices that refer to specific `https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/GroundingMetadata/GroundingChunk.html` structs within the
  `https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/GroundingMetadata.html#/s:15FirebaseAILogic17GroundingMetadataV15groundingChunksSayAC0C5ChunkVGvp` array. These referenced chunks are the sources that
  support the claim made in the associated `https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/GroundingMetadata/GroundingSupport.html#/s:15FirebaseAILogic17GroundingMetadataV0C7SupportV7segmentAA7SegmentVvp` of the response. For example, an array
  `[1, 3, 4]`
  means that `groundingChunks[1]`, `groundingChunks[3]`, `groundingChunks[4]` are the
  retrieved content supporting this part of the response.

  #### Declaration

  Swift

      public let groundingChunkIndices: [Int]