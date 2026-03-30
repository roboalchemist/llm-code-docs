# Source: https://firebase.google.com/docs/reference/swift/firebasefirestoreswift/api/reference/Extensions/Firestore/Decoder.md.txt

# FirebaseFirestoreSwift Framework Reference

# Decoder

    struct Decoder

Undocumented
- `


  ### [init()](https://firebase.google.com/docs/reference/swift/firebasefirestoreswift/api/reference/Extensions/Firestore/Decoder#/s:So12FIRFirestoreC22FirebaseFirestoreSwiftE7DecoderVAEycfc)


  ` Undocumented

  #### Declaration

  Swift

      public init()

- `


  ### [decode(_:from:in:)](https://firebase.google.com/docs/reference/swift/firebasefirestoreswift/api/reference/Extensions/Firestore/Decoder#/s:So12FIRFirestoreC22FirebaseFirestoreSwiftE7DecoderV6decode_4from2inxxm_ypSo20FIRDocumentReferenceCSgtKSeRzlF)


  ` Returns an instance of specified type from a Firestore document.

  If exists in `container`, Firestore specific types are recognized, and
  passed through to `Decodable` implementations. This means types below
  in `container` are directly supported:
  - GeoPoint
  - Timestamp
  - DocumentReference

  - A type to decode a document to.

  - container: A Map keyed of String representing a Firestore document.

  - document: A reference to the Firestore Document that is being
    decoded.

  #### Declaration

  Swift

      public func decode<T: Decodable>(_: T.Type,
                                       from container: Any,
                                       in document: DocumentReference? = nil) throws -> T

  #### Parameters

  |---|---|
  | ` container ` | A Map keyed of String representing a Firestore document. |
  | ` document ` | A reference to the Firestore Document that is being decoded. |

  #### Return Value

  An instance of specified type by the first parameter.