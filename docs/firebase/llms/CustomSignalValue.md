# Source: https://firebase.google.com/docs/reference/swift/firebaseremoteconfig/api/reference/Structs/CustomSignalValue.md.txt

# FirebaseRemoteConfig Framework Reference

# CustomSignalValue

    public struct CustomSignalValue

    extension CustomSignalValue: ExpressibleByStringInterpolation

    extension CustomSignalValue: ExpressibleByIntegerLiteral

    extension CustomSignalValue: ExpressibleByFloatLiteral

Represents a value associated with a key in a custom signal, restricted to the allowed data
types : String, Int, Double.
- `
  ``
  ``
  `

  ### [string(_:)](https://firebase.google.com/docs/reference/swift/firebaseremoteconfig/api/reference/Structs/CustomSignalValue#/s:20FirebaseRemoteConfig17CustomSignalValueV6stringyACSSFZ)

  `
  `  
  Returns a string backed custom signal.  

  #### Declaration

  Swift  

      public static func string(_ string: String) -> CustomSignalValue

  #### Parameters

  |----------------|--------------------------------------------------|
  | ` `*string*` ` | The given string to back the custom signal with. |

  #### Return Value

  A string backed custom signal.
- `
  ``
  ``
  `

  ### [integer(_:)](https://firebase.google.com/docs/reference/swift/firebaseremoteconfig/api/reference/Structs/CustomSignalValue#/s:20FirebaseRemoteConfig17CustomSignalValueV7integeryACSiFZ)

  `
  `  
  Returns an integer backed custom signal.  

  #### Declaration

  Swift  

      public static func integer(_ integer: Int) -> CustomSignalValue

  #### Parameters

  |-----------------|---------------------------------------------------|
  | ` `*integer*` ` | The given integer to back the custom signal with. |

  #### Return Value

  An integer backed custom signal.
- `
  ``
  ``
  `

  ### [double(_:)](https://firebase.google.com/docs/reference/swift/firebaseremoteconfig/api/reference/Structs/CustomSignalValue#/s:20FirebaseRemoteConfig17CustomSignalValueV6doubleyACSdFZ)

  `
  `  
  Returns an floating-point backed custom signal.  

  #### Declaration

  Swift  

      public static func double(_ double: Double) -> CustomSignalValue

  #### Parameters

  |----------------|----------------------------------------------------------------|
  | ` `*double*` ` | The given floating-point value to back the custom signal with. |

  #### Return Value

  An floating-point backed custom signal
- `
  ``
  ``
  `

  ### [init(stringLiteral:)](https://firebase.google.com/docs/reference/swift/firebaseremoteconfig/api/reference/Structs/CustomSignalValue#/s:s26ExpressibleByStringLiteralP06stringD0x0cD4TypeQz_tcfc)

  `
  `  

  #### Declaration

  Swift  

      public init(stringLiteral value: String)

- `
  ``
  ``
  `

  ### [init(integerLiteral:)](https://firebase.google.com/docs/reference/swift/firebaseremoteconfig/api/reference/Structs/CustomSignalValue#/s:s27ExpressibleByIntegerLiteralP07integerD0x0cD4TypeQz_tcfc)

  `
  `  

  #### Declaration

  Swift  

      public init(integerLiteral value: Int)

- `
  ``
  ``
  `

  ### [init(floatLiteral:)](https://firebase.google.com/docs/reference/swift/firebaseremoteconfig/api/reference/Structs/CustomSignalValue#/s:s25ExpressibleByFloatLiteralP05floatD0x0cD4TypeQz_tcfc)

  `
  `  

  #### Declaration

  Swift  

      public init(floatLiteral value: Double)