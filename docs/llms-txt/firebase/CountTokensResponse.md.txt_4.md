# Source: https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/CountTokensResponse.md.txt

# FirebaseVertexAI Framework Reference

# CountTokensResponse

    @available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
    public struct CountTokensResponse

    extension CountTokensResponse: Decodable

The model's response to a count tokens request.
- `


  ### [totalTokens](https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/CountTokensResponse#/s:16FirebaseVertexAI19CountTokensResponseV05totalE0Sivp)


  ` The total number of tokens in the input given to the model as a prompt.

  #### Declaration

  Swift

      public let totalTokens: Int

- `


  ### [totalBillableCharacters](https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/CountTokensResponse#/s:16FirebaseVertexAI19CountTokensResponseV23totalBillableCharactersSiSgvp)


  ` The total number of billable characters in the text input given to the model as a prompt.
  Important

  This does not include billable image, video or other non-text input. See
  [Vertex AI pricing](https://firebase.google.com/docs/vertex-ai/pricing) for details.

  #### Declaration

  Swift

      public let totalBillableCharacters: Int?

- `


  ### [promptTokensDetails](https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/CountTokensResponse#/s:16FirebaseVertexAI19CountTokensResponseV06promptE7DetailsSayAA013ModalityTokenD0VGvp)


  ` The breakdown, by modality, of how many tokens are consumed by the prompt.

  #### Declaration

  Swift

      public let promptTokensDetails: [https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/ModalityTokenCount.html]

[## Codable Conformances](https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/CountTokensResponse#/Codable-Conformances)

- `


  ### [init(from:)](https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/CountTokensResponse#/s:Se4fromxs7Decoder_p_tKcfc)


  `

  #### Declaration

  Swift

      public init(from decoder: any Decoder) throws