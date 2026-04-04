# Source: https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/PromptFeedback/BlockReason.md.txt

# FirebaseAILogic Framework Reference

# BlockReason

    @available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
    public struct BlockReason : DecodableProtoEnum, Hashable, Sendable

A type describing possible reasons to block a prompt.
- `


  ### [safety](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/PromptFeedback/BlockReason#/s:15FirebaseAILogic14PromptFeedbackV11BlockReasonV6safetyAEvpZ)


  ` The prompt was blocked because it was deemed unsafe.

  #### Declaration

  Swift

      public static let safety: https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/PromptFeedback.html.BlockReason

- `


  ### [other](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/PromptFeedback/BlockReason#/s:15FirebaseAILogic14PromptFeedbackV11BlockReasonV5otherAEvpZ)


  ` All other block reasons.

  #### Declaration

  Swift

      public static let other: https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/PromptFeedback.html.BlockReason

- `


  ### [blocklist](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/PromptFeedback/BlockReason#/s:15FirebaseAILogic14PromptFeedbackV11BlockReasonV9blocklistAEvpZ)


  ` The prompt was blocked because it contained terms from the terminology blocklist.

  #### Declaration

  Swift

      public static let blocklist: https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/PromptFeedback.html.BlockReason

- `


  ### [prohibitedContent](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/PromptFeedback/BlockReason#/s:15FirebaseAILogic14PromptFeedbackV11BlockReasonV17prohibitedContentAEvpZ)


  ` The prompt was blocked due to prohibited content.

  #### Declaration

  Swift

      public static let prohibitedContent: https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/PromptFeedback.html.BlockReason

- `


  ### [rawValue](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/PromptFeedback/BlockReason#/s:15FirebaseAILogic14PromptFeedbackV11BlockReasonV8rawValueSSvp)


  ` Returns the raw string representation of the `BlockReason` value.
  Note

  This value directly corresponds to the values in the [REST
  API](https://cloud.google.com/vertex-ai/docs/reference/rest/v1beta1/GenerateContentResponse#BlockedReason).

  #### Declaration

  Swift

      public let rawValue: String