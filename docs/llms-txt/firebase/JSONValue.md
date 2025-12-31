# Source: https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Enums/JSONValue.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Enums/JSONValue.md.txt

# FirebaseAI Framework Reference

# JSONValue

    @available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
    public enum JSONValue : Sendable

    extension JSONValue: Decodable

    extension JSONValue: Encodable

    extension JSONValue: Equatable

Represents a value in one of JSON's data types.

This may be decoded from, or encoded to, a
[`google.protobuf.Value`](https://protobuf.dev/reference/protobuf/google.protobuf/#value).
- `
  ``
  ``
  `

  ### [null](https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Enums/JSONValue#/s:10FirebaseAI9JSONValueO4nullyA2CmF)

  `
  `  
  A `null` value.  

  #### Declaration

  Swift  

      case null

- `
  ``
  ``
  `

  ### [number(_:)](https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Enums/JSONValue#/s:10FirebaseAI9JSONValueO6numberyACSdcACmF)

  `
  `  
  A numeric value.  

  #### Declaration

  Swift  

      case number(Double)

- `
  ``
  ``
  `

  ### [string(_:)](https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Enums/JSONValue#/s:10FirebaseAI9JSONValueO6stringyACSScACmF)

  `
  `  
  A string value.  

  #### Declaration

  Swift  

      case string(String)

- `
  ``
  ``
  `

  ### [bool(_:)](https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Enums/JSONValue#/s:10FirebaseAI9JSONValueO4boolyACSbcACmF)

  `
  `  
  A boolean value.  

  #### Declaration

  Swift  

      case bool(Bool)

- `
  ``
  ``
  `

  ### [object(_:)](https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Enums/JSONValue#/s:10FirebaseAI9JSONValueO6objectyACSDySSACGcACmF)

  `
  `  
  A JSON object.  

  #### Declaration

  Swift  

      case object(https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Typealiases.html#/s:10FirebaseAI10JSONObjecta)

- `
  ``
  ``
  `

  ### [array(_:)](https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Enums/JSONValue#/s:10FirebaseAI9JSONValueO5arrayyACSayACGcACmF)

  `
  `  
  An array of `JSONValue`s.  

  #### Declaration

  Swift  

      case array([JSONValue])

- `
  ``
  ``
  `

  ### [init(from:)](https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Enums/JSONValue#/s:Se4fromxs7Decoder_p_tKcfc)

  `
  `  

  #### Declaration

  Swift  

      public init(from decoder: Decoder) throws

- `
  ``
  ``
  `

  ### [encode(to:)](https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Enums/JSONValue#/s:SE6encode2toys7Encoder_p_tKF)

  `
  `  

  #### Declaration

  Swift  

      public func encode(to encoder: Encoder) throws