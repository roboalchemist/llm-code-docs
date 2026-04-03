# Source: https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Classes/Schema/IntegerFormat.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Classes/Schema/IntegerFormat.md.txt

# FirebaseAI Framework Reference

# IntegerFormat

    @available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
    public struct IntegerFormat : EncodableProtoEnum, Sendable

Modifiers describing the expected format of an integer [Schema](https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Classes/Schema.html).
- `
  ``
  ``
  `

  ### [int32](https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Classes/Schema/IntegerFormat#/s:10FirebaseAI6SchemaC13IntegerFormatV5int32AEvpZ)

  `
  `  
  A 32-bit signed integer.  

  #### Declaration

  Swift  

      public static let int32: https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Classes/Schema.html.IntegerFormat

- `
  ``
  ``
  `

  ### [int64](https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Classes/Schema/IntegerFormat#/s:10FirebaseAI6SchemaC13IntegerFormatV5int64AEvpZ)

  `
  `  
  A 64-bit signed integer.  

  #### Declaration

  Swift  

      public static let int64: https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Classes/Schema.html.IntegerFormat

- `
  ``
  ``
  `

  ### [custom(_:)](https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Classes/Schema/IntegerFormat#/s:10FirebaseAI6SchemaC13IntegerFormatV6customyAESSFZ)

  `
  `  
  A custom integer format.  

  #### Declaration

  Swift  

      public static func custom(_ format: String) -> IntegerFormat