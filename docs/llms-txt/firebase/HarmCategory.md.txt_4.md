# Source: https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/HarmCategory.md.txt

# FirebaseAILogic Framework Reference

# HarmCategory

    @available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
    public struct HarmCategory : CodableProtoEnum, Hashable, Sendable

Categories describing the potential harm a piece of content may pose.
- `


  ### [harassment](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/HarmCategory#/s:15FirebaseAILogic12HarmCategoryV10harassmentACvpZ)


  ` Harassment content.

  #### Declaration

  Swift

      public static let harassment: HarmCategory

- `


  ### [hateSpeech](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/HarmCategory#/s:15FirebaseAILogic12HarmCategoryV10hateSpeechACvpZ)


  ` Negative or harmful comments targeting identity and/or protected attributes.

  #### Declaration

  Swift

      public static let hateSpeech: HarmCategory

- `


  ### [sexuallyExplicit](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/HarmCategory#/s:15FirebaseAILogic12HarmCategoryV16sexuallyExplicitACvpZ)


  ` Contains references to sexual acts or other lewd content.

  #### Declaration

  Swift

      public static let sexuallyExplicit: HarmCategory

- `


  ### [dangerousContent](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/HarmCategory#/s:15FirebaseAILogic12HarmCategoryV16dangerousContentACvpZ)


  ` Promotes or enables access to harmful goods, services, or activities.

  #### Declaration

  Swift

      public static let dangerousContent: HarmCategory

- `


  ### [civicIntegrity](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/HarmCategory#/s:15FirebaseAILogic12HarmCategoryV14civicIntegrityACvpZ)


  ` Content that may be used to harm civic integrity.

  #### Declaration

  Swift

      public static let civicIntegrity: HarmCategory

- `


  ### [rawValue](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/HarmCategory#/s:15FirebaseAILogic12HarmCategoryV8rawValueSSvp)


  ` Returns the raw string representation of the `HarmCategory` value.
  Note

  This value directly corresponds to the values in the
  [REST API](https://cloud.google.com/vertex-ai/docs/reference/rest/v1beta1/HarmCategory).

  #### Declaration

  Swift

      public let rawValue: String