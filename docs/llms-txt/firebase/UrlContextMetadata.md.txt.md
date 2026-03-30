# Source: https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/URLContextMetadata.md.txt

# FirebaseAILogic Framework Reference

# URLContextMetadata

    @available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
    public struct URLContextMetadata : Sendable, Hashable

    extension URLContextMetadata: Decodable

Metadata related to the `https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/Tool.html#/s:15FirebaseAILogic4ToolV10urlContextACyFZ` tool.
- `


  ### [urlMetadata](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/URLContextMetadata#/s:15FirebaseAILogic18URLContextMetadataV03urlD0SayAA11URLMetadataVGvp)


  ` List of URL metadata used to provide context to the Gemini model.

  #### Declaration

  Swift

      public let urlMetadata: [https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/URLMetadata.html]

[## Codable Conformances](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/URLContextMetadata#/Codable-Conformances)

- `


  ### [init(from:)](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/URLContextMetadata#/s:Se4fromxs7Decoder_p_tKcfc)


  `

  #### Declaration

  Swift

      public init(from decoder: any Decoder) throws