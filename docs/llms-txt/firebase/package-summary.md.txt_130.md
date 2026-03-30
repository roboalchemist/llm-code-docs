# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/package-summary.md.txt

# com.google.firebase.firestore

# com.google.firebase.firestore

## Interfaces

|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/EventListener` | An interface for event listeners. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/ListenerRegistration` | Represents a listener that can be removed by calling `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/ListenerRegistration#remove()`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LocalCacheSettings` | Marker interface implemented by all supported cache settings. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/MemoryGarbageCollectorSettings` |   |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/OnProgressListener` | A listener that is called periodically during execution of a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTask`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Transaction.Function` | An interface for providing code to be executed within a transaction context. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/WriteBatch.Function` | An interface for providing code to be executed within a `WriteBatch` context. |

## Classes

|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateField` | Represents an aggregation that can be performed by Firestore. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateField.AverageAggregateField` | Represents an "average" aggregation that can be performed by Firestore. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateField.CountAggregateField` | Represents a "count" aggregation that can be performed by Firestore. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateField.SumAggregateField` | Represents a "sum" aggregation that can be performed by Firestore. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateQuery` | A query that calculates aggregations over an underlying query. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateQuerySnapshot` | The results of executing an `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateQuery`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Blob` | Immutable class representing an array of bytes in Cloud Firestore. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/CollectionReference` | A `CollectionReference` can be used for adding documents, getting document references, and querying for documents (using the methods inherited from `Query`). |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentChange` | A `DocumentChange` represents a change to the documents matching a query. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentReference` | A `DocumentReference` refers to a document location in a Cloud Firestore database and can be used to write, read, or listen to the location. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot` | A `DocumentSnapshot` contains data read from a document in your Cloud Firestore database. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FieldPath` | A `FieldPath` refers to a field in a document. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FieldValue` | Sentinel values that can be used when writing document fields with `set()` or ` update()`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Filter` | A `Filter` represents a restriction on one or more field values and can be used to refine the results of a `Query`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestore` | Represents a Cloud Firestore database and is the entry point for all Cloud Firestore operations. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestoreSettings` | Settings used to configure a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestore` instance. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestoreSettings.Builder` | A Builder for creating `FirebaseFirestoreSettings`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/GeoPoint` | Immutable class representing a `GeoPoint` in Cloud Firestore |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTask` | Represents the task of loading a Firestore bundle. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTaskProgress` | Represents a progress update or a final state from loading bundles. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/MemoryCacheSettings` | Configures the SDK to use a memory cache. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/MemoryCacheSettings.Builder` | A Builder for creating `MemoryCacheSettings` instance. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/MemoryEagerGcSettings` | Configures the SDK to use an eager garbage collector for memory cache. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/MemoryEagerGcSettings.Builder` |   |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/MemoryLruGcSettings` | Configures the SDK to use a Least-Recently-Used garbage collector for memory cache. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/MemoryLruGcSettings.Builder` |   |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/PersistentCacheIndexManager` | Persistent cache indexes can improve performance of local query execution. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/PersistentCacheSettings` | Configures the SDK to use a persistent cache. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/PersistentCacheSettings.Builder` | A Builder for creating `PersistentCacheSettings` instance. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline` | A `Pipeline` is composed of a sequence of stages. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline.ExecuteOptions` |   |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline.ExecuteOptions.IndexMode` |   |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline.Snapshot` | A `Snapshot` contains the results of a pipeline execution. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/PipelineResult` | Represents the results of a Pipeline query, including the data and metadata. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/PipelineSource` | Start of a Firestore Pipeline |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query` | A `Query` which you can read or listen to. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/QueryDocumentSnapshot` | A `QueryDocumentSnapshot` contains data read from a document in your Cloud Firestore database as part of a query. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/QuerySnapshot` | A `QuerySnapshot` contains the results of a query. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/SetOptions` | An options object that configures the behavior of `set()` calls. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/SnapshotListenOptions` | An options object that configures the behavior of `addSnapshotListener()` calls. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/SnapshotListenOptions.Builder` | Builder for constructing `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/SnapshotListenOptions` instances. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/SnapshotMetadata` | Metadata about a snapshot, describing the state of the snapshot. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Transaction` | A `Transaction` is passed to a Function to provide the methods to read and write data within the transaction context. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/TransactionOptions` | Options to customize transaction behavior for `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestore#runTransaction(com.google.firebase.firestore.TransactionOptions,com.google.firebase.firestore.Transaction.Function<TResult>)`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/TransactionOptions.Builder` | A Builder for creating `TransactionOptions`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/VectorValue` | Represent a vector type in Firestore documents. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/WriteBatch` | A write batch, used to perform multiple writes as a single atomic unit. |

