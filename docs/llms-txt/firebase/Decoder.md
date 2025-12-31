# Source: https://firebase.google.com/docs/reference/swift/firebasefirestoreswift/api/reference/Extensions/Firestore/Decoder.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/Firestore/Decoder.md.txt

# FirebaseFirestore Framework Reference

# Decoder

    class Decoder

Undocumented
- `
  ``
  ``
  `

  ### [dateDecodingStrategy](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/Firestore/Decoder#/s:So12FIRFirestoreC17FirebaseFirestoreE7DecoderC20dateDecodingStrategy0B11SharedSwift0b4DataD0C04DatefG0Ovp)

  `
  `  
  The strategy to use in decoding dates. Defaults to `.timestamp`.  

  #### Declaration

  Swift  

      public var dateDecodingStrategy: FirebaseDataDecoder.DateDecodingStrategy

- `
  ``
  ``
  `

  ### [dataDecodingStrategy](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/Firestore/Decoder#/s:So12FIRFirestoreC17FirebaseFirestoreE7DecoderC20dataDecodingStrategy0B11SharedSwift0b4DataD0C0jfG0Ovp)

  `
  `  
  Firestore decodes Data from `NSData` blobs versus the default .base64 strings.  

  #### Declaration

  Swift  

      public var dataDecodingStrategy: FirebaseDataDecoder.DataDecodingStrategy

- `
  ``
  ``
  `

  ### [nonConformingFloatDecodingStrategy](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/Firestore/Decoder#/s:So12FIRFirestoreC17FirebaseFirestoreE7DecoderC34nonConformingFloatDecodingStrategy0B11SharedSwift0b4DataD0C03NonfghI0Ovp)

  `
  `  
  The strategy to use in decoding non-conforming numbers. Defaults to `.throw`.  

  #### Declaration

  Swift  

      public var nonConformingFloatDecodingStrategy: FirebaseDataDecoder.NonConformingFloatDecodingStrategy

- `
  ``
  ``
  `

  ### [keyDecodingStrategy](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/Firestore/Decoder#/s:So12FIRFirestoreC17FirebaseFirestoreE7DecoderC19keyDecodingStrategy0B11SharedSwift0b4DataD0C03KeyfG0Ovp)

  `
  `  
  The strategy to use for decoding keys. Defaults to `.useDefaultKeys`.  

  #### Declaration

  Swift  

      public var keyDecodingStrategy: FirebaseDataDecoder.KeyDecodingStrategy

- `
  ``
  ``
  `

  ### [userInfo](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/Firestore/Decoder#/s:So12FIRFirestoreC17FirebaseFirestoreE7DecoderC8userInfoSDys010CodingUserF3KeyVypGvp)

  `
  `  
  Contextual user-provided information for use during decoding.  

  #### Declaration

  Swift  

      public var userInfo: [CodingUserInfoKey : Any]

- `
  ``
  ``
  `

  ### [decode(_:from:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/Firestore/Decoder#/s:So12FIRFirestoreC17FirebaseFirestoreE7DecoderC6decode_4fromxxm_yptKSeRzlF)

  `
  `  
  Undocumented  

  #### Declaration

  Swift  

      public func decode<T>(_ t: T.Type, from data: Any) throws -> T where T : Decodable

- `
  ``
  ``
  `

  ### [decode(_:from:in:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/Firestore/Decoder#/s:So12FIRFirestoreC17FirebaseFirestoreE7DecoderC6decode_4from2inxxm_ypSo20FIRDocumentReferenceCSgtKSeRzlF)

  `
  `  
  Undocumented  

  #### Declaration

  Swift  

      public func decode<T: Decodable>(_ t: T.Type, from data: Any,
                                       in reference: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/DocumentReference.html?) throws -> T

- `
  ``
  ``
  `

  ### [init()](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/Firestore/Decoder#/s:So12FIRFirestoreC17FirebaseFirestoreE7DecoderCAEycfc)

  `
  `  
  Undocumented  

  #### Declaration

  Swift  

      public init()