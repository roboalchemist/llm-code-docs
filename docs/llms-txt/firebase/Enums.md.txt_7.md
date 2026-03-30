# Source: https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Enums.md.txt

# FirebaseFirestore Framework Reference

# Enumerations

The following enumerations are available globally.
- `


  ### [FIRAggregateSource](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Enums/FIRAggregateSource)


  ` The sources from which an `AggregateQuery` can retrieve its results.

  See `AggregateQuery.getAggregation(source:completion:)`.

  #### Declaration

  Objective-C

      enum FIRAggregateSource : NSUInteger {}

- `


  ### [FIRDocumentChangeType](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Enums/FIRDocumentChangeType)


  ` An enumeration of document change types.

  #### Declaration

  Objective-C

      enum FIRDocumentChangeType : NSInteger {}

- `


  ### [FIRServerTimestampBehavior](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Enums/FIRServerTimestampBehavior)


  ` Controls the return value for server timestamps that have not yet been set to
  their final value.

  #### Declaration

  Objective-C

      enum FIRServerTimestampBehavior : NSInteger {}

- `


  ### [FIRFirestoreErrorCode](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Enums/FIRFirestoreErrorCode)


  ` Error codes used by Cloud Firestore.

  #### Declaration

  Objective-C

      enum FIRFirestoreErrorCode : NSInteger {}

- `


  ### [FIRFirestoreSource](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Enums/FIRFirestoreSource)


  ` An enum that configures the behavior of `DocumentReference.getDocument()` and
  `Query.getDocuments()`. By providing a source enum the `getDocument[s]`
  methods can be configured to fetch results only from the server, only from
  the local cache, or attempt to fetch results from the server and fall back to
  the cache (which is the default).

  #### Declaration

  Objective-C

      enum FIRFirestoreSource : NSUInteger {}

- `


  ### [FIRLoadBundleTaskState](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Enums/FIRLoadBundleTaskState)


  ` Represents the state of bundle loading tasks.

  Both `error` and `inProgress` are final states: the task will be in either an aborted or
  completed state and there will be no more subsequent updates.

  #### Declaration

  Objective-C

      enum FIRLoadBundleTaskState : NSInteger {}

- `


  ### [FIRListenSource](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Enums/FIRListenSource)


  ` The source the snapshot listener retrieves data from.

  #### Declaration

  Objective-C

      enum FIRListenSource : NSUInteger {}