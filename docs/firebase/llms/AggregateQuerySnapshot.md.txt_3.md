# Source: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/AggregateQuerySnapshot.md.txt

# FirebaseFirestore Framework Reference

# AggregateQuerySnapshot

    class AggregateQuerySnapshot : NSObject, @unchecked Sendable

The results of executing an `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/AggregateQuery.html`.
- `


  ### [query](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/AggregateQuerySnapshot#/c:objc(cs)FIRAggregateQuerySnapshot(py)query)


  ` The query that was executed to produce this result.

  #### Declaration

  Swift

      var query: FIRAggregateQuery { get }

- `


  ### [count](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/AggregateQuerySnapshot#/c:objc(cs)FIRAggregateQuerySnapshot(py)count)


  ` The number of documents in the result set of the underlying query.

  #### Declaration

  Swift

      var count: NSNumber { get }

- `


  ### [get(_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/AggregateQuerySnapshot#/c:objc(cs)FIRAggregateQuerySnapshot(im)valueForAggregateField:)


  ` Gets the aggregate result for the specified aggregate field without loss of precision. No
  coercion of data types or values is performed.

  See the `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/AggregateField.html` class for the expected aggregate result values and types. Numeric
  aggregate results will be boxed in an `NSNumber`.
  Warning
  Throws an `InvalidArgument` exception if the aggregate field was not requested in the `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/AggregateQuery.html`. See
  `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/AggregateField.html`

  #### Declaration

  Swift

      func get(_ aggregateField: FIRAggregateField) -> Any

  #### Parameters

  |---|---|
  | ` aggregateField ` | An instance of `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/AggregateField.html` that specifies which aggregate result to return. |

  #### Return Value

  Returns the aggregate result from the server without loss of precision.