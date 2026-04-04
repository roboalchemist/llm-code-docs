# Source: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/AggregateQuery.md.txt

# FirebaseFirestore Framework Reference

# AggregateQuery

    class AggregateQuery : NSObject, @unchecked Sendable

A query that calculates aggregations over an underlying query.
- `


  ### [query](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/AggregateQuery#/c:objc(cs)FIRAggregateQuery(py)query)


  ` The query whose aggregations will be calculated by this object.

  #### Declaration

  Swift

      var query: FIRQuery { get }

- `


  ### [getAggregation(source:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/AggregateQuery#/c:objc(cs)FIRAggregateQuery(im)aggregationWithSource:completion:)


  ` Executes this query.

  #### Declaration

  Swift

      func getAggregation(source: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Enums/AggregateSource.html) async throws -> FIRAggregateQuerySnapshot

  #### Parameters

  |---|---|
  | ` source ` | The source from which to acquire the aggregate results. |
  | ` completion ` | a block to execute once the results have been successfully read. snapshot will be `nil` only if error is `non-nil`. |