## Exceptions

|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestoreException` | A class of exceptions thrown by Cloud Firestore. |

## Annotations

|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentId` | Annotation used to mark a POJO property to be automatically populated with the document's ID when the POJO is created from a Cloud Firestore document (for example, via `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot#toObject(java.lang.Class<T>)`). |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Exclude` | Marks a field as excluded from the database instance. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/IgnoreExtraProperties` | Properties that don't map to class fields are ignored when serializing to a class annotated with this annotation. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/PropertyName` | Marks a field to be renamed when serialized. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/ServerTimestamp` | Annotation used to mark a timestamp field to be populated with a server timestamp. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/ThrowOnExtraProperties` | Properties that don't map to class fields when serializing to a class annotated with this annotation cause an exception to be thrown. |

## Enums

|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateSource` | The sources from which an `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateQuery` can retrieve its results. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentChange.Type` | An enumeration of snapshot diff types. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot.ServerTimestampBehavior` | Controls the return value for server timestamps that have not yet been set to their final value. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestoreException.Code` | The set of Cloud Firestore status codes. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/ListenSource` | Configures the source option of `addSnapshotListener()` calls on `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentReference` and `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTaskProgress.TaskState` | Represents the state of bundle loading tasks. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/MetadataChanges` | Indicates whether metadata-only changes (that is, only `DocumentSnapshot.getMetadata()` or `QuerySnapshot.getMetadata()` changed) should trigger snapshot events. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query.Direction` | An enum for the direction of a sort. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Source` | Configures the behavior of `get()` calls on `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentReference` and `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query`. |

## Top-level functions summary

|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestoreSettings` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/package-summary#firestoreSettings(kotlin.Function1)(init: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestoreSettings.Builder.() -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` Returns a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestoreSettings` instance initialized using the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/package-summary#firestoreSettings(kotlin.Function1)` function. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/MemoryCacheSettings` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/package-summary#memoryCacheSettings(kotlin.Function1)(init: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/MemoryCacheSettings.Builder.() -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/MemoryEagerGcSettings` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/package-summary#memoryEagerGcSettings(kotlin.Function1)(init: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/MemoryEagerGcSettings.Builder.() -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/MemoryLruGcSettings` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/package-summary#memoryLruGcSettings(kotlin.Function1)(init: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/MemoryLruGcSettings.Builder.() -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/PersistentCacheSettings` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/package-summary#persistentCacheSettings(kotlin.Function1)(init: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/PersistentCacheSettings.Builder.() -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |

## Extension functions summary

