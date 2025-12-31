# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/WriteBatch.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebasefirestoreswift/api/reference/Extensions/WriteBatch.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/WriteBatch.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/WriteBatch.md.txt

# WriteBatch

# WriteBatch


```
class WriteBatch
```

<br />

*** ** * ** ***

A write batch, used to perform multiple writes as a single atomic unit.

A Batch object can be acquired by calling [batch](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestore#batch()). It provides methods for adding writes to the write batch. None of the writes will be committed (or visible locally) until [commit](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/WriteBatch#commit()) is called.

Unlike transactions, write batches are persisted offline and therefore are preferable when you don't need to condition your writes on read data.

**Subclassing Note**: Cloud Firestore classes are not meant to be subclassed except for use in test mocks. Subclassing is not supported in production code and new SDK releases may break code that does so.

## Summary

|                                                                                                   ### Nested types                                                                                                   |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `interface `[WriteBatch.Function](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/WriteBatch.Function) An interface for providing code to be executed within a `WriteBatch` context. |

|                                                                              ### Public functions                                                                               |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)`<`[Void](https://developer.android.com/reference/kotlin/java/lang/Void.html)`!>` | [commit](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/WriteBatch#commit())`()` Commits all of the writes in this write batch as a single atomic unit.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [WriteBatch](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/WriteBatch)                                                                        | [delete](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/WriteBatch#delete(com.google.firebase.firestore.DocumentReference))`(documentRef: `[DocumentReference](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentReference)`)` Deletes the document referred to by the provided `DocumentReference`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [WriteBatch](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/WriteBatch)                                                                        | [set](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/WriteBatch#set(com.google.firebase.firestore.DocumentReference,java.lang.Object))`(documentRef: `[DocumentReference](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentReference)`, data: `[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)`)` Overwrites the document referred to by the provided `DocumentReference`.                                                                                                                                                                                                                                                                                                                                                                                                        |
| [WriteBatch](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/WriteBatch)                                                                        | [set](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/WriteBatch#set(com.google.firebase.firestore.DocumentReference,java.lang.Object,com.google.firebase.firestore.SetOptions))`(documentRef: `[DocumentReference](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentReference)`, data: `[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)`, options: `[SetOptions](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/SetOptions)`)` Writes to the document referred to by the provided `DocumentReference`.                                                                                                                                                                                                                                           |
| [WriteBatch](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/WriteBatch)                                                                        | [update](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/WriteBatch#update(com.google.firebase.firestore.DocumentReference,java.util.Map<java.lang.String,java.lang.Object>))`(documentRef: `[DocumentReference](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentReference)`, data: (`[Mutable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-map/index.html)`)`[Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html)`<`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!, `[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)`!>)` Updates fields in the document referred to by the provided `DocumentReference`.                                                                     |
| [WriteBatch](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/WriteBatch)                                                                        | [update](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/WriteBatch#update(com.google.firebase.firestore.DocumentReference,java.lang.String,java.lang.Object,java.lang.Object...))`(` ` documentRef: `[DocumentReference](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentReference)`,` ` field: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`,` ` value: `[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)`?,` ` moreFieldsAndValues: `[Array](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html)`<`[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)`!>!` `)` Updates field in the document referred to by the provided `DocumentReference`.                                                   |
| [WriteBatch](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/WriteBatch)                                                                        | [update](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/WriteBatch#update(com.google.firebase.firestore.DocumentReference,com.google.firebase.firestore.FieldPath,java.lang.Object,java.lang.Object...))`(` ` documentRef: `[DocumentReference](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentReference)`,` ` fieldPath: `[FieldPath](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FieldPath)`,` ` value: `[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)`?,` ` moreFieldsAndValues: `[Array](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html)`<`[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)`!>!` `)` Updates fields in the document referred to by the provided `DocumentReference`. |

## Public functions

### commit

```
funÂ commit():Â Task<Void!>
```

Commits all of the writes in this write batch as a single atomic unit.  

|                                                                                     Returns                                                                                     |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------|
| [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)`<`[Void](https://developer.android.com/reference/kotlin/java/lang/Void.html)`!>` | A Task that will be resolved when the write finishes. |

### delete

```
funÂ delete(documentRef:Â DocumentReference):Â WriteBatch
```

Deletes the document referred to by the provided `DocumentReference`.  

|                                                              Parameters                                                               |
|---------------------------------------------------------------------------------------------------------------------------------------|------------------------------------|
| `documentRef: `[DocumentReference](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentReference) | The `DocumentReference` to delete. |

|                                                 Returns                                                  |
|----------------------------------------------------------------------------------------------------------|-------------------------------------------------------------|
| [WriteBatch](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/WriteBatch) | This `WriteBatch` instance. Used for chaining method calls. |

### set

```
funÂ set(documentRef:Â DocumentReference,Â data:Â Any):Â WriteBatch
```

Overwrites the document referred to by the provided `DocumentReference`. If the document does not yet exist, it will be created. If a document already exists, it will be overwritten.  

|                                                              Parameters                                                               |
|---------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------|
| `documentRef: `[DocumentReference](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentReference) | The `DocumentReference` to overwrite.                                                              |
| `data: `[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)                                                    | The data to write to the document (like a Map or a POJO containing the desired document contents). |

|                                                 Returns                                                  |
|----------------------------------------------------------------------------------------------------------|-------------------------------------------------------------|
| [WriteBatch](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/WriteBatch) | This `WriteBatch` instance. Used for chaining method calls. |

### set

```
funÂ set(documentRef:Â DocumentReference,Â data:Â Any,Â options:Â SetOptions):Â WriteBatch
```

Writes to the document referred to by the provided `DocumentReference`. If the document does not yet exist, it will be created. If you pass `SetOptions`, the provided data can be merged into an existing document.  

|                                                              Parameters                                                               |
|---------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------|
| `documentRef: `[DocumentReference](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentReference) | The `DocumentReference` to overwrite.                                                              |
| `data: `[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)                                                    | The data to write to the document (like a Map or a POJO containing the desired document contents). |
| `options: `[SetOptions](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/SetOptions)                   | An object to configure the set behavior.                                                           |

|                                                 Returns                                                  |
|----------------------------------------------------------------------------------------------------------|-------------------------------------------------------------|
| [WriteBatch](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/WriteBatch) | This `WriteBatch` instance. Used for chaining method calls. |

### update

```
funÂ update(documentRef:Â DocumentReference,Â data:Â (Mutable)Map<String!,Â Any!>):Â WriteBatch
```

Updates fields in the document referred to by the provided `DocumentReference`. If no document exists yet, the update will fail.  

|                                                                                                                                                                                 Parameters                                                                                                                                                                                 |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|
| `documentRef: `[DocumentReference](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentReference)                                                                                                                                                                                                                                      | The `DocumentReference` to update.                                                                              |
| `data: (`[Mutable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-map/index.html)`)`[Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html)`<`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!, `[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)`!>` | A map of field / value pairs to update. Fields can contain dots to reference nested fields within the document. |

|                                                 Returns                                                  |
|----------------------------------------------------------------------------------------------------------|-------------------------------------------------------------|
| [WriteBatch](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/WriteBatch) | This `WriteBatch` instance. Used for chaining method calls. |

### update

```
funÂ update(
Â Â Â Â documentRef:Â DocumentReference,
Â Â Â Â field:Â String,
Â Â Â Â value:Â Any?,
Â Â Â Â moreFieldsAndValues:Â Array<Any!>!
):Â WriteBatch
```

Updates field in the document referred to by the provided `DocumentReference`. If no document exists yet, the update will fail.  

|                                                                                       Parameters                                                                                        |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|
| `documentRef: `[DocumentReference](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentReference)                                                   | The `DocumentReference` to update.                                                                  |
| `field: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)                                                                                               | The first field to update. Fields can contain dots to reference a nested field within the document. |
| `value: `[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)`?`                                                                                                  | The first value                                                                                     |
| `moreFieldsAndValues: `[Array](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html)`<`[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)`!>!` | Additional field/value pairs.                                                                       |

|                                                 Returns                                                  |
|----------------------------------------------------------------------------------------------------------|-------------------------------------------------------------|
| [WriteBatch](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/WriteBatch) | This `WriteBatch` instance. Used for chaining method calls. |

### update

```
funÂ update(
Â Â Â Â documentRef:Â DocumentReference,
Â Â Â Â fieldPath:Â FieldPath,
Â Â Â Â value:Â Any?,
Â Â Â Â moreFieldsAndValues:Â Array<Any!>!
):Â WriteBatch
```

Updates fields in the document referred to by the provided `DocumentReference`. If no document exists yet, the update will fail.  

|                                                                                       Parameters                                                                                        |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------|
| `documentRef: `[DocumentReference](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentReference)                                                   | The `DocumentReference` to update. |
| `fieldPath: `[FieldPath](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FieldPath)                                                                     | The first field to update.         |
| `value: `[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)`?`                                                                                                  | The first value                    |
| `moreFieldsAndValues: `[Array](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html)`<`[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)`!>!` | Additional field/value pairs.      |

|                                                 Returns                                                  |
|----------------------------------------------------------------------------------------------------------|-------------------------------------------------------------|
| [WriteBatch](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/WriteBatch) | This `WriteBatch` instance. Used for chaining method calls. |