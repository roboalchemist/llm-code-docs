# Source: https://firebase.google.com/docs/reference/swift/firebasefirestoreswift/api/reference/Structs/DocumentID.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs/DocumentID.md.txt

# FirebaseFirestore Framework Reference

# DocumentID

    @propertyWrapper
    public struct DocumentID<Value: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/DocumentIDWrappable.html & Codable>:
      StructureCodingUncodedUnkeyed

    extension DocumentID: Codable

    extension DocumentID: Equatable where Value: Equatable

    extension DocumentID: Hashable where Value: Hashable

A property wrapper type that marks a `DocumentReference?` or `String?` field to
be populated with a document identifier when it is read.

Apply the `@DocumentID` annotation to a `DocumentReference?` or `String?`
property in a `Codable` object to have it populated with the document
identifier when it is read and decoded from Firestore.  
Important

The name of the property annotated with `@DocumentID` must not
match the name of any fields in the Firestore document being read or else
an error will be thrown. For example, if the `Codable` object has a
property named `firstName` annotated with `@DocumentID`, and the Firestore
document contains a field named `firstName`, an error will be thrown when
attempting to decode the document.

- Example Read:

      struct Player: Codable {
      @DocumentID var playerID: String?
      var health: Int64
      }

let p = try! await Firestore.firestore()
.collection("players")
.document("player-1")
.getDocument(as: Player.self)
print("(p.playerID!) Health: (p.health)")

// Prints: "Player: player-1, Health: 95"  


    - Important: Trying to encode/decode this type using encoders/decoders other than
      Firestore.Encoder throws an error.

    - Important: When writing a Codable object containing an `@DocumentID` annotated field,
      its value is ignored. This allows you to read a document from one path and
      write it into another without adjusting the value here.

- `
  ``
  ``
  `

  ### [init(wrappedValue:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs/DocumentID#/s:17FirebaseFirestore10DocumentIDV12wrappedValueACyxGxSg_tcfc)

  `
  `  
  Undocumented  

  #### Declaration

  Swift  

      public init(https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs/DocumentID.html#/s:17FirebaseFirestore10DocumentIDV12wrappedValuexSgvp value: Value?)

- `
  ``
  ``
  `

  ### [wrappedValue](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs/DocumentID#/s:17FirebaseFirestore10DocumentIDV12wrappedValuexSgvp)

  `
  `  
  Undocumented  

  #### Declaration

  Swift  

      public var wrappedValue: Value? { get set }

- `
  ``
  ``
  `

  ### [init(from:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs/DocumentID#/s:17FirebaseFirestore10DocumentIDV4fromACyxGs7Decoder_p_tKcfc)

  `
  `  
  A `Codable` object containing an `@DocumentID` annotated field should
  only be decoded with [Firestore.Decoder](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/Firestore/Decoder.html); this initializer throws if an
  unsupported decoder is used.  
  Throws
  [FirestoreDecodingError](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Enums/FirestoreDecodingError.html)  

  #### Declaration

  Swift  

      public init(from decoder: Decoder) throws

  #### Parameters

  |-----------------|------------|
  | ` `*decoder*` ` | A decoder. |

- `
  ``
  ``
  `

  ### [encode(to:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs/DocumentID#/s:17FirebaseFirestore10DocumentIDV6encode2toys7Encoder_p_tKF)

  `
  `  
  A `Codable` object containing an `@DocumentID` annotated field can only
  be encoded with [Firestore.Encoder](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/Firestore/Encoder.html); this initializer always throws.  
  Throws
  [FirestoreEncodingError](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Enums/FirestoreEncodingError.html)  

  #### Declaration

  Swift  

      public func encode(to encoder: Encoder) throws

  #### Parameters

  |-----------------|---------------------|
  | ` `*encoder*` ` | An invalid encoder. |