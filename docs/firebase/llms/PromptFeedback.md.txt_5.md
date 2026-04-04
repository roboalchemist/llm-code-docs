# Source: https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/PromptFeedback.md.txt

# FirebaseVertexAI Framework Reference

# PromptFeedback

    @available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
    public struct PromptFeedback : Sendable

    extension PromptFeedback: Decodable

A metadata struct containing any feedback the model had on the prompt it was provided.
- `


  ### [BlockReason](https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/PromptFeedback/BlockReason.html)


  ` A type describing possible reasons to block a prompt.

  #### Declaration

  Swift

      @available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
      public struct BlockReason : DecodableProtoEnum, Hashable, Sendable

- `


  ### [blockReason](https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/PromptFeedback#/s:16FirebaseVertexAI14PromptFeedbackV11blockReasonAC05BlockG0VSgvp)


  ` The reason a prompt was blocked, if it was blocked.

  #### Declaration

  Swift

      public let blockReason: https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/PromptFeedback/BlockReason.html?

- `


  ### [blockReasonMessage](https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/PromptFeedback#/s:16FirebaseVertexAI14PromptFeedbackV18blockReasonMessageSSSgvp)


  ` A human-readable description of the `https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/PromptFeedback.html#/s:16FirebaseVertexAI14PromptFeedbackV11blockReasonAC05BlockG0VSgvp`.

  #### Declaration

  Swift

      public let blockReasonMessage: String?

- `


  ### [safetyRatings](https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/PromptFeedback#/s:16FirebaseVertexAI14PromptFeedbackV13safetyRatingsSayAA12SafetyRatingVGvp)


  ` The safety ratings of the prompt.

  #### Declaration

  Swift

      public let safetyRatings: [https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/SafetyRating.html]

- `


  ### [init(blockReason:blockReasonMessage:safetyRatings:)](https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/PromptFeedback#/s:16FirebaseVertexAI14PromptFeedbackV11blockReason0fG7Message13safetyRatingsA2C05BlockG0VSg_SSSgSayAA12SafetyRatingVGtcfc)


  ` Initializer for SwiftUI previews or tests.

  #### Declaration

  Swift

      public init(blockReason: https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/PromptFeedback/BlockReason.html?, blockReasonMessage: String? = nil,
                  safetyRatings: [https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/SafetyRating.html])

[## Codable Conformances](https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/PromptFeedback#/Codable-Conformances)

- `


  ### [init(from:)](https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/PromptFeedback#/s:Se4fromxs7Decoder_p_tKcfc)


  `

  #### Declaration

  Swift

      public init(from decoder: Decoder) throws