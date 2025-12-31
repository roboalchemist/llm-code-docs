# Source: https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRAggregateField.md.txt

# FirebaseFirestore Framework Reference

# FIRAggregateField


    @interface FIRAggregateField : NSObject

Represents an aggregation that can be performed by Firestore.
- `
  ``
  ``
  `

  ### [+aggregateFieldForCount](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRAggregateField#/c:objc(cs)FIRAggregateField(cm)aggregateFieldForCount)

  `
  `  
  Create an `AggregateField` object that can be used to compute the count of
  documents in the result set of a query.

  The result of a count operation will always be a 64-bit integer value.  

  #### Declaration

  Objective-C  

      + (nonnull instancetype)aggregateFieldForCount;

  #### Return Value

  `AggregateField` object that can be used to compute the count of
  documents in the result set of a query.
- `
  ``
  ``
  `

  ### [+aggregateFieldForSumOfField:](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRAggregateField#/c:objc(cs)FIRAggregateField(cm)aggregateFieldForSumOfField:)

  `
  `  
  Create an `AggregateField` object that can be used to compute the sum of
  a specified field over a range of documents in the result set of a query.

  The result of a sum operation will always be a 64-bit integer value, a double, or NaN.
  - Summing over zero documents or fields will result in 0L.
  - Summing over NaN will result in a double value representing NaN.
  - A sum that overflows the maximum representable 64-bit integer value will result in a double return value. This may result in lost precision of the result.
  - A sum that overflows the maximum representable double value will result in a double return
    value representing infinity.

  #### Declaration

  Objective-C  

      + (nonnull instancetype)aggregateFieldForSumOfField:(nonnull NSString *)field;

  #### Parameters

  |---------------|---------------------------------------------------|
  | ` `*field*` ` | Specifies the field to sum across the result set. |

  #### Return Value

  `AggregateField` object that can be used to compute the sum of
  a specified field over a range of documents in the result set of a query.
- `
  ``
  ``
  `

  ### [+aggregateFieldForSumOfFieldPath:](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRAggregateField#/c:objc(cs)FIRAggregateField(cm)aggregateFieldForSumOfFieldPath:)

  `
  `  
  Create an `AggregateField` object that can be used to compute the sum of
  a specified field over a range of documents in the result set of a query.

  The result of a sum operation will always be a 64-bit integer value, a double, or NaN.
  - Summing over zero documents or fields will result in 0L.
  - Summing over NaN will result in a double value representing NaN.
  - A sum that overflows the maximum representable 64-bit integer value will result in a double return value. This may result in lost precision of the result.
  - A sum that overflows the maximum representable double value will result in a double return
    value representing infinity.

  #### Declaration

  Objective-C  

      + (nonnull instancetype)aggregateFieldForSumOfFieldPath:
          (nonnull https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRFieldPath.html *)fieldPath;

  #### Parameters

  |-------------------|---------------------------------------------------|
  | ` `*fieldPath*` ` | Specifies the field to sum across the result set. |

  #### Return Value

  `AggregateField` object that can be used to compute the sum of
  a specified field over a range of documents in the result set of a query.
- `
  ``
  ``
  `

  ### [+aggregateFieldForAverageOfField:](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRAggregateField#/c:objc(cs)FIRAggregateField(cm)aggregateFieldForAverageOfField:)

  `
  `  
  Create an `AggregateField` object that can be used to compute the average of
  a specified field over a range of documents in the result set of a query.

  The result of an average operation will always be a double or NaN.
  - Averaging over zero documents or fields will result in a double value representing NaN.
  - Averaging over NaN will result in a double value representing NaN.

  #### Declaration

  Objective-C  

      + (nonnull instancetype)aggregateFieldForAverageOfField:
          (nonnull NSString *)field;

  #### Parameters

  |---------------|-------------------------------------------------------|
  | ` `*field*` ` | Specifies the field to average across the result set. |

  #### Return Value

  `AggregateField` object that can be used to compute the average of
  a specified field over a range of documents in the result set of a query.
- `
  ``
  ``
  `

  ### [+aggregateFieldForAverageOfFieldPath:](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRAggregateField#/c:objc(cs)FIRAggregateField(cm)aggregateFieldForAverageOfFieldPath:)

  `
  `  
  Create an `AggregateField` object that can be used to compute the average of
  a specified field over a range of documents in the result set of a query.

  The result of an average operation will always be a double or NaN.
  - Averaging over zero documents or fields will result in a double value representing NaN.
  - Averaging over NaN will result in a double value representing NaN.

  #### Declaration

  Objective-C  

      + (nonnull instancetype)aggregateFieldForAverageOfFieldPath:
          (nonnull https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRFieldPath.html *)fieldPath;

  #### Parameters

  |-------------------|-------------------------------------------------------|
  | ` `*fieldPath*` ` | Specifies the field to average across the result set. |

  #### Return Value

  `AggregateField` object that can be used to compute the average of
  a specified field over a range of documents in the result set of a query.