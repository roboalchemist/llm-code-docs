# Source: https://firebase.google.com/docs/reference/swift/firebasefirestoreswift/api/reference/Extensions/Date.md.txt

# FirebaseFirestoreSwift Framework Reference

# Date

    extension Date: https://firebase.google.com/docs/reference/swift/firebasefirestoreswift/api/reference/Protocols/ServerTimestampWrappable.html

- `


  ### [wrap(_:)](https://firebase.google.com/docs/reference/swift/firebasefirestoreswift/api/reference/Extensions/Date#/s:22FirebaseFirestoreSwift24ServerTimestampWrappableP4wrapyxSo12FIRTimestampCKFZ)


  `

  #### Declaration

  Swift

      public static func wrap(_ timestamp: Timestamp) throws -> Date

- `


  ### [unwrap(_:)](https://firebase.google.com/docs/reference/swift/firebasefirestoreswift/api/reference/Extensions/Date#/s:22FirebaseFirestoreSwift24ServerTimestampWrappableP6unwrapySo12FIRTimestampCxKFZ)


  `

  #### Declaration

  Swift

      public static func unwrap(_ value: `Self`) throws -> Timestamp