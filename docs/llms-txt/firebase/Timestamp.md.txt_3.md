# Source: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Extensions/Timestamp.md.txt

# FirebaseFirestore Framework Reference

# Timestamp

    extension Timestamp: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/ServerTimestampWrappable.html

- `


  ### [wrap(_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Extensions/Timestamp#/s:17FirebaseFirestore24ServerTimestampWrappableP4wrapyxSo12FIRTimestampCKFZ)


  `

  #### Declaration

  Swift

      public static func wrap(_ timestamp: Timestamp) throws -> Self

- `


  ### [unwrap(_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Extensions/Timestamp#/s:17FirebaseFirestore24ServerTimestampWrappableP6unwrapySo12FIRTimestampCxKFZ)


  `

  #### Declaration

  Swift

      public static func unwrap(_ value: Timestamp) throws -> Timestamp