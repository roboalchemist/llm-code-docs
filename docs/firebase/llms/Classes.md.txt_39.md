# Source: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes.md.txt

# FirebaseFirestore Framework Reference

# Classes

The following classes are available globally.
- `


  ### [CollectionReference](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/CollectionReference)


  ` A `CollectionReference` object can be used for adding documents, getting document references,
  and querying for documents (using the methods inherited from `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/Query`).

  #### Declaration

  Swift

      class CollectionReference : https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/Query, @unchecked Sendable

- `


  ### [Firestore](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/Firestore)


  ` `Firestore` represents a Firestore Database and is the entry point for all Firestore
  operations.

  #### Declaration

  Swift

      class Firestore : NSObject

- `


  ### [DocumentReference](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/DocumentReference)


  ` A `DocumentReference` refers to a document location in a Firestore database and can be
  used to write, read, or listen to the location. The document at the referenced location
  may or may not exist. A `DocumentReference` can also be used to create a `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/CollectionReference` to
  a subcollection.

  #### Declaration

  Swift

      class DocumentReference : NSObject, @unchecked Sendable

- `


  ### [DocumentSnapshot](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/DocumentSnapshot)


  ` A `DocumentSnapshot` contains data read from a document in your Firestore database. The data
  can be extracted with the `data` property or by using subscript syntax to access a specific
  field.

  For a `DocumentSnapshot` that points to a non-existing document, any data access will return
  `nil`. You can use the `exists` property to explicitly verify a documents existence.

  #### Declaration

  Swift

      class DocumentSnapshot : NSObject, @unchecked Sendable

- `


  ### [Transaction](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/Transaction)


  ` `Transaction` provides methods to read and write data within a transaction.
  See
  `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/Firestore#/s:So12FIRFirestoreC17FirebaseFirestoreE14runTransactionyypSgAESo14FIRTransactionC_SAySo7NSErrorCSgGSgtYTcYaKF`

  #### Declaration

  Swift

      class Transaction : NSObject

- `


  ### [WriteBatch](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/WriteBatch)


  ` A write batch is used to perform multiple writes as a single atomic unit.

  A WriteBatch object can be acquired by calling `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/Firestore#/c:objc(cs)FIRFirestore(im)batch`. It provides methods for
  adding writes to the write batch. None of the writes will be committed (or visible locally)
  until `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/WriteBatch#/c:objc(cs)FIRWriteBatch(im)commit` is called.

  Unlike transactions, write batches are persisted offline and therefore are preferable when you
  don't need to condition your writes on read data.

  #### Declaration

  Swift

      class WriteBatch : NSObject

- `


  ### [FieldValue](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FieldValue)


  ` Sentinel values that can be used when writing document fields with `setData()` or `updateData()`.

  #### Declaration

  Swift

      class FieldValue : NSObject, @unchecked Sendable

- `


  ### [AggregateField](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/AggregateField)


  ` Represents an aggregation that can be performed by Firestore.

  #### Declaration

  Swift

      class AggregateField : NSObject, @unchecked Sendable

- `


  ### [AggregateQuery](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/AggregateQuery)


  ` A query that calculates aggregations over an underlying query.

  #### Declaration

  Swift

      class AggregateQuery : NSObject, @unchecked Sendable

- `


  ### [AggregateQuerySnapshot](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/AggregateQuerySnapshot)


  ` The results of executing an `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/AggregateQuery`.

  #### Declaration

  Swift

      class AggregateQuerySnapshot : NSObject, @unchecked Sendable

- `


  ### [DocumentChange](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/DocumentChange)


  ` A `DocumentChange` represents a change to the documents matching a query. It contains the
  document affected and the type of change that occurred (added, modified, or removed).

  #### Declaration

  Swift

      class DocumentChange : NSObject, @unchecked Sendable

- `


  ### [QueryDocumentSnapshot](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/QueryDocumentSnapshot)


  ` A `QueryDocumentSnapshot` contains data read from a document in your Firestore database as
  part of a query. The document is guaranteed to exist and its data can be extracted with the
  `data` property or by using subscript syntax to access a specific field.

  A `QueryDocumentSnapshot` offers the same API surface as a `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/DocumentSnapshot`. As
  deleted documents are not returned from queries, its `exists` property will always be true and
  `data()` will never return `nil`.

  #### Declaration

  Swift

      class QueryDocumentSnapshot : https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/DocumentSnapshot

