# Source: https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/SafetySetting/HarmBlockThreshold.md.txt

# FirebaseVertexAI Framework Reference

# HarmBlockThreshold

    public struct HarmBlockThreshold : EncodableProtoEnum, Sendable

    extension https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/SafetySetting.html.HarmBlockThreshold: Encodable

Block at and beyond a specified `https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/SafetyRating/HarmProbability.html`.
- `


  ### [blockLowAndAbove](https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/SafetySetting/HarmBlockThreshold#/s:16FirebaseVertexAI13SafetySettingV18HarmBlockThresholdV16blockLowAndAboveAEvpZ)


  ` Content with `.negligible` will be allowed.

  #### Declaration

  Swift

      public static let blockLowAndAbove: https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/SafetySetting.html.HarmBlockThreshold

- `


  ### [blockMediumAndAbove](https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/SafetySetting/HarmBlockThreshold#/s:16FirebaseVertexAI13SafetySettingV18HarmBlockThresholdV19blockMediumAndAboveAEvpZ)


  ` Content with `.negligible` and `.low` will be allowed.

  #### Declaration

  Swift

      public static let blockMediumAndAbove: https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/SafetySetting.html.HarmBlockThreshold

- `


  ### [blockOnlyHigh](https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/SafetySetting/HarmBlockThreshold#/s:16FirebaseVertexAI13SafetySettingV18HarmBlockThresholdV13blockOnlyHighAEvpZ)


  ` Content with `.negligible`, `.low`, and `.medium` will be allowed.

  #### Declaration

  Swift

      public static let blockOnlyHigh: https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/SafetySetting.html.HarmBlockThreshold

- `


  ### [blockNone](https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/SafetySetting/HarmBlockThreshold#/s:16FirebaseVertexAI13SafetySettingV18HarmBlockThresholdV9blockNoneAEvpZ)


  ` All content will be allowed.

  #### Declaration

  Swift

      public static let blockNone: https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/SafetySetting.html.HarmBlockThreshold

- `


  ### [off](https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/SafetySetting/HarmBlockThreshold#/s:16FirebaseVertexAI13SafetySettingV18HarmBlockThresholdV3offAEvpZ)


  ` Turn off the safety filter.

  #### Declaration

  Swift

      public static let off: https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/SafetySetting.html.HarmBlockThreshold