# Source: https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/SafetyRating/HarmProbability.md.txt

# FirebaseAILogic Framework Reference

# HarmProbability

    @available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
    public struct HarmProbability : DecodableProtoEnum, Hashable, Sendable

The probability that a given model output falls under a harmful content category.
Note

This does not indicate the severity of harm for a piece of content.
- `


  ### [negligible](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/SafetyRating/HarmProbability#/s:15FirebaseAILogic12SafetyRatingV15HarmProbabilityV10negligibleAEvpZ)


  ` The probability is zero or close to zero.

  For benign content, the probability across all categories will be this value.

  #### Declaration

  Swift

      public static let negligible: https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/SafetyRating.html.HarmProbability

- `


  ### [low](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/SafetyRating/HarmProbability#/s:15FirebaseAILogic12SafetyRatingV15HarmProbabilityV3lowAEvpZ)


  ` The probability is small but non-zero.

  #### Declaration

  Swift

      public static let low: https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/SafetyRating.html.HarmProbability

- `


  ### [medium](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/SafetyRating/HarmProbability#/s:15FirebaseAILogic12SafetyRatingV15HarmProbabilityV6mediumAEvpZ)


  ` The probability is moderate.

  #### Declaration

  Swift

      public static let medium: https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/SafetyRating.html.HarmProbability

- `


  ### [high](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/SafetyRating/HarmProbability#/s:15FirebaseAILogic12SafetyRatingV15HarmProbabilityV4highAEvpZ)


  ` The probability is high.

  The content described is very likely harmful.

  #### Declaration

  Swift

      public static let high: https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/SafetyRating.html.HarmProbability

- `


  ### [rawValue](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/SafetyRating/HarmProbability#/s:15FirebaseAILogic12SafetyRatingV15HarmProbabilityV8rawValueSSvp)


  ` Returns the raw string representation of the `HarmProbability` value.
  Note

  This value directly corresponds to the values in the [REST
  API](https://cloud.google.com/vertex-ai/docs/reference/rest/v1beta1/GenerateContentResponse#SafetyRating).

  #### Declaration

  Swift

      public let rawValue: String