# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/ServerTimestamp.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs/ServerTimestamp.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Structs/ServerTimestamp.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/ServerTimestamp.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebasefirestoreswift/api/reference/Structs/ServerTimestamp.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebasedatabaseswift/api/reference/Structs/ServerTimestamp.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebasefirestoreswift/api/reference/Structs/ServerTimestamp.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebasedatabaseswift/api/reference/Structs/ServerTimestamp.md.txt

# FirebaseDatabaseSwift Framework Reference

# ServerTimestamp

    @propertyWrapper
    public struct ServerTimestamp : Codable, Equatable, Hashable

A property wrapper that marks an `Optional<Date>` field to be
populated with a server timestamp. If a `Codable` object being written
contains a `nil` for an `@ServerTimestamp`-annotated field, it will be
replaced with `ServerValue.timestamp()` as it is sent.

Example:  

    struct CustomModel {
      @ServerTimestamp var ts: Date?
    }

Then writing `CustomModel(ts: nil)` will tell server to fill `ts` with
current timestamp.
- `
  ``
  ``
  `

  ### [init(wrappedValue:)](https://firebase.google.com/docs/reference/swift/firebasedatabaseswift/api/reference/Structs/ServerTimestamp#/s:21FirebaseDatabaseSwift15ServerTimestampV12wrappedValueAC10Foundation4DateVSg_tcfc)

  `
  `  
  Undocumented  

  #### Declaration

  Swift  

      public init(https://firebase.google.com/docs/reference/swift/firebasedatabaseswift/api/reference/Structs/ServerTimestamp.html#/s:21FirebaseDatabaseSwift15ServerTimestampV12wrappedValue10Foundation4DateVSgvp value: Date?)

- `
  ``
  ``
  `

  ### [wrappedValue](https://firebase.google.com/docs/reference/swift/firebasedatabaseswift/api/reference/Structs/ServerTimestamp#/s:21FirebaseDatabaseSwift15ServerTimestampV12wrappedValue10Foundation4DateVSgvp)

  `
  `  
  Undocumented  

  #### Declaration

  Swift  

      public var wrappedValue: Date? { get set }

[## Codable](https://firebase.google.com/docs/reference/swift/firebasedatabaseswift/api/reference/Structs/ServerTimestamp#/Codable)

- `
  ``
  ``
  `

  ### [init(from:)](https://firebase.google.com/docs/reference/swift/firebasedatabaseswift/api/reference/Structs/ServerTimestamp#/s:Se4fromxs7Decoder_p_tKcfc)

  `
  `  

  #### Declaration

  Swift  

      public init(from decoder: Decoder) throws

- `
  ``
  ``
  `

  ### [encode(to:)](https://firebase.google.com/docs/reference/swift/firebasedatabaseswift/api/reference/Structs/ServerTimestamp#/s:SE6encode2toys7Encoder_p_tKF)

  `
  `  

  #### Declaration

  Swift  

      public func encode(to encoder: Encoder) throws