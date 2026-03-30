# Source: https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/GroundingMetadata/WebGroundingChunk.md.txt

# FirebaseAILogic Framework Reference

# WebGroundingChunk

    @available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
    public struct WebGroundingChunk : Sendable, Equatable, Hashable

    extension https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/GroundingMetadata.html.WebGroundingChunk: Decodable

A grounding chunk sourced from the web.
- `


  ### [uri](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/GroundingMetadata/WebGroundingChunk#/s:15FirebaseAILogic17GroundingMetadataV03WebC5ChunkV3uriSSSgvp)


  ` The URI of the retrieved web page.

  #### Declaration

  Swift

      public let uri: String?

- `


  ### [title](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/GroundingMetadata/WebGroundingChunk#/s:15FirebaseAILogic17GroundingMetadataV03WebC5ChunkV5titleSSSgvp)


  ` The title of the retrieved web page.

  #### Declaration

  Swift

      public let title: String?

- `


  ### [domain](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/GroundingMetadata/WebGroundingChunk#/s:15FirebaseAILogic17GroundingMetadataV03WebC5ChunkV6domainSSSgvp)


  ` The domain of the original URI from which the content was retrieved.

  This field is only populated when using the Vertex AI Gemini API.

  #### Declaration

  Swift

      public let domain: String?