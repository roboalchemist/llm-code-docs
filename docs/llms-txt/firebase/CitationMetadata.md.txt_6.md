# Source: https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/CitationMetadata.md.txt

# FirebaseVertexAI Framework Reference

# CitationMetadata

    @available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
    public struct CitationMetadata : Sendable

    extension CitationMetadata: Decodable

A collection of source attributions for a piece of content.
- `


  ### [citations](https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/CitationMetadata#/s:16FirebaseVertexAI16CitationMetadataV9citationsSayAA0D0VGvp)


  ` A list of individual cited sources and the parts of the content to which they apply.

  #### Declaration

  Swift

      public let citations: [https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/Citation.html]