# Source: https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Structs.md.txt

# FirebaseDatabase Framework Reference

# Structures

The following structures are available globally.
- `


  ### [ServerTimestamp](https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Structs/ServerTimestamp)


  ` A property wrapper that marks an `Optional<Date>` field to be
  populated with a server timestamp. If a `Codable` object being written
  contains a `nil` for an `@ServerTimestamp`-annotated field, it will be
  replaced with `https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Classes/ServerValue#/c:objc(cs)FIRServerValue(cm)timestamp` as it is sent.

  Example:

      struct CustomModel {
        @ServerTimestamp var ts: Date?
      }

  Then writing `CustomModel(ts: nil)` will tell server to fill `ts` with
  current timestamp.

  #### Declaration

  Swift

      @propertyWrapper
      public struct ServerTimestamp : Codable, Equatable, Hashable