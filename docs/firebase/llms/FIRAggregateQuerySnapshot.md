# Source: https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRAggregateQuerySnapshot.md.txt

# FirebaseFirestore Framework Reference

# FIRAggregateQuerySnapshot


    @interface FIRAggregateQuerySnapshot : NSObject

The results of executing an `AggregateQuery`.
- `
  ``
  ``
  `

  ### [query](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRAggregateQuerySnapshot#/c:objc(cs)FIRAggregateQuerySnapshot(py)query)

  `
  `  
  The query that was executed to produce this result.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly) https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRAggregateQuery.html *_Nonnull query;

- `
  ``
  ``
  `

  ### [count](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRAggregateQuerySnapshot#/c:objc(cs)FIRAggregateQuerySnapshot(py)count)

  `
  `  
  The number of documents in the result set of the underlying query.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly) NSNumber *_Nonnull count;

- `
  ``
  ``
  `

  ### [-valueForAggregateField:](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRAggregateQuerySnapshot#/c:objc(cs)FIRAggregateQuerySnapshot(im)valueForAggregateField:)

  `
  `  
  Gets the aggregate result for the specified aggregate field without loss of precision. No
  coercion of data types or values is performed.

  See the `AggregateField` class for the expected aggregate result values and types. Numeric
  aggregate results will be boxed in an `NSNumber`.  
  Warning
  Throws an `InvalidArgument` exception if the aggregate field was not requested in the `AggregateQuery`.  
  See
  `AggregateField`  

  #### Declaration

  Objective-C  

      - (nonnull id)valueForAggregateField:
          (nonnull https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRAggregateField.html *)aggregateField;

  #### Parameters

  |------------------------|----------------------------------------------------------------------------------|
  | ` `*aggregateField*` ` | An instance of `AggregateField` that specifies which aggregate result to return. |

  #### Return Value

  Returns the aggregate result from the server without loss of precision.