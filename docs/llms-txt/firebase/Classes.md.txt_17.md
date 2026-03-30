# Source: https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes.md.txt

# FirebaseFirestore Framework Reference

# Classes

The following classes are available globally.
- `


  ### [FIRAggregateField](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRAggregateField)


  ` Represents an aggregation that can be performed by Firestore.

  #### Declaration

  Objective-C


      @interface FIRAggregateField : NSObject

- `


  ### [FIRAggregateQuery](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRAggregateQuery)


  ` A query that calculates aggregations over an underlying query.

  #### Declaration

  Objective-C


      @interface FIRAggregateQuery : NSObject

- `


  ### [FIRAggregateQuerySnapshot](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRAggregateQuerySnapshot)


  ` The results of executing an `AggregateQuery`.

  #### Declaration

  Objective-C


      @interface FIRAggregateQuerySnapshot : NSObject

- `


  ### [FIRCollectionReference](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRCollectionReference)


  ` A `CollectionReference` object can be used for adding documents, getting document references,
  and querying for documents (using the methods inherited from `Query`).

  #### Declaration

  Objective-C


      @interface FIRCollectionReference : https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRQuery

- `


  ### [FIRDocumentChange](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRDocumentChange)


  ` A `DocumentChange` represents a change to the documents matching a query. It contains the
  document affected and the type of change that occurred (added, modified, or removed).

  #### Declaration

  Objective-C


      @interface FIRDocumentChange : NSObject

- `


  ### [FIRDocumentReference](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRDocumentReference)


  ` A `DocumentReference` refers to a document location in a Firestore database and can be
  used to write, read, or listen to the location. The document at the referenced location
  may or may not exist. A `DocumentReference` can also be used to create a `CollectionReference` to
  a subcollection.

  #### Declaration

  Objective-C


      @interface FIRDocumentReference : NSObject

- `


  ### [FIRDocumentSnapshot](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRDocumentSnapshot)


  ` A `DocumentSnapshot` contains data read from a document in your Firestore database. The data
  can be extracted with the `data` property or by using subscript syntax to access a specific
  field.

  For a `DocumentSnapshot` that points to a non-existing document, any data access will return
  `nil`. You can use the `exists` property to explicitly verify a documents existence.

  #### Declaration

  Objective-C


      @interface FIRDocumentSnapshot : NSObject

- `


  ### [FIRQueryDocumentSnapshot](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRQueryDocumentSnapshot)


  ` A `QueryDocumentSnapshot` contains data read from a document in your Firestore database as
  part of a query. The document is guaranteed to exist and its data can be extracted with the
  `data` property or by using subscript syntax to access a specific field.

  A `QueryDocumentSnapshot` offers the same API surface as a `DocumentSnapshot`. As
  deleted documents are not returned from queries, its `exists` property will always be true and
  `data()` will never return `nil`.

  #### Declaration

  Objective-C


      @interface FIRQueryDocumentSnapshot : https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRDocumentSnapshot

- `


  ### [FIRFieldPath](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRFieldPath)


  ` A `FieldPath` refers to a field in a document. The path may consist of a single field name
  (referring to a top level field in the document), or a list of field names (referring to a nested
  field in the document).

  #### Declaration

  Objective-C


      @interface FIRFieldPath : NSObject <NSCopying>

- `


  ### [FIRFieldValue](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRFieldValue)


  ` Sentinel values that can be used when writing document fields with `setData()` or `updateData()`.

  #### Declaration

  Objective-C


      @interface FIRFieldValue : NSObject

- `


  ### [FIRFilter](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRFilter)


  ` A Filter represents a restriction on one or more field values and can be used to refine
  the results of a Query.

  #### Declaration

  Objective-C


      @interface FIRFilter : NSObject

- `


  ### [FIRFirestore](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRFirestore)


  ` `Firestore` represents a Firestore Database and is the entry point for all Firestore
  operations.

  #### Declaration

  Objective-C


      @interface FIRFirestore : NSObject

