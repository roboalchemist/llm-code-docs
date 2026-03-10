# Source: https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/ModalityTokenCount.md.txt

# FirebaseVertexAI Framework Reference

# ModalityTokenCount

    @available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
    public struct ModalityTokenCount : Sendable

    extension ModalityTokenCount: Decodable

Represents token counting info for a single modality.
- `


  ### [modality](https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/ModalityTokenCount#/s:16FirebaseVertexAI18ModalityTokenCountV8modalityAA07ContentD0Vvp)


  ` The modality associated with this token count.

  #### Declaration

  Swift

      public let modality: https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/ContentModality.html

- `


  ### [tokenCount](https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/ModalityTokenCount#/s:16FirebaseVertexAI18ModalityTokenCountV05tokenF0Sivp)


  ` The number of tokens counted.

  #### Declaration

  Swift

      public let tokenCount: Int