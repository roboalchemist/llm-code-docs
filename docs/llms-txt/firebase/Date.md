# Source: https://firebase.google.com/docs/reference/swift/firebasefirestoreswift/api/reference/Extensions/Date.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Extensions/Date.md.txt

# FirebaseFirestore Framework Reference

# Date

    extension Date: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/ServerTimestampWrappable.html

- `
  ``
  ``
  `

  ### [wrap(_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Extensions/Date#/s:17FirebaseFirestore24ServerTimestampWrappableP4wrapyxSo12FIRTimestampCKFZ)

  `
  `  

  #### Declaration

  Swift  

      public static func wrap(_ timestamp: Timestamp) throws -> Date

- `
  ``
  ``
  `

  ### [unwrap(_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Extensions/Date#/s:17FirebaseFirestore24ServerTimestampWrappableP6unwrapySo12FIRTimestampCxKFZ)

  `
  `  

  #### Declaration

  Swift  

      public static func unwrap(_ value: `Self`) throws -> Timestamp