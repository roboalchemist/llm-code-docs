# Source: https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/SpeechConfig.md.txt

# FirebaseAILogic Framework Reference

# SpeechConfig

    @available(iOS 15.0, macOS 12.0, tvOS 15.0, *)
    @available(watchOS, unavailable)
    public struct SpeechConfig : Sendable

Configuration for controlling the voice of the model during conversation.
- `


  ### [init(voiceName:languageCode:)](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/SpeechConfig#/s:15FirebaseAILogic12SpeechConfigV9voiceName12languageCodeACSS_SSSgtcfc)


  ` Creates a new `SpeechConfig` value.

  #### Declaration

  Swift

      public init(voiceName: String, languageCode: String? = nil)

  #### Parameters

  |---|---|
  | ` voiceName ` | The name of the prebuilt voice to be used for the model's speech response. |
  | ` languageCode ` | ISO-639 language code to use when parsing text sent from the client, instead of audio. By default, the model will attempt to detect the input language automatically. |