- `


  ### [FIRFirestoreSettings](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRFirestoreSettings)


  ` Settings used to configure a `Firestore` instance.

  #### Declaration

  Objective-C


      @interface FIRFirestoreSettings : NSObject <NSCopying>

- `


  ### [FIRGeoPoint](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRGeoPoint)


  ` An immutable object representing a geographical point in Firestore. The point is represented as
  a latitude/longitude pair.

  Latitude values are in the range of \[-90, 90\].
  Longitude values are in the range of \[-180, 180\].

  #### Declaration

  Objective-C


      @interface FIRGeoPoint : NSObject <NSCopying>

- `


  ### [FIRLoadBundleTaskProgress](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRLoadBundleTaskProgress)


  ` Represents a progress update or a final state from loading bundles.

  #### Declaration

  Objective-C


      @interface FIRLoadBundleTaskProgress : NSObject

- `


  ### [FIRLoadBundleTask](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRLoadBundleTask)


  ` Represents the task of loading a Firestore bundle. Observers can be registered with this task to
  observe the bundle loading progress, as well as task completion and error events.

  #### Declaration

  Objective-C


      @interface FIRLoadBundleTask : NSObject

- `


  ### [FIRPersistentCacheSettings](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRPersistentCacheSettings)


  ` Configures the SDK to use a persistent cache. Firestore documents and mutations are persisted
  across App restart.

  This is the default cache type unless explicitly specified otherwise.

  To use, create an instance using one of the initializers, then set the instance to
  `FirestoreSettings.cacheSettings`, and use `FirestoreSettings` instance to configure Firestore
  SDK.

  #### Declaration

  Objective-C


      @interface FIRPersistentCacheSettings
          : NSObject <NSCopying, https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Protocols#/c:objc(pl)FIRLocalCacheSettings>

- `


  ### [FIRMemoryEagerGCSettings](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRMemoryEagerGCSettings)


  ` Configures the SDK to use an eager garbage collector for memory cache.

  Once configured, the SDK will remove any Firestore documents from memory as soon as they are not
  used by any active queries.

  To use, create an instance using the initializer, then initialize
  `MemoryCacheSettings` with this instance. This is the default garbage collector, so alternatively
  you can use the default initializer of `MemoryCacheSettings`.

  #### Declaration

  Objective-C


      @interface FIRMemoryEagerGCSettings
          : NSObject <NSCopying, https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Protocols#/c:objc(pl)FIRMemoryGarbageCollectorSettings>

- `


  ### [FIRMemoryLRUGCSettings](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRMemoryLRUGCSettings)


  ` Configures the SDK to use a least-recently-used garbage collector for memory cache.

  Once configured, the SDK will attempt to remove documents that are least recently used in
  batches, if the current cache size is larger than the given target cache size. Default cache size
  is 100MB.

  To use, create an instance using one of the initializers, then initialize
  `MemoryCacheSettings` with this instance.

  #### Declaration

  Objective-C


      @interface FIRMemoryLRUGCSettings
          : NSObject <NSCopying, https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Protocols#/c:objc(pl)FIRMemoryGarbageCollectorSettings>

- `


  ### [FIRMemoryCacheSettings](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRMemoryCacheSettings)


  ` Configures the SDK to use a memory cache. Firestore documents and mutations are NOT persisted
  across App restart.

  To use, create an instance using one of the initializer, then set the instance to
  `FirestoreSettings.cacheSettings`, and use `FirestoreSettings` instance to configure Firestore
  SDK.

  #### Declaration

  Objective-C


      @interface FIRMemoryCacheSettings : NSObject <NSCopying, https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Protocols#/c:objc(pl)FIRLocalCacheSettings>

- `


  ### [FIRExprBridge](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes#/c:objc(cs)FIRExprBridge)


  ` Undocumented

  #### Declaration

  Objective-C

      @interface FIRExprBridge : NSObject
      @end

