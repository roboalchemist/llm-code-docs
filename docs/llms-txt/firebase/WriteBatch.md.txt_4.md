# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/WriteBatch.md.txt

# WriteBatch

# WriteBatch


```
class WriteBatch
```

<br />

*** ** * ** ***

A write batch, used to perform multiple writes as a single atomic unit.

A Batch object can be acquired by calling `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestore#batch()`. It provides methods for adding writes to the write batch. None of the writes will be committed (or visible locally) until `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/WriteBatch#commit()` is called.

Unlike transactions, write batches are persisted offline and therefore are preferable when you don't need to condition your writes on read data.

**Subclassing Note**: Cloud Firestore classes are not meant to be subclassed except for use in test mocks. Subclassing is not supported in production code and new SDK releases may break code that does so.

## Summary

| ### Nested types |
|---|
| `interface https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/WriteBatch.Function` An interface for providing code to be executed within a `WriteBatch` context. |

| ### Public functions |
|---|---|
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/kotlin/java/lang/Void.html!>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/WriteBatch#commit()()` Commits all of the writes in this write batch as a single atomic unit. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/WriteBatch` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/WriteBatch#delete(com.google.firebase.firestore.DocumentReference)(documentRef: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentReference)` Deletes the document referred to by the provided `DocumentReference`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/WriteBatch` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/WriteBatch#set(com.google.firebase.firestore.DocumentReference,java.lang.Object)(documentRef: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentReference, data: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)` Overwrites the document referred to by the provided `DocumentReference`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/WriteBatch` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/WriteBatch#set(com.google.firebase.firestore.DocumentReference,java.lang.Object,com.google.firebase.firestore.SetOptions)(documentRef: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentReference, data: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html, options: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/SetOptions)` Writes to the document referred to by the provided `DocumentReference`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/WriteBatch` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/WriteBatch#update(com.google.firebase.firestore.DocumentReference,java.util.Map<java.lang.String,java.lang.Object>)(documentRef: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentReference, data: (https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-map/index.html)https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!, https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html!>)` Updates fields in the document referred to by the provided `DocumentReference`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/WriteBatch` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/WriteBatch#update(com.google.firebase.firestore.DocumentReference,java.lang.String,java.lang.Object,java.lang.Object...)( documentRef: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentReference, field: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?, moreFieldsAndValues: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html!>! )` Updates field in the document referred to by the provided `DocumentReference`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/WriteBatch` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/WriteBatch#update(com.google.firebase.firestore.DocumentReference,com.google.firebase.firestore.FieldPath,java.lang.Object,java.lang.Object...)( documentRef: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentReference, fieldPath: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FieldPath, value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?, moreFieldsAndValues: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html!>! )` Updates fields in the document referred to by the provided `DocumentReference`. |

## Public functions

### commit

```
fun commit(): Task<Void!>
```

Commits all of the writes in this write batch as a single atomic unit.

| Returns |
|---|---|
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/kotlin/java/lang/Void.html!>` | A Task that will be resolved when the write finishes. |

### delete

```
fun delete(documentRef: DocumentReference): WriteBatch
```

Deletes the document referred to by the provided `DocumentReference`.

| Parameters |
|---|---|
| `documentRef: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentReference` | The `DocumentReference` to delete. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/WriteBatch` | This `WriteBatch` instance. Used for chaining method calls. |

### set

```
fun set(documentRef: DocumentReference, data: Any): WriteBatch
```

Overwrites the document referred to by the provided `DocumentReference`. If the document does not yet exist, it will be created. If a document already exists, it will be overwritten.

| Parameters |
|---|---|
| `documentRef: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentReference` | The `DocumentReference` to overwrite. |
| `data: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html` | The data to write to the document (like a Map or a POJO containing the desired document contents). |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/WriteBatch` | This `WriteBatch` instance. Used for chaining method calls. |

### set

```
fun set(documentRef: DocumentReference, data: Any, options: SetOptions): WriteBatch
```

Writes to the document referred to by the provided `DocumentReference`. If the document does not yet exist, it will be created. If you pass `SetOptions`, the provided data can be merged into an existing document.

| Parameters |
|---|---|
| `documentRef: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentReference` | The `DocumentReference` to overwrite. |
| `data: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html` | The data to write to the document (like a Map or a POJO containing the desired document contents). |
| `options: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/SetOptions` | An object to configure the set behavior. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/WriteBatch` | This `WriteBatch` instance. Used for chaining method calls. |

### update

```
fun update(documentRef: DocumentReference, data: (Mutable)Map<String!, Any!>): WriteBatch
```

Updates fields in the document referred to by the provided `DocumentReference`. If no document exists yet, the update will fail.

| Parameters |
|---|---|
| `documentRef: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentReference` | The `DocumentReference` to update. |
| `data: (https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-map/index.html)https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!, https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html!>` | A map of field / value pairs to update. Fields can contain dots to reference nested fields within the document. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/WriteBatch` | This `WriteBatch` instance. Used for chaining method calls. |

### update

```
fun update(
    documentRef: DocumentReference,
    field: String,
    value: Any?,
    moreFieldsAndValues: Array<Any!>!
): WriteBatch
```

Updates field in the document referred to by the provided `DocumentReference`. If no document exists yet, the update will fail.

| Parameters |
|---|---|
| `documentRef: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentReference` | The `DocumentReference` to update. |
| `field: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The first field to update. Fields can contain dots to reference a nested field within the document. |
| `value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?` | The first value |
| `moreFieldsAndValues: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html!>!` | Additional field/value pairs. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/WriteBatch` | This `WriteBatch` instance. Used for chaining method calls. |

### update

```
fun update(
    documentRef: DocumentReference,
    fieldPath: FieldPath,
    value: Any?,
    moreFieldsAndValues: Array<Any!>!
): WriteBatch
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
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/WriteBatch` | This `WriteBatch` instance. Used for chaining method calls. |