|---|---|
| `inline https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html<T?>` | `<T : https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html> https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentReference.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/package-summary#(com.google.firebase.firestore.DocumentReference).dataObjects(com.google.firebase.firestore.MetadataChanges)(metadataChanges: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/MetadataChanges)` Starts listening to the document referenced by this `DocumentReference` with the given options and emits its values converted to a POJO via a `https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html`. |
| `inline https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<T>>` | `<T : https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html> https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/package-summary#(com.google.firebase.firestore.Query).dataObjects(com.google.firebase.firestore.MetadataChanges)(metadataChanges: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/MetadataChanges)` Starts listening to this query with the given options and emits its values converted to a POJO via a `https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestore` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/Firebase.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/package-summary#(com.google.firebase.Firebase).firestore(com.google.firebase.FirebaseApp,kotlin.String)(app: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp, database: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Returns the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestore` instance of a given `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp` and database name. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestore` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/Firebase.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/package-summary#(com.google.firebase.Firebase).firestore(com.google.firebase.FirebaseApp)(app: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp)` Returns the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestore` instance of a given `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestore` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/Firebase.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/package-summary#(com.google.firebase.Firebase).firestore(kotlin.String)(database: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Returns the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestore` instance of the default `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp`, given the database name. |
| `inline T?` | `<T : https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?> https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/package-summary#(com.google.firebase.firestore.DocumentSnapshot).getField(com.google.firebase.firestore.FieldPath,com.google.firebase.firestore.DocumentSnapshot.ServerTimestampBehavior)( fieldPath: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FieldPath, serverTimestampBehavior: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot.ServerTimestampBehavior )` Returns the value at the field, converted to a POJO, or null if the field or document doesn't exist. |
| `inline T?` | `<T : https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?> https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/package-summary#(com.google.firebase.firestore.DocumentSnapshot).getField(com.google.firebase.firestore.FieldPath)(fieldPath: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FieldPath)` Returns the value at the field, converted to a POJO, or null if the field or document doesn't exist. |
| `inline T?` | `<T : https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?> https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/package-summary#(com.google.firebase.firestore.DocumentSnapshot).getField(kotlin.String,com.google.firebase.firestore.DocumentSnapshot.ServerTimestampBehavior)( field: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, serverTimestampBehavior: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot.ServerTimestampBehavior )` Returns the value at the field, converted to a POJO, or null if the field or document doesn't exist. |
| `inline T?` | `<T : https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?> https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/package-summary#(com.google.firebase.firestore.DocumentSnapshot).getField(kotlin.String)(field: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Returns the value at the field, converted to a POJO, or null if the field or document doesn't exist. |
| `https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentReference.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/package-summary#(com.google.firebase.firestore.DocumentReference).snapshots(com.google.firebase.firestore.MetadataChanges)(metadataChanges: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/MetadataChanges)` Starts listening to the document referenced by this `DocumentReference` with the given options and emits its values via a `https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html`. |
| `https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/QuerySnapshot>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/package-summary#(com.google.firebase.firestore.Query).snapshots(com.google.firebase.firestore.MetadataChanges)(metadataChanges: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/MetadataChanges)` Starts listening to this query with the given options and emits its values via a `https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html`. |
| `inline T?` | `<T : https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?> https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/package-summary#(com.google.firebase.firestore.DocumentSnapshot).toObject()()` Returns the contents of the document converted to a POJO or null if the document doesn't exist. |
| `inline T?` | `<T : https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?> https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/package-summary#(com.google.firebase.firestore.DocumentSnapshot).toObject(com.google.firebase.firestore.DocumentSnapshot.ServerTimestampBehavior)( serverTimestampBehavior: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot.ServerTimestampBehavior )` Returns the contents of the document converted to a POJO or null if the document doesn't exist. |
| `inline T` | `<T : https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html> https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/QueryDocumentSnapshot.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/package-summary#(com.google.firebase.firestore.QueryDocumentSnapshot).toObject()()` Returns the contents of the document converted to a POJO. |
| `inline T` | `<T : https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html> https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/QueryDocumentSnapshot.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/package-summary#(com.google.firebase.firestore.QueryDocumentSnapshot).toObject(com.google.firebase.firestore.DocumentSnapshot.ServerTimestampBehavior)( serverTimestampBehavior: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot.ServerTimestampBehavior )` Returns the contents of the document converted to a POJO. |
| `inline https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<T>` | `<T : https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html> https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/QuerySnapshot.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/package-summary#(com.google.firebase.firestore.QuerySnapshot).toObjects()()` Returns the contents of the documents in the QuerySnapshot, converted to the provided class, as a list. |
| `inline https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<T>` | `<T : https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html> https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/QuerySnapshot.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/package-summary#(com.google.firebase.firestore.QuerySnapshot).toObjects(com.google.firebase.firestore.DocumentSnapshot.ServerTimestampBehavior)( serverTimestampBehavior: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot.ServerTimestampBehavior )` Returns the contents of the documents in the QuerySnapshot, converted to the provided class, as a list. |

## Extension properties summary

|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestore` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/Firebase.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/package-summary#(com.google.firebase.Firebase).firestore()` Returns the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestore` instance of the default `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp`. |

## Top-level functions

### firestoreSettings

```
fun firestoreSettings(init: FirebaseFirestoreSettings.Builder.() -> Unit): FirebaseFirestoreSettings
```

Returns a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestoreSettings` instance initialized using the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/package-summary#firestoreSettings(kotlin.Function1)` function.

