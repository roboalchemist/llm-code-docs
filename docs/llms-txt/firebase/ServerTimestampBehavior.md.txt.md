# Source: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Enums/ServerTimestampBehavior.md.txt

# FirebaseFirestore Framework Reference

# ServerTimestampBehavior

    enum ServerTimestampBehavior : Int, @unchecked Sendable

Controls the return value for server timestamps that have not yet been set to
their final value.
- `


  ### [none](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Enums/ServerTimestampBehavior#/c:@E@FIRServerTimestampBehavior@FIRServerTimestampBehaviorNone)


  ` Return `NSNull` for `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FieldValue.html#/c:objc(cs)FIRFieldValue(cm)fieldValueForServerTimestamp` fields that have not yet
  been set to their final value.

  #### Declaration

  Swift

      case none = 0

- `


  ### [estimate](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Enums/ServerTimestampBehavior#/c:@E@FIRServerTimestampBehavior@FIRServerTimestampBehaviorEstimate)


  ` Return a local estimates for `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FieldValue.html#/c:objc(cs)FIRFieldValue(cm)fieldValueForServerTimestamp`
  fields that have not yet been set to their final value. This estimate will
  likely differ from the final value and may cause these pending values to
  change once the server result becomes available.

  #### Declaration

  Swift

      case estimate = 1

- `


  ### [previous](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Enums/ServerTimestampBehavior#/c:@E@FIRServerTimestampBehavior@FIRServerTimestampBehaviorPrevious)


  ` Return the previous value for `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FieldValue.html#/c:objc(cs)FIRFieldValue(cm)fieldValueForServerTimestamp` fields that
  have not yet been set to their final value.

  #### Declaration

  Swift

      case previous = 2