# Source: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Extensions/FirebaseFirestore/FieldValue.md.txt

# FirebaseFirestore Framework Reference

# FieldValue

    extension FirebaseFirestore.FieldValue: Swift.Encodable

Extends FieldValue to conform to Encodable.
- `


  ### [encode(to:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Extensions/FirebaseFirestore/FieldValue#/s:So13FIRFieldValueC17FirebaseFirestoreE6encode2toys7Encoder_p_tKF)


  ` Encoding a FieldValue will throw by default unless the encoder implementation
  explicitly handles it, which is what Firestore.Encoder does.

  #### Declaration

  Swift

      public func encode(to encoder: Encoder) throws