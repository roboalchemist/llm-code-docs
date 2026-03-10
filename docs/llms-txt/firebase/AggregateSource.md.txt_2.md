# Source: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Enums/AggregateSource.md.txt

# FirebaseFirestore Framework Reference

# AggregateSource

    enum AggregateSource : UInt, @unchecked Sendable

The sources from which an `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/AggregateQuery.html` can retrieve its results.

See `AggregateQuery.getAggregation(source:completion:)`.
- `


  ### [server](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Enums/AggregateSource#/c:@E@FIRAggregateSource@FIRAggregateSourceServer)


  ` Perform the aggregation on the server and download the result.

  The result received from the server is presented, unaltered, without considering any local
  state. That is, documents in the local cache are not taken into consideration, neither are
  local modifications not yet synchronized with the server. Previously-downloaded results, if
  any, are not used. Every request using this source necessarily involves a round trip to the
  server.

  The `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/AggregateQuery.html` will fail if the server cannot be reached, such as if the client is
  offline.

  #### Declaration

  Swift

      case server = 0