# Source: https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/LiveServerMessage.md.txt

# FirebaseAILogic Framework Reference

# LiveServerMessage

    @available(iOS 15.0, macOS 12.0, tvOS 15.0, *)
    @available(watchOS, unavailable)
    public struct LiveServerMessage : Sendable

Update from the server, generated from the model in response to client messages.
- `


  ### [Payload](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/LiveServerMessage/Payload.html)


  ` The type of message sent from the server.
  Important
  Potential future additions to the `Payload` enum may not trigger a semantic versioning major version update. If ensure forward compatibility, client code should avoid exhaustive switch statements over this enum by adding a default case.

  #### Declaration

  Swift

      public enum Payload : Sendable

- `


  ### [payload](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/LiveServerMessage#/s:15FirebaseAILogic17LiveServerMessageV7payloadAC7PayloadOvp)


  ` The message sent from the server.

  #### Declaration

  Swift

      public let payload: https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/LiveServerMessage/Payload.html

- `


  ### [usageMetadata](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/LiveServerMessage#/s:15FirebaseAILogic17LiveServerMessageV13usageMetadataAA23GenerateContentResponseV05UsageG0VSgvp)


  ` Metadata on the usage of the cached content.

  #### Declaration

  Swift

      public var usageMetadata: https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/GenerateContentResponse.html.UsageMetadata? { get }