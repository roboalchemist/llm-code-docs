# Source: https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Enums/FIRAggregateSource.md.txt

# FirebaseFirestore Framework Reference

# FIRAggregateSource

    enum FIRAggregateSource : NSUInteger {}

The sources from which an `AggregateQuery` can retrieve its results.

See `AggregateQuery.getAggregation(source:completion:)`.
- `
  ``
  ``
  `

  ### [FIRAggregateSourceServer](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Enums/FIRAggregateSource#/c:@E@FIRAggregateSource@FIRAggregateSourceServer)

  `
  `  
  Perform the aggregation on the server and download the result.

  The result received from the server is presented, unaltered, without considering any local
  state. That is, documents in the local cache are not taken into consideration, neither are
  local modifications not yet synchronized with the server. Previously-downloaded results, if
  any, are not used. Every request using this source necessarily involves a round trip to the
  server.

  The `AggregateQuery` will fail if the server cannot be reached, such as if the client is
  offline.  

  #### Declaration

  Objective-C  

      FIRAggregateSourceServer