# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/QuerySnapshot.md.txt

# QuerySnapshot

# QuerySnapshot


```
class QuerySnapshot : Iterable
```

<br />

*** ** * ** ***

A `QuerySnapshot` contains the results of a query. It can contain zero or more `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot` objects.

**Subclassing Note**: Cloud Firestore classes are not meant to be subclassed except for use in test mocks. Subclassing is not supported in production code and new SDK releases may break code that does so.

## Summary

| ### Public functions |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/QuerySnapshot#equals(java.lang.Object)(obj: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?)` |
| `(https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-list/index.html)https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentChange!>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/QuerySnapshot#getDocumentChanges()()` Returns the list of documents that changed since the last snapshot. |
| `(https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-list/index.html)https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentChange!>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/QuerySnapshot#getDocumentChanges(com.google.firebase.firestore.MetadataChanges)(metadataChanges: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/MetadataChanges)` Returns the list of documents that changed since the last snapshot. |
| `(https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-list/index.html)https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot!>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/QuerySnapshot#getDocuments()()` Returns the documents in this `QuerySnapshot` as a List in order of the query. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/QuerySnapshot#getQuery()()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/QuerySnapshot#hashCode()()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/QuerySnapshot#isEmpty()()` Returns true if there are no documents in the `QuerySnapshot`. |
| `(https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-iterator/index.html)https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-iterator/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/QueryDocumentSnapshot!>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/QuerySnapshot#iterator()()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/QuerySnapshot#size()()` Returns the number of documents in the `QuerySnapshot`. |
| `(https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-list/index.html)https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<T!>` | `<T> https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/QuerySnapshot#toObjects(java.lang.Class<T>)(clazz: https://developer.android.com/reference/kotlin/java/lang/Class.html<T!>)` Returns the contents of the documents in the `QuerySnapshot`, converted to the provided class, as a list. |
| `(https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-list/index.html)https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<T!>` | `<T> https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/QuerySnapshot#toObjects(java.lang.Class<T>,com.google.firebase.firestore.DocumentSnapshot.ServerTimestampBehavior)( clazz: https://developer.android.com/reference/kotlin/java/lang/Class.html<T!>, serverTimestampBehavior: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot.ServerTimestampBehavior )` Returns the contents of the documents in the `QuerySnapshot`, converted to the provided class, as a list. |

| ### Public properties |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/SnapshotMetadata!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/QuerySnapshot#metadata()` |

| ### Extension functions |
|---|---|
| `inline https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<T>` | `<T : https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html> https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/QuerySnapshot.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/QuerySnapshot#(com.google.firebase.firestore.QuerySnapshot).toObjects()()` Returns the contents of the documents in the QuerySnapshot, converted to the provided class, as a list. |
| `inline https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<T>` | `<T : https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html> https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/QuerySnapshot.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/QuerySnapshot#(com.google.firebase.firestore.QuerySnapshot).toObjects(com.google.firebase.firestore.DocumentSnapshot.ServerTimestampBehavior)( serverTimestampBehavior: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot.ServerTimestampBehavior )` Returns the contents of the documents in the QuerySnapshot, converted to the provided class, as a list. |

| ### Inherited functions |
|---|
| From [java.lang.Iterable](https://developer.android.com/reference/kotlin/java/lang/Iterable.html) |---|---| | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-iterable/for-each.html(action: https://developer.android.com/reference/kotlin/java/util/function/Consumer.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html!>!)` | | `https://developer.android.com/reference/kotlin/java/util/Spliterator.html<T!>!` | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-iterable/spliterator.html()` | |

## Public functions

### equals

```
fun equals(obj: Any?): Boolean
```

### getDocumentChanges

```
fun getDocumentChanges(): (Mutable)List<DocumentChange!>
```

Returns the list of documents that changed since the last snapshot. If it's the first snapshot all documents will be in the list as added changes.

Documents with changes only to their metadata will not be included.

| Returns |
|---|---|
| `(https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-list/index.html)https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentChange!>` | The list of document changes since the last snapshot. |

### getDocumentChanges

```
fun getDocumentChanges(metadataChanges: MetadataChanges): (Mutable)List<DocumentChange!>
```

Returns the list of documents that changed since the last snapshot. If it's the first snapshot all documents will be in the list as added changes.

| Parameters |
|---|---|
| `metadataChanges: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/MetadataChanges` | Indicates whether metadata-only changes (specifically, only ` DocumentSnapshot.getMetadata()` changed) should be included. |

| Returns |
|---|---|
| `(https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-list/index.html)https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentChange!>` | The list of document changes since the last snapshot. |

### getDocuments

```
fun getDocuments(): (Mutable)List<DocumentSnapshot!>
```

Returns the documents in this `QuerySnapshot` as a List in order of the query.

| Returns |
|---|---|
| `(https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-list/index.html)https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot!>` | The list of documents. |

### getQuery

```
fun getQuery(): Query
```

### hashCode

```
fun hashCode(): Int
```

### isEmpty

```
fun isEmpty(): Boolean
```

Returns true if there are no documents in the `QuerySnapshot`.

### iterator

```
fun iterator(): (Mutable)Iterator<QueryDocumentSnapshot!>
```

### size

```
fun size(): Int
```

Returns the number of documents in the `QuerySnapshot`.

### toObjects

```
fun <T> toObjects(clazz: Class<T!>): (Mutable)List<T!>
```

Returns the contents of the documents in the `QuerySnapshot`, converted to the provided class, as a list.

| Parameters |
|---|---|
| `clazz: https://developer.android.com/reference/kotlin/java/lang/Class.html<T!>` | The POJO type used to convert the documents in the list. |

### toObjects

```
fun <T> toObjects(
    clazz: Class<T!>,
    serverTimestampBehavior: DocumentSnapshot.ServerTimestampBehavior
): (Mutable)List<T!>
```

Returns the contents of the documents in the `QuerySnapshot`, converted to the provided class, as a list.

| Parameters |
|---|---|
| `clazz: https://developer.android.com/reference/kotlin/java/lang/Class.html<T!>` | The POJO type used to convert the documents in the list. |
| `serverTimestampBehavior: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot.ServerTimestampBehavior` | Configures the behavior for server timestamps that have not yet been set to their final value. |

## Public properties

### metadata

```
val metadata: SnapshotMetadata!
```

## Extension functions

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