### memoryCacheSettings

```
fun memoryCacheSettings(init: MemoryCacheSettings.Builder.() -> Unit): MemoryCacheSettings
```

### memoryEagerGcSettings

```
fun memoryEagerGcSettings(init: MemoryEagerGcSettings.Builder.() -> Unit): MemoryEagerGcSettings
```

### memoryLruGcSettings

```
fun memoryLruGcSettings(init: MemoryLruGcSettings.Builder.() -> Unit): MemoryLruGcSettings
```

### persistentCacheSettings

```
fun persistentCacheSettings(init: PersistentCacheSettings.Builder.() -> Unit): PersistentCacheSettings
```

## Extension functions

### dataObjects

```
inline fun <T : Any> DocumentReference.dataObjects(
    metadataChanges: MetadataChanges = MetadataChanges.EXCLUDE
): Flow<T?>
```

Starts listening to the document referenced by this `DocumentReference` with the given options and emits its values converted to a POJO via a `https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html`.

- When the returned flow starts being collected, an `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/EventListener` will be attached.

- When the flow completes, the listener will be removed.

| Parameters |
|---|---|
| `<T : https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html>` | The type of the object to convert to. |
| `metadataChanges: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/MetadataChanges = MetadataChanges.EXCLUDE` | controls metadata-only changes. Default: `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/MetadataChanges#EXCLUDE` |

### dataObjects

```
inline fun <T : Any> Query.dataObjects(
    metadataChanges: MetadataChanges = MetadataChanges.EXCLUDE
): Flow<List<T>>
```

Starts listening to this query with the given options and emits its values converted to a POJO via a `https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html`.

- When the returned flow starts being collected, an `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/EventListener` will be attached.

- When the flow completes, the listener will be removed.

| Parameters |
|---|---|
| `<T : https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html>` | The type of the object to convert to. |
| `metadataChanges: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/MetadataChanges = MetadataChanges.EXCLUDE` | controls metadata-only changes. Default: `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/MetadataChanges#EXCLUDE` |

### firestore

```
fun Firebase.firestore(app: FirebaseApp, database: String): FirebaseFirestore
```

Returns the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestore` instance of a given `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp` and database name.

### firestore

```
fun Firebase.firestore(app: FirebaseApp): FirebaseFirestore
```

Returns the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestore` instance of a given `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp`.

### firestore

```
fun Firebase.firestore(database: String): FirebaseFirestore
```

Returns the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestore` instance of the default `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp`, given the database name.

### getField

```
inline fun <T : Any?> DocumentSnapshot.getField(
    fieldPath: FieldPath,
    serverTimestampBehavior: DocumentSnapshot.ServerTimestampBehavior
): T?
```

Returns the value at the field, converted to a POJO, or null if the field or document doesn't exist.

| Parameters |
|---|---|
| `<T : https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?>` | The type to convert the field value to. |
| `fieldPath: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FieldPath` | The path to the field. |
| `serverTimestampBehavior: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot.ServerTimestampBehavior` | Configures the behavior for server timestamps that have not yet ```kotlin been set to their final value. @return ``` The value at the given field or null. |

### getField

```
inline fun <T : Any?> DocumentSnapshot.getField(fieldPath: FieldPath): T?
```

Returns the value at the field, converted to a POJO, or null if the field or document doesn't exist.

| Parameters |
|---|---|
| `<T : https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?>` | The type to convert the field value to. |
| `fieldPath: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FieldPath` | The path to the field. |

| Returns |
|---|---|
| `T?` | The value at the given field or null. |

### getField

```
inline fun <T : Any?> DocumentSnapshot.getField(
    field: String,
    serverTimestampBehavior: DocumentSnapshot.ServerTimestampBehavior
): T?
```

Returns the value at the field, converted to a POJO, or null if the field or document doesn't exist.

| Parameters |
|---|---|
| `<T : https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?>` | The type to convert the field value to. |
| `field: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The path to the field. |
| `serverTimestampBehavior: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot.ServerTimestampBehavior` | Configures the behavior for server timestamps that have not yet ```kotlin been set to their final value. @return ``` The value at the given field or null. |

### getField

```
inline fun <T : Any?> DocumentSnapshot.getField(field: String): T?
```

