# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/QuerySnapshot.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/QuerySnapshot.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/QuerySnapshot.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/QuerySnapshot.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/QuerySnapshot.md.txt

# QuerySnapshot

# QuerySnapshot


```
class QuerySnapshot : Iterable
```

<br />

*** ** * ** ***

A `QuerySnapshot` contains the results of a query. It can contain zero or more [DocumentSnapshot](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot) objects.

**Subclassing Note**: Cloud Firestore classes are not meant to be subclassed except for use in test mocks. Subclassing is not supported in production code and new SDK releases may break code that does so.

## Summary

|                                                                                                                                                                ### Public functions                                                                                                                                                                |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)                                                                                                                                                                                                                                                                 | [equals](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/QuerySnapshot#equals(java.lang.Object))`(obj: `[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)`?)`                                                                                                                                                                                                                                                                                                                                                                                                                |
| `(`[Mutable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-list/index.html)`)`[List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)`<`[DocumentChange](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentChange)`!>`                           | [getDocumentChanges](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/QuerySnapshot#getDocumentChanges())`()` Returns the list of documents that changed since the last snapshot.                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `(`[Mutable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-list/index.html)`)`[List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)`<`[DocumentChange](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentChange)`!>`                           | [getDocumentChanges](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/QuerySnapshot#getDocumentChanges(com.google.firebase.firestore.MetadataChanges))`(metadataChanges: `[MetadataChanges](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/MetadataChanges)`)` Returns the list of documents that changed since the last snapshot.                                                                                                                                                                                                                                    |
| `(`[Mutable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-list/index.html)`)`[List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)`<`[DocumentSnapshot](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot)`!>`                       | [getDocuments](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/QuerySnapshot#getDocuments())`()` Returns the documents in this `QuerySnapshot` as a List in order of the query.                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [Query](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query)                                                                                                                                                                                                                                                     | [getQuery](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/QuerySnapshot#getQuery())`()`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)                                                                                                                                                                                                                                                                         | [hashCode](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/QuerySnapshot#hashCode())`()`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)                                                                                                                                                                                                                                                                 | [isEmpty](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/QuerySnapshot#isEmpty())`()` Returns true if there are no documents in the `QuerySnapshot`.                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `(`[Mutable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-iterator/index.html)`)`[Iterator](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-iterator/index.html)`<`[QueryDocumentSnapshot](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/QueryDocumentSnapshot)`!>` | [iterator](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/QuerySnapshot#iterator())`()`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)                                                                                                                                                                                                                                                                         | [size](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/QuerySnapshot#size())`()` Returns the number of documents in the `QuerySnapshot`.                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `(`[Mutable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-list/index.html)`)`[List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)`<T!>`                                                                                                                                            | `<T> `[toObjects](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/QuerySnapshot#toObjects(java.lang.Class<T>))`(clazz: `[Class](https://developer.android.com/reference/kotlin/java/lang/Class.html)`<T!>)` Returns the contents of the documents in the `QuerySnapshot`, converted to the provided class, as a list.                                                                                                                                                                                                                                                                                 |
| `(`[Mutable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-list/index.html)`)`[List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)`<T!>`                                                                                                                                            | `<T> `[toObjects](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/QuerySnapshot#toObjects(java.lang.Class<T>,com.google.firebase.firestore.DocumentSnapshot.ServerTimestampBehavior))`(` ` clazz: `[Class](https://developer.android.com/reference/kotlin/java/lang/Class.html)`<T!>,` ` serverTimestampBehavior: `[DocumentSnapshot.ServerTimestampBehavior](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot.ServerTimestampBehavior) `)` Returns the contents of the documents in the `QuerySnapshot`, converted to the provided class, as a list. |

|                                                  ### Public properties                                                  |
|-------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|
| [SnapshotMetadata](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/SnapshotMetadata)`!` | [metadata](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/QuerySnapshot#metadata()) |

|                                        ### Extension functions                                         |
|--------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `inline `[List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)`<T>` | `<T : `[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)`> `[QuerySnapshot](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/QuerySnapshot)`.`[toObjects](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/QuerySnapshot#(com.google.firebase.firestore.QuerySnapshot).toObjects())`()` Returns the contents of the documents in the QuerySnapshot, converted to the provided class, as a list.                                                                                                                                                                                                                                                                           |
| `inline `[List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)`<T>` | `<T : `[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)`> `[QuerySnapshot](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/QuerySnapshot)`.`[toObjects](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/QuerySnapshot#(com.google.firebase.firestore.QuerySnapshot).toObjects(com.google.firebase.firestore.DocumentSnapshot.ServerTimestampBehavior))`(` ` serverTimestampBehavior: `[DocumentSnapshot.ServerTimestampBehavior](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot.ServerTimestampBehavior) `)` Returns the contents of the documents in the QuerySnapshot, converted to the provided class, as a list. |

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         ### Inherited functions                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| From [java.lang.Iterable](https://developer.android.com/reference/kotlin/java/lang/Iterable.html) |-------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)                    | [forEach](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-iterable/for-each.html)`(action: `[Consumer](https://developer.android.com/reference/kotlin/java/util/function/Consumer.html)`<`[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)`!>!)` | | [Spliterator](https://developer.android.com/reference/kotlin/java/util/Spliterator.html)`<T!>!` | [spliterator](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-iterable/spliterator.html)`()`                                                                                                                                                                               | |

## Public functions

### equals

```
funÂ equals(obj:Â Any?):Â Boolean
```  

### getDocumentChanges

```
funÂ getDocumentChanges():Â (Mutable)List<DocumentChange!>
```

Returns the list of documents that changed since the last snapshot. If it's the first snapshot all documents will be in the list as added changes.

Documents with changes only to their metadata will not be included.  

|                                                                                                                                                         Returns                                                                                                                                                          |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------|
| `(`[Mutable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-list/index.html)`)`[List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)`<`[DocumentChange](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentChange)`!>` | The list of document changes since the last snapshot. |

### getDocumentChanges

```
funÂ getDocumentChanges(metadataChanges:Â MetadataChanges):Â (Mutable)List<DocumentChange!>
```

Returns the list of documents that changed since the last snapshot. If it's the first snapshot all documents will be in the list as added changes.  

|                                                              Parameters                                                               |
|---------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|
| `metadataChanges: `[MetadataChanges](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/MetadataChanges) | Indicates whether metadata-only changes (specifically, only ` DocumentSnapshot.getMetadata()` changed) should be included. |

|                                                                                                                                                         Returns                                                                                                                                                          |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------|
| `(`[Mutable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-list/index.html)`)`[List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)`<`[DocumentChange](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentChange)`!>` | The list of document changes since the last snapshot. |

### getDocuments

```
funÂ getDocuments():Â (Mutable)List<DocumentSnapshot!>
```

Returns the documents in this `QuerySnapshot` as a List in order of the query.  

|                                                                                                                                                           Returns                                                                                                                                                            |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------|
| `(`[Mutable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-list/index.html)`)`[List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)`<`[DocumentSnapshot](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot)`!>` | The list of documents. |

### getQuery

```
funÂ getQuery():Â Query
```  

### hashCode

```
funÂ hashCode():Â Int
```  

### isEmpty

```
funÂ isEmpty():Â Boolean
```

Returns true if there are no documents in the `QuerySnapshot`.  

### iterator

```
funÂ iterator():Â (Mutable)Iterator<QueryDocumentSnapshot!>
```  

### size

```
funÂ size():Â Int
```

Returns the number of documents in the `QuerySnapshot`.  

### toObjects

```
funÂ <T> toObjects(clazz:Â Class<T!>):Â (Mutable)List<T!>
```

Returns the contents of the documents in the `QuerySnapshot`, converted to the provided class, as a list.  

|                                         Parameters                                          |
|---------------------------------------------------------------------------------------------|----------------------------------------------------------|
| `clazz: `[Class](https://developer.android.com/reference/kotlin/java/lang/Class.html)`<T!>` | The POJO type used to convert the documents in the list. |

### toObjects

```
funÂ <T> toObjects(
Â Â Â Â clazz:Â Class<T!>,
Â Â Â Â serverTimestampBehavior:Â DocumentSnapshot.ServerTimestampBehavior
):Â (Mutable)List<T!>
```

Returns the contents of the documents in the `QuerySnapshot`, converted to the provided class, as a list.  

|                                                                                           Parameters                                                                                            |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|
| `clazz: `[Class](https://developer.android.com/reference/kotlin/java/lang/Class.html)`<T!>`                                                                                                     | The POJO type used to convert the documents in the list.                                       |
| `serverTimestampBehavior: `[DocumentSnapshot.ServerTimestampBehavior](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot.ServerTimestampBehavior) | Configures the behavior for server timestamps that have not yet been set to their final value. |

## Public properties

### metadata

```
valÂ metadata:Â SnapshotMetadata!
```  

## Extension functions

### toObjects

```
inlineÂ funÂ <TÂ :Â Any> QuerySnapshot.toObjects():Â List<T>
```

Returns the contents of the documents in the QuerySnapshot, converted to the provided class, as a list.  

|                                      Parameters                                      |
|--------------------------------------------------------------------------------------|----------------------------------------------------------|
| `<T : `[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)`>` | The POJO type used to convert the documents in the list. |

### toObjects

```
inlineÂ funÂ <TÂ :Â Any> QuerySnapshot.toObjects(
Â Â Â Â serverTimestampBehavior:Â DocumentSnapshot.ServerTimestampBehavior
):Â List<T>
```

Returns the contents of the documents in the QuerySnapshot, converted to the provided class, as a list.  

|                                                                                           Parameters                                                                                            |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| `<T : `[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)`>`                                                                                                            | The POJO type used to convert the documents in the list.                                                     |
| `serverTimestampBehavior: `[DocumentSnapshot.ServerTimestampBehavior](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot.ServerTimestampBehavior) | Configures the behavior for server timestamps that have not yet ```kotlin been set to their final value. ``` |