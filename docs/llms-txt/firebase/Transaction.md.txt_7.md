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

| See also |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestore#runTransaction(com.google.firebase.firestore.Transaction.Function<TResult>)` |   |

## Summary

| ### Nested types |
|---|
| `interface https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Transaction.Function<TResult>` An interface for providing code to be executed within a transaction context. |

| ### Public functions |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Transaction` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Transaction#delete(com.google.firebase.firestore.DocumentReference)(documentRef: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentReference)` Deletes the document referred to by the provided `DocumentReference`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Transaction#get(com.google.firebase.firestore.DocumentReference)(documentRef: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentReference)` Reads the document referenced by this `DocumentReference` |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Transaction` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Transaction#set(com.google.firebase.firestore.DocumentReference,java.lang.Object)(documentRef: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentReference, data: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)` Overwrites the document referred to by the provided `DocumentReference`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Transaction` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Transaction#set(com.google.firebase.firestore.DocumentReference,java.lang.Object,com.google.firebase.firestore.SetOptions)(documentRef: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentReference, data: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html, options: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/SetOptions)` Writes to the document referred to by the provided DocumentReference. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Transaction` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Transaction#update(com.google.firebase.firestore.DocumentReference,java.util.Map<java.lang.String,java.lang.Object>)(documentRef: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentReference, data: (https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-map/index.html)https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!, https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html!>)` Updates fields in the document referred to by the provided `DocumentReference`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Transaction` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Transaction#update(com.google.firebase.firestore.DocumentReference,java.lang.String,java.lang.Object,java.lang.Object...)( documentRef: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentReference, field: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?, moreFieldsAndValues: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html!>! )` Updates fields in the document referred to by the provided `DocumentReference`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Transaction` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Transaction#update(com.google.firebase.firestore.DocumentReference,com.google.firebase.firestore.FieldPath,java.lang.Object,java.lang.Object...)( documentRef: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentReference, fieldPath: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FieldPath, value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?, moreFieldsAndValues: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html!>! )` Updates fields in the document referred to by the provided `DocumentReference`. |

## Public functions

### delete

```
fun delete(documentRef: DocumentReference): Transaction
```

Deletes the document referred to by the provided `DocumentReference`.

| Parameters |
|---|---|
| `documentRef: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentReference` | The `DocumentReference` to delete. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Transaction` | This `Transaction` instance. Used for chaining method calls. |

### get

```
fun get(documentRef: DocumentReference): DocumentSnapshot
```

Reads the document referenced by this `DocumentReference`

| Parameters |
|---|---|
| `documentRef: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentReference` | The `DocumentReference` to read. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot` | The contents of the Document at this `DocumentReference`. |

| Throws |
|---|---|
| `com.google.firebase.firestore.FirebaseFirestoreException: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestoreException` |   |

### set

```
fun set(documentRef: DocumentReference, data: Any): Transaction
```

Overwrites the document referred to by the provided `DocumentReference`. If the document does not yet exist, it will be created. If a document already exists, it will be overwritten.

| Parameters |
|---|---|
| `documentRef: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentReference` | The `DocumentReference` to overwrite. |
| `data: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html` | The data to write to the document (like a Map or a POJO containing the desired document contents). |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Transaction` | This `Transaction` instance. Used for chaining method calls. |

### set

```
fun set(documentRef: DocumentReference, data: Any, options: SetOptions): Transaction
```

Writes to the document referred to by the provided DocumentReference. If the document does not yet exist, it will be created. If you pass `SetOptions`, the provided data can be merged into an existing document.

| Parameters |
|---|---|
| `documentRef: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentReference` | The `DocumentReference` to overwrite. |
| `data: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html` | The data to write to the document (like a Map or a POJO containing the desired document contents). |
| `options: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/SetOptions` | An object to configure the set behavior. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Transaction` | This `Transaction` instance. Used for chaining method calls. |

### update

```
fun update(documentRef: DocumentReference, data: (Mutable)Map<String!, Any!>): Transaction
```

Updates fields in the document referred to by the provided `DocumentReference`. If no document exists yet, the update will fail.

| Parameters |
|---|---|
| `documentRef: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentReference` | The `DocumentReference` to update. |
| `data: (https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-map/index.html)https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!, https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html!>` | A map of field / value pairs to update. Fields can contain dots to reference nested fields within the document. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Transaction` | This `Transaction` instance. Used for chaining method calls. |

### update

```
fun update(
    documentRef: DocumentReference,
    field: String,
    value: Any?,
    moreFieldsAndValues: Array<Any!>!
): Transaction
```

Updates fields in the document referred to by the provided `DocumentReference`. If no document exists yet, the update will fail.

| Parameters |
|---|---|
| `documentRef: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentReference` | The `DocumentReference` to update. |
| `field: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The first field to update. Fields can contain dots to reference a nested field within the document. |
| `value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?` | The first value |
| `moreFieldsAndValues: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html!>!` | Additional field/value pairs. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Transaction` | This `Transaction` instance. Used for chaining method calls. |

### update

```
fun update(
    documentRef: DocumentReference,
    fieldPath: FieldPath,
    value: Any?,
    moreFieldsAndValues: Array<Any!>!
): Transaction
```

Updates fields in the document referred to by the provided `DocumentReference`. If no document exists yet, the update will fail.

| Parameters |
|---|---|
| `documentRef: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentReference` | The `DocumentReference` to update. |
| `fieldPath: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FieldPath` | The first field to update. |
| `value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?` | The first value |
| `moreFieldsAndValues: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html!>!` | Additional field/value pairs. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Transaction` | This `Transaction` instance. Used for chaining method calls. |