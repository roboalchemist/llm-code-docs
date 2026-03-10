# Source: https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/SafetySetting/HarmBlockMethod.md.txt

# FirebaseAILogic Framework Reference

# HarmBlockMethod

    @available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
    public struct HarmBlockMethod : EncodableProtoEnum, Sendable

The method of computing whether the `https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/SafetySetting/HarmBlockThreshold.html` has been exceeded.
- `


  ### [severity](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/SafetySetting/HarmBlockMethod#/s:15FirebaseAILogic13SafetySettingV15HarmBlockMethodV8severityAEvpZ)


  ` Use both probability and severity scores.

  #### Declaration

  Swift

      public static let severity: https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/SafetySetting.html.HarmBlockMethod

- `


  ### [probability](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/SafetySetting/HarmBlockMethod#/s:15FirebaseAILogic13SafetySettingV15HarmBlockMethodV11probabilityAEvpZ)


  ` Use only the probability score.

  #### Declaration

  Swift

      public static let probability: https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/SafetySetting.html.HarmBlockMethod