# Source: https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/SafetyRating.md.txt

# FirebaseVertexAI Framework Reference

# SafetyRating

    @available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
    public struct SafetyRating : Equatable, Hashable, Sendable

    extension SafetyRating: Decodable

A type defining potentially harmful media categories and their model-assigned ratings. A value
of this type may be assigned to a category for every model-generated response, not just
responses that exceed a certain threshold.
- `


  ### [category](https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/SafetyRating#/s:16FirebaseVertexAI12SafetyRatingV8categoryAA12HarmCategoryVvp)


  ` The category describing the potential harm a piece of content may pose.

  See `https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/HarmCategory.html` for a list of possible values.

  #### Declaration

  Swift

      public let category: https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/HarmCategory.html

- `


  ### [probability](https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/SafetyRating#/s:16FirebaseVertexAI12SafetyRatingV11probabilityAC15HarmProbabilityVvp)


  ` The model-generated probability that the content falls under the specified harm `https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/SafetyRating.html#/s:16FirebaseVertexAI12SafetyRatingV8categoryAA12HarmCategoryVvp`.

  See `https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/SafetyRating/HarmProbability.html` for a list of possible values. This is a discretized representation
  of the `https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/SafetyRating.html#/s:16FirebaseVertexAI12SafetyRatingV16probabilityScoreSfvp`.
  Important

  This does not indicate the severity of harm for a piece of content.

  #### Declaration

  Swift

      public let probability: https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/SafetyRating/HarmProbability.html

- `


  ### [probabilityScore](https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/SafetyRating#/s:16FirebaseVertexAI12SafetyRatingV16probabilityScoreSfvp)


  ` The confidence score that the response is associated with the corresponding harm `https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/SafetyRating.html#/s:16FirebaseVertexAI12SafetyRatingV8categoryAA12HarmCategoryVvp`.

  The probability safety score is a confidence score between 0.0 and 1.0, rounded to one decimal
  place; it is discretized into a `https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/SafetyRating/HarmProbability.html` in `https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/SafetyRating.html#/s:16FirebaseVertexAI12SafetyRatingV11probabilityAC15HarmProbabilityVvp`. See [probability
  scores](https://cloud.google.com/vertex-ai/generative-ai/docs/multimodal/configure-safety-filters#comparison_of_probability_scores_and_severity_scores)
  in the Google Cloud documentation for more details.

  #### Declaration

  Swift

      public let probabilityScore: Float

- `


  ### [severity](https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/SafetyRating#/s:16FirebaseVertexAI12SafetyRatingV8severityAC12HarmSeverityVvp)


  ` The severity reflects the magnitude of how harmful a model response might be.

  See `https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/SafetyRating/HarmSeverity.html` for a list of possible values. This is a discretized representation of
  the `https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/SafetyRating.html#/s:16FirebaseVertexAI12SafetyRatingV13severityScoreSfvp`.

  #### Declaration

  Swift

      public let severity: https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/SafetyRating/HarmSeverity.html

- `


  ### [severityScore](https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/SafetyRating#/s:16FirebaseVertexAI12SafetyRatingV13severityScoreSfvp)


  ` The severity score is the magnitude of how harmful a model response might be.

  The severity score ranges from 0.0 to 1.0, rounded to one decimal place; it is discretized
  into a `https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/SafetyRating/HarmSeverity.html` in `https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/SafetyRating.html#/s:16FirebaseVertexAI12SafetyRatingV8severityAC12HarmSeverityVvp`. See [severity scores](https://cloud.google.com/vertex-ai/generative-ai/docs/multimodal/configure-safety-filters#comparison_of_probability_scores_and_severity_scores)
  in the Google Cloud documentation for more details.

  #### Declaration

  Swift

      public let severityScore: Float

- `


  ### [blocked](https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/SafetyRating#/s:16FirebaseVertexAI12SafetyRatingV7blockedSbvp)


  ` If true, the response was blocked.

  #### Declaration

  Swift

      public let blocked: Bool

- `


  ### [init(category:probability:probabilityScore:severity:severityScore:blocked:)](https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/SafetyRating#/s:16FirebaseVertexAI12SafetyRatingV8category11probability0G5Score8severity0iH07blockedAcA12HarmCategoryV_AC0K11ProbabilityVSfAC0K8SeverityVSfSbtcfc)


  ` Initializes a new `SafetyRating` instance with the given category and probability.
  Use this initializer for SwiftUI previews or tests.

  #### Declaration

  Swift

      public init(category: https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/HarmCategory.html,
                  probability: https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/SafetyRating/HarmProbability.html,
                  probabilityScore: Float,
                  severity: https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/SafetyRating/HarmSeverity.html,
                  severityScore: Float,
                  blocked: Bool)

- `


  ### [HarmProbability](https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/SafetyRating/HarmProbability.html)


  ` The probability that a given model output falls under a harmful content category.
  Note

  This does not indicate the severity of harm for a piece of content.

  #### Declaration

  Swift

      @available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
      public struct HarmProbability : DecodableProtoEnum, Hashable, Sendable

- `


  ### [HarmSeverity](https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/SafetyRating/HarmSeverity.html)


  ` The magnitude of how harmful a model response might be for the respective `https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/HarmCategory.html`.

  #### Declaration

  Swift

      @available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
      public struct HarmSeverity : DecodableProtoEnum, Hashable, Sendable

[## Codable Conformances](https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/SafetyRating#/Codable-Conformances)

- `


  ### [init(from:)](https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/SafetyRating#/s:Se4fromxs7Decoder_p_tKcfc)


  `

  #### Declaration

  Swift

      public init(from decoder: any Decoder) throws