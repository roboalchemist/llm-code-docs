# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/PipelineResult.md.txt

# PipelineResult

# PipelineResult


```
@Beta
public final class PipelineResult
```

<br />

*** ** * ** ***

Represents the results of a Pipeline query, including the data and metadata. It is usually accessed via `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/Pipeline.Snapshot`.

## Summary

| ### Public fields |
|---|---|
| `final https://firebase.google.com/docs/reference/android/com/google/firebase/Timestamp` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/PipelineResult#createTime()` The time the document was created. |
| `final https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentReference` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/PipelineResult#ref()` The reference to the document, if the query returns the document id for a document. |
| `final https://firebase.google.com/docs/reference/android/com/google/firebase/Timestamp` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/PipelineResult#updateTime()` The time the document was last updated (at the time the snapshot was generated). |

| ### Public methods |
|---|---|
| `boolean` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/PipelineResult#equals(kotlin.Any)(https://developer.android.com/reference/kotlin/java/lang/Object.html other)` |
| `final https://developer.android.com/reference/kotlin/java/lang/Object.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/PipelineResult#get(kotlin.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html field)` Retrieves the field specified by `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/PipelineResult#get(kotlin.String)`. |
| `final https://developer.android.com/reference/kotlin/java/lang/Object.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/PipelineResult#get(com.google.firebase.firestore.FieldPath)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FieldPath fieldPath)` Retrieves the field specified by `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/PipelineResult#get(com.google.firebase.firestore.FieldPath)`. |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/Map.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html, https://developer.android.com/reference/kotlin/java/lang/Object.html>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/PipelineResult#getData()()` Retrieves all fields in the result as an object map. |
| `final https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/PipelineResult#getId()()` Returns the ID of the document represented by this result. |
| `int` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/PipelineResult#hashCode()()` |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/PipelineResult#toString()()` |

## Public fields

### createTime

```
public final Timestamp createTime
```

The time the document was created. Null if this result is not a document.

### ref

```
public final DocumentReference ref
```

The reference to the document, if the query returns the document id for a document. The name field will be returned by default if querying a document.

Document ids will not be returned if certain pipeline stages omit the document id. For example, `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/Pipeline#select(com.google.firebase.firestore.pipeline.Selectable,kotlin.Array)`, `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/Pipeline#removeFields(com.google.firebase.firestore.pipeline.Field,kotlin.Array)` and `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/Pipeline#aggregate(com.google.firebase.firestore.pipeline.AliasedAggregate,kotlin.Array)` can omit the document id.

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentReference` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentReference` Reference to the document, if applicable. |

### updateTime

```
public final Timestamp updateTime
```

The time the document was last updated (at the time the snapshot was generated). Null if this result is not a document.

## Public methods

### equals

```
public boolean equals(Object other)
```

### get

```
public final Object get(@NonNull String field)
```

Retrieves the field specified by `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/PipelineResult#get(kotlin.String)`.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html field` | The field path (e.g. "foo" or "foo.bar") to a specific field. |

| Returns |
|---|---|
| `https://developer.android.com/reference/kotlin/java/lang/Object.html` | The data at the specified field location or null if no such field exists. |

### get

```
public final Object get(@NonNull FieldPath fieldPath)
```

Retrieves the field specified by `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/PipelineResult#get(com.google.firebase.firestore.FieldPath)`.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FieldPath fieldPath` | The field path to a specific field. |

| Returns |
|---|---|
| `https://developer.android.com/reference/kotlin/java/lang/Object.html` | The data at the specified field location or null if no such field exists. |

### getData

```
public final @NonNull Map<@NonNull String, Object> getData()
```

Retrieves all fields in the result as an object map.

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/Map.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html, https://developer.android.com/reference/kotlin/java/lang/Object.html>` | Map of field names to objects. |

### getId

```
public final String getId()
```

Returns the ID of the document represented by this result. Returns null if this result is not corresponding to a Firestore document.

| Returns |
|---|---|
| `https://developer.android.com/reference/kotlin/java/lang/String.html` | ID of document, if applicable. |

### hashCode

```
public int hashCode()
```

### toString

```
public @NonNull String toString()
```