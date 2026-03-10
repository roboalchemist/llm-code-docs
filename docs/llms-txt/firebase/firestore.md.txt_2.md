# Source: https://firebase.google.com/docs/reference/swift/firebasefirestoreswift/api/reference/Extensions/Firestore.md.txt

# FirebaseFirestoreSwift Framework Reference

# Firestore

    public extension Firestore

- `


  ### [loadBundle(_:)](https://firebase.google.com/docs/reference/swift/firebasefirestoreswift/api/reference/Extensions/Firestore#/s:So12FIRFirestoreC22FirebaseFirestoreSwiftE10loadBundleySo07FIRLoadF12TaskProgressC10Foundation4DataVYaKF)


  ` Loads a Firestore bundle into the local cache.
  Throws
  `Error` if the bundle data cannot be parsed.

  #### Declaration

  Swift

      func loadBundle(_ bundleData: Data) async throws -> LoadBundleTaskProgress

  #### Parameters

  |---|---|
  | ` bundleData ` | Data from the bundle to be loaded. |

  #### Return Value

  The final `LoadBundleTaskProgress` that contains the total number of documents loaded.
- `


  ### [loadBundle(_:)](https://firebase.google.com/docs/reference/swift/firebasefirestoreswift/api/reference/Extensions/Firestore#/s:So12FIRFirestoreC22FirebaseFirestoreSwiftE10loadBundleySo07FIRLoadF12TaskProgressCSo13NSInputStreamCYaKF)


  ` Loads a Firestore bundle into the local cache.
  Throws
  `Error` if the bundle stream cannot be parsed.

  #### Declaration

  Swift

      func loadBundle(_ bundleStream: InputStream) async throws -> LoadBundleTaskProgress

  #### Parameters

  |---|---|
  | ` bundleStream ` | An input stream from which the bundle can be read. |

  #### Return Value

  The final `LoadBundleTaskProgress` that contains the total number of documents loaded.
- `


  ### [Decoder](https://firebase.google.com/docs/reference/swift/firebasefirestoreswift/api/reference/Extensions/Firestore/Decoder.html)


  ` Undocumented

  #### Declaration

  Swift

      struct Decoder

- `


  ### [Encoder](https://firebase.google.com/docs/reference/swift/firebasefirestoreswift/api/reference/Extensions/Firestore/Encoder.html)


  ` Undocumented

  #### Declaration

  Swift

      struct Encoder