- `


  ### [FieldPath](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FieldPath)


  ` A `FieldPath` refers to a field in a document. The path may consist of a single field name
  (referring to a top level field in the document), or a list of field names (referring to a nested
  field in the document).

  #### Declaration

  Swift

      class FieldPath : NSObject, NSCopying, @unchecked Sendable

- `


  ### [Filter](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/Filter)


  ` A Filter represents a restriction on one or more field values and can be used to refine
  the results of a Query.

  #### Declaration

  Swift

      class Filter : NSObject, @unchecked Sendable

- `


  ### [FirestoreSettings](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FirestoreSettings)


  ` Settings used to configure a `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/Firestore` instance.

  #### Declaration

  Swift

      class FirestoreSettings : NSObject, NSCopying

- `


  ### [GeoPoint](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/GeoPoint)


  ` An immutable object representing a geographical point in Firestore. The point is represented as
  a latitude/longitude pair.

  Latitude values are in the range of \[-90, 90\].
  Longitude values are in the range of \[-180, 180\].

  #### Declaration

  Swift

      class GeoPoint : NSObject, NSCopying, @unchecked Sendable

- `


  ### [LoadBundleTaskProgress](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/LoadBundleTaskProgress)


  ` Represents a progress update or a final state from loading bundles.

  #### Declaration

  Swift

      class LoadBundleTaskProgress : NSObject, @unchecked Sendable

- `


  ### [LoadBundleTask](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/LoadBundleTask)


  ` Represents the task of loading a Firestore bundle. Observers can be registered with this task to
  observe the bundle loading progress, as well as task completion and error events.

  #### Declaration

  Swift

      class LoadBundleTask : NSObject

- `


  ### [PersistentCacheSettings](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/PersistentCacheSettings)


  ` Configures the SDK to use a persistent cache. Firestore documents and mutations are persisted
  across App restart.

  This is the default cache type unless explicitly specified otherwise.

  To use, create an instance using one of the initializers, then set the instance to
  `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FirestoreSettings#/c:objc(cs)FIRFirestoreSettings(py)cacheSettings`, and use `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FirestoreSettings` instance to configure Firestore
  SDK.

  #### Declaration

  Swift

      class PersistentCacheSettings : NSObject, NSCopying, https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols#/c:objc(pl)FIRLocalCacheSettings

- `


  ### [MemoryEagerGCSetting](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/MemoryEagerGCSetting)


  ` Configures the SDK to use an eager garbage collector for memory cache.

  Once configured, the SDK will remove any Firestore documents from memory as soon as they are not
  used by any active queries.

  To use, create an instance using the initializer, then initialize
  `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/MemoryCacheSettings` with this instance. This is the default garbage collector, so alternatively
  you can use the default initializer of `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/MemoryCacheSettings`.

  #### Declaration

  Swift

      class MemoryEagerGCSetting : NSObject, NSCopying, https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols#/c:objc(pl)FIRMemoryGarbageCollectorSettings

- `


  ### [MemoryLRUGCSettings](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/MemoryLRUGCSettings)


  ` Configures the SDK to use a least-recently-used garbage collector for memory cache.

  Once configured, the SDK will attempt to remove documents that are least recently used in
  batches, if the current cache size is larger than the given target cache size. Default cache size
  is 100MB.

  To use, create an instance using one of the initializers, then initialize
  `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/MemoryCacheSettings` with this instance.

  #### Declaration

  Swift

      class MemoryLRUGCSettings : NSObject, NSCopying, https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols#/c:objc(pl)FIRMemoryGarbageCollectorSettings

- `


  ### [MemoryCacheSettings](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/MemoryCacheSettings)


  ` Configures the SDK to use a memory cache. Firestore documents and mutations are NOT persisted
  across App restart.

  To use, create an instance using one of the initializer, then set the instance to
  `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FirestoreSettings#/c:objc(cs)FIRFirestoreSettings(py)cacheSettings`, and use `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FirestoreSettings` instance to configure Firestore
  SDK.

  #### Declaration

  Swift

      class MemoryCacheSettings : NSObject, NSCopying, https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols#/c:objc(pl)FIRLocalCacheSettings

