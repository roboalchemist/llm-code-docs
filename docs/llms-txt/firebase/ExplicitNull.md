# Source: https://firebase.google.com/docs/reference/swift/firebasefirestoreswift/api/reference/Structs/ExplicitNull.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs/ExplicitNull.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebasefirestoreswift/api/reference/Structs/ExplicitNull.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs/ExplicitNull.md.txt

# FirebaseFirestore Framework Reference

# ExplicitNull

    @propertyWrapper
    public struct ExplicitNull<Value>

    extension ExplicitNull: Equatable where Value: Equatable

    extension ExplicitNull: Hashable where Value: Hashable

    extension ExplicitNull: Encodable where Value: Encodable

    extension ExplicitNull: Decodable where Value: Decodable

Wraps an `Optional` field in a `Codable` object such that when the field
has a `nil` value it will encode to a null value in Firestore. Normally,
optional fields are omitted from the encoded document.

This is useful for ensuring a field is present in a Firestore document,
even when there is no associated value.
- `
  ``
  ``
  `

  ### [init(wrappedValue:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs/ExplicitNull#/s:17FirebaseFirestore12ExplicitNullV12wrappedValueACyxGxSg_tcfc)

  `
  `  
  Undocumented  

  #### Declaration

  Swift  

      public init(https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs/ExplicitNull.html#/s:17FirebaseFirestore12ExplicitNullV12wrappedValuexSgvp value: Value?)

- `
  ``
  ``
  `

  ### [wrappedValue](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs/ExplicitNull#/s:17FirebaseFirestore12ExplicitNullV12wrappedValuexSgvp)

  `
  `  
  Undocumented  

  #### Declaration

  Swift  

      public var wrappedValue: Value? { get set }

[## Available where \`Value\`: \`Encodable\`](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs/ExplicitNull#/Available-where-%60Value%60%3A-%60Encodable%60)

- `
  ``
  ``
  `

  ### [encode(to:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs/ExplicitNull#/s:SE6encode2toys7Encoder_p_tKF)

  `
  `  

  #### Declaration

  Swift  

      public func encode(to encoder: Encoder) throws

[## Available where \`Value\`: \`Decodable\`](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs/ExplicitNull#/Available-where-%60Value%60%3A-%60Decodable%60)

- `
  ``
  ``
  `

  ### [init(from:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs/ExplicitNull#/s:Se4fromxs7Decoder_p_tKcfc)

  `
  `  

  #### Declaration

  Swift  

      public init(from decoder: Decoder) throws