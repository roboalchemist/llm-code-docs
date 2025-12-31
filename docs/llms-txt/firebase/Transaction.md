# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/Transaction.md.txt

# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/database/Transaction.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Transaction.md.txt

# Source: https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/Transaction.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebasefirestoreswift/api/reference/Extensions/Transaction.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/Transaction.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Transaction.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebasefirestoreswift/api/reference/Extensions/Transaction.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/Transaction.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Transaction.md.txt

# Transaction

# Transaction


```
class Transaction
```

<br />

*** ** * ** ***

A `Transaction` is passed to a Function to provide the methods to read and write data within the transaction context.

**Subclassing Note**: Cloud Firestore classes are not meant to be subclassed except for use in test mocks. Subclassing is not supported in production code and new SDK releases may break code that does so.  

|                                                                                            See also                                                                                             |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---|
| [runTransaction](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestore#runTransaction(com.google.firebase.firestore.Transaction.Function<TResult>)) |   |

## Summary

|                                                                                                         ### Nested types                                                                                                         |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `interface `[Transaction.Function](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Transaction.Function)`<TResult>` An interface for providing code to be executed within a transaction context. |

|                                                 ### Public functions                                                 |
|----------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Transaction](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Transaction)           | [delete](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Transaction#delete(com.google.firebase.firestore.DocumentReference))`(documentRef: `[DocumentReference](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentReference)`)` Deletes the document referred to by the provided `DocumentReference`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [DocumentSnapshot](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot) | [get](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Transaction#get(com.google.firebase.firestore.DocumentReference))`(documentRef: `[DocumentReference](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentReference)`)` Reads the document referenced by this `DocumentReference`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [Transaction](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Transaction)           | [set](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Transaction#set(com.google.firebase.firestore.DocumentReference,java.lang.Object))`(documentRef: `[DocumentReference](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentReference)`, data: `[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)`)` Overwrites the document referred to by the provided `DocumentReference`.                                                                                                                                                                                                                                                                                                                                                                                                        |
| [Transaction](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Transaction)           | [set](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Transaction#set(com.google.firebase.firestore.DocumentReference,java.lang.Object,com.google.firebase.firestore.SetOptions))`(documentRef: `[DocumentReference](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentReference)`, data: `[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)`, options: `[SetOptions](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/SetOptions)`)` Writes to the document referred to by the provided DocumentReference.                                                                                                                                                                                                                                             |
| [Transaction](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Transaction)           | [update](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Transaction#update(com.google.firebase.firestore.DocumentReference,java.util.Map<java.lang.String,java.lang.Object>))`(documentRef: `[DocumentReference](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentReference)`, data: (`[Mutable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-map/index.html)`)`[Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html)`<`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!, `[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)`!>)` Updates fields in the document referred to by the provided `DocumentReference`.                                                                     |
| [Transaction](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Transaction)           | [update](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Transaction#update(com.google.firebase.firestore.DocumentReference,java.lang.String,java.lang.Object,java.lang.Object...))`(` ` documentRef: `[DocumentReference](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentReference)`,` ` field: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`,` ` value: `[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)`?,` ` moreFieldsAndValues: `[Array](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html)`<`[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)`!>!` `)` Updates fields in the document referred to by the provided `DocumentReference`.                                                  |
| [Transaction](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Transaction)           | [update](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Transaction#update(com.google.firebase.firestore.DocumentReference,com.google.firebase.firestore.FieldPath,java.lang.Object,java.lang.Object...))`(` ` documentRef: `[DocumentReference](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentReference)`,` ` fieldPath: `[FieldPath](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FieldPath)`,` ` value: `[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)`?,` ` moreFieldsAndValues: `[Array](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html)`<`[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)`!>!` `)` Updates fields in the document referred to by the provided `DocumentReference`. |

## Public functions

### delete

```
funÂ delete(documentRef:Â DocumentReference):Â Transaction
```

Deletes the document referred to by the provided `DocumentReference`.  

|                                                              Parameters                                                               |
|---------------------------------------------------------------------------------------------------------------------------------------|------------------------------------|
| `documentRef: `[DocumentReference](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentReference) | The `DocumentReference` to delete. |

|                                                  Returns                                                   |
|------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------|
| [Transaction](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Transaction) | This `Transaction` instance. Used for chaining method calls. |

### get

```
funÂ get(documentRef:Â DocumentReference):Â DocumentSnapshot
```

Reads the document referenced by this `DocumentReference`  

|                                                              Parameters                                                               |
|---------------------------------------------------------------------------------------------------------------------------------------|----------------------------------|
| `documentRef: `[DocumentReference](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentReference) | The `DocumentReference` to read. |

|                                                       Returns                                                        |
|----------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------|
| [DocumentSnapshot](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot) | The contents of the Document at this `DocumentReference`. |

|                                                                                                               Throws                                                                                                               |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---|
| `com.google.firebase.firestore.FirebaseFirestoreException: `[com.google.firebase.firestore.FirebaseFirestoreException](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestoreException) |   |

### set

```
funÂ set(documentRef:Â DocumentReference,Â data:Â Any):Â Transaction
```

Overwrites the document referred to by the provided `DocumentReference`. If the document does not yet exist, it will be created. If a document already exists, it will be overwritten.  

|                                                              Parameters                                                               |
|---------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------|
| `documentRef: `[DocumentReference](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentReference) | The `DocumentReference` to overwrite.                                                              |
| `data: `[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)                                                    | The data to write to the document (like a Map or a POJO containing the desired document contents). |

|                                                  Returns                                                   |
|------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------|
| [Transaction](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Transaction) | This `Transaction` instance. Used for chaining method calls. |

### set

```
funÂ set(documentRef:Â DocumentReference,Â data:Â Any,Â options:Â SetOptions):Â Transaction
```

Writes to the document referred to by the provided DocumentReference. If the document does not yet exist, it will be created. If you pass `SetOptions`, the provided data can be merged into an existing document.  

|                                                              Parameters                                                               |
|---------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------|
| `documentRef: `[DocumentReference](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentReference) | The `DocumentReference` to overwrite.                                                              |
| `data: `[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)                                                    | The data to write to the document (like a Map or a POJO containing the desired document contents). |
| `options: `[SetOptions](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/SetOptions)                   | An object to configure the set behavior.                                                           |

|                                                  Returns                                                   |
|------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------|
| [Transaction](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Transaction) | This `Transaction` instance. Used for chaining method calls. |

### update

```
funÂ update(documentRef:Â DocumentReference,Â data:Â (Mutable)Map<String!,Â Any!>):Â Transaction
```

Updates fields in the document referred to by the provided `DocumentReference`. If no document exists yet, the update will fail.  

|                                                                                                                                                                                 Parameters                                                                                                                                                                                 |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|
| `documentRef: `[DocumentReference](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentReference)                                                                                                                                                                                                                                      | The `DocumentReference` to update.                                                                              |
| `data: (`[Mutable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-map/index.html)`)`[Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html)`<`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!, `[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)`!>` | A map of field / value pairs to update. Fields can contain dots to reference nested fields within the document. |

|                                                  Returns                                                   |
|------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------|
| [Transaction](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Transaction) | This `Transaction` instance. Used for chaining method calls. |

### update

```
funÂ update(
Â Â Â Â documentRef:Â DocumentReference,
Â Â Â Â field:Â String,
Â Â Â Â value:Â Any?,
Â Â Â Â moreFieldsAndValues:Â Array<Any!>!
):Â Transaction
```

Updates fields in the document referred to by the provided `DocumentReference`. If no document exists yet, the update will fail.  

|                                                                                       Parameters                                                                                        |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|
| `documentRef: `[DocumentReference](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentReference)                                                   | The `DocumentReference` to update.                                                                  |
| `field: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)                                                                                               | The first field to update. Fields can contain dots to reference a nested field within the document. |
| `value: `[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)`?`                                                                                                  | The first value                                                                                     |
| `moreFieldsAndValues: `[Array](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html)`<`[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)`!>!` | Additional field/value pairs.                                                                       |

|                                                  Returns                                                   |
|------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------|
| [Transaction](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Transaction) | This `Transaction` instance. Used for chaining method calls. |

### update

```
funÂ update(
Â Â Â Â documentRef:Â DocumentReference,
Â Â Â Â fieldPath:Â FieldPath,
Â Â Â Â value:Â Any?,
Â Â Â Â moreFieldsAndValues:Â Array<Any!>!
):Â Transaction
```

Updates fields in the document referred to by the provided `DocumentReference`. If no document exists yet, the update will fail.  

|                                                                                       Parameters                                                                                        |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------|
| `documentRef: `[DocumentReference](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentReference)                                                   | The `DocumentReference` to update. |
| `fieldPath: `[FieldPath](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FieldPath)                                                                     | The first field to update.         |
| `value: `[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)`?`                                                                                                  | The first value                    |
| `moreFieldsAndValues: `[Array](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html)`<`[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)`!>!` | Additional field/value pairs.      |

|                                                  Returns                                                   |
|------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------|
| [Transaction](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Transaction) | This `Transaction` instance. Used for chaining method calls. |