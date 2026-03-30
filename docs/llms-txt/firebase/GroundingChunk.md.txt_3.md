# Source: https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/GroundingMetadata/GroundingChunk.md.txt

# FirebaseAILogic Framework Reference

# GroundingChunk

    @available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
    public struct GroundingChunk : Sendable, Equatable, Hashable

    extension https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/GroundingMetadata.html.GroundingChunk: Decodable

Represents a chunk of retrieved data that supports a claim in the model's response. This is
part of the grounding information provided when grounding is enabled.
- `


  ### [web](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/GroundingMetadata/GroundingChunk#/s:15FirebaseAILogic17GroundingMetadataV0C5ChunkV3webAC03WebcE0VSgvp)


  ` Contains details if the grounding chunk is from a web source.

  #### Declaration

  Swift

      public let web: https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/GroundingMetadata/WebGroundingChunk.html?