# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/package-summary.md.txt

# com.google.firebase.firestore

# com.google.firebase.firestore

## Annotations

|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentId` | Annotation used to mark a POJO property to be automatically populated with the document's ID when the POJO is created from a Cloud Firestore document (for example, via `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot#toObject(java.lang.Class<T>)`). |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/Exclude` | Marks a field as excluded from the database instance. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/IgnoreExtraProperties` | Properties that don't map to class fields are ignored when serializing to a class annotated with this annotation. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/PropertyName` | Marks a field to be renamed when serialized. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/ServerTimestamp` | Annotation used to mark a timestamp field to be populated with a server timestamp. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/ThrowOnExtraProperties` | Properties that don't map to class fields when serializing to a class annotated with this annotation cause an exception to be thrown. |

## Interfaces

|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/EventListener` | An interface for event listeners. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/ListenerRegistration` | Represents a listener that can be removed by calling `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/ListenerRegistration#remove()`. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/LocalCacheSettings` | Marker interface implemented by all supported cache settings. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/MemoryGarbageCollectorSettings` |   |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/OnProgressListener` | A listener that is called periodically during execution of a `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/LoadBundleTask`. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/Transaction.Function` | An interface for providing code to be executed within a transaction context. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/WriteBatch.Function` | An interface for providing code to be executed within a `WriteBatch` context. |

## Classes

|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/AggregateField` | Represents an aggregation that can be performed by Firestore. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/AggregateField.AverageAggregateField` | Represents an "average" aggregation that can be performed by Firestore. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/AggregateField.CountAggregateField` | Represents a "count" aggregation that can be performed by Firestore. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/AggregateField.SumAggregateField` | Represents a "sum" aggregation that can be performed by Firestore. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/AggregateQuery` | A query that calculates aggregations over an underlying query. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/AggregateQuerySnapshot` | The results of executing an `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/AggregateQuery`. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/Blob` | Immutable class representing an array of bytes in Cloud Firestore. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/CollectionReference` | A `CollectionReference` can be used for adding documents, getting document references, and querying for documents (using the methods inherited from `Query`). |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentChange` | A `DocumentChange` represents a change to the documents matching a query. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentReference` | A `DocumentReference` refers to a document location in a Cloud Firestore database and can be used to write, read, or listen to the location. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot` | A `DocumentSnapshot` contains data read from a document in your Cloud Firestore database. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FieldPath` | A `FieldPath` refers to a field in a document. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FieldValue` | Sentinel values that can be used when writing document fields with `set()` or ` update()`. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/Filter` | A `Filter` represents a restriction on one or more field values and can be used to refine the results of a `Query`. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestore` | Represents a Cloud Firestore database and is the entry point for all Cloud Firestore operations. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestoreSettings` | Settings used to configure a `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestore` instance. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestoreSettings.Builder` | A Builder for creating `FirebaseFirestoreSettings`. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirestoreKt` |   |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/GeoPoint` | Immutable class representing a `GeoPoint` in Cloud Firestore |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/LoadBundleTask` | Represents the task of loading a Firestore bundle. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/LoadBundleTaskProgress` | Represents a progress update or a final state from loading bundles. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/MemoryCacheSettings` | Configures the SDK to use a memory cache. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/MemoryCacheSettings.Builder` | A Builder for creating `MemoryCacheSettings` instance. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/MemoryEagerGcSettings` | Configures the SDK to use an eager garbage collector for memory cache. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/MemoryEagerGcSettings.Builder` |   |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/MemoryLruGcSettings` | Configures the SDK to use a Least-Recently-Used garbage collector for memory cache. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/MemoryLruGcSettings.Builder` |   |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/PersistentCacheIndexManager` | Persistent cache indexes can improve performance of local query execution. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/PersistentCacheSettings` | Configures the SDK to use a persistent cache. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/PersistentCacheSettings.Builder` | A Builder for creating `PersistentCacheSettings` instance. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/Pipeline` | A `Pipeline` is composed of a sequence of stages. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/Pipeline.ExecuteOptions` |   |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/Pipeline.ExecuteOptions.IndexMode` |   |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/Pipeline.Snapshot` | A `Snapshot` contains the results of a pipeline execution. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/PipelineResult` | Represents the results of a Pipeline query, including the data and metadata. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/PipelineSource` | Start of a Firestore Pipeline |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/Query` | A `Query` which you can read or listen to. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/QueryDocumentSnapshot` | A `QueryDocumentSnapshot` contains data read from a document in your Cloud Firestore database as part of a query. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/QuerySnapshot` | A `QuerySnapshot` contains the results of a query. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/SetOptions` | An options object that configures the behavior of `set()` calls. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/SnapshotListenOptions` | An options object that configures the behavior of `addSnapshotListener()` calls. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/SnapshotListenOptions.Builder` | Builder for constructing `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/SnapshotListenOptions` instances. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/SnapshotMetadata` | Metadata about a snapshot, describing the state of the snapshot. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/Transaction` | A `Transaction` is passed to a Function to provide the methods to read and write data within the transaction context. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/TransactionOptions` | Options to customize transaction behavior for `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestore#runTransaction(com.google.firebase.firestore.TransactionOptions,com.google.firebase.firestore.Transaction.Function<TResult>)`. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/TransactionOptions.Builder` | A Builder for creating `TransactionOptions`. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/VectorValue` | Represent a vector type in Firestore documents. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/WriteBatch` | A write batch, used to perform multiple writes as a single atomic unit. |

## Enums

|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/AggregateSource` | The sources from which an `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/AggregateQuery` can retrieve its results. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentChange.Type` | An enumeration of snapshot diff types. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot.ServerTimestampBehavior` | Controls the return value for server timestamps that have not yet been set to their final value. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestoreException.Code` | The set of Cloud Firestore status codes. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/ListenSource` | Configures the source option of `addSnapshotListener()` calls on `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentReference` and `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/Query`. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/LoadBundleTaskProgress.TaskState` | Represents the state of bundle loading tasks. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/MetadataChanges` | Indicates whether metadata-only changes (that is, only `DocumentSnapshot.getMetadata()` or `QuerySnapshot.getMetadata()` changed) should trigger snapshot events. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/Query.Direction` | An enum for the direction of a sort. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/Source` | Configures the behavior of `get()` calls on `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentReference` and `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/Query`. |

## Exceptions

|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestoreException` | A class of exceptions thrown by Cloud Firestore. |