# Source: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/Firestore/Encoder.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebasefirestoreswift/api/reference/Extensions/Firestore/Encoder.md.txt

# FirebaseFirestoreSwift Framework Reference

# Encoder

    struct Encoder

Undocumented
- `
  ``
  ``
  `

  ### [init()](https://firebase.google.com/docs/reference/swift/firebasefirestoreswift/api/reference/Extensions/Firestore/Encoder#/s:So12FIRFirestoreC22FirebaseFirestoreSwiftE7EncoderVAEycfc)

  `
  `  
  Undocumented  

  #### Declaration

  Swift  

      public init()

- `
  ``
  ``
  `

  ### [encode(_:)](https://firebase.google.com/docs/reference/swift/firebasefirestoreswift/api/reference/Extensions/Firestore/Encoder#/s:So12FIRFirestoreC22FirebaseFirestoreSwiftE7EncoderV6encodeySDySSypGxKSERzlF)

  `
  `  
  Returns encoded data that Firestore API recognizes.

  If possible, all types will be converted to compatible types Firestore
  can handle. This means certain Firestore specific types will be encoded
  as pass-through: this encoder will only pass those types along since that
  is what Firestore can handle. The same types will be encoded differently
  with other encoders (for example: JSONEncoder).

  The Firestore pass-through types are:
  - GeoPoint
  - Timestamp
  - DocumentReference

  #### Declaration

  Swift  

      public func encode<T>(_ value: T) throws -> [String : Any] where T : Encodable

  #### Parameters

  |---------------|--------------------------------------------------|
  | ` `*value*` ` | The Encodable object to convert to encoded data. |

  #### Return Value

  A Map keyed by String representing a document Firestore
  API can work with.