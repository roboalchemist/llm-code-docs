# Source: https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/GenerateContentResponse.md.txt

# FirebaseAILogic Framework Reference

# GenerateContentResponse

    @available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
    public struct GenerateContentResponse : Sendable

    extension GenerateContentResponse: Decodable

The model's response to a generate content request.
- `


  ### [UsageMetadata](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/GenerateContentResponse/UsageMetadata.html)


  ` Token usage metadata for processing the generate content request.

  #### Declaration

  Swift

      @available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
      public struct UsageMetadata : Sendable

      extension https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/GenerateContentResponse.html.UsageMetadata: Decodable

- `


  ### [candidates](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/GenerateContentResponse#/s:15FirebaseAILogic23GenerateContentResponseV10candidatesSayAA9CandidateVGvp)


  ` A list of candidate response content, ordered from best to worst.

  #### Declaration

  Swift

      public let candidates: [https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/Candidate.html]

- `


  ### [promptFeedback](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/GenerateContentResponse#/s:15FirebaseAILogic23GenerateContentResponseV14promptFeedbackAA06PromptG0VSgvp)


  ` A value containing the safety ratings for the response, or, if the request was blocked, a
  reason for blocking the request.

  #### Declaration

  Swift

      public let promptFeedback: https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/PromptFeedback.html?

- `


  ### [usageMetadata](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/GenerateContentResponse#/s:15FirebaseAILogic23GenerateContentResponseV13usageMetadataAC05UsageG0VSgvp)


  ` Token usage metadata for processing the generate content request.

  #### Declaration

  Swift

      public let usageMetadata: https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/GenerateContentResponse/UsageMetadata.html?

- `


  ### [text](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/GenerateContentResponse#/s:15FirebaseAILogic23GenerateContentResponseV4textSSSgvp)


  ` The response's content as text, if it exists.
  Note
  This does not include thought summaries; see `https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/GenerateContentResponse.html#/s:15FirebaseAILogic23GenerateContentResponseV14thoughtSummarySSSgvp` for more details.

  #### Declaration

  Swift

      public var text: String? { get }

- `


  ### [thoughtSummary](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/GenerateContentResponse#/s:15FirebaseAILogic23GenerateContentResponseV14thoughtSummarySSSgvp)


  ` A summary of the model's thinking process, if available.
  Important
  Thought summaries are only available when `includeThoughts` is enabled in the `https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/ThinkingConfig.html`. For more information, see the [Thinking](https://firebase.google.com/docs/ai-logic/thinking) documentation.

  #### Declaration

  Swift

      public var thoughtSummary: String? { get }

- `


  ### [functionCalls](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/GenerateContentResponse#/s:15FirebaseAILogic23GenerateContentResponseV13functionCallsSayAA16FunctionCallPartVGvp)


  ` Returns function calls found in any `https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Protocols/Part.html`s of the first candidate of the response, if any.

  #### Declaration

  Swift

      public var functionCalls: [https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/FunctionCallPart.html] { get }

- `


  ### [inlineDataParts](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/GenerateContentResponse#/s:15FirebaseAILogic23GenerateContentResponseV15inlineDataPartsSayAA06InlineG4PartVGvp)


  ` Returns inline data parts found in any `https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Protocols/Part.html`s of the first candidate of the response, if any.

  #### Declaration

  Swift

      public var inlineDataParts: [https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/InlineDataPart.html] { get }

- `


  ### [init(candidates:promptFeedback:usageMetadata:)](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/GenerateContentResponse#/s:15FirebaseAILogic23GenerateContentResponseV10candidates14promptFeedback13usageMetadataACSayAA9CandidateVG_AA06PromptH0VSgAC05UsageJ0VSgtcfc)


  ` Initializer for SwiftUI previews or tests.

  #### Declaration

  Swift

      public init(candidates: [https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/Candidate.html], promptFeedback: https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/PromptFeedback.html? = nil,
                  usageMetadata: https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/GenerateContentResponse/UsageMetadata.html? = nil)

[## Codable Conformances](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/GenerateContentResponse#/Codable-Conformances)

- `


  ### [init(from:)](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/GenerateContentResponse#/s:Se4fromxs7Decoder_p_tKcfc)


  `

  #### Declaration

  Swift

      public init(from decoder: Decoder) throws