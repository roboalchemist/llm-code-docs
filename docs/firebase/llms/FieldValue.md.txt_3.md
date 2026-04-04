# Source: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FieldValue.md.txt

# FirebaseFirestore Framework Reference

# FieldValue

    class FieldValue : NSObject, @unchecked Sendable

Sentinel values that can be used when writing document fields with `setData()` or `updateData()`.
- `


  ### [delete()](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FieldValue#/c:objc(cs)FIRFieldValue(cm)fieldValueForDelete)


  ` Used with `updateData()` to mark a field for deletion.

  #### Declaration

  Swift

      class func delete() -> Self

- `


  ### [serverTimestamp()](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FieldValue#/c:objc(cs)FIRFieldValue(cm)fieldValueForServerTimestamp)


  ` Used with `setData()` or `updateData()` to include a server-generated timestamp in the written
  data.

  #### Declaration

  Swift

      class func serverTimestamp() -> Self

- `


  ### [arrayUnion(_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FieldValue#/c:objc(cs)FIRFieldValue(cm)fieldValueForArrayUnion:)


  ` Returns a special value that can be used with `setData()` or `updateData()` that tells the server
  to union the given elements with any array value that already exists on the server. Each
  specified element that doesn't already exist in the array will be added to the end. If the
  field being modified is not already an array it will be overwritten with an array containing
  exactly the specified elements.

  #### Declaration

  Swift

      class func arrayUnion(_ elements: [Any]) -> Self

  #### Parameters

  |---|---|
  | ` elements ` | The elements to union into the array. |

  #### Return Value

  The `FieldValue` sentinel for use in a call to `setData()` or `updateData()`.
- `


  ### [arrayRemove(_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FieldValue#/c:objc(cs)FIRFieldValue(cm)fieldValueForArrayRemove:)


  ` Returns a special value that can be used with `setData()` or `updateData()` that tells the server
  to remove the given elements from any array value that already exists on the server. All
  instances of each element specified will be removed from the array. If the field being
  modified is not already an array it will be overwritten with an empty array.

  #### Declaration

  Swift

      class func arrayRemove(_ elements: [Any]) -> Self

  #### Parameters

  |---|---|
  | ` elements ` | The elements to remove from the array. |

  #### Return Value

  The `FieldValue` sentinel for use in a call to `setData()` or `updateData()`.
- `


  ### [increment(_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FieldValue#/c:objc(cs)FIRFieldValue(cm)fieldValueForDoubleIncrement:)


  ` Returns a special value that can be used with `setData()` or `updateData()` that tells the server
  to increment the field's current value by the given value.

  If the current value is an integer or a double, both the current and the given value will be
  interpreted as doubles and all arithmetic will follow IEEE 754 semantics. Otherwise, the
  transformation will set the field to the given value.

  #### Declaration

  Swift

      class func increment(_ d: Double) -> Self

  #### Parameters

  |---|---|
  | ` d ` | The double value to increment by. |

  #### Return Value

  The `FieldValue` sentinel for use in a call to `setData()` or `updateData()`.
- `


  ### [increment(_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FieldValue#/c:objc(cs)FIRFieldValue(cm)fieldValueForIntegerIncrement:)


  ` Returns a special value that can be used with `setData()` or `updateData()` that tells the server
  to increment the field's current value by the given value.

  If the current field value is an integer, possible integer overflows are resolved to LONG_MAX or
  LONG_MIN. If the current field value is a double, both values will be interpreted as doubles and
  the arithmetic will follow IEEE 754 semantics.

  If field is not an integer or double, or if the field does not yet exist, the transformation
  will set the field to the given value.

  #### Declaration

  Swift

      class func increment(_ l: Int64) -> Self

  #### Parameters

  |---|---|
  | ` l ` | The integer value to increment by. |

  #### Return Value

  The `FieldValue` sentinel for use in a call to `setData()` or `updateData()`.
- `


  ### [+vectorWithArray:](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FieldValue#/c:objc(cs)FIRFieldValue(cm)vectorWithArray:)


  ` Creates a new `VectorValue` constructed with a copy of the given array of NSNumbers.

  #### Parameters

  |---|---|
  | ` array ` | Create a `VectorValue` instance with a copy of this array of NSNumbers. |

  #### Return Value

  A new `VectorValue` constructed with a copy of the given array of NSNumbers.
- `


  ### [vector(_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FieldValue#/s:So13FIRFieldValueC17FirebaseFirestoreE6vectorySo09FIRVectorB0CSaySdGFZ)


  ` Creates a new `VectorValue` constructed with a copy of the given array of Doubles.

  #### Declaration

  Swift

      static func vector(_ array: [Double]) -> VectorValue

  #### Parameters

  |---|---|
  | ` array ` | An array of Doubles. |

  #### Return Value

  A new `VectorValue` constructed with a copy of the given array of Doubles.
- `


  ### [vector(_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FieldValue#/s:So13FIRFieldValueC17FirebaseFirestoreE6vectorySo09FIRVectorB0CSaySfGFZ)


  ` Creates a new `VectorValue` constructed with a copy of the given array of Floats.

  #### Declaration

  Swift

      static func vector(_ array: [Float]) -> VectorValue

  #### Parameters

  |---|---|
  | ` array ` | An array of Floats. |

  #### Return Value

  A new `VectorValue` constructed with a copy of the given array of Floats.