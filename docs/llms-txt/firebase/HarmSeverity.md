# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/HarmSeverity.md.txt

# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/HarmSeverity.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/SafetyRating/HarmSeverity.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/HarmSeverity.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/HarmSeverity.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/SafetyRating/HarmSeverity.md.txt

# FirebaseAI Framework Reference

# HarmSeverity

    @available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
    public struct HarmSeverity : DecodableProtoEnum, Hashable, Sendable

The magnitude of how harmful a model response might be for the respective [HarmCategory](https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/HarmCategory.html).
- `
  ``
  ``
  `

  ### [negligible](https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/SafetyRating/HarmSeverity#/s:10FirebaseAI12SafetyRatingV12HarmSeverityV10negligibleAEvpZ)

  `
  `  
  Negligible level of harm severity.  

  #### Declaration

  Swift  

      public static let negligible: https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/SafetyRating.html.HarmSeverity

- `
  ``
  ``
  `

  ### [low](https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/SafetyRating/HarmSeverity#/s:10FirebaseAI12SafetyRatingV12HarmSeverityV3lowAEvpZ)

  `
  `  
  Low level of harm severity.  

  #### Declaration

  Swift  

      public static let low: https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/SafetyRating.html.HarmSeverity

- `
  ``
  ``
  `

  ### [medium](https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/SafetyRating/HarmSeverity#/s:10FirebaseAI12SafetyRatingV12HarmSeverityV6mediumAEvpZ)

  `
  `  
  Medium level of harm severity.  

  #### Declaration

  Swift  

      public static let medium: https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/SafetyRating.html.HarmSeverity

- `
  ``
  ``
  `

  ### [high](https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/SafetyRating/HarmSeverity#/s:10FirebaseAI12SafetyRatingV12HarmSeverityV4highAEvpZ)

  `
  `  
  High level of harm severity.  

  #### Declaration

  Swift  

      public static let high: https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/SafetyRating.html.HarmSeverity

- `
  ``
  ``
  `

  ### [rawValue](https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/SafetyRating/HarmSeverity#/s:10FirebaseAI12SafetyRatingV12HarmSeverityV8rawValueSSvp)

  `
  `  
  Returns the raw string representation of the `HarmSeverity` value.  
  Note

  This value directly corresponds to the values in the [REST
  API](https://cloud.google.com/vertex-ai/docs/reference/rest/v1beta1/GenerateContentResponse#HarmSeverity).  

  #### Declaration

  Swift  

      public let rawValue: String