Returns the value at the field, converted to a POJO, or null if the field or document doesn't exist.

| Parameters |
|---|---|
| `<T : https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?>` | The type to convert the field value to. |
| `field: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The path to the field. |

| Returns |
|---|---|
| `T?` | The value at the given field or null. |

### snapshots

```
fun DocumentReference.snapshots(
    metadataChanges: MetadataChanges = MetadataChanges.EXCLUDE
): Flow<DocumentSnapshot>
```

Starts listening to the document referenced by this `DocumentReference` with the given options and emits its values via a `https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html`.

- When the returned flow starts being collected, an `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/EventListener` will be attached.

- When the flow completes, the listener will be removed.

| Parameters |
|---|---|
| `metadataChanges: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/MetadataChanges = MetadataChanges.EXCLUDE` | controls metadata-only changes. Default: `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/MetadataChanges#EXCLUDE` |

### snapshots

```
fun Query.snapshots(
    metadataChanges: MetadataChanges = MetadataChanges.EXCLUDE
): Flow<QuerySnapshot>
```

Starts listening to this query with the given options and emits its values via a `https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html`.

- When the returned flow starts being collected, an `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/EventListener` will be attached.

- When the flow completes, the listener will be removed.

| Parameters |
|---|---|
| `metadataChanges: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/MetadataChanges = MetadataChanges.EXCLUDE` | controls metadata-only changes. Default: `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/MetadataChanges#EXCLUDE` |

### toObject

```
inline fun <T : Any?> DocumentSnapshot.toObject(): T?
```

Returns the contents of the document converted to a POJO or null if the document doesn't exist.

| Parameters |
|---|---|
| `<T : https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?>` | The type of the object to create. |

| Returns |
|---|---|
| `T?` | The contents of the document in an object of type T or null if the document doesn't ```kotlin exist. ``` |

### toObject

```
inline fun <T : Any?> DocumentSnapshot.toObject(
    serverTimestampBehavior: DocumentSnapshot.ServerTimestampBehavior
): T?
```

Returns the contents of the document converted to a POJO or null if the document doesn't exist.

| Parameters |
|---|---|
| `<T : https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?>` | The type of the object to create. |
| `serverTimestampBehavior: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot.ServerTimestampBehavior` | Configures the behavior for server timestamps that have not yet ```kotlin been set to their final value. @return ``` The contents of the document in an object of type T or null if the document doesn't ```kotlin exist. ``` |

### toObject

```
inline fun <T : Any> QueryDocumentSnapshot.toObject(): T
```

Returns the contents of the document converted to a POJO.

| Parameters |
|---|---|
| `<T : https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html>` | The type of the object to create. |

| Returns |
|---|---|
| `T` | The contents of the document in an object of type T. |

### toObject

```
inline fun <T : Any> QueryDocumentSnapshot.toObject(
    serverTimestampBehavior: DocumentSnapshot.ServerTimestampBehavior
): T
```

Returns the contents of the document converted to a POJO.

| Parameters |
|---|---|
| `<T : https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html>` | The type of the object to create. |
| `serverTimestampBehavior: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot.ServerTimestampBehavior` | Configures the behavior for server timestamps that have not yet ```kotlin been set to their final value. @return ``` The contents of the document in an object of type T. |

### toObjects

```
inline fun <T : Any> QuerySnapshot.toObjects(): List<T>
```

Returns the contents of the documents in the QuerySnapshot, converted to the provided class, as a list.

| Parameters |
|---|---|
| `<T : https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html>` | The POJO type used to convert the documents in the list. |

### toObjects

```
inline fun <T : Any> QuerySnapshot.toObjects(
    serverTimestampBehavior: DocumentSnapshot.ServerTimestampBehavior
): List<T>
```

Returns the contents of the documents in the QuerySnapshot, converted to the provided class, as a list.

| Parameters |
|---|---|
| `<T : https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html>` | The POJO type used to convert the documents in the list. |
| `serverTimestampBehavior: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot.ServerTimestampBehavior` | Configures the behavior for server timestamps that have not yet ```kotlin been set to their final value. ``` |

## Extension properties

### firestore

```
val Firebase.firestore: FirebaseFirestore
```

Returns the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestore` instance of the default `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp`.