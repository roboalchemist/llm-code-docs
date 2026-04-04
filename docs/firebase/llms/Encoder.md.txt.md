# Source: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/Firestore/Encoder.md.txt

# FirebaseFirestore Framework Reference

# Encoder

    class Encoder

Undocumented
- `


  ### [dateEncodingStrategy](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/Firestore/Encoder#/s:So12FIRFirestoreC17FirebaseFirestoreE7EncoderC20dateEncodingStrategy0B11SharedSwift0b4DataD0C04DatefG0Ovp)


  ` The strategy to use in encoding dates. Defaults to `.timestamp`.

  #### Declaration

  Swift

      public var dateEncodingStrategy: FirebaseDataEncoder.DateEncodingStrategy

- `


  ### [dataEncodingStrategy](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/Firestore/Encoder#/s:So12FIRFirestoreC17FirebaseFirestoreE7EncoderC20dataEncodingStrategy0B11SharedSwift0b4DataD0C0jfG0Ovp)


  ` Firestore encodes Data as `NSData` blobs versus the default .base64 strings.

  #### Declaration

  Swift

      public var dataEncodingStrategy: FirebaseDataEncoder.DataEncodingStrategy

- `


  ### [nonConformingFloatEncodingStrategy](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/Firestore/Encoder#/s:So12FIRFirestoreC17FirebaseFirestoreE7EncoderC34nonConformingFloatEncodingStrategy0B11SharedSwift0b4DataD0C03NonfghI0Ovp)


  ` The strategy to use in encoding non-conforming numbers. Defaults to `.throw`.

  #### Declaration

  Swift

      public var nonConformingFloatEncodingStrategy: FirebaseDataEncoder.NonConformingFloatEncodingStrategy

- `


  ### [keyEncodingStrategy](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/Firestore/Encoder#/s:So12FIRFirestoreC17FirebaseFirestoreE7EncoderC19keyEncodingStrategy0B11SharedSwift0b4DataD0C03KeyfG0Ovp)


  ` The strategy to use for encoding keys. Defaults to `.useDefaultKeys`.

  #### Declaration

  Swift

      public var keyEncodingStrategy: FirebaseDataEncoder.KeyEncodingStrategy

- `


  ### [userInfo](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/Firestore/Encoder#/s:So12FIRFirestoreC17FirebaseFirestoreE7EncoderC8userInfoSDys010CodingUserF3KeyVypGvp)


  ` Contextual user-provided information for use during encoding.

  #### Declaration

  Swift

      public var userInfo: [CodingUserInfoKey : Any]

- `


  ### [encode(_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/Firestore/Encoder#/s:So12FIRFirestoreC17FirebaseFirestoreE7EncoderC6encodeySDySSypGxKSERzlF)


  ` Undocumented

  #### Declaration

  Swift

      public func encode<T>(_ value: T) throws -> [String : Any] where T : Encodable

- `


  ### [init()](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/Firestore/Encoder#/s:So12FIRFirestoreC17FirebaseFirestoreE7EncoderCAEycfc)


  ` Undocumented

  #### Declaration

  Swift

      public init()