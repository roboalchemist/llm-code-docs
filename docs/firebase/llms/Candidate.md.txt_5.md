# Source: https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/Candidate.md.txt

# FirebaseAILogic Framework Reference

# Candidate

    @available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
    public struct Candidate : Sendable

    extension Candidate: Decodable

A struct representing a possible reply to a content generation prompt. Each content generation
prompt may produce multiple candidate responses.
- `


  ### [content](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/Candidate#/s:15FirebaseAILogic9CandidateV7contentAA12ModelContentVvp)


  ` The response's content.

  #### Declaration

  Swift

      public let content: https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/ModelContent.html

- `


  ### [safetyRatings](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/Candidate#/s:15FirebaseAILogic9CandidateV13safetyRatingsSayAA12SafetyRatingVGvp)


  ` The safety rating of the response content.

  #### Declaration

  Swift

      public let safetyRatings: [https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/SafetyRating.html]

- `


  ### [finishReason](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/Candidate#/s:15FirebaseAILogic9CandidateV12finishReasonAA06FinishE0VSgvp)


  ` The reason the model stopped generating content, if it exists; for example, if the model
  generated a predefined stop sequence.

  #### Declaration

  Swift

      public let finishReason: https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/FinishReason.html?

- `


  ### [citationMetadata](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/Candidate#/s:15FirebaseAILogic9CandidateV16citationMetadataAA08CitationE0VSgvp)


  ` Cited works in the model's response content, if it exists.

  #### Declaration

  Swift

      public let citationMetadata: https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/CitationMetadata.html?

- `


  ### [groundingMetadata](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/Candidate#/s:15FirebaseAILogic9CandidateV17groundingMetadataAA09GroundingE0VSgvp)


  ` Undocumented

  #### Declaration

  Swift

      public let groundingMetadata: https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/GroundingMetadata.html?

- `


  ### [urlContextMetadata](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/Candidate#/s:15FirebaseAILogic9CandidateV18urlContextMetadataAA010URLContextF0VSgvp)


  ` Metadata related to the `URLContext` tool.

  #### Declaration

  Swift

      public let urlContextMetadata: https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/URLContextMetadata.html?

- `


  ### [init(content:safetyRatings:finishReason:citationMetadata:groundingMetadata:urlContextMetadata:)](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/Candidate#/s:15FirebaseAILogic9CandidateV7content13safetyRatings12finishReason16citationMetadata09groundingJ0010urlContextJ0AcA12ModelContentV_SayAA12SafetyRatingVGAA06FinishH0VSgAA08CitationJ0VSgAA09GroundingJ0VSgAA010URLContextJ0VSgtcfc)


  ` Initializer for SwiftUI previews or tests.

  #### Declaration

  Swift

      public init(content: https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/ModelContent.html, safetyRatings: [https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/SafetyRating.html], finishReason: https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/FinishReason.html?,
                  citationMetadata: https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/CitationMetadata.html?, groundingMetadata: https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/GroundingMetadata.html? = nil,
                  urlContextMetadata: https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/URLContextMetadata.html? = nil)

[## Codable Conformances](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/Candidate#/Codable-Conformances)

- `


  ### [init(from:)](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/Candidate#/s:15FirebaseAILogic9CandidateV4fromACs7Decoder_p_tKcfc)


  ` Initializes a response from a decoder. Used for decoding server responses; not for public
  use.

  #### Declaration

  Swift

      public init(from decoder: Decoder) throws