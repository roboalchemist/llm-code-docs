# Source: https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRFieldValue.md.txt

# FirebaseFirestore Framework Reference

# FIRFieldValue


    @interface FIRFieldValue : NSObject

Sentinel values that can be used when writing document fields with `setData()` or `updateData()`.
- `
  ``
  ``
  `

  ### [+fieldValueForDelete](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRFieldValue#/c:objc(cs)FIRFieldValue(cm)fieldValueForDelete)

  `
  `  
  Used with `updateData()` to mark a field for deletion.  

  #### Declaration

  Objective-C  

      + (nonnull instancetype)fieldValueForDelete;

- `
  ``
  ``
  `

  ### [+fieldValueForServerTimestamp](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRFieldValue#/c:objc(cs)FIRFieldValue(cm)fieldValueForServerTimestamp)

  `
  `  
  Used with `setData()` or `updateData()` to include a server-generated timestamp in the written
  data.  

  #### Declaration

  Objective-C  

      + (nonnull instancetype)fieldValueForServerTimestamp;

- `
  ``
  ``
  `

  ### [+fieldValueForArrayUnion:](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRFieldValue#/c:objc(cs)FIRFieldValue(cm)fieldValueForArrayUnion:)

  `
  `  
  Returns a special value that can be used with `setData()` or `updateData()` that tells the server
  to union the given elements with any array value that already exists on the server. Each
  specified element that doesn't already exist in the array will be added to the end. If the
  field being modified is not already an array it will be overwritten with an array containing
  exactly the specified elements.  

  #### Declaration

  Objective-C  

      + (nonnull instancetype)fieldValueForArrayUnion:(nonnull NSArray<id> *)elements;

  #### Parameters

  |------------------|---------------------------------------|
  | ` `*elements*` ` | The elements to union into the array. |

  #### Return Value

  The `FieldValue` sentinel for use in a call to `setData()` or `updateData()`.
- `
  ``
  ``
  `

  ### [+fieldValueForArrayRemove:](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRFieldValue#/c:objc(cs)FIRFieldValue(cm)fieldValueForArrayRemove:)

  `
  `  
  Returns a special value that can be used with `setData()` or `updateData()` that tells the server
  to remove the given elements from any array value that already exists on the server. All
  instances of each element specified will be removed from the array. If the field being
  modified is not already an array it will be overwritten with an empty array.  

  #### Declaration

  Objective-C  

      + (nonnull instancetype)fieldValueForArrayRemove:
          (nonnull NSArray<id> *)elements;

  #### Parameters

  |------------------|----------------------------------------|
  | ` `*elements*` ` | The elements to remove from the array. |

  #### Return Value

  The `FieldValue` sentinel for use in a call to `setData()` or `updateData()`.
- `
  ``
  ``
  `

  ### [+fieldValueForDoubleIncrement:](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRFieldValue#/c:objc(cs)FIRFieldValue(cm)fieldValueForDoubleIncrement:)

  `
  `  
  Returns a special value that can be used with `setData()` or `updateData()` that tells the server
  to increment the field's current value by the given value.

  If the current value is an integer or a double, both the current and the given value will be
  interpreted as doubles and all arithmetic will follow IEEE 754 semantics. Otherwise, the
  transformation will set the field to the given value.  

  #### Declaration

  Objective-C  

      + (nonnull instancetype)fieldValueForDoubleIncrement:(double)d;

  #### Parameters

  |-----------|-----------------------------------|
  | ` `*d*` ` | The double value to increment by. |

  #### Return Value

  The `FieldValue` sentinel for use in a call to `setData()` or `updateData()`.
- `
  ``
  ``
  `

  ### [+fieldValueForIntegerIncrement:](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRFieldValue#/c:objc(cs)FIRFieldValue(cm)fieldValueForIntegerIncrement:)

  `
  `  
  Returns a special value that can be used with `setData()` or `updateData()` that tells the server
  to increment the field's current value by the given value.

  If the current field value is an integer, possible integer overflows are resolved to LONG_MAX or
  LONG_MIN. If the current field value is a double, both values will be interpreted as doubles and
  the arithmetic will follow IEEE 754 semantics.

  If field is not an integer or double, or if the field does not yet exist, the transformation
  will set the field to the given value.  

  #### Declaration

  Objective-C  

      + (nonnull instancetype)fieldValueForIntegerIncrement:(int64_t)l;

  #### Parameters

  |-----------|------------------------------------|
  | ` `*l*` ` | The integer value to increment by. |

  #### Return Value

  The `FieldValue` sentinel for use in a call to `setData()` or `updateData()`.
- `
  ``
  ``
  `

  ### [+vectorWithArray:](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRFieldValue#/c:objc(cs)FIRFieldValue(cm)vectorWithArray:)

  `
  `  
  Creates a new `VectorValue` constructed with a copy of the given array of NSNumbers.  

  #### Declaration

  Objective-C  

      + (nonnull FIRVectorValue *)vectorWithArray:
          (nonnull NSArray<NSNumber *> *)array;

  #### Parameters

  |---------------|-------------------------------------------------------------------------|
  | ` `*array*` ` | Create a `VectorValue` instance with a copy of this array of NSNumbers. |

  #### Return Value

  A new `VectorValue` constructed with a copy of the given array of NSNumbers.