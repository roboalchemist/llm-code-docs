# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/CitationMetadata.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/CitationMetadata.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/CitationMetadata.md.txt

# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/CitationMetadata.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/CitationMetadata.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/CitationMetadata.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/CitationMetadata.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/CitationMetadata.md.txt

# FirebaseAI Framework Reference

# CitationMetadata

    @available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
    public struct CitationMetadata : Sendable

    extension CitationMetadata: Decodable

A collection of source attributions for a piece of content.
- `
  ``
  ``
  `

  ### [citations](https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/CitationMetadata#/s:10FirebaseAI16CitationMetadataV9citationsSayAA0C0VGvp)

  `
  `  
  A list of individual cited sources and the parts of the content to which they apply.  

  #### Declaration

  Swift  

      public let citations: [https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/Citation.html]

[## Codable Conformances](https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/CitationMetadata#/Codable-Conformances)

- `
  ``
  ``
  `

  ### [init(from:)](https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/CitationMetadata#/s:Se4fromxs7Decoder_p_tKcfc)

  `
  `  

  #### Declaration

  Swift  

      public init(from decoder: any Decoder) throws