- `


  ### [ExprBridge](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes#/c:objc(cs)FIRExprBridge)


  ` Undocumented

  #### Declaration

  Swift

      class ExprBridge : NSObject, @unchecked Sendable

- `


  ### [FieldBridge](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FieldBridge)


  ` Undocumented

  #### Declaration

  Swift

      class FieldBridge : https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes#/c:objc(cs)FIRExprBridge, @unchecked Sendable

- `


  ### [ConstantBridge](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/ConstantBridge)


  ` Undocumented

  #### Declaration

  Swift

      class ConstantBridge : https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes#/c:objc(cs)FIRExprBridge, @unchecked Sendable

- `


  ### [FunctionExprBridge](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExprBridge)


  ` Undocumented

  #### Declaration

  Swift

      class FunctionExprBridge : https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes#/c:objc(cs)FIRExprBridge, @unchecked Sendable

- `


  ### [AggregateFunctionBridge](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/AggregateFunctionBridge)


  ` Undocumented

  #### Declaration

  Swift

      class AggregateFunctionBridge : NSObject, @unchecked Sendable

- `


  ### [OrderingBridge](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/OrderingBridge)


  ` Undocumented

  #### Declaration

  Swift

      class OrderingBridge : NSObject, @unchecked Sendable

- `


  ### [StageBridge](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/StageBridge)


  ` Undocumented

  #### Declaration

  Swift

      class StageBridge : NSObject, @unchecked Sendable

- `


  ### [CollectionSourceStageBridge](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/CollectionSourceStageBridge)


  ` Undocumented

  #### Declaration

  Swift

      class CollectionSourceStageBridge : https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/StageBridge, @unchecked Sendable

- `


  ### [DatabaseSourceStageBridge](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/DatabaseSourceStageBridge)


  ` Undocumented

  #### Declaration

  Swift

      class DatabaseSourceStageBridge : https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/StageBridge, @unchecked Sendable

- `


  ### [CollectionGroupSourceStageBridge](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/CollectionGroupSourceStageBridge)


  ` Undocumented

  #### Declaration

  Swift

      class CollectionGroupSourceStageBridge : https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/StageBridge, @unchecked Sendable

- `


  ### [DocumentsSourceStageBridge](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/DocumentsSourceStageBridge)


  ` Undocumented

  #### Declaration

  Swift

      class DocumentsSourceStageBridge : https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/StageBridge, @unchecked Sendable

- `


  ### [WhereStageBridge](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/WhereStageBridge)


  ` Undocumented

  #### Declaration

  Swift

      class WhereStageBridge : https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/StageBridge, @unchecked Sendable

- `


  ### [LimitStageBridge](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/LimitStageBridge)


  ` Undocumented

  #### Declaration

  Swift

      class LimitStageBridge : https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/StageBridge, @unchecked Sendable

- `


  ### [OffsetStageBridge](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/OffsetStageBridge)


  ` Undocumented

  #### Declaration

  Swift

      class OffsetStageBridge : https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/StageBridge, @unchecked Sendable

- `


  ### [AddFieldsStageBridge](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/AddFieldsStageBridge)


  ` Undocumented

  #### Declaration

  Swift

      class AddFieldsStageBridge : https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/StageBridge, @unchecked Sendable

- `


  ### [RemoveFieldsStageBridge](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/RemoveFieldsStageBridge)


  ` Undocumented

  #### Declaration

  Swift

      class RemoveFieldsStageBridge : https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/StageBridge, @unchecked Sendable

- `


  ### [SelectStageBridge](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/SelectStageBridge)


  ` Undocumented

  #### Declaration

  Swift

      class SelectStageBridge : https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/StageBridge, @unchecked Sendable

- `


  ### [DistinctStageBridge](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/DistinctStageBridge)


  ` Undocumented

  #### Declaration

  Swift

      class DistinctStageBridge : https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/StageBridge, @unchecked Sendable

- `


  ### [AggregateStageBridge](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/AggregateStageBridge)


  ` Undocumented

  #### Declaration

  Swift

      class AggregateStageBridge : https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/StageBridge, @unchecked Sendable

- `


  ### [FindNearestStageBridge](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FindNearestStageBridge)


  ` Undocumented

  #### Declaration

  Swift

      class FindNearestStageBridge : https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/StageBridge, @unchecked Sendable

