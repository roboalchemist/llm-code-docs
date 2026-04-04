# Source: https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/CountTokensResponse.md.txt

# FirebaseAILogic Framework Reference

# CountTokensResponse

    @available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
    public struct CountTokensResponse : Sendable

    extension CountTokensResponse: Decodable

The model's response to a count tokens request.
- `


  ### [totalTokens](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/CountTokensResponse#/s:15FirebaseAILogic19CountTokensResponseV05totalD0Sivp)


  ` The total number of tokens in the input given to the model as a prompt.

  #### Declaration

  Swift

      public let totalTokens: Int

- `


  ### [promptTokensDetails](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/CountTokensResponse#/s:15FirebaseAILogic19CountTokensResponseV06promptD7DetailsSayAA013ModalityTokenC0VGvp)


  ` The breakdown, by modality, of how many tokens are consumed by the prompt.

  #### Declaration

  Swift

      public let promptTokensDetails: [https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/ModalityTokenCount.html]

[## Codable Conformances](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/CountTokensResponse#/Codable-Conformances)

- `


  ### [init(from:)](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/CountTokensResponse#/s:Se4fromxs7Decoder_p_tKcfc)


  `

  #### Declaration

  Swift

      public init(from decoder: any Decoder) throws