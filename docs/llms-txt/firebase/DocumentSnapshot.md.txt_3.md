# Source: https://firebase.google.com/docs/reference/swift/firebasefirestoreswift/api/reference/Extensions/DocumentSnapshot.md.txt

# FirebaseFirestoreSwift Framework Reference

# DocumentSnapshot

    public extension DocumentSnapshot

- `


  ### [data(as:with:decoder:)](https://firebase.google.com/docs/reference/swift/firebasefirestoreswift/api/reference/Extensions/DocumentSnapshot#/s:So19FIRDocumentSnapshotC22FirebaseFirestoreSwiftE4data2as4with7decoderxxm_So26FIRServerTimestampBehaviorVSo12FIRFirestoreCACE7DecoderVtKSeRzlF)


  ` Retrieves all fields in a document and converts them to an instance of
  caller-specified type.

  By default, server-provided timestamps that have not yet been set to their
  final value will be returned as `NSNull`. Pass `serverTimestampBehavior`
  to configure this behavior.

  See `https://firebase.google.com/docs/reference/swift/firebasefirestoreswift/api/reference/Extensions/Firestore/Decoder.html` for more details about the decoding process.

  #### Declaration

  Swift

      func data<T: Decodable>(as type: T.Type,
                              with serverTimestampBehavior: ServerTimestampBehavior = .none,
                              decoder: Firestore.Decoder = .init()) throws -> T