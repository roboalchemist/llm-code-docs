# Source: https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Protocols.md.txt

# FirebaseVertexAI Framework Reference

# Protocols

The following protocols are available globally.
- `


  ### [PartsRepresentable](https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Protocols/PartsRepresentable)


  ` A protocol describing any data that could be serialized to model-interpretable input data,
  where the serialization process cannot fail with an error.

  #### Declaration

  Swift

      @available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
      public protocol PartsRepresentable

- `


  ### [Part](https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Protocols/Part)


  ` A discrete piece of data in a media format interpretable by an AI model.

  Within a single value of `Part`, different data types may not mix.

  #### Declaration

  Swift

      @available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
      public protocol Part : https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Protocols/PartsRepresentable, Decodable, Encodable, Equatable, Sendable