# Source: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/AggregateField.md.txt

# FirebaseFirestore Framework Reference

# AggregateField

    class AggregateField : NSObject, @unchecked Sendable

Represents an aggregation that can be performed by Firestore.
- `


  ### [count()](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/AggregateField#/c:objc(cs)FIRAggregateField(cm)aggregateFieldForCount)


  ` Create an `AggregateField` object that can be used to compute the count of
  documents in the result set of a query.

  The result of a count operation will always be a 64-bit integer value.

  #### Declaration

  Swift

      class func count() -> Self

  #### Return Value

  `AggregateField` object that can be used to compute the count of
  documents in the result set of a query.
- `


  ### [sum(_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/AggregateField#/c:objc(cs)FIRAggregateField(cm)aggregateFieldForSumOfField:)


  ` Create an `AggregateField` object that can be used to compute the sum of
  a specified field over a range of documents in the result set of a query.

  The result of a sum operation will always be a 64-bit integer value, a double, or NaN.
  - Summing over zero documents or fields will result in 0L.
  - Summing over NaN will result in a double value representing NaN.
  - A sum that overflows the maximum representable 64-bit integer value will result in a double return value. This may result in lost precision of the result.
  - A sum that overflows the maximum representable double value will result in a double return
    value representing infinity.

  #### Declaration

  Swift

      class func sum(_ field: String) -> Self

  #### Parameters

  |---|---|
  | ` field ` | Specifies the field to sum across the result set. |

  #### Return Value

  `AggregateField` object that can be used to compute the sum of
  a specified field over a range of documents in the result set of a query.
- `


  ### [sum(_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/AggregateField#/c:objc(cs)FIRAggregateField(cm)aggregateFieldForSumOfFieldPath:)


  ` Create an `AggregateField` object that can be used to compute the sum of
  a specified field over a range of documents in the result set of a query.

  The result of a sum operation will always be a 64-bit integer value, a double, or NaN.
  - Summing over zero documents or fields will result in 0L.
  - Summing over NaN will result in a double value representing NaN.
  - A sum that overflows the maximum representable 64-bit integer value will result in a double return value. This may result in lost precision of the result.
  - A sum that overflows the maximum representable double value will result in a double return
    value representing infinity.

  #### Declaration

  Swift

      class func sum(_ fieldPath: FIRFieldPath) -> Self

  #### Parameters

  |---|---|
  | ` fieldPath ` | Specifies the field to sum across the result set. |

  #### Return Value

  `AggregateField` object that can be used to compute the sum of
  a specified field over a range of documents in the result set of a query.
- `


  ### [average(_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/AggregateField#/c:objc(cs)FIRAggregateField(cm)aggregateFieldForAverageOfField:)


  ` Create an `AggregateField` object that can be used to compute the average of
  a specified field over a range of documents in the result set of a query.

  The result of an average operation will always be a double or NaN.
  - Averaging over zero documents or fields will result in a double value representing NaN.
  - Averaging over NaN will result in a double value representing NaN.

  #### Declaration

  Swift

      class func average(_ field: String) -> Self

  #### Parameters

  |---|---|
  | ` field ` | Specifies the field to average across the result set. |

  #### Return Value

  `AggregateField` object that can be used to compute the average of
  a specified field over a range of documents in the result set of a query.
- `


  ### [average(_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/AggregateField#/c:objc(cs)FIRAggregateField(cm)aggregateFieldForAverageOfFieldPath:)


  ` Create an `AggregateField` object that can be used to compute the average of
  a specified field over a range of documents in the result set of a query.

  The result of an average operation will always be a double or NaN.
  - Averaging over zero documents or fields will result in a double value representing NaN.
  - Averaging over NaN will result in a double value representing NaN.

  #### Declaration

  Swift

      class func average(_ fieldPath: FIRFieldPath) -> Self

  #### Parameters

  |---|---|
  | ` fieldPath ` | Specifies the field to average across the result set. |

  #### Return Value

  `AggregateField` object that can be used to compute the average of
  a specified field over a range of documents in the result set of a query.