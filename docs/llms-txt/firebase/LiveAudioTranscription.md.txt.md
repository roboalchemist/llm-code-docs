# Source: https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/LiveAudioTranscription.md.txt

# FirebaseAILogic Framework Reference

# LiveAudioTranscription

    @available(iOS 15.0, macOS 12.0, tvOS 15.0, *)
    @available(watchOS, unavailable)
    public struct LiveAudioTranscription : Sendable

Text transcription of some audio form during a live interaction with the model.
- `


  ### [text](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/LiveAudioTranscription#/s:15FirebaseAILogic22LiveAudioTranscriptionV4textSSSgvp)


  ` Text representing the model's interpretation of what the audio said.

  #### Declaration

  Swift

      public var text: String? { get }