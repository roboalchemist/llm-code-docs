# Source: https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/ModalityTokenCount.md.txt

# FirebaseAILogic Framework Reference

# ModalityTokenCount

    @available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
    public struct ModalityTokenCount : Sendable

    extension ModalityTokenCount: Decodable

Represents token counting info for a single modality.
- `


  ### [modality](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/ModalityTokenCount#/s:15FirebaseAILogic18ModalityTokenCountV8modalityAA07ContentC0Vvp)


  ` The modality associated with this token count.

  #### Declaration

  Swift

      public let modality: https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/ContentModality.html

- `


  ### [tokenCount](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/ModalityTokenCount#/s:15FirebaseAILogic18ModalityTokenCountV05tokenE0Sivp)


  ` The number of tokens counted.

  #### Declaration

  Swift

      public let tokenCount: Int

[## Codable Conformances](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/ModalityTokenCount#/Codable-Conformances)

- `


  ### [init(from:)](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/ModalityTokenCount#/s:Se4fromxs7Decoder_p_tKcfc)


  `

  #### Declaration

  Swift

      public init(from decoder: any Decoder) throws