- `


  ### [SortStageBridge](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/SortStageBridge)


  ` Undocumented

  #### Declaration

  Swift

      class SortStageBridge : https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/StageBridge, @unchecked Sendable

- `


  ### [ReplaceWithStageBridge](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/ReplaceWithStageBridge)


  ` Undocumented

  #### Declaration

  Swift

      class ReplaceWithStageBridge : https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/StageBridge, @unchecked Sendable

- `


  ### [SampleStageBridge](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/SampleStageBridge)


  ` Undocumented

  #### Declaration

  Swift

      class SampleStageBridge : https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/StageBridge, @unchecked Sendable

- `


  ### [UnionStageBridge](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/UnionStageBridge)


  ` Undocumented

  #### Declaration

  Swift

      class UnionStageBridge : https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/StageBridge, @unchecked Sendable

- `


  ### [UnnestStageBridge](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/UnnestStageBridge)


  ` Undocumented

  #### Declaration

  Swift

      class UnnestStageBridge : https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/StageBridge, @unchecked Sendable

- `


  ### [RawStageBridge](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/RawStageBridge)


  ` Undocumented

  #### Declaration

  Swift

      class RawStageBridge : https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/StageBridge, @unchecked Sendable

- `


  ### [__PipelineResultBridge](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/__PipelineResultBridge)


  ` Undocumented

  #### Declaration

  Swift

      class __PipelineResultBridge : NSObject, @unchecked Sendable

- `


  ### [__PipelineResultChangeBridge](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/__PipelineResultChangeBridge)


  ` Undocumented

  #### Declaration

  Swift

      class __PipelineResultChangeBridge : NSObject, @unchecked Sendable

- `


  ### [__PipelineSnapshotBridge](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/__PipelineSnapshotBridge)


  ` Undocumented

  #### Declaration

  Swift

      class __PipelineSnapshotBridge : NSObject, @unchecked Sendable

- `


  ### [PipelineBridge](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/PipelineBridge)


  ` Undocumented

  #### Declaration

  Swift

      class PipelineBridge : NSObject, @unchecked Sendable

- `


  ### [__RealtimePipelineSnapshotBridge](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/__RealtimePipelineSnapshotBridge)


  ` Undocumented

  #### Declaration

  Swift

      class __RealtimePipelineSnapshotBridge : NSObject, @unchecked Sendable

- `


  ### [__PipelineListenOptionsBridge](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/__PipelineListenOptionsBridge)


  ` Undocumented

  #### Declaration

  Swift

      class __PipelineListenOptionsBridge : NSObject, @unchecked Sendable

- `


  ### [RealtimePipelineBridge](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/RealtimePipelineBridge)


  ` Undocumented

  #### Declaration

  Swift

      class RealtimePipelineBridge : NSObject, @unchecked Sendable

- `


  ### [Query](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/Query)


  ` A `Query` refers to a query which you can read or listen to. You can also construct
  refined `Query` objects by adding filters and ordering.

  #### Declaration

  Swift

      class Query : NSObject, @unchecked Sendable

- `


  ### [QuerySnapshot](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/QuerySnapshot)


  ` A `QuerySnapshot` contains zero or more `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/DocumentSnapshot` objects. It can be enumerated
  using the `documents` property and its size can be inspected with `isEmpty` and
  `count`.

  #### Declaration

  Swift

      class QuerySnapshot : NSObject, @unchecked Sendable

- `


  ### [SnapshotListenOptions](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/SnapshotListenOptions)


  ` Options to configure the behavior of `Firestore.addSnapshotListenerWithOptions()`. Instances
  of this class control settings like whether metadata-only changes trigger events and the
  preferred data source.

  #### Declaration

  Swift

      class SnapshotListenOptions : NSObject, @unchecked Sendable

- `


  ### [SnapshotMetadata](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/SnapshotMetadata)


  ` Metadata about a snapshot, describing the state of the snapshot.

  #### Declaration

  Swift

      class SnapshotMetadata : NSObject, @unchecked Sendable

- `


  ### [TransactionOptions](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/TransactionOptions)


  ` Options to customize the behavior of `Firestore.runTransactionWithOptions()`.

  #### Declaration

  Swift

      class TransactionOptions : NSObject, NSCopying

