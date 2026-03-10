# Source: https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/GenerateContentResponse/UsageMetadata.md.txt

# FirebaseVertexAI Framework Reference

# UsageMetadata

    @available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
    public struct UsageMetadata : Sendable

    extension https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/GenerateContentResponse.html.UsageMetadata: Decodable

Token usage metadata for processing the generate content request.
- `


  ### [promptTokenCount](https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/GenerateContentResponse/UsageMetadata#/s:16FirebaseVertexAI23GenerateContentResponseV13UsageMetadataV16promptTokenCountSivp)


  ` The number of tokens in the request prompt.

  #### Declaration

  Swift

      public let promptTokenCount: Int

- `


  ### [candidatesTokenCount](https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/GenerateContentResponse/UsageMetadata#/s:16FirebaseVertexAI23GenerateContentResponseV13UsageMetadataV20candidatesTokenCountSivp)


  ` The total number of tokens across the generated response candidates.

  #### Declaration

  Swift

      public let candidatesTokenCount: Int

- `


  ### [totalTokenCount](https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/GenerateContentResponse/UsageMetadata#/s:16FirebaseVertexAI23GenerateContentResponseV13UsageMetadataV15totalTokenCountSivp)


  ` The total number of tokens in both the request and response.

  #### Declaration

  Swift

      public let totalTokenCount: Int

- `


  ### [promptTokensDetails](https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/GenerateContentResponse/UsageMetadata#/s:16FirebaseVertexAI23GenerateContentResponseV13UsageMetadataV19promptTokensDetailsSayAA18ModalityTokenCountVGvp)


  ` The breakdown, by modality, of how many tokens are consumed by the prompt

  #### Declaration

  Swift

      public let promptTokensDetails: [https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/ModalityTokenCount.html]

- `


  ### [candidatesTokensDetails](https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/GenerateContentResponse/UsageMetadata#/s:16FirebaseVertexAI23GenerateContentResponseV13UsageMetadataV23candidatesTokensDetailsSayAA18ModalityTokenCountVGvp)


  ` The breakdown, by modality, of how many tokens are consumed by the candidates

  #### Declaration

  Swift

      public let candidatesTokensDetails: [https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/ModalityTokenCount.html]

[## Codable Conformances](https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/GenerateContentResponse/UsageMetadata#/Codable-Conformances)

- `


  ### [init(from:)](https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/GenerateContentResponse/UsageMetadata#/s:Se4fromxs7Decoder_p_tKcfc)


  `

  #### Declaration

  Swift

      public init(from decoder: any Decoder) throws