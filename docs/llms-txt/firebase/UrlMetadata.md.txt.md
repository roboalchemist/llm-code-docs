# Source: https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/URLMetadata.md.txt

# FirebaseAILogic Framework Reference

# URLMetadata

    @available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
    public struct URLMetadata : Sendable, Hashable

    extension URLMetadata: Decodable

Metadata for a single URL retrieved by the `https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/Tool.html#/s:15FirebaseAILogic4ToolV10urlContextACyFZ` tool.
- `


  ### [URLRetrievalStatus](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/URLMetadata/URLRetrievalStatus.html)


  ` Status of the URL retrieval.

  #### Declaration

  Swift

      public struct URLRetrievalStatus : DecodableProtoEnum, Hashable

- `


  ### [retrievedURL](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/URLMetadata#/s:15FirebaseAILogic11URLMetadataV12retrievedURL10Foundation0E0VSgvp)


  ` The retrieved URL.

  #### Declaration

  Swift

      public let retrievedURL: URL?

- `


  ### [retrievalStatus](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/URLMetadata#/s:15FirebaseAILogic11URLMetadataV15retrievalStatusAC012URLRetrievalE0Vvp)


  ` The status of the URL retrieval.

  #### Declaration

  Swift

      public let retrievalStatus: https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/URLMetadata/URLRetrievalStatus.html

[## Codable Conformances](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/URLMetadata#/Codable-Conformances)

- `


  ### [init(from:)](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/URLMetadata#/s:Se4fromxs7Decoder_p_tKcfc)


  `

  #### Declaration

  Swift

      public init(from decoder: any Decoder) throws