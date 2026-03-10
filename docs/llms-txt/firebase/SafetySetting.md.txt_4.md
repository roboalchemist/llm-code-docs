# Source: https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/SafetySetting.md.txt

# FirebaseAILogic Framework Reference

# SafetySetting

    @available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
    public struct SafetySetting : Sendable

    extension SafetySetting: Encodable

A type used to specify a threshold for harmful content, beyond which the model will return a
fallback response instead of generated content.

See [safety settings for Gemini
models](https://firebase.google.com/docs/vertex-ai/safety-settings?platform=ios#gemini) for
more details.
- `


  ### [HarmBlockThreshold](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/SafetySetting/HarmBlockThreshold.html)


  ` Block at and beyond a specified `https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/SafetyRating/HarmProbability.html`.

  #### Declaration

  Swift

      public struct HarmBlockThreshold : EncodableProtoEnum, Sendable

      extension https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/SafetySetting.html.HarmBlockThreshold: Encodable

- `


  ### [HarmBlockMethod](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/SafetySetting/HarmBlockMethod.html)


  ` The method of computing whether the `https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/SafetySetting/HarmBlockThreshold.html` has been exceeded.

  #### Declaration

  Swift

      @available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
      public struct HarmBlockMethod : EncodableProtoEnum, Sendable

- `


  ### [harmCategory](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/SafetySetting#/s:15FirebaseAILogic13SafetySettingV12harmCategoryAA04HarmF0Vvp)


  ` The category this safety setting should be applied to.

  #### Declaration

  Swift

      public let harmCategory: https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/HarmCategory.html

- `


  ### [threshold](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/SafetySetting#/s:15FirebaseAILogic13SafetySettingV9thresholdAC18HarmBlockThresholdVvp)


  ` The threshold describing what content should be blocked.

  #### Declaration

  Swift

      public let threshold: https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/SafetySetting/HarmBlockThreshold.html

- `


  ### [method](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/SafetySetting#/s:15FirebaseAILogic13SafetySettingV6methodAC15HarmBlockMethodVSgvp)


  ` The method of computing whether the `https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/SafetySetting.html#/s:15FirebaseAILogic13SafetySettingV9thresholdAC18HarmBlockThresholdVvp` has been exceeded.

  #### Declaration

  Swift

      public let method: https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/SafetySetting/HarmBlockMethod.html?

- `


  ### [init(harmCategory:threshold:method:)](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/SafetySetting#/s:15FirebaseAILogic13SafetySettingV12harmCategory9threshold6methodAcA04HarmF0V_AC0I14BlockThresholdVAC0iJ6MethodVSgtcfc)


  ` Initializes a new safety setting with the given category and threshold.

  #### Declaration

  Swift

      public init(harmCategory: https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/HarmCategory.html, threshold: https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/SafetySetting/HarmBlockThreshold.html,
                  method: https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/SafetySetting/HarmBlockMethod.html? = nil)

  #### Parameters

  |---|---|
  | ` harmCategory ` | The category this safety setting should be applied to. |
  | ` threshold ` | The threshold describing what content should be blocked. |
  | ` method ` | The method of computing whether the threshold has been exceeded; if not specified, the default method is `https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/SafetySetting/HarmBlockMethod.html#/s:15FirebaseAILogic13SafetySettingV15HarmBlockMethodV8severityAEvpZ` for most models. See [harm block methods](https://cloud.google.com/vertex-ai/generative-ai/docs/multimodal/configure-safety-filters#how_to_configure_safety_filters) in the Google Cloud documentation for more details. \> Note: For models older than `gemini-1.5-flash` and `gemini-1.5-pro`, the default method \> is `https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/SafetySetting/HarmBlockMethod.html#/s:15FirebaseAILogic13SafetySettingV15HarmBlockMethodV11probabilityAEvpZ`. |