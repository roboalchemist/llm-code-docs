# Source: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Enums.md.txt

# FirebaseFirestore Framework Reference

# Enumerations

The following enumerations are available globally.
- `


  ### [AggregateSource](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Enums/AggregateSource)


  ` The sources from which an `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/AggregateQuery` can retrieve its results.

  See `AggregateQuery.getAggregation(source:completion:)`.

  #### Declaration

  Swift

      enum AggregateSource : UInt, @unchecked Sendable

- `


  ### [DocumentChangeType](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Enums/DocumentChangeType)


  ` An enumeration of document change types.

  #### Declaration

  Swift

      @frozen enum DocumentChangeType : Int, @unchecked Sendable

- `


  ### [ServerTimestampBehavior](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Enums/ServerTimestampBehavior)


  ` Controls the return value for server timestamps that have not yet been set to
  their final value.

  #### Declaration

  Swift

      enum ServerTimestampBehavior : Int, @unchecked Sendable

- `


  ### [_ErrorType](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Enums/_ErrorType)


  ` Error codes used by Cloud Firestore.

  #### Declaration

  Swift

      typealias FirestoreErrorCode.Code._ErrorType = FirestoreErrorCode

- `


  ### [FirestoreSource](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Enums/FirestoreSource)


  ` An enum that configures the behavior of `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/DocumentReference#/c:objc(cs)FIRDocumentReference(im)getDocumentWithCompletion:` and
  `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/Query#/c:objc(cs)FIRQuery(im)getDocumentsWithCompletion:`. By providing a source enum the `getDocument[s]`
  methods can be configured to fetch results only from the server, only from
  the local cache, or attempt to fetch results from the server and fall back to
  the cache (which is the default).

  #### Declaration

  Swift

      enum FirestoreSource : UInt, @unchecked Sendable

- `


  ### [LoadBundleTaskState](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Enums/LoadBundleTaskState)


  ` Represents the state of bundle loading tasks.

  Both `error` and `inProgress` are final states: the task will be in either an aborted or
  completed state and there will be no more subsequent updates.

  #### Declaration

  Swift

      enum LoadBundleTaskState : Int, @unchecked Sendable

- `


  ### [ListenSource](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Enums/ListenSource)


  ` The source the snapshot listener retrieves data from.

  #### Declaration

  Swift

      enum ListenSource : UInt, @unchecked Sendable

- `


  ### [FirestoreDecodingError](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Enums/FirestoreDecodingError)


  ` Undocumented

  #### Declaration

  Swift

      public enum FirestoreDecodingError : Error

- `


  ### [FirestoreEncodingError](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Enums/FirestoreEncodingError)


  ` Undocumented

  #### Declaration

  Swift

      public enum FirestoreEncodingError : Error

- `


  ### [DecodingFailureStrategy](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Enums/DecodingFailureStrategy)


  ` The strategy to use when an error occurs during mapping Firestore documents
  to the target type of `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs/FirestoreQuery`.

  #### Declaration

  Swift

      public enum DecodingFailureStrategy

- `


  ### [QueryPredicate](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Enums/QueryPredicate)


  ` Query predicates that can be used to filter results fetched by `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs/FirestoreQuery`.

  Construct predicates using one of the following ways:

      let onlyFavourites: QueryPredicate = .whereField("isFavourite", isEqualTo: true)
      let onlyFavourites2: QueryPredicate = .isEqualTo("isFavourite", true)
      let onlyFavourites3: QueryPredicate = .where("isFavourite", isEqualTo: true)

  #### Declaration

  Swift

      public enum QueryPredicate