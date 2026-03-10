# Source: https://firebase.google.com/docs/reference/swift/firebasefirestoreswift/api/reference/Extensions/FieldValue.md.txt

# FirebaseFirestoreSwift Framework Reference

# FieldValue

    extension FieldValue: Encodable

Extends FieldValue to conform to Encodable.
- `


  ### [encode(to:)](https://firebase.google.com/docs/reference/swift/firebasefirestoreswift/api/reference/Extensions/FieldValue#/s:So13FIRFieldValueC22FirebaseFirestoreSwiftE6encode2toys7Encoder_p_tKF)


  ` Encoding a FieldValue will throw by default unless the encoder implementation
  explicitly handles it, which is what Firestore.Encoder does.

  #### Declaration

  Swift

      public func encode(to encoder: Encoder) throws