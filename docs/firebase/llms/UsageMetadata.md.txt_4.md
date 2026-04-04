# Source: https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/GenerateContentResponse/UsageMetadata.md.txt

# FirebaseAILogic Framework Reference

# UsageMetadata

    @available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
    public struct UsageMetadata : Sendable

    extension https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/GenerateContentResponse.html.UsageMetadata: Decodable

Token usage metadata for processing the generate content request.
- `


  ### [promptTokenCount](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/GenerateContentResponse/UsageMetadata#/s:15FirebaseAILogic23GenerateContentResponseV13UsageMetadataV16promptTokenCountSivp)


  ` The number of tokens in the request prompt.

  #### Declaration

  Swift

      public let promptTokenCount: Int

- `


  ### [cachedContentTokenCount](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/GenerateContentResponse/UsageMetadata#/s:15FirebaseAILogic23GenerateContentResponseV13UsageMetadataV06cachedD10TokenCountSivp)


  ` The number of tokens in the prompt that were served from the cache.
  If implicit caching is not active or no content was cached, this will be 0.

  #### Declaration

  Swift

      public let cachedContentTokenCount: Int

- `


  ### [candidatesTokenCount](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/GenerateContentResponse/UsageMetadata#/s:15FirebaseAILogic23GenerateContentResponseV13UsageMetadataV20candidatesTokenCountSivp)


  ` The total number of tokens across the generated response candidates.

  #### Declaration

  Swift

      public let candidatesTokenCount: Int

- `


  ### [toolUsePromptTokenCount](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/GenerateContentResponse/UsageMetadata#/s:15FirebaseAILogic23GenerateContentResponseV13UsageMetadataV23toolUsePromptTokenCountSivp)


  ` The number of tokens used by tools.

  #### Declaration

  Swift

      public let toolUsePromptTokenCount: Int

- `


  ### [thoughtsTokenCount](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/GenerateContentResponse/UsageMetadata#/s:15FirebaseAILogic23GenerateContentResponseV13UsageMetadataV18thoughtsTokenCountSivp)


  ` The number of tokens used by the model's internal "thinking" process.

  For models that support thinking (like Gemini 2.5 Pro and Flash), this represents the actual
  number of tokens consumed for reasoning before the model generated a response. For models
  that do not support thinking, this value will be `0`.

  When thinking is used, this count will be less than or equal to the `thinkingBudget` set in
  the `https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/ThinkingConfig.html`.

  #### Declaration

  Swift

      public let thoughtsTokenCount: Int

- `


  ### [totalTokenCount](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/GenerateContentResponse/UsageMetadata#/s:15FirebaseAILogic23GenerateContentResponseV13UsageMetadataV15totalTokenCountSivp)


  ` The total number of tokens in both the request and response.

  #### Declaration

  Swift

      public let totalTokenCount: Int

- `


  ### [promptTokensDetails](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/GenerateContentResponse/UsageMetadata#/s:15FirebaseAILogic23GenerateContentResponseV13UsageMetadataV19promptTokensDetailsSayAA18ModalityTokenCountVGvp)


  ` The breakdown, by modality, of how many tokens are consumed by the prompt.

  #### Declaration

  Swift

      public let promptTokensDetails: [https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/ModalityTokenCount.html]

- `


  ### [cacheTokensDetails](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/GenerateContentResponse/UsageMetadata#/s:15FirebaseAILogic23GenerateContentResponseV13UsageMetadataV18cacheTokensDetailsSayAA18ModalityTokenCountVGvp)


  ` The breakdown, by modality, of how many tokens are consumed by the cached content.

  #### Declaration

  Swift

      public let cacheTokensDetails: [https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/ModalityTokenCount.html]

- `


  ### [candidatesTokensDetails](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/GenerateContentResponse/UsageMetadata#/s:15FirebaseAILogic23GenerateContentResponseV13UsageMetadataV23candidatesTokensDetailsSayAA18ModalityTokenCountVGvp)


  ` Detailed breakdown of the cached tokens by modality (e.g., text, image).
  This list provides granular insight into which parts of the content were cached.

  #### Declaration

  Swift

      public let candidatesTokensDetails: [https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/ModalityTokenCount.html]

- `


  ### [toolUsePromptTokensDetails](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/GenerateContentResponse/UsageMetadata#/s:15FirebaseAILogic23GenerateContentResponseV13UsageMetadataV26toolUsePromptTokensDetailsSayAA18ModalityTokenCountVGvp)


  ` The breakdown, by modality, of how many tokens were consumed by the tools used to process
  the request.

  #### Declaration

  Swift

      public let toolUsePromptTokensDetails: [https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/ModalityTokenCount.html]

[## Codable Conformances](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/GenerateContentResponse/UsageMetadata#/Codable-Conformances)

- `


  ### [init(from:)](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/GenerateContentResponse/UsageMetadata#/s:Se4fromxs7Decoder_p_tKcfc)


  `

  #### Declaration

  Swift

      public init(from decoder: any Decoder) throws