# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/PipelineResult.md.txt

# PipelineResult

# PipelineResult


```
@Beta
class PipelineResult
```

<br />

*** ** * ** ***

Represents the results of a Pipeline query, including the data and metadata. It is usually accessed via `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline.Snapshot`.

## Summary

| ### Public functions |
|---|---|
| `open operator https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/PipelineResult#equals(kotlin.Any)(other: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?)` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/PipelineResult#get(kotlin.String)(field: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Retrieves the field specified by `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/PipelineResult#get(kotlin.String)`. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/PipelineResult#get(com.google.firebase.firestore.FieldPath)(fieldPath: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FieldPath)` Retrieves the field specified by `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/PipelineResult#get(com.google.firebase.firestore.FieldPath)`. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/PipelineResult#getData()()` Retrieves all fields in the result as an object map. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/PipelineResult#getId()()` Returns the ID of the document represented by this result. |
| `open https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/PipelineResult#hashCode()()` |
| `open https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/PipelineResult#toString()()` |

| ### Public properties |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/Timestamp?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/PipelineResult#createTime()` The time the document was created. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentReference?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/PipelineResult#ref()` The reference to the document, if the query returns the document id for a document. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/Timestamp?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/PipelineResult#updateTime()` The time the document was last updated (at the time the snapshot was generated). |

## Public functions

### equals

```
open operator fun equals(other: Any?): Boolean
```

### get

```
fun get(field: String): Any?
```

Retrieves the field specified by `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/PipelineResult#get(kotlin.String)`.

| Parameters |
|---|---|
| `field: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The field path (e.g. "foo" or "foo.bar") to a specific field. |

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?` | The data at the specified field location or null if no such field exists. |

### get

```
fun get(fieldPath: FieldPath): Any?
```

Retrieves the field specified by `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/PipelineResult#get(com.google.firebase.firestore.FieldPath)`.

| Parameters |
|---|---|
| `fieldPath: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FieldPath` | The field path to a specific field. |

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?` | The data at the specified field location or null if no such field exists. |

### getData

```
fun getData(): Map<String, Any?>
```

Retrieves all fields in the result as an object map.

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?>` | Map of field names to objects. |

### getId

```
fun getId(): String?
```

Returns the ID of the document represented by this result. Returns null if this result is not corresponding to a Firestore document.

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | ID of document, if applicable. |

### hashCode

```
open fun hashCode(): Int
```

### toString

```
open fun toString(): String
```

## Public properties

### createTime

```
val createTime: Timestamp?
```

The time the document was created. Null if this result is not a document.

### ref

```
val ref: DocumentReference?
```

The reference to the document, if the query returns the document id for a document. The name field will be returned by default if querying a document.

Document ids will not be returned if certain pipeline stages omit the document id. For example, `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline#select(com.google.firebase.firestore.pipeline.Selectable,kotlin.Array)`, `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline#removeFields(com.google.firebase.firestore.pipeline.Field,kotlin.Array)` and `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline#aggregate(com.google.firebase.firestore.pipeline.AliasedAggregate,kotlin.Array)` can omit the document id.

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentReference?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentReference` Reference to the document, if applicable. |

### updateTime

```
val updateTime: Timestamp?
```

The time the document was last updated (at the time the snapshot was generated). Null if this result is not a document.