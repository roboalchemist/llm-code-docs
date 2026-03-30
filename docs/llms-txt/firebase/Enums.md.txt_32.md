# Source: https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Enums.md.txt

# FirebaseVertexAI Framework Reference

# Enumerations

The following enumerations are available globally.
- `


  ### [GenerateContentError](https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Enums/GenerateContentError)


  ` Errors that occur when generating content from a model.

  #### Declaration

  Swift

      @available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
      public enum GenerateContentError : Error

- `


  ### [JSONValue](https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Enums/JSONValue)


  ` Represents a value in one of JSON's data types.

  This may be decoded from, or encoded to, a
  [`google.protobuf.Value`](https://protobuf.dev/reference/protobuf/google.protobuf/#value).

  #### Declaration

  Swift

      @available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
      public enum JSONValue : Sendable

      extension JSONValue: Decodable

      extension JSONValue: Encodable

      extension JSONValue: Equatable