- `


  ### [FIRFieldBridge](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRFieldBridge)


  ` Undocumented

  #### Declaration

  Objective-C

      @interface FIRFieldBridge : https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes#/c:objc(cs)FIRExprBridge
      - (id)initWithName:(NSString *)name;
      - (id)initWithPath:(https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRFieldPath *)path;
      - (NSString *)field_name;
      @end

- `


  ### [FIRConstantBridge](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRConstantBridge)


  ` Undocumented

  #### Declaration

  Objective-C

      @interface FIRConstantBridge : https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes#/c:objc(cs)FIRExprBridge
      - (id)init:(id)input;
      @end

- `


  ### [FIRFunctionExprBridge](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRFunctionExprBridge)


  ` Undocumented

  #### Declaration

  Objective-C

      @interface FIRFunctionExprBridge : https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes#/c:objc(cs)FIRExprBridge
      - (id)initWithName:(NSString *)name Args:(NSArray<https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes#/c:objc(cs)FIRExprBridge *> *)args;
      @end

- `


  ### [FIRAggregateFunctionBridge](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRAggregateFunctionBridge)


  ` Undocumented

  #### Declaration

  Objective-C

      @interface FIRAggregateFunctionBridge : NSObject
      - (id)initWithName:(NSString *)name Args:(NSArray<https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes#/c:objc(cs)FIRExprBridge *> *)args;
      @end

- `


  ### [FIROrderingBridge](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIROrderingBridge)


  ` Undocumented

  #### Declaration

  Objective-C

      @interface FIROrderingBridge : NSObject
      - (id)initWithExpr:(https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes#/c:objc(cs)FIRExprBridge *)expr Direction:(NSString *)direction;
      @end

- `


  ### [FIRStageBridge](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRStageBridge)


  ` Undocumented

  #### Declaration

  Objective-C

      @interface FIRStageBridge : NSObject
      @property(nonatomic, readonly) NSString *name;
      @end

- `


  ### [FIRCollectionSourceStageBridge](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRCollectionSourceStageBridge)


  ` Undocumented

  #### Declaration

  Objective-C

      @interface FIRCollectionSourceStageBridge : https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRStageBridge

      - (id)initWithRef:(https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRCollectionReference *)ref firestore:(https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRFirestore *)db;
      @end

- `


  ### [FIRDatabaseSourceStageBridge](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRDatabaseSourceStageBridge)


  ` Undocumented

  #### Declaration

  Objective-C

      @interface FIRDatabaseSourceStageBridge : https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRStageBridge

      - (id)init;
      @end

- `


  ### [FIRCollectionGroupSourceStageBridge](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRCollectionGroupSourceStageBridge)


  ` Undocumented

  #### Declaration

  Objective-C

      @interface FIRCollectionGroupSourceStageBridge : https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRStageBridge

      - (id)initWithCollectionId:(NSString *)id;
      @end

- `


  ### [FIRDocumentsSourceStageBridge](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRDocumentsSourceStageBridge)


  ` Undocumented

  #### Declaration

  Objective-C

      @interface FIRDocumentsSourceStageBridge : https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRStageBridge

      - (id)initWithDocuments:(NSArray<https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRDocumentReference *> *)documents firestore:(https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRFirestore *)db;
      @end

- `


  ### [FIRWhereStageBridge](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRWhereStageBridge)


  ` Undocumented

  #### Declaration

  Objective-C

      @interface FIRWhereStageBridge : https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRStageBridge

      - (id)initWithExpr:(https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes#/c:objc(cs)FIRExprBridge *)expr;
      @end

- `


  ### [FIRLimitStageBridge](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRLimitStageBridge)


  ` Undocumented

  #### Declaration

  Objective-C

      @interface FIRLimitStageBridge : https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRStageBridge

      - (id)initWithLimit:(NSInteger)value;
      @end

- `


  ### [FIROffsetStageBridge](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIROffsetStageBridge)


  ` Undocumented

  #### Declaration

  Objective-C

      @interface FIROffsetStageBridge : https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRStageBridge

      - (id)initWithOffset:(NSInteger)value;
      @end

- `


  ### [FIRAddFieldsStageBridge](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRAddFieldsStageBridge)


  ` Undocumented

  #### Declaration

  Objective-C

      @interface FIRAddFieldsStageBridge : https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRStageBridge
      - (id)initWithFields:(NSDictionary<NSString *, https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes#/c:objc(cs)FIRExprBridge *> *)fields;
      @end

- `


  ### [FIRRemoveFieldsStageBridge](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRRemoveFieldsStageBridge)


  ` Undocumented

  #### Declaration

  Objective-C

      @interface FIRRemoveFieldsStageBridge : https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRStageBridge
      - (id)initWithFields:(NSArray<NSString *> *)fields;
      @end

- `


  ### [FIRSelectStageBridge](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRSelectStageBridge)


  ` Undocumented

  #### Declaration

  Objective-C

      @interface FIRSelectStageBridge : https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRStageBridge
      - (id)initWithSelections:(NSDictionary<NSString *, https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes#/c:objc(cs)FIRExprBridge *> *)selections;
      @end

- `


  ### [FIRDistinctStageBridge](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRDistinctStageBridge)


  ` Undocumented

  #### Declaration

  Objective-C

      @interface FIRDistinctStageBridge : https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRStageBridge
      - (id)initWithGroups:(NSDictionary<NSString *, https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes#/c:objc(cs)FIRExprBridge *> *)groups;
      @end

- `


  ### [FIRAggregateStageBridge](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRAggregateStageBridge)


  ` Undocumented

  #### Declaration

  Objective-C

      @interface FIRAggregateStageBridge : https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRStageBridge
      - (id)initWithAccumulators:(NSDictionary<NSString *, https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRAggregateFunctionBridge *> *)accumulators
                          groups:(NSDictionary<NSString *, https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes#/c:objc(cs)FIRExprBridge *> *)groups;
      @end

- `


  ### [FIRFindNearestStageBridge](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRFindNearestStageBridge)


  ` Undocumented

  #### Declaration

  Objective-C

      @interface FIRFindNearestStageBridge : https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRStageBridge
      - (id)initWithField:(https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRFieldBridge *)field
              vectorValue:(FIRVectorValue *)vectorValue
          distanceMeasure:(NSString *)distanceMeasure
                    limit:(NSNumber *_Nullable)limit
            distanceField:(https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes#/c:objc(cs)FIRExprBridge *_Nullable)distanceField;
      @end

- `


  ### [FIRSorStageBridge](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRSorStageBridge)


  ` Undocumented

  #### Declaration

  Objective-C

      @interface FIRSorStageBridge : https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRStageBridge
      - (id)initWithOrderings:(NSArray<id> *)orderings;
      @end

- `


  ### [FIRReplaceWithStageBridge](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRReplaceWithStageBridge)


  ` Undocumented

  #### Declaration

  Objective-C

      @interface FIRReplaceWithStageBridge : https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRStageBridge
      - (id)initWithExpr:(https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes#/c:objc(cs)FIRExprBridge *)expr;
      @end

- `


  ### [FIRSampleStageBridge](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRSampleStageBridge)


  ` Undocumented

  #### Declaration

  Objective-C

      @interface FIRSampleStageBridge : https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRStageBridge
      - (id)initWithCount:(int64_t)count;
      - (id)initWithPercentage:(double)percentage;
      @end

- `


  ### [FIRUnionStageBridge](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRUnionStageBridge)


  ` Undocumented

  #### Declaration

  Objective-C

      @interface FIRUnionStageBridge : https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRStageBridge
      - (id)initWithOther:(https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRPipelineBridge *)other;
      @end

- `


  ### [FIRUnnestStageBridge](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRUnnestStageBridge)


  ` Undocumented

  #### Declaration

  Objective-C

      @interface FIRUnnestStageBridge : https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRStageBridge
      - (id)initWithField:(https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes#/c:objc(cs)FIRExprBridge *)field
                    alias:(https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes#/c:objc(cs)FIRExprBridge *)alias
               indexField:(https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes#/c:objc(cs)FIRExprBridge *_Nullable)index_field;
      @end

- `


  ### [FIRRawStageBridge](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRRawStageBridge)


  ` Undocumented

  #### Declaration

  Objective-C

      @interface FIRRawStageBridge : https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRStageBridge
      - (id)initWithName:(NSString *)name
                  params:(NSArray<id> *)params
                 options:(NSDictionary<NSString *, https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes#/c:objc(cs)FIRExprBridge *> *_Nullable)options;
      @end

- `


  ### [__FIRPipelineResultBridge](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/__FIRPipelineResultBridge)


  ` Undocumented

  #### Declaration

  Objective-C

      @interface __FIRPipelineResultBridge : NSObject

      @property(nonatomic, strong, readonly, nullable) https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRDocumentReference *reference;

      @property(nonatomic, copy, readonly, nullable) NSString *documentID;

      @property(nonatomic, strong, readonly, nullable) FIRTimestamp *create_time;

      @property(nonatomic, strong, readonly, nullable) FIRTimestamp *update_time;

      - (NSDictionary<NSString *, id> *)data;

      - (NSDictionary<NSString *, id> *)dataWithServerTimestampBehavior:
          (https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Enums/FIRServerTimestampBehavior)serverTimestampBehavior;

      - (nullable id)get:(id)field;

      - (nullable id)get:(id)field
          serverTimestampBehavior:(https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Enums/FIRServerTimestampBehavior)serverTimestampBehavior;

      @end

- `


  ### [__FIRPipelineResultChangeBridge](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/__FIRPipelineResultChangeBridge)


  ` Undocumented

  #### Declaration

  Objective-C

      @interface __FIRPipelineResultChangeBridge : NSObject

      /** The type of change that occurred (added, modified, or removed). */
      @property(nonatomic, readonly) https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Enums/FIRDocumentChangeType type;

      /** The document affected by this change. */
      @property(nonatomic, strong, readonly) https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/__FIRPipelineResultBridge *result;

      @property(nonatomic, readonly) NSUInteger oldIndex;

      @property(nonatomic, readonly) NSUInteger newIndex;

      @end

- `


  ### [__FIRPipelineSnapshotBridge](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/__FIRPipelineSnapshotBridge)


  ` Undocumented

  #### Declaration

  Objective-C

      @interface __FIRPipelineSnapshotBridge : NSObject

      @property(nonatomic, strong, readonly) NSArray<https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/__FIRPipelineResultBridge *> *results;

      @property(nonatomic, strong, readonly) FIRTimestamp *execution_time;

      @end

- `


  ### [FIRPipelineBridge](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRPipelineBridge)


  ` Undocumented

  #### Declaration

  Objective-C

      @interface FIRPipelineBridge : NSObject

      /** :nodoc: */
      - (id)initWithStages:(NSArray<https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRStageBridge *> *)stages db:(https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRFirestore *)db;

      - (void)executeWithCompletion:(void (^)(https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/__FIRPipelineSnapshotBridge *_Nullable result,
                                              NSError *_Nullable error))completion;

      + (NSArray<https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRStageBridge *> *)createStageBridgesFromQuery:(https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRQuery *)query;
      @end

- `


  ### [__FIRRealtimePipelineSnapshotBridge](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/__FIRRealtimePipelineSnapshotBridge)


  ` Undocumented

  #### Declaration

  Objective-C

      @interface __FIRRealtimePipelineSnapshotBridge : NSObject

      @property(nonatomic, strong, readonly) NSArray<https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/__FIRPipelineResultBridge *> *results;

      @property(nonatomic, strong, readonly) NSArray<https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/__FIRPipelineResultChangeBridge *> *changes;

      @property(nonatomic, strong, readonly) https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRSnapshotMetadata *metadata;

      @end

- `


  ### [__FIRPipelineListenOptionsBridge](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/__FIRPipelineListenOptionsBridge)


  ` Undocumented

  #### Declaration

  Objective-C

      @interface __FIRPipelineListenOptionsBridge : NSObject

      @property(nonatomic, readonly) NSString *serverTimestampBehavior;
      @property(nonatomic, readonly) BOOL includeMetadata;
      @property(nonatomic, readonly) https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Enums/FIRListenSource source;
      - (instancetype)initWithServerTimestampBehavior:(NSString *)serverTimestampBehavior
                                      includeMetadata:(BOOL)includeMetadata
                                               source:(https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Enums/FIRListenSource)source NS_DESIGNATED_INITIALIZER;

      /**
       * The default initializer is unavailable. Please use the designated initializer.
       */
      - (instancetype)init NS_UNAVAILABLE;

      @end

- `


  ### [FIRRealtimePipelineBridge](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRRealtimePipelineBridge)


  ` Undocumented

  #### Declaration

  Objective-C

      @interface FIRRealtimePipelineBridge : NSObject

      /** :nodoc: */
      - (id)initWithStages:(NSArray<https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRStageBridge *> *)stages db:(https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRFirestore *)db;

      - (id<https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Protocols/FIRListenerRegistration>)
          addSnapshotListenerWithOptions:(https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/__FIRPipelineListenOptionsBridge *)options
                                listener:
                                    (void (^)(https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/__FIRRealtimePipelineSnapshotBridge *_Nullable snapshot,
                                              NSError *_Nullable error))listener
          NS_SWIFT_NAME(addSnapshotListener(options:listener:));

      @end

- `


  ### [FIRQuery](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRQuery)


  ` A `Query` refers to a query which you can read or listen to. You can also construct
  refined `Query` objects by adding filters and ordering.

  #### Declaration

  Objective-C


      @interface FIRQuery : NSObject

- `


  ### [FIRQuerySnapshot](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRQuerySnapshot)


  ` A `QuerySnapshot` contains zero or more `DocumentSnapshot` objects. It can be enumerated
  using the `documents` property and its size can be inspected with `isEmpty` and
  `count`.

  #### Declaration

  Objective-C


      @interface FIRQuerySnapshot : NSObject

- `


  ### [FIRSnapshotListenOptions](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRSnapshotListenOptions)


  ` Options to configure the behavior of `Firestore.addSnapshotListenerWithOptions()`. Instances
  of this class control settings like whether metadata-only changes trigger events and the
  preferred data source.

  #### Declaration

  Objective-C


      @interface FIRSnapshotListenOptions : NSObject

- `


  ### [FIRSnapshotMetadata](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRSnapshotMetadata)


  ` Metadata about a snapshot, describing the state of the snapshot.

  #### Declaration

  Objective-C


      @interface FIRSnapshotMetadata : NSObject

- `


  ### [FIRTransaction](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRTransaction)


  ` `Transaction` provides methods to read and write data within a transaction.
  See
  `Firestore.runTransaction(_:)`

  #### Declaration

  Objective-C


      @interface FIRTransaction : NSObject

- `


  ### [FIRTransactionOptions](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRTransactionOptions)


  ` Options to customize the behavior of `Firestore.runTransactionWithOptions()`.

  #### Declaration

  Objective-C


      @interface FIRTransactionOptions : NSObject <NSCopying>

- `


  ### [FIRWriteBatch](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRWriteBatch)


  ` A write batch is used to perform multiple writes as a single atomic unit.

  A WriteBatch object can be acquired by calling `Firestore.batch()`. It provides methods for
  adding writes to the write batch. None of the writes will be committed (or visible locally)
  until `WriteBatch.commit()` is called.

  Unlike transactions, write batches are persisted offline and therefore are preferable when you
  don't need to condition your writes on read data.

  #### Declaration

  Objective-C


      @interface FIRWriteBatch : NSObject