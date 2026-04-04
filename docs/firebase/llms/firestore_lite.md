# Source: https://firebase.google.com/docs/reference/js/firestore_lite.md.txt

# @firebase/firestore/lite

## Functions

|                                                                           Function                                                                           |                                                                                                                                                                                                                                                                                                                                                                                                                                             Description                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **function(app, ...)**                                                                                                                                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [getFirestore(app)](https://firebase.google.com/docs/reference/js/firestore_lite.md#getfirestore_cf608e1)                                                    | Returns the existing default [Firestore](https://firebase.google.com/docs/reference/js/firestore_.firestore.md#firestore_class) instance that is associated with the provided [FirebaseApp](https://firebase.google.com/docs/reference/js/app.firebaseapp.md#firebaseapp_interface). If no instance exists, initializes a new instance with default settings.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [getFirestore(app, databaseId)](https://firebase.google.com/docs/reference/js/firestore_lite.md#getfirestore_48de6cb)                                        | ***(Public Preview)*** Returns the existing [Firestore](https://firebase.google.com/docs/reference/js/firestore_.firestore.md#firestore_class) instance that is associated with the provided [FirebaseApp](https://firebase.google.com/docs/reference/js/app.firebaseapp.md#firebaseapp_interface). If no instance exists, initializes a new instance with default settings.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [initializeFirestore(app, settings)](https://firebase.google.com/docs/reference/js/firestore_lite.md#initializefirestore_87c6318)                            | Initializes a new instance of Cloud Firestore with the provided settings. Can only be called before any other functions, including [getFirestore()](https://firebase.google.com/docs/reference/js/firestore_.md#getfirestore). If the custom settings are empty, this function is equivalent to calling [getFirestore()](https://firebase.google.com/docs/reference/js/firestore_.md#getfirestore).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [initializeFirestore(app, settings, databaseId)](https://firebase.google.com/docs/reference/js/firestore_lite.md#initializefirestore_37baaaf)                | ***(Public Preview)*** Initializes a new instance of Cloud Firestore with the provided settings. Can only be called before any other functions, including [getFirestore()](https://firebase.google.com/docs/reference/js/firestore_.md#getfirestore). If the custom settings are empty, this function is equivalent to calling [getFirestore()](https://firebase.google.com/docs/reference/js/firestore_.md#getfirestore).                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| **function(firestore, ...)**                                                                                                                                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [collection(firestore, path, pathSegments)](https://firebase.google.com/docs/reference/js/firestore_lite.md#collection_1eb4c23)                              | Gets a `CollectionReference` instance that refers to the collection at the specified absolute path.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [collectionGroup(firestore, collectionId)](https://firebase.google.com/docs/reference/js/firestore_lite.md#collectiongroup_1838fc3)                          | Creates and returns a new `Query` instance that includes all documents in the database that are contained in a collection or subcollection with the given `collectionId`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [connectFirestoreEmulator(firestore, host, port, options)](https://firebase.google.com/docs/reference/js/firestore_lite.md#connectfirestoreemulator_7c247cd) | Modify this instance to communicate with the Cloud Firestore emulator.Note: This must be called before this instance has been used to do any operations.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [doc(firestore, path, pathSegments)](https://firebase.google.com/docs/reference/js/firestore_lite.md#doc_1eb4c23)                                            | Gets a `DocumentReference` instance that refers to the document at the specified absolute path.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [runTransaction(firestore, updateFunction, options)](https://firebase.google.com/docs/reference/js/firestore_lite.md#runtransaction_6f03ec4)                 | Executes the given `updateFunction` and then attempts to commit the changes applied within the transaction. If any document read within the transaction has changed, Cloud Firestore retries the `updateFunction`. If it fails to commit after 5 attempts, the transaction fails.The maximum number of writes allowed in a single transaction is 500.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [terminate(firestore)](https://firebase.google.com/docs/reference/js/firestore_lite.md#terminate_231a8e0)                                                    | Terminates the provided `Firestore` instance.After calling `terminate()` only the `clearIndexedDbPersistence()` functions may be used. Any other function will throw a `FirestoreError`. Termination does not cancel any pending writes, and any promises that are awaiting a response from the server will not be resolved.To restart after termination, create a new instance of `Firestore` with [getFirestore()](https://firebase.google.com/docs/reference/js/firestore_.md#getfirestore).Note: Under normal circumstances, calling `terminate()` is not required. This function is useful only when you want to force this instance to release all of its resources or in combination with [clearIndexedDbPersistence()](https://firebase.google.com/docs/reference/js/firestore_.md#clearindexeddbpersistence_231a8e0) to ensure that all local state is destroyed between test runs.        |
| [writeBatch(firestore)](https://firebase.google.com/docs/reference/js/firestore_lite.md#writebatch_231a8e0)                                                  | Creates a write batch, used for performing multiple writes as a single atomic operation. The maximum number of writes allowed in a single WriteBatch is 500.The result of these writes will only be reflected in document reads that occur after the returned promise resolves. If the client is offline, the write fails. If you would like to see local modifications or buffer writes until the client is online, use the full Firestore SDK.                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| **function()**                                                                                                                                               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [count()](https://firebase.google.com/docs/reference/js/firestore_lite.md#count)                                                                             | Create an AggregateField object that can be used to compute the count of documents in the result set of a query.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [deleteField()](https://firebase.google.com/docs/reference/js/firestore_lite.md#deletefield)                                                                 | Returns a sentinel for use with [updateDoc()](https://firebase.google.com/docs/reference/js/firestore_lite.md#updatedoc_51a65e3) or [setDoc()](https://firebase.google.com/docs/reference/js/firestore_lite.md#setdoc_ee215ad) with `{merge: true}` to mark a field for deletion.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [documentId()](https://firebase.google.com/docs/reference/js/firestore_lite.md#documentid)                                                                   | Returns a special sentinel `FieldPath` to refer to the ID of a document. It can be used in queries to sort or filter by the document ID.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [getFirestore()](https://firebase.google.com/docs/reference/js/firestore_lite.md#getfirestore)                                                               | Returns the existing default [Firestore](https://firebase.google.com/docs/reference/js/firestore_.firestore.md#firestore_class) instance that is associated with the default [FirebaseApp](https://firebase.google.com/docs/reference/js/app.firebaseapp.md#firebaseapp_interface). If no instance exists, initializes a new instance with default settings.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [serverTimestamp()](https://firebase.google.com/docs/reference/js/firestore_lite.md#servertimestamp)                                                         | Returns a sentinel used with [setDoc()](https://firebase.google.com/docs/reference/js/firestore_lite.md#setdoc_ee215ad) or [updateDoc()](https://firebase.google.com/docs/reference/js/firestore_lite.md#updatedoc_51a65e3) to include a server-generated timestamp in the written data.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| **function(databaseId, ...)**                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [getFirestore(databaseId)](https://firebase.google.com/docs/reference/js/firestore_lite.md#getfirestore_53dc891)                                             | ***(Public Preview)*** Returns the existing [Firestore](https://firebase.google.com/docs/reference/js/firestore_.firestore.md#firestore_class) instance that is associated with the default [FirebaseApp](https://firebase.google.com/docs/reference/js/app.firebaseapp.md#firebaseapp_interface). If no instance exists, initializes a new instance with default settings.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| **function(elements, ...)**                                                                                                                                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [arrayRemove(elements)](https://firebase.google.com/docs/reference/js/firestore_lite.md#arrayremove_7d853aa)                                                 | Returns a special value that can be used with [setDoc()](https://firebase.google.com/docs/reference/js/firestore_.md#setdoc_ee215ad) or that tells the server to remove the given elements from any array value that already exists on the server. All instances of each element specified will be removed from the array. If the field being modified is not already an array it will be overwritten with an empty array.                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [arrayUnion(elements)](https://firebase.google.com/docs/reference/js/firestore_lite.md#arrayunion_7d853aa)                                                   | Returns a special value that can be used with [setDoc()](https://firebase.google.com/docs/reference/js/firestore_lite.md#setdoc_ee215ad) or [updateDoc()](https://firebase.google.com/docs/reference/js/firestore_lite.md#updatedoc_51a65e3) that tells the server to union the given elements with any array value that already exists on the server. Each specified element that doesn't already exist in the array will be added to the end. If the field being modified is not already an array it will be overwritten with an array containing exactly the specified elements.                                                                                                                                                                                                                                                                                                                 |
| **function(field, ...)**                                                                                                                                     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [average(field)](https://firebase.google.com/docs/reference/js/firestore_lite.md#average_aacc3a9)                                                            | Create an AggregateField object that can be used to compute the average of a specified field over a range of documents in the result set of a query.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [sum(field)](https://firebase.google.com/docs/reference/js/firestore_lite.md#sum_aacc3a9)                                                                    | Create an AggregateField object that can be used to compute the sum of a specified field over a range of documents in the result set of a query.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| **function(fieldPath, ...)**                                                                                                                                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [orderBy(fieldPath, directionStr)](https://firebase.google.com/docs/reference/js/firestore_lite.md#orderby_006d61f)                                          | Creates a [QueryOrderByConstraint](https://firebase.google.com/docs/reference/js/firestore_.queryorderbyconstraint.md#queryorderbyconstraint_class) that sorts the query result by the specified field, optionally in descending order instead of ascending.Note: Documents that do not contain the specified field will not be present in the query result.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [where(fieldPath, opStr, value)](https://firebase.google.com/docs/reference/js/firestore_lite.md#where_0fae4bf)                                              | Creates a [QueryFieldFilterConstraint](https://firebase.google.com/docs/reference/js/firestore_.queryfieldfilterconstraint.md#queryfieldfilterconstraint_class) that enforces that documents must contain the specified field and that the value should satisfy the relation constraint provided.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| **function(fieldValues, ...)**                                                                                                                               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [endAt(fieldValues)](https://firebase.google.com/docs/reference/js/firestore_lite.md#endat_8b2f2c8)                                                          | Creates a [QueryEndAtConstraint](https://firebase.google.com/docs/reference/js/firestore_.queryendatconstraint.md#queryendatconstraint_class) that modifies the result set to end at the provided fields relative to the order of the query. The order of the field values must match the order of the order by clauses of the query.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [endBefore(fieldValues)](https://firebase.google.com/docs/reference/js/firestore_lite.md#endbefore_8b2f2c8)                                                  | Creates a [QueryEndAtConstraint](https://firebase.google.com/docs/reference/js/firestore_.queryendatconstraint.md#queryendatconstraint_class) that modifies the result set to end before the provided fields relative to the order of the query. The order of the field values must match the order of the order by clauses of the query.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [startAfter(fieldValues)](https://firebase.google.com/docs/reference/js/firestore_lite.md#startafter_8b2f2c8)                                                | Creates a [QueryStartAtConstraint](https://firebase.google.com/docs/reference/js/firestore_.querystartatconstraint.md#querystartatconstraint_class) that modifies the result set to start after the provided fields relative to the order of the query. The order of the field values must match the order of the order by clauses of the query.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [startAt(fieldValues)](https://firebase.google.com/docs/reference/js/firestore_lite.md#startat_8b2f2c8)                                                      | Creates a [QueryStartAtConstraint](https://firebase.google.com/docs/reference/js/firestore_.querystartatconstraint.md#querystartatconstraint_class) that modifies the result set to start at the provided fields relative to the order of the query. The order of the field values must match the order of the order by clauses of the query.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| **function(left, ...)**                                                                                                                                      |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [aggregateFieldEqual(left, right)](https://firebase.google.com/docs/reference/js/firestore_lite.md#aggregatefieldequal_e80a2b2)                              | Compares two 'AggregateField\` instances for equality.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [aggregateQuerySnapshotEqual(left, right)](https://firebase.google.com/docs/reference/js/firestore_lite.md#aggregatequerysnapshotequal_1529a20)              | Compares two `AggregateQuerySnapshot` instances for equality.Two `AggregateQuerySnapshot` instances are considered "equal" if they have underlying queries that compare equal, and the same data.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [queryEqual(left, right)](https://firebase.google.com/docs/reference/js/firestore_lite.md#queryequal_7a1f045)                                                | Returns true if the provided queries point to the same collection and apply the same constraints.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [refEqual(left, right)](https://firebase.google.com/docs/reference/js/firestore_lite.md#refequal_598b780)                                                    | Returns true if the provided references are equal.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [snapshotEqual(left, right)](https://firebase.google.com/docs/reference/js/firestore_lite.md#snapshotequal_5109204)                                          | Returns true if the provided snapshots are equal.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| **function(limit, ...)**                                                                                                                                     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [limit(limit)](https://firebase.google.com/docs/reference/js/firestore_lite.md#limit_ec46c78)                                                                | Creates a [QueryLimitConstraint](https://firebase.google.com/docs/reference/js/firestore_.querylimitconstraint.md#querylimitconstraint_class) that only returns the first matching documents.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [limitToLast(limit)](https://firebase.google.com/docs/reference/js/firestore_lite.md#limittolast_ec46c78)                                                    | Creates a [QueryLimitConstraint](https://firebase.google.com/docs/reference/js/firestore_.querylimitconstraint.md#querylimitconstraint_class) that only returns the last matching documents.You must specify at least one `orderBy` clause for `limitToLast` queries, otherwise an exception will be thrown during execution.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| **function(logLevel, ...)**                                                                                                                                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [setLogLevel(logLevel)](https://firebase.google.com/docs/reference/js/firestore_lite.md#setloglevel_d02fda2)                                                 | Sets the verbosity of Cloud Firestore logs (debug, error, or silent).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| **function(n, ...)**                                                                                                                                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [increment(n)](https://firebase.google.com/docs/reference/js/firestore_lite.md#increment_5685735)                                                            | Returns a special value that can be used with [setDoc()](https://firebase.google.com/docs/reference/js/firestore_lite.md#setdoc_ee215ad) or [updateDoc()](https://firebase.google.com/docs/reference/js/firestore_lite.md#updatedoc_51a65e3) that tells the server to increment the field's current value by the given value.If either the operand or the current field value uses floating point precision, all arithmetic follows IEEE 754 semantics. If both values are integers, values outside of JavaScript's safe number range (`Number.MIN_SAFE_INTEGER` to `Number.MAX_SAFE_INTEGER`) are also subject to precision loss. Furthermore, once processed by the Firestore backend, all integer operations are capped between -2\^63 and 2\^63-1.If the current field value is not of type `number`, or if the field does not yet exist, the transformation sets the field to the given value. |
| **function(query, ...)**                                                                                                                                     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [getAggregate(query, aggregateSpec)](https://firebase.google.com/docs/reference/js/firestore_lite.md#getaggregate_2073a74)                                   | Calculates the specified aggregations over the documents in the result set of the given query without actually downloading the documents.Using this function to perform aggregations is efficient because only the final aggregation values, not the documents' data, are downloaded. This function can perform aggregations of the documents in cases where the result set is prohibitively large to download entirely (thousands of documents).                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [getCount(query)](https://firebase.google.com/docs/reference/js/firestore_lite.md#getcount_4e56953)                                                          | Calculates the number of documents in the result set of the given query without actually downloading the documents.Using this function to count the documents is efficient because only the final count, not the documents' data, is downloaded. This function can count the documents in cases where the result set is prohibitively large to download entirely (thousands of documents).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [getDocs(query)](https://firebase.google.com/docs/reference/js/firestore_lite.md#getdocs_4e56953)                                                            | Executes the query and returns the results as a [QuerySnapshot](https://firebase.google.com/docs/reference/js/firestore_.querysnapshot.md#querysnapshot_class).All queries are executed directly by the server, even if the query was previously executed. Recent modifications are only reflected in the retrieved results if they have already been applied by the backend. If the client is offline, the operation fails. To see previously cached result and local modifications, use the full Firestore SDK.                                                                                                                                                                                                                                                                                                                                                                                   |
| [query(query, compositeFilter, queryConstraints)](https://firebase.google.com/docs/reference/js/firestore_lite.md#query_9f7b0f4)                             | Creates a new immutable instance of [Query](https://firebase.google.com/docs/reference/js/firestore_.query.md#query_class) that is extended to also include additional query constraints.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [query(query, queryConstraints)](https://firebase.google.com/docs/reference/js/firestore_lite.md#query_0f46da1)                                              | Creates a new immutable instance of [Query](https://firebase.google.com/docs/reference/js/firestore_.query.md#query_class) that is extended to also include additional query constraints.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| **function(queryConstraints, ...)**                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [and(queryConstraints)](https://firebase.google.com/docs/reference/js/firestore_lite.md#and_e72c712)                                                         | Creates a new [QueryCompositeFilterConstraint](https://firebase.google.com/docs/reference/js/firestore_.querycompositefilterconstraint.md#querycompositefilterconstraint_class) that is a conjunction of the given filter constraints. A conjunction filter includes a document if it satisfies all of the given filters.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [or(queryConstraints)](https://firebase.google.com/docs/reference/js/firestore_lite.md#or_e72c712)                                                           | Creates a new [QueryCompositeFilterConstraint](https://firebase.google.com/docs/reference/js/firestore_.querycompositefilterconstraint.md#querycompositefilterconstraint_class) that is a disjunction of the given filter constraints. A disjunction filter includes a document if it satisfies any of the given filters.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| **function(reference, ...)**                                                                                                                                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [addDoc(reference, data)](https://firebase.google.com/docs/reference/js/firestore_lite.md#adddoc_6e783ff)                                                    | Add a new document to specified `CollectionReference` with the given data, assigning it a document ID automatically.The result of this write will only be reflected in document reads that occur after the returned promise resolves. If the client is offline, the write fails. If you would like to see local modifications or buffer writes until the client is online, use the full Firestore SDK.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [collection(reference, path, pathSegments)](https://firebase.google.com/docs/reference/js/firestore_lite.md#collection_568f98d)                              | Gets a `CollectionReference` instance that refers to a subcollection of `reference` at the specified relative path.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [collection(reference, path, pathSegments)](https://firebase.google.com/docs/reference/js/firestore_lite.md#collection_70b4396)                              | Gets a `CollectionReference` instance that refers to a subcollection of `reference` at the specified relative path.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [deleteDoc(reference)](https://firebase.google.com/docs/reference/js/firestore_lite.md#deletedoc_4569087)                                                    | Deletes the document referred to by the specified `DocumentReference`.The deletion will only be reflected in document reads that occur after the returned promise resolves. If the client is offline, the delete fails. If you would like to see local modifications or buffer writes until the client is online, use the full Firestore SDK.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [doc(reference, path, pathSegments)](https://firebase.google.com/docs/reference/js/firestore_lite.md#doc_568f98d)                                            | Gets a `DocumentReference` instance that refers to a document within `reference` at the specified relative path. If no path is specified, an automatically-generated unique ID will be used for the returned `DocumentReference`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [doc(reference, path, pathSegments)](https://firebase.google.com/docs/reference/js/firestore_lite.md#doc_70b4396)                                            | Gets a `DocumentReference` instance that refers to a document within `reference` at the specified relative path.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [getDoc(reference)](https://firebase.google.com/docs/reference/js/firestore_lite.md#getdoc_4569087)                                                          | Reads the document referred to by the specified document reference.All documents are directly fetched from the server, even if the document was previously read or modified. Recent modifications are only reflected in the retrieved `DocumentSnapshot` if they have already been applied by the backend. If the client is offline, the read fails. If you like to use caching or see local modifications, please use the full Firestore SDK.                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [setDoc(reference, data)](https://firebase.google.com/docs/reference/js/firestore_lite.md#setdoc_ee215ad)                                                    | Writes to the document referred to by the specified `DocumentReference`. If the document does not yet exist, it will be created.The result of this write will only be reflected in document reads that occur after the returned promise resolves. If the client is offline, the write fails. If you would like to see local modifications or buffer writes until the client is online, use the full Firestore SDK.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [setDoc(reference, data, options)](https://firebase.google.com/docs/reference/js/firestore_lite.md#setdoc_ff80739)                                           | Writes to the document referred to by the specified `DocumentReference`. If the document does not yet exist, it will be created. If you provide `merge` or `mergeFields`, the provided data can be merged into an existing document.The result of this write will only be reflected in document reads that occur after the returned promise resolves. If the client is offline, the write fails. If you would like to see local modifications or buffer writes until the client is online, use the full Firestore SDK.                                                                                                                                                                                                                                                                                                                                                                              |
| [updateDoc(reference, data)](https://firebase.google.com/docs/reference/js/firestore_lite.md#updatedoc_51a65e3)                                              | Updates fields in the document referred to by the specified `DocumentReference`. The update will fail if applied to a document that does not exist.The result of this update will only be reflected in document reads that occur after the returned promise resolves. If the client is offline, the update fails. If you would like to see local modifications or buffer writes until the client is online, use the full Firestore SDK.                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [updateDoc(reference, field, value, moreFieldsAndValues)](https://firebase.google.com/docs/reference/js/firestore_lite.md#updatedoc_7c28659)                 | Updates fields in the document referred to by the specified `DocumentReference` The update will fail if applied to a document that does not exist.Nested fields can be updated by providing dot-separated field path strings or by providing `FieldPath` objects.The result of this update will only be reflected in document reads that occur after the returned promise resolves. If the client is offline, the update fails. If you would like to see local modifications or buffer writes until the client is online, use the full Firestore SDK.                                                                                                                                                                                                                                                                                                                                               |
| **function(snapshot, ...)**                                                                                                                                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [endAt(snapshot)](https://firebase.google.com/docs/reference/js/firestore_lite.md#endat_9a4477f)                                                             | Creates a [QueryEndAtConstraint](https://firebase.google.com/docs/reference/js/firestore_.queryendatconstraint.md#queryendatconstraint_class) that modifies the result set to end at the provided document (inclusive). The end position is relative to the order of the query. The document must contain all of the fields provided in the orderBy of the query.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [endBefore(snapshot)](https://firebase.google.com/docs/reference/js/firestore_lite.md#endbefore_9a4477f)                                                     | Creates a [QueryEndAtConstraint](https://firebase.google.com/docs/reference/js/firestore_.queryendatconstraint.md#queryendatconstraint_class) that modifies the result set to end before the provided document (exclusive). The end position is relative to the order of the query. The document must contain all of the fields provided in the orderBy of the query.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [startAfter(snapshot)](https://firebase.google.com/docs/reference/js/firestore_lite.md#startafter_9a4477f)                                                   | Creates a [QueryStartAtConstraint](https://firebase.google.com/docs/reference/js/firestore_.querystartatconstraint.md#querystartatconstraint_class) that modifies the result set to start after the provided document (exclusive). The starting position is relative to the order of the query. The document must contain all of the fields provided in the orderBy of the query.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [startAt(snapshot)](https://firebase.google.com/docs/reference/js/firestore_lite.md#startat_9a4477f)                                                         | Creates a [QueryStartAtConstraint](https://firebase.google.com/docs/reference/js/firestore_.querystartatconstraint.md#querystartatconstraint_class) that modifies the result set to start at the provided document (inclusive). The starting position is relative to the order of the query. The document must contain all of the fields provided in the `orderBy` of this query.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| **function(values, ...)**                                                                                                                                    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [vector(values)](https://firebase.google.com/docs/reference/js/firestore_lite.md#vector_0dbdaf2)                                                             | Creates a new `VectorValue` constructed with a copy of the given array of numbers.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |

## Classes

|                                                                                 Class                                                                                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [AggregateField](https://firebase.google.com/docs/reference/js/firestore_lite.aggregatefield.md#aggregatefield_class)                                                 | Represents an aggregation that can be performed by Firestore.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [AggregateQuerySnapshot](https://firebase.google.com/docs/reference/js/firestore_lite.aggregatequerysnapshot.md#aggregatequerysnapshot_class)                         | The results of executing an aggregation query.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [Bytes](https://firebase.google.com/docs/reference/js/firestore_lite.bytes.md#bytes_class)                                                                            | An immutable object representing an array of bytes.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [CollectionReference](https://firebase.google.com/docs/reference/js/firestore_lite.collectionreference.md#collectionreference_class)                                  | A `CollectionReference` object can be used for adding documents, getting document references, and querying for documents (using [query()](https://firebase.google.com/docs/reference/js/firestore_.md#query_9f7b0f4)).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [DocumentReference](https://firebase.google.com/docs/reference/js/firestore_lite.documentreference.md#documentreference_class)                                        | A `DocumentReference` refers to a document location in a Firestore database and can be used to write, read, or listen to the location. The document at the referenced location may or may not exist.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [DocumentSnapshot](https://firebase.google.com/docs/reference/js/firestore_lite.documentsnapshot.md#documentsnapshot_class)                                           | A `DocumentSnapshot` contains data read from a document in your Firestore database. The data can be extracted with `.data()` or `.get(<field>)` to get a specific field.For a `DocumentSnapshot` that points to a non-existing document, any data access will return 'undefined'. You can use the `exists()` method to explicitly verify a document's existence.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [FieldPath](https://firebase.google.com/docs/reference/js/firestore_lite.fieldpath.md#fieldpath_class)                                                                | A `FieldPath` refers to a field in a document. The path may consist of a single field name (referring to a top-level field in the document), or a list of field names (referring to a nested field in the document).Create a `FieldPath` by providing field names. If more than one field name is provided, the path will point to a nested field in a document.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [FieldValue](https://firebase.google.com/docs/reference/js/firestore_lite.fieldvalue.md#fieldvalue_class)                                                             | Sentinel values that can be used when writing document fields with `set()` or `update()`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [Firestore](https://firebase.google.com/docs/reference/js/firestore_lite.firestore.md#firestore_class)                                                                | The Cloud Firestore service interface.Do not call this constructor directly. Instead, use [getFirestore()](https://firebase.google.com/docs/reference/js/firestore_.md#getfirestore).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [FirestoreError](https://firebase.google.com/docs/reference/js/firestore_lite.firestoreerror.md#firestoreerror_class)                                                 | An error returned by a Firestore operation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [GeoPoint](https://firebase.google.com/docs/reference/js/firestore_lite.geopoint.md#geopoint_class)                                                                   | An immutable object representing a geographic location in Firestore. The location is represented as latitude/longitude pair.Latitude values are in the range of \[-90, 90\]. Longitude values are in the range of \[-180, 180\].                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [Query](https://firebase.google.com/docs/reference/js/firestore_lite.query.md#query_class)                                                                            | A `Query` refers to a query which you can read or listen to. You can also construct refined `Query` objects by adding filters and ordering.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [QueryCompositeFilterConstraint](https://firebase.google.com/docs/reference/js/firestore_lite.querycompositefilterconstraint.md#querycompositefilterconstraint_class) | A `QueryCompositeFilterConstraint` is used to narrow the set of documents returned by a Firestore query by performing the logical OR or AND of multiple [QueryFieldFilterConstraint](https://firebase.google.com/docs/reference/js/firestore_.queryfieldfilterconstraint.md#queryfieldfilterconstraint_class)s or [QueryCompositeFilterConstraint](https://firebase.google.com/docs/reference/js/firestore_.querycompositefilterconstraint.md#querycompositefilterconstraint_class)s. `QueryCompositeFilterConstraint`s are created by invoking [or()](https://firebase.google.com/docs/reference/js/firestore_.md#or_e72c712) or [and()](https://firebase.google.com/docs/reference/js/firestore_.md#and_e72c712) and can then be passed to [query()](https://firebase.google.com/docs/reference/js/firestore_.md#query_9f7b0f4) to create a new query instance that also contains the `QueryCompositeFilterConstraint`.                                                                                                                                                          |
| [QueryConstraint](https://firebase.google.com/docs/reference/js/firestore_lite.queryconstraint.md#queryconstraint_class)                                              | A `QueryConstraint` is used to narrow the set of documents returned by a Firestore query. `QueryConstraint`s are created by invoking [where()](https://firebase.google.com/docs/reference/js/firestore_.md#where_0fae4bf), [orderBy()](https://firebase.google.com/docs/reference/js/firestore_.md#orderby_006d61f), [startAt()](https://firebase.google.com/docs/reference/js/firestore_.md#startat_9a4477f), [startAfter()](https://firebase.google.com/docs/reference/js/firestore_.md#startafter_9a4477f), [endBefore()](https://firebase.google.com/docs/reference/js/firestore_.md#endbefore_9a4477f), [endAt()](https://firebase.google.com/docs/reference/js/firestore_.md#endat_9a4477f), [limit()](https://firebase.google.com/docs/reference/js/firestore_.md#limit_ec46c78), [limitToLast()](https://firebase.google.com/docs/reference/js/firestore_.md#limittolast_ec46c78) and can then be passed to [query()](https://firebase.google.com/docs/reference/js/firestore_.md#query_9f7b0f4) to create a new query instance that also contains this `QueryConstraint`. |
| [QueryDocumentSnapshot](https://firebase.google.com/docs/reference/js/firestore_lite.querydocumentsnapshot.md#querydocumentsnapshot_class)                            | A `QueryDocumentSnapshot` contains data read from a document in your Firestore database as part of a query. The document is guaranteed to exist and its data can be extracted with `.data()` or `.get(<field>)` to get a specific field.A `QueryDocumentSnapshot` offers the same API surface as a `DocumentSnapshot`. Since query results contain only existing documents, the `exists` property will always be true and `data()` will never return 'undefined'.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [QueryEndAtConstraint](https://firebase.google.com/docs/reference/js/firestore_lite.queryendatconstraint.md#queryendatconstraint_class)                               | A `QueryEndAtConstraint` is used to exclude documents from the end of a result set returned by a Firestore query. `QueryEndAtConstraint`s are created by invoking [endAt()](https://firebase.google.com/docs/reference/js/firestore_.md#endat_9a4477f) or [endBefore()](https://firebase.google.com/docs/reference/js/firestore_.md#endbefore_9a4477f) and can then be passed to [query()](https://firebase.google.com/docs/reference/js/firestore_.md#query_9f7b0f4) to create a new query instance that also contains this `QueryEndAtConstraint`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [QueryFieldFilterConstraint](https://firebase.google.com/docs/reference/js/firestore_lite.queryfieldfilterconstraint.md#queryfieldfilterconstraint_class)             | A `QueryFieldFilterConstraint` is used to narrow the set of documents returned by a Firestore query by filtering on one or more document fields. `QueryFieldFilterConstraint`s are created by invoking [where()](https://firebase.google.com/docs/reference/js/firestore_.md#where_0fae4bf) and can then be passed to [query()](https://firebase.google.com/docs/reference/js/firestore_.md#query_9f7b0f4) to create a new query instance that also contains this `QueryFieldFilterConstraint`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [QueryLimitConstraint](https://firebase.google.com/docs/reference/js/firestore_lite.querylimitconstraint.md#querylimitconstraint_class)                               | A `QueryLimitConstraint` is used to limit the number of documents returned by a Firestore query. `QueryLimitConstraint`s are created by invoking [limit()](https://firebase.google.com/docs/reference/js/firestore_.md#limit_ec46c78) or [limitToLast()](https://firebase.google.com/docs/reference/js/firestore_.md#limittolast_ec46c78) and can then be passed to [query()](https://firebase.google.com/docs/reference/js/firestore_.md#query_9f7b0f4) to create a new query instance that also contains this `QueryLimitConstraint`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [QueryOrderByConstraint](https://firebase.google.com/docs/reference/js/firestore_lite.queryorderbyconstraint.md#queryorderbyconstraint_class)                         | A `QueryOrderByConstraint` is used to sort the set of documents returned by a Firestore query. `QueryOrderByConstraint`s are created by invoking [orderBy()](https://firebase.google.com/docs/reference/js/firestore_.md#orderby_006d61f) and can then be passed to [query()](https://firebase.google.com/docs/reference/js/firestore_.md#query_9f7b0f4) to create a new query instance that also contains this `QueryOrderByConstraint`.Note: Documents that do not contain the orderBy field will not be present in the query result.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [QuerySnapshot](https://firebase.google.com/docs/reference/js/firestore_lite.querysnapshot.md#querysnapshot_class)                                                    | A `QuerySnapshot` contains zero or more `DocumentSnapshot` objects representing the results of a query. The documents can be accessed as an array via the `docs` property or enumerated using the `forEach` method. The number of documents can be determined via the `empty` and `size` properties.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [QueryStartAtConstraint](https://firebase.google.com/docs/reference/js/firestore_lite.querystartatconstraint.md#querystartatconstraint_class)                         | A `QueryStartAtConstraint` is used to exclude documents from the start of a result set returned by a Firestore query. `QueryStartAtConstraint`s are created by invoking [startAt()](https://firebase.google.com/docs/reference/js/firestore_.md#startat_9a4477f) or [startAfter()](https://firebase.google.com/docs/reference/js/firestore_.md#startafter_9a4477f) and can then be passed to [query()](https://firebase.google.com/docs/reference/js/firestore_.md#query_9f7b0f4) to create a new query instance that also contains this `QueryStartAtConstraint`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [Timestamp](https://firebase.google.com/docs/reference/js/firestore_lite.timestamp.md#timestamp_class)                                                                | A `Timestamp` represents a point in time independent of any time zone or calendar, represented as seconds and fractions of seconds at nanosecond resolution in UTC Epoch time.It is encoded using the Proleptic Gregorian Calendar which extends the Gregorian calendar backwards to year one. It is encoded assuming all minutes are 60 seconds long, i.e. leap seconds are "smeared" so that no leap second table is needed for interpretation. Range is from 0001-01-01T00:00:00Z to 9999-12-31T23:59:59.999999999Z.For examples and further specifications, refer to the [Timestamp definition](https://github.com/google/protobuf/blob/master/src/google/protobuf/timestamp.proto).                                                                                                                                                                                                                                                                                                                                                                                           |
| [Transaction](https://firebase.google.com/docs/reference/js/firestore_lite.transaction.md#transaction_class)                                                          | A reference to a transaction.The `Transaction` object passed to a transaction's `updateFunction` provides the methods to read and write data within the transaction context. See [runTransaction()](https://firebase.google.com/docs/reference/js/firestore_.md#runtransaction_6f03ec4).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [VectorValue](https://firebase.google.com/docs/reference/js/firestore_lite.vectorvalue.md#vectorvalue_class)                                                          | Represents a vector type in Firestore documents. Create an instance with [vector()](https://firebase.google.com/docs/reference/js/firestore_.md#vector_0dbdaf2). VectorValue                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [WriteBatch](https://firebase.google.com/docs/reference/js/firestore_lite.writebatch.md#writebatch_class)                                                             | A write batch, used to perform multiple writes as a single atomic unit.A `WriteBatch` object can be acquired by calling [writeBatch()](https://firebase.google.com/docs/reference/js/firestore_.md#writebatch_231a8e0). It provides methods for adding writes to the write batch. None of the writes will be committed (or visible locally) until [WriteBatch.commit()](https://firebase.google.com/docs/reference/js/firestore_.writebatch.md#writebatchcommit) is called.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |

## Interfaces

|                                                                     Interface                                                                     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|---------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [AggregateSpec](https://firebase.google.com/docs/reference/js/firestore_lite.aggregatespec.md#aggregatespec_interface)                            | Specifies a set of aggregations and their aliases.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [DocumentData](https://firebase.google.com/docs/reference/js/firestore_lite.documentdata.md#documentdata_interface)                               | Document data (for use with [setDoc()](https://firebase.google.com/docs/reference/js/firestore_lite.md#setdoc_ee215ad)) consists of fields mapped to values.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [FirestoreDataConverter](https://firebase.google.com/docs/reference/js/firestore_lite.firestoredataconverter.md#firestoredataconverter_interface) | Converter used by `withConverter()` to transform user objects of type `AppModelType` into Firestore data of type `DbModelType`.Using the converter allows you to specify generic type arguments when storing and retrieving objects from Firestore.In this context, an "AppModel" is a class that is used in an application to package together related information and functionality. Such a class could, for example, have properties with complex, nested data types, properties used for memoization, properties of types not supported by Firestore (such as `symbol` and `bigint`), and helper functions that perform compound operations. Such classes are not suitable and/or possible to store into a Firestore database. Instead, instances of such classes need to be converted to "plain old JavaScript objects" (POJOs) with exclusively primitive properties, potentially nested inside other POJOs or arrays of POJOs. In this context, this type is referred to as the "DbModel" and would be an object suitable for persisting into Firestore. For convenience, applications can implement `FirestoreDataConverter` and register the converter with Firestore objects, such as `DocumentReference` or `Query`, to automatically convert `AppModel` to `DbModel` when storing into Firestore, and convert `DbModel` to `AppModel` when retrieving from Firestore. |
| [Settings](https://firebase.google.com/docs/reference/js/firestore_lite.settings.md#settings_interface)                                           | Specifies custom configurations for your Cloud Firestore instance. You must set these before invoking any other methods.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [TransactionOptions](https://firebase.google.com/docs/reference/js/firestore_lite.transactionoptions.md#transactionoptions_interface)             | Options to customize transaction behavior.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |

## Type Aliases

|                                                      Type Alias                                                      |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|----------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [AddPrefixToKeys](https://firebase.google.com/docs/reference/js/firestore_lite.md#addprefixtokeys)                   | Returns a new map where every key is prefixed with the outer key appended to a dot.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [AggregateFieldType](https://firebase.google.com/docs/reference/js/firestore_lite.md#aggregatefieldtype)             | The union of all `AggregateField` types that are supported by Firestore.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [AggregateSpecData](https://firebase.google.com/docs/reference/js/firestore_lite.md#aggregatespecdata)               | A type whose keys are taken from an `AggregateSpec`, and whose values are the result of the aggregation performed by the corresponding `AggregateField` from the input `AggregateSpec`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [AggregateType](https://firebase.google.com/docs/reference/js/firestore_lite.md#aggregatetype)                       | Union type representing the aggregate type to be performed.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [ChildUpdateFields](https://firebase.google.com/docs/reference/js/firestore_lite.md#childupdatefields)               | Helper for calculating the nested fields for a given type T1. This is needed to distribute union types such as `undefined | {...}` (happens for optional props) or `{a: A} | {b: B}`.In this use case, `V` is used to distribute the union types of `T[K]` on `Record`, since `T[K]` is evaluated as an expression and not distributed.See https://www.typescriptlang.org/docs/handbook/advanced-types.html#distributive-conditional-types                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [FirestoreErrorCode](https://firebase.google.com/docs/reference/js/firestore_lite.md#firestoreerrorcode)             | The set of Firestore status codes. The codes are the same at the ones exposed by gRPC here: https://github.com/grpc/grpc/blob/master/doc/statuscodes.mdPossible values: - 'cancelled': The operation was cancelled (typically by the caller). - 'unknown': Unknown error or an error from a different error domain. - 'invalid-argument': Client specified an invalid argument. Note that this differs from 'failed-precondition'. 'invalid-argument' indicates arguments that are problematic regardless of the state of the system (e.g. an invalid field name). - 'deadline-exceeded': Deadline expired before operation could complete. For operations that change the state of the system, this error may be returned even if the operation has completed successfully. For example, a successful response from a server could have been delayed long enough for the deadline to expire. - 'not-found': Some requested document was not found. - 'already-exists': Some document that we attempted to create already exists. - 'permission-denied': The caller does not have permission to execute the specified operation. - 'resource-exhausted': Some resource has been exhausted, perhaps a per-user quota, or perhaps the entire file system is out of space. - 'failed-precondition': Operation was rejected because the system is not in a state required for the operation's execution. - 'aborted': The operation was aborted, typically due to a concurrency issue like transaction aborts, etc. - 'out-of-range': Operation was attempted past the valid range. - 'unimplemented': Operation is not implemented or not supported/enabled. - 'internal': Internal errors. Means some invariants expected by underlying system has been broken. If you see one of these errors, something is very broken. - 'unavailable': The service is currently unavailable. This is most likely a transient condition and may be corrected by retrying with a backoff. - 'data-loss': Unrecoverable data loss or corruption. - 'unauthenticated': The request does not have valid authentication credentials for the operation. |
| [NestedUpdateFields](https://firebase.google.com/docs/reference/js/firestore_lite.md#nestedupdatefields)             | For each field (e.g. 'bar'), find all nested keys (e.g. {'bar.baz': T1, 'bar.qux': T2}). Intersect them together to make a single map containing all possible keys that are all marked as optional                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [OrderByDirection](https://firebase.google.com/docs/reference/js/firestore_lite.md#orderbydirection)                 | The direction of a [orderBy()](https://firebase.google.com/docs/reference/js/firestore_.md#orderby_006d61f) clause is specified as 'desc' or 'asc' (descending or ascending).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [PartialWithFieldValue](https://firebase.google.com/docs/reference/js/firestore_lite.md#partialwithfieldvalue)       | Similar to TypeScript's `Partial<T>`, but allows nested fields to be omitted and FieldValues to be passed in as property values.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [Primitive](https://firebase.google.com/docs/reference/js/firestore_lite.md#primitive)                               | Primitive types.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [QueryConstraintType](https://firebase.google.com/docs/reference/js/firestore_lite.md#queryconstrainttype)           | Describes the different query constraints available in this SDK.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [QueryFilterConstraint](https://firebase.google.com/docs/reference/js/firestore_lite.md#queryfilterconstraint)       | `QueryFilterConstraint` is a helper union type that represents [QueryFieldFilterConstraint](https://firebase.google.com/docs/reference/js/firestore_.queryfieldfilterconstraint.md#queryfieldfilterconstraint_class) and [QueryCompositeFilterConstraint](https://firebase.google.com/docs/reference/js/firestore_.querycompositefilterconstraint.md#querycompositefilterconstraint_class).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [QueryNonFilterConstraint](https://firebase.google.com/docs/reference/js/firestore_lite.md#querynonfilterconstraint) | `QueryNonFilterConstraint` is a helper union type that represents QueryConstraints which are used to narrow or order the set of documents, but that do not explicitly filter on a document field. `QueryNonFilterConstraint`s are created by invoking [orderBy()](https://firebase.google.com/docs/reference/js/firestore_.md#orderby_006d61f), [startAt()](https://firebase.google.com/docs/reference/js/firestore_.md#startat_9a4477f), [startAfter()](https://firebase.google.com/docs/reference/js/firestore_.md#startafter_9a4477f), [endBefore()](https://firebase.google.com/docs/reference/js/firestore_.md#endbefore_9a4477f), [endAt()](https://firebase.google.com/docs/reference/js/firestore_.md#endat_9a4477f), [limit()](https://firebase.google.com/docs/reference/js/firestore_.md#limit_ec46c78) or [limitToLast()](https://firebase.google.com/docs/reference/js/firestore_.md#limittolast_ec46c78) and can then be passed to [query()](https://firebase.google.com/docs/reference/js/firestore_.md#query_9f7b0f4) to create a new query instance that also contains the `QueryConstraint`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [SetOptions](https://firebase.google.com/docs/reference/js/firestore_lite.md#setoptions)                             | An options object that configures the behavior of [setDoc()](https://firebase.google.com/docs/reference/js/firestore_lite.md#setdoc_ee215ad), and calls. These calls can be configured to perform granular merges instead of overwriting the target documents in their entirety by providing a `SetOptions` with `merge: true`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [UnionToIntersection](https://firebase.google.com/docs/reference/js/firestore_lite.md#uniontointersection)           | Given a union type `U = T1 | T2 | ...`, returns an intersected type `(T1 & T2 & ...)`.Uses distributive conditional types and inference from conditional types. This works because multiple candidates for the same type variable in contra-variant positions causes an intersection type to be inferred. https://www.typescriptlang.org/docs/handbook/advanced-types.html#type-inference-in-conditional-types https://stackoverflow.com/questions/50374908/transform-union-type-to-intersection-type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [UpdateData](https://firebase.google.com/docs/reference/js/firestore_lite.md#updatedata)                             | Update data (for use with [updateDoc()](https://firebase.google.com/docs/reference/js/firestore_.md#updatedoc_51a65e3)) that consists of field paths (e.g. 'foo' or 'foo.baz') mapped to values. Fields that contain dots reference nested fields within the document. FieldValues can be passed in as property values.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [WhereFilterOp](https://firebase.google.com/docs/reference/js/firestore_lite.md#wherefilterop)                       | Filter conditions in a [where()](https://firebase.google.com/docs/reference/js/firestore_.md#where_0fae4bf) clause are specified using the strings '\&lt;', '\&lt;=', '==', '!=', '\&gt;=', '\&gt;', 'array-contains', 'in', 'array-contains-any', and 'not-in'.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [WithFieldValue](https://firebase.google.com/docs/reference/js/firestore_lite.md#withfieldvalue)                     | Allows FieldValues to be passed in as a property value while maintaining type safety.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |

## function(app, ...)

### getFirestore(app)

Returns the existing default [Firestore](https://firebase.google.com/docs/reference/js/firestore_.firestore.md#firestore_class) instance that is associated with the provided [FirebaseApp](https://firebase.google.com/docs/reference/js/app.firebaseapp.md#firebaseapp_interface). If no instance exists, initializes a new instance with default settings.

**Signature:**  

    export declare function getFirestore(app: FirebaseApp): Firestore;

#### Parameters

| Parameter |                                                 Type                                                  |                                                                                                                             Description                                                                                                                              |
|-----------|-------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| app       | [FirebaseApp](https://firebase.google.com/docs/reference/js/app.firebaseapp.md#firebaseapp_interface) | The [FirebaseApp](https://firebase.google.com/docs/reference/js/app.firebaseapp.md#firebaseapp_interface) instance that the returned [Firestore](https://firebase.google.com/docs/reference/js/firestore_.firestore.md#firestore_class) instance is associated with. |

**Returns:**

[Firestore](https://firebase.google.com/docs/reference/js/firestore_lite.firestore.md#firestore_class)

The [Firestore](https://firebase.google.com/docs/reference/js/firestore_.firestore.md#firestore_class) instance of the provided app.

### getFirestore(app, databaseId)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Returns the existing [Firestore](https://firebase.google.com/docs/reference/js/firestore_.firestore.md#firestore_class) instance that is associated with the provided [FirebaseApp](https://firebase.google.com/docs/reference/js/app.firebaseapp.md#firebaseapp_interface). If no instance exists, initializes a new instance with default settings.

**Signature:**  

    export declare function getFirestore(app: FirebaseApp, databaseId: string): Firestore;

#### Parameters

| Parameter  |                                                 Type                                                  |                                                                                                                             Description                                                                                                                              |
|------------|-------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| app        | [FirebaseApp](https://firebase.google.com/docs/reference/js/app.firebaseapp.md#firebaseapp_interface) | The [FirebaseApp](https://firebase.google.com/docs/reference/js/app.firebaseapp.md#firebaseapp_interface) instance that the returned [Firestore](https://firebase.google.com/docs/reference/js/firestore_.firestore.md#firestore_class) instance is associated with. |
| databaseId | string                                                                                                | The name of the database.                                                                                                                                                                                                                                            |

**Returns:**

[Firestore](https://firebase.google.com/docs/reference/js/firestore_lite.firestore.md#firestore_class)

The [Firestore](https://firebase.google.com/docs/reference/js/firestore_.firestore.md#firestore_class) instance of the provided app.

### initializeFirestore(app, settings)

Initializes a new instance of Cloud Firestore with the provided settings. Can only be called before any other functions, including [getFirestore()](https://firebase.google.com/docs/reference/js/firestore_.md#getfirestore). If the custom settings are empty, this function is equivalent to calling [getFirestore()](https://firebase.google.com/docs/reference/js/firestore_.md#getfirestore).

**Signature:**  

    export declare function initializeFirestore(app: FirebaseApp, settings: Settings): Firestore;

#### Parameters

| Parameter |                                                  Type                                                   |                                                                            Description                                                                            |
|-----------|---------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| app       | [FirebaseApp](https://firebase.google.com/docs/reference/js/app.firebaseapp.md#firebaseapp_interface)   | The [FirebaseApp](https://firebase.google.com/docs/reference/js/app.firebaseapp.md#firebaseapp_interface) with which the `Firestore` instance will be associated. |
| settings  | [Settings](https://firebase.google.com/docs/reference/js/firestore_lite.settings.md#settings_interface) | A settings object to configure the `Firestore` instance.                                                                                                          |

**Returns:**

[Firestore](https://firebase.google.com/docs/reference/js/firestore_lite.firestore.md#firestore_class)

A newly initialized `Firestore` instance.

### initializeFirestore(app, settings, databaseId)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Initializes a new instance of Cloud Firestore with the provided settings. Can only be called before any other functions, including [getFirestore()](https://firebase.google.com/docs/reference/js/firestore_.md#getfirestore). If the custom settings are empty, this function is equivalent to calling [getFirestore()](https://firebase.google.com/docs/reference/js/firestore_.md#getfirestore).

**Signature:**  

    export declare function initializeFirestore(app: FirebaseApp, settings: Settings, databaseId?: string): Firestore;

#### Parameters

| Parameter  |                                                  Type                                                   |                                                                            Description                                                                            |
|------------|---------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| app        | [FirebaseApp](https://firebase.google.com/docs/reference/js/app.firebaseapp.md#firebaseapp_interface)   | The [FirebaseApp](https://firebase.google.com/docs/reference/js/app.firebaseapp.md#firebaseapp_interface) with which the `Firestore` instance will be associated. |
| settings   | [Settings](https://firebase.google.com/docs/reference/js/firestore_lite.settings.md#settings_interface) | A settings object to configure the `Firestore` instance.                                                                                                          |
| databaseId | string                                                                                                  | The name of the database.                                                                                                                                         |

**Returns:**

[Firestore](https://firebase.google.com/docs/reference/js/firestore_lite.firestore.md#firestore_class)

A newly initialized `Firestore` instance.

## function(firestore, ...)

### collection(firestore, path, pathSegments)

Gets a `CollectionReference` instance that refers to the collection at the specified absolute path.

**Signature:**  

    export declare function collection(firestore: Firestore, path: string, ...pathSegments: string[]): CollectionReference<DocumentData, DocumentData>;

#### Parameters

|  Parameter   |                                                  Type                                                  |                            Description                            |
|--------------|--------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------|
| firestore    | [Firestore](https://firebase.google.com/docs/reference/js/firestore_lite.firestore.md#firestore_class) | A reference to the root `Firestore` instance.                     |
| path         | string                                                                                                 | A slash-separated path to a collection.                           |
| pathSegments | string\[\]                                                                                             | Additional path segments to apply relative to the first argument. |

**Returns:**

[CollectionReference](https://firebase.google.com/docs/reference/js/firestore_lite.collectionreference.md#collectionreference_class)\<[DocumentData](https://firebase.google.com/docs/reference/js/firestore_lite.documentdata.md#documentdata_interface), [DocumentData](https://firebase.google.com/docs/reference/js/firestore_lite.documentdata.md#documentdata_interface)\>

The `CollectionReference` instance.

#### Exceptions

If the final path has an even number of segments and does not point to a collection.

### collectionGroup(firestore, collectionId)

Creates and returns a new `Query` instance that includes all documents in the database that are contained in a collection or subcollection with the given `collectionId`.

**Signature:**  

    export declare function collectionGroup(firestore: Firestore, collectionId: string): Query<DocumentData, DocumentData>;

#### Parameters

|  Parameter   |                                                  Type                                                  |                                                                            Description                                                                             |
|--------------|--------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| firestore    | [Firestore](https://firebase.google.com/docs/reference/js/firestore_lite.firestore.md#firestore_class) | A reference to the root `Firestore` instance.                                                                                                                      |
| collectionId | string                                                                                                 | Identifies the collections to query over. Every collection or subcollection with this ID as the last segment of its path will be included. Cannot contain a slash. |

**Returns:**

[Query](https://firebase.google.com/docs/reference/js/firestore_lite.query.md#query_class)\<[DocumentData](https://firebase.google.com/docs/reference/js/firestore_lite.documentdata.md#documentdata_interface), [DocumentData](https://firebase.google.com/docs/reference/js/firestore_lite.documentdata.md#documentdata_interface)\>

The created `Query`.

### connectFirestoreEmulator(firestore, host, port, options)

Modify this instance to communicate with the Cloud Firestore emulator.
| **Note:** This must be called before this instance has been used to do any operations.

**Signature:**  

    export declare function connectFirestoreEmulator(firestore: Firestore, host: string, port: number, options?: {
        mockUserToken?: EmulatorMockTokenOptions | string;
    }): void;

#### Parameters

| Parameter |                                                                   Type                                                                    |                            Description                            |
|-----------|-------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------|
| firestore | [Firestore](https://firebase.google.com/docs/reference/js/firestore_lite.firestore.md#firestore_class)                                    | The `Firestore` instance to configure to connect to the emulator. |
| host      | string                                                                                                                                    | the emulator host (ex: localhost).                                |
| port      | number                                                                                                                                    | the emulator port (ex: 9000).                                     |
| options   | { mockUserToken?: [EmulatorMockTokenOptions](https://firebase.google.com/docs/reference/js/util.md#emulatormocktokenoptions) \| string; } |                                                                   |

**Returns:**

void

### doc(firestore, path, pathSegments)

Gets a `DocumentReference` instance that refers to the document at the specified absolute path.

**Signature:**  

    export declare function doc(firestore: Firestore, path: string, ...pathSegments: string[]): DocumentReference<DocumentData, DocumentData>;

#### Parameters

|  Parameter   |                                                  Type                                                  |                                  Description                                  |
|--------------|--------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------|
| firestore    | [Firestore](https://firebase.google.com/docs/reference/js/firestore_lite.firestore.md#firestore_class) | A reference to the root `Firestore` instance.                                 |
| path         | string                                                                                                 | A slash-separated path to a document.                                         |
| pathSegments | string\[\]                                                                                             | Additional path segments that will be applied relative to the first argument. |

**Returns:**

[DocumentReference](https://firebase.google.com/docs/reference/js/firestore_lite.documentreference.md#documentreference_class)\<[DocumentData](https://firebase.google.com/docs/reference/js/firestore_lite.documentdata.md#documentdata_interface), [DocumentData](https://firebase.google.com/docs/reference/js/firestore_lite.documentdata.md#documentdata_interface)\>

The `DocumentReference` instance.

#### Exceptions

If the final path has an odd number of segments and does not point to a document.

### runTransaction(firestore, updateFunction, options)

Executes the given `updateFunction` and then attempts to commit the changes applied within the transaction. If any document read within the transaction has changed, Cloud Firestore retries the `updateFunction`. If it fails to commit after 5 attempts, the transaction fails.

The maximum number of writes allowed in a single transaction is 500.

**Signature:**  

    export declare function runTransaction<T>(firestore: Firestore, updateFunction: (transaction: Transaction) => Promise<T>, options?: TransactionOptions): Promise<T>;

#### Parameters

|   Parameter    |                                                                     Type                                                                     |                              Description                               |
|----------------|----------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------|
| firestore      | [Firestore](https://firebase.google.com/docs/reference/js/firestore_lite.firestore.md#firestore_class)                                       | A reference to the Firestore database to run this transaction against. |
| updateFunction | (transaction: [Transaction](https://firebase.google.com/docs/reference/js/firestore_lite.transaction.md#transaction_class)) =\> Promise\<T\> | The function to execute within the transaction context.                |
| options        | [TransactionOptions](https://firebase.google.com/docs/reference/js/firestore_lite.transactionoptions.md#transactionoptions_interface)        | An options object to configure maximum number of attempts to commit.   |

**Returns:**

Promise\<T\>

If the transaction completed successfully or was explicitly aborted (the `updateFunction` returned a failed promise), the promise returned by the `updateFunction`is returned here. Otherwise, if the transaction failed, a rejected promise with the corresponding failure error is returned.

### terminate(firestore)

Terminates the provided `Firestore` instance.

After calling `terminate()` only the `clearIndexedDbPersistence()` functions may be used. Any other function will throw a `FirestoreError`. Termination does not cancel any pending writes, and any promises that are awaiting a response from the server will not be resolved.

To restart after termination, create a new instance of `Firestore` with [getFirestore()](https://firebase.google.com/docs/reference/js/firestore_.md#getfirestore).
| **Note:** Under normal circumstances, calling `terminate()` is not required. This function is useful only when you want to force this instance to release all of its resources or in combination with [clearIndexedDbPersistence()](https://firebase.google.com/docs/reference/js/firestore_.md#clearindexeddbpersistence_231a8e0) to ensure that all local state is destroyed between test runs.

**Signature:**  

    export declare function terminate(firestore: Firestore): Promise<void>;

#### Parameters

| Parameter |                                                  Type                                                  |              Description               |
|-----------|--------------------------------------------------------------------------------------------------------|----------------------------------------|
| firestore | [Firestore](https://firebase.google.com/docs/reference/js/firestore_lite.firestore.md#firestore_class) | The `Firestore` instance to terminate. |

**Returns:**

Promise\<void\>

A `Promise` that is resolved when the instance has been successfully terminated.

### writeBatch(firestore)

Creates a write batch, used for performing multiple writes as a single atomic operation. The maximum number of writes allowed in a single WriteBatch is 500.

The result of these writes will only be reflected in document reads that occur after the returned promise resolves. If the client is offline, the write fails. If you would like to see local modifications or buffer writes until the client is online, use the full Firestore SDK.

**Signature:**  

    export declare function writeBatch(firestore: Firestore): WriteBatch;

#### Parameters

| Parameter |                                                  Type                                                  | Description |
|-----------|--------------------------------------------------------------------------------------------------------|-------------|
| firestore | [Firestore](https://firebase.google.com/docs/reference/js/firestore_lite.firestore.md#firestore_class) |             |

**Returns:**

[WriteBatch](https://firebase.google.com/docs/reference/js/firestore_lite.writebatch.md#writebatch_class)

A `WriteBatch` that can be used to atomically execute multiple writes.

## function()

### count()

Create an AggregateField object that can be used to compute the count of documents in the result set of a query.

**Signature:**  

    export declare function count(): AggregateField<number>;

**Returns:**

[AggregateField](https://firebase.google.com/docs/reference/js/firestore_lite.aggregatefield.md#aggregatefield_class)\<number\>

### deleteField()

Returns a sentinel for use with [updateDoc()](https://firebase.google.com/docs/reference/js/firestore_lite.md#updatedoc_51a65e3) or [setDoc()](https://firebase.google.com/docs/reference/js/firestore_lite.md#setdoc_ee215ad) with `{merge: true}` to mark a field for deletion.

**Signature:**  

    export declare function deleteField(): FieldValue;

**Returns:**

[FieldValue](https://firebase.google.com/docs/reference/js/firestore_lite.fieldvalue.md#fieldvalue_class)

### documentId()

Returns a special sentinel `FieldPath` to refer to the ID of a document. It can be used in queries to sort or filter by the document ID.

**Signature:**  

    export declare function documentId(): FieldPath;

**Returns:**

[FieldPath](https://firebase.google.com/docs/reference/js/firestore_lite.fieldpath.md#fieldpath_class)

### getFirestore()

Returns the existing default [Firestore](https://firebase.google.com/docs/reference/js/firestore_.firestore.md#firestore_class) instance that is associated with the default [FirebaseApp](https://firebase.google.com/docs/reference/js/app.firebaseapp.md#firebaseapp_interface). If no instance exists, initializes a new instance with default settings.

**Signature:**  

    export declare function getFirestore(): Firestore;

**Returns:**

[Firestore](https://firebase.google.com/docs/reference/js/firestore_lite.firestore.md#firestore_class)

The [Firestore](https://firebase.google.com/docs/reference/js/firestore_.firestore.md#firestore_class) instance of the provided app.

### serverTimestamp()

Returns a sentinel used with [setDoc()](https://firebase.google.com/docs/reference/js/firestore_lite.md#setdoc_ee215ad) or [updateDoc()](https://firebase.google.com/docs/reference/js/firestore_lite.md#updatedoc_51a65e3) to include a server-generated timestamp in the written data.

**Signature:**  

    export declare function serverTimestamp(): FieldValue;

**Returns:**

[FieldValue](https://firebase.google.com/docs/reference/js/firestore_lite.fieldvalue.md#fieldvalue_class)

## function(databaseId, ...)

### getFirestore(databaseId)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Returns the existing [Firestore](https://firebase.google.com/docs/reference/js/firestore_.firestore.md#firestore_class) instance that is associated with the default [FirebaseApp](https://firebase.google.com/docs/reference/js/app.firebaseapp.md#firebaseapp_interface). If no instance exists, initializes a new instance with default settings.

**Signature:**  

    export declare function getFirestore(databaseId: string): Firestore;

#### Parameters

| Parameter  |  Type  |        Description        |
|------------|--------|---------------------------|
| databaseId | string | The name of the database. |

**Returns:**

[Firestore](https://firebase.google.com/docs/reference/js/firestore_lite.firestore.md#firestore_class)

The [Firestore](https://firebase.google.com/docs/reference/js/firestore_.firestore.md#firestore_class) instance of the provided app.

## function(elements, ...)

### arrayRemove(elements)

Returns a special value that can be used with [setDoc()](https://firebase.google.com/docs/reference/js/firestore_.md#setdoc_ee215ad) or that tells the server to remove the given elements from any array value that already exists on the server. All instances of each element specified will be removed from the array. If the field being modified is not already an array it will be overwritten with an empty array.

**Signature:**  

    export declare function arrayRemove(...elements: unknown[]): FieldValue;

#### Parameters

| Parameter |    Type     |              Description               |
|-----------|-------------|----------------------------------------|
| elements  | unknown\[\] | The elements to remove from the array. |

**Returns:**

[FieldValue](https://firebase.google.com/docs/reference/js/firestore_lite.fieldvalue.md#fieldvalue_class)

The `FieldValue` sentinel for use in a call to `setDoc()` or `updateDoc()`

### arrayUnion(elements)

Returns a special value that can be used with [setDoc()](https://firebase.google.com/docs/reference/js/firestore_lite.md#setdoc_ee215ad) or [updateDoc()](https://firebase.google.com/docs/reference/js/firestore_lite.md#updatedoc_51a65e3) that tells the server to union the given elements with any array value that already exists on the server. Each specified element that doesn't already exist in the array will be added to the end. If the field being modified is not already an array it will be overwritten with an array containing exactly the specified elements.

**Signature:**  

    export declare function arrayUnion(...elements: unknown[]): FieldValue;

#### Parameters

| Parameter |    Type     |              Description              |
|-----------|-------------|---------------------------------------|
| elements  | unknown\[\] | The elements to union into the array. |

**Returns:**

[FieldValue](https://firebase.google.com/docs/reference/js/firestore_lite.fieldvalue.md#fieldvalue_class)

The `FieldValue` sentinel for use in a call to `setDoc()` or `updateDoc()`.

## function(field, ...)

### average(field)

Create an AggregateField object that can be used to compute the average of a specified field over a range of documents in the result set of a query.

**Signature:**  

    export declare function average(field: string | FieldPath): AggregateField<number | null>;

#### Parameters

| Parameter |                                                       Type                                                       |                      Description                      |
|-----------|------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------|
| field     | string \| [FieldPath](https://firebase.google.com/docs/reference/js/firestore_lite.fieldpath.md#fieldpath_class) | Specifies the field to average across the result set. |

**Returns:**

[AggregateField](https://firebase.google.com/docs/reference/js/firestore_lite.aggregatefield.md#aggregatefield_class)\<number \| null\>

### sum(field)

Create an AggregateField object that can be used to compute the sum of a specified field over a range of documents in the result set of a query.

**Signature:**  

    export declare function sum(field: string | FieldPath): AggregateField<number>;

#### Parameters

| Parameter |                                                       Type                                                       |                    Description                    |
|-----------|------------------------------------------------------------------------------------------------------------------|---------------------------------------------------|
| field     | string \| [FieldPath](https://firebase.google.com/docs/reference/js/firestore_lite.fieldpath.md#fieldpath_class) | Specifies the field to sum across the result set. |

**Returns:**

[AggregateField](https://firebase.google.com/docs/reference/js/firestore_lite.aggregatefield.md#aggregatefield_class)\<number\>

## function(fieldPath, ...)

### orderBy(fieldPath, directionStr)

Creates a [QueryOrderByConstraint](https://firebase.google.com/docs/reference/js/firestore_.queryorderbyconstraint.md#queryorderbyconstraint_class) that sorts the query result by the specified field, optionally in descending order instead of ascending.
| **Note:** Documents that do not contain the specified field will not be present in the query result.

**Signature:**  

    export declare function orderBy(fieldPath: string | FieldPath, directionStr?: OrderByDirection): QueryOrderByConstraint;

#### Parameters

|  Parameter   |                                                       Type                                                       |                                         Description                                         |
|--------------|------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|
| fieldPath    | string \| [FieldPath](https://firebase.google.com/docs/reference/js/firestore_lite.fieldpath.md#fieldpath_class) | The field to sort by.                                                                       |
| directionStr | [OrderByDirection](https://firebase.google.com/docs/reference/js/firestore_lite.md#orderbydirection)             | Optional direction to sort by ('asc' or 'desc'). If not specified, order will be ascending. |

**Returns:**

[QueryOrderByConstraint](https://firebase.google.com/docs/reference/js/firestore_lite.queryorderbyconstraint.md#queryorderbyconstraint_class)

The created [QueryOrderByConstraint](https://firebase.google.com/docs/reference/js/firestore_.queryorderbyconstraint.md#queryorderbyconstraint_class).

### where(fieldPath, opStr, value)

Creates a [QueryFieldFilterConstraint](https://firebase.google.com/docs/reference/js/firestore_.queryfieldfilterconstraint.md#queryfieldfilterconstraint_class) that enforces that documents must contain the specified field and that the value should satisfy the relation constraint provided.

**Signature:**  

    export declare function where(fieldPath: string | FieldPath, opStr: WhereFilterOp, value: unknown): QueryFieldFilterConstraint;

#### Parameters

| Parameter |                                                       Type                                                       |                                 Description                                  |
|-----------|------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------|
| fieldPath | string \| [FieldPath](https://firebase.google.com/docs/reference/js/firestore_lite.fieldpath.md#fieldpath_class) | The path to compare                                                          |
| opStr     | [WhereFilterOp](https://firebase.google.com/docs/reference/js/firestore_lite.md#wherefilterop)                   | The operation string (e.g "\&lt;", "\&lt;=", "==", "\&lt;", "\&lt;=", "!="). |
| value     | unknown                                                                                                          | The value for comparison                                                     |

**Returns:**

[QueryFieldFilterConstraint](https://firebase.google.com/docs/reference/js/firestore_lite.queryfieldfilterconstraint.md#queryfieldfilterconstraint_class)

The created [QueryFieldFilterConstraint](https://firebase.google.com/docs/reference/js/firestore_.queryfieldfilterconstraint.md#queryfieldfilterconstraint_class).

## function(fieldValues, ...)

### endAt(fieldValues)

Creates a [QueryEndAtConstraint](https://firebase.google.com/docs/reference/js/firestore_.queryendatconstraint.md#queryendatconstraint_class) that modifies the result set to end at the provided fields relative to the order of the query. The order of the field values must match the order of the order by clauses of the query.

**Signature:**  

    export declare function endAt(...fieldValues: unknown[]): QueryEndAtConstraint;

#### Parameters

|  Parameter  |    Type     |                               Description                                |
|-------------|-------------|--------------------------------------------------------------------------|
| fieldValues | unknown\[\] | The field values to end this query at, in order of the query's order by. |

**Returns:**

[QueryEndAtConstraint](https://firebase.google.com/docs/reference/js/firestore_lite.queryendatconstraint.md#queryendatconstraint_class)

A [QueryEndAtConstraint](https://firebase.google.com/docs/reference/js/firestore_.queryendatconstraint.md#queryendatconstraint_class) to pass to `query()`

### endBefore(fieldValues)

Creates a [QueryEndAtConstraint](https://firebase.google.com/docs/reference/js/firestore_.queryendatconstraint.md#queryendatconstraint_class) that modifies the result set to end before the provided fields relative to the order of the query. The order of the field values must match the order of the order by clauses of the query.

**Signature:**  

    export declare function endBefore(...fieldValues: unknown[]): QueryEndAtConstraint;

#### Parameters

|  Parameter  |    Type     |                                 Description                                  |
|-------------|-------------|------------------------------------------------------------------------------|
| fieldValues | unknown\[\] | The field values to end this query before, in order of the query's order by. |

**Returns:**

[QueryEndAtConstraint](https://firebase.google.com/docs/reference/js/firestore_lite.queryendatconstraint.md#queryendatconstraint_class)

A [QueryEndAtConstraint](https://firebase.google.com/docs/reference/js/firestore_.queryendatconstraint.md#queryendatconstraint_class) to pass to `query()`

### startAfter(fieldValues)

Creates a [QueryStartAtConstraint](https://firebase.google.com/docs/reference/js/firestore_.querystartatconstraint.md#querystartatconstraint_class) that modifies the result set to start after the provided fields relative to the order of the query. The order of the field values must match the order of the order by clauses of the query.

**Signature:**  

    export declare function startAfter(...fieldValues: unknown[]): QueryStartAtConstraint;

#### Parameters

|  Parameter  |    Type     |                                  Description                                  |
|-------------|-------------|-------------------------------------------------------------------------------|
| fieldValues | unknown\[\] | The field values to start this query after, in order of the query's order by. |

**Returns:**

[QueryStartAtConstraint](https://firebase.google.com/docs/reference/js/firestore_lite.querystartatconstraint.md#querystartatconstraint_class)

A [QueryStartAtConstraint](https://firebase.google.com/docs/reference/js/firestore_.querystartatconstraint.md#querystartatconstraint_class) to pass to `query()`

### startAt(fieldValues)

Creates a [QueryStartAtConstraint](https://firebase.google.com/docs/reference/js/firestore_.querystartatconstraint.md#querystartatconstraint_class) that modifies the result set to start at the provided fields relative to the order of the query. The order of the field values must match the order of the order by clauses of the query.

**Signature:**  

    export declare function startAt(...fieldValues: unknown[]): QueryStartAtConstraint;

#### Parameters

|  Parameter  |    Type     |                                Description                                 |
|-------------|-------------|----------------------------------------------------------------------------|
| fieldValues | unknown\[\] | The field values to start this query at, in order of the query's order by. |

**Returns:**

[QueryStartAtConstraint](https://firebase.google.com/docs/reference/js/firestore_lite.querystartatconstraint.md#querystartatconstraint_class)

A [QueryStartAtConstraint](https://firebase.google.com/docs/reference/js/firestore_.querystartatconstraint.md#querystartatconstraint_class) to pass to `query()`.

## function(left, ...)

### aggregateFieldEqual(left, right)

Compares two 'AggregateField\` instances for equality.

**Signature:**  

    export declare function aggregateFieldEqual(left: AggregateField<unknown>, right: AggregateField<unknown>): boolean;

#### Parameters

| Parameter |                                                               Type                                                               |                 Description                 |
|-----------|----------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------|
| left      | [AggregateField](https://firebase.google.com/docs/reference/js/firestore_lite.aggregatefield.md#aggregatefield_class)\<unknown\> | Compare this AggregateField to the `right`. |
| right     | [AggregateField](https://firebase.google.com/docs/reference/js/firestore_lite.aggregatefield.md#aggregatefield_class)\<unknown\> | Compare this AggregateField to the `left`.  |

**Returns:**

boolean

### aggregateQuerySnapshotEqual(left, right)

Compares two `AggregateQuerySnapshot` instances for equality.

Two `AggregateQuerySnapshot` instances are considered "equal" if they have underlying queries that compare equal, and the same data.

**Signature:**  

    export declare function aggregateQuerySnapshotEqual<AggregateSpecType extends AggregateSpec, AppModelType, DbModelType extends DocumentData>(left: AggregateQuerySnapshot<AggregateSpecType, AppModelType, DbModelType>, right: AggregateQuerySnapshot<AggregateSpecType, AppModelType, DbModelType>): boolean;

#### Parameters

| Parameter |                                                                                             Type                                                                                              |                   Description                   |
|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------|
| left      | [AggregateQuerySnapshot](https://firebase.google.com/docs/reference/js/firestore_lite.aggregatequerysnapshot.md#aggregatequerysnapshot_class)\<AggregateSpecType, AppModelType, DbModelType\> | The first `AggregateQuerySnapshot` to compare.  |
| right     | [AggregateQuerySnapshot](https://firebase.google.com/docs/reference/js/firestore_lite.aggregatequerysnapshot.md#aggregatequerysnapshot_class)\<AggregateSpecType, AppModelType, DbModelType\> | The second `AggregateQuerySnapshot` to compare. |

**Returns:**

boolean

`true` if the objects are "equal", as defined above, or `false` otherwise.

### queryEqual(left, right)

Returns true if the provided queries point to the same collection and apply the same constraints.

**Signature:**  

    export declare function queryEqual<AppModelType, DbModelType extends DocumentData>(left: Query<AppModelType, DbModelType>, right: Query<AppModelType, DbModelType>): boolean;

#### Parameters

| Parameter |                                                          Type                                                           |      Description      |
|-----------|-------------------------------------------------------------------------------------------------------------------------|-----------------------|
| left      | [Query](https://firebase.google.com/docs/reference/js/firestore_lite.query.md#query_class)\<AppModelType, DbModelType\> | A `Query` to compare. |
| right     | [Query](https://firebase.google.com/docs/reference/js/firestore_lite.query.md#query_class)\<AppModelType, DbModelType\> | A `Query` to compare. |

**Returns:**

boolean

true if the references point to the same location in the same Firestore database.

### refEqual(left, right)

Returns true if the provided references are equal.

**Signature:**  

    export declare function refEqual<AppModelType, DbModelType extends DocumentData>(left: DocumentReference<AppModelType, DbModelType> | CollectionReference<AppModelType, DbModelType>, right: DocumentReference<AppModelType, DbModelType> | CollectionReference<AppModelType, DbModelType>): boolean;

#### Parameters

| Parameter |                                                                                                                                                               Type                                                                                                                                                               |       Description       |
|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------|
| left      | [DocumentReference](https://firebase.google.com/docs/reference/js/firestore_lite.documentreference.md#documentreference_class)\<AppModelType, DbModelType\> \| [CollectionReference](https://firebase.google.com/docs/reference/js/firestore_lite.collectionreference.md#collectionreference_class)\<AppModelType, DbModelType\> | A reference to compare. |
| right     | [DocumentReference](https://firebase.google.com/docs/reference/js/firestore_lite.documentreference.md#documentreference_class)\<AppModelType, DbModelType\> \| [CollectionReference](https://firebase.google.com/docs/reference/js/firestore_lite.collectionreference.md#collectionreference_class)\<AppModelType, DbModelType\> | A reference to compare. |

**Returns:**

boolean

true if the references point to the same location in the same Firestore database.

### snapshotEqual(left, right)

Returns true if the provided snapshots are equal.

**Signature:**  

    export declare function snapshotEqual<AppModelType, DbModelType extends DocumentData>(left: DocumentSnapshot<AppModelType, DbModelType> | QuerySnapshot<AppModelType, DbModelType>, right: DocumentSnapshot<AppModelType, DbModelType> | QuerySnapshot<AppModelType, DbModelType>): boolean;

#### Parameters

| Parameter |                                                                                                                                                    Type                                                                                                                                                     |      Description       |
|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------|
| left      | [DocumentSnapshot](https://firebase.google.com/docs/reference/js/firestore_lite.documentsnapshot.md#documentsnapshot_class)\<AppModelType, DbModelType\> \| [QuerySnapshot](https://firebase.google.com/docs/reference/js/firestore_lite.querysnapshot.md#querysnapshot_class)\<AppModelType, DbModelType\> | A snapshot to compare. |
| right     | [DocumentSnapshot](https://firebase.google.com/docs/reference/js/firestore_lite.documentsnapshot.md#documentsnapshot_class)\<AppModelType, DbModelType\> \| [QuerySnapshot](https://firebase.google.com/docs/reference/js/firestore_lite.querysnapshot.md#querysnapshot_class)\<AppModelType, DbModelType\> | A snapshot to compare. |

**Returns:**

boolean

true if the snapshots are equal.

## function(limit, ...)

### limit(limit)

Creates a [QueryLimitConstraint](https://firebase.google.com/docs/reference/js/firestore_.querylimitconstraint.md#querylimitconstraint_class) that only returns the first matching documents.

**Signature:**  

    export declare function limit(limit: number): QueryLimitConstraint;

#### Parameters

| Parameter |  Type  |              Description               |
|-----------|--------|----------------------------------------|
| limit     | number | The maximum number of items to return. |

**Returns:**

[QueryLimitConstraint](https://firebase.google.com/docs/reference/js/firestore_lite.querylimitconstraint.md#querylimitconstraint_class)

The created [QueryLimitConstraint](https://firebase.google.com/docs/reference/js/firestore_.querylimitconstraint.md#querylimitconstraint_class).

### limitToLast(limit)

Creates a [QueryLimitConstraint](https://firebase.google.com/docs/reference/js/firestore_.querylimitconstraint.md#querylimitconstraint_class) that only returns the last matching documents.

You must specify at least one `orderBy` clause for `limitToLast` queries, otherwise an exception will be thrown during execution.

**Signature:**  

    export declare function limitToLast(limit: number): QueryLimitConstraint;

#### Parameters

| Parameter |  Type  |              Description               |
|-----------|--------|----------------------------------------|
| limit     | number | The maximum number of items to return. |

**Returns:**

[QueryLimitConstraint](https://firebase.google.com/docs/reference/js/firestore_lite.querylimitconstraint.md#querylimitconstraint_class)

The created [QueryLimitConstraint](https://firebase.google.com/docs/reference/js/firestore_.querylimitconstraint.md#querylimitconstraint_class).

## function(logLevel, ...)

### setLogLevel(logLevel)

Sets the verbosity of Cloud Firestore logs (debug, error, or silent).

**Signature:**  

    export declare function setLogLevel(logLevel: LogLevel): void;

#### Parameters

| Parameter |   Type   |                                                                                                             Description                                                                                                              |
|-----------|----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| logLevel  | LogLevel | The verbosity you set for activity and error logging. Can be any of the following values: - `debug` for the most verbose logging level, primarily for debugging. - `error` to log errors only. - `silent`` to turn off logging.` ` ` |

**Returns:**

void

## function(n, ...)

### increment(n)

Returns a special value that can be used with [setDoc()](https://firebase.google.com/docs/reference/js/firestore_lite.md#setdoc_ee215ad) or [updateDoc()](https://firebase.google.com/docs/reference/js/firestore_lite.md#updatedoc_51a65e3) that tells the server to increment the field's current value by the given value.

If either the operand or the current field value uses floating point precision, all arithmetic follows IEEE 754 semantics. If both values are integers, values outside of JavaScript's safe number range (`Number.MIN_SAFE_INTEGER` to `Number.MAX_SAFE_INTEGER`) are also subject to precision loss. Furthermore, once processed by the Firestore backend, all integer operations are capped between -2\^63 and 2\^63-1.

If the current field value is not of type `number`, or if the field does not yet exist, the transformation sets the field to the given value.

**Signature:**  

    export declare function increment(n: number): FieldValue;

#### Parameters

| Parameter |  Type  |        Description         |
|-----------|--------|----------------------------|
| n         | number | The value to increment by. |

**Returns:**

[FieldValue](https://firebase.google.com/docs/reference/js/firestore_lite.fieldvalue.md#fieldvalue_class)

The `FieldValue` sentinel for use in a call to `setDoc()` or `updateDoc()`

## function(query, ...)

### getAggregate(query, aggregateSpec)

Calculates the specified aggregations over the documents in the result set of the given query without actually downloading the documents.

Using this function to perform aggregations is efficient because only the final aggregation values, not the documents' data, are downloaded. This function can perform aggregations of the documents in cases where the result set is prohibitively large to download entirely (thousands of documents).

**Signature:**  

    export declare function getAggregate<AggregateSpecType extends AggregateSpec, AppModelType, DbModelType extends DocumentData>(query: Query<AppModelType, DbModelType>, aggregateSpec: AggregateSpecType): Promise<AggregateQuerySnapshot<AggregateSpecType, AppModelType, DbModelType>>;

#### Parameters

|   Parameter   |                                                          Type                                                           |                                                                                             Description                                                                                             |
|---------------|-------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| query         | [Query](https://firebase.google.com/docs/reference/js/firestore_lite.query.md#query_class)\<AppModelType, DbModelType\> | The query whose result set is aggregated over.                                                                                                                                                      |
| aggregateSpec | AggregateSpecType                                                                                                       | An `AggregateSpec` object that specifies the aggregates to perform over the result set. The AggregateSpec specifies aliases for each aggregate, which can be used to retrieve the aggregate result. |

**Returns:**

Promise\<[AggregateQuerySnapshot](https://firebase.google.com/docs/reference/js/firestore_lite.aggregatequerysnapshot.md#aggregatequerysnapshot_class)\<AggregateSpecType, AppModelType, DbModelType\>\>

### Example

    const aggregateSnapshot = await getAggregate(query, {
      countOfDocs: count(),
      totalHours: sum('hours'),
      averageScore: average('score')
    });

    const countOfDocs: number = aggregateSnapshot.data().countOfDocs;
    const totalHours: number = aggregateSnapshot.data().totalHours;
    const averageScore: number | null = aggregateSnapshot.data().averageScore;

### getCount(query)

Calculates the number of documents in the result set of the given query without actually downloading the documents.

Using this function to count the documents is efficient because only the final count, not the documents' data, is downloaded. This function can count the documents in cases where the result set is prohibitively large to download entirely (thousands of documents).

**Signature:**  

    export declare function getCount<AppModelType, DbModelType extends DocumentData>(query: Query<AppModelType, DbModelType>): Promise<AggregateQuerySnapshot<{
        count: AggregateField<number>;
    }, AppModelType, DbModelType>>;

#### Parameters

| Parameter |                                                          Type                                                           |                  Description                   |
|-----------|-------------------------------------------------------------------------------------------------------------------------|------------------------------------------------|
| query     | [Query](https://firebase.google.com/docs/reference/js/firestore_lite.query.md#query_class)\<AppModelType, DbModelType\> | The query whose result set size is calculated. |

**Returns:**

Promise\<[AggregateQuerySnapshot](https://firebase.google.com/docs/reference/js/firestore_lite.aggregatequerysnapshot.md#aggregatequerysnapshot_class)\<{ count: [AggregateField](https://firebase.google.com/docs/reference/js/firestore_lite.aggregatefield.md#aggregatefield_class)\<number\>; }, AppModelType, DbModelType\>\>

A Promise that will be resolved with the count; the count can be retrieved from `snapshot.data().count`, where `snapshot` is the `AggregateQuerySnapshot` to which the returned Promise resolves.

### getDocs(query)

Executes the query and returns the results as a [QuerySnapshot](https://firebase.google.com/docs/reference/js/firestore_.querysnapshot.md#querysnapshot_class).

All queries are executed directly by the server, even if the query was previously executed. Recent modifications are only reflected in the retrieved results if they have already been applied by the backend. If the client is offline, the operation fails. To see previously cached result and local modifications, use the full Firestore SDK.

**Signature:**  

    export declare function getDocs<AppModelType, DbModelType extends DocumentData>(query: Query<AppModelType, DbModelType>): Promise<QuerySnapshot<AppModelType, DbModelType>>;

#### Parameters

| Parameter |                                                          Type                                                           |       Description       |
|-----------|-------------------------------------------------------------------------------------------------------------------------|-------------------------|
| query     | [Query](https://firebase.google.com/docs/reference/js/firestore_lite.query.md#query_class)\<AppModelType, DbModelType\> | The `Query` to execute. |

**Returns:**

Promise\<[QuerySnapshot](https://firebase.google.com/docs/reference/js/firestore_lite.querysnapshot.md#querysnapshot_class)\<AppModelType, DbModelType\>\>

A Promise that will be resolved with the results of the query.

### query(query, compositeFilter, queryConstraints)

Creates a new immutable instance of [Query](https://firebase.google.com/docs/reference/js/firestore_.query.md#query_class) that is extended to also include additional query constraints.

**Signature:**  

    export declare function query<AppModelType, DbModelType extends DocumentData>(query: Query<AppModelType, DbModelType>, compositeFilter: QueryCompositeFilterConstraint, ...queryConstraints: QueryNonFilterConstraint[]): Query<AppModelType, DbModelType>;

#### Parameters

|    Parameter     |                                                                                 Type                                                                                  |                                                                                                                                                                                                                                                            Description                                                                                                                                                                                                                                                             |
|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| query            | [Query](https://firebase.google.com/docs/reference/js/firestore_lite.query.md#query_class)\<AppModelType, DbModelType\>                                               | The [Query](https://firebase.google.com/docs/reference/js/firestore_.query.md#query_class) instance to use as a base for the new constraints.                                                                                                                                                                                                                                                                                                                                                                                      |
| compositeFilter  | [QueryCompositeFilterConstraint](https://firebase.google.com/docs/reference/js/firestore_lite.querycompositefilterconstraint.md#querycompositefilterconstraint_class) | The [QueryCompositeFilterConstraint](https://firebase.google.com/docs/reference/js/firestore_.querycompositefilterconstraint.md#querycompositefilterconstraint_class) to apply. Create [QueryCompositeFilterConstraint](https://firebase.google.com/docs/reference/js/firestore_.querycompositefilterconstraint.md#querycompositefilterconstraint_class) using [and()](https://firebase.google.com/docs/reference/js/firestore_.md#and_e72c712) or [or()](https://firebase.google.com/docs/reference/js/firestore_.md#or_e72c712). |
| queryConstraints | [QueryNonFilterConstraint](https://firebase.google.com/docs/reference/js/firestore_lite.md#querynonfilterconstraint)\[\]                                              | Additional [QueryNonFilterConstraint](https://firebase.google.com/docs/reference/js/firestore_.md#querynonfilterconstraint)s to apply (e.g. [orderBy()](https://firebase.google.com/docs/reference/js/firestore_.md#orderby_006d61f), [limit()](https://firebase.google.com/docs/reference/js/firestore_.md#limit_ec46c78)).                                                                                                                                                                                                       |

**Returns:**

[Query](https://firebase.google.com/docs/reference/js/firestore_lite.query.md#query_class)\<AppModelType, DbModelType\>

#### Exceptions

if any of the provided query constraints cannot be combined with the existing or new constraints.

### query(query, queryConstraints)

Creates a new immutable instance of [Query](https://firebase.google.com/docs/reference/js/firestore_.query.md#query_class) that is extended to also include additional query constraints.

**Signature:**  

    export declare function query<AppModelType, DbModelType extends DocumentData>(query: Query<AppModelType, DbModelType>, ...queryConstraints: QueryConstraint[]): Query<AppModelType, DbModelType>;

#### Parameters

|    Parameter     |                                                             Type                                                             |                                                                  Description                                                                  |
|------------------|------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| query            | [Query](https://firebase.google.com/docs/reference/js/firestore_lite.query.md#query_class)\<AppModelType, DbModelType\>      | The [Query](https://firebase.google.com/docs/reference/js/firestore_.query.md#query_class) instance to use as a base for the new constraints. |
| queryConstraints | [QueryConstraint](https://firebase.google.com/docs/reference/js/firestore_lite.queryconstraint.md#queryconstraint_class)\[\] | The list of [QueryConstraint](https://firebase.google.com/docs/reference/js/firestore_.queryconstraint.md#queryconstraint_class)s to apply.   |

**Returns:**

[Query](https://firebase.google.com/docs/reference/js/firestore_lite.query.md#query_class)\<AppModelType, DbModelType\>

#### Exceptions

if any of the provided query constraints cannot be combined with the existing or new constraints.

## function(queryConstraints, ...)

### and(queryConstraints)

Creates a new [QueryCompositeFilterConstraint](https://firebase.google.com/docs/reference/js/firestore_.querycompositefilterconstraint.md#querycompositefilterconstraint_class) that is a conjunction of the given filter constraints. A conjunction filter includes a document if it satisfies all of the given filters.

**Signature:**  

    export declare function and(...queryConstraints: QueryFilterConstraint[]): QueryCompositeFilterConstraint;

#### Parameters

|    Parameter     |                                                        Type                                                        |                                                                                                                                                                                                                          Description                                                                                                                                                                                                                           |
|------------------|--------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| queryConstraints | [QueryFilterConstraint](https://firebase.google.com/docs/reference/js/firestore_lite.md#queryfilterconstraint)\[\] | Optional. The list of [QueryFilterConstraint](https://firebase.google.com/docs/reference/js/firestore_.md#queryfilterconstraint)s to perform a conjunction for. These must be created with calls to [where()](https://firebase.google.com/docs/reference/js/firestore_.md#where_0fae4bf), [or()](https://firebase.google.com/docs/reference/js/firestore_.md#or_e72c712), or [and()](https://firebase.google.com/docs/reference/js/firestore_.md#and_e72c712). |

**Returns:**

[QueryCompositeFilterConstraint](https://firebase.google.com/docs/reference/js/firestore_lite.querycompositefilterconstraint.md#querycompositefilterconstraint_class)

The newly created [QueryCompositeFilterConstraint](https://firebase.google.com/docs/reference/js/firestore_.querycompositefilterconstraint.md#querycompositefilterconstraint_class).

### or(queryConstraints)

Creates a new [QueryCompositeFilterConstraint](https://firebase.google.com/docs/reference/js/firestore_.querycompositefilterconstraint.md#querycompositefilterconstraint_class) that is a disjunction of the given filter constraints. A disjunction filter includes a document if it satisfies any of the given filters.

**Signature:**  

    export declare function or(...queryConstraints: QueryFilterConstraint[]): QueryCompositeFilterConstraint;

#### Parameters

|    Parameter     |                                                        Type                                                        |                                                                                                                                                                                                                          Description                                                                                                                                                                                                                           |
|------------------|--------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| queryConstraints | [QueryFilterConstraint](https://firebase.google.com/docs/reference/js/firestore_lite.md#queryfilterconstraint)\[\] | Optional. The list of [QueryFilterConstraint](https://firebase.google.com/docs/reference/js/firestore_.md#queryfilterconstraint)s to perform a disjunction for. These must be created with calls to [where()](https://firebase.google.com/docs/reference/js/firestore_.md#where_0fae4bf), [or()](https://firebase.google.com/docs/reference/js/firestore_.md#or_e72c712), or [and()](https://firebase.google.com/docs/reference/js/firestore_.md#and_e72c712). |

**Returns:**

[QueryCompositeFilterConstraint](https://firebase.google.com/docs/reference/js/firestore_lite.querycompositefilterconstraint.md#querycompositefilterconstraint_class)

The newly created [QueryCompositeFilterConstraint](https://firebase.google.com/docs/reference/js/firestore_.querycompositefilterconstraint.md#querycompositefilterconstraint_class).

## function(reference, ...)

### addDoc(reference, data)

Add a new document to specified `CollectionReference` with the given data, assigning it a document ID automatically.

The result of this write will only be reflected in document reads that occur after the returned promise resolves. If the client is offline, the write fails. If you would like to see local modifications or buffer writes until the client is online, use the full Firestore SDK.

**Signature:**  

    export declare function addDoc<AppModelType, DbModelType extends DocumentData>(reference: CollectionReference<AppModelType, DbModelType>, data: WithFieldValue<AppModelType>): Promise<DocumentReference<AppModelType, DbModelType>>;

#### Parameters

| Parameter |                                                                               Type                                                                                |                      Description                       |
|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------|
| reference | [CollectionReference](https://firebase.google.com/docs/reference/js/firestore_lite.collectionreference.md#collectionreference_class)\<AppModelType, DbModelType\> | A reference to the collection to add this document to. |
| data      | [WithFieldValue](https://firebase.google.com/docs/reference/js/firestore_lite.md#withfieldvalue)\<AppModelType\>                                                  | An Object containing the data for the new document.    |

**Returns:**

Promise\<[DocumentReference](https://firebase.google.com/docs/reference/js/firestore_lite.documentreference.md#documentreference_class)\<AppModelType, DbModelType\>\>

A `Promise` resolved with a `DocumentReference` pointing to the newly created document after it has been written to the backend.

#### Exceptions

Error - If the provided input is not a valid Firestore document.

### collection(reference, path, pathSegments)

Gets a `CollectionReference` instance that refers to a subcollection of `reference` at the specified relative path.

**Signature:**  

    export declare function collection<AppModelType, DbModelType extends DocumentData>(reference: CollectionReference<AppModelType, DbModelType>, path: string, ...pathSegments: string[]): CollectionReference<DocumentData, DocumentData>;

#### Parameters

|  Parameter   |                                                                               Type                                                                                |                            Description                            |
|--------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------|
| reference    | [CollectionReference](https://firebase.google.com/docs/reference/js/firestore_lite.collectionreference.md#collectionreference_class)\<AppModelType, DbModelType\> | A reference to a collection.                                      |
| path         | string                                                                                                                                                            | A slash-separated path to a collection.                           |
| pathSegments | string\[\]                                                                                                                                                        | Additional path segments to apply relative to the first argument. |

**Returns:**

[CollectionReference](https://firebase.google.com/docs/reference/js/firestore_lite.collectionreference.md#collectionreference_class)\<[DocumentData](https://firebase.google.com/docs/reference/js/firestore_lite.documentdata.md#documentdata_interface), [DocumentData](https://firebase.google.com/docs/reference/js/firestore_lite.documentdata.md#documentdata_interface)\>

The `CollectionReference` instance.

#### Exceptions

If the final path has an even number of segments and does not point to a collection.

### collection(reference, path, pathSegments)

Gets a `CollectionReference` instance that refers to a subcollection of `reference` at the specified relative path.

**Signature:**  

    export declare function collection<AppModelType, DbModelType extends DocumentData>(reference: DocumentReference<AppModelType, DbModelType>, path: string, ...pathSegments: string[]): CollectionReference<DocumentData, DocumentData>;

#### Parameters

|  Parameter   |                                                                            Type                                                                             |                                  Description                                  |
|--------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------|
| reference    | [DocumentReference](https://firebase.google.com/docs/reference/js/firestore_lite.documentreference.md#documentreference_class)\<AppModelType, DbModelType\> | A reference to a Firestore document.                                          |
| path         | string                                                                                                                                                      | A slash-separated path to a collection.                                       |
| pathSegments | string\[\]                                                                                                                                                  | Additional path segments that will be applied relative to the first argument. |

**Returns:**

[CollectionReference](https://firebase.google.com/docs/reference/js/firestore_lite.collectionreference.md#collectionreference_class)\<[DocumentData](https://firebase.google.com/docs/reference/js/firestore_lite.documentdata.md#documentdata_interface), [DocumentData](https://firebase.google.com/docs/reference/js/firestore_lite.documentdata.md#documentdata_interface)\>

The `CollectionReference` instance.

#### Exceptions

If the final path has an even number of segments and does not point to a collection.

### deleteDoc(reference)

Deletes the document referred to by the specified `DocumentReference`.

The deletion will only be reflected in document reads that occur after the returned promise resolves. If the client is offline, the delete fails. If you would like to see local modifications or buffer writes until the client is online, use the full Firestore SDK.

**Signature:**  

    export declare function deleteDoc<AppModelType, DbModelType extends DocumentData>(reference: DocumentReference<AppModelType, DbModelType>): Promise<void>;

#### Parameters

| Parameter |                                                                            Type                                                                             |              Description               |
|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------|
| reference | [DocumentReference](https://firebase.google.com/docs/reference/js/firestore_lite.documentreference.md#documentreference_class)\<AppModelType, DbModelType\> | A reference to the document to delete. |

**Returns:**

Promise\<void\>

A `Promise` resolved once the document has been successfully deleted from the backend.

### doc(reference, path, pathSegments)

Gets a `DocumentReference` instance that refers to a document within `reference` at the specified relative path. If no path is specified, an automatically-generated unique ID will be used for the returned `DocumentReference`.

**Signature:**  

    export declare function doc<AppModelType, DbModelType extends DocumentData>(reference: CollectionReference<AppModelType, DbModelType>, path?: string, ...pathSegments: string[]): DocumentReference<AppModelType, DbModelType>;

#### Parameters

|  Parameter   |                                                                               Type                                                                                |                                    Description                                     |
|--------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| reference    | [CollectionReference](https://firebase.google.com/docs/reference/js/firestore_lite.collectionreference.md#collectionreference_class)\<AppModelType, DbModelType\> | A reference to a collection.                                                       |
| path         | string                                                                                                                                                            | A slash-separated path to a document. Has to be omitted to use auto-generated IDs. |
| pathSegments | string\[\]                                                                                                                                                        | Additional path segments that will be applied relative to the first argument.      |

**Returns:**

[DocumentReference](https://firebase.google.com/docs/reference/js/firestore_lite.documentreference.md#documentreference_class)\<AppModelType, DbModelType\>

The `DocumentReference` instance.

#### Exceptions

If the final path has an odd number of segments and does not point to a document.

### doc(reference, path, pathSegments)

Gets a `DocumentReference` instance that refers to a document within `reference` at the specified relative path.

**Signature:**  

    export declare function doc<AppModelType, DbModelType extends DocumentData>(reference: DocumentReference<AppModelType, DbModelType>, path: string, ...pathSegments: string[]): DocumentReference<DocumentData, DocumentData>;

#### Parameters

|  Parameter   |                                                                            Type                                                                             |                                  Description                                  |
|--------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------|
| reference    | [DocumentReference](https://firebase.google.com/docs/reference/js/firestore_lite.documentreference.md#documentreference_class)\<AppModelType, DbModelType\> | A reference to a Firestore document.                                          |
| path         | string                                                                                                                                                      | A slash-separated path to a document.                                         |
| pathSegments | string\[\]                                                                                                                                                  | Additional path segments that will be applied relative to the first argument. |

**Returns:**

[DocumentReference](https://firebase.google.com/docs/reference/js/firestore_lite.documentreference.md#documentreference_class)\<[DocumentData](https://firebase.google.com/docs/reference/js/firestore_lite.documentdata.md#documentdata_interface), [DocumentData](https://firebase.google.com/docs/reference/js/firestore_lite.documentdata.md#documentdata_interface)\>

The `DocumentReference` instance.

#### Exceptions

If the final path has an odd number of segments and does not point to a document.

### getDoc(reference)

Reads the document referred to by the specified document reference.

All documents are directly fetched from the server, even if the document was previously read or modified. Recent modifications are only reflected in the retrieved `DocumentSnapshot` if they have already been applied by the backend. If the client is offline, the read fails. If you like to use caching or see local modifications, please use the full Firestore SDK.

**Signature:**  

    export declare function getDoc<AppModelType, DbModelType extends DocumentData>(reference: DocumentReference<AppModelType, DbModelType>): Promise<DocumentSnapshot<AppModelType, DbModelType>>;

#### Parameters

| Parameter |                                                                            Type                                                                             |               Description               |
|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------|
| reference | [DocumentReference](https://firebase.google.com/docs/reference/js/firestore_lite.documentreference.md#documentreference_class)\<AppModelType, DbModelType\> | The reference of the document to fetch. |

**Returns:**

Promise\<[DocumentSnapshot](https://firebase.google.com/docs/reference/js/firestore_lite.documentsnapshot.md#documentsnapshot_class)\<AppModelType, DbModelType\>\>

A Promise resolved with a `DocumentSnapshot` containing the current document contents.

### setDoc(reference, data)

Writes to the document referred to by the specified `DocumentReference`. If the document does not yet exist, it will be created.

The result of this write will only be reflected in document reads that occur after the returned promise resolves. If the client is offline, the write fails. If you would like to see local modifications or buffer writes until the client is online, use the full Firestore SDK.

**Signature:**  

    export declare function setDoc<AppModelType, DbModelType extends DocumentData>(reference: DocumentReference<AppModelType, DbModelType>, data: WithFieldValue<AppModelType>): Promise<void>;

#### Parameters

| Parameter |                                                                            Type                                                                             |                   Description                    |
|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------|
| reference | [DocumentReference](https://firebase.google.com/docs/reference/js/firestore_lite.documentreference.md#documentreference_class)\<AppModelType, DbModelType\> | A reference to the document to write.            |
| data      | [WithFieldValue](https://firebase.google.com/docs/reference/js/firestore_lite.md#withfieldvalue)\<AppModelType\>                                            | A map of the fields and values for the document. |

**Returns:**

Promise\<void\>

A `Promise` resolved once the data has been successfully written to the backend.

#### Exceptions

Error - If the provided input is not a valid Firestore document.

### setDoc(reference, data, options)

Writes to the document referred to by the specified `DocumentReference`. If the document does not yet exist, it will be created. If you provide `merge` or `mergeFields`, the provided data can be merged into an existing document.

The result of this write will only be reflected in document reads that occur after the returned promise resolves. If the client is offline, the write fails. If you would like to see local modifications or buffer writes until the client is online, use the full Firestore SDK.

**Signature:**  

    export declare function setDoc<AppModelType, DbModelType extends DocumentData>(reference: DocumentReference<AppModelType, DbModelType>, data: PartialWithFieldValue<AppModelType>, options: SetOptions): Promise<void>;

#### Parameters

| Parameter |                                                                            Type                                                                             |                   Description                    |
|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------|
| reference | [DocumentReference](https://firebase.google.com/docs/reference/js/firestore_lite.documentreference.md#documentreference_class)\<AppModelType, DbModelType\> | A reference to the document to write.            |
| data      | [PartialWithFieldValue](https://firebase.google.com/docs/reference/js/firestore_lite.md#partialwithfieldvalue)\<AppModelType\>                              | A map of the fields and values for the document. |
| options   | [SetOptions](https://firebase.google.com/docs/reference/js/firestore_lite.md#setoptions)                                                                    | An object to configure the set behavior.         |

**Returns:**

Promise\<void\>

A `Promise` resolved once the data has been successfully written to the backend.

#### Exceptions

Error - If the provided input is not a valid Firestore document.

### updateDoc(reference, data)

Updates fields in the document referred to by the specified `DocumentReference`. The update will fail if applied to a document that does not exist.

The result of this update will only be reflected in document reads that occur after the returned promise resolves. If the client is offline, the update fails. If you would like to see local modifications or buffer writes until the client is online, use the full Firestore SDK.

**Signature:**  

    export declare function updateDoc<AppModelType, DbModelType extends DocumentData>(reference: DocumentReference<AppModelType, DbModelType>, data: UpdateData<DbModelType>): Promise<void>;

#### Parameters

| Parameter |                                                                            Type                                                                             |                                                                      Description                                                                      |
|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| reference | [DocumentReference](https://firebase.google.com/docs/reference/js/firestore_lite.documentreference.md#documentreference_class)\<AppModelType, DbModelType\> | A reference to the document to update.                                                                                                                |
| data      | [UpdateData](https://firebase.google.com/docs/reference/js/firestore_lite.md#updatedata)\<DbModelType\>                                                     | An object containing the fields and values with which to update the document. Fields can contain dots to reference nested fields within the document. |

**Returns:**

Promise\<void\>

A `Promise` resolved once the data has been successfully written to the backend.

#### Exceptions

Error - If the provided input is not valid Firestore data.

### updateDoc(reference, field, value, moreFieldsAndValues)

Updates fields in the document referred to by the specified `DocumentReference` The update will fail if applied to a document that does not exist.

Nested fields can be updated by providing dot-separated field path strings or by providing `FieldPath` objects.

The result of this update will only be reflected in document reads that occur after the returned promise resolves. If the client is offline, the update fails. If you would like to see local modifications or buffer writes until the client is online, use the full Firestore SDK.

**Signature:**  

    export declare function updateDoc<AppModelType, DbModelType extends DocumentData>(reference: DocumentReference<AppModelType, DbModelType>, field: string | FieldPath, value: unknown, ...moreFieldsAndValues: unknown[]): Promise<void>;

#### Parameters

|      Parameter      |                                                                            Type                                                                             |              Description               |
|---------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------|
| reference           | [DocumentReference](https://firebase.google.com/docs/reference/js/firestore_lite.documentreference.md#documentreference_class)\<AppModelType, DbModelType\> | A reference to the document to update. |
| field               | string \| [FieldPath](https://firebase.google.com/docs/reference/js/firestore_lite.fieldpath.md#fieldpath_class)                                            | The first field to update.             |
| value               | unknown                                                                                                                                                     | The first value.                       |
| moreFieldsAndValues | unknown\[\]                                                                                                                                                 | Additional key value pairs.            |

**Returns:**

Promise\<void\>

A `Promise` resolved once the data has been successfully written to the backend.

#### Exceptions

Error - If the provided input is not valid Firestore data.

## function(snapshot, ...)

### endAt(snapshot)

Creates a [QueryEndAtConstraint](https://firebase.google.com/docs/reference/js/firestore_.queryendatconstraint.md#queryendatconstraint_class) that modifies the result set to end at the provided document (inclusive). The end position is relative to the order of the query. The document must contain all of the fields provided in the orderBy of the query.

**Signature:**  

    export declare function endAt<AppModelType, DbModelType extends DocumentData>(snapshot: DocumentSnapshot<AppModelType, DbModelType>): QueryEndAtConstraint;

#### Parameters

| Parameter |                                                                           Type                                                                           |               Description               |
|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------|
| snapshot  | [DocumentSnapshot](https://firebase.google.com/docs/reference/js/firestore_lite.documentsnapshot.md#documentsnapshot_class)\<AppModelType, DbModelType\> | The snapshot of the document to end at. |

**Returns:**

[QueryEndAtConstraint](https://firebase.google.com/docs/reference/js/firestore_lite.queryendatconstraint.md#queryendatconstraint_class)

A [QueryEndAtConstraint](https://firebase.google.com/docs/reference/js/firestore_.queryendatconstraint.md#queryendatconstraint_class) to pass to `query()`

### endBefore(snapshot)

Creates a [QueryEndAtConstraint](https://firebase.google.com/docs/reference/js/firestore_.queryendatconstraint.md#queryendatconstraint_class) that modifies the result set to end before the provided document (exclusive). The end position is relative to the order of the query. The document must contain all of the fields provided in the orderBy of the query.

**Signature:**  

    export declare function endBefore<AppModelType, DbModelType extends DocumentData>(snapshot: DocumentSnapshot<AppModelType, DbModelType>): QueryEndAtConstraint;

#### Parameters

| Parameter |                                                                           Type                                                                           |                 Description                 |
|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------|
| snapshot  | [DocumentSnapshot](https://firebase.google.com/docs/reference/js/firestore_lite.documentsnapshot.md#documentsnapshot_class)\<AppModelType, DbModelType\> | The snapshot of the document to end before. |

**Returns:**

[QueryEndAtConstraint](https://firebase.google.com/docs/reference/js/firestore_lite.queryendatconstraint.md#queryendatconstraint_class)

A [QueryEndAtConstraint](https://firebase.google.com/docs/reference/js/firestore_.queryendatconstraint.md#queryendatconstraint_class) to pass to `query()`

### startAfter(snapshot)

Creates a [QueryStartAtConstraint](https://firebase.google.com/docs/reference/js/firestore_.querystartatconstraint.md#querystartatconstraint_class) that modifies the result set to start after the provided document (exclusive). The starting position is relative to the order of the query. The document must contain all of the fields provided in the orderBy of the query.

**Signature:**  

    export declare function startAfter<AppModelType, DbModelType extends DocumentData>(snapshot: DocumentSnapshot<AppModelType, DbModelType>): QueryStartAtConstraint;

#### Parameters

| Parameter |                                                                           Type                                                                           |                 Description                  |
|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------|
| snapshot  | [DocumentSnapshot](https://firebase.google.com/docs/reference/js/firestore_lite.documentsnapshot.md#documentsnapshot_class)\<AppModelType, DbModelType\> | The snapshot of the document to start after. |

**Returns:**

[QueryStartAtConstraint](https://firebase.google.com/docs/reference/js/firestore_lite.querystartatconstraint.md#querystartatconstraint_class)

A [QueryStartAtConstraint](https://firebase.google.com/docs/reference/js/firestore_.querystartatconstraint.md#querystartatconstraint_class) to pass to `query()`

### startAt(snapshot)

Creates a [QueryStartAtConstraint](https://firebase.google.com/docs/reference/js/firestore_.querystartatconstraint.md#querystartatconstraint_class) that modifies the result set to start at the provided document (inclusive). The starting position is relative to the order of the query. The document must contain all of the fields provided in the `orderBy` of this query.

**Signature:**  

    export declare function startAt<AppModelType, DbModelType extends DocumentData>(snapshot: DocumentSnapshot<AppModelType, DbModelType>): QueryStartAtConstraint;

#### Parameters

| Parameter |                                                                           Type                                                                           |                Description                |
|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------|
| snapshot  | [DocumentSnapshot](https://firebase.google.com/docs/reference/js/firestore_lite.documentsnapshot.md#documentsnapshot_class)\<AppModelType, DbModelType\> | The snapshot of the document to start at. |

**Returns:**

[QueryStartAtConstraint](https://firebase.google.com/docs/reference/js/firestore_lite.querystartatconstraint.md#querystartatconstraint_class)

A [QueryStartAtConstraint](https://firebase.google.com/docs/reference/js/firestore_.querystartatconstraint.md#querystartatconstraint_class) to pass to `query()`.

## function(values, ...)

### vector(values)

Creates a new `VectorValue` constructed with a copy of the given array of numbers.

**Signature:**  

    export declare function vector(values?: number[]): VectorValue;

#### Parameters

| Parameter |    Type    |                              Description                              |
|-----------|------------|-----------------------------------------------------------------------|
| values    | number\[\] | Create a `VectorValue` instance with a copy of this array of numbers. |

**Returns:**

[VectorValue](https://firebase.google.com/docs/reference/js/firestore_lite.vectorvalue.md#vectorvalue_class)

A new `VectorValue` constructed with a copy of the given array of numbers.

## AddPrefixToKeys

Returns a new map where every key is prefixed with the outer key appended to a dot.

**Signature:**  

    export declare type AddPrefixToKeys<Prefix extends string, T extends Record<string, unknown>> = {
        [K in keyof T & string as `${Prefix}.${K}`]+?: string extends K ? any : T[K];
    };

## AggregateFieldType

The union of all `AggregateField` types that are supported by Firestore.

**Signature:**  

    export declare type AggregateFieldType = ReturnType<typeof sum> | ReturnType<typeof average> | ReturnType<typeof count>;

## AggregateSpecData

A type whose keys are taken from an `AggregateSpec`, and whose values are the result of the aggregation performed by the corresponding `AggregateField` from the input `AggregateSpec`.

**Signature:**  

    export declare type AggregateSpecData<T extends AggregateSpec> = {
        [P in keyof T]: T[P] extends AggregateField<infer U> ? U : never;
    };

## AggregateType

Union type representing the aggregate type to be performed.

**Signature:**  

    export declare type AggregateType = 'count' | 'avg' | 'sum';

## ChildUpdateFields

Helper for calculating the nested fields for a given type T1. This is needed to distribute union types such as `undefined | {...}` (happens for optional props) or `{a: A} | {b: B}`.

In this use case, `V` is used to distribute the union types of `T[K]` on `Record`, since `T[K]` is evaluated as an expression and not distributed.

See https://www.typescriptlang.org/docs/handbook/advanced-types.html#distributive-conditional-types

**Signature:**  

    export declare type ChildUpdateFields<K extends string, V> = V extends Record<string, unknown> ? AddPrefixToKeys<K, UpdateData<V>> : never;

## FirestoreErrorCode

The set of Firestore status codes. The codes are the same at the ones exposed by gRPC here: https://github.com/grpc/grpc/blob/master/doc/statuscodes.md

Possible values: - 'cancelled': The operation was cancelled (typically by the caller). - 'unknown': Unknown error or an error from a different error domain. - 'invalid-argument': Client specified an invalid argument. Note that this differs from 'failed-precondition'. 'invalid-argument' indicates arguments that are problematic regardless of the state of the system (e.g. an invalid field name). - 'deadline-exceeded': Deadline expired before operation could complete. For operations that change the state of the system, this error may be returned even if the operation has completed successfully. For example, a successful response from a server could have been delayed long enough for the deadline to expire. - 'not-found': Some requested document was not found. - 'already-exists': Some document that we attempted to create already exists. - 'permission-denied': The caller does not have permission to execute the specified operation. - 'resource-exhausted': Some resource has been exhausted, perhaps a per-user quota, or perhaps the entire file system is out of space. - 'failed-precondition': Operation was rejected because the system is not in a state required for the operation's execution. - 'aborted': The operation was aborted, typically due to a concurrency issue like transaction aborts, etc. - 'out-of-range': Operation was attempted past the valid range. - 'unimplemented': Operation is not implemented or not supported/enabled. - 'internal': Internal errors. Means some invariants expected by underlying system has been broken. If you see one of these errors, something is very broken. - 'unavailable': The service is currently unavailable. This is most likely a transient condition and may be corrected by retrying with a backoff. - 'data-loss': Unrecoverable data loss or corruption. - 'unauthenticated': The request does not have valid authentication credentials for the operation.

**Signature:**  

    export declare type FirestoreErrorCode = 'cancelled' | 'unknown' | 'invalid-argument' | 'deadline-exceeded' | 'not-found' | 'already-exists' | 'permission-denied' | 'resource-exhausted' | 'failed-precondition' | 'aborted' | 'out-of-range' | 'unimplemented' | 'internal' | 'unavailable' | 'data-loss' | 'unauthenticated';

## NestedUpdateFields

For each field (e.g. 'bar'), find all nested keys (e.g. {'bar.baz': T1, 'bar.qux': T2}). Intersect them together to make a single map containing all possible keys that are all marked as optional

**Signature:**  

    export declare type NestedUpdateFields<T extends Record<string, unknown>> = UnionToIntersection<{
        [K in keyof T & string]: ChildUpdateFields<K, T[K]>;
    }[keyof T & string]>;

## OrderByDirection

The direction of a [orderBy()](https://firebase.google.com/docs/reference/js/firestore_.md#orderby_006d61f) clause is specified as 'desc' or 'asc' (descending or ascending).

**Signature:**  

    export declare type OrderByDirection = 'desc' | 'asc';

## PartialWithFieldValue

Similar to TypeScript's `Partial<T>`, but allows nested fields to be omitted and FieldValues to be passed in as property values.

**Signature:**  

    export declare type PartialWithFieldValue<T> = Partial<T> | (T extends Primitive ? T : T extends {} ? {
        [K in keyof T]?: PartialWithFieldValue<T[K]> | FieldValue;
    } : never);

## Primitive

Primitive types.

**Signature:**  

    export declare type Primitive = string | number | boolean | undefined | null;

## QueryConstraintType

Describes the different query constraints available in this SDK.

**Signature:**  

    export declare type QueryConstraintType = 'where' | 'orderBy' | 'limit' | 'limitToLast' | 'startAt' | 'startAfter' | 'endAt' | 'endBefore';

## QueryFilterConstraint

`QueryFilterConstraint` is a helper union type that represents [QueryFieldFilterConstraint](https://firebase.google.com/docs/reference/js/firestore_.queryfieldfilterconstraint.md#queryfieldfilterconstraint_class) and [QueryCompositeFilterConstraint](https://firebase.google.com/docs/reference/js/firestore_.querycompositefilterconstraint.md#querycompositefilterconstraint_class).

**Signature:**  

    export declare type QueryFilterConstraint = QueryFieldFilterConstraint | QueryCompositeFilterConstraint;

## QueryNonFilterConstraint

`QueryNonFilterConstraint` is a helper union type that represents QueryConstraints which are used to narrow or order the set of documents, but that do not explicitly filter on a document field. `QueryNonFilterConstraint`s are created by invoking [orderBy()](https://firebase.google.com/docs/reference/js/firestore_.md#orderby_006d61f), [startAt()](https://firebase.google.com/docs/reference/js/firestore_.md#startat_9a4477f), [startAfter()](https://firebase.google.com/docs/reference/js/firestore_.md#startafter_9a4477f), [endBefore()](https://firebase.google.com/docs/reference/js/firestore_.md#endbefore_9a4477f), [endAt()](https://firebase.google.com/docs/reference/js/firestore_.md#endat_9a4477f), [limit()](https://firebase.google.com/docs/reference/js/firestore_.md#limit_ec46c78) or [limitToLast()](https://firebase.google.com/docs/reference/js/firestore_.md#limittolast_ec46c78) and can then be passed to [query()](https://firebase.google.com/docs/reference/js/firestore_.md#query_9f7b0f4) to create a new query instance that also contains the `QueryConstraint`.

**Signature:**  

    export declare type QueryNonFilterConstraint = QueryOrderByConstraint | QueryLimitConstraint | QueryStartAtConstraint | QueryEndAtConstraint;

## SetOptions

An options object that configures the behavior of [setDoc()](https://firebase.google.com/docs/reference/js/firestore_lite.md#setdoc_ee215ad), and calls. These calls can be configured to perform granular merges instead of overwriting the target documents in their entirety by providing a `SetOptions` with `merge: true`.

**Signature:**  

    export declare type SetOptions = {
        readonly merge?: boolean;
    } | {
        readonly mergeFields?: Array<string | FieldPath>;
    };

## UnionToIntersection

Given a union type `U = T1 | T2 | ...`, returns an intersected type `(T1 & T2 & ...)`.

Uses distributive conditional types and inference from conditional types. This works because multiple candidates for the same type variable in contra-variant positions causes an intersection type to be inferred. https://www.typescriptlang.org/docs/handbook/advanced-types.html#type-inference-in-conditional-types https://stackoverflow.com/questions/50374908/transform-union-type-to-intersection-type

**Signature:**  

    export declare type UnionToIntersection<U> = (U extends unknown ? (k: U) => void : never) extends (k: infer I) => void ? I : never;

## UpdateData

Update data (for use with [updateDoc()](https://firebase.google.com/docs/reference/js/firestore_.md#updatedoc_51a65e3)) that consists of field paths (e.g. 'foo' or 'foo.baz') mapped to values. Fields that contain dots reference nested fields within the document. FieldValues can be passed in as property values.

**Signature:**  

    export declare type UpdateData<T> = T extends Primitive ? T : T extends {} ? {
        [K in keyof T]?: UpdateData<T[K]> | FieldValue;
    } & NestedUpdateFields<T> : Partial<T>;

## WhereFilterOp

Filter conditions in a [where()](https://firebase.google.com/docs/reference/js/firestore_.md#where_0fae4bf) clause are specified using the strings '\&lt;', '\&lt;=', '==', '!=', '\&gt;=', '\&gt;', 'array-contains', 'in', 'array-contains-any', and 'not-in'.

**Signature:**  

    export declare type WhereFilterOp = '<' | '<=' | '==' | '!=' | '>=' | '>' | 'array-contains' | 'in' | 'array-contains-any' | 'not-in';

## WithFieldValue

Allows FieldValues to be passed in as a property value while maintaining type safety.

**Signature:**  

    export declare type WithFieldValue<T> = T | (T extends Primitive ? T : T extends {} ? {
        [K in keyof T]: WithFieldValue<T[K]> | FieldValue;
    } : never);