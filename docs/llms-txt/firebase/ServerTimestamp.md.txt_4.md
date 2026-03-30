# Source: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs/ServerTimestamp.md.txt

# FirebaseFirestore Framework Reference

# ServerTimestamp

    @propertyWrapper
    public struct ServerTimestamp<Value>: Codable
      where Value: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/ServerTimestampWrappable.html & Codable

    extension ServerTimestamp: Equatable where Value: Equatable

    extension ServerTimestamp: Hashable where Value: Hashable

    extension ServerTimestamp: Sendable where Value: Sendable

A property wrapper that marks an `Optional<Timestamp>` field to be
populated with a server timestamp. If a `Codable` object being written
contains a `nil` for an `@ServerTimestamp`-annotated field, it will be
replaced with `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FieldValue.html#/c:objc(cs)FIRFieldValue(cm)fieldValueForServerTimestamp` as it is sent.

Example:

    struct CustomModel {
      @ServerTimestamp var ts: Timestamp?
    }

Then writing `CustomModel(ts: nil)` will tell server to fill `ts` with
current timestamp.
- `


  ### [init(wrappedValue:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs/ServerTimestamp#/s:17FirebaseFirestore15ServerTimestampV12wrappedValueACyxGxSg_tcfc)


  ` Undocumented

  #### Declaration

  Swift

      public init(https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs/ServerTimestamp.html#/s:17FirebaseFirestore15ServerTimestampV12wrappedValuexSgvp value: Value?)

- `


  ### [wrappedValue](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs/ServerTimestamp#/s:17FirebaseFirestore15ServerTimestampV12wrappedValuexSgvp)


  ` Undocumented

  #### Declaration

  Swift

      public var wrappedValue: Value? { get set }

[## Codable](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs/ServerTimestamp#/Codable)

- `


  ### [init(from:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs/ServerTimestamp#/s:Se4fromxs7Decoder_p_tKcfc)


  `

  #### Declaration

  Swift

      public init(from decoder: Decoder) throws

- `


  ### [encode(to:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs/ServerTimestamp#/s:SE6encode2toys7Encoder_p_tKF)


  `

  #### Declaration

  Swift

      public func encode(to encoder: Encoder) throws