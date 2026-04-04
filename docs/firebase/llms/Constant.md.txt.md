# Source: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs/Constant.md.txt

# FirebaseFirestore Framework Reference

# Constant

    public struct Constant : https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression.html, BridgeWrapper, @unchecked Sendable

A `Constant` is an `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression.html` that represents a fixed, literal value within a Firestore
pipeline.

`Constant`s are used to introduce literal values into a query, which can be useful for:

- Comparing a field to a specific value in a `where` clause.
- Adding new fields with fixed values using `addFields`.
- Providing literal arguments to functions like `sum` or `average`.

Example of using a `Constant` to add a new field:

    // Add a new field "source" with the value "manual" to each document
    firestore.pipeline()
      .collection("entries")
      .addFields([
        Constant("manual").as("source")
      ])

- `


  ### [init(_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs/Constant#/s:17FirebaseFirestore8ConstantVyACSicfc)


  ` Creates a new `Constant` expression from an integer literal.

  #### Declaration

  Swift

      public init(_ value: Int)

  #### Parameters

  |---|---|
  | ` value ` | The integer value. |

- `


  ### [init(_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs/Constant#/s:17FirebaseFirestore8ConstantVyACSdcfc)


  ` Creates a new `Constant` expression from a double-precision floating-point literal.

  #### Declaration

  Swift

      public init(_ value: Double)

  #### Parameters

  |---|---|
  | ` value ` | The double value. |

- `


  ### [init(_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs/Constant#/s:17FirebaseFirestore8ConstantVyACSScfc)


  ` Creates a new `Constant` expression from a string literal.

  #### Declaration

  Swift

      public init(_ value: String)

  #### Parameters

  |---|---|
  | ` value ` | The string value. |

- `


  ### [init(_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs/Constant#/s:17FirebaseFirestore8ConstantVyACSbcfc)


  ` Creates a new `Constant` expression from a boolean literal.

  #### Declaration

  Swift

      public init(_ value: Bool)

  #### Parameters

  |---|---|
  | ` value ` | The boolean value. |

- `


  ### [init(_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs/Constant#/s:17FirebaseFirestore8ConstantVyAC10Foundation4DataVcfc)


  ` Creates a new `Constant` expression from a `Data` (bytes) literal.

  #### Declaration

  Swift

      public init(_ value: Data)

  #### Parameters

  |---|---|
  | ` value ` | The `Data` value. |

- `


  ### [init(_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs/Constant#/s:17FirebaseFirestore8ConstantVyACSo11FIRGeoPointCcfc)


  ` Creates a new `Constant` expression from a `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/GeoPoint.html` literal.

  #### Declaration

  Swift

      public init(_ value: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/GeoPoint.html)

  #### Parameters

  |---|---|
  | ` value ` | The `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/GeoPoint.html` value. |

- `


  ### [init(_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs/Constant#/s:17FirebaseFirestore8ConstantVyACSo12FIRTimestampCcfc)


  ` Creates a new `Constant` expression from a `Timestamp` literal.

  #### Declaration

  Swift

      public init(_ value: Timestamp)

  #### Parameters

  |---|---|
  | ` value ` | The `Timestamp` value. |

- `


  ### [init(_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs/Constant#/s:17FirebaseFirestore8ConstantVyAC10Foundation4DateVcfc)


  ` Creates a new `Constant` expression from a `Date` literal.

  The `Date` will be converted to a `Timestamp` internally.

  #### Declaration

  Swift

      public init(_ value: Date)

  #### Parameters

  |---|---|
  | ` value ` | The `Date` value. |

- `


  ### [init(_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs/Constant#/s:17FirebaseFirestore8ConstantVyACSo20FIRDocumentReferenceCcfc)


  ` Creates a new `Constant` expression from a `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/DocumentReference.html` literal.

  #### Declaration

  Swift

      public init(_ value: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/DocumentReference.html)

  #### Parameters

  |---|---|
  | ` value ` | The `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/DocumentReference.html` value. |

- `


  ### [init(_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs/Constant#/s:17FirebaseFirestore8ConstantVyACSo14FIRVectorValueCcfc)


  ` Creates a new `Constant` expression from a `VectorValue` literal.

  #### Declaration

  Swift

      public init(_ value: VectorValue)

  #### Parameters

  |---|---|
  | ` value ` | The `VectorValue` value. |

- `


  ### [nil](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs/Constant#/s:17FirebaseFirestore8ConstantV3nilACvpZ)


  ` A `Constant` representing a `nil` value.

  #### Declaration

  Swift

      public static let `nil`: Constant