- `


  ### [AggregateFunction](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/AggregateFunction)


  ` Represents an aggregate function in a pipeline.

  An `AggregateFunction` is a function that computes a single value from a set of input values.

  `AggregateFunction`s are typically used in the `aggregate` stage of a pipeline.

  #### Declaration

  Swift

      public class AggregateFunction : AggregateBridgeWrapper, @unchecked Sendable

- `


  ### [CountAll](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/CountAll)


  ` Represents an aggregation that counts all documents in the input set.

  `CountAll` is used within the `aggregate` pipeline stage to get the total number of documents
  that match the query criteria up to that point.

  Example usage:

      // Count all books in the collection
      firestore.pipeline()
        .collection("books")
        .aggregate([
          CountAll().as("totalBooks")
        ])

      // Count all sci-fi books published after 1960
      firestore.pipeline()
        .collection("books")
        .where(Field("genre").equal("Science Fiction") && Field("published").greaterThan(1960))
        .aggregate([
          CountAll().as("sciFiBooksCount")
        ])

  #### Declaration

  Swift

      public class CountAll : https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/AggregateFunction, @unchecked Sendable

- `


  ### [ArrayExpression](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/ArrayExpression)


  ` An expression that represents an array of values.

  `ArrayExpression` is used to construct an array from a list of `Sendable`
  values, which can include literals (like numbers and strings) as well as other
  `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression` instances. This allows for the creation of dynamic arrays within
  a pipeline.

  Example:

      ArrayExpression([
        1,
        2,
        Field("genre"),
        Field("rating").multiply(10),
        ArrayExpression([Field("title")]),
        MapExpression(["published": Field("published")]),
      ]).as("metadataArray")

  #### Declaration

  Swift

      public class ArrayExpression : https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression, @unchecked Sendable

- `


  ### [ConditionalExpression](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/ConditionalExpression)


  ` A `ConditionalExpression` is a `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression` that evaluates to one of two expressions
  based on a boolean condition.

  This is equivalent to a ternary operator (`condition ? then : else`).

  Example of using `ConditionalExpression`:

      // Create a new field "status" based on the "rating" field.
      // If rating > 4.5, status is "top_rated", otherwise "regular".
      firestore.pipeline()
        .collection("products")
        .addFields([
          ConditionalExpression(
            Field("rating").greaterThan(4.5),
            then: Constant("top_rated"),
            else: Constant("regular")
          ).as("status")
        ])

  #### Declaration

  Swift

      public class ConditionalExpression : https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression, @unchecked Sendable

- `


  ### [CurrentTimestamp](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/CurrentTimestamp)


  ` An expression that represents a server-side timestamp.

  `CurrentTimestamp` is used to generate a timestamp on the server.
  This is useful for recording current date and time.

  Example:

      CurrentTimestamp().as("createdAt")

  #### Declaration

  Swift

      public class CurrentTimestamp : https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression, @unchecked Sendable

- `


  ### [ErrorExpression](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/ErrorExpression)


  ` An expression that produces an error with a custom error message.
  This is primarily used for debugging purposes.

  Example:

      ErrorExpression("This is a custom error message").as("errorResult")

  #### Declaration

  Swift

      public class ErrorExpression : https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression, @unchecked Sendable

- `


  ### [FunctionExpression](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression)


  ` Represents a function call in a pipeline.

  A `FunctionExpression` is an expression that represents a function call with a given name and
  arguments.

  `FunctionExpression`s are typically used to perform operations on data in a pipeline, such as
  mathematical calculations, string manipulations, or array operations.

  #### Declaration

  Swift

      public class FunctionExpression : https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression, BridgeWrapper, @unchecked Sendable

- `


  ### [MapExpression](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/MapExpression)


  ` An expression that represents a map (or dictionary) of key-value pairs.

  `MapExpression` is used to construct a map from a dictionary of `String` keys
  and `Sendable` values. The values can be literals (like numbers and strings)
  or other `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression` instances, allowing for the creation of dynamic nested
  objects within a pipeline.

  Example:

      MapExpression([
        "genre": Field("genre"),
        "rating": Field("rating").multiply(10),
        "nestedArray": ArrayExpression([Field("title")]),
        "nestedMap": MapExpression(["published": Field("published")]),
      ]).as("metadata")

  #### Declaration

  Swift

      public class MapExpression : https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression, @unchecked Sendable